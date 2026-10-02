#!/usr/bin/env python3
"""Revision Kohn-Sham REFERENCE run: an independent Python solver for SPEC section 7 with a different
discretisation (staggered finite differences in y, Richardson extrapolation over G = 300, 600, 1200).

Revision code only: it imports nothing from the old stages and nothing from the Rust solver.  Inputs:
Revision/kohn_sham/ks-theory.json (the functional coefficients and the checked formulas).  The physical
constants are the problem definition of SPEC section 7 (H = m = 1, L = 3, dk = 0.25, v_t = 1, regular tip
theta = 0, ASSUMED Z2 brane, history a4 = A H x4 with A = 1 and slices a4,0 in {0, 0.5, 1, 1.5, 2},
temperatures {0.01, 0.02, 0.05} m, first-order mean-field targets sigma = 0.1 and 0.3 m).  The particle
numbers N_mid, N_large and the couplings lambda_1, lambda_2 are RE-DERIVED here from their stated rules.

Coordinates: x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times
(scale factor e^{-a4} sin^{1/6} z, a4 increasing); x8 = hidden direction, y = ln(sin z)/(6H).

The FULL canonical matrix is solved: 75 ground states (N in {8, N_mid, N_large}, 5 coupling tags, 5 slices) with
their Delta-SCF states, a4 neighbours, adiabaticity pairs and particle-hole lists; the exact-Fock-exchange
variant of the 60 states with lambda != 0; the rescaling partners of the 60 states with a4,0 > 0; the crossing
demonstration (lambda = 0, N_demo re-derived); 135 thermal states (lambda in {0, +-lambda_1}, 3 temperatures) with
their temperature neighbours and the sea-hole diagnostic of the filling convention.

Every result is reported as the three-grid Richardson value R = (64 x(4G) - 20 x(2G) + x(G))/45 with the
measured grid uncertainty U = |R - R2| + 2e-12 max(1, |R|), R2 = (4 x(4G) - x(2G))/3 (the size of the
h^4 term at the finest grid; validated on a fourth grid G = 2400 for one state).

Usage (from the repository root):
  python Revision/kohn_sham/reference/run_reference.py [--out DIR] [--report FILE] [--timing FILE] [--jobs N]
Defaults: --out Revision/kohn_sham/reference/results, --report Revision/kohn_sham/reports/ks-reference.json.
Outputs are deterministic (LF, no timings or paths); --timing writes the wall-clock times separately.
"""

from __future__ import annotations

import os

for _v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import hashlib
import json
import math
import multiprocessing as mp
import re
import shutil
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ks_fd as K  # noqa: E402

KS = HERE.parent
REPO = KS.parent.parent
KS_THEORY = KS / "ks-theory.json"

GRIDS = (300, 600, 1200)
G_VALID = (300, 600, 1200, 2400)
BASE = dict(H=1.0, m=1.0, L=3.0, dk=0.25, vt=1.0)
SLICES = (0.0, 0.5, 1.0, 1.5, 2.0)
TEMPS = (0.01, 0.02, 0.05)
SIGMA = {"lam0": 0.0, "lamp1": 0.1, "lamm1": 0.1, "lamp2": 0.3, "lamm2": 0.3}
FD_DELTA = 2e-3          # a4 step of the fixed-occupation neighbours (+- delta, +- 2 delta, Richardson)
DT_REL = 0.01            # temperature step dT = 0.01 T of the thermal neighbours
PAD_RANKS = 2            # ranks 0..2 in every sector of an occupied shell (pairs of the adiabaticity measure)

# The FULL canonical matrix (N: 8, "mid" = N_mid, "large" = N_large): 75 ground states (5 coupling tags, 5 slices)
# and 135 thermal states (lambda in {0, +-lambda_1}, 5 slices, 3 temperatures).
N_KEYS = (8, "mid", "large")
GROUND_TAGS = ("lam0", "lamp1", "lamm1", "lamp2", "lamm2")
THERMO_TAGS = ("lam0", "lamp1", "lamm1")
GROUND_MATRIX = [(Nk, tag, a4) for Nk in N_KEYS for tag in GROUND_TAGS for a4 in SLICES]
THERMO_MATRIX = [(Nk, tag, a4, T) for Nk in N_KEYS for tag in THERMO_TAGS for a4 in SLICES for T in TEMPS]
VALIDATION_STATE = ("mid", "lamp2", 2.0)
PH_ROWS = 48             # particle-hole excitations kept per ground state (the Rust solver lists the lowest 24)
CROSSING_EMAX = 1.6      # free a4,0 = 0 closed shells up to this energy: the N of the crossing demonstration
SEA_EXTRA_SHELLS = 5     # sea-hole diagnostic: shells beyond the thermal label set that are also evaluated

PROFILE_NAMES = ("n", "S", "Q", "M_eff", "v_v", "e_int", "rho", "p3", "p_t", "p8")


# ------------------------------------------------------------------------------------------------
# helpers
# ------------------------------------------------------------------------------------------------
def rich3(x1, x2, x3):
    """Richardson over h, h/2, h/4 (x1 coarsest) for errors in even powers of h."""
    x1, x2, x3 = (np.asarray(v, dtype=float) for v in (x1, x2, x3))
    r2 = (4.0 * x3 - x2) / 3.0
    r1 = (4.0 * x2 - x1) / 3.0
    R = (16.0 * r2 - r1) / 15.0
    U = np.abs(R - r2) + 2e-12 * np.maximum(1.0, np.abs(R))
    return R, U


def rich_fd(fp1, fm1, fp2, fm2, d):
    """Richardson-extrapolated central difference from f(+-d), f(+-2d)."""
    d1 = (np.asarray(fp1) - np.asarray(fm1)) / (2.0 * d)
    d2 = (np.asarray(fp2) - np.asarray(fm2)) / (4.0 * d)
    return (4.0 * d1 - d2) / 3.0


def asym_ratio(x1, x2, x3, floor=1e-10):
    """(x(G) - x(2G)) / (x(2G) - x(4G)) for the elements whose differences exceed the floor."""
    x1, x2, x3 = (np.atleast_1d(np.asarray(v, dtype=float)) for v in (x1, x2, x3))
    d1, d2 = x1 - x2, x2 - x3
    m = (np.abs(d2) > floor) & (np.abs(d1) > floor)
    return (d1[m] / d2[m]).tolist()


def jsonable(o):
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    if isinstance(o, np.ndarray):
        return jsonable(o.tolist())
    if isinstance(o, (np.floating, float)):
        x = float(o)
        return x if math.isfinite(x) else None
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    return o


def dump_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(jsonable(obj), indent=1, ensure_ascii=True) + "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)


def f16(x):
    return "null" if x is None or not math.isfinite(float(x)) else f"{float(x):.15e}"


def write_csv(path: Path, header, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(",".join(header) + "\n")
        for r in rows:
            fh.write(",".join(str(v) for v in r) + "\n")


def run_id(N, tag, a4, T=None):
    s = f"N{int(N)}_{tag}_a{int(round(a4 * 10)):02d}"
    if T is not None:
        s += f"_T{int(round(T * 1000))}"
    return s


def round_sig(x, d=4):
    return float(f"{x:.{d}g}")


def key_str(k):
    return f"{k[0]}:{'+1' if k[1] > 0 else '-1'}:{k[2]}:{k[3]}"


def theory_coefficients():
    th = json.loads(KS_THEORY.read_text(encoding="utf-8"))
    ex = th["exchange"]
    cM = Fraction(ex["kohnShamPotentials"]["Meff_coefficient_of_lambda_S"])
    cV = Fraction(ex["kohnShamPotentials"]["vv_coefficient_of_lambda_n"])
    cn2 = Fraction(ex["uniformGas"]["coefficient_n2"])
    cs2 = Fraction(ex["uniformGas"]["coefficient_S2"])
    slope = float(th["checksNumeric"]["braneBandSlope_M1_H1_L3_a0"])
    # exact-Fock variant (exchange.exactFockSlab): e_x^exact = -(lambda/c)(n^2 + S^2 - Q^2 - Y^2), Y = 0, so it exceeds
    # the uniform-gas e_x = -(lambda/32)(n^2 + S^2) by +(lambda/c) Q^2; the variant adds w_Q = +lambda Q/d sigma3
    fk = ex["exactFockSlab"]
    m1 = re.search(r"e_x\^exact = -\(lambda/(\d+)\)\(n\^2 \+ S\^2 - Q\^2 - Y\^2\)", fk["result"])
    m2 = re.search(r"w_Q = \+lambda Q/(\d+) sigma3", fk["status"])
    m3 = re.search(r"\+\(lambda/(\d+)\) Q\^2 to e_int", fk["status"])
    cQ2 = Fraction(1, int(m1.group(1))) if m1 else None
    cWQ = Fraction(1, int(m2.group(1))) if m2 else None
    cQ2_status = Fraction(1, int(m3.group(1))) if m3 else None
    return {
        "sha256": hashlib.sha256(KS_THEORY.read_bytes()).hexdigest(),
        "cM": cM, "cV": cV, "cn2": cn2, "cs2": cs2,
        # e_int = lambda[(1/2 + c_S2) S^2 + c_n2 n^2] (Hartree (lambda/2) S^2 plus the uniform-gas exchange)
        "eS2": Fraction(1, 2) + cs2, "eN2": cn2,
        "cQ2": cQ2, "cWQ": cWQ, "cQ2_status": cQ2_status,
        "slope_theory_a0": slope,
    }


def make_phys(co, **kw):
    p = K.Phys(**BASE, cM=float(co["cM"]), cV=float(co["cV"]), cS2=float(co["eS2"]), cN2=float(co["eN2"]),
               cQ2=float(co["cQ2"]) if co["cQ2"] is not None else float("nan"))
    for k, v in kw.items():
        setattr(p, k, v)
    return p


def slope_formula(a4, M=1.0, H=1.0, L=3.0):
    """ks-theory.json checksNumeric.braneBandSlopeFormula."""
    return math.exp(-a4) * (2 * M / (2 * M - H)) * (1 - math.exp(-(2 * M - H) * L)) / (1 - math.exp(-2 * M * L))


# ------------------------------------------------------------------------------------------------
# job: free-field checks of the reference itself
# ------------------------------------------------------------------------------------------------
def _odd_roots(M, L, nr):
    out = []
    for l in range(nr):
        lo, hi = (l + 0.5) * math.pi / L, (l + 1) * math.pi / L
        f = lambda p: M * math.sin(p * L) + p * math.cos(p * L)   # tan(pL) = -p/M
        flo = f(lo)
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            fm = f(mid)
            if (fm > 0) == (flo > 0):
                lo, flo = mid, fm
            else:
                hi = mid
        out.append(0.5 * (lo + hi))
    return out


def _analytic(M, L, odd, r):
    """ks-theory.json boundaryConditions.exactK0Spectra (k = 0, constant M, v = 0, theta_tip = 0)."""
    if not odd:
        if r == 0:
            return 0.0
        return math.copysign(math.sqrt(M * M + (abs(r) * math.pi / L) ** 2), r)
    p = _odd_roots(M, L, 12)
    return math.sqrt(M * M + p[r] ** 2) if r >= 0 else -math.sqrt(M * M + p[-r - 1] ** 2)


def free_checks_job(co):
    t0 = time.time()
    out = {}
    # (1) analytic k = 0 spectra, both parities and block types, five grids
    rows = []
    errs = {G: [] for G in (150, 300, 600, 1200, 2400)}
    rerr, ratios, jsym = [], [], 0.0
    ranks = list(range(-3, 6))
    for (M, L) in ((1.0, 3.0), (1.0, 2.0), (2.0, 3.0)):
        ph = make_phys(co, m=M, L=L)
        sec = K.Sectors([(0, 1, j, odd) for (j, odd) in K.SECTOR_ORDER])
        vals = {}
        for G in (150, 300, 600, 1200, 2400):
            g = K.Grid(ph, G)
            imin, al, be = K.particle_offsets(g, ph, sec)
            ls_sec = np.repeat(np.arange(4), len(ranks))
            idx = imin[ls_sec] + np.tile(ranks, 4)
            eps, _ = K.eigen(al[:, ls_sec], be[:, ls_sec], idx)
            vals[G] = eps
            jsym = max(jsym, float(np.max(np.abs(eps[:2 * len(ranks)] - eps[2 * len(ranks):]))))
        exact = np.array([_analytic(M, L, bool(sec.odd[s]), r) for s in range(4) for r in ranks])
        R, U = rich3(vals[300], vals[600], vals[1200])
        for G in errs:
            errs[G].append(np.abs(vals[G] - exact))
        rerr.append(np.abs(R - exact))
        ratios += asym_ratio(vals[300], vals[600], vals[1200])
        for i, (s, r) in enumerate([(s, r) for s in range(4) for r in ranks]):
            rows.append([f16(M), f16(L), "odd" if sec.odd[s] else "even", int(sec.j[s]), r, f16(R[i]), f16(U[i]),
                         f16(exact[i]), f16(R[i] - exact[i]), f16(vals[1200][i] - exact[i])])
    out["analytic"] = {
        "rows_header": ["m", "L", "parity", "j", "rank", "eps_richardson", "U", "eps_analytic", "richardson_minus_analytic", "G1200_minus_analytic"],
        "rows": rows,
        "max_error_per_grid": {str(G): float(np.max(np.concatenate(errs[G]))) for G in errs},
        "max_error_richardson": float(np.max(np.concatenate(rerr))),
        "max_U": max(float(r[6]) for r in rows),
        "ratio_median": float(np.median(ratios)), "ratio_min": float(np.min(ratios)), "ratio_max": float(np.max(ratios)),
        "jsym_max": jsym,
    }
    # (2) the k = 0 brane zero mode (M = H = 1, L = 3)
    ph = make_phys(co)
    zm = {}
    for G in GRIDS:
        g = K.Grid(ph, G)
        sec = K.Sectors([(0, 1, 1, 0), (0, 1, -1, 0)])
        imin, al, be = K.particle_offsets(g, ph, sec)
        eps, Z = K.eigen(al, be, imin)
        a, b = K.orbitals_ext(g, Z, sec.j, sec.odd)
        ri = g.report_indices()
        sign = np.sign(a[ri][-1])
        zm[G] = {"eps": eps, "a": a[ri] * sign, "wmax": float(np.max(np.abs(Z[1::2]))), "umax": float(np.max(np.abs(Z[0::2])))}
    ya = -3.0 + 0.02 * np.arange(151)
    a_exact = math.sqrt(2.0 / (1.0 - math.exp(-6.0))) * np.exp(ya)
    Ra, Ua = rich3(zm[300]["a"][:, 0], zm[600]["a"][:, 0], zm[1200]["a"][:, 0])
    out["zero_mode"] = {
        "max_abs_eps": max(float(np.max(np.abs(zm[G]["eps"]))) for G in GRIDS),
        "max_w_over_u": max(zm[G]["wmax"] / zm[G]["umax"] for G in GRIDS),
        "profile_richardson_max_error": float(np.max(np.abs(Ra - a_exact))),
        "profile_richardson_max_U": float(np.max(Ua)),
        "jsym_profile": max(float(np.max(np.abs(zm[G]["a"][:, 0] - zm[G]["a"][:, 1]))) for G in GRIDS),
    }
    # (3) brane-band slope d eps/dk at k = 0 (discrete Hellmann-Feynman, exact for the discrete matrix)
    srows = []
    sl = {}
    for G in GRIDS:
        g = K.Grid(ph, G)
        sec = K.Sectors([(0, 1, 1, 0)])
        imin, al, be = K.particle_offsets(g, ph, sec)
        eps, Z = K.eigen(al, be, imin)
        zu2 = Z[0::2, 0] ** 2
        sl[G] = [float(np.sum(np.exp(-g.y[0::2] - a4) * zu2)) for a4 in SLICES]
    Rs, Us = rich3(sl[300], sl[600], sl[1200])
    for i, a4 in enumerate(SLICES):
        c = slope_formula(a4)
        srows.append([f16(a4), f16(Rs[i]), f16(Us[i]), f16(c), f16((Rs[i] - c) / c)])
    out["brane_band_slope"] = {
        "rows_header": ["a4", "slope_richardson", "U", "slope_formula", "relative_difference"],
        "rows": srows,
        "max_rel": max(abs(float(r[4])) for r in srows),
        "formula_vs_theory_number": abs(slope_formula(0.0) - co["slope_theory_a0"]) / co["slope_theory_a0"],
    }
    # (4) particle branch split by the sign of the free levels (shells n2 <= 30, every slice)
    closest, bad = np.inf, 0
    for a4 in SLICES:
        p = make_phys(co, a4=a4)
        g = K.Grid(p, 300)
        sec = K.shell_sectors(K.shells(30))
        imin, al, be = K.particle_offsets(g, p, sec)
        e_hi, _ = K.eigen(al, be, imin)
        e_lo, _ = K.eigen(al, be, imin - 1)
        zero = (sec.n2 == 0) & (~sec.odd)
        bad += int(np.sum(e_lo >= 0)) + int(np.sum((e_hi <= 0) & ~zero)) + int(np.sum(np.abs(e_hi[zero]) > 1e-12))
        nz = np.concatenate([np.abs(e_hi[~zero]), np.abs(e_lo)])
        closest = min(closest, float(nz.min()))
    out["particle_branch"] = {"violations": bad, "closest_to_zero_away_from_zero_modes": closest}
    return {"kind": "free", "data": out, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: particle numbers and coupling calibration (re-derived from the stated rules)
# ------------------------------------------------------------------------------------------------
def parameters_job(co):
    t0 = time.time()
    out = {}
    # bulk edge and closed shells of the free a4,0 = 0 aufbau
    per_grid = {}
    for G in GRIDS:
        ph = make_phys(co, a4=0.0)
        g = K.Grid(ph, G)
        sec = K.Sectors([(0, 1, 1, 0), (0, 1, 1, 1)])
        imin, al, be = K.particle_offsets(g, ph, sec)
        e, _ = K.eigen(al, be, np.array([imin[0] + 1, imin[1]]))
        edge = float(min(e))
        scan = K.ShellScan(g, ph)
        c = scan.shells_below(edge)
        secs = K.shell_sectors(scan.sh[:c])
        imin, al, be = K.particle_offsets(g, ph, secs)
        ls_sec, ls_idx, ls_rank = K.free_levels_below(g, ph, secs, imin, edge - 1e-9, al, be)
        ls_sec = np.array(ls_sec)
        eps, _ = K.eigen(al[:, ls_sec], be[:, ls_sec], np.array(ls_idx))
        ls = K.LevelSet(secs, ls_sec, ls_idx, ls_rank, imin)
        grs = K.groups(eps, ls.order_key())
        cum, closed = 0.0, []
        keys = ls.keys()
        for i, gidx in enumerate(grs):
            cum += float(np.sum(ls.deg[gidx]))
            e_next = float(eps[grs[i + 1][0]]) if i + 1 < len(grs) else edge
            closed.append({"N": cum, "eps_last": float(eps[gidx[0]]), "eps_next": e_next,
                           "group": ";".join(key_str(keys[k]) for k in sorted(gidx, key=lambda k: keys[k]))})
        per_grid[G] = {"edge": edge, "closed": closed}
    Ns = [[c["N"] for c in per_grid[G]["closed"]] for G in GRIDS]
    same = all(x == Ns[0] for x in Ns)
    redge, uedge = rich3(*[per_grid[G]["edge"] for G in GRIDS])
    closed = []
    for i, c in enumerate(per_grid[GRIDS[-1]]["closed"]):
        Rl, Ul = rich3(*[per_grid[G]["closed"][i]["eps_last"] for G in GRIDS])
        Rn, Un = rich3(*[per_grid[G]["closed"][i]["eps_next"] for G in GRIDS])
        closed.append({"N": c["N"], "eps_last": float(Rl), "U_last": float(Ul), "eps_next": float(Rn), "U_next": float(Un), "group": c["group"]})
    below = [c for c in closed if c["eps_last"] < float(redge)]
    n_large = max(c["N"] for c in below)
    cand = [c["N"] for c in below if c["N"] >= 8]
    n_mid = min(cand, key=lambda x: (abs(x - n_large / 4.0), x))
    out["bulk_edge"] = {"value": float(redge), "U": float(uedge)}
    out["closed_shells_a0"] = closed
    out["closed_shells_same_on_all_grids"] = same
    out["N_large"], out["N_mid"] = n_large, n_mid
    out["N_mid_distance_rule"] = sorted([[c, abs(c - n_large / 4.0)] for c in cand], key=lambda t: t[1])[:4]
    # the N of the crossing demonstration: the smallest closed shell N > 8 of the free a4,0 = 0 aufbau (levels up to
    # CROSSING_EMAX) whose last group holds a level off the even j = +1 brane band (rank 0 of the (n2, +1, even) sectors)
    demo = {}
    for G in GRIDS:
        ph = make_phys(co, a4=0.0)
        g = K.Grid(ph, G)
        scan = K.ShellScan(g, ph)
        c = scan.shells_below(CROSSING_EMAX)
        secs = K.shell_sectors(scan.sh[:c])
        imin, al, be = K.particle_offsets(g, ph, secs)
        ls_sec, ls_idx, ls_rank = K.free_levels_below(g, ph, secs, imin, CROSSING_EMAX, al, be)
        ls_sec = np.array(ls_sec)
        eps, _ = K.eigen(al[:, ls_sec], be[:, ls_sec], np.array(ls_idx))
        ls = K.LevelSet(secs, ls_sec, ls_idx, ls_rank, imin)
        keys = ls.keys()
        cum, rows = 0.0, []
        for gidx in K.groups(eps, ls.order_key()):
            cum += float(np.sum(ls.deg[gidx]))
            names = sorted(key_str(keys[k]) for k in gidx)
            off_band = any(not (keys[k][1] == 1 and keys[k][2] == "even" and keys[k][3] == 0) for k in gidx)
            rows.append({"N": cum, "eps": float(eps[gidx[0]]), "group": ";".join(names), "off_brane_band": off_band})
        demo[G] = rows
    n_demo = [next((r["N"] for r in demo[G] if r["N"] > 8.0 and r["off_brane_band"]), None) for G in GRIDS]
    out["crossing_demo"] = {"emax": CROSSING_EMAX, "N_demo": n_demo[-1], "same_on_all_grids": len(set(n_demo)) == 1,
                            "closed_shells": [{"N": r["N"], "eps_G1200": r["eps"], "group": r["group"], "off_brane_band": r["off_brane_band"]}
                                              for r in demo[GRIDS[-1]] if r["N"] <= (n_demo[-1] or 0.0) + 1e-9]}
    # calibration: strength = max over slices and y of max(cM |S|, |cV| |n|) of the free ground states
    cal = []
    for N in (8.0, n_mid, n_large):
        per_slice = []
        for a4 in SLICES:
            ph = make_phys(co, a4=a4, N=N)
            g0 = K.Grid(ph, GRIDS[0])
            ls0, _ = K.build_window(g0, ph, 0.0)
            vals, locs, curvs = [], [], []
            for G in GRIDS:
                g = K.Grid(ph, G)
                ls = K.relabel(g, ph, ls0)
                st = K.solve_state(g, ph, ls)
                # nodes only (ext even indices, spacing h): the half-node and node values carry different
                # O(h^2) error constants, so the maximum is taken over one position type
                prof = np.maximum(abs(ph.cM) * np.abs(st.dens.S), abs(ph.cV) * np.abs(st.dens.n))[0::2]
                yn = g.yext[0::2]
                i = int(np.argmax(prof))
                if 2 <= i <= len(prof) - 3:
                    # continuous maximum: quartic through the five nodes around the discrete maximum
                    # (interpolation error O(h^5), far below the O(h^2) discretisation error), maximised
                    # by Newton on its derivative in t = (y - y_i)/h
                    c = np.polyfit(np.arange(-2.0, 3.0), prof[i - 2:i + 3], 4)
                    dc, ddc = np.polyder(c), np.polyder(c, 2)
                    t = 0.0
                    for _ in range(50):
                        t -= np.polyval(dc, t) / np.polyval(ddc, t)
                    t = min(max(t, -1.0), 1.0)
                    peak, ypk = float(np.polyval(c, t)), float(yn[i] + t * g.h)
                    curv = float(np.polyval(ddc, t)) / g.h ** 2
                else:
                    peak, ypk, curv = prof[i], yn[i], 0.0
                vals.append(float(peak))
                locs.append(float(ypk))
                curvs.append(curv)
            R, U = rich3(*vals)
            per_slice.append({"a4": a4, "strength": float(R), "U": float(U), "argmax_y": locs,
                              "peak_interior": bool(curvs[-1] != 0.0), "curvature_at_peak": float(curvs[-1])})
        s = max(per_slice, key=lambda d: d["strength"])
        lam1u, lam2u = 0.1 / s["strength"], 0.3 / s["strength"]
        lam1, lam2 = round_sig(lam1u), round_sig(lam2u)

        def margin(x):
            # relative distance of the unrounded value to the nearest rounding boundary of 4 digits
            e = math.floor(math.log10(abs(x))) - 3
            q = x / 10.0 ** e
            return abs(q - math.floor(q) - 0.5) / q

        cal.append({"N": N, "per_slice": per_slice, "strength": s["strength"], "U": s["U"],
                    "lambda1_unrounded": lam1u, "lambda2_unrounded": lam2u, "lambda1": lam1, "lambda2": lam2,
                    "rounding_margin_rel": min(margin(lam1u), margin(lam2u)),
                    "strength_rel_U": s["U"] / s["strength"]})
    out["calibration"] = cal
    return {"kind": "parameters", "data": out, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: one ground state of the subset on every grid (plus Delta-SCF, a4 neighbours, adiabaticity)
# ------------------------------------------------------------------------------------------------
def _ground_on_grid(co, spec, G, ls0):
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"])
    g = K.Grid(ph, G)
    ls = K.relabel(g, ph, ls0)
    free = K.solve_state(g, ph.copy(lam=0.0), ls)
    gs = free if ph.lam == 0.0 else K.solve_state(g, ph, ls, guess=free.eps)
    o, prof = K.observables(gs)
    homo, lumo, hg, lg = K.homo_lumo(gs)
    o["HOMO"], o["LUMO"], o["KS_gap"] = homo, lumo, lumo - homo
    o["lowest_excluded"] = K.lowest_excluded(g, ph, ls, gs.dM, gs.v)
    o["max_abs_Meff_minus_m"] = float(np.max(np.abs(prof["M_eff"] - ph.m)))
    o["max_abs_v_v"] = float(np.max(np.abs(prof["v_v"])))
    o["n_max"] = float(np.max(np.abs(prof["n"])))
    rec = {"G": G, "iterations": gs.iters, "residual": gs.res, "open_shell": gs.open_shell}
    keys = ls.keys()
    rec["homo_group"] = sorted(key_str(keys[i]) for i in hg)
    rec["lumo_group"] = sorted(key_str(keys[i]) for i in lg)
    # Delta-SCF: one particle from the HOMO group to the LUMO group, uniform over each group
    fx = gs.f.copy()
    fx[hg] -= 1.0 / float(np.sum(ls.deg[hg]))
    fx[lg] += 1.0 / float(np.sum(ls.deg[lg]))
    ex = K.solve_state(g, ph, ls, mode="fixed", fixed=fx, start=(gs.dM, gs.v), guess=gs.eps)
    oex, _ = K.observables(ex)
    o["E_excited"] = oex["E_KS"]
    o["delta_SCF"] = oex["E_KS"] - o["E_KS"]
    rec["excited_iterations"], rec["excited_residual"] = ex.iters, ex.res
    # a4 neighbours at fixed occupations (self-consistent), Richardson differences
    nb = []
    for s in (1.0, -1.0, 2.0, -2.0):
        p = ph.copy(a4=ph.a4 + s * FD_DELTA)
        st = K.solve_state(g, p, ls, mode="fixed", fixed=gs.f, start=(gs.dM, gs.v), guess=gs.eps)
        nb.append((K.observables(st)[0]["E_KS"], st.dM, st.v, st.eps, st.iters, st.res))
    rec["neighbour_iterations"] = [x[4] for x in nb]
    rec["neighbour_residual_max"] = max(x[5] for x in nb)
    o["dE_da4_fd"] = float(rich_fd(nb[0][0], nb[1][0], nb[2][0], nb[3][0], FD_DELTA))
    dM = rich_fd(nb[0][1], nb[1][1], nb[2][1], nb[3][1], FD_DELTA)
    dv = rich_fd(nb[0][2], nb[1][2], nb[2][2], nb[3][2], FD_DELTA)
    deps = rich_fd(nb[0][3], nb[1][3], nb[2][3], nb[3][3], FD_DELTA)
    dal, dbe = K.sector_derivative_arrays(g, ph, gs.sec_u, dM, dv)
    B = len(gs.eps)
    hf = K.matrix_elements(gs, dal, dbe, [(i, i) for i in range(B)])
    rec["hellmann_feynman_maxdev"] = float(np.max(np.abs(deps - hf)))
    o["max_abs_deps_da4"] = float(np.max(np.abs(deps)))
    # adiabaticity pairs: n occupied, m not full, same sector, rank_m <= PAD_RANKS
    occ = np.nonzero(gs.f > 1e-12)[0]
    pairs = []
    for p in occ:
        same = np.nonzero((ls.lev_sec == ls.lev_sec[p]) & (gs.f < 1.0 - 1e-12) & (ls.lev_rank <= PAD_RANKS))[0]
        pairs += [(int(p), int(q)) for q in same if q != p]
    me = K.matrix_elements(gs, dal, dbe, pairs) if pairs else np.zeros(0)
    de = np.array([gs.eps[p] - gs.eps[q] for (p, q) in pairs]) if pairs else np.zeros(0)
    Q = np.abs(me) / de ** 2 if pairs else np.zeros(0)
    rec["occupations"] = gs.f
    ri = g.report_indices()
    return {"rec": rec, "scalars": o, "eps": gs.eps, "Q": Q, "me": np.abs(me), "de": np.abs(de), "pairs": pairs,
            "keys": keys, "f": gs.f, "profiles": {k: prof[k][ri] for k in PROFILE_NAMES}, "hf": hf, "deps": deps,
            "deg": ls.deg, "okey": ls.order_key()}


def particle_hole_list(keys, eps_g, f, deg, okey, ecut, Re, Ue, rows):
    """The lowest particle-hole excitations between degenerate groups (the degenerate groups from the finest grid;
    energies and the cut from the Richardson values): hole groups hold particles (sum f g > 1e-12), particle groups
    lie above the hole group and below the lowest level outside the label set (ecut, Richardson) and have
    vacancies; sorted by delta_eps.  Returns at most `rows` entries."""
    grs = K.groups(eps_g, okey)
    out = []
    for gh in grs:
        fh = float(np.sum(f[gh] * deg[gh]))
        if fh <= 1e-12:
            continue
        for gp in grs:
            ep = float(Re[gp[0]])
            if not (ep < ecut and ep > float(Re[gh[0]])):
                continue
            gpv = float(np.sum((1.0 - f[gp]) * deg[gp]))
            if gpv <= 1e-12:
                continue
            same = any(keys[a][:3] == keys[b][:3] for a in gh for b in gp)
            hole = ";".join(sorted(key_str(keys[i]) for i in gh))
            part = ";".join(sorted(key_str(keys[i]) for i in gp))
            de = float(Re[gp[0]] - Re[gh[0]])
            out.append({"hole": hole, "particle": part, "eps_hole": float(Re[gh[0]]), "eps_particle": float(Re[gp[0]]),
                        "delta_eps": de, "U_delta_eps": float(Ue[gp[0]] + Ue[gh[0]]), "multiplicity": fh * gpv,
                        "same_sector": bool(same)})
    out.sort(key=lambda r: (r["delta_eps"], r["hole"], r["particle"]))
    return out[:rows]


def ground_job(co, spec, grids=GRIDS, full=True):
    t0 = time.time()
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"])
    g0 = K.Grid(ph, grids[0])
    ls0, winfo = K.build_window(g0, ph, spec["sigma"], pad_ranks=PAD_RANKS)
    runs = [_ground_on_grid(co, spec, G, ls0) for G in grids]
    keys = runs[0]["keys"]
    out = {"id": spec["id"], "N": spec["N"], "lambda_tag": spec["tag"], "lambda": spec["lam"], "a4": spec["a4"],
           "grids": list(grids), "window": winfo, "levels_in_set": len(keys),
           "shells_in_set": len(set(k[0] for k in keys))}
    out["per_grid"] = [r["rec"] | {"scalars": r["scalars"]} for r in runs]
    for r in out["per_grid"]:
        r.pop("occupations")
    sel = runs[-3:]                                  # Richardson over the last three grids
    sc = {}
    for k in runs[0]["scalars"]:
        R, U = rich3(*[r["scalars"][k] for r in sel])
        sc[k] = {"value": float(R), "U": float(U)}
    out["scalars"] = sc
    Re, Ue = rich3(*[r["eps"] for r in sel])
    out["levels"] = {"columns": ["n2", "j", "parity", "rank"], "keys": [list(k) for k in keys],
                     "eps": Re, "U": Ue, "f": runs[-1]["f"]}
    out["profiles"] = {"y": (-3.0 + 0.02 * np.arange(151)).tolist()}
    for nm in PROFILE_NAMES:
        R, U = rich3(*[r["profiles"][nm] for r in sel])
        out["profiles"][nm] = {"value": R, "U": U}
    # adiabaticity
    pairs = runs[-1]["pairs"]
    if pairs:
        RQ, UQ = rich3(*[r["Q"] for r in sel])
        order = np.argsort(-RQ, kind="stable")[:10]
        RM, UM = rich3(*[r["me"] for r in sel])
        RD, UD = rich3(*[r["de"] for r in sel])
        out["adiabatic"] = {"pairs_considered": len(pairs), "Q_max": float(RQ[order[0]]), "U_Q_max": float(UQ[order[0]]),
                            "top": [{"hole": key_str(keys[pairs[i][0]]), "particle": key_str(keys[pairs[i][1]]),
                                     "Q": float(RQ[i]), "U": float(UQ[i]),
                                     "matrix_element": float(RM[i]), "U_matrix_element": float(UM[i]),
                                     "delta_eps": float(RD[i]), "U_delta_eps": float(UD[i])} for i in order]}
    else:
        out["adiabatic"] = {"pairs_considered": 0, "Q_max": 0.0, "U_Q_max": 0.0, "top": []}
    # grid consistency and asymptotic ratios
    out["consistency"] = {
        "same_occupations_all_grids": all(np.array_equal(r["f"], runs[0]["f"]) for r in runs),
        "same_homo_lumo_groups_all_grids": all(r["rec"]["homo_group"] == runs[0]["rec"]["homo_group"] and
                                               r["rec"]["lumo_group"] == runs[0]["rec"]["lumo_group"] for r in runs),
        "ratio_eps": asym_ratio(*[r["eps"] for r in sel]),
        "ratio_E_KS": asym_ratio(*[r["scalars"]["E_KS"] for r in sel], floor=1e-11),
    }
    rr = out["consistency"]["ratio_eps"]
    out["consistency"]["ratio_eps"] = {"count": len(rr), "median": float(np.median(rr)) if rr else None,
                                       "min": float(np.min(rr)) if rr else None, "max": float(np.max(rr)) if rr else None}
    out["homo_group"] = runs[-1]["rec"]["homo_group"]
    out["lumo_group"] = runs[-1]["rec"]["lumo_group"]
    # particle-hole list (finest-grid degenerate groups; Richardson energies and cut)
    fin = runs[-1]
    ecut = sc["lowest_excluded"]["value"]
    out["particle_hole"] = {"rows_kept": PH_ROWS, "cut_lowest_excluded": ecut,
                            "list": particle_hole_list(keys, fin["eps"], fin["f"], fin["deg"], fin["okey"], ecut, Re, Ue, PH_ROWS)}
    return {"kind": "ground", "id": spec["id"], "data": out, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: the exact-Fock-exchange VARIANT of a ground state (lambda != 0), self-consistent on every grid
# ------------------------------------------------------------------------------------------------
def exx_job(co, spec):
    t0 = time.time()
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"])
    g0 = K.Grid(ph, GRIDS[0])
    ls0, _ = K.build_window(g0, ph, spec["sigma"], pad_ranks=PAD_RANKS)
    per = []
    for G in GRIDS:
        g = K.Grid(ph, G)
        ls = K.relabel(g, ph, ls0)
        free = K.solve_state(g, ph.copy(lam=0.0), ls)
        gs = K.solve_state(g, ph, ls, guess=free.eps)
        olda, _ = K.observables(gs)
        px = ph.copy(exx=True)
        # started from the converged uniform-gas state (w_Q = 0), as in the Rust canonical matrix
        sx = K.solve_state(g, px, ls, start=(gs.dM, gs.v, np.zeros(g.n)), guess=gs.eps)
        ox, _ = K.observables(sx)
        h, l, _, _ = K.homo_lumo(sx)
        sc = {"E_exact_fock_scf": ox["E_KS"], "E_uniform_gas": olda["E_KS"], "deltaE_x_exact_fock": olda["deltaE_x_exact_fock"],
              "E_uniform_gas_plus_deltaE_x": olda["E_KS"] + olda["deltaE_x_exact_fock"],
              "E_exx_minus_first_order": ox["E_KS"] - olda["E_KS"] - olda["deltaE_x_exact_fock"],
              "HOMO_exact_fock": h, "LUMO_exact_fock": l, "gap_exact_fock": l - h,
              "int_rho": ox["int_rho"], "E_variational": ox["E_variational"], "ycons_jump": ox["ycons_jump"],
              "ycons_integral": ox["ycons_integral"], "p8_tip": ox["p8_tip"], "p8_brane": ox["p8_brane"], "N_sum": ox["N_sum"],
              "max_abs_wQ": float(np.max(np.abs(sx.wq)))}
        per.append({"G": G, "iterations": sx.iters, "residual": sx.res, "uniform_gas_residual": gs.res,
                    "same_occupations_as_uniform_gas": bool(np.array_equal(sx.f, gs.f)), "open_shell": sx.open_shell, "scalars": sc})
    out = {"id": spec["id"], "N": spec["N"], "lambda_tag": spec["tag"], "lambda": spec["lam"], "a4": spec["a4"], "grids": list(GRIDS),
           "per_grid": per, "scalars": {}}
    for k in per[0]["scalars"]:
        R, U = rich3(*[p["scalars"][k] for p in per])
        out["scalars"][k] = {"value": float(R), "U": float(U)}
    return {"kind": "exx", "id": spec["id"], "data": out, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: the rescaling partner KS(0; dk e^{-a4,0}, v_t e^{-3 a4,0}, lambda) of a ground state (a4,0 > 0)
# ------------------------------------------------------------------------------------------------
def rescale_job(co, spec):
    t0 = time.time()
    a4 = spec["a4"]
    pr = make_phys(co, a4=0.0, lam=spec["lam"], N=spec["N"], dk=BASE["dk"] * math.exp(-a4), vt=BASE["vt"] * math.exp(-3.0 * a4))
    g0 = K.Grid(pr, GRIDS[0])
    ls0, _ = K.build_window(g0, pr, spec["sigma"], pad_ranks=PAD_RANKS)
    runs = []
    for G in GRIDS:
        g = K.Grid(pr, G)
        ls = K.relabel(g, pr, ls0)
        free = K.solve_state(g, pr.copy(lam=0.0), ls)
        st = free if pr.lam == 0.0 else K.solve_state(g, pr, ls, guess=free.eps)
        o, prof = K.observables(st)
        ri = g.report_indices()
        runs.append({"G": G, "iterations": st.iters, "residual": st.res, "E_KS": o["E_KS"], "eps": st.eps, "f": st.f,
                     "profiles": {k: prof[k][ri] for k in ("n", "S", "rho", "p3", "p8")}})
    keys = ls0.keys()
    R, U = rich3(*[r["E_KS"] for r in runs])
    Re, Ue = rich3(*[r["eps"] for r in runs])
    out = {"id": spec["id"], "N": spec["N"], "lambda_tag": spec["tag"], "lambda": spec["lam"], "a4": a4,
           "partner_dk": pr.dk, "partner_v_t": pr.vt, "grids": list(GRIDS),
           "per_grid": [{"G": r["G"], "iterations": r["iterations"], "residual": r["residual"], "E_KS": r["E_KS"]} for r in runs],
           "E_KS": {"value": float(R), "U": float(U)},
           "levels": {"keys": [list(k) for k in keys], "eps": Re, "U": Ue, "f": runs[-1]["f"]},
           "same_occupations_all_grids": all(np.array_equal(r["f"], runs[0]["f"]) for r in runs),
           "profiles": {}}
    for nm in ("n", "S", "rho", "p3", "p8"):
        Rp, Up = rich3(*[r["profiles"][nm] for r in runs])
        out["profiles"][nm] = {"value": Rp, "U": Up}
    return {"kind": "rescale", "id": spec["id"], "data": out, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: crossing demonstration (lambda = 0, N = N_demo): instantaneous aufbau vs the adiabatically continued state
# ------------------------------------------------------------------------------------------------
def with_keys(grid, phys, ls: K.LevelSet, keys):
    """The label set ls extended by the given level keys (n2, j, parity, rank), adding sectors where needed."""
    items = list(ls.sec.items)
    lev_sec, lev_rank = [int(x) for x in ls.lev_sec], [int(x) for x in ls.lev_rank]
    present = set(ls.keys())
    r3 = dict(K.shells(max(k[0] for k in keys) + 1))
    for k in keys:
        if tuple(k) in present:
            continue
        n2, jj, par, rank = int(k[0]), int(k[1]), k[2], int(k[3])
        odd = 1 if par == "odd" else 0
        s = next((i for i, it in enumerate(items) if it[0] == n2 and int(it[2]) == jj and int(it[3]) == odd), None)
        if s is None:
            items.append((n2, r3[n2], jj, odd))
            s = len(items) - 1
        lev_sec.append(s)
        lev_rank.append(rank)
    sec = K.Sectors(items)
    imin = K.particle_offsets_chunked(grid, phys.copy(lam=0.0), sec)
    lev_sec = np.array(lev_sec, dtype=np.int64)
    lev_rank = np.array(lev_rank, dtype=np.int64)
    return K.LevelSet(sec, lev_sec, imin[lev_sec] + lev_rank, lev_rank, imin)


def crossing_job(co, n_demo):
    t0 = time.time()
    # a4,0 = 0: the occupation that is continued adiabatically
    ph0 = make_phys(co, a4=0.0, N=n_demo)
    ls00, _ = K.build_window(K.Grid(ph0, GRIDS[0]), ph0, 0.0, pad_ranks=PAD_RANKS)
    occ0_per_grid = []
    for G in GRIDS:
        g = K.Grid(ph0, G)
        st = K.solve_state(g, ph0, K.relabel(g, ph0, ls00))
        kk = ls00.keys()
        occ0_per_grid.append({kk[i]: float(st.f[i]) for i in range(len(kk)) if st.f[i] > 0.0})
    occ0 = occ0_per_grid[-1]
    rows = []
    for a4 in SLICES:
        ph = make_phys(co, a4=a4, N=n_demo)
        g0 = K.Grid(ph, GRIDS[0])
        lsw, _ = K.build_window(g0, ph, 0.0, pad_ranks=PAD_RANKS)
        ls0 = with_keys(g0, ph, lsw, sorted(occ0))
        keys = ls0.keys()
        fc = np.array([occ0.get(k, 0.0) for k in keys])
        per = []
        for G in GRIDS:
            g = K.Grid(ph, G)
            ls = K.relabel(g, ph, ls0)
            st = K.solve_state(g, ph, ls)
            cont = K.solve_state(g, ph, ls, mode="fixed", fixed=fc)
            occ = {keys[i]: float(st.f[i]) for i in range(len(keys)) if st.f[i] > 0.0}
            per.append({"G": G, "E_aufbau": K.observables(st)[0]["E_KS"], "E_continued": K.observables(cont)[0]["E_KS"],
                        "open_shell": bool(st.open_shell), "occ": occ, "N_cont": float(np.sum(ls.deg * fc))})
        occf = per[-1]["occ"]
        Ra, Ua = rich3(*[p["E_aufbau"] for p in per])
        Rc, Uc = rich3(*[p["E_continued"] for p in per])
        Rd, Ud = rich3(*[p["E_continued"] - p["E_aufbau"] for p in per])
        rows.append({"a4": a4, "occupied_set_equal_to_a4_0": occf == occ0,
                     "occupied_labels_same_on_all_grids": all(set(p["occ"]) == set(occf) for p in per),
                     "occupations_same_on_all_grids": all(p["occ"] == occf for p in per),
                     "open_shell": per[-1]["open_shell"], "open_shell_all_grids": [p["open_shell"] for p in per],
                     "E_aufbau": {"value": float(Ra), "U": float(Ua)}, "E_adiabatically_continued": {"value": float(Rc), "U": float(Uc)},
                     "difference": {"value": float(Rd), "U": float(Ud)},
                     "labels_left": sorted(key_str(k) for k in occ0 if k not in occf),
                     "labels_entered": sorted(key_str(k) for k in occf if k not in occ0),
                     "N_continued": per[-1]["N_cont"]})
    out = {"N_demo": n_demo, "grids": list(GRIDS), "occupation_a4_0": {key_str(k): v for k, v in sorted(occ0.items())},
           "occupation_a4_0_same_on_all_grids": all(o == occ0 for o in occ0_per_grid), "rows": rows}
    return {"kind": "crossing", "id": "", "data": out, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: validation of the uncertainty estimate on a fourth grid
# ------------------------------------------------------------------------------------------------
def validation_job(co, spec):
    t0 = time.time()
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"])
    g0 = K.Grid(ph, G_VALID[0])
    ls0, _ = K.build_window(g0, ph, spec["sigma"], pad_ranks=PAD_RANKS)
    vals = []
    for G in G_VALID:
        g = K.Grid(ph, G)
        ls = K.relabel(g, ph, ls0)
        free = K.solve_state(g, ph.copy(lam=0.0), ls)
        st = K.solve_state(g, ph, ls, guess=free.eps)
        o, prof = K.observables(st)
        h, l, _, _ = K.homo_lumo(st)
        o["HOMO"], o["LUMO"] = h, l
        ri = g.report_indices()
        vals.append({"o": o, "eps": st.eps, "prof": {k: prof[k][ri] for k in PROFILE_NAMES}})
    res = {"id": spec["id"], "grids": list(G_VALID), "classes": {}}

    def comp(name, x):
        R1, U1 = rich3(x[0], x[1], x[2])
        R2, U2 = rich3(x[1], x[2], x[3])
        d = np.abs(np.atleast_1d(R1 - R2))
        U1 = np.atleast_1d(U1)
        res["classes"][name] = {"elements": int(d.size), "max_abs_R123_minus_R234": float(d.max()),
                                "max_ratio_to_U123": float(np.max(d / U1)), "all_within_U123": bool(np.all(d <= U1)),
                                "max_U123": float(U1.max()), "max_U234": float(np.max(U2))}

    for k in ("E_KS", "E_int", "HOMO", "LUMO", "int_rho", "int_p3", "int_p8", "dE_da4_emt", "deltaE_x_exact_fock",
              "rho_tip", "p8_tip", "rho_brane", "p8_brane"):
        comp(k, [v["o"][k] for v in vals])
    comp("eigenvalues", [v["eps"] for v in vals])
    for k in ("n", "S", "rho", "p3", "p8"):
        comp("profile_" + k, [v["prof"][k] for v in vals])
    return {"kind": "validation", "id": spec["id"], "data": res, "seconds": time.time() - t0}


# ------------------------------------------------------------------------------------------------
# job: one thermal (Mermin) state of the subset
# ------------------------------------------------------------------------------------------------
def _thermo_on_grid(co, spec, G, ls0, wcut, sea_shells):
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"], T=spec["T"])
    g = K.Grid(ph, G)
    ls = K.relabel(g, ph, ls0)
    free = K.solve_state(g, ph.copy(lam=0.0), ls, mode="mermin")
    st = free if ph.lam == 0.0 else K.solve_state(g, ph, ls, mode="mermin", guess=free.eps)
    # sea-hole diagnostic of the filling CONVENTION: thermal holes the excluded sea brane band (j = -1, even, the highest
    # sea level, rank -1) of every shell n2 >= 1 would carry at the same mu and T, in the converged potentials
    es = K.sea_brane_levels(g, ph, sea_shells, st.dM, st.v)
    holes = 4.0 * np.array([r3 for (_, r3) in sea_shells], dtype=float) * K.fermi((st.mu - es) / ph.T)

    def thermo(s, T):
        o, _ = K.observables(s)
        ent, lg = K.mermin_sums(s.eps, ls.deg, s.mu, T)
        E = o["E_KS"]
        F = E - T * ent
        return {"mu": s.mu, "E": E, "entropy": ent, "F": F, "Omega_direct": -T * lg - o["E_int"],
                "Omega_F_minus_muN": F - s.mu * ph.N, "E_int": o["E_int"], "N_sum": o["N_sum"], "int_n": o["int_n"]}

    T = ph.T
    th = thermo(st, T)
    dT = DT_REL * T
    nb = []
    for s in (1.0, -1.0, 2.0, -2.0):
        Ts = T + s * dT
        x = K.solve_state(g, ph.copy(T=Ts), ls, mode="mermin", start=(st.dM, st.v), guess=st.eps)
        nb.append((thermo(x, Ts), x.iters, x.res))
    th["C_V"] = T * float(rich_fd(*[x[0]["entropy"] for x in nb], dT))
    th["C_V_from_dEdT"] = float(rich_fd(*[x[0]["E"] for x in nb], dT))
    th["minus_dFdT"] = -float(rich_fd(*[x[0]["F"] for x in nb], dT))
    excl = K.lowest_excluded(g, ph, ls, st.dM, st.v)
    th["lowest_excluded"] = excl
    th["f_at_window_cut"] = float(K.fermi(np.array([(wcut - st.mu) / T]))[0])
    th["f_at_lowest_excluded"] = float(K.fermi(np.array([(excl - st.mu) / T]))[0])
    rec = {"G": G, "iterations": st.iters, "residual": st.res, "neighbour_iterations": [x[1] for x in nb],
           "neighbour_residual_max": max(x[2] for x in nb)}
    return {"rec": rec, "th": th, "eps": st.eps, "f": st.f, "keys": ls.keys(), "sea_eps": es, "sea_holes": holes}


def thermo_job(co, spec):
    t0 = time.time()
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"], T=spec["T"])
    g0 = K.Grid(ph, GRIDS[0])
    ls0, winfo = K.build_window(g0, ph, spec["sigma"])
    # the shells of the label set (the first winfo["shells"] shells) and SEA_EXTRA_SHELLS more, without n2 = 0
    sea_shells = [s for s in K.shells(4096)[:winfo["shells"] + SEA_EXTRA_SHELLS] if s[0] >= 1]
    runs = [_thermo_on_grid(co, spec, G, ls0, winfo["window_cut"], sea_shells) for G in GRIDS]
    out = {"id": spec["id"], "N": spec["N"], "lambda_tag": spec["tag"], "lambda": spec["lam"], "a4": spec["a4"],
           "T": spec["T"], "grids": list(GRIDS), "window": winfo, "levels_in_set": len(runs[0]["keys"]),
           "shells_in_set": len(set(k[0] for k in runs[0]["keys"]))}
    out["per_grid"] = [r["rec"] | {"thermo": r["th"]} for r in runs]
    th = {}
    for k in runs[0]["th"]:
        R, U = rich3(*[r["th"][k] for r in runs])
        th[k] = {"value": float(R), "U": float(U)}
    out["thermo"] = th
    Re, Ue = rich3(*[r["eps"] for r in runs])
    Rf, Uf = rich3(*[r["f"] for r in runs])
    out["levels"] = {"columns": ["n2", "j", "parity", "rank"], "keys": [list(k) for k in runs[0]["keys"]],
                     "eps": Re, "U": Ue, "f": Rf, "U_f": Uf}
    Rse, Use = rich3(*[r["sea_eps"] for r in runs])
    Rsh, Ush = rich3(*[r["sea_holes"] for r in runs])
    Rcum, Ucum = rich3(*[np.cumsum(r["sea_holes"]) for r in runs])
    nw = sum(1 for s in K.shells(4096)[:winfo["shells"]] if s[0] >= 1)
    out["sea_holes"] = {"definition": "4 r3 f((mu - eps_sea)/T) per shell n2 >= 1, eps_sea = the highest sea level (rank -1) of the "
                                      "j = -1 even sector in the converged potentials; cumulative = sum over the shells up to that n2",
                        "shells_n2_r3": [list(s) for s in sea_shells], "eps_sea": Rse, "U_eps_sea": Use, "holes": Rsh, "U_holes": Ush,
                        "cumulative": Rcum, "U_cumulative": Ucum, "shells_in_window": nw,
                        "total_window": float(Rcum[nw - 1]) if nw > 0 else 0.0, "U_total_window": float(Ucum[nw - 1]) if nw > 0 else 0.0,
                        "extra_shells_contribution": float(Rcum[-1] - (Rcum[nw - 1] if nw > 0 else 0.0))}
    return {"kind": "thermo", "id": spec["id"], "data": out, "seconds": time.time() - t0}


def _dispatch(task):
    kind, co, spec = task
    if kind == "ground":
        return ground_job(co, spec)
    if kind == "thermo":
        return thermo_job(co, spec)
    if kind == "exx":
        return exx_job(co, spec)
    if kind == "rescale":
        return rescale_job(co, spec)
    if kind == "crossing":
        return crossing_job(co, spec)
    if kind == "validation":
        return validation_job(co, spec)
    if kind == "free":
        return free_checks_job(co)
    raise ValueError(kind)


def cost_estimate(task):
    """Rough relative cost of a job (only orders the queue, longest first; outputs do not depend on it)."""
    kind, _, spec = task
    nf = {8.0: 1.0}.get(spec["N"], 2.0) if isinstance(spec, dict) else 1.0
    if kind == "thermo":
        return {0.01: 8.0, 0.02: 20.0, 0.05: 60.0}[spec["T"]] * nf * (1.0 + spec["a4"]) * (1.5 if spec["lam"] != 0.0 else 1.0)
    if kind == "ground":
        return 10.0 * nf * (1.0 + spec["a4"]) * (2.0 if spec["lam"] != 0.0 else 0.5)
    if kind in ("exx", "rescale"):
        return 3.0 * nf * (1.0 + spec["a4"])
    return {"validation": 30.0, "free": 10.0, "crossing": 15.0}[kind]


# ------------------------------------------------------------------------------------------------
# report
# ------------------------------------------------------------------------------------------------
class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail):
        self.checks.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
        print(f"{'PASS' if ok else 'FAIL'} - {name}: {detail}", file=sys.stderr, flush=True)


class Agg:
    """Aggregated per-state check: worst value, its state, failures."""

    def __init__(self, desc, tol):
        self.desc, self.tol = desc, tol
        self.n, self.worst, self.wid, self.fails = 0, -np.inf, "", []

    def add(self, sid, value, ok=None):
        ok = (value <= self.tol) if ok is None else ok
        self.n += 1
        v = value if math.isfinite(value) else np.inf
        if v > self.worst:
            self.worst, self.wid = v, sid
        if not ok:
            self.fails.append(f"{sid} ({value:.3e})")

    def emit(self, rep, name):
        rep.check(name, not self.fails, f"{self.desc}; {self.n} cases; worst value {self.worst:.3e} ({self.wid}); "
                                        f"tolerance {self.tol:.1e}; failures: {', '.join(self.fails) if self.fails else 'none'}")


def build_report(co, params, free, grounds, thermos, valid, exxs, rescales, crossing):
    rep = Report()
    fock_ok = (co["cQ2"] == Fraction(1, 32) and co["cWQ"] == 2 * co["cQ2"] and co["cQ2_status"] == co["cQ2"]
               and -co["cQ2"] == co["cn2"] and -co["cQ2"] == co["cs2"])
    rep.check("theory_input_coefficients",
              co["cM"] == Fraction(15, 16) and co["cV"] == Fraction(-1, 16) and co["eS2"] == Fraction(15, 32) and co["eN2"] == Fraction(-1, 32) and fock_ok,
              f"ks-theory.json (sha256 {co['sha256'][:16]}): M_eff = m + {co['cM']} lambda S, v_v = {co['cV']} lambda n, "
              f"e_int = lambda[{co['eS2']} S^2 + {co['eN2']} n^2] (Hartree 1/2 plus the uniform-gas exchange {co['cs2']}, {co['cn2']}); "
              f"consistent: M_eff - m = d e_int/dS ({2 * co['eS2']} = {co['cM']}), v_v = d e_int/dn ({2 * co['eN2']} = {co['cV']}): "
              f"{2 * co['eS2'] == co['cM'] and 2 * co['eN2'] == co['cV']}; exact-Fock variant (exchange.exactFockSlab): "
              f"e_x^exact = -lambda {co['cQ2']} (n^2 + S^2 - Q^2), i.e. e_int + lambda {co['cQ2']} Q^2 (stated: {co['cQ2_status']}) and "
              f"w_Q = lambda {co['cWQ']} Q sigma3 = d(lambda {co['cQ2']} Q^2)/dQ, the n^2 and S^2 coefficients equal the uniform-gas "
              f"{co['cn2']}, {co['cs2']}: {fock_ok}")
    an = free["analytic"]
    rep.check("free_k0_analytic_spectra", an["max_error_richardson"] <= 1e-11,
              f"k = 0, constant M, v = 0, theta_tip = 0 (ks-theory.json boundaryConditions.exactK0Spectra), (m, L) = (1, 3), (1, 2), (2, 3), "
              f"ranks -3..5 of both parities and both block types: Richardson (G = 300, 600, 1200) max |error| {an['max_error_richardson']:.3e} "
              f"(tolerance 1e-11; max stated U {an['max_U']:.2e}); single grids: "
              + ", ".join(f"G = {G}: {e:.3e}" for G, e in an["max_error_per_grid"].items()))
    rep.check("free_convergence_order_two", 3.99 <= an["ratio_min"] and an["ratio_max"] <= 4.01,
              f"error ratios (x(300) - x(600))/(x(600) - x(1200)) of the analytic spectra: median {an['ratio_median']:.5f}, "
              f"min {an['ratio_min']:.5f}, max {an['ratio_max']:.5f} (second order: 4; required within [3.99, 4.01])")
    rep.check("free_k0_block_type_symmetry", an["jsym_max"] <= 1e-13 and free["zero_mode"]["jsym_profile"] <= 1e-13,
              f"k = 0: the spectra of j = +1 and j = -1 agree to {an['jsym_max']:.1e} and the zero-mode profiles to "
              f"{free['zero_mode']['jsym_profile']:.1e} (exact discrete symmetry w -> -w of the staggered scheme; tolerance 1e-13)")
    zm = free["zero_mode"]
    rep.check("free_zero_mode", zm["max_abs_eps"] <= 1e-13 and zm["max_w_over_u"] <= 1e-12 and zm["profile_richardson_max_error"] <= 1e-9,
              f"k = 0 brane zero mode (M = H = 1, L = 3, both j): |eps| <= {zm['max_abs_eps']:.1e} (tolerance 1e-13), "
              f"max |w| / max |u| = {zm['max_w_over_u']:.1e} (b = 0 identically; tolerance 1e-12), Richardson profile vs "
              f"sqrt(2M/(1 - e^(-2ML))) e^(My) at the 151 report points: max error {zm['profile_richardson_max_error']:.2e} (tolerance 1e-9)")
    bb = free["brane_band_slope"]
    rep.check("free_brane_band_slope", bb["max_rel"] <= 1e-11 and bb["formula_vs_theory_number"] <= 1e-15,
              f"d eps/dk at k = 0 of the even j = +1 brane band (discrete Hellmann-Feynman, Richardson) equals ks-theory.json "
              f"c e^(-a4,0) at a4,0 = {list(SLICES)} to {bb['max_rel']:.2e} relative (tolerance 1e-11); the formula reproduces "
              f"checksNumeric.braneBandSlope_M1_H1_L3_a0 to {bb['formula_vs_theory_number']:.1e}")
    pb = free["particle_branch"]
    rep.check("free_particle_branch", pb["violations"] == 0 and pb["closest_to_zero_away_from_zero_modes"] > 1e-3,
              f"shells n2 <= 30 at every slice (G = 300): the lowest particle index (count of free levels below -1e-9) has eps > 0 "
              f"(the k = 0 even zero mode: eps = 0), the index below has eps < 0; violations {pb['violations']}; closest level to zero "
              f"away from the zero modes {pb['closest_to_zero_away_from_zero_modes']:.4f} m (required > 1e-3)")
    # parameters
    P = params
    rep.check("parameters_closed_shells", P["closed_shells_same_on_all_grids"],
              f"free a4,0 = 0 aufbau: bulk edge {P['bulk_edge']['value']:.12f} m (U {P['bulk_edge']['U']:.1e}); closed shells below it "
              f"{[int(c['N']) for c in P['closed_shells_a0']]} (same on every grid: {P['closed_shells_same_on_all_grids']}); "
              f"N_large = {int(P['N_large'])}, N_mid = {int(P['N_mid'])} (nearest to N_large/4 = {P['N_large'] / 4:.1f})")
    cal_ok = all(c["rounding_margin_rel"] > 50 * c["strength_rel_U"] for c in P["calibration"])
    rep.check("parameters_calibration", cal_ok,
              "couplings re-derived (strength = max over slices and y of max((15/16)|S|, |n|/16), free ground states): "
              + "; ".join(f"N = {int(c['N'])}: strength {c['strength']:.10g} (U {c['U']:.1e}), lambda_1 = {c['lambda1']}, lambda_2 = {c['lambda2']}"
                          for c in P["calibration"])
              + "; the unrounded couplings lie farther from a 4-digit rounding boundary than 50 x their relative uncertainty: " + str(cal_ok))
    # per-state checks (ground)
    A = {
        "ground_scf_converged": Agg("SCF converged (max |potential residual|, units of m) for the ground state, the Delta-SCF state and the four a4 neighbours on every grid", 1e-12),
        "ground_grid_consistency": Agg("the same occupations and the same HOMO/LUMO groups on every grid (value 1 = differ)", 0.0),
        "ground_closed_shell": Agg("closed-shell aufbau on every grid (value 1 = open)", 0.0),
        "ground_window_complete": Agg("label set complete on every grid: LUMO - lowest excluded level (must be < 0)", 0.0),
        "ground_N_conservation": Agg("particle number: |sum g f - N| <= 1e-9 on every grid and |2 Vol_7 int e^{6Hy} n dy - N| (Richardson) <= 3U + 1e-10 N; "
                                     "value = the larger of the two ratios |difference| / allowance", 1.0),
        "ground_energy_two_forms": Agg("E_KS = sum g f eps - E_int equals the variational form on every grid: relative difference", 1e-9),
        "emt_energy_integral": Agg("2 Vol_7 int e^{6Hy} rho dy = E_KS (Richardson values): |difference| / (3 (U1 + U2) + 1e-12 max(1, |E|))", 1.0),
        "emt_y_conservation_integrated": Agg("[e^{6Hy} p8]_{-L}^{0} = 3H int e^{6Hy}(p3 + p_t) dy (Richardson values): |difference| / (3 (U1 + U2) + 1e-8 scale), "
                                             "scale = max(|jump|, |integral|, |e^{6Hy} p8| at both ends)", 1.0),
        "emt_energy_change_dE_da4": Agg("dE/da4 at fixed occupations (a4 +- delta, +- 2 delta, Richardson) = -6 Vol_7 int e^{6Hy}(p3 - p_t) dy (Richardson in h): "
                                        "|difference| / (3 (U1 + U2) + 1e-10 max(1, |dE/da4|))", 1.0),
        "adiabatic_hellmann_feynman_discrete": Agg("d eps_n/da4 (differences of the self-consistent levels) = z_n^T (dT/da4) z_n on every grid: max |deviation| (units of m)", 1e-8),
        "excited_delta_scf_free_equals_gap": Agg("lambda = 0: Delta-SCF excitation energy equals the KS gap on every grid (|difference|, m)", 1e-11),
        "richardson_asymptotic_ratio": Agg("asymptotic regime: |median ratio (x(300)-x(600))/(x(600)-x(1200)) of the eigenvalues - 4|", 0.05),
        "excited_particle_hole_lowest_is_gap": Agg("particle-hole list: the lowest excitation is HOMO group -> LUMO group with delta_eps = KS gap "
                                                   "(Richardson values): |difference| / (3 (U1 + U2) + 1e-12), value 1e9 if the groups differ", 1.0),
    }
    for gr in grounds:
        d = gr["data"]
        sid = d["id"]
        sc = d["scalars"]
        pg = d["per_grid"]
        A["ground_scf_converged"].add(sid, max(max(r["residual"], r["excited_residual"], r["neighbour_residual_max"]) for r in pg))
        cons = d["consistency"]
        A["ground_grid_consistency"].add(sid, 0.0 if (cons["same_occupations_all_grids"] and cons["same_homo_lumo_groups_all_grids"]) else 1.0)
        A["ground_closed_shell"].add(sid, 1.0 if any(r["open_shell"] for r in pg) else 0.0)
        wc = max(r["scalars"]["LUMO"] - r["scalars"]["lowest_excluded"] for r in pg)
        A["ground_window_complete"].add(sid, wc, ok=wc < 0)
        N = d["N"]
        nv = max(max(abs(r["scalars"]["N_sum"] - N) for r in pg) / 1e-9,
                 abs(sc["int_n"]["value"] - N) / (3 * sc["int_n"]["U"] + 1e-10 * N))
        A["ground_N_conservation"].add(sid, nv)
        A["ground_energy_two_forms"].add(sid, max(abs(r["scalars"]["E_variational"] - r["scalars"]["E_KS"]) / max(1.0, abs(r["scalars"]["E_KS"])) for r in pg))

        def cmp(a, b, rel, scale=None):
            x, y = sc[a], sc[b]
            s = scale if scale is not None else max(1.0, abs(x["value"]))
            return abs(x["value"] - y["value"]) / (3 * (x["U"] + y["U"]) + rel * s)

        A["emt_energy_integral"].add(sid, cmp("int_rho", "E_KS", 1e-12))
        ysc = max(abs(sc["ycons_integral"]["value"]), abs(sc["ycons_jump"]["value"]),
                  abs(sc["p8_tip"]["value"]) * math.exp(-18.0), abs(sc["p8_brane"]["value"]), 1e-300)
        A["emt_y_conservation_integrated"].add(sid, cmp("ycons_jump", "ycons_integral", 1e-8, scale=ysc))
        A["emt_energy_change_dE_da4"].add(sid, cmp("dE_da4_fd", "dE_da4_emt", 1e-10))
        A["adiabatic_hellmann_feynman_discrete"].add(sid, max(r["hellmann_feynman_maxdev"] for r in pg))
        if d["lambda"] == 0.0:
            A["excited_delta_scf_free_equals_gap"].add(sid, max(abs(r["scalars"]["delta_SCF"] - r["scalars"]["KS_gap"]) for r in pg))
        rm = cons["ratio_eps"]["median"]
        A["richardson_asymptotic_ratio"].add(sid, abs(rm - 4.0) if rm is not None else 0.0)
        ph0 = d["particle_hole"]["list"][0] if d["particle_hole"]["list"] else None
        same_groups = ph0 is not None and ph0["hole"] == ";".join(sorted(d["homo_group"])) and ph0["particle"] == ";".join(sorted(d["lumo_group"]))
        A["excited_particle_hole_lowest_is_gap"].add(
            sid, abs(ph0["delta_eps"] - sc["KS_gap"]["value"]) / (3 * (ph0["U_delta_eps"] + sc["KS_gap"]["U"]) + 1e-12) if same_groups else 1e9)
    for name, ag in A.items():
        ag.emit(rep, name)
    # exact-Fock variant
    X = {
        "exx_scf_converged": Agg("exact-Fock variant (w_Q = lambda Q/16 sigma3, e_int + lambda Q^2/32), started from the converged uniform-gas state: "
                                 "max |potential residual| (dM, v_v, w_Q) on every grid (m)", 1e-12),
        "exx_N_conservation": Agg("exact-Fock variant: |sum g f - N| on every grid", 1e-9),
        "exx_energy_two_forms": Agg("exact-Fock variant: E_KS equals the variational form (incl. - int w_Q Q) on every grid: relative difference", 1e-9),
        "exx_emt_energy_integral": Agg("exact-Fock variant: 2 Vol_7 int e^{6Hy} rho dy = E_KS (Richardson): |difference| / (3 (U1 + U2) + 1e-12 max(1, |E|))", 1.0),
        "exx_y_conservation_integrated": Agg("exact-Fock variant: [e^{6Hy} p8]_{-L}^{0} = 3H int e^{6Hy}(p3 + p_t) dy with p8 including - w_Q Q "
                                             "(Richardson): |difference| / (3 (U1 + U2) + 1e-8 scale)", 1.0),
    }
    for e in exxs:
        d = e["data"]
        sid = d["id"]
        sc = d["scalars"]
        pg = d["per_grid"]
        X["exx_scf_converged"].add(sid, max(r["residual"] for r in pg))
        X["exx_N_conservation"].add(sid, max(abs(r["scalars"]["N_sum"] - d["N"]) for r in pg))
        X["exx_energy_two_forms"].add(sid, max(abs(r["scalars"]["E_variational"] - r["scalars"]["E_exact_fock_scf"]) /
                                               max(1.0, abs(r["scalars"]["E_exact_fock_scf"])) for r in pg))
        x, y = sc["int_rho"], sc["E_exact_fock_scf"]
        X["exx_emt_energy_integral"].add(sid, abs(x["value"] - y["value"]) / (3 * (x["U"] + y["U"]) + 1e-12 * max(1.0, abs(y["value"]))))
        ysc = max(abs(sc["ycons_integral"]["value"]), abs(sc["ycons_jump"]["value"]), abs(sc["p8_tip"]["value"]) * math.exp(-18.0),
                  abs(sc["p8_brane"]["value"]), 1e-300)
        x, y = sc["ycons_jump"], sc["ycons_integral"]
        X["exx_y_conservation_integrated"].add(sid, abs(x["value"] - y["value"]) / (3 * (x["U"] + y["U"]) + 1e-8 * ysc))
    for name, ag in X.items():
        ag.emit(rep, name)
    # rescaling partners (the reference's own identity, solved independently)
    gmap = {g["data"]["id"]: g["data"] for g in grounds}
    R_ = Agg("KS(a4,0; dk, v_t, lambda) = KS(0; dk e^{-a4,0}, v_t e^{-3 a4,0}, lambda), solved independently by the reference: the same "
             "label set and occupations (value 1e9 otherwise), max over the levels |delta eps| (m), |delta E_KS| / max(1, |E|) and "
             "max |delta profile| / profile maximum (n, S, rho, p3, p8), all Richardson values: the largest", 1e-10)
    for r in rescales:
        d = r["data"]
        g = gmap[d["id"]]
        same = d["levels"]["keys"] == g["levels"]["keys"] and np.array_equal(np.asarray(d["levels"]["f"]), np.asarray(g["levels"]["f"]))
        if not same:
            R_.add(d["id"], 1e9)
            continue
        dl = float(np.max(np.abs(np.asarray(d["levels"]["eps"]) - np.asarray(g["levels"]["eps"]))))
        de = abs(d["E_KS"]["value"] - g["scalars"]["E_KS"]["value"]) / max(1.0, abs(g["scalars"]["E_KS"]["value"]))
        dp = max(float(np.max(np.abs(np.asarray(d["profiles"][nm]["value"]) - np.asarray(g["profiles"][nm]["value"])))) /
                 max(float(np.max(np.abs(np.asarray(g["profiles"][nm]["value"])))), 1e-300) for nm in ("n", "S", "rho", "p3", "p8"))
        R_.add(d["id"], max(dl, de, dp))
    R_.emit(rep, "rescaling_identity_reference")
    # crossing demonstration
    cd = crossing["data"]
    rows = cd["rows"]
    flagged = [r for r in rows if not r["occupied_set_equal_to_a4_0"]]
    cont_ok = all(r["difference"]["value"] >= -3 * r["difference"]["U"] for r in flagged)
    cons = all(r["occupied_labels_same_on_all_grids"] and r["occupations_same_on_all_grids"] for r in rows) and cd["occupation_a4_0_same_on_all_grids"]
    pc = params["crossing_demo"]
    rep.check("crossing_demo_reference", pc["same_on_all_grids"] and rows[0]["occupied_set_equal_to_a4_0"] and bool(flagged) and cont_ok and cons,
              f"lambda = 0, N_demo = {int(cd['N_demo'])} re-derived (the smallest closed shell N > 8 of the free a4,0 = 0 aufbau, levels up to "
              f"{pc['emax']} m, whose last group holds a level off the even j = +1 brane band; same on all grids: {pc['same_on_all_grids']}); "
              f"the instantaneous aufbau occupation differs from the a4,0 = 0 one at a4,0 = {[r['a4'] for r in flagged]} (flagged: {bool(flagged)}); "
              f"the adiabatically continued state (a4,0 = 0 occupations) is not below the aufbau state there (within 3U): {cont_ok}; occupations "
              f"the same on every grid: {cons}; differences E_cont - E_aufbau: " + ", ".join(f"{r['a4']}: {r['difference']['value']:.10g}" for r in rows))
    # thermal
    T = {
        "thermo_scf_converged": Agg("Mermin SCF converged at T, T +- dT, T +- 2 dT on every grid: max residual (m)", 1e-12),
        "thermo_N_conservation": Agg("|sum g f - N| / N on every grid", 1e-12),
        "thermo_grand_potential_two_forms": Agg("Omega = -T sum g ln(1 + e^{-(eps-mu)/T}) - E_int equals F - mu N (every grid): relative difference", 1e-11),
        "thermo_CV_identity": Agg("C_V = T dS/dT equals dE/dT (Richardson in T and in h): |difference| / (3 (U1 + U2) + eta + 1e-4 |C_V|), "
                                  "eta = N x 1e-12 / dT the noise floor of a difference quotient of energies at the SCF tolerance", 1.0),
        "thermo_entropy_identity": Agg("-dF/dT = S (Richardson in T and in h): |difference| / (3 (U1 + U2) + eta + 1e-4 S), eta as for thermo_CV_identity", 1.0),
        "thermo_window_cut": Agg("occupation at the window cut and at the lowest excluded level (every grid)", 2e-13),
        "thermo_sea_holes_tail": Agg("sea-hole diagnostic (j = -1 even sea brane band, rank -1, n2 >= 1, converged potentials): finite on every grid, and "
                                     f"the {SEA_EXTRA_SHELLS} shells beyond the thermal label set add at most 1e-9 max(1, total) (value: their share; "
                                     "1e9 if not finite)", 1e-9),
    }
    for t in thermos:
        d = t["data"]
        sid = d["id"]
        pg = d["per_grid"]
        th = d["thermo"]
        T["thermo_scf_converged"].add(sid, max(max(r["residual"], r["neighbour_residual_max"]) for r in pg))
        T["thermo_N_conservation"].add(sid, max(abs(r["thermo"]["N_sum"] - d["N"]) for r in pg) / d["N"])
        T["thermo_grand_potential_two_forms"].add(sid, max(abs(r["thermo"]["Omega_direct"] - r["thermo"]["Omega_F_minus_muN"]) /
                                                         max(abs(r["thermo"]["Omega_direct"]), 1e-300) for r in pg))

        eta = d["N"] * 1e-12 / (DT_REL * d["T"])

        def tc(a, b, ref_value):
            return abs(th[a]["value"] - th[b]["value"]) / (3 * (th[a]["U"] + th[b]["U"]) + eta + 1e-4 * abs(ref_value))

        T["thermo_CV_identity"].add(sid, tc("C_V", "C_V_from_dEdT", th["C_V"]["value"]))
        T["thermo_entropy_identity"].add(sid, tc("minus_dFdT", "entropy", th["entropy"]["value"]))
        T["thermo_window_cut"].add(sid, max(max(r["thermo"]["f_at_window_cut"], r["thermo"]["f_at_lowest_excluded"]) for r in pg))
        sh = d["sea_holes"]
        fin = bool(np.all(np.isfinite(sh["holes"])) and np.all(np.isfinite(sh["eps_sea"])))
        T["thermo_sea_holes_tail"].add(sid, abs(sh["extra_shells_contribution"]) / max(1.0, abs(sh["total_window"])) if fin else 1e9)
    for name, ag in T.items():
        ag.emit(rep, name)
    # uncertainty validation
    v = valid["data"]
    bad = [k for k, c in v["classes"].items() if not c["all_within_U123"]]
    worst = max(v["classes"].items(), key=lambda kv: kv[1]["max_ratio_to_U123"])
    rep.check("richardson_uncertainty_validated", not bad,
              f"{v['id']} solved also on G = 2400: the three-grid value of (600, 1200, 2400) differs from that of (300, 600, 1200) by at most "
              f"the stated U of the latter for every element of {len(v['classes'])} quantity classes (scalars, all levels, profiles); "
              f"largest |R123 - R234| / U123 = {worst[1]['max_ratio_to_U123']:.3f} ({worst[0]}); classes exceeding: {bad if bad else 'none'}")
    return rep


# ------------------------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "results"))
    ap.add_argument("--report", default=str(KS / "reports" / "ks-reference.json"))
    ap.add_argument("--timing", default=None)
    ap.add_argument("--jobs", type=int, default=min(20, max(1, (os.cpu_count() or 4) - 2)))
    args = ap.parse_args()
    out = Path(args.out)
    t_all = time.time()
    co = theory_coefficients()
    timing = {}

    print("parameters (particle numbers, calibration) ...", file=sys.stderr, flush=True)
    pj = parameters_job(co)
    params = pj["data"]
    timing["parameters"] = pj["seconds"]
    nmap = {8: 8.0, "mid": params["N_mid"], "large": params["N_large"]}
    lam_of = {}
    for c in params["calibration"]:
        lam_of[c["N"]] = {"lam0": 0.0, "lamp1": c["lambda1"], "lamm1": -c["lambda1"], "lamp2": c["lambda2"], "lamm2": -c["lambda2"]}

    def gspec(Nk, tag, a4):
        N = nmap[Nk]
        return {"id": run_id(N, tag, a4), "N": N, "tag": tag, "lam": lam_of[N][tag], "a4": a4, "sigma": SIGMA[tag]}

    def tspec(Nk, tag, a4, T):
        sp = gspec(Nk, tag, a4)
        sp["T"] = T
        sp["id"] = run_id(sp["N"], tag, a4, T)
        return sp

    n_demo = params["crossing_demo"]["N_demo"]
    tasks = [("free", co, None), ("validation", co, gspec(*VALIDATION_STATE)), ("crossing", co, n_demo)]
    tasks += [("ground", co, gspec(*s)) for s in GROUND_MATRIX]
    tasks += [("exx", co, gspec(*s)) for s in GROUND_MATRIX if gspec(*s)["lam"] != 0.0]
    tasks += [("rescale", co, gspec(*s)) for s in GROUND_MATRIX if s[2] > 0.0]
    tasks += [("thermo", co, tspec(*s)) for s in THERMO_MATRIX]
    # longest jobs first (the order changes no output: results are keyed and written in a fixed order)
    tasks.sort(key=lambda t: -cost_estimate(t))
    print(f"{len(tasks)} jobs on {args.jobs} processes ...", file=sys.stderr, flush=True)
    results = {}
    with mp.get_context("spawn").Pool(args.jobs) as pool:
        for r in pool.imap_unordered(_dispatch, tasks):
            key = (r["kind"], r.get("id", ""))
            results[key] = r
            timing[f"{r['kind']}:{r.get('id', '')}"] = r["seconds"]
            print(f"  done {r['kind']} {r.get('id', '')} ({r['seconds']:.1f} s; {len(results)}/{len(tasks)})", file=sys.stderr, flush=True)
    free = results[("free", "")]["data"]
    valid = results[("validation", run_id(nmap[VALIDATION_STATE[0]], VALIDATION_STATE[1], VALIDATION_STATE[2]))]
    crossing = results[("crossing", "")]
    grounds = [results[("ground", gspec(*s)["id"])] for s in GROUND_MATRIX]
    exxs = [results[("exx", gspec(*s)["id"])] for s in GROUND_MATRIX if gspec(*s)["lam"] != 0.0]
    rescales = [results[("rescale", gspec(*s)["id"])] for s in GROUND_MATRIX if s[2] > 0.0]
    thermos = [results[("thermo", tspec(*s)["id"])] for s in THERMO_MATRIX]

    # ---- outputs
    params_out = {
        "description": "Revision Kohn-Sham REFERENCE solver (Revision/kohn_sham/reference): independent Python solver, staggered finite "
                       "differences in y with Richardson extrapolation over G = 300, 600, 1200 (SPEC section 7, Revision/kohn_sham/ks-theory.json). "
                       "x1..x3 = 3-space, x4 = time, x5..x7 = the exponentially deflating extra times (scale factor e^{-a4} sin^{1/6} z), "
                       "x8 = hidden direction (y = ln(sin z)/(6H)).",
        "theoryInputs": {"ksTheorySha256": co["sha256"], "MeffCoefficientOfLambdaS": str(co["cM"]), "vvCoefficientOfLambdaN": str(co["cV"]),
                         "eintCoefficientS2": str(co["eS2"]), "eintCoefficientN2": str(co["eN2"]),
                         "exactFockVariantEintCoefficientQ2": str(co["cQ2"]), "exactFockVariantWQCoefficientOfLambdaQ": str(co["cWQ"])},
        "physics": dict(BASE, tipTheta=0.0, historyA=1.0, slicesA4=list(SLICES), temperatures=list(TEMPS), sigmas=SIGMA),
        "numerics": {"grids": list(GRIDS), "validationGrids": list(G_VALID), "richardson": "R = (64 x(4G) - 20 x(2G) + x(G))/45; U = |R - (4 x(4G) - x(2G))/3| + 2e-12 max(1, |R|)",
                     "scfTolerance": 1e-12, "degeneracyTolerance": K.DEG_TOL, "zeroModeThreshold": K.TAU_ZERO, "a4Step": FD_DELTA,
                     "temperatureStepRelative": DT_REL, "endExtrapolation": "quintic from the six nearest half nodes",
                     "windowT0": "free particle levels below max(E_F, LUMO) + 0.25 + 2 sigma, plus ranks 0..2 of every sector of an occupied shell",
                     "windowThermal": "free particle levels below mu + T ln(1e13) + 0.2 + 2 sigma"},
        "derived": params,
        "matrix": {"ground": [gspec(*s)["id"] for s in GROUND_MATRIX],
                   "thermal": [tspec(*s)["id"] for s in THERMO_MATRIX],
                   "exact_fock_variant": [e["id"] for e in exxs],
                   "rescaling_partners": [r["id"] for r in rescales],
                   "crossing_demo_N": n_demo,
                   "validation": gspec(*VALIDATION_STATE)["id"]},
        "particleHoleRows": PH_ROWS, "seaHoleExtraShells": SEA_EXTRA_SHELLS, "crossingDemoEmax": CROSSING_EMAX,
    }
    files = {}
    files["parameters.json"] = params_out
    files["free-checks.json"] = free
    files[f"validation/{valid['data']['id']}.json"] = valid["data"]
    files["crossing/crossing-demo.json"] = crossing["data"]
    for gr in grounds:
        files[f"ground/{gr['id']}.json"] = gr["data"]
    for e in exxs:
        files[f"exx/{e['id']}.json"] = e["data"]
    for r in rescales:
        files[f"rescaling/{r['id']}.json"] = r["data"]
    for t in thermos:
        files[f"thermo/{t['id']}.json"] = t["data"]
    # a fresh output directory (only a former output directory of this program, or an empty one, is replaced)
    if out.exists():
        if not ((out / "manifest.json").exists() or not any(out.iterdir())):
            raise SystemExit(f"{out} exists and is not an output directory of run_reference.py")
        shutil.rmtree(out)
    for p, obj in files.items():
        dump_json(out / p, obj)
    hdr = ["id", "N", "lambda_tag", "lambda", "a4"]
    gcols = ["E_KS", "E_band", "E_int", "HOMO", "LUMO", "KS_gap", "delta_SCF", "int_rho", "int_p3", "int_p_t", "int_p8", "int_n",
             "dE_da4_emt", "dE_da4_fd", "deltaE_x_exact_fock", "rho_brane", "p8_brane", "rho_tip", "p8_tip"]
    rows = []
    for gr in grounds:
        d = gr["data"]
        row = [d["id"], int(d["N"]), d["lambda_tag"], f16(d["lambda"]), f16(d["a4"])]
        for c in gcols:
            row += [f16(d["scalars"][c]["value"]), f16(d["scalars"][c]["U"])]
        row += [f16(d["adiabatic"]["Q_max"]), f16(d["adiabatic"]["U_Q_max"]), d["levels_in_set"], d["shells_in_set"]]
        rows.append(row)
    write_csv(out / "ground-summary.csv", hdr + [x for c in gcols for x in (c, "U_" + c)] + ["Q_max", "U_Q_max", "levels", "shells"], rows)
    tcols = ["mu", "E", "entropy", "F", "Omega_direct", "Omega_F_minus_muN", "C_V", "C_V_from_dEdT", "minus_dFdT"]
    rows = []
    for t in thermos:
        d = t["data"]
        row = [d["id"], int(d["N"]), d["lambda_tag"], f16(d["lambda"]), f16(d["a4"]), f16(d["T"])]
        for c in tcols:
            row += [f16(d["thermo"][c]["value"]), f16(d["thermo"][c]["U"])]
        row += [d["levels_in_set"], d["shells_in_set"], f16(d["sea_holes"]["total_window"]), f16(d["sea_holes"]["U_total_window"])]
        rows.append(row)
    write_csv(out / "thermo-summary.csv", hdr + ["T"] + [x for c in tcols for x in (c, "U_" + c)] + ["levels", "shells", "sea_holes_window",
                                                                                                    "U_sea_holes_window"], rows)
    xcols = ["E_uniform_gas", "deltaE_x_exact_fock", "E_exact_fock_scf", "E_exx_minus_first_order", "gap_exact_fock"]
    rows = []
    for e in exxs:
        d = e["data"]
        row = [d["id"], int(d["N"]), d["lambda_tag"], f16(d["lambda"]), f16(d["a4"])]
        for c in xcols:
            row += [f16(d["scalars"][c]["value"]), f16(d["scalars"][c]["U"])]
        rows.append(row)
    write_csv(out / "exx-summary.csv", hdr + [x for c in xcols for x in (c, "U_" + c)], rows)
    rows = []
    for r in rescales:
        d = r["data"]
        rows.append([d["id"], int(d["N"]), d["lambda_tag"], f16(d["lambda"]), f16(d["a4"]), f16(d["partner_dk"]), f16(d["partner_v_t"]),
                     f16(d["E_KS"]["value"]), f16(d["E_KS"]["U"])])
    write_csv(out / "rescaling-summary.csv", hdr + ["partner_dk", "partner_v_t", "partner_E_KS", "U_partner_E_KS"], rows)
    rows = []
    for r in crossing["data"]["rows"]:
        rows.append([int(crossing["data"]["N_demo"]), f16(r["a4"]), str(r["occupied_set_equal_to_a4_0"]).lower(), str(r["open_shell"]).lower(),
                     f16(r["E_aufbau"]["value"]), f16(r["E_aufbau"]["U"]), f16(r["E_adiabatically_continued"]["value"]),
                     f16(r["E_adiabatically_continued"]["U"]), f16(r["difference"]["value"]), f16(r["difference"]["U"]),
                     ";".join(r["labels_left"]), ";".join(r["labels_entered"])])
    write_csv(out / "crossing-demo.csv", ["N", "a4", "occupied_set_equal_to_a4_0", "open_shell", "E_aufbau", "U_E_aufbau", "E_adiabatically_continued",
                                          "U_E_adiabatically_continued", "difference", "U_difference", "labels_left", "labels_entered"], rows)
    man = {}
    for p in sorted(x for x in out.rglob("*") if x.is_file() and x.name != "manifest.json"):
        man[p.relative_to(out).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    dump_json(out / "manifest.json", {"files": man})

    rep = build_report(co, params, free, grounds, thermos, valid, exxs, rescales, crossing)
    npass = sum(c["verdict"] == "PASS" for c in rep.checks)
    report = {"report": "Revision Kohn-Sham reference solver (independent Python, staggered finite differences + Richardson): self-checks",
              "producer": "Revision/kohn_sham/reference/run_reference.py",
              "matrix": {k: (len(v) if isinstance(v, list) else v) for k, v in params_out["matrix"].items()},
              "summary": {"checks": len(rep.checks), "pass": npass, "fail": len(rep.checks) - npass},
              "checks": rep.checks}
    dump_json(Path(args.report), report)
    timing["total"] = time.time() - t_all
    if args.timing:
        dump_json(Path(args.timing), timing)
    print(f"total {timing['total']:.1f} s", file=sys.stderr)
    print("SUCCESS" if npass == len(rep.checks) else "FAILURE")
    return 0 if npass == len(rep.checks) else 1


if __name__ == "__main__":
    sys.exit(main())
