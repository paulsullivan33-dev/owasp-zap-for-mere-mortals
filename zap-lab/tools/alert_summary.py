#!/usr/bin/env python3
"""Summarise ZAP's alerts JSON: count instances by alert and risk.

Reads the JSON produced by the core/view/alerts API call on stdin:

    curl -s -H "X-ZAP-API-Key: ..." \
        http://127.0.0.1:18924/JSON/core/view/alerts/ |
        python3 alert_summary.py
"""

import json
import sys
import collections

data = json.load(sys.stdin)
counts = collections.Counter(
    (a["name"], a["risk"]) for a in data["alerts"])
for (name, risk), n in sorted(counts.items()):
    print(f"{n:3d}  [{risk}] {name}")
print(f"total alert instances: {len(data['alerts'])}")
