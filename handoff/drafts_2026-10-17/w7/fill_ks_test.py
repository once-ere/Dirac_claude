"""Assemble Revision/tests/test_kohn_sham_deflating_field_publication.py from test_ks.draft.py and its parts.
Usage: fill_ks_test.py OUT.py [MD_SHA TEX_SHA]"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
t = (HERE / "test_ks.draft.py").read_text(encoding="utf-8")
parts = {"@@TIP_TESTS@@": "test_ks_tip.py.part", "@@SOURCE_TESTS@@": "test_ks_source.py.part",
         "@@RUNTIME_TESTS@@": "test_ks_runtimes.py.part"}
for tag, name in parts.items():
    assert t.count(tag) == 1, tag
    t = t.replace(tag, (HERE / name).read_text(encoding="utf-8").rstrip("\n"))
old = '    ("Revision/kohn_sham/reports/ks-crosscheck.json", "(Rust solver and reference, {p} of {t} checks, "),\n'
new = '    ("Revision/kohn_sham/reports/ks-crosscheck.json", "within the stated uncertainty ({p} of {t} checks, "),\n'
assert t.count(old) == 1
t = t.replace(old, new)
if len(sys.argv) > 3:
    t = t.replace("@@MD_SHA@@", sys.argv[2]).replace("@@TEX_SHA@@", sys.argv[3])
Path(sys.argv[1]).write_text(t, encoding="utf-8", newline="\n")
print("wrote", sys.argv[1])
