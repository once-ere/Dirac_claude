#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/compute/compute_eos.py - the equation of state a 3-space observer infers for
dirac16complex as the extra times deflate and 3-space inflates (SPEC sections 8, 11): (i) the Kohn-Sham fermion
gas (instantaneous states along a4, outputs/ks-history-dense.csv of run_ks_history.py), (ii) the homogeneous
condensate (exact solution), (iii) mixtures; CPL tangents and fits; comparison with the Supernovae Unite values.

The corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1):
g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)), z = 6 H x0 real, in the author's
coordinates {x0, x1, ..., x7}: x0 = hidden direction; x1, x2, x3 = 3-space (scale factor e^{a4}); x4 = time; x5, x6, x7 =
the three exponentially DEFLATING extra times (scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}).  The history: a4 = H x4,
b4 = e^{(4/3) H x4}, beta = d ln b4/d a4 = 4/3, a PRESCRIBED background (test field, no back-reaction).  Observer scale
factor a = e^{a4 - a4_today}.

Every formula used here is derived exactly in derive/derive_effective.py (outputs/effective-formulas.json):
  E, P3, Pt, P0 = the cell integrals 2 Vol_7 int e^{3Hy} (rho, p3, p_t, p0) dy of the Kohn-Sham record
  (Vol_7 = ell^3 v_t e^{(5/3) a4}); conservation dE/da4 = -3 P3 - (beta/2 - 1)(P0 + 3 Pt) = -3 P3 + Pt + P0/3 (fixed
  occupations); w_eff(A) = w_eff(B) = P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E) = P3/E - (P0 + 3 Pt)/(9E) (extra times and hidden
  direction compact with fixed coordinate period, ASSUMPTION; or per unit of their coordinate volume), w_eff(C) =
  w_eff(A) - (4 - 2 beta)/3 = w_eff(A) - 4/9 (per unit proper 7-volume); ratios w3 = P3/E, wt = Pt/E, wx0 = P0/E (the x0
  ratio, not the CPL w0); CPL w(a) = w0 + wa (1 - a): tangent w0 = w(1), wa = -dw/da4 at a4_today; least-squares fits
  over a in [a1, 1].
The homogeneous condensate: S = S0 e^{a4} b4^{-2}, so u = lambda S/m = u_today e^{(1 - 2 beta)(a4 - a4_today)} =
u_today e^{-(5/3)(a4 - a4_today)}; w_c = u/(2 + u), w_eff(A) = ((2 beta - 1)/3) w_c = (5/9) w_c.
Interpretation is labelled in the outputs.  Numbers only from Revision outputs.  Deterministic (LF).
"""

import csv
import json
import math
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
OWN = HERE.parent
DENSE = OWN / "outputs" / "ks-history-dense.csv"
FORMULAS = OWN / "outputs" / "effective-formulas.json"
OUT_HIST = OWN / "outputs" / "eos-history.csv"
OUT_SUM = OWN / "outputs" / "eos-summary.json"
OUT_REP = OWN / "reports" / "eos-checks.json"
UNITE = {"w_const": -0.764, "w0": -0.861, "wa": -0.60}
TAGS = ["lam0", "lamp1", "lamm1", "lamp2", "lamm2"]
TODAY = [0.5, 1.0, 1.5, 2.0]
BETA = 4.0 / 3.0                                             # d ln b4/d a4 on the history
SHIFT_C = -(4.0 - 2.0 * BETA) / 3.0                          # w_eff(C) - w_eff(A) = -4/9
FIT_RANGES = [(2.0, 0.5), (2.0, 1.0 / 3.0), (1.5, 0.5)]     # (a4_today, a1): a in [a1, 1]
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})


def r(v, n=12):
    """deterministic rounding for the JSON outputs"""
    if v is None or (isinstance(v, float) and not math.isfinite(v)):
        return None
    if v == 0:
        return 0.0                                      # no negative zero in the outputs
    return float(f"{v:.{n}e}")


def deriv(f, h):
    """4th-order finite-difference derivative on a uniform grid (central inside, one-sided at the ends)"""
    n = len(f)
    d = np.empty(n)
    for i in range(n):
        if 2 <= i <= n - 3:
            d[i] = (f[i - 2] - 8 * f[i - 1] + 8 * f[i + 1] - f[i + 2]) / (12 * h)
        elif i < 2:
            s = f[i:i + 5]
            d[i] = ((-25 * s[0] + 48 * s[1] - 36 * s[2] + 16 * s[3] - 3 * s[4]) / (12 * h) if i == 0 else
                    (-3 * f[0] - 10 * f[1] + 18 * f[2] - 6 * f[3] + f[4]) / (12 * h))
        else:
            if i == n - 1:
                s = f[n - 5:]
                d[i] = (25 * s[4] - 48 * s[3] + 36 * s[2] - 16 * s[1] + 3 * s[0]) / (12 * h)
            else:
                d[i] = (3 * f[n - 1] + 10 * f[n - 2] - 18 * f[n - 3] + 6 * f[n - 4] - f[n - 5]) / (12 * h)
    return d


def interp(xg, fg, xq):
    """4-point Lagrange (cubic) interpolation on the uniform grid"""
    h = xg[1] - xg[0]
    out = []
    for x in np.atleast_1d(xq):
        i = int(math.floor((x - xg[0]) / h))
        i0 = min(max(i - 1, 0), len(xg) - 4)
        xs, fs = xg[i0:i0 + 4], fg[i0:i0 + 4]
        v = 0.0
        for j in range(4):
            lj = 1.0
            for m in range(4):
                if m != j:
                    lj *= (x - xs[m]) / (xs[j] - xs[m])
            v += fs[j] * lj
        out.append(v)
    return np.array(out)


GL_X, GL_W = np.polynomial.legendre.leggauss(32)


def cpl_fit(wfun, a1):
    """least squares of w(a) by w0 + wa (1 - a) on [a1, 1] (continuous L2 in a) and the constant-w fit"""
    a = 0.5 * (1 - a1) * GL_X + 0.5 * (1 + a1)
    wq = 0.5 * (1 - a1) * GL_W
    w = wfun(a)
    Lr = 1 - a1
    J0 = float(np.sum(wq * w))
    J1 = float(np.sum(wq * w * (1 - a)))
    Amat = np.array([[Lr, Lr ** 2 / 2], [Lr ** 2 / 2, Lr ** 3 / 3]])
    w0, wa = np.linalg.solve(Amat, np.array([J0, J1]))
    return float(w0), float(wa), J0 / Lr


def load():
    rows = list(csv.DictReader(open(DENSE, encoding="utf-8")))
    series = {}
    for row in rows:
        key = (int(row["N"]), row["lambda_tag"])
        series.setdefault(key, []).append(row)
    out = {}
    for key, rs in series.items():
        rs.sort(key=lambda q: float(q["a4"]))
        g = lambda c: np.array([float(q[c]) for q in rs])  # noqa: E731
        out[key] = {"a4": g("a4"), "E": g("int_rho"), "P3": g("int_p3"), "Pt": g("int_p_t"), "P0": g("int_p0"),
                    "lambda": float(rs[0]["lambda"])}
    return out


def w_A(P3, Pt, P0, E):
    return P3 / E + (0.5 * BETA - 1.0) * (P0 + 3.0 * Pt) / (3.0 * E)


def main():
    formulas = json.loads(FORMULAS.read_text(encoding="utf-8"))
    check("formulas_input_present",
          formulas["wEff"]["A"] == "P3/E + (beta/2 - 1)(P0 + 3 Pt)/(3E)" and formulas["wEff"]["C"] == "A - (4 - 2 beta)/3"
          and "corrected primordial metric" in formulas["description"],
          "outputs/effective-formulas.json (derive_effective.py, corrected metric): w_eff(A) = P3/E + (beta/2 - 1)(P0 + "
          "3 Pt)/(3E), w_eff(C) = w_eff(A) - (4 - 2 beta)/3; the history's beta = 4/3")
    S = load()
    ns = sorted({k[0] for k in S})
    nsl = sorted({len(v["a4"]) for v in S.values()})
    check("dense_history_complete", len(S) == 3 * len(TAGS) and len(nsl) == 1 and nsl[0] >= 41,
          f"{len(S)} series (N = {', '.join(map(str, ns))} x {len(TAGS)} couplings) x {nsl} slices from "
          f"outputs/ks-history-dense.csv")
    a4g = next(iter(S.values()))["a4"]
    h = float(a4g[1] - a4g[0])
    nsl = len(a4g)
    hist_rows = []
    summary_series = []
    worst_cons, worst_int, worst_dw = 0.0, 0.0, 0.0
    zero_series = []
    for key in sorted(S, key=lambda k: (k[0], TAGS.index(k[1]))):
        d = S[key]
        a4, E, P3, Pt, P0 = d["a4"], d["E"], d["P3"], d["Pt"], d["P0"]
        sid = f"N{key[0]}_{key[1]}"
        if np.max(np.abs(E)) == 0.0:
            zero_series.append(sid)
            summary_series.append({"series": sid, "N": key[0], "lambda": d["lambda"],
                                   "status": "E = P3 = Pt = P0 = 0 at every slice (the k = 0 fold zero modes have eps = 0 "
                                             "and no interaction): no energy, w undefined"})
            continue
        # conservation dE/da4 = -3 P3 + Pt + P0/3 (pointwise in a4) and integrated (Simpson on pairs of intervals)
        dE = deriv(E, h)
        scale = np.max(np.abs(E))
        src = 3 * P3 + (0.5 * BETA - 1.0) * (P0 + 3 * Pt)          # dE/da4 = -src
        dev = np.max(np.abs(dE + src)[2:-2]) / scale
        worst_cons = max(worst_cons, dev)
        integ = 0.0
        devint = 0.0
        for i in range(0, nsl - 1, 2):
            integ += h / 3 * (src[i] + 4 * src[i + 1] + src[i + 2])
            devint = max(devint, abs(E[i + 2] - E[0] + integ) / scale)
        worst_int = max(worst_int, devint)
        wA = w_A(P3, Pt, P0, E)
        wC = wA + SHIFT_C
        w3, wt, wx0 = P3 / E, Pt / E, P0 / E
        dwA = deriv(wA, h)
        dnum = deriv(P3, h) + (0.5 * BETA - 1.0) * (deriv(P0, h) + 3 * deriv(Pt, h)) / 3.0
        dwA_id = dnum / E + wA * src / E                     # identity: E' = -src
        worst_dw = max(worst_dw, float(np.max(np.abs(dwA - dwA_id)[2:-2])))
        dw3 = deriv(w3, h)
        for i in range(nsl):
            hist_rows.append([sid, key[0], d["lambda"], a4[i], E[i], P3[i], Pt[i], P0[i], wA[i], wC[i], w3[i], wt[i],
                              wx0[i], dwA[i], dw3[i]])
        tang = []
        for t in TODAY:
            i = int(round(t / h))
            tang.append({"a4_today": t, "w_eff_A_B": {"w0": r(wA[i]), "wa": r(-dwA[i])},
                         "w_eff_C": {"w0": r(wC[i]), "wa": r(-dwA[i])},
                         "ratio_w3": {"w0": r(w3[i]), "wa": r(-dw3[i])}})
        fits = []
        for t, a1 in FIT_RANGES:
            def wfa(aa, arr=wA, t=t):
                return interp(a4, arr, t + np.log(aa))
            w0A, waA, wcA = cpl_fit(wfa, a1)
            w0r, war, wcr = cpl_fit(lambda aa, t=t: interp(a4, w3, t + np.log(aa)), a1)
            fits.append({"a4_today": t, "a_range": [r(a1), 1.0],
                         "w_eff_A_B": {"w0": r(w0A), "wa": r(waA), "w_const": r(wcA)},
                         "w_eff_C": {"w0": r(w0A + SHIFT_C), "wa": r(waA), "w_const": r(wcA + SHIFT_C)},
                         "ratio_w3": {"w0": r(w0r), "wa": r(war), "w_const": r(wcr)}})
        summary_series.append({
            "series": sid, "N": key[0], "lambda": d["lambda"],
            "w_eff_A_B_range": [r(float(np.min(wA))), r(float(np.max(wA)))],
            "w_eff_C_range": [r(float(np.min(wC))), r(float(np.max(wC)))],
            "ratio_w3_range": [r(float(np.min(w3))), r(float(np.max(w3)))],
            "ratio_wt_range": [r(float(np.min(wt))), r(float(np.max(wt)))],
            "ratio_wx0_range": [r(float(np.min(wx0))), r(float(np.max(wx0)))],
            "dlnE_da4_at_0_and_end": [r(float(dE[0] / E[0])), r(float(dE[-1] / E[-1]))],
            "sign_of_E": "positive" if np.all(E > 0) else ("negative" if np.all(E < 0) else "mixed"),
            "cplTangent": tang, "cplFits": fits,
            "conservation_rel_dev": r(dev, 3), "conservation_integrated_rel_dev": r(devint, 3)})

    check("conservation_identity", worst_cons <= 1e-5,
          f"4th-order finite differences of E on the dense grid (h = {h:g}) vs -3 P3 + Pt + P0/3 (beta = 4/3) from the "
          f"solver's EMT integrals: max |dE/da4 + 3 P3 - Pt - P0/3|/max|E| = {worst_cons:.3e} (interior slices, every "
          f"series with E != 0)")
    check("conservation_integrated_simpson", worst_int <= 1e-5,
          f"E(a4) - E(0) = -int_0^a4 (3 P3 - Pt - P0/3): max relative deviation {worst_int:.3e}")
    check("derivative_two_ways", worst_dw <= 1e-5,
          f"d w_eff(A)/da4 by finite differences vs the identity (P3' - (P0' + 3 Pt')/9)/E + w_eff(A) (3 P3 - Pt - P0/3)/E "
          f"at the interior slices of every series: max deviation {worst_dw:.3e}")

    # ---- the free gas: exact fold-band gas (P3 = E/3, Pt = P0 = 0) at every slice
    free = {k: v for k, v in S.items() if k[1] == "lam0" and np.max(np.abs(v["E"])) > 0}
    fdev = max(max(float(np.max(np.abs(v["P3"] / v["E"] - 1.0 / 3.0))), float(np.max(np.abs(v["Pt"] / v["E"]))),
                   float(np.max(np.abs(v["P0"] / v["E"])))) for v in free.values())
    edil = max(float(np.max(np.abs(v["E"] * np.exp(v["a4"]) / v["E"][0] - 1.0))) for v in free.values())
    check("free_gas_exact_fold_band", fdev <= 1e-12 and edil <= 1e-12,
          f"lambda = 0, N = {', '.join(str(k[0]) for k in sorted(free))}: P3/E = 1/3, Pt/E = P0/E = 0 to {fdev:.1e} and "
          f"E e^(a4) constant to {edil:.1e} at every slice (every occupied orbital is the fold-band orbital, eps = e^(-a4) |k|): "
          f"w_eff(A) = 1/3 exactly (radiation-like), w_eff(C) = 1/3 - 4/9 = -1/9, wa = 0")

    # ---- the interacting gas (N = N_mid, N_large, lambda != 0): measured ranges
    gas = {k: v for k, v in S.items() if k[0] != 8 and k[1] != "lam0"}
    wA_all = np.concatenate([w_A(v["P3"], v["Pt"], v["P0"], v["E"]) for v in gas.values()])
    epos = all(np.all(v["E"] > 0) for v in gas.values())
    p0E = np.concatenate([v["P0"] / v["E"] for v in gas.values()])
    ptE = np.concatenate([v["Pt"] / v["E"] for v in gas.values()])
    check("interacting_gas_ranges", epos and bool(np.all(np.isfinite(wA_all))),
          f"Kohn-Sham gas N = {', '.join(sorted({str(k[0]) for k in gas}))}, lambda != 0 ({len(gas)} series): E > 0 at every "
          f"slice: {epos}; w_eff(A) in [{np.min(wA_all):.6f}, {np.max(wA_all):.6f}], w_eff(C) = w_eff(A) - 4/9 in "
          f"[{np.min(wA_all) + SHIFT_C:.6f}, {np.max(wA_all) + SHIFT_C:.6f}]; Pt/E in [{np.min(ptE):.3e}, {np.max(ptE):.3e}], "
          f"P0/E in [{np.min(p0E):.3e}, {np.max(p0E):.3e}]")

    # ---- the interacting N = 8 states (only k = 0 levels: no 3-momentum)
    n8 = {k: v for k, v in S.items() if k[0] == 8 and k[1] != "lam0"}
    n8_sign = all((np.all(v["E"] < 0) if v["lambda"] > 0 else np.all(v["E"] > 0)) for v in n8.values())
    n8_wA = np.concatenate([w_A(v["P3"], v["Pt"], v["P0"], v["E"]) for v in n8.values()])
    n8_w3 = np.concatenate([v["P3"] / v["E"] for v in n8.values()])
    check("n8_interacting_states", n8_sign,
          f"N = 8, lambda != 0 ({len(n8)} series; only the k = 0 levels, the energy is interaction energy): E has the sign "
          f"of -lambda at every slice: {n8_sign}; P3/E in [{np.min(n8_w3):.6f}, {np.max(n8_w3):.6f}]; w_eff(A) in "
          f"[{np.min(n8_wA):.6f}, {np.max(n8_wA):.6f}]")

    # ---- condensate (exact): S ~ e^{a4} b4^{-2}, u = lambda S/m ~ e^{(1 - 2 beta) a4}
    u = -382.0 / 441.0
    wc0 = u / (2 + u)
    rate = 1.0 - 2.0 * BETA                                 # d ln u/d a4 = -5/3
    wa_ratio = -2.0 * rate * u / (2 + u) ** 2               # -d/da4 [u/(2 + u)] = -2 u'/(2 + u)^2, u' = rate u
    kA = (2.0 * BETA - 1.0) / 3.0                           # w_eff(A) = kA w_c = (5/9) w_c
    cond = {"S": "S0 e^(a4) b4^(-2) = S_today e^(-(5/3)(a4 - a4_today))", "rho": "m S + lambda S^2/2",
            "p3=p_t=p0": "lambda S^2/2",
            "ratio_w": "w_c = u/(2 + u), u = lambda S/m = u_today e^(-(5/3)(a4 - a4_today))",
            "ratio_wa": "(10/3) u/(2 + u)^2 (thawing sign for u < 0)",
            "w_eff_A_B": "((2 beta - 1)/3) w_c = (5/9) w_c", "w_eff_C": "(5/9) w_c - 4/9",
            "u_for_ratio_minus_0p764_today": r(u), "ratio_today": r(wc0), "ratio_wa_at_that_u": r(wa_ratio),
            "w_eff_A_B_today_at_that_u": r(kA * wc0), "w_eff_C_today_at_that_u": r(kA * wc0 + SHIFT_C),
            "wa_A_B_C_at_that_u": r(kA * wa_ratio),
            "history": "exact homogeneous solution for every a4(x4), b4(x4) (Revision/field_equations_a4/a4-equations.json "
                       "fields.dirac16complex00.homogeneousCondensate); the 3-space observer's expansion-inferred "
                       "w_exp = -1 exactly on a4 = H x4"}
    check("condensate_ratio_value", abs(wc0 + 0.764) < 1e-15, f"u = -382/441 today: ratio {wc0:.15f}")
    check("condensate_drifts", wa_ratio < 0,
          f"u = lambda S/m falls like e^(-(5/3) a4), so the ratio w_c = u/(2 + u) has wa = (10/3) u/(2 + u)^2 = "
          f"{wa_ratio:.6f} at the u that gives w_c = -0.764 today; w_eff(A) = (5/9) w_c = {kA * wc0:.6f} and w_eff(C) = "
          f"(5/9) w_c - 4/9 = {kA * wc0 + SHIFT_C:.6f}, both with wa = {kA * wa_ratio:.6f}")

    # ---- mixtures: free gas (N = N_large, lambda = 0: E ~ e^{-a4}, P3 = E/3, Pt = P0 = 0) + lambda = 0 condensate
    # (E_c = m S0 constant, P = 0): w_eff(A) = (1/3) E_g/(E_g + E_c) in [0, 1/3), w_eff(C) = w_eff(A) - 4/9
    nl = max(ns)
    g = S[(nl, "lam0")]
    a4g, Eg, P3g = g["a4"], g["E"], g["P3"]
    mix = []
    t = float(a4g[-1])
    it = len(a4g) - 1
    for f0 in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        Ec = Eg[it] * (1 - f0) / f0                     # gas fraction f0 = E_g/(E_g + E_c) at a4_today
        wmA = P3g / (Eg + Ec)
        dwm = deriv(wmA, h)
        entry = {"gas_fraction_today": f0, "w_eff_A_B": {"w0": r(wmA[it]), "wa": r(-dwm[it])},
                 "w_eff_C": {"w0": r(wmA[it] + SHIFT_C), "wa": r(-dwm[it])}}
        for a1 in (0.5, 1.0 / 3.0):
            w0f, waf, wcf = cpl_fit(lambda aa, wm=wmA: interp(a4g, wm, t + np.log(aa)), a1)
            entry[f"fit_a1_{a1:.4f}"] = {"A_B": {"w0": r(w0f), "wa": r(waf), "w_const": r(wcf)},
                                        "C": {"w0": r(w0f + SHIFT_C), "wa": r(waf), "w_const": r(wcf + SHIFT_C)}}
        mix.append(entry)
    wC_min = min(float(np.min(P3g / (Eg + Eg[it] * (1 - f0) / f0))) for f0 in np.linspace(0.001, 1.0, 1000)) + SHIFT_C
    check("mixture_C_cannot_reach_unite_w0_with_lambda0_condensate", wC_min >= SHIFT_C - 1e-12,
          f"free gas N = {nl} + lambda = 0 condensate, normalisation C: w_eff(C) = P3_g/(E_g + E_c) - 4/9 >= {wC_min:.6f} "
          f">= -4/9 at every slice and gas fraction: neither -0.861 nor a constant -0.764 is reached")

    # ---- free gas + a condensate of any ratio w_c today (u_today = 2 w_c/(1 - w_c), u > -2), any gas fraction, in
    # three definitions; the condensate drifts: u' = -(5/3) u, E_c = m S0 (1 + u/2), P_c = m S0 u/2 (= Pt_c = P3_c = P0_c),
    # so E_c' = P_c' = -(5/6) m S0 u
    dEg, dP3g = deriv(Eg, h), deriv(P3g, h)
    scans = {}
    for definition in ("ratio", "A_B", "C"):
        best = {"distance": float("inf")}
        min_wa_near, max_wa_near = float("inf"), float("-inf")
        for t2 in TODAY:
            i2 = int(round(t2 / h))
            wcs = np.linspace(-3.0, 0.99, 400)
            uu = 2 * wcs / (1 - wcs)
            for f0 in np.linspace(0.0, 1.0, 201):
                eg, p3g = f0, f0 * P3g[i2] / Eg[i2]
                deg, dp3g = f0 * dEg[i2] / Eg[i2], f0 * dP3g[i2] / Eg[i2]
                ms0 = (1 - f0) / (1 + uu / 2)
                ec, pc = ms0 * (1 + uu / 2), ms0 * uu / 2
                dec = dpc = 0.5 * rate * ms0 * uu
                den, dden = eg + ec, deg + dec
                if definition == "ratio":
                    num, dnum, shift = p3g + pc, dp3g + dpc, 0.0
                else:
                    # w_eff(A) numerator P3 + (beta/2 - 1)(P0 + 3 Pt)/3: the condensate has P3 = Pt = P0 = P_c
                    num = p3g + pc + (0.5 * BETA - 1.0) * 4.0 * pc / 3.0
                    dnum = dp3g + dpc + (0.5 * BETA - 1.0) * 4.0 * dpc / 3.0
                    shift = 0.0 if definition == "A_B" else SHIFT_C
                w0 = num / den + shift
                wa = -(dnum * den - num * dden) / den ** 2
                dist = np.hypot(w0 - UNITE["w0"], wa - UNITE["wa"])
                j = int(np.argmin(dist))
                if dist[j] < best["distance"]:
                    best = {"distance": float(dist[j]), "a4_today": t2, "w_c_today": float(wcs[j]),
                            "gas_fraction": float(f0), "w0": float(w0[j]), "wa": float(wa[j])}
                near = np.abs(w0 - UNITE["w0"]) <= 0.1
                if np.any(near):
                    min_wa_near = min(min_wa_near, float(np.min(wa[near])))
                    max_wa_near = max(max_wa_near, float(np.max(wa[near])))
        scans[definition] = {"min_wa_with_w0_within_0p1_of_unite": r(min_wa_near),
                             "max_wa_with_w0_within_0p1_of_unite": r(max_wa_near),
                             "closest": {k: (r(v) if isinstance(v, float) else v) for k, v in best.items()}}
    check("mixture_scan_three_definitions", all(math.isfinite(scans[k]["closest"]["distance"]) for k in scans),
          f"free gas (N = {nl}, lambda = 0) + condensate with ratio w_c in [-3, 0.99] today (drifting: u ~ e^(-(5/3) a4)), "
          "gas fraction in [0, 1], a4_today in " + str(TODAY) + ": closest points to the Unite pair (-0.861, -0.60): " +
          "; ".join(f"{k}: w0 = {scans[k]['closest']['w0']}, wa = {scans[k]['closest']['wa']} (distance "
                    f"{scans[k]['closest']['distance']})" for k in scans) +
          "; the mixtures with |w0 + 0.861| <= 0.1 have wa in: " +
          ", ".join(f"{k} [{scans[k]['min_wa_with_w0_within_0p1_of_unite']}, "
                    f"{scans[k]['max_wa_with_w0_within_0p1_of_unite']}]" for k in scans))

    # ---- the expansion-inferred w of the observer on the prescribed history
    expl = {"w_exp": "-1 - (2/3) a4''/a4'^2", "prescribed_history_a4_linear": -1.0,
            "statement": "on the history a4 = H x4 (with b4 = e^((4/3) H x4)) the 3-space observer's Hubble rate a4' = H is "
                         "constant (b4 does not enter a = e^{a4}): the expansion itself reads as w_exp = -1 exactly; the "
                         "Kohn-Sham states are not admissible sources of the a4 equations "
                         "(Revision/field_equations_a4/reports/ks-source-conditions.json), so no self-consistent history is "
                         "available (OPEN)"}

    # ---- the comparison with the Unite values (labelled interpretation)
    gas_series = [q for q in summary_series if q.get("N") != 8 and "w_eff_C_range" in q]
    tan_wa = [t_["w_eff_C"]["wa"] for q in gas_series for t_ in q["cplTangent"]]
    fit_wa = [f_["w_eff_C"]["wa"] for q in gas_series for f_ in q["cplFits"]]
    wc_all = [v for q in gas_series for v in q["w_eff_C_range"]]
    check("gas_cpl_far_from_unite", max(abs(v) for v in tan_wa + fit_wa) < abs(UNITE["wa"]) and min(wc_all) > UNITE["w0"],
          f"Kohn-Sham gas (N != 8, all lambda): tangent wa in [{min(tan_wa):.6f}, {max(tan_wa):.6f}], least-squares fit wa in "
          f"[{min(fit_wa):.6f}, {max(fit_wa):.6f}] (|wa| far below the Unite 0.60); w_eff(C) in [{min(wc_all):.6f}, "
          f"{max(wc_all):.6f}] (never near -0.861)")
    unite_cmp = {
        "unite": UNITE,
        "kohn_sham_gas": {
            "A_B": "w_eff(A) = 1/3 exactly for the free gas (fold band); interacting gas in the range of check "
                   "interacting_gas_ranges; no dark-energy value",
            "C": f"w_eff(C) = w_eff(A) - 4/9 in [{min(wc_all):.4f}, {max(wc_all):.4f}] (all gas series); tangent wa in "
                 f"[{min(tan_wa):.4f}, {max(tan_wa):.4f}], fitted wa in [{min(fit_wa):.4f}, {max(fit_wa):.4f}]; not the "
                 f"Unite values"},
        "condensate": f"the condensate drifts: u = lambda S/m ~ e^(-(5/3) a4); at the u that gives the ratio -0.764 today its "
                      f"wa is {wa_ratio:.4f} (thawing sign), w_eff(A) = (5/9) w_c = {kA * wc0:.4f}, w_eff(C) = (5/9) w_c - 4/9 "
                      f"= {kA * wc0 + SHIFT_C:.4f}, both with wa = {kA * wa_ratio:.4f}",
        "mixtures": "free gas + lambda = 0 condensate: w_eff(C) >= -4/9, the Unite values are not reached; free gas + a "
                    "drifting condensate: closest points to (-0.861, -0.60) in the three definitions in mixture_scan",
        "label": "INTERPRETATION (labelled): the comparison treats the Unite numbers as constraints on the dilution of "
                 "a 4-dimensional effective density; the Kohn-Sham history is a prescribed background without "
                 "back-reaction"}

    fails = [c for c in CHECKS if c["verdict"] != "PASS"]
    summary = {
        "producer": "Revision/dark_sector/dirac16complex/compute/compute_eos.py",
        "metric": "the corrected primordial metric of 2026-10-16 (version 2)",
        "inputs": ["outputs/ks-history-dense.csv (run_ks_history.py, Rust Kohn-Sham solver)",
                   "outputs/effective-formulas.json (derive_effective.py, sympy)"],
        "definitions": formulas["wEff"], "rho4": formulas["rho4"],
        "history": "a4 = H x4 and b4 = e^((4/3) H x4) PRESCRIBED (test field, no back-reaction); beta = 4/3; slices a4 in "
                   f"[0, {a4g[-1]:g}]; a = e^(a4 - a4_today)",
        "beta": BETA, "zeroSeries": zero_series,
        "series": summary_series, "condensate": cond, "mixtures_free_gas_today_last_slice": mix,
        "mixture_C_lambda0_condensate_min_w_eff_C": r(wC_min),
        "mixture_scan": scans,
        "expansion_inferred": expl, "unite_comparison": unite_cmp,
        "checks": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails)}}
    with open(OUT_SUM, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(summary, indent=1) + "\n")
    with open(OUT_HIST, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("series,N,lambda_hat,a4,E,P3,Pt,P0,w_eff_A_B,w_eff_C,w3,wt,wx0,dw_eff_da4,dw3_da4\n")
        for row in hist_rows:
            fh.write(",".join([row[0], str(row[1])] + [f"{float(v):.15e}" for v in row[2:]]) + "\n")
    rep = {"producer": "Revision/dark_sector/dirac16complex/compute/compute_eos.py", "checks": CHECKS,
           "summary": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails), "fail": len(fails)}}
    with open(OUT_REP, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rep, indent=1) + "\n")
    for c in CHECKS:
        print(f"{c['verdict']} - {c['name']}: {c['detail']}")
    print(f"{len(CHECKS) - len(fails)}/{len(CHECKS)} checks pass")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
