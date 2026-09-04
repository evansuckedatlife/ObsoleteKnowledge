---
type: concept
category: misc
defines: [distributed denial-of-service attack, DDoS attack, distributed denial of service]
related: ["[[cold-war]]", "[[united-states]]", "[[new-york-city]]", "[[geometry]]", "[[perception]]"]
requires: ["[[united-states]]"]
lists: ["[[misc-hubs]]"]
tour_order: 0
read: false
---

# distributed denial-of-service attack

<!-- foundations -->
```dataviewjs
dv.view("_dv/foundations")
```
<!-- /foundations -->

## summary

A **distributed denial-of-service attack** is a malicious cyberattack that attempts to disrupt the normal traffic of a targeted server, service, or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic. Originating in the late 1990s and evolving alongside modern networking, these attacks leverage multiple compromised computer systems as sources of attack traffic. Understanding their operational architecture, attack vectors, and historical landmarks is foundational in computer science, cybersecurity, and information warfare competitions.

## you gotta know

- Weaponizes a botnet—a coordinated network of malware-infected computers, servers, or Internet of Things (*IoT*) devices—controlled remotely by an attacker via command-and-control servers.
- Distinguishes itself from a simple denial-of-service attack by utilizing multiple distributed source IP addresses, rendering simple packet filtering based on origin address ineffective.
- Categorized into three primary vectors: volume-based attacks (such as UDP floods and ICMP floods), protocol attacks (such as SYN floods and Ping of Death), and application-layer attacks (such as HTTP GET/POST floods).
- Amplification attacks exploit publicly accessible network services like DNS, NTP, and Memcached to reflect spoofed request packets, multiplying response payload volume directed at the victim.
- The historic *MafiaBoy* attacks of February 2000 orchestrated by Canadian teenager *Michael Calce* shut down major web services including *Yahoo!*, *eBay*, *CNN*, and *Amazon*.
- The October 2016 attack on the *Dyn* managed DNS service utilized the *Mirai* botnet, composed largely of consumer webcams and routers, crippling access to major services across the eastern [[united-states]].
- Contemporary defenses involve traffic scrubbers, content delivery networks (*CDNs*), Anycast routing architecture, and challenge-response mechanisms like *CAPTCHA*.

## connections

- [[united-states]] — host to federal agencies like CISA that coordinate critical infrastructure defense against large-scale state-sponsored cyberattacks.
- [[cold-war]] — historical geopolitical rivalry that spurred early decentralized network architecture (*ARPANET*) designed to survive catastrophic infrastructure disruption.
- [[new-york-city]] — major global telecommunications and financial hub whose exchanges rely heavily on anti-DDoS scrubbing centers to maintain market operations.
- [[perception]] — psychological factor exploited in hacktivist flood campaigns intended to signal institutional vulnerability and panic beyond physical system damage.
- [[geometry]] — topological study of network graphs and distributed node clusters utilized in modeling botnet command hierarchies and rerouting paths.

## see also

- [[cold-war]] · [[united-states]] · [[new-york-city]]

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
