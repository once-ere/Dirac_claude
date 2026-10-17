"""H15 (W5): the reference solves every state to the SCF tolerance 1e-14 (ks_fd.SCF_TOL; before 1e-12 except the a4
neighbours, NB_TOL since H12), and evaluates the sea-hole diagnostic over at least 10% more shells than its thermal
label set (before 5 shells), so that the Rust thermal label sets, whose window rule differs, are covered.  Applied in
place to Revision/kohn_sham/reference/{ks_fd.py, run_reference.py} and checker/crosscheck_ks.py."""
from pathlib import Path

KS = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham")


def patch(path, pairs):
    t = path.read_text(encoding="utf-8")
    for a, b in pairs:
        assert t.count(a) == 1, (path.name, t.count(a), a[:80])
        t = t.replace(a, b)
    path.write_text(t, encoding="utf-8", newline="\n")
    print("patched", path.name)


if "SCF_TOL = 1e-14" not in (KS / "reference" / "ks_fd.py").read_text(encoding="utf-8"):
  patch(KS / "reference" / "ks_fd.py", [
    ('''def solve_state(grid: Grid, phys: Phys, ls: LevelSet, mode="aufbau", fixed=None, start=None, guess=None,
                tol=1e-12, maxit=400, mix_beta=0.5):''',
     '''# SCF tolerance of every state (units of m).  The SCF stopping error enters E_band - E_int and p0 at first order (they
# use the output densities with the levels of the input potential) and is not part of the Richardson uncertainty (it
# is nearly the same on the three grids); at 1e-12 it reached 4e-11 in int_p0 of N = 2352 (claude_failures.md H15)
SCF_TOL = 1e-14


def solve_state(grid: Grid, phys: Phys, ls: LevelSet, mode="aufbau", fixed=None, start=None, guess=None,
                tol=SCF_TOL, maxit=400, mix_beta=0.5):'''),
    ('''def solve_state_robust(grid: Grid, phys: Phys, ls: LevelSet, mode="aufbau", guess=None, tol=1e-12, maxit=400):''',
     '''def solve_state_robust(grid: Grid, phys: Phys, ls: LevelSet, mode="aufbau", guess=None, tol=SCF_TOL, maxit=400):'''),
])

patch(KS / "reference" / "run_reference.py", [
    ('''# SCF tolerance of those neighbours: their energies enter dE/da4 with the weights of rich_fd, about 1.5/delta, so an
# energy noise at the canonical tolerance 1e-12 m becomes ~1e-9 in dE/da4, above the Richardson uncertainty in the
# strongest couplings (claude_failures.md H12); at 1e-14 the finite difference is a clean h^2 series on the three grids
NB_TOL = 1e-14''',
     '''# SCF tolerance of those neighbours: their energies enter dE/da4 with the weights of rich_fd, about 1.5/delta, so an
# energy noise at the former tolerance 1e-12 m became ~1e-9 in dE/da4, above the Richardson uncertainty in the
# strongest couplings (claude_failures.md H12); at 1e-14 the finite difference is a clean h^2 series on the three grids.
# Since H15 every state is solved to ks_fd.SCF_TOL = 1e-14 as well.
NB_TOL = 1e-14'''),
    ('''SEA_EXTRA_SHELLS = 5     # sea-hole diagnostic: shells beyond the thermal label set that are also evaluated''',
     '''SEA_EXTRA_SHELLS = 5     # sea-hole diagnostic: at least this many shells beyond the thermal label set are evaluated,
SEA_EXTRA_FRACTION = 0.1  # and at least this fraction of the label set's shells: the cross-check sums the Rust sea holes
                          # over the Rust thermal label set, whose window rule differs (claude_failures.md H15)'''),
    ('''    # the shells of the label set (the first winfo["shells"] shells) and SEA_EXTRA_SHELLS more, without n2 = 0
    sea_shells = [s for s in K.shells(4096)[:winfo["shells"] + SEA_EXTRA_SHELLS] if s[0] >= 1]''',
     '''    # the shells of the label set (the first winfo["shells"] shells) and max(SEA_EXTRA_SHELLS, SEA_EXTRA_FRACTION x
    # shells) more, without n2 = 0
    extra = max(SEA_EXTRA_SHELLS, int(math.ceil(SEA_EXTRA_FRACTION * winfo["shells"])))
    sea_shells = [s for s in K.shells(4096)[:winfo["shells"] + extra] if s[0] >= 1]'''),
    ('''the four a4 neighbours on every grid", 1e-12),''',
     '''the four a4 neighbours on every grid", K.SCF_TOL),'''),
    ('''                                 "max |potential residual| (dM, v_v, w_Q) on every grid (m)", 1e-12),''',
     '''                                 "max |potential residual| (dM, v_v, w_Q) on every grid (m)", K.SCF_TOL),'''),
    ('''        "thermo_scf_converged": Agg("Mermin SCF converged at T, T +- dT, T +- 2 dT on every grid: max residual (m)", 1e-12),''',
     '''        "thermo_scf_converged": Agg("Mermin SCF converged at T, T +- dT, T +- 2 dT on every grid: max residual (m)", K.SCF_TOL),'''),
    ('''                                  "eta = N x 1e-12 / dT the noise floor of a difference quotient of energies at the SCF tolerance", 1.0),''',
     '''                                  f"eta = N x {K.SCF_TOL:g} / dT the noise floor of a difference quotient of energies at the SCF tolerance", 1.0),'''),
    ('''                                     f"the {SEA_EXTRA_SHELLS} shells beyond the thermal label set add at most 1e-9 max(1, total) (value: their share; "''',
     '''                                     f"the max({SEA_EXTRA_SHELLS}, {SEA_EXTRA_FRACTION:g} x shells) shells beyond the thermal label set add at most "
                                     "1e-9 max(1, total) (value: their share; "'''),
    ('''        eta = d["N"] * 1e-12 / (DT_REL * d["T"])''',
     '''        eta = d["N"] * K.SCF_TOL / (DT_REL * d["T"])'''),
    ('''                     "scfTolerance": 1e-12, "degeneracyTolerance": K.DEG_TOL,''',
     '''                     "scfTolerance": K.SCF_TOL, "degeneracyTolerance": K.DEG_TOL,'''),
])

patch(KS / "checker" / "crosscheck_ks.py", [
    ('''            u_ref = x[k]["U"] + (N * 1e-12 / dT if quotient else 0.0)''',
     '''            u_ref = x[k]["U"] + (N * scf_tol_ref / dT if quotient else 0.0)'''),
    ('''    scf_tol_R = float(rp["numerics"]["scfTolerance"])''',
     '''    scf_tol_R = float(rp["numerics"]["scfTolerance"])
    scf_tol_ref = float(fp["numerics"]["scfTolerance"])           # the reference's SCF tolerance (its parameters.json)'''),
    ('''as in its thermo_CV_identity check), eta_ref = N x 1e-12 / dT "''',
     '''as in its thermo_CV_identity check), eta_ref = N x {scf_tol_ref:g} / dT "'''),
])
print("ok")
