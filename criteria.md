# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 15 names what the tool
   cannot do: the logic flaws and un-crawled corners a scanner
   cannot see, the inference behind every alert, the login
   wall, the modern application shapes the crawl cannot
   follow, the daemon and its recordings as liabilities, and
   the legal edge around scanning anything that is not yours.
8. **The ethics rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *your systems, or explicit
   permission to test them* — before any procedure depends on
   it, and later chapters point back to it where the tooling
   would make crossing the line easy.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 2-CPU, 7.7 GB Ubuntu 24.04 sandbox.
OWASP ZAP **2.17.0** (the official Linux tarball) ran on the
machine's OpenJDK 21, with its heap capped at 512 MB through
`~/.ZAP/.ZAP_JVM.properties`, against a practice application
written for this guide (`zap-lab/app/vulnapp.py`): a small
Python program on loopback (127.0.0.1:18923) with its flaws
planted and labelled. ZAP was driven as a daemon on
127.0.0.1:18924, entirely through its API, and stopped with
the API's own shutdown action. **No target other than the
lab's own practice application was ever scanned, proxied or
requested through ZAP.** All transcripts live in
`zap-lab/transcripts/`; the tools are `zap-lab/tools/`; the
generated reports are kept in `zap-lab/reports/`.

Run for real, with transcripts as evidence:

- Install and version: the tarball unpacked, `zap.sh -version`
  printing 2.17.0 and creating `~/.ZAP` (t00).
- The practice app met directly: its missing headers, its
  indiscreet HTML comment, the reflected parameter, the
  flagless session cookie on login, and the database-style
  error page answering a quote (t01).
- The daemon started with an API key; a single `accessUrl`
  fetch and the passive scanner's first six alerts after the
  queue drained (t02).
- The spider's crawl: eight URLs on the tree including the
  unlinked `robots.txt` and `sitemap.xml`; the spider
  submitted the login form itself, earning the cookie alerts;
  42 passive alert instances in 11 kinds (t03).
- Three alerts read in full through the API — CSP, the
  HttpOnly flag, the suspicious comment — every field as
  returned (t04).
- The active scan of the whole tree (about 35 seconds):
  three Reflected Cross Site Scripting findings (High),
  including one inside the error page, with the attack and
  evidence; and one SQL Injection finding (High, confidence
  Low) against an application that has no database — kept
  and taught as a false positive (t05).
- HTML (93 KB) and JSON (39 KB) reports generated from the
  session and read back, including the JSON report's
  `@`-prefixed keys, found by a KeyError the transcript
  keeps (t06).
- The one-command quick scan and its report: passive
  findings only, no attack findings, because the quick scan
  never attacks (t07).
- One request driven through the proxy with curl, landing
  in the core's message count and earning its five passive
  alerts (t08).
- A context created through the API, given its include
  pattern, and read back whole (t09).
- The sandbox's central trap, also run for real: the
  environment resets loopback connections from default
  dual-stack Java sockets — ZAP's fetches failed with
  "Connection reset" until `-Djava.net.preferIPv4Stack=true`
  was set, proven independently with a ten-line Java
  program failing and then succeeding (t90).

Documented only — described from the project's documentation,
not run, and the text does not claim otherwise:

- The desktop graphical interface: its windows and panels.
  The same engine was driven through the daemon and API,
  which is where this guide's evidence lives.
- HTTPS interception and ZAP's dynamic certificate
  authority; the lab is plain HTTP between its own programs.
- Pointing a real browser at the proxy (the curl-driven
  proxy path of chapter 5 is verified; the browser setting
  is the same setting in another window).
- Authenticated scanning: contexts were created and read
  back, but no login was taught to ZAP, because the practice
  app's login accepts anything and would prove nothing.
- The browser-driven (AJAX) spider for JavaScript-heavy
  sites; the lab's pages are plain HTML.
- The packaged automation scans (baseline, full, API) and
  the published API client libraries and zap-cli; the lab
  drove the raw API because the packaged routes need a
  Docker daemon the sandbox does not provide.
- Scan policies beyond the defaults the active scan used.
- The comparison tools in chapter 14 are characterised, not
  benchmarked.

Fixtures are this guide's own and deliberately generic: a
small seed-store program whose flaws are planted and
labelled in its own comments, two small report tools, and an
API key invented for the occasion and printed openly. No
example is modelled on any real person, network, service or
organisation, and nothing was scanned that the lab did not
itself write and run.
