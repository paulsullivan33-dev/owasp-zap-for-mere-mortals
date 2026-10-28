# Glossary

**Active scanning** — ZAP sending
crafted requests of its own and judging
the responses; the scanner as attacker.
Chapter 8.

**Add-on** — an installable extension:
extra scan rules, crawlers, report
templates. The scanner is only as
current as its add-ons.

**Alert** — one finding: a named
weakness at one place, with risk,
confidence, evidence and a suggested
fix. Chapter 9 takes one apart.

**API key** — the password a ZAP
daemon's API demands with every call,
sent as the `X-ZAP-API-Key` header.

**Attack** — in an alert, the exact
crafted input the scanner sent. The
evidence is what came back.

**Baseline scan** — the packaged
automation pattern: spider plus passive
scan, no attacks; safe enough for a
pipeline, honest enough to say what it
skipped.

**Confidence** — the scanner's graded
opinion of its own finding: Low,
Medium, High. Read it before the risk.

**Context** — a named bundle defining
an application to ZAP: its URL
patterns, technologies and login.
Chapter 12.

**CWE** — Common Weakness Enumeration:
the catalogue number of a weakness
family. CWE-79 is cross-site scripting,
everywhere, in every tool.

**Daemon** — ZAP running with no
window, driven entirely through the
API: `zap.sh -daemon`.

**False positive** — an alert that is
wrong about this application. The
lab's database-free SQL injection is
the standing example.

**Message** — one recorded request and
its response, held by the proxy core.

**Passive scanning** — rules testing
recorded traffic; sends nothing.
Chapter 7.

**Quick scan** — the one-command run
of chapter 4: spider, passive scan,
report. No active attacks.

**Risk** — an alert's grade of harm
*if true*: Informational, Low, Medium,
High.

**Scan policy** — the active scanner's
rule book for a run: which families,
how strong, how fast.

**Scope** — the part of the sites tree
current work may touch; scans can be
confined to it.

**Sites tree** — ZAP's map of every
URL it has seen, with parameters: the
scanners' whole world.

**Spider** — the crawler that builds
the tree by following links and
submitting forms. Chapter 6.

**Triage** — the human review that
turns alerts into verdicts: confirmed,
false positive, or needs more
evidence.

**WASC** — the Web Application Security
Consortium's threat classification;
alerts carry its class beside the CWE.

**ZAP** — the Zed Attack Proxy, from
the Open Web Application Security
Project (OWASP): a free, open-source
web application security scanner.
