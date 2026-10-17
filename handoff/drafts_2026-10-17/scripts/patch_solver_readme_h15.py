"""H15: Revision/kohn_sham/solver/README.md - the refined run (SCF tolerance 1e-14, cap 1000 iterations), its results
(every number from reports/ks-rust-determinism.json of the H15 rerun) and its timings (from the step log of
scratchpad/run_h15.sh).  Usage: patch_solver_readme_h15.py STEPLOG"""
import json
import re
import sys
from pathlib import Path

KS = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham")
p = KS / "solver" / "README.md"
t = p.read_text(encoding="utf-8")
det = json.loads((KS / "reports" / "ks-rust-determinism.json").read_text(encoding="utf-8"))
C = {c["name"]: c["detail"] for c in det["checks"]}
assert all(c["verdict"] == "PASS" for c in det["checks"]), [c["name"] for c in det["checks"] if c["verdict"] != "PASS"]
steps = {}
for line in Path(sys.argv[1]).read_text(encoding="utf-8").splitlines():
    m = re.match(r"(\S+) rc=0 ([0-9.]+) s", line)
    if m:
        steps[m.group(1)] = float(m.group(2))


def g(name, pat):
    m = re.search(pat, C[name])
    assert m, (name, pat)
    return m.group(1)


def rep(a, b):
    global t
    assert t.count(a) == 1, (t.count(a), a[:80])
    t = t.replace(a, b)


rep('''refined-tolerance run (RK4 steps x 2, root tolerance / 10, SCF tolerance / 10, thermal cut / 100, and the
Mermin root in the form `LinearDeviation` instead of `LogBalance`).''',
    '''refined-tolerance run (RK4 steps x 2, root tolerance / 10, SCF tolerance / 1000 with at most 1000 iterations,
thermal cut / 100, and the Mermin root in the form `LinearDeviation` instead of `LogBalance`). The refined run
measures the canonical error, so it must differ in every error source: with the SCF tolerance / 10 (1e-12, until
2026-10-17) both runs could stop at the same iteration (the residual can drop from above 1e-11 to below 1e-12 in one
Anderson step) and carry the same SCF stopping error, which enters E_band - E_int and p0 at first order; the
cross-check then found int_p0 2.4e-10 off the reference with U_Rust = 2.7e-12 (`claude_failures.md` H15).''')
old_res = t[t.index("Results of 2026-10-16:\n`ks-rust-determinism.json` 14/14."):t.index("\n\n## Canonical results")]
new_res = (
    "Results of 2026-10-17 (after H15): `ks-rust-determinism.json` " + "%d/%d" % (sum(1 for c in det["checks"] if c["verdict"] == "PASS"), len(det["checks"]))
    + ". The repeat (three parts with `--inner-threads 2`, assembly with 3, against the\ncanonical two parts with 4) is "
    + "byte-identical in all " + g("repeat_byte_identical", r"(\d+ files \(\d+ bytes\))") + " and in its report. Refined against\n"
    + "canonical: E_KS to " + g("refined_ground_energies", r"max relative difference of E_KS ([0-9.e+-]+ \([^)]*\))") + " relative; HOMO, LUMO and gaps to "
    + g("refined_ground_homo_lumo_gap", r"KS gap ([0-9.e+-]+) m") + " m; " + g("refined_eigenvalues", r"(\d+) Kohn-Sham levels") + " levels label by label to\n"
    + g("refined_eigenvalues", r"max \|difference\| ([0-9.e+-]+ m)") + ", label sets and occupations identical; Delta-SCF to "
    + g("refined_delta_scf", r"excitation energies ([0-9.e+-]+ m)") + "; profiles to " + g("refined_profiles", r"the largest of their maxima\) ([0-9.e+-]+)")
    + " of their family's maximum\n(the measure was changed from the profile's own maximum, see `claude_failures.md` H9); Q_max and dE/da4 to "
    + g("refined_adiabatic_derivatives", r"max relative difference ([0-9.e+-]+)") + ";\nthermodynamics (mu, E, F, both forms of Omega, S) to "
    + g("refined_thermodynamics", r"\): max ([0-9.e+-]+)") + "; C_V to " + g("refined_heat_capacity", r"1e-6\)\) ([0-9.e+-]+)")
    + "; the analytic spectra converge with the\nerror ratio " + g("refined_free_spectra_convergence_order", r"median error ratio ([0-9.]+)")
    + " (RK4). The Mermin root along the two rounding paths: U_mu <= " + g("refined_mermin_root_path", r"U_mu = [^;]*?max ([0-9.e+-]+ m \([^)]*\))")
    + " and U_Omega <= " + g("refined_mermin_root_path", r"U_Omega = [^;]*?max ([0-9.e+-]+ \([^)]*\))")
    + ". The canonical-refined differences now contain the canonical SCF stopping error (refined SCF residual <= 1e-14).")
t = t.replace(old_res, new_res)
rep('''* Repeat in three parts: 76.9 s, 73.0 s, 84.7 s; assembly 6 s.
* Refined-tolerance run (G = 1800, root tolerance 1e-14, SCF tolerance 1e-12, thermal cut 1e-14, Mermin form
  `LinearDeviation`) in four parts: 152.5 s, 147.8 s, 156.0 s, 125.9 s; assembly 11.3 s.''',
    '''* Repeat in three parts: %.1f s, %.1f s, %.1f s; assembly %.1f s (2026-10-17, with the binary of H15; byte-identical
  to the record).
* Refined-tolerance run (G = 1800, root tolerance 1e-14, SCF tolerance 1e-14 with at most 1000 iterations, thermal cut
  1e-14, Mermin form `LinearDeviation`; 2026-10-17, H15) in four parts: %.1f s, %.1f s, %.1f s, %.1f s; assembly %.1f s
  (before H15, with the SCF tolerance 1e-12: 152.5 s, 147.8 s, 156.0 s, 125.9 s).'''
    % tuple(steps[k] for k in ("rust-repeat-p1", "rust-repeat-p2", "rust-repeat-p3", "rust-repeat", "rust-refined-p1",
                               "rust-refined-p2", "rust-refined-p3", "rust-refined-p4", "rust-refined")))
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
