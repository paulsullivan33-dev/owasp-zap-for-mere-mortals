# Reading Alerts

Outcome: one alert taken apart field by
field, and a triage habit — confirm,
dismiss, or send back for more evidence —
applied to every finding this guide has
raised, including the one that was
wrong.

An alert is a claim, and it arrives
wearing a uniform that makes all claims
look alike. The fields are how you tell
them apart. Here is one from the lab,
printed by `alert_detail.py`
(`zap-lab/tools/`):

```text
name: Cookie No HttpOnly Flag
risk: Low
confidence: Medium
url: http://127.0.0.1:18923/login
param: session
evidence: Set-Cookie: session
description: A cookie has been set without the
  HttpOnly flag, which means that the cookie can
  be accessed by JavaScript...
solution: Ensure that the HttpOnly flag is set
  for all cookies.
cweid: 1004
wascid: 13
```

Check: transcript
`zap-lab/transcripts/t04-passive-alert-details.txt`
has this one and two more, word for
word as the API returned them.

## The fields, and what each is for

- **Name.** The rule that fired. Rules
  are written by people and have habits;
  learning a rule's habits — what it
  counts as evidence, when it cries
  wolf — is most of triage.
- **Risk.** *If this is true, how bad?*
  Informational, Low, Medium, High. Risk
  orders the work; it does not grade
  the evidence.
- **Confidence.** *How sure is the
  scanner?* Low, Medium, High. The
  field readers skip, and the one that
  separates chapter 8's two Highs: the
  scripting findings at Medium
  confidence with the attack printed in
  the page, and the SQL injection at
  Low, resting on an error message.
- **URL and param.** Where the claim
  lives — the exact page and field, so
  the person fixing it starts at the
  right door.
- **Attack and evidence.** What was
  sent, and what in the response
  convicted it. For passive alerts the
  evidence is a fragment — a header
  line, one word of a comment. Evidence
  is always a pointer: follow it to the
  actual response before believing or
  dismissing anything.
- **Description and solution.** The
  weakness in plain language, and the
  fix in general terms — written for
  whoever owns the application, and
  good enough to paste into a ticket.
- **CWE and WASC ids.** The weakness's
  catalogue numbers. CWE-79 is
  cross-site scripting everywhere on
  earth; the ids are how a finding in
  ZAP joins the same conversation in
  every other tool, report and textbook.

## Triage: the verdict is yours

Every alert ends in one of three human
verdicts. **Confirmed** — the evidence
checks out against the application
itself: the lab's three scripting
holes, verified in transcript t01
before the scanner ever ran, where the
echo sits in the source for anyone to
see. **False positive** — the claim is
wrong about *this* application: the
SQL injection, dismissed not because
the scanner lied (the error page is
real, and it does disclose internals —
a lesser finding hiding inside the
wrong one) but because there is no
database for it to be true of.
**Needs more** — the evidence is thin
and the application can answer: most
Informational alerts live here until
someone reads the page they point at.

ZAP keeps your verdicts with the alert
when you mark them in a session, and
chapter 11's reports can carry them —
a report that says *reviewed, two
dismissed and why* is worth ten that
only count. The habit underneath all
of it: the scanner proposes, the human
disposes. A team that fixes Highs in
order without reading confidence and
evidence will someday spend a week
armouring a database that does not
exist, while a Medium with the attack
printed in the page waits its turn.
