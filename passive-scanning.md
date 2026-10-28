# Passive Scanning

Outcome: the findings that cost nothing
— no attack requests, no risk to the
application — read properly: what each
rule saw, why it matters, and where the
noise lives. Passive scanning is the
part of ZAP anyone may run against
their own applications, any day, and
this chapter is its field guide.

The passive scanner reads every message
the core records and tests it against a
book of rules. It runs continuously, in
the background; the only discipline it
asks is that you let it finish. The
queue is one API question away:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/pscan/view/recordsToScan/
```

Zero means every recorded message has
been judged. Reading results before the
drain is how "the scanner found nothing"
turns out to mean "the scanner hadn't
looked yet" — the lab checked before
every count in its transcripts.

## What it found in the lab

After the spider's crawl, 42 alert
instances in 11 kinds. Counted by the
lab's `alert_summary.py`
(`zap-lab/tools/`), in transcript
`zap-lab/transcripts/t03-spider.txt`:

- **Content Security Policy (CSP)
  Header Not Set** — Medium, 8 instances.
  No page tells the browser which sources
  of script and content to trust, so a
  scripting hole — chapter 8 finds three —
  has nothing standing behind it.
- **Missing Anti-clickjacking Header** —
  Medium, 6. Nothing stops another site
  framing these pages and dressing its
  own buttons over them.
- **Server Leaks Version Information** —
  Low, 8. Every response announces
  `BaseHTTP/0.6 Python/3.12.3`. An
  attacker shopping for known holes
  reads the label first.
- **X-Powered-By leak** — Low, 8. The
  same confession, in a second header.
- **X-Content-Type-Options Header
  Missing** — Low, 6. Browsers are free
  to sniff content and decide a text
  file is a script.
- **Absence of Anti-CSRF Tokens** —
  Medium, 1. The login form carries no
  token tying the submission to a page
  the application itself served, so a
  hostile page could submit it riding a
  visitor's browser.
- **Cookie No HttpOnly Flag** and
  **Cookie without SameSite Attribute** —
  Low, 1 each. The session cookie can be
  read by any script on the page, and
  travels on cross-site requests.
- **Information Disclosure - Suspicious
  Comments** — Informational, 1. The
  home page's comment names a test
  account and its password. ZAP's
  evidence is one word — `TODO` — and
  the comment behind it is the whole
  story. Evidence is a pointer, not the
  finding; chapter 9 insists on
  following it.
- **Authentication Request Identified**
  and **Session Management Response
  Identified** — Informational. Not
  weaknesses at all: ZAP noting *here is
  a login*, *here is a session starting*.
  Informational alerts are the scanner
  thinking aloud, and a healthy report
  is full of them.

## Reading the pattern, not the items

Three habits separate a reader from a
recipient. **Count kinds, not
instances.** Eight CSP findings are one
missing header on one framework setting,
fixed once; the instance count measures
the crawl, not the danger. **Follow
every Informational to ground.** They
are how the scanner shows its working —
and occasionally where the real secret
hides, as the `TODO` comment proves.
**Notice what passive scanning cannot
say.** It never sent an attack, so it
can only report shapes it recognises in
responses: it cannot know whether the
echo page is exploitable, only that the
defences around it are missing. The
findings it *cannot* make are the
active scanner's whole reason to exist
— and the boundary matters the other
way, too: passive findings are the
safest thing in this guide to collect
about an application you are still
deciding whether you may test. Reading
is reading; chapter 1's rule binds the
asking, not the algebra.
