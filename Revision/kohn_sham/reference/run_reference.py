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

# The representative subset of the canonical matrix (N: 8, "mid" = N_mid, "large" = N_large).
GROUND_SUBSET = [
    (8, "lam0", 0.0), (8, "lamp1", 1.0), (8, "lamp2", 0.0), (8, "lamm2", 2.0),
    ("mid", "lam0", 0.0), ("mid", "lam0", 2.0), ("mid", "lamp1", 0.5), ("mid", "lamm1", 1.5),
    ("mid", "lamp2", 1.0), ("mid", "lamp2", 2.0), ("mid", "lamm2", 2.0),
    ("large", "lam0", 0.0), ("large", "lam0", 2.0), ("large", "lamp1", 1.5), ("large", "lamm1", 0.5),
    ("large", "lamp2", 0.0), ("large", "lamp2", 2.0), ("large", "lamm2", 1.0),
]
THERMO_SUBSET = [
    (8, "lam0", 2.0, 0.05), (8, "lamp1", 1.0, 0.02), (8, "lamm1", 0.0, 0.01),
    ("mid", "lam0", 1.5, 0.05), ("mid", "lamp1", 2.0, 0.02), ("mid", "lamm1", 0.5, 0.01),
    ("large", "lam0", 1.0, 0.02), ("large", "lamp1", 2.0, 0.05),
]
VALIDATION_STATE = ("mid", "lamp2", 2.0)

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
    return {
        "sha256": hashlib.sha256(KS_THEORY.read_bytes()).hexdigest(),
        "cM": cM, "cV": cV, "cn2": cn2, "cs2": cs2,
        # e_int = lambda[(1/2 + c_S2) S^2 + c_n2 n^2] (Hartree (lambda/2) S^2 plus the uniform-gas exchange)
        "eS2": Fraction(1, 2) + cs2, "eN2": cn2,
        "slope_theory_a0": slope,
    }


def make_phys(co, **kw):
    p = K.Phys(**BASE, cM=float(co["cM"]), cV=float(co["cV"]), cS2=float(co["eS2"]), cN2=float(co["eN2"]))
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
            "keys": keys, "f": gs.f, "profiles": {k: prof[k][ri] for k in PROFILE_NAMES}, "hf": hf, "deps": deps}


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
    return {"kind": "ground", "id": spec["id"], "data": out, "seconds": time.time() - t0}


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
def _thermo_on_grid(co, spec, G, ls0, wcut):
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"], T=spec["T"])
    g = K.Grid(ph, G)
    ls = K.relabel(g, ph, ls0)
    free = K.solve_state(g, ph.copy(lam=0.0), ls, mode="mermin")
    st = free if ph.lam == 0.0 else K.solve_state(g, ph, ls, mode="mermin", guess=free.eps)

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
    return {"rec": rec, "th": th, "eps": st.eps, "f": st.f, "keys": ls.keys()}


def thermo_job(co, spec):
    t0 = time.time()
    ph = make_phys(co, a4=spec["a4"], lam=spec["lam"], N=spec["N"], T=spec["T"])
    g0 = K.Grid(ph, GRIDS[0])
    ls0, winfo = K.build_window(g0, ph, spec["sigma"])
    runs = [_thermo_on_grid(co, spec, G, ls0, winfo["window_cut"]) for G in GRIDS]
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
    return {"kind": "thermo", "id": spec["id"], "data": out, "seconds": time.time() - t0}


def _dispatch(task):
    kind, co, spec = task
    if kind == "ground":
        return ground_job(co, spec)
    if kind == "thermo":
        return thermo_job(co, spec)
    if kind == "validation":
        return validation_job(co, spec)
    if kind == "free":
        return free_checks_job(co)
    raise ValueError(kind)


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


def build_report(co, params, free, grounds, thermos, valid):
    rep = Report()
    rep.check("theory_input_coefficients",
              co["cM"] == Fraction(15, 16) and co["cV"] == Fraction(-1, 16) and co["eS2"] == Fraction(15, 32) and co["eN2"] == Fraction(-1, 32),
              f"ks-theory.json (sha256 {co['sha256'][:16]}): M_eff = m + {co['cM']} lambda S, v_v = {co['cV']} lambda n, "
              f"e_int = lambda[{co['eS2']} S^2 + {co['eN2']} n^2] (Hartree 1/2 plus the uniform-gas exchange {co['cs2']}, {co['cn2']}); "
              f"consistent: M_eff - m = d e_int/dS ({2 * co['eS2']} = {co['cM']}), v_v = d e_int/dn ({2 * co['eN2']} = {co['cV']}): "
              f"{2 * co['eS2'] == co['cM'] and 2 * co['eN2'] == co['cV']}")
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
    for name, ag in A.items():
        ag.emit(rep, name)
    # thermal
    T = {
        "thermo_scf_converged": Agg("Mermin SCF converged at T, T +- dT, T +- 2 dT on every grid: max residual (m)", 1e-12),
        "thermo_N_conservation": Agg("|sum g f - N| / N on every grid", 1e-12),
        "thermo_grand_potential_two_forms": Agg("Omega = -T sum g ln(1 + e^{-(eps-mu)/T}) - E_int equals F - mu N (every grid): relative difference", 1e-11),
        "thermo_CV_identity": Agg("C_V = T dS/dT equals dE/dT (Richardson in T and in h): |difference| / (3 (U1 + U2) + eta + 1e-4 |C_V|), "
                                  "eta = N x 1e-12 / dT the noise floor of a difference quotient of energies at the SCF tolerance", 1.0),
        "thermo_entropy_identity": Agg("-dF/dT = S (Richardson in T and in h): |difference| / (3 (U1 + U2) + eta + 1e-4 S), eta as for thermo_CV_identity", 1.0),
        "thermo_window_cut": Agg("occupation at the window cut and at the lowest excluded level (every grid)", 2e-13),
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

    tasks = [("free", co, None), ("validation", co, gspec(*VALIDATION_STATE))]
    tasks += [("ground", co, gspec(*s)) for s in GROUND_SUBSET]
    for (Nk, tag, a4, T) in THERMO_SUBSET:
        sp = gspec(Nk, tag, a4)
        sp["T"] = T
        sp["id"] = run_id(sp["N"], tag, a4, T)
        tasks.append(("thermo", co, sp))
    print(f"{len(tasks)} jobs on {args.jobs} processes ...", file=sys.stderr, flush=True)
    results = {}
    with mp.get_context("spawn").Pool(args.jobs) as pool:
        for r in pool.imap_unordered(_dispatch, tasks):
            key = (r["kind"], r.get("id", ""))
            results[key] = r
            timing[f"{r['kind']}:{r.get('id', '')}"] = r["seconds"]
            print(f"  done {r['kind']} {r.get('id', '')} ({r['seconds']:.1f} s)", file=sys.stderr, flush=True)
    free = results[("free", "")]["data"]
    valid = results[("validation", run_id(nmap[VALIDATION_STATE[0]], VALIDATION_STATE[1], VALIDATION_STATE[2]))]
    grounds = [results[("ground", gspec(*s)["id"])] for s in GROUND_SUBSET]
    thermos = [results[("thermo", run_id(nmap[s[0]], s[1], s[2], s[3]))] for s in THERMO_SUBSET]

    # ---- outputs
    params_out = {
        "description": "Revision Kohn-Sham REFERENCE solver (Revision/kohn_sham/reference): independent Python solver, staggered finite "
                       "differences in y with Richardson extrapolation over G = 300, 600, 1200 (SPEC section 7, Revision/kohn_sham/ks-theory.json). "
                       "x1..x3 = 3-space, x4 = time, x5..x7 = the exponentially deflating extra times (scale factor e^{-a4} sin^{1/6} z), "
                       "x8 = hidden direction (y = ln(sin z)/(6H)).",
        "theoryInputs": {"ksTheorySha256": co["sha256"], "MeffCoefficientOfLambdaS": str(co["cM"]), "vvCoefficientOfLambdaN": str(co["cV"]),
                         "eintCoefficientS2": str(co["eS2"]), "eintCoefficientN2": str(co["eN2"])},
        "physics": dict(BASE, tipTheta=0.0, historyA=1.0, slicesA4=list(SLICES), temperatures=list(TEMPS), sigmas=SIGMA),
        "numerics": {"grids": list(GRIDS), "validationGrids": list(G_VALID), "richardson": "R = (64 x(4G) - 20 x(2G) + x(G))/45; U = |R - (4 x(4G) - x(2G))/3| + 2e-12 max(1, |R|)",
                     "scfTolerance": 1e-12, "degeneracyTolerance": K.DEG_TOL, "zeroModeThreshold": K.TAU_ZERO, "a4Step": FD_DELTA,
                     "temperatureStepRelative": DT_REL, "endExtrapolation": "quintic from the six nearest half nodes",
                     "windowT0": "free particle levels below max(E_F, LUMO) + 0.25 + 2 sigma, plus ranks 0..2 of every sector of an occupied shell",
                     "windowThermal": "free particle levels below mu + T ln(1e13) + 0.2 + 2 sigma"},
        "derived": params,
        "subset": {"ground": [gspec(*s)["id"] for s in GROUND_SUBSET],
                   "thermal": [run_id(nmap[s[0]], s[1], s[2], s[3]) for s in THERMO_SUBSET],
                   "validation": gspec(*VALIDATION_STATE)["id"]},
    }
    files = {}
    files["parameters.json"] = params_out
    files["free-checks.json"] = free
    files[f"validation/{valid['data']['id']}.json"] = valid["data"]
    for gr in grounds:
        files[f"ground/{gr['id']}.json"] = gr["data"]
    for t in thermos:
        files[f"thermo/{t['id']}.json"] = t["data"]
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
        row += [d["levels_in_set"], d["shells_in_set"]]
        rows.append(row)
    write_csv(out / "thermo-summary.csv", hdr + ["T"] + [x for c in tcols for x in (c, "U_" + c)] + ["levels", "shells"], rows)
    man = {}
    for p in sorted(x for x in out.rglob("*") if x.is_file() and x.name != "manifest.json"):
        man[p.relative_to(out).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    dump_json(out / "manifest.json", {"files": man})

    rep = build_report(co, params, free, grounds, thermos, valid)
    npass = sum(c["verdict"] == "PASS" for c in rep.checks)
    report = {"report": "Revision Kohn-Sham reference solver (independent Python, staggered finite differences + Richardson): self-checks",
              "producer": "Revision/kohn_sham/reference/run_reference.py",
              "subset": params_out["subset"],
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
