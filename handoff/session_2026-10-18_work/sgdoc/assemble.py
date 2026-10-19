#!/usr/bin/env python3
"""Assemble the student guide from its parts and fill the placeholders."""
import json, re, sys
from pathlib import Path
D = Path(__file__).resolve().parent
parts = ["s00.md", "s01.md", "s04.md", "s06.md", "s07.md", "s08.md", "s09.md", "s10.md", "s11.md", "s12.md", "s13.md", "s14.md", "s16.md", "s17.md"]
fills = json.loads((D / "fills.json").read_text()) if (D / "fills.json").exists() else {}
text = "\n".join((D / p).read_text().rstrip("\n") + "\n" for p in parts)
def sub(match):
    key = match.group(1)
    return fills.get(key, match.group(0))
text = re.sub(r"\{\{([a-z0-9]+)\}\}", sub, text)
out = Path(sys.argv[1])
out.write_text(text, encoding="utf-8")
left = sorted(set(re.findall(r"\{\{([a-z0-9]+)\}\}", text)))
print("written", out, "lines", text.count("\n"), "placeholders left", left)
