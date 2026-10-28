# Troubleshooting

The failures this guide's lab actually
met, in the order a reader is likeliest
to meet them — plus the ones the lab's
design makes common. Every diagnosis
here was earned against the real tool.

## The API says Internal Error, and the fetch never happens

**Symptom.** `core/action/accessUrl`
answers `{"code":"internal_error"}`,
the spider finds nothing, the log
(`~/.ZAP/zap.log`) shows *Failed to
send the HTTP request:
java.net.SocketException: Connection
reset* — while curl reaches the target
perfectly.

**What it was in the lab.** Not ZAP.
The lab's sandbox resets loopback
connections from programs using the
Java platform's default dual-stack
sockets — proven outside ZAP with a
ten-line Java program that failed the
same way, and succeeded the moment it
was run with the IPv4 stack forced:

```bash
java -Djava.net.preferIPv4Stack=true Sock.java
```

The standing fix for ZAP itself is the
same flag, given to its launcher
through the JVM properties file
(chapter 3):

```bash
echo '-Xmx512m -Djava.net.preferIPv4Stack=true' \
  > ~/.ZAP/.ZAP_JVM.properties
```

Check: transcript
`zap-lab/transcripts/t90-ipv6-reset.txt`
keeps the failure, the proof and the
fix side by side. On an ordinary
machine this entry will never apply —
which is its other lesson: when ZAP
cannot fetch, test the same fetch
*without* ZAP before blaming either
side. A scanner is a witness, and
witnesses get cross-examined.

## The page loads, but ZAP records nothing

**Symptom.** Traffic sent "through the
proxy" returns fine; the tree stays
empty and the message count does not
move.

**Cause.** Your client bypassed the
proxy. Machines carry a `no_proxy`
list — loopback almost always on it —
and curl honours the list even when
`-x` names a proxy explicitly. The
request went direct; the success was
real and the recording never happened.
Defeat it per call with `--noproxy ''`,
and verify on ZAP's side
(`core/view/numberOfMessages`), never
by the page. Chapter 5 has the full
story; the lab's earlier sibling guide
fell into the same hole, which is how
the lab knew to look.

## The API refuses everything

**Symptom.** Calls answer with a
forbidden error or the connection is
refused outright.

**Causes, in order.** No key, or the
wrong one — the header is
`X-ZAP-API-Key`, and the value must
match the daemon's (`-config api.key=`
at start, or the stored key in
`~/.ZAP/config.xml`). The daemon bound
to a different address or port than the
one in your URL — check the start
command, not the script. Or the
daemon is not running at all: ask it
something free first,
`core/view/version`, and read
`zap.log` before reading your own code.

## The scanner found nothing at all

**Symptom.** A completed scan, a clean
report, a suspicious feeling.

**Causes.** The crawl never reached
the application (read the tree — the
URLs view is the ground truth of what
was scanned). The passive queue had
not drained when the alerts were read
(`pscan/view/recordsToScan`). The
active scan was aimed at a node with
`recurse` off, so it tested one page.
Or the target quietly requires a login
and served the lobby to every probe.
In the lab's experience the order of
suspicion is: tree, drain, scope,
login — and the fix is never *scan
harder* until all four are cleared.

## Alerts you expected are missing

The quick scan's report held no
scripting findings, and that was
correct behaviour wearing a worrying
face: the quick scan does not attack
(chapter 4). Rules also retire and
change between versions, and a scan
policy can disable families. Check
what ran before concluding what is
absent — or run the calibration recipe
in chapter 13 against the practice
app, whose truths do not move.

## ZAP runs out of memory, or crawls

The default heap offer is a quarter of
the machine's RAM, and a big crawl on
a small machine meets the ceiling.
Cap it deliberately
(`~/.ZAP/.ZAP_JVM.properties`,
chapter 3), then raise it on purpose
rather than by accident. The lab ran
everything in this guide at 512 MB —
proof that a small, well-scoped scan
is a light thing, and that *scope*,
not hardware, is the usual cure.

## A process command kills the wrong thing

For operators cleaning up by pattern:
`pkill -f` matches the full command
line of *every* process, including the
shell running the command — the lab
terminated its own session mid-cleanup
this way and lost a daemon start with
it. Kill by the PID you looked up, and
let ZAP's own shutdown action
(chapter 4) do the tidy work it was
built for.
