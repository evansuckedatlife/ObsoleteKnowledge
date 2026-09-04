---
type: concept
category: misc
defines: [HTTP, Hypertext Transfer Protocol]
related: ["[[http-451-status-code]]", "[[ibm]]", "[[united-kingdom]]", "[[france]]", "[[cold-war]]", "[[space-age]]", "[[linguistics]]"]
requires: ["[[united-kingdom]]", "[[france]]"]
lists: ["[[misc-hubs]]"]
tour_order: 0
read: false
---

# HTTP

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

**HTTP**, standing for the **Hypertext Transfer Protocol**, is an application-layer network protocol initiated by British computer scientist *Tim Berners-Lee* at *CERN* in 1989. Operating as a stateless client-server request-response protocol traditionally layered over *Transmission Control Protocol* (*TCP*), it provides the standardized framework by which distributed hypermedia resources are addressed, transmitted, and rendered across the global internet. The protocol forms the universal architectural bedrock of the modern World Wide Web, transforming global telecommunications, scholarly data exchange, and modern digital commerce.

## you gotta know

- Conceived in 1989 by *Tim Berners-Lee* at the *CERN* laboratory situated along the border of *Switzerland* and [[france]], alongside *HTML*, *URIs*, and the first web server daemon.
- Governed by an extensible set of request methods or verbs, most notably *GET* for retrieving resources, *POST* for submitting enclosed entities, *PUT* for replacing targets, *DELETE* for stripping resources, and *HEAD* for fetching metadata headers alone.
- Relies on structured three-digit numeric response codes grouped by category: 1xx for informational notices, 2xx for successful actions such as *200 OK*, 3xx for redirections, 4xx for client errors such as *404 Not Found* or the censorship-indicating [[http-451-status-code]], and 5xx for internal server failures.
- Standardized historically through influential *IETF* specifications, progressing from the simplistic, one-line exchange model of *HTTP/0.9* to the header-rich *HTTP/1.0* (*RFC 1945*) and persistent connection pipelining in *HTTP/1.1* (*RFC 2068* and *RFC 2616*).
- Secured via transport layer encryption to create *HTTPS*, which utilizes *TLS* or *SSL* over port 443 to safeguard communications against eavesdropping, spoofing, and man-in-the-middle tampering.
- Major corporate technology developers, including network pioneers at [[ibm]], developed foundational web server hardware, enterprise middleware, and web-scale computing infrastructures that accelerated commercial adoption of the protocol during the late twentieth century.
- Evolved into binary framing protocols with *HTTP/2*, published in 2015 based on Google's *SPDY* research, which introduced multiplexed streams over a single connection, header compression via *HPACK*, and server push capabilities.
- Modernized with *HTTP/3*, which shifts the underlying transport layer from *TCP* to *QUIC*, an *IETF* protocol running over *UDP* to eliminate head-of-line blocking and streamline mobile handoffs.

## connections

- [[http-451-status-code]] — an official extension indicating that access to a resource has been denied due to legal demands or state censorship.
- [[ibm]] — early enterprise computing titan that created mainframe server hardware and middleware running widespread commercial protocol deployments.
- [[united-kingdom]] — homeland of protocol designer *Tim Berners-Lee*, who was knighted by the British Crown for inventing the World Wide Web.
- [[france]] — co-host nation of the *CERN* particle physics laboratory where the protocol was originally prototyped.
- [[cold-war]] — geopolitical era whose defense-funded networks like *ARPANET* laid the foundational packet-switching technologies enabling the web.
- [[space-age]] — technological epoch whose telecommunications satellites and electronic computation directly fostered the infrastructure of distributed hypermedia.
- [[linguistics]] — discipline underpinning formal syntax parsing, content negotiation, and the structural representation of semantic hypermedia documents.

## see also

- [[http-451-status-code]] · [[ibm]] · [[space-age]]

<!-- crosslinks -->
```dataviewjs
dv.view("_dv/crosslinks")
```
<!-- /crosslinks -->

<!-- tournav -->
```dataviewjs
dv.view("_dv/tournav")
```
<!-- /tournav -->

<!-- footer -->

---

Lists: [[misc-hubs]] · Mark read: `INPUT[toggle:read]`
