# Active Scanning

Outcome: the practice application
attacked by its own scanner — thousands
of crafted requests, three real holes
found, one phantom raised — and the
judgement to run this only where it is
invited. This is the chapter the whole
guide's ethics exist for; read the
warning before the results.

## The warning, once more, with feeling

An active scan sends attacks. Against
the lab's practice app — built for it,
backed by nothing, holding no data —
that is sport. Against anything real it
can submit forms that delete, order,
email and publish; it can fill disks
with junk accounts and error logs; it
can knock a fragile application flat.
Scanners do not know which buttons are
load-bearing. You are the part of the
system that knows.

So: active-scan only what you own or
hold explicit permission to test
(chapter 1), on a staging copy rather
than the live thing wherever one
exists, in scope (chapter 12), at a
time when breaking it would be an
inconvenience and not an incident.

## Running it

The active scanner works the tree the
spider built. One API action starts it,
with `recurse=true` to take the whole
subtree:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  "http://127.0.0.1:18924/JSON/ascan/action/scan/?url=http://127.0.0.1:18923/&recurse=true"
```

Progress polls the same way the
spider's did. The lab's run — every URL
and parameter on an eight-page tree,
worked through rule family by rule
family — took about 35 seconds and
sent its requests in the thousands.
Against a real application, multiply
everything: hours are normal, and the
scan policy (which families run, at
what strength) is how you trade time
against thoroughness.

Check: transcript
`zap-lab/transcripts/t05-active-scan.txt`
keeps the start, the polling, and the
full results.

## What it found

The alert count moved from 42 instances
to 46 — but the new arrivals outrank
everything before them:

**Cross Site Scripting (Reflected) —
High, 3 instances.** The planted flaw,
found on all three pages that echo: the
item page, the search page, and the
hello page. One instance deserves a
look: on `/item`, the attack string was
sent in the `id` parameter and came
back inside the *error page* — the app
prints the offending value into its
database-error message, so the error
page is itself the hole. The alert
keeps the receipt:

```text
attack: </h1><scrIpt>alert(1);</scRipt><h1>
evidence: </h1><scrIpt>alert(1);</scRipt><h1>
```

The attack went in; the evidence is the
attack, sitting in the returned page
where a browser would run it. That is
what a confirmed finding looks like.

**SQL Injection — High, 1 instance,
confidence Low.** The scanner sent a
single quote as the `id`, got the 500
error page, and reported that SQL
injection *may be possible* — its own
description hedges, and its confidence
admits the hedge. And the lab can close
the case: **the practice app has no
database.** The error page is a canned
string the app prints for any quote;
nothing is queried, nothing can be
injected. The finding is a phantom —
raised honestly, from real evidence,
about a weakness that does not exist.

Both results are the chapter's lesson.
The active scanner is a tireless,
literal-minded attacker with no
knowledge of what stands behind the
page. It will find real holes a human
would take days to reach — three
scripting holes, one hiding in an error
page, is a good day's work. And it will
present a guess in the same format, at
the same High risk, as a certainty.
Risk is the scanner's opinion of *if
true, how bad*; confidence is its
opinion of *how likely true*. Reading
both, and checking the evidence, is the
human's job — and it is important
enough to get the next chapter to
itself.
