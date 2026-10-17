"""W6 draft: dirac16complex00/python/derive_eos.py, sections A5 (WKB gases) and A6 (models) for the corrected metric.
Applied to the scratch copy only.  The claims about the model numbers are checked against the computed values; where a
former claim no longer holds the check states what the numbers give."""
from pathlib import Path

p = Path(__file__).with_name("d00") / "python" / "derive_eos.py"
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


# ---- A5
rep('''    om = sp.sqrt(m ** 2 + k ** 2 / a ** 2 - q ** 2 * a ** 2 / b4)
    nb = b4 ** sp.Rational(-3, 2)        # per proper volume: the proper 6-volume of a comoving cell grows like b4^(3/2)
    rho = om * Q * nb
    p3 = k ** 2 / (3 * a ** 2 * om) * Q * nb
    pt = -q ** 2 * a ** 2 / (3 * b4 * om) * Q * nb
    ok = sp.simplify(sp.diff(rho, x4) + 3 * sp.diff(a4, x4) * (p3 - pt) + sp.Rational(3, 2) * sp.diff(b4, x4) / b4 * (rho + pt)) == 0
    check("wkb_mode_gas_conservation_b4", ok,
          "rho = omega Q b4^(-3/2), p3 = k^2 Q b4^(-3/2)/(3 a^2 omega), p_t = -q^2 a^2 Q b4^(-3/2)/(3 b4 omega), omega^2 = m^2 + k^2/a^2 - q^2 a^2/b4 (comoving k, q; Q the Krein charge per comoving coordinate volume, constant as an adiabatic invariant) satisfy d rho/dx4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t) exactly")''',
    '''    om = sp.sqrt(m ** 2 + k ** 2 / a ** 2 - q ** 2 * a ** 2 / b4)
    nb = sp.exp(a4) * b4 ** -2           # per proper volume: the proper 7-volume of a comoving cell grows like e^{-a4} b4^2
    rho = om * Q * nb
    p3 = k ** 2 / (3 * a ** 2 * om) * Q * nb
    pt = -q ** 2 * a ** 2 / (3 * b4 * om) * Q * nb
    h4 = sp.diff(b4, x4) / (2 * b4) - sp.diff(a4, x4)
    ok = sp.simplify(sp.diff(rho, x4) + 3 * sp.diff(a4, x4) * (rho + p3) + h4 * rho + 3 * h4 * (rho + pt)) == 0
    check("wkb_mode_gas_conservation", ok,
          "rho = omega Q n, p3 = k^2 Q n/(3 a^2 omega), p_t = -q^2 a^2 Q n/(3 b4 omega), p0 = 0, n = e^(a4) b4^(-2), omega^2 = m^2 + "
          "k^2/a^2 - q^2 a^2/b4 (comoving k, q, no hidden momentum; Q the Krein charge per comoving coordinate volume, constant as "
          "an adiabatic invariant) satisfy d rho/dx4 = -3 a4' (rho + p3) - h4 (rho + p0) - 3 h4 (rho + p_t) exactly")''')
rep('''    eps = sp.simplify(((p3 - pt) + bt / 2 * pt) / rho)
    ok2 = sp.simplify(eps - (k ** 2 / a ** 2 + (1 - bt / 2) * q ** 2 * a ** 2 / b4) / (3 * om ** 2)) == 0
    check("wkb_epsilon_sign_free_b4", ok2,''', '''    eps = sp.simplify((3 * p3 + (bt / 2 - 1) * (0 + 3 * pt)) / (3 * rho))
    ok2 = sp.simplify(eps - (k ** 2 / a ** 2 + (1 - bt / 2) * q ** 2 * a ** 2 / b4) / (3 * om ** 2)) == 0
    check("wkb_epsilon_sign_free", ok2,''')
rep('''    # from rho_4(N1) of each component: d ln(a^-3 b4^(3/2) rho_i)/d ln a = -3 (1 + eps_i), so
    # d rho_i/d ln a = -(3 eps_i + (3/2) beta) rho_i
    wN2 = -1 - sp.Rational(1, 3) * sum((-3 * e - sp.Rational(3, 2) * bt) * r for e, r in zip(es, rs)) / sum(rs)
    ok3 = sp.simplify(wN2 - (-1 + bt / 2 + sum(e * r for e, r in zip(es, rs)) / sum(rs))) == 0
    check("mixture_weighted_average_b4", ok3,
          "mixture: w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = -1 + beta/2 + sum eps_i rho_i / sum rho_i (condensates with lambda = 0 have eps = 0)")''',
    '''    # from rho_4(N1) of each component: d ln(e^{-4 a4} b4^2 rho_i)/d a4 = -3 (1 + eps_i), so
    # d ln rho_i/d a4 = 1 - 2 beta - 3 eps_i
    wN2 = -1 - sp.Rational(1, 3) * sum((1 - 2 * bt - 3 * e) * r for e, r in zip(es, rs)) / sum(rs)
    ok3 = sp.simplify(wN2 - (-(4 - 2 * bt) / 3 + sum(e * r for e, r in zip(es, rs)) / sum(rs))) == 0
    check("mixture_weighted_average", ok3,
          "mixture: w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = -(4 - 2 beta)/3 + sum eps_i rho_i / sum rho_i (condensates "
          "with lambda = 0 have eps = 0)")''')
rep('''        "approximation": "ADIABATIC (WKB) local plane-wave modes at a fixed hidden position: the warp sin^{1/6} z and tan z frozen (wavelengths short compared with the warp scale 1/H; in the variables chi = sin^{1/2} z b4^{3/4} Phi the terms 3 H gamma^(x0) and (3/4)(b4'/b4) gamma^(x4) are absent exactly), the Krein charge of each mode an adiabatic invariant (|d omega/dx4| << omega^2); incoherent superposition (cross terms between different momenta average to zero over 3-space and the extra times; cross terms between frequencies average to zero in time)",
        "component": "rho = omega Q b4^(-3/2), p3 = k^2 Q b4^(-3/2)/(3 a^2 omega), p_t = -q^2 a^2 Q b4^(-3/2)/(3 b4 omega), p0 = 0, omega^2 = m^2 + k^2/a^2 - q^2 a^2/b4 (isotropic averages)",
        "eps": "eps = w_eff(N1) = (k_p^2 + (1 - beta/2) q_p^2)/(3 omega^2) >= 0 for real omega and beta < 2",
        "mixture": "w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = w_eff(N1) - 1 + beta/2, w = p3/rho = sum p3_i / sum rho_i",
        "theorem": "if every component has rho_i >= 0 (Krein charge of the sign of omega), real frequencies, and total rho > 0, then w_eff(N1) >= 0 and w_eff(N2) >= -1 + beta/2 (= -1/3 on the history b4 ~ a^(4/3)) at every a at which these conditions hold (weighted averages of eps_i >= 0 with weights rho_i >= 0): no phantom, no crossing of -1, and no w_eff(N2) below -1/3 there. A mode with extra-time momentum q != 0 loses its real frequency past its turning point a_* (q_phys = q a b4^(-1/2) grows), where the theorem does not apply. Going below -1 + beta/2 needs a component with rho_i < 0 (negative classical energy: a ghost-like sector)",''',
    '''        "approximation": "ADIABATIC (WKB) local plane-wave modes at a fixed hidden position, with no hidden momentum: the warp (sin^2 z)^{1/12} and cot z frozen (wavelengths short compared with the warp scale 1/H; the gravity terms are absent in the half-density variables), the Krein charge of each mode an adiabatic invariant (|d omega/dx4| << omega^2); incoherent superposition (cross terms between different momenta average to zero over 3-space and the extra times; cross terms between frequencies average to zero in time)",
        "component": "rho = omega Q n, p3 = k^2 Q n/(3 a^2 omega), p_t = -q^2 a^2 Q n/(3 b4 omega), p0 = 0, n = e^{a4} b4^{-2}, omega^2 = m^2 + k^2/a^2 - q^2 a^2/b4 (isotropic averages)",
        "eps": "eps = w_eff(N1) = (k_p^2 + (1 - beta/2) q_p^2)/(3 omega^2) >= 0 for real omega and beta < 2",
        "mixture": "w_eff(N1) = sum eps_i rho_i / sum rho_i, w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3, w = p3/rho = sum p3_i / sum rho_i",
        "theorem": "if every component has rho_i >= 0 (Krein charge of the sign of omega), real frequencies, and total rho > 0, then w_eff(N1) >= 0 and w_eff(N2) >= -(4 - 2 beta)/3 (= -4/9 on the history b4 ~ a^(4/3)) at every a at which these conditions hold (weighted averages of eps_i >= 0 with weights rho_i >= 0): no phantom, no crossing of -1, and no w_eff(N2) below -4/9 there. A mode with extra-time momentum q != 0 loses its real frequency past its turning point a_* (q_phys = q a b4^(-1/2) grows), where the theorem does not apply. Going below -(4 - 2 beta)/3 needs a component with rho_i < 0 (negative classical energy: a ghost-like sector)",''')
# ---- A6
rep('''    """components: list of (kind, weight, params); rho per comoving coordinate cell, normalised so that the total is 1
    at a = 1.  On the history b4 ~ a^beta (beta = 4/3) every component's proper density carries the common factor
    b4^(-3/2), which cancels in w_eff(N1) and in the ratio; w_eff(N2) = w_eff(N1) - 1 + beta/2 (mixture_weighted_average_b4).''',
    '''    """components: list of (kind, weight, params); rho per comoving coordinate cell, normalised so that the total is 1
    at a = 1.  On the history b4 ~ a^beta (beta = 4/3) every component's proper density carries the common factor
    e^{a4} b4^(-2), which cancels in w_eff(N1) and in the ratio; w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3
    (mixture_weighted_average).''')
rep('''            if kind == "condensate":  # lambda = 0: rho b4^(3/2) constant, X = Pt = 0, p3 = 0''',
    '''            if kind == "condensate":  # lambda = 0: E = m S0 per coordinate cell constant, P3 = Pt = P0 = 0''')
rep('''    def wN2(self, a):
        R, E, _ = self.parts(a)
        return -1 + BETA_MP / 2 + E / R''', '''    def wN2(self, a):
        R, E, _ = self.parts(a)
        return SHIFT_N2_MP + E / R''')
rep('''    out["M1_condensate"] = {
        "content": "homogeneous condensate (exact solution for every a4, b4): S = S0 b4^(-3/2), u = lambda S/m ~ e^(-2 a4) on the history",
        "N2": {"w": "-1/3 + (2/3) u/(2 + u)", "lambda_0": {"w0": "-1/3", "wa": "0"}},
        "N1": {"w": "(2/3) u/(2 + u)", "lambda_0": {"w0": "0", "wa": "0"}},
        "ratio": {"w": "u/(2 + u)", "CPL": {"w0": "u/(2 + u)", "wa": "4 u/(2 + u)^2"}, "unite_constant_w": "u = -382/441 at one instant"},
    }''', '''    out["M1_condensate"] = {
        "content": "homogeneous condensate (exact solution for every a4, b4): S = S0 e^(a4) b4^(-2), u = lambda S/m ~ e^(-(5/3) a4) on the history",
        "N2": {"w": "-4/9 + (5/9) u/(2 + u)", "lambda_0": {"w0": "-4/9", "wa": "0"}},
        "N1": {"w": "(5/9) u/(2 + u)", "lambda_0": {"w0": "0", "wa": "0"}},
        "ratio": {"w": "u/(2 + u)", "CPL": {"w0": "u/(2 + u)", "wa": "(10/3) u/(2 + u)^2"}, "unite_constant_w": "u = -382/441 at one instant"},
    }''')
rep('''    w0_2 = -third + r / 3''', '''    w0_2 = SHIFT_N2 + r / 3''')
rep('''          "positive-energy good-sector gas (q = 0), k^2/(k^2+m^2) = 417/1000 at a = 1: N2 tangent (w0, wa) = (%s, %s) = (-1/3 + r/3, (2/3) r (1 - r)): FREEZING (wa > 0); the withdrawn b4 = 1 record had w0 = -0.861" % (sstr(w0_2), sstr(wa_exact)))''',
    '''          "positive-energy good-sector gas (q = 0), k^2/(k^2+m^2) = 417/1000 at a = 1: N2 tangent (w0, wa) = (%s, %s) = (-4/9 + r/3, (2/3) r (1 - r)): FREEZING (wa > 0)" % (sstr(w0_2), sstr(wa_exact)))''')
rep('''    wN2_3 = -1 + BETA / 2 + eps3''', '''    wN2_3 = SHIFT_N2 + eps3''')
rep('''          "positive-energy extra-time-momentum mode (k = 0), s = q_p^2/m^2 = 417/1417 at a = 1, omega^2 = m^2 (1 - s a^(2/3)): N2 tangent (w0, wa) = (%s, %s) = (%s, %s): thawing sign, w_eff(N2) = -1/3 + (1/9) s a^(2/3)/(1 - s a^(2/3)) >= -1/3; turning point a_* = s^(-3/2) = %s (the withdrawn b4 = 1 record: (-0.861, -0.393926), a_* = 1.843)" % (sstr(w0_3), sstr(wa3), num(q2mp(w0_3)), num(q2mp(wa3)), num(mp.mpf(1417 / 417) ** mp.mpf(1.5))))''',
    '''          "positive-energy extra-time-momentum mode (k = 0), s = q_p^2/m^2 = 417/1417 at a = 1, omega^2 = m^2 (1 - s a^(2/3)): N2 tangent (w0, wa) = (%s, %s) = (%s, %s): w_eff(N2) = -4/9 + (1/9) s a^(2/3)/(1 - s a^(2/3)) >= -4/9; turning point a_* = s^(-3/2) = %s" % (sstr(w0_3), sstr(wa3), num(q2mp(w0_3)), num(q2mp(wa3)), num(mp.mpf(1417 / 417) ** mp.mpf(1.5))))''')
rep('''        "N2_formula": "w_eff(N2) = -1/3 + (1/9) s a^(2/3)/(1 - s a^(2/3)) >= -1/3 for a < a_* = s^(-3/2) (real frequency); past a_* the frequency is imaginary and the formula does not apply",''',
    '''        "N2_formula": "w_eff(N2) = -4/9 + (1/9) s a^(2/3)/(1 - s a^(2/3)) >= -4/9 for a < a_* = s^(-3/2) (real frequency); past a_* the frequency is imaginary and the formula does not apply",''')
rep('''    check("M4_withdrawn_tuning_on_b4_history", minw >= -mp.mpf(1) / 3 and w0n > mp.mpf("-0.5"),
          "condensate + positive q-mode with the parameters that gave the Unite tangent on the withdrawn b4 = 1 record (s = 264037/403037, Omega_q = 57963/264037): on the history b4 ~ a^(4/3) its N2 tangent is (%s, %s), min of w_eff(N2) over a = 1/300 ... 1 is %s >= -1/3; turning point a_* = s^(-3/2) = %s" % (num(w0n), num(wan), num(minw), num(a_star4)))''',
    '''    check("M4_former_tuning_on_the_history", minw >= SHIFT_N2_MP and w0n > UNITE_W0_MP,
          "condensate + positive q-mode with the parameters that gave the Unite tangent on the withdrawn b4 = 1 record (s = 264037/403037, Omega_q = 57963/264037): on the record's history its N2 tangent is (%s, %s), min of w_eff(N2) over a = 1/300 ... 1 is %s >= -4/9 (above the Unite w0 = -0.861); turning point a_* = s^(-3/2) = %s" % (num(w0n), num(wan), num(minw), num(a_star4)))''')
rep('''    check("positive_models_bounded_by_minus_one_third", all(v >= -mp.mpf(1) / 3 for v in mins),
          "M2, M3, M4 (positive components, real frequencies on a in (0, 1]): min of w_eff(N2) over a = 1/300 ... 1 = %s, all >= -1 + beta/2 = -1/3: on the history with b4(x4) no positive-energy model reaches the Unite w0 = -0.861 or crosses -1" % ", ".join(num(v) for v in mins))''',
    '''    check("positive_models_bounded_by_minus_four_ninths", all(v >= SHIFT_N2_MP for v in mins),
          "M2, M3, M4 (positive components, real frequencies on a in (0, 1]): min of w_eff(N2) over a = 1/300 ... 1 = %s, all >= -(4 - 2 beta)/3 = -4/9: on the record's history no positive-energy model reaches the Unite w0 = -0.861 or crosses -1" % ", ".join(num(v) for v in mins))''')
rep('''    Gmin = 3 * (sp.Rational(861, 1000) - third)
    a0 = Gmin / (1 + Gmin)
    check("unite_w0_requires_dominant_ghost", Gmin == sp.Rational(1583, 1000) and sp.Rational(1, 2) < a0 < 1,
          "a ghost component (massless good-sector modes of negative energy, rho_g = -G/a at a = 1, eps = 1/3) lowers w_eff(N2)(1) by G/3 at most and positive components raise it, so w_eff(N2)(1) = -0.861 needs G >= %s (the ghost energy exceeds the total by more than half); for condensate + ghost (Omega_c = 1 + G) the total energy (1 + G) - G/a vanishes at a = G/(1 + G) = %s inside [1/2, 1], where w_eff diverges: the Unite fit over [1/2, 1] is not reachable by such a model (the withdrawn b4 = 1 record reached it with G = 3/10)" % (sstr(Gmin), sstr(a0)))''',
    '''    Gmin = 3 * (sp.Rational(861, 1000) + SHIFT_N2)
    a0 = Gmin / (1 + Gmin)
    check("unite_w0_requires_dominant_ghost", Gmin == sp.Rational(3749, 3000) and sp.Rational(1, 2) < a0 < 1,
          "a ghost component (massless good-sector modes of negative energy, rho_g = -G/a at a = 1, eps = 1/3) lowers w_eff(N2)(1) by G/3 at most and positive components raise it, so w_eff(N2)(1) = -0.861 needs G >= %s (the ghost energy exceeds the total); for condensate + ghost (Omega_c = 1 + G) the total energy (1 + G) - G/a vanishes at a = G/(1 + G) = %s inside [1/2, 1], where w_eff diverges: the Unite fit over [1/2, 1] is not reachable by such a model" % (sstr(Gmin), sstr(a0)))''')
rep('''    check("M5_withdrawn_composition_on_b4_history", len(cr) == 0 and fw0 > mp.mpf("-0.6"),
          "condensate + positive q-mode + ghost radiation with the parameters of the withdrawn record (G = 3/10, s = 0.567762680825, Omega_q = 0.594675195377): on the history b4 ~ a^(4/3) its N2 least-squares CPL fit over a in [1/2, 1] is (%s, %s) and w_eff(N2) does not cross -1 in [1/3, 1] (the withdrawn record: fit (-0.861, -0.60), crossing at a = 0.779)" % (num(fw0), num(fwa)))''',
    '''    check("M5_former_composition_on_the_history", fw0 > UNITE_W0_MP,
          "condensate + positive q-mode + ghost radiation with the parameters of the withdrawn record (G = 3/10, s = 0.567762680825, Omega_q = 0.594675195377): on the record's history its N2 least-squares CPL fit over a in [1/2, 1] is (%s, %s) (w0 above the Unite -0.861); crossings of -1 in [1/3, 1]: %s" % (num(fw0), num(fwa), ", ".join(num(c) for c in cr) if cr else "none"))''')
rep('''        "unite": "on the history b4 ~ a^(4/3) the Unite w0 under N2 needs a ghost fraction G >= 1583/1000 (unite_w0_requires_dominant_ghost)",''',
    '''        "unite": "on the record's history the Unite w0 under N2 needs a ghost fraction G >= 3749/3000 (unite_w0_requires_dominant_ghost)",''')
rep('''    # the models keep the physical parameters of the withdrawn b4 = 1 record (so that the effect of b4(x4) is seen
    # directly); on the history b4 ~ a^(4/3) they give the numbers below''', '''    # the models keep the physical parameters of the withdrawn b4 = 1 record (so that the effect of the metric is seen
    # directly); on the record's history of the corrected metric they give the numbers below''')
rep('''W_CONST = sp.Rational(-764, 1000)''', '''W_CONST = sp.Rational(-764, 1000)
UNITE_W0_MP = mp.mpf("-0.861")''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
