# Helper for the ZAP lab: talk to the daemon's API on loopback.
# Usage: source api.sh, then: api core/view/version/
ZAPAPI=http://127.0.0.1:18924
ZAPKEY=labkey42
api() {
  curl -s --noproxy '*' -H "X-ZAP-API-Key: $ZAPKEY" "$ZAPAPI/JSON/$1"
}
# Wait until the passive scanner has no records left to check.
pscan_wait() {
  while :; do
    N=$(api pscan/view/recordsToScan/ | sed 's/[^0-9]//g')
    [ "$N" = "0" ] && break
    sleep 2
  done
}
