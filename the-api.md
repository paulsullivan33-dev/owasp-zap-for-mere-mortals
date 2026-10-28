# The API

Outcome: everything this guide has done,
understood as one interface — so a scan
can become a script, a script can become
a habit, and a habit can run before
every release. The lab's transcripts are
the examples; this chapter is the
grammar behind them.

## The shape of it

The API lives on the same port as the
proxy and speaks in URLs:

```text
http://127.0.0.1:18924/JSON/<component>/<kind>/<name>/
```

- **Component** — the part of ZAP:
  `core` (messages, sites, alerts),
  `pscan`, `spider`, `ascan`, `context`,
  and more as add-ons arrive.
- **Kind** — `view` for questions,
  `action` for orders. Views never
  change anything; actions do, and the
  distinction is worth respecting in
  scripts exactly as the tool draws it.
- **Name and parameters** — `view/alerts`,
  `action/scan/?url=...&recurse=true`,
  each taking its arguments as ordinary
  URL parameters.

Answers come back as JSON. Reports —
the big documents — live under a
sibling prefix, `/OTHER/`, and answer
with the document itself (chapter 11).

## The key, and the address

Every call in this guide carried the
header `X-ZAP-API-Key`. Without it, or
with a wrong one, the API refuses —
the refusal is the feature. Three
habits keep it honest:

- **Set a key** whenever the daemon
  runs, even on loopback; the lab set
  one in the start command, and ZAP can
  also generate and store one in
  `~/.ZAP/config.xml`.
- **Bind the daemon to loopback**
  (`-host 127.0.0.1`) unless the network
  case is deliberate and defended. An
  API that can start an active scan is
  a loaded tool; address plus key is
  the safety catch.
- **Keep the key out of the code you
  share.** The lab's key is invented and
  printed everywhere on purpose; a real
  key in a committed script is a secret
  leaked the way chapter 7's comment
  leaked — quietly, in plain sight.

## Automation, honestly graded

The lab drove the API by hand, with
curl, one call at a time — the slow
road, chosen because every step fits in
a transcript and can be checked. The
roads beyond it, in order of machinery:

- **Scripts like the lab's own.**
  `zap-lab/tools/api.sh` is eleven lines
  that remember the address and the key;
  `alert_summary.py` and
  `alert_detail.py` read the JSON the
  way any program can. A shell script
  that starts the daemon, spiders,
  waits, scans, and files the report is
  an evening's work from these parts,
  and it is this guide's verified
  ceiling.
- **Client libraries.** The project
  publishes API clients for Python,
  Java and other languages; a program
  gets objects instead of URLs. Read,
  not run, in this lab.
- **The packaged scans.** Docker images
  that run a baseline (spider plus
  passive), a full scan, or an API scan
  from one command, made for pipelines.
  The baseline is the packaged cousin of
  chapter 4's quick scan. Also read, not
  run — the lab had no Docker daemon,
  and `criteria.md` says so.
- **zap-cli and friends.** Community
  command-line wrappers over the same
  API. Same status: they exist, they
  work on these primitives, and this
  guide's claims stop at the primitives
  it ran.

The pattern to carry away: every layer
above the API is convenience, and every
convenience hides a decision the raw
calls make visible — which is why the
guide learned it raw first.
