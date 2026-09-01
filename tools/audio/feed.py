#!/usr/bin/env python3
"""Build a public podcast RSS feed from the episodes already rendered locally.

The private Spotify library and the public podcast are two separate things:
Save to Spotify Personal Podcasts cannot be shared, so going public means
hosting the same mp3s behind an RSS feed and submitting that feed to Spotify
for Creators. This assembles the publishable directory.

Output layout (everything Pages needs, nothing else):

    <out>/
      feed.xml
      cover.jpg
      episodes/<slug>.mp3
      chapters/<slug>.json      # podcast:chapters, honoured by Overcast etc.

Usage:
    python tools/audio/feed.py --out ../buzzer \\
        --base-url https://evansuckedatlife.github.io/buzzer \\
        --email you@example.com
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
from email.utils import formatdate
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
WORK = os.path.join(HERE, "work")
STATE = os.path.join(HERE, "state.json")

TITLE = "Buzzer"
SUBTITLE = "Guided tours through a quiz-bowl knowledge base"
DESCRIPTION = (
    "Short, chaptered tours through a personal reference collection: mythology, "
    "history, literature, science and more. Each episode walks one topic, one "
    "chapter per entry, ordered so the most recognisable facts come first. "
    "Written from open sources and narrated with a synthetic voice."
)
AUTHOR = "Buzzer"
CATEGORY = "Education"
SUBCATEGORY = "Courses"


def ffprobe_seconds(path: str) -> int:
    ff = shutil.which("ffprobe") or os.path.expanduser(
        "~/AppData/Local/Microsoft/WinGet/Packages/"
        "Gyan.FFmpeg.Essentials_Microsoft.Winget.Source_8wekyb3d8bbwe/"
        "ffmpeg-8.1.1-essentials_build/bin/ffprobe.exe"
    )
    out = subprocess.run(
        [ff, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        capture_output=True, text=True,
    ).stdout.strip()
    try:
        return int(float(out))
    except ValueError:
        return 0


def hms(seconds: int) -> str:
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, help="directory to write the publishable site into")
    ap.add_argument("--base-url", required=True,
                    help="public URL the directory will be served from, no trailing slash")
    ap.add_argument("--email", required=True,
                    help="owner email. Spotify for Creators sends the ownership "
                         "verification code here, and it IS published in the feed, "
                         "so use an address you are willing to make public.")
    ap.add_argument("--title", default=TITLE)
    ap.add_argument("--author", default=AUTHOR)
    ap.add_argument("--explicit", default="false", choices=["true", "false"])
    args = ap.parse_args()

    base = args.base_url.rstrip("/")
    out = os.path.abspath(args.out)
    os.makedirs(os.path.join(out, "episodes"), exist_ok=True)
    os.makedirs(os.path.join(out, "chapters"), exist_ok=True)

    if not os.path.exists(STATE):
        sys.exit("no state.json — publish at least one episode first")
    with open(STATE, encoding="utf-8") as fh:
        state = json.load(fh)

    items = []
    missing = []
    for slug in sorted(state.get("episodes", {})):
        epdir = os.path.join(WORK, slug)
        mp3 = os.path.join(epdir, "episode.mp3")
        plan_path = os.path.join(epdir, "plan.json")
        if not (os.path.exists(mp3) and os.path.exists(plan_path)):
            missing.append(slug)
            continue
        with open(plan_path, encoding="utf-8") as fh:
            plan = json.load(fh)

        shutil.copyfile(mp3, os.path.join(out, "episodes", f"{slug}.mp3"))
        tl = os.path.join(epdir, "timeline.json")
        chapters_url = ""
        if os.path.exists(tl):
            with open(tl, encoding="utf-8") as fh:
                chaps = [i["chapter"] for i in json.load(fh)["items"] if "chapter" in i]
            payload = {
                "version": "1.2.0",
                "chapters": [
                    {"startTime": c["start_time_ms"] / 1000.0, "title": c["title"]}
                    for c in chaps
                ],
            }
            with open(os.path.join(out, "chapters", f"{slug}.json"), "w",
                      encoding="utf-8") as fh:
                json.dump(payload, fh, indent=2)
            chapters_url = f"{base}/chapters/{slug}.json"

        size = os.path.getsize(mp3)
        secs = ffprobe_seconds(mp3)
        titles = [n["title"] for n in plan["nodes"]]
        desc = (f"{len(titles)} topics, one per chapter: " + ", ".join(titles) + ".")
        items.append({
            "slug": slug,
            "title": plan["title"],
            "desc": desc,
            "size": size,
            "secs": secs,
            "mtime": os.path.getmtime(mp3),
            "chapters_url": chapters_url,
            "category": plan["category"],
        })

    if not items:
        sys.exit("no rendered episodes found — run build.py (episodes are deleted "
                 "after upload unless you pass --keep-audio)")

    items.sort(key=lambda i: i["mtime"])

    cover_src = os.path.join(WORK, "_covers", "show-mythology.jpg")
    if not os.path.exists(cover_src):
        sys.path.insert(0, HERE)
        from covers import make_cover
        cover_src = make_cover(args.title, os.path.join(WORK, "_covers", "podcast.jpg"),
                               key="podcast:obsoleteknowledge")
    shutil.copyfile(cover_src, os.path.join(out, "cover.jpg"))

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0"',
        '     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"',
        '     xmlns:content="http://purl.org/rss/1.0/modules/content/"',
        '     xmlns:podcast="https://podcastindex.org/namespace/1.0">',
        "  <channel>",
        f"    <title>{escape(args.title)}</title>",
        f"    <link>{escape(base)}</link>",
        f"    <language>en-us</language>",
        f"    <description>{escape(DESCRIPTION)}</description>",
        f"    <itunes:subtitle>{escape(SUBTITLE)}</itunes:subtitle>",
        f"    <itunes:summary>{escape(DESCRIPTION)}</itunes:summary>",
        f"    <itunes:author>{escape(args.author)}</itunes:author>",
        f"    <itunes:explicit>{args.explicit}</itunes:explicit>",
        f"    <itunes:type>episodic</itunes:type>",
        f'    <itunes:image href="{escape(base)}/cover.jpg"/>',
        f'    <itunes:category text="{CATEGORY}">',
        f'      <itunes:category text="{SUBCATEGORY}"/>',
        f"    </itunes:category>",
        "    <itunes:owner>",
        f"      <itunes:name>{escape(args.author)}</itunes:name>",
        f"      <itunes:email>{escape(args.email)}</itunes:email>",
        "    </itunes:owner>",
        f"    <lastBuildDate>{formatdate(items[-1]['mtime'], usegmt=True)}</lastBuildDate>",
    ]

    for it in items:
        url = f"{base}/episodes/{it['slug']}.mp3"
        parts += [
            "    <item>",
            f"      <title>{escape(it['title'])}</title>",
            f"      <description>{escape(it['desc'])}</description>",
            f"      <itunes:summary>{escape(it['desc'])}</itunes:summary>",
            f'      <enclosure url="{escape(url)}" length="{it["size"]}" type="audio/mpeg"/>',
            f'      <guid isPermaLink="false">obsoleteknowledge-{escape(it["slug"])}</guid>',
            f"      <pubDate>{formatdate(it['mtime'], usegmt=True)}</pubDate>",
            f"      <itunes:duration>{hms(it['secs'])}</itunes:duration>",
            f"      <itunes:explicit>{args.explicit}</itunes:explicit>",
        ]
        if it["chapters_url"]:
            parts.append(
                f'      <podcast:chapters url="{escape(it["chapters_url"])}" type="application/json+chapters"/>'
            )
        parts.append("    </item>")

    parts += ["  </channel>", "</rss>", ""]

    feed_path = os.path.join(out, "feed.xml")
    with open(feed_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(parts))

    total = sum(i["secs"] for i in items)
    print(f"wrote {feed_path}")
    print(f"  {len(items)} episodes, {total / 3600:.1f} h, "
          f"{sum(i['size'] for i in items) / 1e6:.0f} MB")
    print(f"  feed URL will be {base}/feed.xml")
    if missing:
        print(f"  SKIPPED {len(missing)} published episode(s) with no local mp3 "
              f"(rebuild with --keep-audio): {', '.join(missing)}")


if __name__ == "__main__":
    main()
