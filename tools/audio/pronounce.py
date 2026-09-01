#!/usr/bin/env python3
"""Respell names espeak-ng gets wrong, applied at synthesis time only.

Kokoro speaks whatever espeak's phonemizer produces, and espeak mishandles a
lot of classical names: `Heracles` comes out "HER-uh-kulz" instead of
"-kleez", `Diomedes` collapses to "dy-OHMDZ", `Antigone` becomes "anti-GONE",
`Mjolnir` is read with M as a letter name.

The fix is a respelling table applied to the narration text just before
synthesis. Deliberately NOT baked into the narration cache: the cache is the
expensive artefact, the respellings are cheap and will keep being tuned, and
the cached text stays readable prose rather than phonetic mush.

Every entry is verified against the phonemizer by `--check`, which prints the
phonemes for the raw name and the respelling side by side so a regression is
visible without listening to anything.

Usage:
    python tools/audio/pronounce.py --check          # verify the table
    python tools/audio/pronounce.py --say "text"     # show what gets spoken
"""

from __future__ import annotations

import re

# name -> respelling espeak pronounces correctly.
# Keep keys capitalised as they appear in prose; matching is case-insensitive
# and whole-word, and possessives are handled by the caller.
RESPELL = {
    # Greek — the ones that were audibly wrong
    "Heracles": "Herra-kleez",
    "Diomedes": "Dye-oh-mee-deez",
    "Agamemnon": "Ag-a-memnon",
    "Clytemnestra": "Klye-tem-nestra",
    "Antigone": "An-tig-oh-nee",
    "Eurydice": "You-rid-iss-ee",
    "Semele": "Sem-uh-lee",
    "Hesperides": "Hess-perr-uh-deez",
    "Colchis": "Kol-kiss",
    "Briseis": "Bry-see-iss",
    "Philoctetes": "Fill-ock-tee-teez",
    "Neoptolemus": "Nee-op-tol-em-uss",
    "Hippomenes": "Hip-om-en-eez",
    "Dionysus": "Dye-oh-nye-sus",
    "Geryon": "Gerry-on",
    "Alcmene": "Alk-mee-nee",
    "Medea": "Muh-dee-uh",
    "Laocoon": "Lay-ock-oh-on",
    "Danae": "Dan-a-ee",
    "Danaë": "Dan-a-ee",
    "Ariadne": "Arr-ee-ad-nee",
    "Iolaus": "Eye-oh-lay-us",
    "Deianira": "Day-a-nye-ra",
    "Peleus": "Pee-lee-us",
    "Nereid": "Neer-ee-ud",
    "Pasiphae": "Pa-sif-a-ee",
    "Idomeneus": "Eye-dom-en-yooss",
    "Sarpedon": "Sar-pee-don",
    "Deiphobus": "Dee-if-oh-bus",
    "Astyanax": "As-tye-a-nax",
    "Andromache": "An-drom-a-kee",
    "Polyxena": "Pol-lix-en-uh",
    "Penthesilea": "Pen-thess-il-ee-a",
    "Chryseis": "Kry-see-iss",
    "Telemachus": "Tel-em-a-kus",
    "Menoetius": "Men-ee-shuss",

    # Norse
    "Mjolnir": "Myawl-neer",
    "Jotunheim": "Yo-tun-hime",
    "Yggdrasil": "Ig-dra-sil",
    "Freyja": "Fray-ya",
    "Ragnarok": "Rag-na-rok",
    "Idunn": "Ee-dun",
    "Jormungandr": "Yor-mun-gand-er",
    "Fenrir": "Fen-reer",
    "Niflheim": "Niff-el-hime",

    # Arthurian
    "Iseult": "Ih-soolt",
    "Bedivere": "Bed-uh-veer",
    "Uther": "Oo-ther",
    "Igraine": "Ee-grain",

    # Egyptian
    "Anubis": "Uh-noo-bis",
    "Nephthys": "Nef-thiss",
    "Sekhmet": "Sek-met",
    "Amun": "Ah-mun",
    "Atum": "Ah-tum",
    "Khepri": "Kep-ree",
    "Sobek": "So-bek",
    "Taweret": "Ta-weh-ret",

    # Hindu
    "Draupadi": "Drow-pa-dee",
    "Yudhishthira": "Yoo-dish-tira",
    "Ashwatthama": "Ash-wat-ama",
    "Vibhishana": "Vib-ee-sha-na",
    "Sugriva": "Soo-gree-va",
    "Jatayu": "Ja-ta-yoo",
    "Kaikeyi": "Kye-kay-ee",
    "Parashurama": "Pa-ra-shu-rama",
}

_PATTERN = re.compile(
    r"\b(" + "|".join(sorted((re.escape(k) for k in RESPELL), key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)

_BY_LOWER = {k.lower(): v for k, v in RESPELL.items()}


def apply(text: str) -> str:
    """Swap known-mispronounced names for respellings espeak gets right."""
    return _PATTERN.sub(lambda m: _BY_LOWER[m.group(1).lower()], text)


def _check() -> None:
    from kokoro_onnx.tokenizer import Tokenizer

    tok = Tokenizer()
    print("%-16s %-24s %-28s %s" % ("NAME", "RESPELLING", "WAS", "NOW"))
    for name, respell in RESPELL.items():
        was = tok.phonemize(name, lang="en-us")
        now = tok.phonemize(respell, lang="en-us")
        flag = "" if was != now else "   <-- NO CHANGE"
        print("%-16s %-24s %-28s %s%s" % (name, respell, was, now, flag))


if __name__ == "__main__":
    import argparse
    import sys

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--say")
    args = ap.parse_args()

    if args.say:
        sys.stdout.reconfigure(encoding="utf-8")
        print(apply(args.say))
    elif args.check:
        sys.stdout.reconfigure(encoding="utf-8")
        _check()
    else:
        ap.error("need --check or --say")
