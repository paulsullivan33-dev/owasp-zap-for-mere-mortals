# Installing OWASP ZAP

Outcome: ZAP 2.17.0 on the machine,
answering with its version, its memory
appetite capped, and its home folder
found. Everything in this chapter is
verified by the lab's first transcript;
the other install routes are named and
labelled as read, not run.

## What ZAP needs

ZAP is written in Java, so it needs a
**Java runtime** — version 17 or newer —
and runs the same on Linux, Windows and
macOS. The lab's machine had OpenJDK 21
already:

```bash
java -version
```

Check: the version prints, 17 or above.
If Java is missing, install it from your
system's packages first; ZAP's own
installers for some platforms bundle a
runtime, but the plain Linux release —
the one this guide uses — expects Java
to be there.

## The official release

Get ZAP from the project's own site,
zaproxy.org, or its GitHub releases —
never from a download mirror; a security
tool from a stranger is a contradiction.
The Linux release is a single tarball,
about 240 MB:

```bash
curl -LO https://github.com/zaproxy/zaproxy/releases/download/v2.17.0/ZAP_2.17.0_Linux.tar.gz
tar xzf ZAP_2.17.0_Linux.tar.gz
cd ZAP_2.17.0
```

Inside are the program (`zap-2.17.0.jar`),
its libraries and plugins, and the two
launchers: `zap.sh` for Linux and macOS,
`zap.bat` for Windows. There is nothing
to compile and nothing installed system
wide; the folder *is* the installation,
and deleting it uninstalls.

Other routes exist — an installer
package, a Docker image the project
publishes (the usual way to run the
packaged automation scans of chapter 10),
package managers on some systems. This
guide does not run them; the tarball is
the verified path, and everything after
this chapter is the same whichever door
you came in.

## First run

```bash
./zap.sh -version
```

The first run creates ZAP's home folder,
**`~/.ZAP`**, and copies a default
configuration into it. Then it prints
the version — and, in the lab, a small
confession the guide keeps because it
teaches something: *No check for updates
for over 3 month*. ZAP checks whether
its add-ons are stale and says so.
Chapter 15 explains why that matters:
the scanner is its rule book.

Check: transcript
`zap-lab/transcripts/t00-version.txt`
shows exactly this — Java found, the
folder created, `2.17.0` printed.

That command also shows ZAP's default
generosity with memory: `Using JVM args:
-Xmx1983m` — a quarter of the machine's
RAM, offered as the heap ceiling. On a
small or shared machine, cap it. The
launcher reads the first line of
`~/.ZAP/.ZAP_JVM.properties` as its JVM
arguments (creating the folder first,
if the first run has not):

```bash
mkdir -p ~/.ZAP
echo '-Xmx512m' > ~/.ZAP/.ZAP_JVM.properties
```

The lab ran ZAP at that cap throughout —
daemon, scans and reports — on a machine
where several other jobs were competing
for the same memory. Large applications
and long scans want more; the setting
is a ceiling, not an appetite, and a
scan that runs out of heap says so in
the log rather than lying about its
results.

## Where things live

- `~/.ZAP/config.xml` — the configuration,
  including the API settings of chapter 10
- `~/.ZAP/zap.log` — the log; when ZAP
  says *Internal Error*, this file says
  why (chapter 16 lives here)
- `~/.ZAP/session/` — saved sessions: the
  tree and alerts of a piece of work,
  kept between runs when you ask
- the install folder — the program and
  its add-ons; never edit by hand

One warning before the next chapter:
the same first run writes a **dynamic
certificate authority** into the ZAP
folder — the key that lets ZAP step
inside HTTPS. It is created quietly and
used only when you route HTTPS through
the proxy and tell a browser to trust
it. This guide never does. If you ever
do, chapter 15 first: a trusted authority
is a key to every encrypted conversation
on that machine.
