"""Diagnostic (not part of the record): is the cross-check mismatch of int_p0 and of the exact-Fock first-order
difference the SCF stopping error of the reference's MAIN ground state (tolerance 1e-12, residual ~5e-13 at a4 = 1.5)?
Recompute one ground state on one grid with the SCF tolerance 1e-12 (canonical) and 1e-14 (main state and neighbours)
and print the quantities of the failing comparisons.
Usage: python diag_scf_main.py ID G"""
import json
import sys
from pathlib import Path

REF = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham\reference")
sys.path.insert(0, str(REF))
import run_reference as R  # noqa: E402
import ks_fd as K  # noqa: E402

sid, G = sys.argv[1], int(sys.argv[2])
co = R.theory_coefficients()
gd = json.loads((REF / "results" / "ground" / f"{sid}.json").read_text(encoding="utf-8"))
tag = gd["lambda_tag"]
spec = {"id": sid, "N": gd["N"], "tag": tag, "lam": gd["lambda"], "a4": gd["a4"], "sigma": R.SIGMA[tag]}
orig_solve, orig_robust = K.solve_state, K.solve_state_robust
for tol in (None, 1e-14):
    if tol is None:
        K.solve_state, K.solve_state_robust = orig_solve, orig_robust
    else:
        def solve(*a, _tol=tol, **kw):
            kw["tol"] = _tol
            kw.setdefault("maxit", 2000)
            return orig_solve(*a, **kw)

        def robust(*a, _tol=tol, **kw):
            kw["tol"] = _tol
            kw.setdefault("maxit", 2000)
            return orig_robust(*a, **kw)
        K.solve_state, K.solve_state_robust = solve, robust
    ph = R.make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"])
    g0 = K.Grid(ph, R.GRIDS[0])
    ls0, _ = K.build_window(g0, ph, spec["sigma"], pad_ranks=R.PAD_RANKS)
    r = R._ground_on_grid(co, spec, G, ls0)
    s = r["scalars"]
    print(f"{sid} G = {G} tol = {'canonical' if tol is None else '%.0e' % tol}: residual {r['rec']['residual']:.1e} "
          f"iterations {r['rec']['iterations']}  int_p0 = {s['int_p0']:.15e}  deltaE_x = {s['deltaE_x_exact_fock']:.15e}  "
          f"E_KS = {s['E_KS']:.15e}  int_p3 = {s['int_p3']:.15e}  int_p_t = {s['int_p_t']:.15e}", flush=True)
K.solve_state, K.solve_state_robust = orig_solve, orig_robust
