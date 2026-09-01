#!/usr/bin/env python3
"""Synthesise an episode: narration scripts -> one mp3 + a chapter timeline.

One TTS render per node, so chapter offsets are exact sample counts rather
than a guess from a probe of the finished file. Segments are joined with a
short pause, normalised, and encoded to mono mp3 (speech does not need more
than ~56 kbps, and disk here is tight).

Runs under Kokoro's own virtualenv. If launched with an interpreter that
cannot import kokoro_onnx, it re-executes itself with the one the CLI
reports, so `python tools/audio/build.py ...` just works.

Usage:
    python tools/audio/build.py --episode greek-heroes
    python tools/audio/build.py --episode greek-heroes --voice bm_george
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = os.path.join(ROOT, "tools", "audio", "work")
CACHE = os.path.join(ROOT, "tools", "audio", ".cache", "narration")
CONFIG = os.path.expanduser("~/.config/save-to-spotify")

GAP_MS = 450          # between nodes
LEAD_MS = 250         # before the very first word
SENTENCE = re.compile(r"(?<=[.!?])\s+")


def cli() -> str:
    for cand in (
        shutil.which("save-to-spotify"),
        os.path.expanduser("~/AppData/Local/save-to-spotify/save-to-spotify.exe"),
    ):
        if cand and os.path.exists(cand):
            return cand
    sys.exit("save-to-spotify CLI not found")


def ensure_kokoro_interpreter() -> None:
    """Re-exec under the Kokoro venv if this interpreter lacks kokoro_onnx."""
    try:
        import kokoro_onnx  # noqa: F401
        return
    except ImportError:
        pass

    out = subprocess.run([cli(), "--json", "tts", "status"],
                         capture_output=True, text=True).stdout
    py = ""
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("{"):
            py = (json.loads(line) or {}).get("kokoro_python", "")
    # tts status can report the *system* python before setup has run; prefer
    # the venv interpreter that `tts setup` actually creates.
    venv = os.path.join(CONFIG, "kokoro-env", "Scripts", "python.exe")
    if not os.path.exists(venv):
        venv = os.path.join(CONFIG, "kokoro-env", "bin", "python3")
    if os.path.exists(venv):
        py = venv
    if not py or not os.path.exists(py):
        sys.exit("Kokoro not installed. Run: save-to-spotify tts setup")
    if os.path.abspath(py) == os.path.abspath(sys.executable):
        sys.exit("kokoro_onnx missing from the Kokoro venv; re-run tts setup")
    os.execv(py, [py, os.path.abspath(__file__), *sys.argv[1:]])


def find_model(pattern: str) -> str:
    for d in (os.path.join(CONFIG, "kokoro-env"), CONFIG):
        hits = glob.glob(os.path.join(d, pattern))
        if hits:
            return sorted(hits)[-1]
    sys.exit(f"no {pattern} found — run: save-to-spotify tts setup")


def patch_kokoro_speed_dtype() -> None:
    """Work around a dtype bug in kokoro-onnx 0.4.7.

    On the newer `input_ids` model export the library sends `speed` as
    int32, but kokoro-v1.0.onnx declares it `tensor(float)[1]`, so every
    synthesis call dies with:

        INVALID_ARGUMENT: Unexpected input data type.
        Actual: (tensor(int32)), expected: (tensor(float))

    The older code path in the same function gets it right, so this is a
    plain bug rather than a model mismatch. Patch it in memory instead of
    editing site-packages, since the venv is managed by `save-to-spotify
    tts setup` and would be overwritten by the next update.
    """
    import numpy as np
    import kokoro_onnx
    from kokoro_onnx import Kokoro

    def _create_audio(self, phonemes, voice, speed):
        tokens = np.array(self.tokenizer.tokenize(phonemes), dtype=np.int64)
        assert len(tokens) <= kokoro_onnx.MAX_PHONEME_LENGTH
        style = voice[len(tokens)]
        inputs = {
            "input_ids": np.array([[0, *tokens, 0]], dtype=np.int64),
            "style": np.array(style, dtype=np.float32),
            "speed": np.array([speed], dtype=np.float32),
        }
        names = {i.name for i in self.sess.get_inputs()}
        if "input_ids" not in names:            # older export
            inputs = {
                "tokens": inputs["input_ids"],
                "style": inputs["style"],
                "speed": inputs["speed"],
            }
        audio = self.sess.run(None, inputs)[0]
        return audio, kokoro_onnx.SAMPLE_RATE

    Kokoro._create_audio = _create_audio


def chunks(text: str, limit: int = 480) -> list[str]:
    """Kokoro degrades on very long inputs; split on sentence boundaries."""
    out, cur = [], ""
    for sent in SENTENCE.split(text.strip()):
        if not sent:
            continue
        if len(cur) + len(sent) + 1 > limit and cur:
            out.append(cur.strip())
            cur = sent
        else:
            cur = f"{cur} {sent}".strip()
    if cur:
        out.append(cur)
    return out or [text]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--episode", required=True)
    ap.add_argument("--voice", default="af_heart")
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--bitrate", default="56k")
    args = ap.parse_args()

    ensure_kokoro_interpreter()

    import numpy as np
    import soundfile as sf
    from kokoro_onnx import Kokoro

    patch_kokoro_speed_dtype()

    epdir = os.path.join(WORK, args.episode)
    plan_path = os.path.join(epdir, "plan.json")
    if not os.path.exists(plan_path):
        sys.exit(f"no plan at {plan_path} — run bundle.py first")
    with open(plan_path, encoding="utf-8") as fh:
        plan = json.load(fh)

    scripts = []
    missing = []
    for node in plan["nodes"]:
        p = os.path.join(CACHE, node["cache_key"] + ".txt")
        if not os.path.exists(p):
            missing.append(node["slug"])
        else:
            with open(p, encoding="utf-8") as fh:
                scripts.append((node["title"], fh.read().strip()))
    if missing:
        sys.exit(f"{len(missing)} node(s) not yet narrated: {', '.join(missing[:8])}")

    # The intro is load-bearing, not decoration: the CLI requires at least two
    # chapters with the first at 0 and consecutive starts >= 5 s apart, so it
    # must contain a comfortable margin of real speech. Naming the topics gets
    # us well past that and orients the listener at the same time.
    names = [t for t, _ in scripts]
    intro = (
        f"{plan['title']}. A guided tour from the ObsoleteKnowledge collection. "
        f"This episode covers {len(scripts)} topics: "
        + ", ".join(names[:-1]) + (f", and {names[-1]}." if len(names) > 1 else ".")
        + " Each one begins a new chapter, so you can skip ahead to any of them."
    )
    segments = [("Introduction", intro)] + scripts

    kokoro = Kokoro(find_model("kokoro-v*.onnx"), find_model("voices-v*.bin"))

    audio, chapters, sr = [], [], None
    audio_ms = 0.0

    def push_silence(ms: float) -> None:
        nonlocal audio_ms
        audio.append(np.zeros(int(sr * ms / 1000.0), dtype=np.float32))
        audio_ms += ms

    for idx, (title, text) in enumerate(segments):
        pieces = []
        for chunk in chunks(text):
            samples, rate = kokoro.create(chunk, voice=args.voice,
                                          speed=args.speed, lang="en-us")
            sr = sr or rate
            pieces.append(np.asarray(samples, dtype=np.float32))
        if sr is None:
            sys.exit("Kokoro returned no audio")
        if idx == 0:
            push_silence(LEAD_MS)
        else:
            push_silence(GAP_MS)

        chapters.append({"title": title, "start_time_ms": int(round(audio_ms))})
        for piece in pieces:
            audio.append(piece)
            audio_ms += 1000.0 * len(piece) / sr
        print(f"  [{idx + 1:>3}/{len(segments)}] {title[:52]:<52} "
              f"{audio_ms / 1000:7.1f}s")

    joined = np.concatenate(audio)
    wav = os.path.join(epdir, "episode.wav")
    sf.write(wav, joined, sr)

    mp3 = os.path.join(epdir, "episode.mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-i", wav,
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
         "-ac", "1", "-ar", "24000", "-b:a", args.bitrate, mp3],
        check=True,
    )
    os.remove(wav)

    # Validate the timeline before it is ever uploaded. Neither the CLI nor the
    # backend checks these, and a bad timeline silently produces an episode
    # whose chapters do not line up with what you hear.
    duration_ms = int(round(audio_ms))
    problems = []
    if len(chapters) < 2:
        problems.append(f"need >=2 chapters, have {len(chapters)}")
    if chapters and chapters[0]["start_time_ms"] != 0:
        problems.append(f"first chapter starts at {chapters[0]['start_time_ms']}, must be 0")
    for a, b in zip(chapters, chapters[1:]):
        gap = b["start_time_ms"] - a["start_time_ms"]
        if gap < 5000:
            problems.append(f"'{a['title']}' -> '{b['title']}' only {gap} ms apart (min 5000)")
    if chapters and chapters[-1]["start_time_ms"] >= duration_ms:
        problems.append(f"last chapter at {chapters[-1]['start_time_ms']} >= duration {duration_ms}")
    if problems:
        sys.exit("timeline invalid:\n  " + "\n  ".join(problems))

    with open(os.path.join(epdir, "timeline.json"), "w", encoding="utf-8", newline="\r\n") as fh:
        json.dump({"items": [{"chapter": c} for c in chapters]}, fh, indent=2)

    # Covers are mandatory on every episode; generate now so publish can't
    # reach the upload call without one.
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from covers import make_cover
    make_cover(plan["title"], os.path.join(epdir, "cover.jpg"), key=plan["episode_id"])

    size = os.path.getsize(mp3)
    print(f"\n{args.episode}: {len(chapters)} chapters, "
          f"{audio_ms / 60000:.1f} min, {size / 1e6:.1f} MB -> {mp3}")


if __name__ == "__main__":
    main()
