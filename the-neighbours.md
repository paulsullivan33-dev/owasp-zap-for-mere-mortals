# The Neighbours

ZAP is one seat at a crowded table.
These are the tools a reader will meet
next to it — characterised, not
benchmarked; the lab ran ZAP and only
ZAP, and says so.

**Burp Suite** is the other proxy
scanner, and the comparison everyone
asks about. It is a commercial tool
(with a limited free edition) from
PortSwigger, polished where ZAP is
sprawling: a superb intercepting proxy,
a first-class manual testing bench —
Repeater, Intruder — and a scanner
reserved to the paid edition. The
working difference is centre of
gravity: Burp is built for a human
driving by hand, ZAP for automation
that runs itself — its API is free,
complete, and the same one its own
automation uses. Many professionals
own both and choose by task.

**mitmproxy** (a sibling guide in this
series) is the proxy without the
scanner: it shows, records and rewrites
traffic beautifully and judges none of
it. If ZAP's question is *what is wrong
with this application*, mitmproxy's is
*what did my program actually send*.
Developers debugging reach for the
second; the same person, wearing the
security hat, reaches for the first.

**Nmap** (also in this series) works a
floor below: hosts, ports, services,
the map of what exists. ZAP assumes a
web application already found and
speaks only HTTP to it. The natural
order on your own network is Nmap's
map first, then ZAP at the web-shaped
pins in it.

**Nikto** is the older, narrower web
server scanner: fast checks against
known-bad files, outdated server
software and misconfigurations, from
the command line, with no proxy and no
pretence of depth. It answers *is this
server obviously stale* in a minute.
ZAP answers a much larger question
much more slowly.

**nuclei** scans by templates —
thousands of small, specific checks
for known vulnerabilities and
exposures, contributed by a community
and run at speed. Where ZAP reasons
about an application's behaviour,
nuclei matches its fingerprints against
a catalogue. The two overlap less than
their reputations suggest.

And a boundary worth naming: **exploit
frameworks** — Metasploit and its kin —
begin where this guide ends, at *the
hole is confirmed; now go through it*.
That is a different discipline with
different rules, and confusing a
scanner's report for an invitation to
it is the exact mistake chapter 1
exists to prevent.
