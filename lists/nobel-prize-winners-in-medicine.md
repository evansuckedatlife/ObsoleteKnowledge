---
type: list
category: science
read: false
---

# Nobel Prize winners in physiology or medicine

The Nobel Prize winners in physiology or medicine most worth knowing for quiz bowl.

## nodes

- [[alexander-fleming|Alexander Fleming]] — Scottish bacteriologist who discovered penicillin in 1928 through the chance observation of a contaminating mould that…
- [[barbara-mcclintock|Barbara McClintock]] — American geneticist who discovered transposable elements (jumping genes) in maize—segments of DNA that move within the genome…
- [[ivan-pavlov|Ivan Pavlov]] — Ivan Pavlov (1849–1936) was a Russian physiologist whose accidental discovery of classical conditioning launched the…
- [[james-watson-and-francis-crick|James Watson and Francis Crick]] — American biologist James Watson and British physicist Francis Crick solved the three-dimensional structure of DNA in 1953,…
- [[karl-landsteiner|Karl Landsteiner]] — Austrian-American pathologist and immunologist who discovered the human ABO blood groups and later the Rh factor, transforming…
- [[paul-ehrlich|Paul Ehrlich]] — German physician and biochemist who pioneered chemotherapy—the use of synthetic chemicals to treat disease.
- [[robert-koch|Robert Koch]] — German physician and microbiologist who identified the bacterium Mycobacterium tuberculosis as the causative agent of…
- [[ronald-ross|Ronald Ross]] — British physician and parasitologist who identified the Plasmodium parasite as the causative agent of malaria and demonstrated…
- [[thomas-hunt-morgan|Thomas Hunt Morgan]] — American biologist and embryologist who founded experimental genetics through his work with Drosophila melanogaster (fruit flies).
- [[willem-einthoven|Willem Einthoven]] — Dutch physiologist who invented the string galvanometer and, through it, founded electrocardiography.

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
      - property: tour_order
        direction: ASC
      - property: file.name
        direction: ASC
```
