"""Diagnostic (not part of the record): the reference's int_p0 (and the cancelling terms of p0) of one ground state on
the grids G = 300, 600, 1200, 2400 with the canonical SCF tolerance; Richardson over (300, 600, 1200) and over
(600, 1200, 2400).  Usage: python diag_ref_grids.py ID"""
import json
import sys
from pathlib import Path

REF = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham\reference")
sys.path.insert(0, str(REF))
import run_reference as R  # noqa: E402
import ks_fd as K  # noqa: E402

sid = sys.argv[1]
co = R.theory_coefficients()
gd = json.loads((REF / "results" / "ground" / f"{sid}.json").read_text(encoding="utf-8"))
tag = gd["lambda_tag"]
spec = {"id": sid, "N": gd["N"], "tag": tag, "lam": gd["lambda"], "a4": gd["a4"], "sigma": R.SIGMA[tag]}
ph = R.make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"])
g0 = K.Grid(ph, R.GRIDS[0])
ls0, _ = K.build_window(g0, ph, spec["sigma"], pad_ranks=R.PAD_RANKS)
vals = {}
for G in (300, 600, 1200, 2400):
    r = R._ground_on_grid(co, spec, G, ls0)
    s = r["scalars"]
    vals[G] = s
    print(f"G = {G}: residual {r['rec']['residual']:.1e} int_p0 = {s['int_p0']:.15e} int_p_t = {s['int_p_t']:.15e} "
          f"E_band = {s['E_band']:.15e}", flush=True)
for gs in ((300, 600, 1200), (600, 1200, 2400)):
    Rv, U = R.rich3(*[vals[G]["int_p0"] for G in gs])
    print(f"Richardson {gs}: int_p0 = {float(Rv):.15e}  U = {float(U):.3e}", flush=True)
