# The Proxy — Seeing Your Own Traffic

Outcome: one request, sent through ZAP
the way a browser sends it, recorded by
the core and judged by the passive
scanner — proof the seat in the middle
works, and a template for driving ZAP
with a real browser on your own machine.

Chapter 4 fed ZAP a page from the
inside, with an API action. This chapter
uses the front door: ZAP is a proxy, and
anything that can be told to use a proxy
can be watched by it. The lab's client
is curl, because curl's conversation
fits in a transcript; a browser pointed
at the same port behaves identically
and sees a great deal more.

With the daemon running (chapter 4),
send one request through it:

```bash
curl -i --noproxy '' -x http://127.0.0.1:18924 \
    "http://127.0.0.1:18923/hello?name=guest"
```

The page comes back exactly as the
practice app sent it — the proxy does
not mark its work. But on ZAP's side,
the exchange is now a message in the
core. Ask what the core holds:

```bash
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/core/view/numberOfMessages/
curl -s -H "X-ZAP-API-Key: labkey42" \
  http://127.0.0.1:18924/JSON/core/view/urls/
```

Two messages — the request and its
response — and the site is on the tree.
And because every recorded message is
passive-scanned, the hello page earns
the five header findings at once, with
nobody scanning anything: watching was
enough.

Check: transcript
`zap-lab/transcripts/t08-proxy.txt`
shows the fetch, the count, the tree,
and the five alerts.

Two traps hide in that one command, and
the lab met both before it met success:

- **The bypass.** Most machines carry a
  `no_proxy` list naming loopback, and
  curl honours it *even when you name a
  proxy yourself* — the request goes
  direct, the page comes back, and ZAP
  records nothing. A working page and an
  empty tree is this trap's signature;
  `--noproxy ''` empties the list for
  that call. Chapter 16 has the whole
  story.
- **The invisible success.** Through the
  proxy, success looks like nothing
  happened. Verify on ZAP's side —
  message count, tree, alerts — never by
  the page alone.

Pointing a real browser at the proxy is
the same setting in a different window:
the browser's proxy configuration, set
to the daemon's host and port, for as
long as the session lasts. Two cautions
belong with it. Your browsing is then
traffic in someone else's tool — yours,
but recorded; ZAP keeps what it sees,
and recordings are secrets (chapter 15).
And HTTPS through the proxy is a tunnel
ZAP cannot read unless the browser
trusts ZAP's certificate authority —
which this guide does not do, and
chapter 15 explains why that trust is a
loaded key. For watching your own
application during development, the
pattern that serves best is a separate
browser profile, used for testing and
nothing else, pointed at ZAP only while
the test lasts.
