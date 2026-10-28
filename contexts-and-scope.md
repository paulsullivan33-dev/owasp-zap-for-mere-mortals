# Contexts and Scope

Outcome: the application drawn as a
boundary inside ZAP — one context
naming exactly what may be scanned —
so that chapter 1's rule is enforced
by the tool and not only by intentions.

Good intentions do not survive a long
afternoon. A scan started at the wrong
URL, a spider that wandered from the
staging copy to the live one through a
link nobody remembered: these are how
scanners cause incidents, and they are
organisational failures before they are
technical ones. ZAP's answer is the
**context**: a named definition of an
application — its URL patterns, its
technologies, its users — that scans
can be confined to.

## Making one

Through the API, as the lab did:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  "http://127.0.0.1:18924/JSON/context/action/newContext/?contextName=Seed%20Store"
curl -s -H "X-ZAP-API-Key: labkey42" \
  "http://127.0.0.1:18924/JSON/context/action/includeInContext/?contextName=Seed%20Store&regex=http://127.0.0.1:18923.*"
```

The first call creates the context;
the second gives it its territory — a
pattern matching the practice app's
address and everything under it. Read
back, the context shows its working:
the include patterns, the technologies
it assumes (the full list ZAP offers,
from databases to frameworks — a scan
policy can skip the families a context
rules out), and its authentication
settings, waiting empty.

Check: transcript
`zap-lab/transcripts/t09-context.txt`
creates the Seed Store context and
reads it back whole.

## Scope: the smaller circle

Inside a session, URLs are **in scope**
or out. Scans can be aimed at the scope
rather than the tree — *these three
folders, this afternoon's work* — and
the desktop colours the difference.
The working pattern the guide
recommends: context for the
application's permanent boundary, scope
for today's piece of it, and a habit of
looking at the scope before any active
scan the way you look at an address
before posting a letter.

## The login wall, honestly

Contexts are also where authentication
lives: ZAP can be taught a login — the
form, the fields, the phrase that
proves it worked — and will then spider
and scan as a logged-in user, which is
how the pages behind the wall reach
the tree. The lab verified the
context's creation and its settings;
it did **not** drive an authenticated
scan, because the practice app's login
is a fiction that accepts anything and
would prove nothing about real login
flows. So this part is taught from the
documentation and labelled: form-based
authentication is configured per
context, a *logged-in* and *logged-out*
pattern tells ZAP whether a session is
alive, and users are defined inside
the context for the scanner to act as.
On a real application, expect to spend
longer teaching the login than running
the scan — and expect the first
authenticated crawl to find a second
application's worth of pages, which is
the point of doing it.
