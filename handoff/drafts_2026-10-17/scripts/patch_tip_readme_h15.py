"""H15: Revision/kohn_sham/tip_convergence/README.md after the rerun - the reference comparison (section 4.6 and the
checks table) and the run paragraph, from tip-convergence.json and the step log of run_h15.sh; asserts that the Rust
side (every number of sections 4.1 to 4.5) is unchanged by comparing the analysis block with the pre-H15 copy.
Usage: patch_tip_readme_h15.py STEPLOG PRE_H15_JSON"""
import json
import re
import sys
from pathlib import Path

D = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham\tip_convergence")
t = (D / "README.md").read_text(encoding="utf-8")
new = json.loads((D / "tip-convergence.json").read_text(encoding="utf-8"))
old = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
assert new["summary"]["passed"] == new["summary"]["total"] == 7, new["summary"]
for k in ("analysis", "couplings", "k0Spectrum", "zeroModeDensity", "firstOrderZeroModeEnergy", "states"):
    assert new[k] == old[k], "the Rust side changed: " + k
steps = {}
for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    m = re.match(r"(\S+) rc=0 ([0-9.]+) s", line)
    if m:
        steps[m.group(1)] = float(m.group(2))
chk = {c["name"]: c for c in new["checks"]}
worst = re.search(r"worst \|diff\|/tolerance ([0-9.]+)", chk["reference_solver_at_two_L"]["detail"]).group(1)
Ld = {(x["id"], x["quantity"]): x for x in new["reference"]["LDifferences"]}


def sub(a, b):
    global t
    assert t.count(a) == 1, (t.count(a), a[:70])
    t = t.replace(a, b)


e = Ld[("N8_lamp1_a00", "E_KS")]
p = Ld[("N8_lamp1_a00", "int_p0")]
sub("""int_rho of N8_lamp1_a00 and N592_lam0_a20), worst |diff|/tolerance 0.006. The $L$ differences agree:
$E_{KS}(4) - E_{KS}(3) = -7.658252309\\times10^{-4}$ (Rust) and $-7.658252252\\times10^{-4}$ (reference) for
N8_lamp1_a00, int_p0 $-8.069695434\\times10^{-3}$ and $-8.069695436\\times10^{-3}$;""",
    f"""int_rho of N8_lamp1_a00 and N592_lam0_a20), worst |diff|/tolerance {worst}. The $L$ differences agree:
$E_{{KS}}(4) - E_{{KS}}(3) = {e['rust_L4_minus_L3'] * 1e4:.9f}\\times10^{{-4}}$ (Rust) and ${e['reference_L4_minus_L3'] * 1e4:.9f}\\times10^{{-4}}$ (reference) for
N8_lamp1_a00, int_p0 ${p['rust_L4_minus_L3'] * 1e3:.9f}\\times10^{{-3}}$ and ${p['reference_L4_minus_L3'] * 1e3:.9f}\\times10^{{-3}}$;""")
sub("| `reference_solver_at_two_L` | abs(Rust - ref) <= 10 (U_ref + U_Rust) + 1e-9 max(1, abs x) | 28 comparisons, worst 0.006 |",
    f"| `reference_solver_at_two_L` | abs(Rust - ref) <= 10 (U_ref + U_Rust) + 1e-9 max(1, abs x) | 28 comparisons, worst {worst} |")
scan = [steps[f"tip-scan-p{i}"] for i in range(1, 7)]
recal = [steps[f"tip-recal-p{i}"] for i in range(1, 4)]
fin = steps["tip-final"]
i0 = t.index("Run of 2026-10-17 (the corrected metric;")
i1 = t.index("\n\n## 9. History")
t = t[:i0] + (
    "Run of 2026-10-17 (the corrected metric; 22 workers, each invocation under `timeout -k 5 423`; the rerun after the\n"
    "reference's SCF tolerance became 1e-14 and the solver's refined numerics changed, `claude_failures.md` H15, with a\n"
    "clean work folder): scan parts " + ", ".join("%.1f" % x for x in scan[:5]) + " and %.1f s; recal parts " % scan[5]
    + ", ".join("%.1f" % x for x in recal[:2]) + " and %.1f s; final %.1f s; %.0f s in all, 7 of 7 checks PASS. " % (recal[2], fin, sum(scan) + sum(recal) + fin)
    + "Every Rust\nnumber of sections 4.1 to 4.5 is the same as in the run before H15 (the canonical numerics did not change); the\n"
    "reference comparison of section 4.6 is the new one. The longest single run is N2352_lamp1_a00 at $L = 6$,\n"
    "$G = 3600$ (254.8 s in a timing test before H15, SCF fails); the parts are balanced so that none comes near the\n"
    "limit.") + t[i1:]
(D / "README.md").write_bytes(t.encode("utf-8"))
print("ok")
