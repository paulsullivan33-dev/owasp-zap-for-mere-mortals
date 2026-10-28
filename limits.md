# Limits

What ZAP cannot do, stated as plainly
as what it can — because the most
dangerous report in security is a
clean one believed too well.

## A clean scan is not a safe application

ZAP tests for the shapes its rules
know. The lab's verdict depended on
that book: change the rules and the
counts move (the recipes chapter turns
this into a calibration habit). What
no rule book holds:

- **Logic flaws.** *Users can check out
  with a negative quantity* is a hole
  no attack string finds; it is not a
  shape, it is a decision. Scanners test
  the application's manners, not its
  arithmetic.
- **The second-order anything.** Data
  stored today and detonated next week
  in a different page, a different
  system, an email: the crawl-and-probe
  rhythm is blind to most of it.
- **Anything behind a door it could
  not open.** Un-crawled is un-scanned.
  The tree's silence about a corner of
  the application is a statement about
  the crawl, never about the corner.

## The scanner guesses — by design

Chapter 8's phantom is the standing
example: a High-risk SQL injection
reported against an application with
no database. That is not a defect to
apologise for; detection from the
outside is inference, and inference
errs. The defect would be a workflow
that forgets it: alerts are
*hypotheses with evidence attached*,
and the evidence — not the risk label —
is what a finding stands on. The same
honesty runs the other way: a rule
that does not fire proves the response
did not match the rule, nothing more.

## The login wall is load-bearing

Most of a real application lives behind
authentication, and ZAP's reach there
is exactly as good as the login you
teach it (chapter 12, where the lab
labels its own limit). Sessions that
expire mid-scan, multi-step logins,
hardware keys, single sign-on
redirects: each can quietly shrink a
scan to the public lobby while the
report prints the whole hotel. The
defence is the sites tree — read what
was actually covered before reading
what was found.

## Modern applications fight the crawl

JavaScript-built interfaces, websockets,
APIs spoken in JSON and GraphQL rather
than pages: ZAP has answers (a
browser-driven spider, API scanning
from a definition file) but they are
add-ons and extra teaching, and this
guide's verified ground is the classic
shape — pages, links, forms. A scanner
run against an application whose shape
it cannot follow completes happily and
finds little, and the little is not
evidence.

## The tool itself is a liability, managed

A ZAP daemon is a machine that attacks
what it is pointed at and records
everything it sees. Its proxy holds
other people's traffic if you route it;
its certificate authority, once trusted,
can impersonate any site to that
browser; its API, if reachable, is a
scanner anyone can drive. None of this
is an argument against the tool — it
is the tool's nature, as a saw's nature
is teeth. It is an argument for the
habits this guide repeats: loopback
binding, an API key, a testing-only
browser profile, recordings treated as
secrets, and the daemon off when the
work is done.

## The legal and ethical edge

Restated without decoration. Scanning
a system you do not own, without
permission you can name, is unlawful
in many jurisdictions *even if nothing
breaks and nothing is taken* — the
scan itself is the act. Permission
means specific: the owner, the systems,
the methods, the window. Employment is
not permission; a client's gratitude
is not permission; a bug-bounty
programme's written scope *is*, read
to the letter. And inside permission,
proportionality still binds: an active
scan against the production system
when a staging copy exists is a choice
to risk other people's service for
your convenience, and no checkbox on
a form makes it careful.

ZAP will not stop you. That is the
last thing this chapter can teach:
the guardrails in this guide are
settings and habits because, in the
end, they are a person deciding. The
decision is the tool's real interface.
