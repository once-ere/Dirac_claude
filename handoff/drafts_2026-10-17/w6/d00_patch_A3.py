"""W6 draft: dirac16complex00/python/derive_eos.py, section A3 (the homogeneous condensate) for the corrected metric.
Applied to the scratch copy only."""
from pathlib import Path

p = Path(__file__).with_name("d00") / "python" / "derive_eos.py"
t = p.read_text(encoding="utf-8")
start = t.index("def section_condensate(g):")
end = t.index("# ----------------------------------------------------------------------------------------------\n# A4. Plane waves")
new = '''def section_condensate(g):
    M, H, m, lam, S = sp.symbols("M H m lambda S", real=True)
    g4, g0 = g[4], g[0]
    C = g[0] * g[1] * g[2] * g[3]
    I16 = sp.eye(16)
    ub, ad = sp.symbols("u a4p", real=True)       # u = b4'/b4, a4p = a4'
    cg = sp.Symbol("c_g", positive=True)            # (3/2) H e^{a4} b4^{-1/2}, a positive scalar on a slice
    B = -M * g4 + cg * g4 * g0
    A = B - (ub - ad / 2) * I16
    ok_S = (C * A + A.T * C + 2 * (ub - ad / 2) * C).expand() == sp.zeros(16)
    K4mat = ((C * g4 * A - A.T * C * g4) / 2).expand()
    ok_K4 = (K4mat - M * C).expand() == sp.zeros(16)
    rec = json.load(open(A4EQ, encoding="utf-8"))
    hc = rec["fields"]["dirac16complex00"]["homogeneousCondensate"]
    stated = ("A = B - (b4'/b4 - a4'/2) I16" in hc and "(3/2) H e^{a4} b4^{-1/2} gamma^x4 gamma^x0" in hc
              and "S = e^{a4} b4^{-2} S0 (exact)" in hc)
    check("condensate_S_T16", ok_S and stated,
          "Phi(x4) on shell in the corrected metric (a4-equations.json fields.dirac16complex00.homogeneousCondensate): d4 Phi = A "
          "Phi, A = B - (b4'/b4 - a4'/2) I16, B = -M gamma^(x4) + (3/2) H e^(a4) b4^(-1/2) gamma^(x4) gamma^(x0), M = m + U'(S); "
          "C A + A^T C = -2 (b4'/b4 - a4'/2) C (author's T16, for every value of the coefficient of gamma^(x4) gamma^(x0)), so "
          "d S/dx4 = -2 (b4'/b4 - a4'/2) S: S = S0 e^(a4) b4^(-2) (S Vol_7 constant); the record states the same: %s" % stated)
    check("condensate_negative_control", (K4mat + M * C).expand() != sp.zeros(16) and (C * A + A.T * C).expand() != sp.zeros(16),
          "controls: K_x4 is not -M S, and C A + A^T C is not zero for b4'/b4 != a4'/2 (S is not constant)")
    check("condensate_K4_equals_MS_T16", ok_K4,
          "K_x4 = (1/2)(Phibar gamma^(x4) d4 Phi - d4 Phibar gamma^(x4) Phi) = M S exactly (matrix identity (C g4 A - A^T C g4)/2 = "
          "M C, for every coefficient of the gravity term); all other K_mu = 0")
    U = lam * S ** 2 / 2
    rho = m * S + U
    p = (m + lam * S) * S - m * S - U
    ok_p = sp.simplify(p - lam * S ** 2 / 2) == 0
    w = sp.simplify(p / rho)
    check("condensate_rho_p_w", ok_p and sp.simplify(w - lam * S / (2 * m + lam * S)) == 0,
          "rho = m S + lambda S^2/2, p3 = p_t = p0 = lambda S^2/2 with S = S0 e^(a4) b4^(-2), w = p/rho = lambda S/(2 m + lambda S) "
          "at each instant")
    # observer: N1 rho_4 = e^{-4 a4} b4^2 rho, N2 rho_4 = rho; on b4 ~ e^{beta a4}: S = S0 e^{(1 - 2 beta) a4}
    bt = sp.Symbol("beta", real=True)
    S0, A4v = sp.symbols("S0 a4", real=True)
    Sa = S0 * sp.exp((1 - 2 * bt) * A4v)
    rho_a = (m * S + U).subs(S, Sa)
    p_a = (lam * S ** 2 / 2).subs(S, Sa)
    rho4_N1 = sp.exp((2 * bt - 4) * A4v) * rho_a
    wN1 = sp.simplify(-1 - sp.diff(sp.log(rho4_N1), A4v) / 3)
    wN2 = sp.simplify(-1 - sp.diff(sp.log(rho_a), A4v) / 3)
    w_a = sp.simplify(p_a / rho_a)
    ok_obs = sp.simplify(wN1 - (2 * bt - 1) / 3 * w_a) == 0 and sp.simplify(wN2 - ((2 * bt - 1) / 3 * w_a - (4 - 2 * bt) / 3)) == 0
    dw = sp.simplify(sp.diff(w_a, A4v))
    ok_dw = sp.simplify(dw - ((1 - 2 * bt) * 2 * m * lam * Sa / (2 * m + lam * Sa) ** 2)) == 0
    check("condensate_observer", ok_obs and ok_dw,
          "with S = S0 e^(a4) b4^(-2) and b4 ~ e^(beta a4): w_eff(N1) = ((2 beta - 1)/3) w, w_eff(N2) = ((2 beta - 1)/3) w - "
          "(4 - 2 beta)/3, and the ratio drifts, d w/d a4 = (1 - 2 beta) 2 m lambda S/(2 m + lambda S)^2 (beta = 4/3: "
          "lambda S/m ~ e^(-(5/3) a4); w_eff(N1) = (5/9) w, w_eff(N2) = (5/9) w - 4/9)")
    x = sp.Symbol("x", real=True)  # x = lambda S/(2 m)
    wx = x / (1 + x)
    phantom_set = sp.solve_univariate_inequality(wx < -1, x, relational=False)
    ok_ph = phantom_set == sp.Interval.open(-1, sp.Rational(-1, 2))
    check("condensate_phantom_interval", ok_ph,
          "w = x/(1+x) with x = lambda S/(2 m): w < -1 exactly for x in (-1, -1/2), i.e. lambda S/m in (-2, -1); there rho = m S "
          "(1 + x) has the sign of m S and p = m S x the opposite sign; since w_eff(N2) = (5/9)(w + 1) - 1 at beta = 4/3, the "
          "observer reads w_eff(N2) < -1 exactly in the same window")
    xU = sp.solve(sp.Eq(wx, W_CONST), x)[0]
    check("condensate_ratio_equals_unite_constant_w", xU == sp.Rational(-191, 441),
          "w = -0.764 at x = -191/441, i.e. lambda S/m = -382/441 = -0.866213... at that instant; rho > 0 then needs m S > 0 and "
          "lambda < 0 (U = lambda S^2/2 < 0); the ratio then drifts (condensate_observer)")
    xs_ = -sp.Rational(382, 441)
    wa_ratio = sp.nsimplify(-(1 - 2 * BETA) * 2 * xs_ / (2 + xs_) ** 2)
    wa_general = sp.simplify(-((1 - 2 * BETA) * 2 * m * lam * S / (2 * m + lam * S) ** 2).subs(lam, xs_ * m / S))
    check("condensate_ratio_drift_at_unite_value", sp.simplify(wa_ratio - wa_general) == 0 and wa_ratio < 0,
          "beta = 4/3: lambda S/m = u ~ e^(-(5/3) a4), so the ratio u/(2 + u) has wa = -dw/da4 = (10/3) u/(2 + u)^2 = %s = %s at "
          "u = -382/441 (thawing sign); w_eff(N1) = (5/9) w and w_eff(N2) = (5/9) w - 4/9 then have wa = %s"
          % (sstr(wa_ratio), num(q2mp(wa_ratio)), num(q2mp(sp.Rational(5, 9) * wa_ratio))))
    # the source the record's history needs with the author's weights (a4-equations.json exponentialHistory.authorWeights,
    # historySource_kappaT_minus_Lam: the left-hand sides with Lambda removed, functions of kk = e^{(2/3) H x4})
    aw = rec["exponentialHistory"]["authorWeights"]
    kk = sp.Symbol("kk", positive=True)
    src = {k: sp.sympify(aw["historySource_kappaT_minus_Lam"][k]["input"].replace("^", "**"), locals={"kk": kk})
           for k in ("minus_rho", "p3", "p0", "pt")}
    aniso = sp.expand(src["p3"] - src["p0"])
    poly_nonzero = sp.Poly(aniso, kk).is_zero is False
    hist_ok = "be = 4/3" in aw["recordHistory"] and src["p0"] == src["pt"]
    check("history_required_source", hist_ok and poly_nonzero,
          "the record's history a4 = H x4, b4 = e^((4/3) H x4) with the author's weights needs the diagonal, x0-independent source of "
          "a4-equations.json exponentialHistory.authorWeights.historySource_kappaT_minus_Lam (kappa T - Lambda delta, kk = "
          "e^((2/3) H x4)): -kappa rho - Lambda = %s, kappa p3 - Lambda = %s, kappa p0 - Lambda = kappa p_t - Lambda = %s; it is "
          "anisotropic: kappa (p3 - p0) = %s" % (sstr(src["minus_rho"]), sstr(src["p3"]), sstr(src["p0"]), sstr(aniso)))
    check("condensate_cannot_source_history", poly_nonzero,
          "every homogeneous condensate (any m, lambda, S0) has p3 = p_t = p0 = lambda S^2/2, while the history needs kappa (p3 - p0) "
          "= %s, a nonzero polynomial in kk: no condensate is the source of the record's history (exact); in addition its S ~ "
          "e^(-(5/3) a4) = kk^(-5/2) decays while the required source grows with kk" % sstr(aniso))
    return {
        "solution": "Phi = e^{a4/2} b4^{-1} chi, chi' = B chi, B = -M gamma^(x4) + (3/2) H e^{a4} b4^{-1/2} gamma^(x4) gamma^(x0), M = m + lambda S, S = S0 e^{a4} b4^{-2} (S Vol_7 constant; re-verified here: C A + A^T C = -2 (b4'/b4 - a4'/2) C, K_x4 = M S)",
        "rho": "m S + lambda S^2/2, S = S0 e^{a4} b4^{-2}", "p": "p3 = p_t = p0 = lambda S^2/2",
        "w_ratio": "lambda S/(2 m + lambda S) at each instant; w < -1 iff lambda S/m in (-2, -1); lambda S/m ~ e^(-(5/3) a4) on the history",
        "w_eff_N1": "((2 beta - 1)/3) w = (5/9) w", "w_eff_N2": "((2 beta - 1)/3) w - (4 - 2 beta)/3 = (5/9) w - 4/9",
        "CPL": "the ratio has wa = (10/3) u/(2 + u)^2, u = lambda S/m (beta = 4/3); w_eff(N1), w_eff(N2): (5/9) of it",
        "unite_constant_w_by_ratio": "lambda S/m = -382/441 at one instant (rho > 0: m S > 0, lambda < 0); then wa = %s" % num(q2mp(wa_ratio)),
        "historyRequiredSource": {k: sstr(v) for k, v in src.items()} | {
            "meaning": "kappa T - Lambda delta (Lambda = -10), the author's weights w1 = 1, w2 = 1/32, w3 = 1/1152, history a4 = H x4, b4 = e^((4/3) H x4), kk = e^((2/3) H x4)"},
        "selfConsistency": "no condensate is the source of the record's history: it is isotropic (p3 = p0) and decays, the required source is anisotropic and grows",
        "expansion_inferred_w": "the observer reads a = e^{a4}: w_exp = -1 - (2/3) a4''/a4'^2 = -1 exactly on a4 = H x4, for every b4(x4)",
    }


'''
t = t[:start] + new + t[end:]
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
