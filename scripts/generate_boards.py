#!/usr/bin/env python3
"""Regenerate the page boards (01-… to 19-…) from design/Main.dc.html.

Main.dc.html is the single source of truth. Each page board is a copy of it
with a different default `screen` (which page/state it opens on) and
`frameH` (board height), both read from design/canvas.json.

Usage:  python3 scripts/generate_boards.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "design"

SCREENS = {
    "01": "dashboard", "02": "crm", "03": "clients", "04": "projects",
    "05": "tasks", "06": "calendar", "07": "finance", "08": "documents",
    "09": "team", "10": "brief", "11": "lead", "12": "client",
    "13": "project", "14": "invoice", "15": "doc", "16": "member",
    "17": "taskDrawer", "18": "eventDrawer", "19": "convert",
}


def template(main: str) -> str:
    """Turn Main.dc.html into a template with __SCREEN__/__FH__/__TITLE__ slots."""
    subs = [
        (r"\(props && props\.screen\) \|\| '[A-Za-z]+'", "(props && props.screen) || '__SCREEN__'"),
        (r'"default":"[A-Za-z]+"\},"frameH"', '"default":"__SCREEN__"},"frameH"'),
        (r"this\.FH = \(props && props\.frameH\) \|\| \d+;", "this.FH = (props && props.frameH) || __FH__;"),
        (r'"default":\d+\},"\$preview":\{"width":1440,"height":\d+\}', '"default":__FH__},"$preview":{"width":1440,"height":__FH__}'),
        (r"<title>[^<]*</title>", "<title>__TITLE__</title>"),
    ]
    out = main
    for pattern, repl in subs:
        out, n = re.subn(pattern, repl, out, count=1)
        if n != 1:
            sys.exit(f"Could not find expected pattern in Main.dc.html: {pattern}")
    return out


def main() -> None:
    src = (ROOT / "Main.dc.html").read_text(encoding="utf-8")
    canvas = json.loads((ROOT / "canvas.json").read_text(encoding="utf-8"))
    tpl = template(src)
    count = 0
    for name, board in canvas["boards"].items():
        key = name[:2]
        if key not in SCREENS:
            continue
        title = "Business OS — " + board.get("title", name).split(" — ", 1)[-1]
        html = (tpl.replace("__SCREEN__", SCREENS[key])
                   .replace("__FH__", str(board["h"]))
                   .replace("__TITLE__", title))
        (ROOT / name).write_text(html, encoding="utf-8")
        count += 1
    print(f"Regenerated {count} boards from Main.dc.html")


if __name__ == "__main__":
    main()
