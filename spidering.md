# Spidering

Outcome: the whole practice application
on the sites tree — every page, every
form, two files nobody linked — found by
the spider in seconds, ready for the
scanners. The lesson underneath: a scan
covers what the crawl found, and the
crawl's habits decide what that is.

The spider is ZAP's crawler. Give it a
starting URL and it fetches the page,
extracts every link and form, visits
each in turn, and keeps going until
nothing new appears. Through the API:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  "http://127.0.0.1:18924/JSON/spider/action/scan/?url=http://127.0.0.1:18923/"
```

The answer is a scan number — `{"scan":"0"}` —
and the honest response to it is
patience, polled:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  "http://127.0.0.1:18924/JSON/spider/view/status/?scanId=0"
```

At 100, read the tree:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/core/view/urls/
```

The lab's tree holds eight URLs: the
home page, the three linked pages with
their parameters, the login page — and
`robots.txt` and `sitemap.xml`, which
nobody linked at all. The spider asks
for those two by convention, on every
crawl, because sites so often publish
their own map. (The practice app has
neither; both answers were 404s, and
they sit on the tree anyway — the tree
records what was *asked*, which is
exactly what a scanner's world looks
like.)

Check: transcript
`zap-lab/transcripts/t03-spider.txt`
shows the crawl, the tree, and what the
passive scanner made of it all: 42 alert
instances, up from 6 — the same few
weaknesses, now counted on every page
that carries them.

## The form it filled in by itself

The tree's quiet surprise is the login.
Among the alerts after spidering sit
*Cookie No HttpOnly Flag* and *Cookie
without SameSite Attribute* — findings
that require a cookie, and the cookie
is only set when the login form is
submitted. Nobody submitted it. The
spider did: it treats forms as doors,
fills each field with plausible text of
the right shape — an email-shaped string
for an email field, a password for a
password field — and walks through.

On a practice app that is delightful.
On anything real it is the chapter 1
rule wearing work clothes: a spider is
not a read-only guest. It submits
forms, follows logout links, presses
buttons labelled *delete*. Crawl a
staging copy, scope the crawl
(chapter 12), and never let a spider
loose on an application whose forms
do things you would not do by hand,
unattended, a hundred times a minute.

## What the spider cannot reach

- **Behind a login.** The spider's junk
  credentials do not log it in. Pages
  past the login wall stay off the tree
  until ZAP is taught to authenticate —
  contexts again, chapter 12.
- **Behind JavaScript.** Links that
  exist only after scripts run are
  invisible to the classic spider. ZAP's
  answer is a second crawler that drives
  a real browser (an add-on); the lab's
  app is plain HTML, so that crawler is
  described in chapter 15, not run here.
- **Behind a click at the wrong moment.**
  One-page applications, infinite
  scrolls, flows that need a human's
  judgement: the crawl stops where the
  clicking stops making sense.

Which is why the working habit is:
**browse first, spider second.** Drive
the application yourself through the
proxy (chapter 5) doing everything a
user can do — then spider to catch
what you missed. The tree is the union,
and the scanners judge the union.
