#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/compute/compute_eos.py - the equation of state a 3-space observer infers for
dirac16complex as the extra times deflate and 3-space inflates (SPEC sections 8, 11): (i) the Kohn-Sham fermion
gas (instantaneous states along a4, outputs/ks-history-dense.csv of run_ks_history.py), (ii) the homogeneous
condensate (exact solution), (iii) mixtures; CPL tangents and fits; comparison with the Supernovae Unite values.

Coordinates as the author names them: x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time;
x5, x6, x7 = the three exponentially DEFLATING extra times (time-like; scale factor e^{-a4} sin^{1/6} z);
x8 = hidden direction.  Observer scale factor a = e^{a4 - a4_today}.

Every formula used here is derived exactly in derive/derive_effective.py (outputs/effective-formulas.json):
  E, P3, Pt, P8 = proper 7-volume integrals 2 Vol_7 int e^{6Hy} (rho, p3, p_t, p8) dy of the doubled
  (universe + Z2 image) system, X = P3 - Pt, conservation dE/da4 = -3 X (fixed occupations);
  w_eff(A) = w_eff(B) = X/E (extra times compact with fixed coordinate period, ASSUMPTION; or per unit extra-time
  coordinate volume), w_eff(C) = X/E - 1 (per unit proper 7-volume); ratios w3 = P3/E, wt = Pt/E, w8 = P8/E;
  CPL w(a) = w0 + wa (1 - a): tangent w0 = w(1), wa = -dw/da4 at a4_today; least-squares fits over a in [a1, 1].
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
        g = lambda c: np.array([float(q[c]) for q in rs])
        out[key] = {"a4": g("a4"), "E": g("int_rho"), "P3": g("int_p3"), "Pt": g("int_p_t"), "P8": g("int_p8"),
                    "lambda": float(rs[0]["lambda"])}
    return out


def main():
    formulas = json.loads(FORMULAS.read_text(encoding="utf-8"))
    check("formulas_input_present", formulas["wEff"]["A"] == "(P3 - Pt)/E" and formulas["wEff"]["C"] == "(P3 - Pt)/E - 1",
          "outputs/effective-formulas.json (derive_effective.py): w_eff(A) = (P3 - Pt)/E, w_eff(C) = (P3 - Pt)/E - 1")
    S = load()
    check("dense_history_complete", len(S) == 15 and all(len(v["a4"]) == 41 for v in S.values()),
          f"{len(S)} series x 41 slices from outputs/ks-history-dense.csv")
    h = 0.05
    hist_rows = []
    summary_series = []
    worst_cons, worst_int, worst_dw = 0.0, 0.0, 0.0
    for key in sorted(S, key=lambda k: (k[0], TAGS.index(k[1]))):
        d = S[key]
        a4, E, P3, Pt, P8 = d["a4"], d["E"], d["P3"], d["Pt"], d["P8"]
        X = P3 - Pt
        sid = f"N{key[0]}_{key[1]}"
        if np.max(np.abs(E)) == 0.0:
            summary_series.append({"series": sid, "N": key[0], "lambda": d["lambda"],
                                   "status": "E = 0 and X = 0 at every slice (the k = 0 brane zero modes have eps = 0 "
                                             "and no interaction): no energy, w undefined"})
            continue
        # conservation dE/da4 = -3 X (pointwise in a4) and integrated (Simpson on pairs of intervals)
        dE = deriv(E, h)
        scale = np.max(np.abs(E))
        dev = np.max(np.abs(dE + 3 * X)[2:-2]) / scale
        worst_cons = max(worst_cons, dev)
        integ = 0.0
        devint = 0.0
        for i in range(0, 40, 2):
            integ += h / 3 * (X[i] + 4 * X[i + 1] + X[i + 2])
            devint = max(devint, abs(E[i + 2] - E[0] + 3 * integ) / scale)
        worst_int = max(worst_int, devint)
        wA = X / E
        wC = wA - 1
        w3, wt, w8 = P3 / E, Pt / E, P8 / E
        dwA = deriv(wA, h)
        dX = deriv(X, h)
        dwA_id = dX / E + 3 * wA ** 2                       # identity d(X/E)/da4 = X'/E + 3 (X/E)^2
        worst_dw = max(worst_dw, float(np.max(np.abs(dwA - dwA_id))))
        dw3 = deriv(w3, h)
        for i in range(41):
            hist_rows.append([sid, key[0], d["lambda"], a4[i], E[i], P3[i], Pt[i], P8[i], wA[i], wC[i], w3[i], wt[i],
                              w8[i], dwA[i], dw3[i]])
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
                         "w_eff_C": {"w0": r(w0A - 1), "wa": r(waA), "w_const": r(wcA - 1)},
                         "ratio_w3": {"w0": r(w0r), "wa": r(war), "w_const": r(wcr)}})
        summary_series.append({
            "series": sid, "N": key[0], "lambda": d["lambda"],
            "w_eff_A_B_range": [r(float(np.min(wA))), r(float(np.max(wA)))],
            "w_eff_C_range": [r(float(np.min(wC))), r(float(np.max(wC)))],
            "ratio_w3_range": [r(float(np.min(w3))), r(float(np.max(w3)))],
            "ratio_wt_range": [r(float(np.min(wt))), r(float(np.max(wt)))],
            "ratio_w8_range": [r(float(np.min(w8))), r(float(np.max(w8)))],
            "dlnE_da4_at_0_and_2": [r(float(dE[0] / E[0])), r(float(dE[-1] / E[-1]))],
            "sign_of_E": "positive" if np.all(E > 0) else ("negative" if np.all(E < 0) else "mixed"),
            "cplTangent": tang, "cplFits": fits,
            "conservation_rel_dev": r(dev, 3), "conservation_integrated_rel_dev": r(devint, 3)})

    check("conservation_dE_da4_equals_minus_3X", worst_cons <= 1e-6,
          f"4th-order finite differences of E on the dense grid vs -3 (P3 - Pt) from the solver's EMT integrals: "
          f"max |dE/da4 + 3X|/max|E| = {worst_cons:.3e} (interior slices, all series)")
    check("conservation_integrated_simpson", worst_int <= 1e-7,
          f"E(a4) - E(0) = -3 int_0^a4 (P3 - Pt): max relative deviation {worst_int:.3e}")
    check("derivative_two_ways", worst_dw <= 1e-5,
          f"d(X/E)/da4 by finite differences vs the identity X'/E + 3 (X/E)^2 at every slice (one-sided 4th-order "
          f"stencils at the ends): max deviation {worst_dw:.3e}")

    # ---- the canonical gas series and the physical statements
    gas = {k: v for k, v in S.items() if k[0] in (136, 688)}
    wA_all = np.concatenate([(v["P3"] - v["Pt"]) / v["E"] for v in gas.values()])
    check("gas_radiation_like_band", float(np.min(wA_all)) > 0.29 and float(np.max(wA_all)) < 1.0 / 3.0,
          f"Kohn-Sham gas N = 136, 688 (all lambda): X/E in [{np.min(wA_all):.6f}, {np.max(wA_all):.6f}], below 1/3 "
          f"and above 0.29 at every slice a4 in [0, 2]")
    rising = all(np.all(np.diff((v["P3"] - v["Pt"]) / v["E"]) > 0) for v in gas.values())
    check("gas_X_over_E_rises_toward_one_third", rising,
          "X/E increases monotonically with a4 for every N = 136, 688 series: w_eff(A) rises toward 1/3 "
          "(radiation), it does not fall toward 0 (dust)")
    n8 = [S[(8, t)] for t in TAGS if t != "lam0"]
    n8ok = all(np.max(np.abs(v["E"] - v["E"][0])) <= 1e-12 * abs(v["E"][0]) and
               np.max(np.abs(v["P3"] - v["Pt"])) <= 1e-12 * abs(v["E"][0]) for v in n8)
    check("n8_interacting_zero_modes_constant", n8ok,
          "N = 8, lambda != 0 (only the k = 0 brane zero modes): E constant and P3 = Pt at every slice: "
          "w_eff(A) = 0, w_eff(C) = -1, constant (condensate-like, no time variation)")

    # ---- condensate (exact)
    u = -382.0 / 441.0
    cond = {"rho": "m S + lambda S^2/2", "p3=p_t=p8": "lambda S^2/2", "w_eff_A_B": 0.0, "w_eff_C": -1.0,
            "ratio_w": "u/(2 + u), u = lambda S/m (constant)", "wa_every_definition": 0.0,
            "u_for_ratio_minus_0p764": r(u), "ratio_check": r(u / (2 + u)),
            "phantom_ratio_window": "ratio < -1 iff -2 < u < -1 (attractive lambda S < 0; rho = m S (1 + u/2) > 0 "
                                    "iff m S > 0): an 8-dimensional phantom ratio is possible but constant",
            "history": "exact solution only on the linear member a4 = A H x4 + a0 (p3 = p_t forces a4'' = 0, "
                       "Revision/field_equations_a4); the 3-space observer's expansion-inferred w_exp = -1 exactly"}
    check("condensate_ratio_value", abs(u / (2 + u) + 0.764) < 1e-15, f"u = -382/441: ratio {u / (2 + u):.15f}")

    # ---- mixtures: gas (N = 688, lambda = 0, the largest canonical gas) + condensate (X = 0, E_c constant)
    g = S[(688, "lam0")]
    a4g, Eg, Xg, P3g = g["a4"], g["E"], g["P3"] - g["Pt"], g["P3"]
    mix = []
    t = 2.0
    it = int(round(t / h))
    best = None
    for f0 in [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        Ec = Eg[it] * (1 - f0) / f0                     # gas fraction f0 = E_g/(E_g + E_c) at a4_today = 2
        wmA = Xg / (Eg + Ec)
        dwm = deriv(wmA, h)
        entry = {"gas_fraction_today": f0, "w_eff_A_B": {"w0": r(wmA[it]), "wa": r(-dwm[it])},
                 "w_eff_C": {"w0": r(wmA[it] - 1), "wa": r(-dwm[it])}}
        for a1 in (0.5, 1.0 / 3.0):
            w0f, waf, wcf = cpl_fit(lambda aa, wm=wmA: interp(a4g, wm, t + np.log(aa)), a1)
            entry[f"fit_a1_{a1:.4f}"] = {"A_B": {"w0": r(w0f), "wa": r(waf), "w_const": r(wcf)},
                                        "C": {"w0": r(w0f - 1), "wa": r(waf), "w_const": r(wcf - 1)}}
        mix.append(entry)
    # gas fraction that makes w_eff(C) = -0.861 today (closed form) and its wa
    target = 1 + UNITE["w0"]                         # X/(E_g + E_c) = 0.139
    Ec861 = Xg[it] / target - Eg[it]
    f861 = Eg[it] / (Eg[it] + Ec861)
    wm861 = Xg / (Eg + Ec861)
    wa861 = -deriv(wm861, h)[it]
    check("mixture_C_w0_unite_has_positive_wa", f861 > 0 and wa861 > 0,
          f"gas + condensate, normalisation C, a4_today = 2: w_eff(C) = -0.861 today needs gas fraction "
          f"{f861:.6f}; then wa = {wa861:.6f} > 0 (freezing), Unite wa = -0.60")
    # constant-w fit (C, a in [1/3, 1]) equal to -0.764: bisection in the gas fraction
    def wconst_C(f0):
        Ec = Eg[it] * (1 - f0) / f0
        return cpl_fit(lambda aa: interp(a4g, Xg / (Eg + Ec), t + np.log(aa)), 1.0 / 3.0)[2] - 1
    lo, hi = 1e-6, 1.0
    if (wconst_C(lo) - UNITE["w_const"]) * (wconst_C(hi) - UNITE["w_const"]) < 0:
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if (wconst_C(lo) - UNITE["w_const"]) * (wconst_C(mid) - UNITE["w_const"]) <= 0:
                hi = mid
            else:
                lo = mid
        f764 = 0.5 * (lo + hi)
        Ec = Eg[it] * (1 - f764) / f764
        w0f, waf, wcf = cpl_fit(lambda aa: interp(a4g, Xg / (Eg + Ec), t + np.log(aa)), 1.0 / 3.0)
        const764 = {"gas_fraction_today": r(f764), "w_const_C": r(wcf - 1), "cpl_fit_C": {"w0": r(w0f - 1), "wa": r(waf)}}
    else:
        const764 = None
    check("mixture_C_constant_w_unite_reachable_only_with_freezing_cpl",
          const764 is not None and const764["cpl_fit_C"]["wa"] > 0,
          f"a constant-w fit (C, a in [1/3, 1]) of -0.764 is reached at a gas fraction "
          f"{const764['gas_fraction_today'] if const764 else None}; its CPL fit has wa = "
          f"{const764['cpl_fit_C']['wa'] if const764 else None} > 0, opposite in sign to the Unite wa = -0.60")

    # ---- ratio definition with a condensate of arbitrary ratio w_c: scan (exact mixing rule w = f w3_g + (1 - f) w_c)
    w3g = P3g / Eg
    dw3g = deriv(w3g, h)
    wAg = Xg / Eg
    scan_best = {"distance": float("inf")}
    min_wa_near = float("inf")
    for t2 in TODAY:
        i2 = int(round(t2 / h))
        for wc in np.linspace(-3.0, 1.0, 401):
            for f0 in np.linspace(0.0, 1.0, 201):
                w0 = f0 * w3g[i2] + (1 - f0) * wc
                fprime = -3 * f0 * (1 - f0) * wAg[i2]
                wa = -(f0 * dw3g[i2] + (w3g[i2] - wc) * fprime) + 0.0
                dist = math.hypot(w0 - UNITE["w0"], wa - UNITE["wa"])
                if dist < scan_best["distance"]:
                    scan_best = {"distance": dist, "a4_today": t2, "w_c": float(wc), "gas_fraction": float(f0),
                                 "w0": w0, "wa": wa}
                if abs(w0 - UNITE["w0"]) <= 0.1:
                    min_wa_near = min(min_wa_near, wa)
    check("ratio_mixture_scan_cannot_reach_unite_wa", min_wa_near > -0.1,
          f"ratio definition, gas (N = 688) + condensate with any constant ratio w_c in [-3, 1], gas fraction in "
          f"[0, 1], a4_today in {TODAY}: among mixtures with |w0 + 0.861| <= 0.1 the smallest wa is "
          f"{min_wa_near:.6f}; closest point to (-0.861, -0.60): w0 = {scan_best['w0']:.6f}, wa = "
          f"{scan_best['wa']:.6f} (distance {scan_best['distance']:.6f})")

    # ---- the expansion-inferred w of the observer on the prescribed history
    expl = {"w_exp": "-1 - (2/3) a4''/a4'^2", "prescribed_history_a4_linear": -1.0,
            "statement": "on the history a4 = A H x4 used by the Kohn-Sham record (and the only history the exact "
                         "condensate allows) the 3-space observer's Hubble rate a4' = A H is constant: the expansion "
                         "itself reads as w_exp = -1 exactly, with no time variation; the Kohn-Sham states are not "
                         "admissible sources of the a4 equations (Revision/field_equations_a4/reports/"
                         "ks-source-conditions.json), so no self-consistent non-linear history is available (OPEN)"}

    # ---- the comparison with the Unite values (labelled interpretation)
    gas688 = next(s for s in summary_series if s["series"] == "N688_lam0")
    gas_series = [q for q in summary_series if q.get("N") in (136, 688)]
    tan_wa = [t_["w_eff_C"]["wa"] for q in gas_series for t_ in q["cplTangent"]]
    fit_wa = [f_["w_eff_C"]["wa"] for q in gas_series for f_ in q["cplFits"]]
    wc_all = [v for q in gas_series for v in q["w_eff_C_range"]]
    check("gas_cpl_thawing_sign_small", max(tan_wa) < 0 and max(fit_wa) < 0 and min(fit_wa) > -0.05,
          f"Kohn-Sham gas (N = 136, 688, all lambda): tangent wa in [{min(tan_wa):.6f}, {max(tan_wa):.6f}], "
          f"least-squares fit wa in [{min(fit_wa):.6f}, {max(fit_wa):.6f}] (all < 0: thawing sign; |wa| far below "
          f"the Unite 0.60); w_eff(C) in [{min(wc_all):.6f}, {max(wc_all):.6f}]")
    unite_cmp = {
        "unite": UNITE,
        "kohn_sham_gas": {
            "A_B": f"w_eff = X/E in {gas688['w_eff_A_B_range']} (N = 688, lambda = 0): radiation-like, rising toward 1/3; "
                   "no dark-energy value",
            "C": f"w_eff = X/E - 1 in [{min(wc_all):.4f}, {max(wc_all):.4f}] (all gas series); tangent wa in "
                 f"[{min(tan_wa):.4f}, {max(tan_wa):.4f}], fitted wa in [{min(fit_wa):.4f}, {max(fit_wa):.4f}] "
                 "(thawing sign, magnitude far below 0.60); w never near -0.861 or below -1; not the Unite values",
            "ratio": f"P3/E in {gas688['ratio_w3_range']}: radiation-like"},
        "condensate": "w_eff(A, B) = 0, w_eff(C) = -1, ratio u/(2 + u): all constant (wa = 0); the ratio can equal "
                      "-0.764 (u = -382/441) but the observer's dilution-inferred w_eff is 0 or -1",
        "mixtures": "gas + condensate: w moves toward the condensate's value as the gas redshifts (wa > 0, freezing) "
                    "in every definition; the Unite thawing pair (wa = -0.60) is not reached (scan above)",
        "phantom": "w_eff(C) < -1 or w_eff(A) < 0 needs (P3 - Pt)/E < 0; every computed state has P3 - Pt >= 0 and "
                   "E > 0 except the N = 8, lambda > 0 states (E < 0, X = 0: w_eff = -1 or 0 exactly)",
        "label": "INTERPRETATION (labelled): the comparison treats the Unite numbers as constraints on the dilution of "
                 "a 4-dimensional effective density; the Kohn-Sham history is a prescribed background without "
                 "back-reaction"}

    fails = [c for c in CHECKS if c["verdict"] != "PASS"]
    summary = {
        "producer": "Revision/dark_sector/dirac16complex/compute/compute_eos.py",
        "inputs": ["outputs/ks-history-dense.csv (run_ks_history.py, Rust Kohn-Sham solver)",
                   "outputs/effective-formulas.json (derive_effective.py, sympy)"],
        "definitions": formulas["wEff"], "rho4": formulas["rho4"],
        "history": "a4 = A H x4 PRESCRIBED (test field, no back-reaction); slices a4 in [0, 2]; a = e^{a4 - a4_today}",
        "series": summary_series, "condensate": cond, "mixtures_N688_lam0_today_a4_2": mix,
        "mixture_C_w0_minus_0p861": {"gas_fraction_today": r(f861), "wa": r(wa861)},
        "mixture_C_const_fit_minus_0p764": const764,
        "ratio_mixture_scan": {"min_wa_with_w0_within_0p1_of_unite": r(min_wa_near),
                               "closest": {k: (r(v) if isinstance(v, float) else v) for k, v in scan_best.items()}},
        "expansion_inferred": expl, "unite_comparison": unite_cmp,
        "checks": {"total": len(CHECKS), "pass": len(CHECKS) - len(fails)}}
    with open(OUT_SUM, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(summary, indent=1) + "\n")
    with open(OUT_HIST, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("series,N,lambda,a4,E,P3,Pt,P8,w_eff_A_B,w_eff_C,w3,wt,w8,dw_eff_da4,dw3_da4\n")
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
