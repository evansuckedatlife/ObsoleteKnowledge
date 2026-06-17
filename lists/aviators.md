---
type: list
category: history
read: false
---

# aviators

The aviators most worth knowing for quiz bowl.

## nodes

- [[amelia-earhart|Amelia Earhart]] — Amelia Earhart set numerous women's aviation records in the 1920s and 1930s, became the first woman to fly solo across the…
- [[bessie-coleman|Bessie Coleman]] — Bessie Coleman became the first Black aviator and the first Black woman to hold a pilot's license, obtaining her license in 1921.
- [[burt-rutan|Burt Rutan]] — Burt Rutan is an American aircraft designer and engineer who pioneered composite aircraft construction and designed innovative…
- [[charles-lindbergh|Charles Lindbergh]] — Charles Lindbergh made the first solo nonstop transatlantic flight on May 20–21, 1927, piloting the Spirit of St.
- [[chuck-yeager|Chuck Yeager]] — Chuck Yeager became the first pilot to break the sound barrier, flying the Bell X-1 aircraft on October 14, 1947, at Mach 1.07…
- [[eddie-rickenbacker|Eddie Rickenbacker]] — Eddie Rickenbacker was the United States' top fighter ace in World War I with 26 confirmed aerial victories, a record…
- [[glenn-curtiss|Glenn Curtiss]] — Glenn Curtiss was an aviation pioneer and aircraft manufacturer who competed with the Wright Brothers for aviation supremacy…
- [[howard-hughes|Howard Hughes]] — Howard Hughes was an aviation pioneer, industrialist, and filmmaker who set multiple world speed records in the 1930s,…
- [[jimmy-doolittle|Jimmy Doolittle]] — Jimmy Doolittle was a pioneering aviator and military officer who made innovations in instrument flight, set numerous speed…
- [[red-baron|Red Baron]] — Manfred von Richthofen, known as the Red Baron, was a German fighter pilot in World War I who became aviation's most famous…
- [[wiley-post|Wiley Post]] — Wiley Post was a pioneering aviator of the 1930s who set multiple speed and distance records, designed the first practical…
- [[wright-brothers|Wright Brothers]] — Orville and Wilbur Wright, American bicycle mechanics, achieved the first powered, controlled, heavier-than-air flight on…

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
