#!/usr/bin/env python3
"""Cover art for shows and episodes.

Every show and every episode MUST ship a cover; `upload` and `shows create`
are never called without `--image`. There is no image-generation API key on
this machine, so this is the skill's terminal fallback: pre-designed CDN base
artwork chosen by a hash of the title, with Pillow typography composited on
top. Deterministic, offline after first fetch, and visually coherent across a
shelf of fifteen shows.

Typography follows the skill spec exactly: Montserrat Bold, white only, no
effects, bottom-left, at most three balanced lines.
"""

from __future__ import annotations

import hashlib
import os
import unicodedata
import urllib.request

from PIL import Image, ImageDraw, ImageFont

CANVAS = 1400
MARGIN = 64
MAX_TEXT_WIDTH = int((CANVAS - 2 * MARGIN) * 0.85)
MAX_TEXT_HEIGHT = CANVAS - MARGIN - CANVAS // 2
MIN_FONT_SIZE = 100
MAX_FONT_SIZE = 400
LEADING_FACTOR = 0.97

CDN = "https://save-to-spotify.spotifycdn.com/assets/uts-{:02d}.png"
CACHE = os.path.join(os.path.expanduser("~"), ".cache", "save-to-spotify")
FONT_CACHE = os.path.join(CACHE, "fonts")
ART_CACHE = os.path.join(CACHE, "art")

FONTS = {
    "latin": ("Montserrat-Bold.ttf",
              "https://raw.githubusercontent.com/JulietaUla/Montserrat/master/fonts/ttf/Montserrat-Bold.ttf"),
    "arabic": ("Tajawal-Bold.ttf",
               "https://raw.githubusercontent.com/google/fonts/main/ofl/tajawal/Tajawal-Bold.ttf"),
    "hebrew": ("NotoSansHebrew-Bold.ttf",
               "https://raw.githubusercontent.com/google/fonts/main/ofl/notosanshebrew/NotoSansHebrew-Bold.ttf"),
}


def detect_script(title: str) -> str:
    for ch in title:
        if unicodedata.bidirectional(ch) in ("R", "AL", "AN"):
            if "֐" <= ch <= "׿":
                return "hebrew"
            return "arabic"
    return "latin"


def load_font(size: int, title: str = "") -> ImageFont.FreeTypeFont:
    os.makedirs(FONT_CACHE, exist_ok=True)
    fname, url = FONTS[detect_script(title)]
    path = os.path.join(FONT_CACHE, fname)
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
    return ImageFont.truetype(path, size)


def measure(font, text: str) -> tuple[int, int]:
    if not text:
        return (0, 0)
    b = font.getbbox(text)
    return b[2] - b[0], b[3] - b[1]


def _split_combos(words, n):
    if n == 1:
        yield [words]
        return
    for i in range(1, len(words) - n + 2):
        for rest in _split_combos(words[i:], n - 1):
            yield [words[:i]] + rest


def break_lines(title: str, font) -> list[str]:
    """Most balanced 1-3 line split that fits; keeps concepts together."""
    words = title.split()
    if not words:
        return [title]
    best, best_d = None, float("inf")
    for n in range(1, min(len(words), 3) + 1):
        for combo in _split_combos(words, n):
            lines = [" ".join(p) for p in combo if p]
            if not lines:
                continue
            widths = [measure(font, l)[0] for l in lines]
            if max(widths) > MAX_TEXT_WIDTH:
                continue
            d = max(widths) - min(widths)
            if d < best_d:
                best_d, best = d, lines
    return best or [title]


def fit_title(title: str):
    if not title:
        title = "Untitled"
    for size in range(MAX_FONT_SIZE, MIN_FONT_SIZE - 1, -2):
        font = load_font(size, title)
        lines = break_lines(title, font)
        if len(lines) > 3:
            continue
        if max(measure(font, l)[0] for l in lines) > MAX_TEXT_WIDTH:
            continue
        lh = int(size * LEADING_FACTOR)
        total = lh * (len(lines) - 1) + font.getbbox(lines[-1])[3]
        if total > MAX_TEXT_HEIGHT:
            continue
        return font, lines, size
    font = load_font(MIN_FONT_SIZE, title)
    return font, break_lines(title, font), MIN_FONT_SIZE


def base_art(key: str) -> Image.Image:
    """CDN base artwork, chosen deterministically by title hash."""
    os.makedirs(ART_CACHE, exist_ok=True)
    variant = int(hashlib.sha256(key.encode("utf-8")).hexdigest(), 16) % 20 + 1
    path = os.path.join(ART_CACHE, f"uts-{variant:02d}.png")
    if not os.path.exists(path):
        urllib.request.urlretrieve(CDN.format(variant), path)
    return Image.open(path).convert("RGB").resize((CANVAS, CANVAS), Image.LANCZOS)


def shorten(title: str) -> str:
    """Covers carry one short label; the full title lives in the metadata."""
    label = title.split(" — ")[0].strip()
    for article in ("The ", "A "):
        if label.startswith(article):
            label = label[len(article):]
    return label or title


def make_cover(title: str, out_path: str, key: str | None = None) -> str:
    img = base_art(key or title)
    label = shorten(title)
    font, lines, size = fit_title(label)

    draw = ImageDraw.Draw(img)
    lh = int(size * LEADING_FACTOR)
    total = lh * (len(lines) - 1) + font.getbbox(lines[-1])[3]
    y = max(CANVAS - MARGIN - total, CANVAS // 2)
    rtl = detect_script(label) != "latin"
    for line in lines:
        x = CANVAS - MARGIN - measure(font, line)[0] if rtl else MARGIN
        draw.text((x, y), line, font=font, fill=(255, 255, 255))
        y += lh

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    quality = 90
    while True:
        img.save(out_path, "JPEG", quality=quality, optimize=True)
        if os.path.getsize(out_path) <= 1_000_000 or quality <= 60:
            break
        quality -= 10
    return out_path


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    p = make_cover(args.title, args.out)
    print(f"{p}  {os.path.getsize(p) / 1000:.0f} KB")
