# OWASP ZAP for Mere Mortals

A web application takes requests and
sends back pages. Some of those pages
have weaknesses: a form that trusts what
you type into it, a cookie set without
its safety flags, a header that should
be there and is not. **OWASP ZAP** — the
Zed Attack Proxy — is a scanner that
finds those weaknesses for you. It
watches traffic pass through its proxy
and notes what looks wrong (that is
**passive scanning**), it crawls your
application to find its pages (that is
**spidering**), and, when you tell it to,
it attacks the application with thousands
of crafted inputs and watches what breaks
(that is **active scanning**).

This guide explains how that works, how
to run your first scan against a practice
application on your own machine, how to
read an **alert** — ZAP's word for one
finding — and how to tell a real hole
from a scanner's guess. It shows the
whole tool driven from the command line
and through its **API**, the interface
that lets scripts run scans and collect
results. The limits are stated plainly,
including the biggest one: a scanner's
report is a list of suspicions, not a
verdict, and chapter 9 teaches the
difference with a finding from this
guide's own lab that turned out to be
a mirage.

The rule that governs everything here is
stated in chapter 1 and repeated in
chapter 15: **scan only systems you own,
or systems you have explicit permission
to test.** The lab obeyed it strictly.
Every scan in this guide was aimed at a
small practice application the lab wrote
for the purpose and ran on the same
machine, at an address that never leaves
that machine.

The lab behind this guide ran the real
thing: **OWASP ZAP 2.17.0**, the official
Linux release, on a small Linux machine,
against a throwaway practice shop —
a small Python program with its
flaws planted on purpose: no security
headers, a cookie with no flags, a login
form with no protection against forged
submissions, two pages that print what
you type straight back into the page,
and an error page that talks too much.
ZAP's spider found every page, its
passive scanner raised 42 findings just
from watching, and its active scanner
found the planted cross-site scripting
three times over — and also reported a
SQL injection that does not exist,
because the practice shop has no
database. The lab kept that finding in
the guide. Knowing why the scanner
believed it is worth more than another
success.

What the lab could not do, it did not
fake. It had one machine and one practice
application, so ZAP's graphical desktop —
the interface most people meet first —
is described rather than driven, and
scanning a site that asks you to log in
is taught through the context settings
the lab did verify, with the login
automation itself labelled as read, not
run. `criteria.md` keeps the full ledger
of what was run and what was only read.

## What this guide covers

- [**What OWASP ZAP is**](what-owasp-zap-is.md) —
  the mental model: a proxy with opinions,
  three kinds of scanning, and the ethics
  that are part of the tool, not an
  afterthought
- [**The moving parts**](the-moving-parts.md) —
  the proxy core, the sites tree, the
  spider, the passive and active scanners,
  alerts, contexts, add-ons and the API,
  and which part holds what
- [**Installing OWASP ZAP**](installing-owasp-zap.md) —
  the official release, the Java it needs,
  the `~/.ZAP` folder, and keeping the
  memory appetite under control
- [**Your first scan**](your-first-scan.md) —
  the practice application, the one-command
  quick scan, and starting ZAP as a daemon
  and asking it for a page
- [**The proxy — seeing your own traffic**](the-proxy.md) —
  sending one request through ZAP the way
  a browser would, and watching it land
  in the sites tree
- [**Spidering**](spidering.md) — the
  crawl that finds the pages, including
  the form it filled in by itself
- [**Passive scanning**](passive-scanning.md) —
  findings that cost no requests of their
  own: missing headers, loose cookies,
  comments that say too much
- [**Active scanning**](active-scanning.md) —
  ZAP as the attacker: the probes it
  sends, and the three scripting holes
  and one phantom it found in the lab
- [**Reading alerts**](reading-alerts.md) —
  one alert taken apart: risk, confidence,
  evidence, the fix, and the references —
  and how to judge the ones that are wrong
- [**The API**](the-api.md) — driving
  everything from scripts: actions and
  views, the API key, and why the lab's
  transcripts are all API calls
- [**Reports**](reports.md) — the HTML
  and JSON reports, what is in them, and
  the odd shape of the JSON
- [**Contexts and scope**](contexts-and-scope.md) —
  telling ZAP exactly which application
  it may touch, and drawing the line
  before the scanner does
- [**Recipes**](recipes.md) — check a
  release before it ships, watch your own
  browsing, rescan after a fix, keep the
  report with the code
- [**The neighbours**](the-neighbours.md) —
  Burp Suite, mitmproxy, Nmap, Nikto and
  nuclei: what each sees that ZAP doesn't,
  and vice versa
- [**Limits**](limits.md) — the scanner
  guesses, the login wall, the applications
  it cannot follow, and the legal and
  ethical edge, stated plainly
- [**Troubleshooting**](troubleshooting.md) —
  the connection that resets, the proxy
  that is not the proxy, the key the API
  refuses, and the traps this guide's lab
  fell into so you don't have to
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Scanning systems you do not own or have
permission to test — that is not a harder
chapter of this book, it is a crime in
most places, and chapter 15 explains the
line. Exploiting the holes ZAP finds —
turning a scripting hole into stolen
sessions, a SQL injection into dumped
tables — is likewise out: this guide
stops at finding and understanding, which
is the defender's half of the work.
Running ZAP as shared infrastructure for
a whole organisation — accounts, policy,
scan scheduling across teams — is pointed
at, not taught; this guide stays with one
person, their own machines, and
applications they are allowed to test.

## How to use this guide

Read chapter 1 for the model and the
rules, and chapter 2 before installing
anything — knowing which part holds what
turns later confusion into a named
problem. Chapters 3 and 4 take you from
download to a first scan in one sitting,
against the practice application; do not
aim ZAP at anything real until the
practice runs feel boring. Chapters 7
and 8 are the heart of it: run the
passive scan until you can predict its
findings, then let the active scanner
loose and read what it claims with
chapter 9 open beside you. The lab's
transcripts live in
`zap-lab/transcripts/`; its practice
application is `zap-lab/app/` and its
two small report tools are
`zap-lab/tools/`; the reports the lab
generated are in `zap-lab/reports/`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [mitmproxy for Mere Mortals](https://paulsullivan33-dev.github.io/mitmproxy-for-mere-mortals/)
- [Nmap for Mere Mortals](https://paulsullivan33-dev.github.io/nmap-for-mere-mortals/)
- [Trivy for Mere Mortals](https://paulsullivan33-dev.github.io/trivy-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/owasp-zap-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/owasp-zap-for-mere-mortals/blob/main/LICENSE-CODE).
