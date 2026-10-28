# Recipes

Short, complete jobs, each built from
parts the earlier chapters verified.
They assume the daemon pattern of
chapter 4 and the lab's two tools in
`zap-lab/tools/`.

## Check a release before it ships

The staging copy is up; the release is
tomorrow. Spider it, let the passive
scanner drain, then active-scan within
the context:

1. Start the daemon, key set, loopback
   bound (chapter 4).
2. `accessUrl` the staging home page,
   then spider it (chapter 6) and wait
   for `recordsToScan` to reach 0.
3. Read the passive summary first — if
   the headers are wrong on staging,
   they are wrong in production, and no
   attack is needed to learn it.
4. Active-scan (chapter 8), in scope
   (chapter 12), in the maintenance
   window you agreed.
5. Triage (chapter 9), generate the
   reports (chapter 11), file them with
   the release.

The gate is a human reading, not a
count: a release with three explained
dismissals ships easier than one with
an unread High.

## Watch your own browsing

Developing a web app and want every
request inspected as you click?

1. Make a browser profile used only for
   testing. Point it at the daemon's
   proxy (chapter 5).
2. Work the application the way a user
   does — every flow, every form,
   including the boring ones.
3. Spider afterwards, to catch the
   pages your clicking missed.
4. Read the passive alerts as you go;
   they accumulate live.

Never do this with your everyday
profile. The recordings are secrets and
the profile would follow you home.

## Prove a fix

A developer says the scripting hole is
closed. Do not rerun the whole battery
on trust:

1. In the same session if it survives —
   or a fresh one fed the same pages —
   rescan the one URL: the active
   scanner accepts a single page.
2. The alert should be gone. If it
   persists, its new evidence shows the
   payload that still lands, which is a
   better bug report than *still
   broken*.
3. Note the verdict and date with the
   original report. Fixes verified beat
   fixes asserted, and the paper trail
   is the difference.

## Keep the scanner honest

Once a quarter, run the lab itself:
the practice application in this
repository, start to finish. ZAP's
rules update constantly; the planted
flaws do not move. If the counts drift
— a rule retired, a confidence changed —
you learn it against a target whose
truth you know, instead of wondering
whether a real application's silence
means *fixed* or *unseen*. Calibration
targets are how measuring tools stay
measurements.
