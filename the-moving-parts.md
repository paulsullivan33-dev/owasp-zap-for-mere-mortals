# The Moving Parts

ZAP is several tools wearing one coat.
Knowing which piece holds what is the
difference between "the scanner found
nothing" and "the scanner was never
shown the page" — a real distinction,
as this guide's lab learned more than
once (chapter 16).

## The proxy core

The engine is a server that listens on
a port you choose — **8080** by default,
18924 in this guide's lab — and speaks
the proxy dialect of HTTP. A client
connects and asks it to fetch a URL. The
core fetches it, and assembles each
exchange into a **message**: the request,
the response, and their timing, kept in
memory. Everything else in this chapter
is a way of feeding messages to the core
or judging the messages it holds.

For HTTPS the client asks the proxy to
open a tunnel, and ZAP can step inside
the encryption with a certificate
authority of its own — the same trick
the mitmproxy guide explores in depth.
This guide's lab is plain HTTP on one
machine, so the authority stays in its
box; chapter 15 says why trusting it
anywhere is a decision, not a default.

## The sites tree

Every URL the core has seen hangs on
the **sites tree**: a map of hosts,
folders and pages, with the parameters
each page takes. The tree is the
scanner's world. If a page is not on
it — behind a login the spider could
not pass, linked only from JavaScript
the crawl never ran — the scanners
have nothing to say about it, and their
silence means *unseen*, not *safe*.

## The spider

The **spider** is the crawler. Given a
starting URL, it fetches the page, reads
every link and form, and visits each in
turn, adding them all to the tree. It
also asks for two files by convention —
`robots.txt` and `sitemap.xml` — because
sites often confess their layout there.
Forms it meets, it fills in with
plausible junk and submits: in the lab,
that is how the practice login got
exercised without a human touching it
(chapter 6). A second, browser-driven
crawler for JavaScript-heavy sites
exists as an add-on; the lab's pages are
plain HTML and the classic spider was
enough, so the browser crawler is
described, not run (chapter 15).

## The passive scanner

The **passive scanner** reads every
message the core records and tests it
against a book of rules — there are
dozens, each looking for one shape of
wrong: a missing header, a cookie
without its flags, a version number
announced to the world, a comment that
mentions a password. It sends nothing.
Its findings are only as fresh as the
traffic it has seen, which is why the
guide's workflow always asks it one
question before reading results: *how
many records are left to scan?* A drain
of zero means its word is final — for
the traffic it was shown.

## The active scanner

The **active scanner** is the attacker.
For each page and parameter on the tree
it sends a battery of crafted requests —
attack strings in the parameter, in the
headers, in the path — and judges the
responses against what an un-attacked
response looks like. A script that comes
back reflected in the page, an error
that smells of a database: each match
becomes an alert. It works to a **scan
policy** — which rule families run, how
hard, how fast — and it is the only part
of ZAP that can do damage, which is why
chapter 8 gives it a chapter of warnings
along with its results.

## Alerts

Everything the scanners conclude is an
**alert**: a name, a risk (Informational,
Low, Medium, High), a confidence in the
finding, the URL and parameter, the
attack that was sent and the evidence
that came back, a plain-language
description, the suggested fix, and
references — the **CWE** number of the
weakness family and its **WASC** class.
Alerts are the unit of the whole tool:
the desktop shows them, the API returns
them, the reports are made of them.
Chapter 9 reads one the way it deserves
to be read — sceptically.

## Contexts and scope

A **context** is a named bundle that
says what an application *is* to ZAP:
the URL patterns that belong to it, the
technologies it is built from, how a
user logs in. Scans can be limited to a
context, and to what is **in scope** —
the part of the tree the current work
is about. Contexts are how chapter 1's
rule becomes machinery: draw the
boundary once, and the active scanner
will not wander past it.

## The faces

One engine, several interfaces. They
share the tree, the alerts and the
options, so nothing you learn in one is
wasted in another.

| Face | Shape |
|---|---|
| Desktop | A graphical application: tree, alerts and scans in windows |
| Daemon | No window at all: `zap.sh -daemon`, driven entirely through the API |
| Command line | One-shot runs, like the quick scan of chapter 4 |
| API | A web interface on the proxy port: every action and view as a URL |

The desktop is where most people explore.
This guide lives in the daemon and the
API, because everything done there can
be written down, repeated, and checked —
the transcripts in `zap-lab/` are the
evidence, and `criteria.md` is honest
that the desktop's windows are described
from the documentation, not driven.

## Add-ons

ZAP grows by **add-ons**: extra scan
rules, the browser-driven spider, report
templates, whole new tools, installed
from a marketplace inside ZAP and
updated the same way. The rules that
found this guide's results ship with
ZAP itself. Add-ons matter to chapter
15's honesty: a scanner is its rule
book, and the book is only as current
as its last update.
