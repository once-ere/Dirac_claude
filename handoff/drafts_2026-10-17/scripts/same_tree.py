"""Byte-for-byte comparison of two result trees and two report files (the gate's `audit same`, written here for the
H15 rerun).  Usage: same_tree.py DIR_A DIR_B REPORT_A REPORT_B; exit 0 iff the same file set and every file identical."""
import sys
from pathlib import Path

a, b, ra, rb = (Path(x) for x in sys.argv[1:5])
fa = {p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file()}
fb = {p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file()}
diff = sorted(f for f in fa & fb if (a / f).read_bytes() != (b / f).read_bytes())
only = sorted(fa ^ fb)
rep_same = ra.read_bytes() == rb.read_bytes()
print(f"{len(fa)} / {len(fb)} files; only in one tree: {only[:10]}; differing: {diff[:10]}; reports identical: {rep_same}")
sys.exit(0 if not diff and not only and rep_same else 1)
