# Reports

Outcome: the scan turned into documents
other people can read — an HTML report
for humans, a JSON report for programs —
generated from the lab's session and
kept in the repository as evidence.

A session's alerts live in the daemon's
memory; a report is how they leave.
Two calls, both under the API's
`/OTHER/` prefix because they answer
with documents rather than JSON data:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/OTHER/core/other/htmlreport/ \
  > zap-report.html
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/OTHER/core/other/jsonreport/ \
  > zap-report.json
```

The lab's HTML report is 93 KB for a
toy application: a summary page of
counts by risk, then every alert with
its description, its instances, its
evidence and its fix — chapter 9's
fields, typeset. It is the document
you hand a person. The JSON report,
39 KB, is the same content for
machines: the input to dashboards,
ticket-filing scripts, and the
diff-the-scans habit of the recipes
chapter.

Check: transcript
`zap-lab/transcripts/t06-reports.txt`
generates both, and the reports
themselves are kept at
`zap-lab/reports/zap-report.html` and
`zap-lab/reports/zap-report.json`,
alongside the quick scan's report from
chapter 4.

## The JSON's odd shape

One wrinkle, earned by the lab the
usual way: the JSON report's keys wear
their history. The list of sites is
under `site`, each entry's name under
`@name` — the `@` marks values that
were attributes in the XML report this
format grew from:

```bash
python3 -c "import json; d=json.load(open('zap-report.json')); \
  s=d['site'][0]; print(s['@name'], len(s['alerts']))"
```

```text
http://127.0.0.1:18923 alert types: 13
```

Asking for `name` instead earns a
`KeyError` — the transcript keeps the
lab's own fumble, because the next
reader's script will make it too, and
now they will know it is the format,
not their data. Note the difference in
kind between this and the live API's
JSON (chapter 10): the API answers
questions with plain keys; the *report*
is a document with a lineage, and it
shows.

## What a report is — and is not

A report is a snapshot of one session's
claims, unreviewed. It does not know
which findings chapter 9's triage would
confirm, and by itself it proves only
that a scanner ran and said these
things. The habits that make reports
worth filing: generate them from a
session whose triage is done, or mark
them *raw* in the filename and mean it;
keep the report with the code version
it describes; and never let the count
on the summary page travel alone — 46
instances, 13 kinds, 3 confirmed Highs
and 1 High dismissed is a sentence;
"46 vulnerabilities" is a headline,
and a false one.
