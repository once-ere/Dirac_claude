"""Diagnostic (not part of the record): does the reference's Mermin SCF converge to the tolerance 1e-14 for a heavy
thermal state, and how many iterations does it need?  Usage: python diag_ref_thermal.py ID G"""
import json
import sys
import time
from pathlib import Path

REF = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham\reference")
sys.path.insert(0, str(REF))
import run_reference as R  # noqa: E402
import ks_fd as K  # noqa: E402

sid, G = sys.argv[1], int(sys.argv[2])
co = R.theory_coefficients()
d = json.loads((REF / "results" / "thermo" / f"{sid}.json").read_text(encoding="utf-8"))
tag = d["lambda_tag"]
spec = {"id": sid, "N": d["N"], "tag": tag, "lam": d["lambda"], "a4": d["a4"], "T": d["T"], "sigma": R.SIGMA[tag]}
orig_solve, orig_robust = K.solve_state, K.solve_state_robust
for tol in (None, 1e-14):
    if tol is None:
        K.solve_state, K.solve_state_robust = orig_solve, orig_robust
    else:
        def solve(*a, _tol=tol, **kw):
            kw["tol"] = _tol
            return orig_solve(*a, **kw)

        def robust(*a, _tol=tol, **kw):
            kw["tol"] = _tol
            return orig_robust(*a, **kw)
        K.solve_state, K.solve_state_robust = solve, robust
    t0 = time.time()
    ls0, winfo, sea = R._thermo_window(co, spec)
    r = R._thermo_on_grid(co, spec, G, ls0, winfo["window_cut"], sea)
    print(f"{sid} G = {G} tol = {'canonical' if tol is None else '%.0e' % tol}: iterations {r['rec']['iterations']} "
          f"residual {r['rec']['residual']:.1e} path {r['rec']['path'][:40]} E = {r['th']['E']:.15e} mu = {r['th']['mu']:.15e} "
          f"({time.time() - t0:.1f} s)", flush=True)
K.solve_state, K.solve_state_robust = orig_solve, orig_robust
