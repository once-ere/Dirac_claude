"""Compare every file listed in the 'writes' table of a notebook PROVENANCE file with its sha256 and size.
Usage: prov_hashes.py NB_ID_PREFIX...   (e.g. 05 or 05a 06b); prints mismatches and a summary."""
import hashlib
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # the repository folder
NB = REPO / "Revision/textbook/notebooks"
ROW = re.compile(r"^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})` \|$")
bad = checked = 0
for prefix in sys.argv[1:]:
    for prov in sorted(NB.glob(f"{prefix}*.PROVENANCE.md")):
        for line in prov.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if not m:
                continue
            rel, size, digest = m.group(1), int(m.group(2)), m.group(3)
            f = REPO / rel
            checked += 1
            if not f.exists():
                print(f"MISSING  {prov.name}: {rel}")
                bad += 1
                continue
            data = f.read_bytes()
            if len(data) != size or hashlib.sha256(data).hexdigest() != digest:
                print(f"MISMATCH {prov.name}: {rel} (size {len(data)} vs {size})")
                bad += 1
print(f"files checked: {checked}; mismatches: {bad}")
sys.exit(1 if bad else 0)
