---
type: list
category: literature
read: false
---

# authors of speculative fiction

The authors of speculative fiction most worth knowing for quiz bowl.

## nodes

- [[aldous-huxley|Aldous Huxley]] — Aldous Huxley was an English author and essayist whose Brave New World stands as one of the canonical dystopian visions of…
- [[douglas-adams|Douglas Adams]] — Douglas Adams was a British author and humorist whose The Hitchhiker's Guide to the Galaxy defined comedic science fiction for…
- [[george-orwell|George Orwell]] — George Orwell, pen name of Eric Arthur Blair, was an English author and political essayist whose dystopian novels warned…
- [[h-g-wells|H.G. Wells]] — Herbert George Wells was an English author whose scientific romances defined the trajectory of science fiction in the late…
- [[isaac-asimov|Isaac Asimov]] — Isaac Asimov was an American biochemist and prolific science fiction author whose works defined the genre's technical and…
- [[jules-verne|Jules Verne]] — Jules Verne was a French author who pioneered the scientific romance and is widely regarded as a father of science fiction.
- [[kurt-vonnegut|Kurt Vonnegut]] — Kurt Vonnegut was an American novelist and social critic whose darkly comic, science-inflected narratives interrogated war,…
- [[margaret-atwood|Margaret Atwood]] — Margaret Atwood is a Canadian author whose speculative works—particularly The Handmaid's Tale—articulate feminist anxieties…
- [[mary-shelley|Mary Shelley]] — Mary Shelley was an English author and the author of Frankenstein, often considered the first science fiction novel.
- [[ray-bradbury|Ray Bradbury]] — Ray Bradbury was an American science fiction author celebrated for the lyrical beauty and emotional depth of his speculative…

## progress

Live read-status for this list (requires the **Bases** core plugin). Flip a node's `read` from its footer toggle and it moves here.

```base
filters:
  and:
    - file.hasLink(this.file)
views:
  - type: table
    name: Progress
    order:
      - file.name
      - read
      - type
    sort:
      - property: read
        direction: ASC
      - property: file.name
        direction: ASC
```
