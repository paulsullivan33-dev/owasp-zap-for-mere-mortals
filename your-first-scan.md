# Your First Scan

Outcome: a complete scan of something
real — small, planted with flaws, and
yours — by two different roads: the
one-command quick scan, and the daemon
that the rest of the guide drives. If
either road fails, chapter 16 is the
map of what the lab hit first.

## The practice application

Scanning needs a target, and the rule
of chapter 1 says the target must be
yours. The lab's is a practice shop,
`zap-lab/app/vulnapp.py` — a single
Python file, no dependencies, serving a
tiny seed store on loopback:

```bash
python3 zap-lab/app/vulnapp.py
```

It listens on `http://127.0.0.1:18923/`
and nowhere else. Its flaws are planted
and labelled in its own comments: no
security headers on any page, a login
that sets a flagless cookie, two pages
that echo what you type, an error page
that talks too much, and a comment in
the home page that names a test
account's password. Meet it directly
first, so the scanner's claims can be
judged against the thing itself:

```bash
curl -i http://127.0.0.1:18923/
curl -i "http://127.0.0.1:18923/hello?name=guest"
```

Check: transcript
`zap-lab/transcripts/t01-practice-app.txt`
shows the home page with its missing
headers and its indiscreet comment, the
echo working, the cookie arriving with
no flags, and the error page answering
a quote in the item number with a full
database-style error. Everything ZAP
reports later is already visible here
to a reader who knows the shapes; the
scanner's job is knowing the shapes so
you don't have to — yet.

## Road one: the quick scan

ZAP's **Quick Start** is the front door:
point it at a URL and it spiders the
site, passive-scans everything it sees,
and writes a report:

```bash
./zap.sh -cmd -quickurl http://127.0.0.1:18923/ \
    -quickout zap-quick-report.html
```

Forty seconds later the lab had a
76 KB report naming the missing headers,
the loose cookie, the unprotected form
and the suspicious comment. What it did
*not* contain is the lesson: no
cross-site scripting, no SQL injection —
because the quick scan never attacks.
It crawls and it watches; the active
scanner is a separate decision
(chapter 8). On a real application that
distinction is a safety feature, and
this guide treats it as one.

Check: transcript
`zap-lab/transcripts/t07-quickscan.txt`
keeps the run and the report's own list
of findings.

## Road two: the daemon

The road the rest of the guide travels:
ZAP as a **daemon** — no window, no
desktop, everything through the API.
Start it on loopback, on its own port,
with an **API key** (a password for the
API; the lab's is invented for the
occasion, and yours should be less
guessable):

```bash
./zap.sh -daemon -host 127.0.0.1 -port 18924 \
    -config api.key=labkey42
```

Two settings in that line are safety,
not decoration. `-host 127.0.0.1` keeps
ZAP's proxy — and its API — reachable
only from this machine; a ZAP daemon on
a network address is a scanner anyone
nearby can drive. And the key means the
API refuses strangers even here: every
call from now on carries it as the
`X-ZAP-API-Key` header.

Ask it for a page — the API action
`accessUrl` makes ZAP fetch a URL
through its own proxy, so the passive
scanner sees it:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  "http://127.0.0.1:18924/JSON/core/action/accessUrl/?url=http://127.0.0.1:18923/"
```

Then ask the passive scanner whether it
has finished reading (`recordsToScan`
must reach 0), and read the alerts:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/pscan/view/recordsToScan/
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/core/view/alerts/
```

One page, one fetch — and already six
findings: two Medium (the missing
Content Security Policy and the missing
anti-clickjacking header), three Low
(the two version leaks and the missing
content-type guard), one Informational
(the comment, caught in the act).

Check: transcript
`zap-lab/transcripts/t02-daemon-and-access.txt`
shows the version answer, the fetch,
the drained queue, and the six alerts
counted by the lab's `alert_summary.py`.

Stopping the daemon is an API call too:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/core/action/shutdown/
```

The lab starts and stops it several
times across the transcripts; each fresh
start is a fresh session, which is why
each chapter's counts begin from the
traffic that chapter creates.
