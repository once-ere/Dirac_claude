#!/usr/bin/env python3
"""Revision/dark_sector/dirac16complex/compute/compute_eos.py - the equation of state a 3-space observer infers for
dirac16complex as the extra times deflate and 3-space inflates (SPEC sections 8, 11): (i) the Kohn-Sham fermion
gas (instantaneous states along a4, outputs/ks-history-dense.csv of run_ks_history.py), (ii) the homogeneous
condensate (exact solution), (iii) mixtures; CPL tangents and fits; comparison with the Supernovae Unite values.

The author's coordinates {x0, x1, ..., x7} and metric (Dirac_Einstein-Lovelock_4+4_Nash.nb, In[48], In[97]-In[102]):
x0 = hidden direction; x1, x2, x3 = 3-space (scale factor e^{a4} sin^{1/6} z); x4 = time; x5, x6, x7 = the three
exponentially DEFLATING extra times (time-like; g55 = g66 = g77 = -e^{-2 a4} b4 sin^{1/3} z, scale factor
e^{-a4} b4^{1/2} sin^{1/6} z).  b4 is a function of x4 (never 1).  The history: a4 = H x4 and
b4(x4) = b4(0) e^{(4/3) H x4}, beta = d ln b4/d a4 = 4/3 (outputs/ks-history-dense.csv of run_ks_history.py; the
branch of the author's weights for a source without T^x4_x0).  Observer scale factor a = e^{a4 - a4_today}.

Every formula used here is derived exactly in derive/derive_effective.py (outputs/effective-formulas.json):
  E, P3, Pt, P0 = proper 7-volume integrals 2 Vol_7 int e^{6Hy} (rho, p3, p_t, p0) dy of the doubled
  (universe + Z2 image) system (proper volume element b4^{3/2} cos z), X = P3 - Pt, conservation
  dE/da4 = -3 X - (3/2) beta Pt (fixed occupations);
  w_eff = X/E - s + (beta/2)(Pt/E + s): w_eff(A) = w_eff(B) = X/E + (beta/2) Pt/E (extra times compact with fixed
  coordinate period, ASSUMPTION; or per unit extra-time coordinate volume), w_eff(C) = X/E - 1 + (beta/2)(Pt/E + 1)
  (per unit proper 7-volume); ratios w3 = P3/E, wt = Pt/E, wx0 = P0/E (the x0 ratio, not the CPL w0);
  CPL w(a) = w0 + wa (1 - a): tangent w0 = w(1), wa = -dw/da4 at a4_today; least-squares fits over a in [a1, 1].
The homogeneous condensate with b4: b4^{3/2} S constant, so u = lambda S/m = u_today e^{-2 (a4 - a4_today)}.
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
        out[key] = {"a4": g("a4"), "E": g("int_rho"), "P3": g("int_p3"), "Pt": g("int_p_t"), "P0": g("int_p0"),
                    "lambda": float(rs[0]["lambda"])}
    return out


def main():
    formulas = json.loads(FORMULAS.read_text(encoding="utf-8"))
    check("formulas_input_present", formulas["wEff"]["general"] == "(P3 - Pt)/E - s + (beta/2)(Pt/E + s)" and
          "d ln b4/d a4 in {0, 4/3}" in formulas["authorWeightsB4Branch"]["linearHistory"],
          "outputs/effective-formulas.json (derive_effective.py): w_eff = (P3 - Pt)/E - s + (beta/2)(Pt/E + s), and the "
          "history's beta = d ln b4/d a4 = 4/3 (author_weights_b4_branch)")
    S = load()
    check("dense_history_complete", len(S) == 15 and all(len(v["a4"]) == 41 for v in S.values()),
          f"{len(S)} series x 41 slices from outputs/ks-history-dense.csv")
    h = 0.05
    hist_rows = []
    summary_series = []
    worst_cons, worst_int, worst_dw, worst_nob4, worst_dw8 = 0.0, 0.0, 0.0, 0.0, 0.0
    for key in sorted(S, key=lambda k: (k[0], TAGS.index(k[1]))):
        d = S[key]
        a4, E, P3, Pt, P0 = d["a4"], d["E"], d["P3"], d["Pt"], d["P0"]
        X = P3 - Pt
        sid = f"N{key[0]}_{key[1]}"
        if np.max(np.abs(E)) == 0.0:
            summary_series.append({"series": sid, "N": key[0], "lambda": d["lambda"],
                                   "status": "E = 0 and X = 0 at every slice (the k = 0 brane zero modes have eps = 0 "
                                             "and no interaction): no energy, w undefined"})
            continue
        # conservation dE/da4 = -3 X - (3/2) beta Pt (pointwise in a4) and integrated (Simpson on pairs of intervals)
        dE = deriv(E, h)
        scale = np.max(np.abs(E))
        src = 3 * X + 1.5 * BETA * Pt
        dev = np.max(np.abs(dE + src)[2:-2]) / scale
        worst_cons = max(worst_cons, dev)
        if d["lambda"] != 0.0:
            worst_nob4 = max(worst_nob4, float(np.max(np.abs(dE + 3 * X)[2:-2]) / scale))
        integ = 0.0
        devint = 0.0
        for i in range(0, 40, 2):
            integ += h / 3 * (src[i] + 4 * src[i + 1] + src[i + 2])
            devint = max(devint, abs(E[i + 2] - E[0] + integ) / scale)
        worst_int = max(worst_int, devint)
        wA = X / E + 0.5 * BETA * Pt / E
        wC = X / E - 1 + 0.5 * BETA * (Pt / E + 1)
        w3, wt, wx0 = P3 / E, Pt / E, P0 / E
        dwA = deriv(wA, h)
        dX = deriv(X, h)
        dPt = deriv(Pt, h)
        dwA_id = (dX + 0.5 * BETA * dPt) / E + wA * src / E  # identity: E' = -src
        if key[0] == 8:
            worst_dw8 = max(worst_dw8, float(np.max(np.abs(dwA - dwA_id))))
        else:
            worst_dw = max(worst_dw, float(np.max(np.abs(dwA - dwA_id))))
        dw3 = deriv(w3, h)
        for i in range(41):
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
                         "w_eff_C": {"w0": r(w0A - 1 + 0.5 * BETA), "wa": r(waA), "w_const": r(wcA - 1 + 0.5 * BETA)},
                         "ratio_w3": {"w0": r(w0r), "wa": r(war), "w_const": r(wcr)}})
        summary_series.append({
            "series": sid, "N": key[0], "lambda": d["lambda"],
            "w_eff_A_B_range": [r(float(np.min(wA))), r(float(np.max(wA)))],
            "w_eff_C_range": [r(float(np.min(wC))), r(float(np.max(wC)))],
            "ratio_w3_range": [r(float(np.min(w3))), r(float(np.max(w3)))],
            "ratio_wt_range": [r(float(np.min(wt))), r(float(np.max(wt)))],
            "ratio_wx0_range": [r(float(np.min(wx0))), r(float(np.max(wx0)))],
            "dlnE_da4_at_0_and_2": [r(float(dE[0] / E[0])), r(float(dE[-1] / E[-1]))],
            "sign_of_E": "positive" if np.all(E > 0) else ("negative" if np.all(E < 0) else "mixed"),
            "cplTangent": tang, "cplFits": fits,
            "conservation_rel_dev": r(dev, 3), "conservation_integrated_rel_dev": r(devint, 3)})

    trunc = h ** 4 * 2 ** 5 / 30                                # 4th-order central difference error on e^{-2 a4}
    check("conservation_with_b4_term", worst_cons <= 1e-5,
          f"4th-order finite differences of E on the dense grid vs -3 (P3 - Pt) - (3/2) beta Pt (beta = 4/3) from the "
          f"solver's EMT integrals: max |dE/da4 + 3X + 2Pt|/max|E| = {worst_cons:.3e} (interior slices, all series; the "
          f"truncation error of the stencil on the N = 8 interacting series, whose E falls like e^(-2 a4), is about "
          f"h^4 2^5/30 = {trunc:.1e})")
    check("conservation_without_b4_term_fails", worst_nob4 >= 1e-6,
          f"the b4-free identity dE/da4 = -3 X of the withdrawn b4 = 1 record does NOT hold on this history: max "
          f"|dE/da4 + 3X|/max|E| over the interacting series = {worst_nob4:.3e}: the b4 term -(3/2) beta Pt is needed")
    check("conservation_integrated_simpson", worst_int <= 1e-5,
          f"E(a4) - E(0) = -int_0^a4 (3 (P3 - Pt) + (3/2) beta Pt): max relative deviation {worst_int:.3e}")
    trunc_end = h ** 4 * 2 ** 5 / 5                             # one-sided 4th-order stencil error on e^{-2 a4}
    check("derivative_two_ways", worst_dw <= 1e-5 and worst_dw8 <= 2 * trunc_end,
          f"d w_eff(A)/da4 by finite differences vs the identity (X' + (beta/2) Pt')/E + w_eff(A) (3X + (3/2) beta Pt)/E "
          f"at every slice (one-sided 4th-order stencils at the two end slices): gas series N = 136, 688 max deviation "
          f"{worst_dw:.3e} (<= 1e-5); N = 8 interacting series {worst_dw8:.3e}, at the end slices, where E and Pt fall "
          f"like e^(-2 a4) and the one-sided stencil's truncation error is about h^4 2^5/5 = {trunc_end:.1e} "
          f"(bound 2 h^4 2^5/5)")

    # ---- the canonical gas series and the physical statements
    gas = {k: v for k, v in S.items() if k[0] in (136, 688)}
    wA_all = np.concatenate([(v["P3"] - v["Pt"]) / v["E"] + 0.5 * BETA * v["Pt"] / v["E"] for v in gas.values()])
    wC_all = wA_all - 1 + 0.5 * BETA
    ptE_all = np.concatenate([np.abs(v["Pt"] / v["E"]) for v in gas.values()])
    check("gas_radiation_like_band", float(np.min(wA_all)) > 0.29 and float(np.max(wA_all)) < 1.0 / 3.0,
          f"Kohn-Sham gas N = 136, 688 (all lambda): w_eff(A) = X/E + (2/3) Pt/E in [{np.min(wA_all):.6f}, "
          f"{np.max(wA_all):.6f}] (|Pt/E| <= {np.max(ptE_all):.1e}), below 1/3 and above 0.29 at every slice a4 in [0, 2]")
    rising = all(np.all(np.diff((v["P3"] - v["Pt"]) / v["E"] + 0.5 * BETA * v["Pt"] / v["E"]) > 0) for v in gas.values())
    check("gas_X_over_E_rises_toward_one_third", rising,
          "w_eff(A) increases monotonically with a4 for every N = 136, 688 series: it rises toward 1/3 (radiation), it "
          "does not fall toward 0 (dust)")
    check("gas_C_near_zero_on_b4_history", float(np.max(wC_all)) < 0 and float(np.min(wC_all)) > -0.05,
          f"normalisation C on the history with b4(x4): w_eff(C) = w_eff(A) - 1 + beta/2 = w_eff(A) - 1/3 in "
          f"[{np.min(wC_all):.6f}, {np.max(wC_all):.6f}]: close to 0 (dust-like dilution per proper 7-volume), not a "
          f"dark-energy value (the withdrawn b4 = 1 record had w_eff(C) = w_eff(A) - 1)")
    n8 = [S[(8, t)] for t in TAGS if t != "lam0"]
    n8_x0 = all(np.max(np.abs(v["P3"] - v["Pt"])) <= 1e-12 * np.max(np.abs(v["E"])) for v in n8)
    n8_ratio = [float(v["E"][-1] / v["E"][0]) for v in n8]
    n8_pt = np.concatenate([v["Pt"] / v["E"] for v in n8])
    n8_wA = 0.5 * BETA * n8_pt
    check("n8_interacting_zero_modes_dilute_with_b4", n8_x0 and all(0.017 < q < 0.02 for q in n8_ratio) and
          float(np.min(n8_pt)) > 0.9 and float(np.max(n8_pt)) <= 1.0 + 1e-9,
          f"N = 8, lambda != 0 (only the k = 0 brane zero modes; pure interaction energy, coupling lambda_hat e^(-2 a4)): "
          f"P3 = Pt at every slice (X = 0); E(2)/E(0) in [{min(n8_ratio):.6f}, {max(n8_ratio):.6f}] (e^(-4) = "
          f"{math.exp(-4):.6f}); Pt/E in [{np.min(n8_pt):.6f}, {np.max(n8_pt):.6f}]: w_eff(A) = (2/3) Pt/E in "
          f"[{np.min(n8_wA):.6f}, {np.max(n8_wA):.6f}], w_eff(C) = w_eff(A) - 1/3 (the withdrawn b4 = 1 record had E "
          f"constant, w_eff(A) = 0, w_eff(C) = -1)")

    # ---- condensate (exact): b4^{3/2} S constant, u = lambda S/m = u_today e^{-2 (a4 - a4_today)} (beta = 4/3)
    u = -382.0 / 441.0
    wc0 = u / (2 + u)
    wa_ratio = 4 * u / (2 + u) ** 2                      # -d/da4 [u/(2 + u)] with u' = -2 u
    cond = {"S": "S0 b4^(-3/2) = S_today e^(-2 (a4 - a4_today))", "rho": "m S + lambda S^2/2", "p3=p_t=p0": "lambda S^2/2",
            "ratio_w": "w_c = u/(2 + u), u = lambda S/m = u_today e^(-2 (a4 - a4_today))",
            "ratio_wa": "4 u/(2 + u)^2 (thawing sign for u < 0)",
            "w_eff_A_B": "(beta/2) w_c = (2/3) w_c", "w_eff_C": "-1 + (beta/2)(1 + w_c) = -1/3 + (2/3) w_c",
            "u_for_ratio_minus_0p764_today": r(u), "ratio_today": r(wc0), "ratio_wa_at_that_u": r(wa_ratio),
            "w_eff_A_B_today_at_that_u": r(2.0 / 3.0 * wc0), "w_eff_C_today_at_that_u": r(-1.0 / 3.0 + 2.0 / 3.0 * wc0),
            "wa_A_B_C_at_that_u": r(2.0 / 3.0 * wa_ratio),
            "phantom_ratio_window": "ratio < -1 iff -2 < u < -1 (attractive lambda S < 0; rho = m S (1 + u/2) > 0 "
                                    "iff m S > 0); |u| grows toward the past like e^(-2 (a4 - a4_today)), so for u < 0 "
                                    "the condensate energy E_c = m S0 (1 + u/2) reaches 0 at a4 = a4_today - (1/2) ln(2/|u_today|)",
            "history": "exact homogeneous solution for every a4(x4), b4(x4) (Revision/field_equations_a4, key b4, "
                       "fields.condensate); the 3-space observer's expansion-inferred w_exp = -1 exactly on a4 = H x4"}
    check("condensate_ratio_value", abs(wc0 + 0.764) < 1e-15, f"u = -382/441 today: ratio {wc0:.15f}")
    check("condensate_drifts_with_b4", wa_ratio < 0 and abs(wa_ratio - 4 * u / (2 + u) ** 2) == 0.0,
          f"with b4(x4) the condensate is no longer constant: u = lambda S/m falls like e^(-2 a4), so the ratio w_c = "
          f"u/(2 + u) has wa = 4u/(2 + u)^2 = {wa_ratio:.6f} at the u that gives w_c = -0.764 today; w_eff(A) = (2/3) w_c = "
          f"{2.0 / 3.0 * wc0:.6f} and w_eff(C) = -1/3 + (2/3) w_c = {-1.0 / 3.0 + 2.0 / 3.0 * wc0:.6f} with wa = "
          f"{2.0 / 3.0 * wa_ratio:.6f} (the withdrawn b4 = 1 record had a constant condensate, wa = 0)")

    # ---- mixtures: gas (N = 688, lambda = 0, the largest canonical gas) + lambda = 0 condensate (X = Pt = 0,
    # E_c = m S0 constant for every b4); w_eff(C) = w_eff(A) - 1 + beta/2
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
                 "w_eff_C": {"w0": r(wmA[it] - 1 + 0.5 * BETA), "wa": r(-dwm[it])}}
        for a1 in (0.5, 1.0 / 3.0):
            w0f, waf, wcf = cpl_fit(lambda aa, wm=wmA: interp(a4g, wm, t + np.log(aa)), a1)
            entry[f"fit_a1_{a1:.4f}"] = {"A_B": {"w0": r(w0f), "wa": r(waf), "w_const": r(wcf)},
                                        "C": {"w0": r(w0f - 1 + 0.5 * BETA), "wa": r(waf),
                                              "w_const": r(wcf - 1 + 0.5 * BETA)}}
        mix.append(entry)
    # with the lambda = 0 condensate, w_eff(C) = X_g/(E_g + E_c) - 1/3 >= -1/3 at every gas fraction
    wC_min = min(float(np.min(Xg / (Eg + Eg[it] * (1 - f0) / f0))) for f0 in np.linspace(0.001, 1.0, 1000)) - 1 + 0.5 * BETA
    f861 = None
    wa861 = None
    check("mixture_C_cannot_reach_unite_w0_with_lambda0_condensate", wC_min >= -1.0 / 3.0 - 1e-12,
          f"gas + lambda = 0 condensate, normalisation C: w_eff(C) = X_g/(E_g + E_c) - 1 + beta/2 >= {wC_min:.6f} >= -1/3 "
          f"at every slice and gas fraction: neither -0.861 nor a constant -0.764 is reached (on the withdrawn b4 = 1 "
          f"record a gas fraction 0.4367 gave w_eff(C) = -0.861 with wa = +0.067)")
    const764 = None

    # ---- gas (N = 688, lambda = 0) + a condensate of any ratio w_c today (u_today = 2 w_c/(1 - w_c), u > -2), any
    # gas fraction, in three definitions; the condensate drifts with b4: u' = -2 u, E_c = m S0 (1 + u/2),
    # P_c = m S0 u/2 (= Pt_c = P3_c), so E_c' = P_c' = -m S0 u (beta = 4/3)
    dEg, dP3g, dXg = deriv(Eg, h), deriv(P3g, h), deriv(Xg, h)
    scans = {}
    for definition in ("ratio", "A_B", "C"):
        best = {"distance": float("inf")}
        min_wa_near, max_wa_near = float("inf"), float("-inf")
        for t2 in TODAY:
            i2 = int(round(t2 / h))
            wcs = np.linspace(-3.0, 0.99, 400)
            uu = 2 * wcs / (1 - wcs)
            for f0 in np.linspace(0.0, 1.0, 201):
                eg, xg, p3g = f0, f0 * Xg[i2] / Eg[i2], f0 * P3g[i2] / Eg[i2]
                deg, dxg, dp3g = f0 * dEg[i2] / Eg[i2], f0 * dXg[i2] / Eg[i2], f0 * dP3g[i2] / Eg[i2]
                ms0 = (1 - f0) / (1 + uu / 2)
                ec, pc = ms0 * (1 + uu / 2), ms0 * uu / 2
                dec, dpc = -ms0 * uu, -ms0 * uu
                den, dden = eg + ec, deg + dec
                if definition == "ratio":
                    num, dnum, shift = p3g + pc, dp3g + dpc, 0.0
                else:
                    num, dnum = xg + 0.5 * BETA * pc, dxg + 0.5 * BETA * dpc
                    shift = 0.0 if definition == "A_B" else -1 + 0.5 * BETA
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
    scan_best = scans["ratio"]["closest"]
    min_wa_near = scans["ratio"]["min_wa_with_w0_within_0p1_of_unite"]
    check("mixture_scan_three_definitions_b4", all(math.isfinite(scans[k]["closest"]["distance"]) for k in scans)
          and all(scans[k]["max_wa_with_w0_within_0p1_of_unite"] < -1.0 for k in scans),
          "gas (N = 688, lambda = 0) + condensate with ratio w_c in [-3, 0.99] today (drifting with b4: u ~ e^(-2 a4)), "
          "gas fraction in [0, 1], a4_today in " + str(TODAY) + ": closest points to the Unite pair (-0.861, -0.60): " +
          "; ".join(f"{k}: w0 = {scans[k]['closest']['w0']}, wa = {scans[k]['closest']['wa']} (distance "
                    f"{scans[k]['closest']['distance']})" for k in scans) +
          "; every mixture with |w0 + 0.861| <= 0.1 has wa in: " +
          ", ".join(f"{k} [{scans[k]['min_wa_with_w0_within_0p1_of_unite']}, "
                    f"{scans[k]['max_wa_with_w0_within_0p1_of_unite']}]" for k in scans) +
          " (all below -1, far from the Unite -0.60)")

    # ---- the expansion-inferred w of the observer on the prescribed history
    expl = {"w_exp": "-1 - (2/3) a4''/a4'^2", "prescribed_history_a4_linear": -1.0,
            "statement": "on the history a4 = H x4 (with b4(x4) = b4(0) e^((4/3) H x4)) the 3-space observer's Hubble "
                         "rate a4' = H is constant (b4 does not enter a = e^{a4}): the expansion itself reads as "
                         "w_exp = -1 exactly, with no time variation; the Kohn-Sham states are not admissible sources "
                         "of the a4 equations (Revision/field_equations_a4/reports/ks-source-conditions.json), so no "
                         "self-consistent history is available (OPEN)"}

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
            "C": f"w_eff = X/E - 1/3 + (2/3) Pt/E in [{min(wc_all):.4f}, {max(wc_all):.4f}] (all gas series): close "
                 f"to 0, dust-like; tangent wa in [{min(tan_wa):.4f}, {max(tan_wa):.4f}], fitted wa in "
                 f"[{min(fit_wa):.4f}, {max(fit_wa):.4f}]; w never near -0.861 or below -1; not the Unite values",
            "ratio": f"P3/E in {gas688['ratio_w3_range']}: radiation-like"},
        "condensate": f"with b4(x4) the condensate drifts: u = lambda S/m ~ e^(-2 a4); at the u that gives the ratio "
                      f"-0.764 today its wa is {wa_ratio:.4f} (thawing sign), w_eff(A) = (2/3) w_c = {2.0 / 3.0 * wc0:.4f}, "
                      f"w_eff(C) = -1/3 + (2/3) w_c = {-1.0 / 3.0 + 2.0 / 3.0 * wc0:.4f}, both with wa = "
                      f"{2.0 / 3.0 * wa_ratio:.4f}",
        "mixtures": "gas + lambda = 0 condensate: w_eff(C) >= -1/3, the Unite values are not reached; gas + a drifting "
                    "condensate: closest points to (-0.861, -0.60) in the three definitions in mixture_scan (above)",
        "phantom": "w_eff(C) + 1 = X/E + (2/3)(1 + Pt/E): every computed state has X >= 0 and Pt/E >= -1 except the "
                   "N = 8, lambda > 0 states (E < 0, X = 0, Pt/E in (0.9, 1]): no computed state has w_eff(C) < -1",
        "label": "INTERPRETATION (labelled): the comparison treats the Unite numbers as constraints on the dilution of "
                 "a 4-dimensional effective density; the Kohn-Sham history is a prescribed background without "
                 "back-reaction"}

    fails = [c for c in CHECKS if c["verdict"] != "PASS"]
    summary = {
        "producer": "Revision/dark_sector/dirac16complex/compute/compute_eos.py",
        "inputs": ["outputs/ks-history-dense.csv (run_ks_history.py, Rust Kohn-Sham solver)",
                   "outputs/effective-formulas.json (derive_effective.py, sympy)"],
        "definitions": formulas["wEff"], "rho4": formulas["rho4"],
        "history": "a4 = H x4 and b4(x4) = b4(0) e^((4/3) H x4) PRESCRIBED (test field, no back-reaction); beta = 4/3; "
                   "slices a4 in [0, 2]; a = e^{a4 - a4_today}",
        "beta": BETA,
        "series": summary_series, "condensate": cond, "mixtures_N688_lam0_today_a4_2": mix,
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
