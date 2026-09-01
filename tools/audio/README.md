# tools/audio — vault tours as private Spotify audiobooks

Turns a guided tour into a chaptered episode in your own Spotify library, using
[Save to Spotify](https://github.com/spotify/save-to-spotify). Episodes are
**private** — visible only to your account — and sync to every device you are
signed in on, including iPhone. There is nothing to install or configure on the
phone.

**Mapping:** one Spotify *show* per vault category · one *episode* per tour
(split into parts above 18 nodes) · one *chapter* per node.

## One-time setup

```bash
curl -fsSL https://saveto.spotify.com/install.sh | bash   # Git Bash on Windows
save-to-spotify auth login                                # browser OAuth
save-to-spotify tts setup                                 # Kokoro, ~340 MB
winget install Gyan.FFmpeg                                # concat + loudnorm
save-to-spotify --json tts status                         # confirm all ready
```

`auth login` waits five minutes for you to approve in the browser, and the
browser must be signed into the **same** Spotify account as your phone.

## Running

```bash
python tools/audio/bundle.py --tour greek-heroes     # resolve + plan
#   ... narrate any uncached nodes (see below) ...
python tools/audio/build.py  --episode greek-heroes  # TTS + assemble + chapters
python tools/audio/publish.py --episode greek-heroes # upload to Spotify
```

`bundle.py --list-tours` shows every tour with its node count.
`bundle.py --category mythology` plans a whole category at once.

## The narration step

Nodes are written to be *read*: bullets, wikilinks, YAML, Dataview blocks.
`bundle.py` strips the markup mechanically, but the result still reads like a
list being recited. So each node is rewritten into flowing spoken prose by a
Haiku pass before synthesis.

That step needs a model, so it runs as a subagent rather than inside these
scripts (there is no API key on this machine). `bundle.py` reports how many
nodes still need narrating; point an agent at the plan and have it write
`tools/audio/.cache/narration/<cache_key>.txt` for each.

The cache key is a hash of the node's own text, so:

- re-running an unchanged tour costs nothing,
- editing one node re-narrates that node only,
- a node shared between two tours is narrated once.

The rewrite is constrained to facts already in the node. It is a rewrite, not
research.

## Why these choices

**Chapters are computed from sample counts, not probed from the mp3.** Each node
is synthesised separately and the offsets accumulate exactly, so chapter marks
cannot drift.

**The intro chapter is load-bearing.** The CLI requires at least two chapters,
the first at `0 ms`, with consecutive starts at least 5 s apart. A spoken intro
listing the topics satisfies all three and orients the listener. `build.py`
asserts every rule before writing `timeline.json`, because neither the CLI nor
the backend validates them — a bad timeline just silently misaligns.

**Covers are mandatory** on every show and every episode. With no image API
available, `covers.py` uses the sanctioned fallback: Spotify's CDN base artwork
selected by a hash of the title, with Montserrat Bold typography composited by
Pillow. Deterministic, and coherent across a shelf of shows.

**Audio is disposable.** Mono 56 kbps is plenty for speech. The local mp3 is
deleted after a confirmed upload — it lives in Spotify now — unless you pass
`--keep-audio`. Only the narration text is kept, because that is the expensive
artifact. This matters: the machine has under 9 GB free.

**`--json` goes before the subcommand** (`save-to-spotify --json upload …`).
The other order silently does something else.

## Resume

`state.json` records show ids, episode ids, and the node hashes behind each
episode. Re-running skips anything already published, so a rate limit or a
crash costs only the time already spent. Spotify enforces per-account save
limits, so publishing many episodes is a multi-session job by design.

Note that show and episode metadata is **immutable after creation** — changing
a title means deleting and re-uploading. `publish.py` therefore never rewrites
a published episode on its own.

## On the phone

Spotify → **Your Library** → **Podcasts & Shows** → the category show. Chapters
appear in the Now Playing view roughly a minute after the episode goes READY.
Download for offline.

## Rate limits

Spotify caps uploads per account. Hitting it is normal for a big batch and
costs nothing: rendering is the expensive step and the audio stays on disk.

```bash
python tools/audio/publish.py --status     # what is published vs pending
python tools/audio/publish.py --pending    # drain the backlog when the cap resets
```

`--pending` stops cleanly on the next 429 and tells you how many remain. The
CLI reports a rate limit inconsistently (sometimes exit 0 with an error payload
on stdout), so publish.py matches on the message text, not the exit code.
