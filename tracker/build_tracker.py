#!/usr/bin/env python3
"""Build tracker/index.html from plan/study-plan.json and tracker/tracker.template.html.

Usage: python3 tracker/build_tracker.py
The plan JSON is embedded inline so the page is fully self-contained.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PLAN = ROOT / "plan" / "study-plan.json"
TEMPLATE = HERE / "tracker.template.html"
OUT = HERE / "index.html"
MARKER = "/*__PLAN_JSON__*/null"


def main() -> None:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    ids = [t["id"] for w in plan["weeks"] for d in w["days"] for t in d["tasks"]]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate task ids in study-plan.json")
    payload = json.dumps(plan, ensure_ascii=False, separators=(",", ":"))
    # Keep the JSON safe inside a <script> element.
    payload = payload.replace("</", "<\\/").replace("<!--", "<\\!--")
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise SystemExit("Template must contain the plan marker exactly once")
    OUT.write_text(template.replace(MARKER, payload), encoding="utf-8")
    core = sum(t["minutes"] for w in plan["weeks"] for d in w["days"] for t in d["tasks"] if not t["optional"])
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(ids)} tasks, {core} core minutes, {OUT.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
