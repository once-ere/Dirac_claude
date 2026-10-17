"""W6 draft: dirac16complex00/python/independent_numerics.py (implementation B) for the corrected metric.
Applied to the scratch copy only."""
from pathlib import Path

p = Path(__file__).with_name("d00") / "python" / "independent_numerics.py"
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''numpy only (no sympy, no code shared with derive_eos.py).  It integrates the 16-component field
equation of the local model of the author's metric WITH b4(x4) (Dirac_Einstein-Lovelock_4+4_Nash.nb,
In[97]-In[102]: g55 = g66 = g77 = -e^{-2 a4} b4 sin^{1/3} z; the warp frozen at a fixed hidden position),
on the history a4 = eps x4 (eps = H in units of the mass m) and b4 = e^{beta a4}, beta = 4/3 (the branch
of the author's weights for a source without T^x4_x0; b4 is a function of x4, never 1):

    gamma^(x4) d4 phi + (3/4)(b4'/b4) gamma^(x4) phi + i e^{-a4} k gamma^(x1) phi
        + i e^{a4} b4^{-1/2} q gamma^(x5) phi = m phi

(the gravity term gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4); its 3 H gamma^(x0) part is
absorbed by the frozen warp) for plane-wave modes exp(i (k x1 + q x5)) phi(x4) with the author's T16 read
from Revision/algebra/gammas.json.  The b4 term commutes with the generator and is integrated exactly.
It computes the energy-momentum bilinears along the solutions (rho = -K1 - K5 + m S, p1 = L0 - K1,
p5 = L0 - K5, L0 = K1 + K4 + K5 - m S), checks the conservation identity with the b4 term and the
conserved Krein charge per coordinate volume b4^{3/2} Q numerically, forms the models of implementation A''',
    '''numpy only (no sympy, no code shared with derive_eos.py).  It integrates the 16-component field
equation of the local model of the corrected primordial metric of 2026-10-16 (version 2; g00 = e^{-2 a4} b4 cot^2 z,
g55 = g66 = g77 = -e^{-2 a4} b4 (sin^2 z)^{1/6}; the warp frozen at a fixed hidden position), on the history
a4 = eps x4 (eps = H in units of the mass m) and b4 = e^{beta a4}, beta = 4/3 (the record's history, a PRESCRIBED
background):

    gamma^(x4) d4 phi + (b4'/b4 - a4'/2) gamma^(x4) phi + i e^{-a4} k gamma^(x1) phi
        + i e^{a4} b4^{-1/2} q gamma^(x5) phi = m phi

(the gravity term gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4); its gamma^(x0)
part is dropped with the frozen warp, the local-model APPROXIMATION) for plane-wave modes exp(i (k x1 + q x5)) phi(x4)
with the author's T16 read from Revision/algebra/gammas.json.  The gravity term commutes with the generator and is
integrated exactly.  It computes the energy-momentum bilinears along the solutions (rho = -K1 - K5 + m S, p1 = L0 - K1,
p5 = L0 - K5, L0 = K1 + K4 + K5 - m S), checks the conservation identity with the expansion of the extra times and
the hidden direction and the conserved Krein charge per coordinate volume e^{-a4} b4^2 Q numerically, forms the models
of implementation A''')
rep('''REV = os.path.normpath(os.path.join(OWN, "..", ".."))''', '''REV = os.environ.get("REVISION_DIR") or os.path.normpath(os.path.join(OWN, "..", ".."))''')
rep('''U = BETA * EPS      # b4'/b4''', '''U = BETA * EPS      # b4'/b4
GR = (BETA - 0.5) * EPS     # the gravity term b4'/b4 - a4'/2 on the history
SHIFT_N2 = -(4.0 - 2.0 * BETA) / 3.0   # w_eff(N2) - w_eff(N1) = -4/9''')
rep('''    """omega phi = h phi for the frozen generator: d4 phi = -i h phi - (3/4)(b4'/b4) phi."""''',
    '''    """omega phi = h phi for the frozen generator: d4 phi = -i h phi - (b4'/b4 - a4'/2) phi."""''')
rep('''    it preserves the Krein form exactly) times the exact factor exp(-(3/4) u dx) of the b4 term (it commutes''',
    '''    it preserves the Krein form exactly) times the exact factor exp(-(b4'/b4 - a4'/2) dx) of the gravity term (it commutes''')
rep('''        dphi = -1j * (h @ phi) - 0.75 * u * phi''', '''        dphi = -1j * (h @ phi) - (u - 0.5 * eps) * phi''')
rep('''        phi = (c * phi - 1j * sc * (hm @ phi)) * math.exp(-0.75 * u * dx)''', '''        phi = (c * phi - 1j * sc * (hm @ phi)) * math.exp(-(u - 0.5 * eps) * dx)''')
rep('''    """w_eff from the formula (N1 = (X + (beta/2) Pt)/rho, X = (K5 - K1)/3, Pt = L0 - K5/3 isotropic;
    N2 = N1 - 1 + beta/2) and DIRECTLY from the dilution of the proper density rho (N2_dilution =
    -1 - (1/3) d ln rho/d ln a)."""''', '''    """w_eff from the formula (N1 = (p3 + (beta/2 - 1)(p0 + 3 p_t)/3)/rho, p3 = L0 - K1/3, p_t = L0 - K5/3, p0 = L0
    isotropic; N2 = N1 - (4 - 2 beta)/3) and DIRECTLY from the dilution of the proper density rho (N2_dilution =
    -1 - (1/3) d ln rho/d ln a)."""''')
rep('''        e = smooth_at(lna, (run["K5"] - run["K1"]) / 3.0 + 0.5 * BETA * pt, a) / c.r1''',
    '''        e = smooth_at(lna, p3 + (0.5 * BETA - 1.0) * (L0 + 3.0 * pt) / 3.0, a) / c.r1''')
rep('''    return {"N2": -1.0 + 0.5 * BETA + E / R, "N1": E / R, "ratio": P3 / R, "rho": R,''',
    '''    return {"N2": SHIFT_N2 + E / R, "N1": E / R, "ratio": P3 / R, "rho": R,''')
rep('''    b4f = lambda lna: np.exp(1.5 * BETA * lna)          # b4^{3/2} along the run (b4 = e^{beta a4})''',
    '''    b4f = lambda lna: np.exp((2.0 * BETA - 1.0) * lna)  # e^{-a4} b4^2 along the run (b4 = e^{beta a4})''')
rep('''        rhs = EPS * (rn["K1"] - rn["K5"]) - 0.5 * U * (3 * rho + 3 * L0 - rn["K5"])''',
    '''        rhs = -EPS * (3 * rho + 3 * L0 - rn["K1"]) - (0.5 * BETA - 1.0) * EPS * (4 * rho + 4 * L0 - rn["K5"])''')
rep('''              "Krein charge per coordinate volume b4^(3/2) Q: drift %s; max |L0| (on shell) %s; conservation with the b4 term d rho/dx4 = a4' (K1 - K5) - (b4'/(2 b4)) (3 rho + 3 L0 - K5): relative residual %s (finite differences)" % (r8(Qd), r8(np.max(np.abs(L0))), r8(cons)))''',
    '''              "Krein charge per coordinate volume e^(-a4) b4^2 Q: drift %s; max |L0| (on shell) %s; conservation d rho/dx4 = -a4' (3 rho + 3 L0 - K1) - h4 (4 rho + 4 L0 - K5), h4 = b4'/(2 b4) - a4': relative residual %s (finite differences)" % (r8(Qd), r8(np.max(np.abs(L0))), r8(cons)))''')
rep('''    check("B_condensate_dilutes_with_b4", np.ptp(rc) < 1e-9 and rr > 0.5,
          "homogeneous solution (k = q = 0): rho = m S with b4^(3/2) rho constant (range %s), while rho itself changes by a factor (relative range %s over a in [0.3, 1.06]): the condensate dilutes with b4^(3/2) ~ a^2" % (r8(np.ptp(rc)), r8(rr)))''',
    '''    check("B_condensate_dilutes", np.ptp(rc) < 1e-9 and rr > 0.5,
          "homogeneous solution (k = q = 0): rho = m S with e^(-a4) b4^2 rho constant (range %s), while rho itself changes by a factor (relative range %s over a in [0.3, 1.06]): the condensate dilutes with the proper 7-volume e^(-a4) b4^2 ~ a^(5/3)" % (r8(np.ptp(rc)), r8(rr)))''')
rep('''              "%s: w_eff(N2) = -1 - (1/3) d ln rho/d ln a measured from the dilution of the proper density of the field-equation solutions equals the formula w_eff(N1) - 1 + beta/2 at a = 1/2, 3/4, 1 to within %s" % (mname, r8(dil)))''',
    '''              "%s: w_eff(N2) = -1 - (1/3) d ln rho/d ln a measured from the dilution of the proper density of the field-equation solutions equals the formula w_eff(N1) - (4 - 2 beta)/3 at a = 1/2, 3/4, 1 to within %s" % (mname, r8(dil)))''')
rep('''                  "w_eff(N2) of M5 (withdrawn composition) from the field equation on the history b4 ~ a^(4/3): %d crossings of -1 on a grid of 67 points in [0.34, 1] (A: %d; the withdrawn b4 = 1 record had one, at a = 0.779)" % (len(cr), len(Acr)))''',
    '''                  "w_eff(N2) of M5 (the composition of the withdrawn b4 = 1 record) from the field equation on the record's history: %d crossings of -1 on a grid of 67 points in [0.34, 1] (A: %d)" % (len(cr), len(Acr)))''')
rep('''    # 4. independent solve: M3 (s from w_eff(N2)(1) = A's value -0.287 on the history b4 ~ a^(4/3))''',
    '''    # 4. independent solve: M3 (s from w_eff(N2)(1) = A's value on the record's history)''')
rep('''    # positive models from the field equation: w_eff(N2) >= -1/3 on a in [0.35, 1]''', '''    # positive models from the field equation: w_eff(N2) >= -4/9 on a in [0.35, 1]''')
rep('''    check("B_positive_models_bounded", pos_min >= -1.0 / 3.0 - TOL_W,
          "M2, M3, M4 from the field-equation solutions: min of w_eff(N2) over a in [0.35, 1] = %s >= -1/3 (within %s): no positive-energy model reaches the Unite w0 on the history b4 ~ a^(4/3)" % (r8(pos_min), TOL_W))''',
    '''    check("B_positive_models_bounded", pos_min >= SHIFT_N2 - TOL_W,
          "M2, M3, M4 from the field-equation solutions: min of w_eff(N2) over a in [0.35, 1] = %s >= -4/9 (within %s): no positive-energy model reaches the Unite w0 on the record's history" % (r8(pos_min), TOL_W))''')
rep('''    # d ln|phi|/dx4 = sqrt(q_p^2 - m^2) - (3/4) b4'/b4, q_p^2 = s a^(2 - beta)''', '''    # d ln|phi|/dx4 = sqrt(q_p^2 - m^2) - (b4'/b4 - a4'/2), q_p^2 = s a^(2 - beta)''')
rep('''    gam = math.sqrt(s3 * math.exp((2.0 - BETA) * np.mean(lna[sel])) - 1) - 0.75 * U''', '''    gam = math.sqrt(s3 * math.exp((2.0 - BETA) * np.mean(lna[sel])) - 1) - GR''')
rep('''          "q-mode of M3 past its turning point a_* = s^(-3/2) = %s: d ln|phi|/dx4 over a in [7.0, 7.4] = %s, WKB rate sqrt(s a^(2/3) - 1) - (3/4) b4'/b4 at the mean a = %s" % (r8(a_star), r8(slope), r8(gam)))''',
    '''          "q-mode of M3 past its turning point a_* = s^(-3/2) = %s: d ln|phi|/dx4 over a in [7.0, 7.4] = %s, WKB rate sqrt(s a^(2/3) - 1) - (b4'/b4 - a4'/2) at the mean a = %s" % (r8(a_star), r8(slope), r8(gam)))''')
rep('''                     "reading": "the extra-time-momentum mode becomes exponentially growing once q_p = q a^(1/3) > m (the deflation blueshifts q, more slowly than on the withdrawn b4 = 1 record); its energy and extra-time pressure then grow without bound"}''',
    '''                     "reading": "the extra-time-momentum mode becomes exponentially growing once q_p = q a^(1/3) > m (the deflation blueshifts q); its energy and extra-time pressure then grow without bound"}''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
