"""Count the old labels (direction 8, the order x1..x8) left in textbook files.
Usage: scan_old.py FILE... [--lines]"""
import re
import sys
from pathlib import Path

LINES = "--lines" in sys.argv
FILES = [Path(a) for a in sys.argv[1:] if not a.startswith("--")]
PATTERNS = {
    "x8": r"(?<![A-Za-z0-9])d?x_?\{?8\}?(?![0-9])",
    "g88": r"g_?\{?88\}?|g\^\{?88\}?",
    "p8/P8/w8": r"(?<![A-Za-z0-9_])(?:p|P|w|rho|M|k|f|d)_?\{?8\}?(?![0-9])",
    "q48/q84": r"q_?\{?(?:48|84)\}?|B_?\{?(?:48|84)\}?",
    "gamma8": r"gamma\^?\{?\(8\)|gamma8|gamma\[7\]",
    "1..8 enum": r"x_?\{?1\}?\s*(?:,\s*)?(?:\\dots|\\ldots|\\cdots|\.\.\.?|…|to|through)\s*(?:,\s*)?x_?\{?8\}?",
    "old eta": r"\+,\s*\+,\s*\+,\s*-,\s*-,\s*-,\s*-,\s*\+|1,\s*1,\s*1,\s*-1,\s*-1,\s*-1,\s*-1,\s*1\b",
    "cot last": r"-e\^\{-2 ?a_4\} ?s,? ?\\?;?\s*\\cot\^2",
}
total = 0
for f in FILES:
    text = f.read_text(encoding="utf-8", errors="replace")
    counts = {k: len(re.findall(p, text)) for k, p in PATTERNS.items()}
    n = sum(counts.values())
    total += n
    if n:
        print(f"{f.name}: {n} " + " ".join(f"{k}={v}" for k, v in counts.items() if v))
        if LINES:
            for i, line in enumerate(text.splitlines(), 1):
                for k, p in PATTERNS.items():
                    if re.search(p, line):
                        print(f"   {i}: [{k}] {line.strip()[:150]}")
                        break
print("TOTAL", total)
