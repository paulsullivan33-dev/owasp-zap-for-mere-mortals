# What OWASP ZAP Is

A web application is a program that
answers requests: *show me this page*,
*here is a form, filled in*, *log me in*.
Its weaknesses live in those answers.
A page that prints whatever you type
straight back into itself can be made to
run an attacker's script in a visitor's
browser. A form with no protection can
be submitted by a different site, riding
on a visitor's login. A cookie set
without its flags can be read by any
script on the page. None of these are
exotic. All of them are the kind of
mistake a careful person makes on a
Tuesday and never notices.

**OWASP ZAP** — the Zed Attack Proxy,
from the Open Web Application Security
Project — is a program that looks for
those mistakes. It began as a proxy: a
program you place between your browser
and the application, which sees every
request and response. From that seat it
grew three ways of working, and this
guide is organised around them:

- **Passive scanning.** Every response
  that passes through the proxy is
  examined against a book of rules: is
  the security header missing, is that
  cookie loose, does that comment give
  something away? Passive scanning sends
  nothing of its own. It only reads.
- **Spidering.** ZAP follows every link
  and form it can find, building a map
  of the application — the **sites tree**.
  A scanner can only test what it has
  found, so the map comes first.
- **Active scanning.** ZAP sends crafted
  requests of its own — thousands of
  them — with attack strings in every
  field and parameter, and judges the
  responses. This is the scanner acting
  as an attacker, politely and on rails.

Each thing it reports is an **alert**:
one kind of weakness, at one place, with
the evidence it found, the risk it
assigns, and the fix it suggests.
Chapter 9 takes one apart.

## Why anyone would do this

Because the alternative is finding out
later, from someone less friendly. A
small team ships a web application; no
one on it is a security specialist; the
question "is there anything obviously
wrong with this?" deserves an answer
better than a shrug. ZAP is free, it is
open source, it is maintained by people
who do this professionally, and it runs
anywhere Java runs. It will not make an
application safe. It will hand you a
list of the known shapes of wrong,
ranked, with the evidence attached —
which is where fixing starts.

A first taste, after installing
(chapter 3) and meeting the practice
application (chapter 4). One command
spiders a small app and reports what
passive scanning saw, in a file:

```bash
zap.sh -cmd -quickurl http://127.0.0.1:18923/ -quickout zap-quick-report.html
```

The word for what that produces is
*starting point*. The rest of the guide
is about earning the right to trust the
list — by knowing what each kind of scan
can see, and what it cannot.

## The rule, stated before everything else

ZAP's active scanner sends attacks. Not
attack-shaped politeness — real attack
strings, of the same kinds real attackers
send, and against a fragile application
they can delete data, corrupt pages or
knock the thing over. The passive scanner
only reads, but what it reads is traffic,
and traffic can be other people's
secrets. So this guide has one rule, and
it is not fine print:

> **Scan only systems you own, or systems
> you have explicit permission to test.**

Your own application on your own machine:
yes. A staging copy your team runs for
testing: yes, that is what it is for. An
employer's production site "just to
look": no — permission is a specific
thing, given by someone who can give it,
covering scanning by name. A client's
site before the contract mentions
testing, a school's, a shop's, a
stranger's: no. In many places an
uninvited scan is a crime even when
nothing breaks, quite apart from the
ethics.

The lab in this guide went further than
most readers will need to: every scan
was aimed at a practice application the
lab itself wrote, on the same machine,
at an address — 127.0.0.1 — that means
*this computer* and never leaves it.
Chapter 12 is about making that
discipline a setting rather than a hope:
ZAP's **contexts** and **scope** draw the
boundary inside the tool, so a slip of
the mouse cannot send an active scan
somewhere it was never invited.

## Who it is for

The developer whose application is about
to meet the public and who wants the
obvious holes found by a friend first.
The small-team operator with a staging
server and an afternoon. The student of
security who learns by breaking a thing
built to be broken — which is exactly
what this guide's practice application
is. The common thread is one person, an
application they are allowed to test,
and a wish to see it the way an attacker
would, before an attacker does.

## What it is not

ZAP is not a guarantee: a clean report
means the known shapes were not found,
not that none exist — chapter 15 is
honest about the gap. It is not an
exploit kit: it reports the hole and
stops, and turning a finding into an
intrusion is a different, darker skill
this guide does not teach. It is not a
network scanner: it speaks HTTP and
HTTPS to web applications, and leaves
ports and services to tools like Nmap
(chapter 14). And it is not quiet
permission: the tool will happily scan
whatever you point it at, which is why
the rule above is yours to keep, not
the tool's.
