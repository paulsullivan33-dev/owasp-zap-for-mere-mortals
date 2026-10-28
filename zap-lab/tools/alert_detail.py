#!/usr/bin/env python3
"""Print the first alert with a given name, field by field.

Reads the JSON produced by the core/view/alerts API call on stdin:

    curl -s -H "X-ZAP-API-Key: ..." \
        http://127.0.0.1:18924/JSON/core/view/alerts/ |
        python3 alert_detail.py "Cross Site Scripting (Reflected)"
"""

import json
import sys

want = sys.argv[1]
data = json.load(sys.stdin)
for alert in data["alerts"]:
    if alert["name"] == want:
        for key in ("name", "risk", "confidence", "url", "param",
                    "attack", "evidence", "description", "solution",
                    "cweid", "wascid"):
            if alert.get(key):
                print(f"{key}: {alert[key]}")
        break
else:
    print(f"no alert named {want!r}")
    sys.exit(1)
