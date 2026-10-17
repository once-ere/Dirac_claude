#!/usr/bin/env python3
"""Revision/universe_model/analysis/x0_mass_analysis.py - the analysis of the x0 mass mechanism of UM-1 (ANALYSIS.md
part A): is the four-dimensional mass of a field the x0 momentum of its wave function, as the author's Heisenberg
argument says (Delta x0 * Delta p_x0 >= hbar/2, momentum ~ mass), and where does that argument hold or fail?

Part A1 (sympy, exact): the x0 operator of a scalar (and of every 4D-vector and TT component, whose 4D indices do not
see x0) for the corrected metric (version 2), in the hidden chart y = ln|sin z|/(6H); the fold conditions from flux
continuity (even <-> Neumann, odd <-> Dirichlet); the flat-measure form v = e^{3Hy/2} u with the warp potential
9H^2/4; the factorisation Lambda = ||(d_s + phi') v||^2 + tip term (a supersymmetric-quantum-mechanics structure: the
zero mode is the ground state of A^dagger A); the exact spectrum without cutoff (one zero mode, a continuum from
3H/(2f), nothing in between); the same boundary identity for the spin-1/2 block of the Kohn-Sham record; the tip
boundary condition of the sigma field from the actions of MODEL.md (beta proportional to f).

Part A2 (numerics, numpy): the x0 spectra of the bosonic operator in four boundary classes by two independent
discretisations (weighted u-form and flat v-form finite elements) against the exact formulas; the gap theorem (no level
of an odd mode and no excited level below 9 eta^2/4); the limit L -> infinity; for every particle of UM-1 the split of
m^2 into hidden kinetic energy <p^2>, warp, fold and tip terms; the author's Heisenberg estimate hbar/(2 Delta s) against
the actual mass; the coordinate x0 picture; the sensitivity d ln m/d ln f of every mass to the block size f and the
bound on the deflation rate today.

Units: H = 1 for the cell, eta = H L = 3, f = 8^{-1/2} (the vacuum of SOLUTION.md section 3), t = y/L in [-1, 0];
eigenvalues Lambda = (m f L)^2.  Physical scales from solution/outputs/masses.json.  Outputs: outputs/x0_mass.json,
reports/x0-mass-checks.json, figures/figA*.png.  Run time about 20 s."""
import json
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = Path(__file__).resolve().parent
UM = HERE.parent
sys.path.insert(0, str(UM / "solution"))
import masses as MS  # noqa: E402

OUT = HERE / "outputs"
REP = HERE / "reports"
FIG = HERE / "figures"
ETA = 3.0
F_VAC = 8.0 ** -0.5
CHECKS = []


def check(name, ok, detail):
    CHECKS.append({"name": name, "verdict": "PASS" if ok else "FAIL", "detail": detail})
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


# ---------------------------------------------------------------------------------------------------------------- A1
def part_a1():
    """exact statements (sympy)"""
    res = {}
    H, f, a4, x0, y, m, kap = sp.symbols("H f a4 x0 y m kappa", positive=True)
    z = 6 * H * x0
    # the corrected metric, version 2, on the half 0 < z < pi/2, where sin z, cos z, cot z > 0 and (sin^2 z)^{1/6} = sin^{1/3} z
    # (the positive branch of SOLUTION.md); b4 = f^2 e^{2 a4}
    b4 = f ** 2 * sp.exp(2 * a4)
    g = [sp.exp(-2 * a4) * b4 * sp.cot(z) ** 2] + [sp.exp(2 * a4)] * 3 + [-1] + [-sp.exp(-2 * a4) * b4 * sp.sin(z) ** sp.Rational(1, 3)] * 3
    sqrtg_claim = f ** 4 * sp.exp(3 * a4) * sp.cot(z) * sp.sin(z) ** sp.Rational(1, 2)
    ok_sqrtg = sp.simplify(sp.prod(g) - sqrtg_claim ** 2) == 0
    # scalar operator (1/sqrt g) d_0 (sqrt g g^00 d_0 U) for U = T(y(x0)), y = ln sin z/(6H), with the generic test
    # profile T(y) = e^{p y}(1 + q y + r y^2); the claim is (1/f^2) e^{-3Hy} d_y (e^{3Hy} T'(y)) = (T'' + 3H T')/f^2
    p_, q_, r_ = sp.symbols("p q r", real=True)
    yx = sp.log(sp.sin(z)) / (6 * H)
    T = sp.exp(p_ * y) * (1 + q_ * y + r_ * y ** 2)
    op_t = sp.diff(sqrtg_claim / g[0] * sp.diff(T.subs(y, yx), x0), x0) / sqrtg_claim
    cl_t = ((sp.diff(T, y, 2) + 3 * H * sp.diff(T, y)) / f ** 2).subs(y, yx)
    ok_op = sp.simplify(op_t - cl_t) == 0
    vals = {H: 1.3, f: 0.7, a4: 0.4, p_: 0.9, q_: -0.6, r_: 0.25}
    num = [float((op_t - cl_t).subs(vals).subs(x0, xv)) for xv in (0.05, 0.11, 0.17)]
    ok_spot = max(abs(v) for v in num) < 1e-10
    check("A1_scalar_x0_operator", bool(ok_sqrtg and (ok_op or ok_spot) and ok_spot),
          "sqrt|g| = f^4 e^{3 a4} |cot z| |sin z|^{1/2} and (1/sqrt g) d_0(sqrt g g^00 d_0 u) = (1/f^2) e^{-3Hy}(e^{3Hy} u_y)_y "
          "for a generic profile (sympy simplify: %s; numeric spot check %.1e)" % ("zero" if ok_op else "not reduced", max(abs(v) for v in num)))
    res["x0_operator"] = "-(1/f^2) e^{-3Hy} d_y(e^{3Hy} d_y u) = m^2 u, measure sqrt|g| dx0 = e^{3 a4} f^4 e^{3Hy} dy"
    # flux: sqrt g g^00 d_0 U = e^{3a4} f^2 sign(cot z) e^{3Hy} u_y (on this half cot z > 0 and e^{3Hy} = sin^{1/2} z)
    flux = sqrtg_claim / g[0] * sp.diff(T.subs(y, yx), x0)
    flux_claim = sp.exp(3 * a4) * f ** 2 * sp.sin(z) ** sp.Rational(1, 2) * sp.diff(T, y).subs(y, yx)
    ok_flux = sp.simplify(flux - flux_claim) == 0 or max(abs(float((flux - flux_claim).subs(vals).subs(x0, xv))) for xv in (0.05, 0.11)) < 1e-12
    check("A1_fold_conditions_from_flux", bool(ok_flux),
          "the x0 flux is e^{3a4} f^2 sign(cot z) e^{3Hy} u_y: continuity at the fold z = pi/2 gives u_y(0) = 0 for a mode "
          "even under z -> pi - z (Neumann) and u(0) = 0 for an odd one (Dirichlet)")
    # v = e^{3Hy/2} u: flat measure, warp potential 9H^2/4 (a generic v)
    v = sp.Function("v")
    uu = sp.exp(-3 * H * y / 2) * v(y)
    lhs = sp.simplify(sp.exp(3 * H * y / 2) * (-(sp.diff(uu, y, 2) + 3 * H * sp.diff(uu, y)) / f ** 2))
    rhs = (-sp.diff(v(y), y, 2) + sp.Rational(9, 4) * H ** 2 * v(y)) / f ** 2
    ok_v = sp.simplify(lhs - rhs) == 0
    check("A1_flat_form_warp_potential", bool(ok_v),
          "u = e^{-3Hy/2} v turns the operator into (1/f^2)(-v'' + (9H^2/4) v): the warp of the three extra times is a "
          "constant potential 9H^2/(4 f^2) in the flat measure; Neumann u'(0) = 0 becomes the Robin condition v'(0) = (3H/2) v(0)")
    # factorisation: A = d_t + phi', phi' = -3 eta/2 on the half (zero mode v0 = e^{3 eta t/2}); ||A v||^2 = int e^{3 eta t} u'^2
    t, e, c1, c2, c3 = sp.symbols("t eta c1 c2 c3", real=True)
    vt = sp.exp(c1 * t) * (1 + c2 * t + c3 * t ** 2)           # a generic test profile
    ut = sp.exp(-3 * e * t / 2) * vt
    lhs_f = sp.integrate(sp.expand((sp.diff(vt, t) - 3 * e / 2 * vt) ** 2), (t, -1, 0))
    rhs_f = sp.integrate(sp.expand(sp.exp(3 * e * t) * sp.diff(ut, t) ** 2), (t, -1, 0))
    quad = sp.integrate(sp.expand(sp.diff(vt, t) ** 2 + sp.Rational(9, 4) * e ** 2 * vt ** 2), (t, -1, 0)) \
        - sp.Rational(3, 2) * e * vt.subs(t, 0) ** 2 + sp.Rational(3, 2) * e * vt.subs(t, -1) ** 2
    vals = {e: sp.Rational(3), c1: sp.Rational(2, 3), c2: sp.Rational(-1, 2), c3: sp.Rational(1, 7)}
    d1 = abs(float((lhs_f - rhs_f).subs(vals)))
    d2 = abs(float((lhs_f - quad).subs(vals)))
    check("A1_factorisation", d1 < 1e-10 and d2 < 1e-10,
          "||(d_t - 3 eta/2) v||^2 = int e^{3 eta t} u'^2 = int v'^2 + (9 eta^2/4) int v^2 - (3 eta/2) v(0)^2 + (3 eta/2) v(-1)^2 "
          "for a generic profile (deviations %.1e, %.1e): m^2 = <p^2> + warp + fold (negative) + tip (positive) terms, and "
          "m^2 >= 0 with equality only for the geometric zero mode v0 = e^{3 eta t/2} (u = const)" % (d1, d2))
    # exact spectrum without cutoff
    kp = sp.Symbol("kappa_p", positive=True)
    u_norm = sp.exp((kp - sp.Rational(3, 2) * H) * y)       # the normalisable solution for f^2 m^2 = 9H^2/4 - kappa^2
    neum = sp.solve(sp.Eq(sp.diff(u_norm, y).subs(y, 0), 0), kp)
    m2_zero = sp.simplify((sp.Rational(9, 4) * H ** 2 - neum[0] ** 2) / f ** 2)
    ok_ex = neum == [sp.Rational(3, 2) * H] and m2_zero == 0
    vol = sp.integrate(sp.exp(3 * H * y), (y, -sp.oo, 0))
    check("A1_exact_spectrum_without_cutoff", bool(ok_ex and sp.simplify(vol - 1 / (3 * H)) == 0),
          "L -> infinity: below 3H/(2f) the only normalisable mode is u = e^{(kappa - 3H/2) y}; Neumann at the fold forces "
          "kappa = 3H/2, i.e. m = 0 (the flat zero mode, norm int e^{3Hy} dy = 1/(3H) finite), and Dirichlet forbids it; above "
          "3H/(2f) the spectrum is continuous. The proper length of a half cell is infinite, its weighted volume finite")
    # spin 1/2: the block of the Kohn-Sham record, h = -i sigma1 d_t + c sigma2 (units 1/(fL)); ||h chi||^2 identity
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    cc = sp.Symbol("c", real=True)
    pa = sp.exp(c1 * t) * (1 + c2 * t)
    pb = sp.exp(c3 * t) * (2 - t)
    chi = sp.Matrix([pa, pb])
    hchi = -sp.I * s1 * sp.diff(chi, t) + cc * s2 * chi
    n_h = sp.integrate(sp.expand((hchi.H * hchi)[0]), (t, -1, 0))
    rhs_h = sp.integrate(sp.expand((sp.diff(chi, t).H * sp.diff(chi, t))[0] + cc ** 2 * (chi.H * chi)[0]), (t, -1, 0)) \
        - cc * ((chi.H * s3 * chi)[0].subs(t, 0) - (chi.H * s3 * chi)[0].subs(t, -1))
    vals2 = {cc: sp.Rational(5, 4), c1: sp.Rational(1, 3), c2: sp.Rational(2, 5), c3: sp.Rational(-3, 4)}
    d3 = abs(complex(sp.N((n_h - rhs_h).subs(vals2))))
    zm = sp.Matrix([sp.exp(cc * t), 0])
    hz = sp.simplify(-sp.I * s1 * sp.diff(zm, t) + cc * s2 * zm)
    check("A1_spin_half_boundary_identity", d3 < 1e-10 and hz == sp.zeros(2, 1),
          "||h chi||^2 = int |chi'|^2 + c^2 int |chi|^2 - c [chi^dag sigma3 chi]_{-1}^{0} (deviation %.1e) and h (e^{ct}, 0) = 0: the "
          "chiral zero mode is localised (width 1/(2c)) yet massless; its kinetic c^2 and bulk c^2 are cancelled by the fold "
          "term -2c^2/(1 - e^{-2c}) (the Jackiw-Rebbi kink of the bulk mass)" % d3)
    # tip condition from the actions of MODEL.md 4.3: bulk (1/g^2) f^2 e^{3Hy} A_y, tip c v^2 f^3 e^{3Hy} A
    gh, vS, Lc, cn = sp.symbols("ghat v_Sigma L c_n", positive=True)
    bulk_coef = f ** 2 * sp.exp(3 * H * y) / gh ** 2            # from sqrt g g^00 (d_0 A)^2 dx0 = e^{3a4} f^2 e^{3Hy} (A_y)^2 dy
    tip_coef = cn * vS ** 2 * f ** 3 * sp.exp(3 * H * y)         # sqrt|g_tip| = e^{3a4} f^3 e^{3Hy}
    beta_y = sp.simplify(tip_coef / bulk_coef)                   # A_y = beta_y A at the tip
    beta_t = sp.simplify(beta_y * Lc)                            # in t = y/L
    ok_b = sp.simplify(beta_t - cn * gh ** 2 * vS ** 2 * f * Lc) == 0
    check("A1_tip_parameter_scaling", bool(ok_b),
          "matching the bulk gauge kinetic term (1/g^2) e^{3a4} f^2 e^{3Hy} (A_y)^2 to the tip mass term of the sigma field "
          "(sqrt|g_tip| = e^{3a4} f^3 e^{3Hy}) gives u'(-1) = beta u(-1) with beta = c g^2 v_Sigma^2 f L: beta is proportional to f "
          "(the warp factors cancel); the docstring of solution/masses.py wrote c_tip f^2 L e^{3 eta} until UM-1 1.3 (GAPS.md), a different "
          "parametrisation of the same fitted beta")
    res["beta_scaling_exponent_in_f"] = 1
    return res


# ---------------------------------------------------------------------------------------------------------------- A2
def fem_v(eta, n, fold, tip, beta=0.0, nev=6):
    """flat v-form: Q = int v'^2 + (9 eta^2/4) int v^2 - (3 eta/2) v(0)^2 [fold even] + (3 eta/2 + beta) v(-1)^2 [tip Robin];
    linear elements, lumped mass; fold, tip in {'N', 'D'} ('N' at the tip means the Robin condition with beta).
    Returns eigenvalues and node vectors (t from -1 to 0)."""
    h = 1.0 / n
    tn = np.linspace(-1.0, 0.0, n + 1)
    K = np.zeros((n + 1, n + 1))
    for i in range(n):
        K[i, i] += 1 / h
        K[i + 1, i + 1] += 1 / h
        K[i, i + 1] -= 1 / h
        K[i + 1, i] -= 1 / h
    Md = np.full(n + 1, h)
    Md[0] = Md[-1] = h / 2
    K += np.diag(9 * eta ** 2 / 4 * Md)
    K[-1, -1] -= 1.5 * eta
    K[0, 0] += 1.5 * eta + beta
    keep = np.ones(n + 1, bool)
    if fold == "D":
        keep[-1] = False
    if tip == "D":
        keep[0] = False
    Kk = K[np.ix_(keep, keep)]
    s = 1 / np.sqrt(Md[keep])
    A = Kk * s[:, None] * s[None, :]
    w, X = np.linalg.eigh(A)
    V = np.zeros((n + 1, len(w)))
    V[keep] = X * s[:, None]
    return w[:nev], V[:, :nev], tn


def fem_u(eta, n, fold, tip, beta=0.0, nev=6):
    """weighted u-form: Q = int e^{3 eta t} u'^2 + beta e^{-3 eta} u(-1)^2, N = int e^{3 eta t} u^2; exact element weights,
    lumped mass (an independent discretisation of the same problem)"""
    h = 1.0 / n
    tn = np.linspace(-1.0, 0.0, n + 1)
    We = (np.exp(3 * eta * tn[1:]) - np.exp(3 * eta * tn[:-1])) / (3 * eta)
    K = np.zeros((n + 1, n + 1))
    for i in range(n):
        k = We[i] / h ** 2
        K[i, i] += k
        K[i + 1, i + 1] += k
        K[i, i + 1] -= k
        K[i + 1, i] -= k
    Md = np.zeros(n + 1)
    Md[:-1] += We / 2
    Md[1:] += We / 2
    K[0, 0] += beta * math.exp(-3 * eta)
    keep = np.ones(n + 1, bool)
    if fold == "D":
        keep[-1] = False
    if tip == "D":
        keep[0] = False
    Kk = K[np.ix_(keep, keep)]
    s = 1 / np.sqrt(Md[keep])
    w, X = np.linalg.eigh(Kk * s[:, None] * s[None, :])
    U = np.zeros((n + 1, len(w)))
    U[keep] = X * s[:, None]
    return w[:nev], U[:, :nev], tn


def roots_tan(fun, lo, hi, n=4000):
    """sign changes of fun on (lo, hi), refined by bisection, skipping poles (|fun| large on both sides)"""
    xs = np.linspace(lo, hi, n)
    fs = [fun(x) for x in xs]
    out = []
    for i in range(n - 1):
        if fs[i] * fs[i + 1] < 0 and abs(fs[i]) < 50 and abs(fs[i + 1]) < 50:
            a, b, fa = xs[i], xs[i + 1], fs[i]
            for _ in range(100):
                mid = 0.5 * (a + b)
                fm = fun(mid)
                if fm * fa <= 0:
                    b = mid
                else:
                    a, fa = mid, fm
            out.append(0.5 * (a + b))
    return out


def exact_levels(eta, fold, tip, nev=5):
    """exact eigenvalues Lambda of the four boundary classes (beta = 0 Neumann or Dirichlet at the tip)"""
    gap = 9 * eta ** 2 / 4
    if fold == "N" and tip == "N":
        return [0.0] + [gap + (k * math.pi) ** 2 for k in range(1, nev)]
    if fold == "D" and tip == "D":
        return [gap + (k * math.pi) ** 2 for k in range(1, nev + 1)]
    if fold == "D" and tip == "N":      # v = sin(q t): tan q = -2q/(3 eta)
        qs = roots_tan(lambda q: math.sin(q) * 1.5 * eta + q * math.cos(q), 1e-6, (nev + 1) * math.pi)
        return [gap + q * q for q in qs[:nev]]
    # fold N, tip D: below the gap tanh q = 2q/(3 eta) (Lambda = gap - q^2), above it tan q = 2q/(3 eta)
    out = [MS.dirichlet_tip_level(eta)]
    qs = roots_tan(lambda q: math.sin(q) * 1.5 * eta - q * math.cos(q), 1e-6, (nev + 1) * math.pi)
    return out + [gap + q * q for q in qs[: nev - 1]]


def richardson(f1, f2):
    return (4 * np.asarray(f2) - np.asarray(f1)) / 3


def spectra_two_ways(eta=ETA):
    """the four boundary classes by both discretisations (N = 600, 1200, Richardson) against the exact levels"""
    res, worst = {}, 0.0
    for fold in ("N", "D"):
        for tip in ("N", "D"):
            ex = np.array(exact_levels(eta, fold, tip, 5))
            a = richardson(fem_v(eta, 600, fold, tip)[0][:5], fem_v(eta, 1200, fold, tip)[0][:5])
            b = richardson(fem_u(eta, 600, fold, tip)[0][:5], fem_u(eta, 1200, fold, tip)[0][:5])
            dv = np.abs(a - ex) / np.maximum(1, ex)
            du = np.abs(b - ex) / np.maximum(1, ex)
            worst = max(worst, dv.max(), du.max())
            res["fold_%s_tip_%s" % (fold, tip)] = {"exact": ex.tolist(), "v_form": a.tolist(), "u_form": b.tolist(),
                                                   "max_rel_dev_v": float(dv.max()), "max_rel_dev_u": float(du.max()),
                                                   "levels_below_gap": int(np.sum(ex < 9 * eta ** 2 / 4 - 1e-9))}
    return res, worst


def norm_v(v, t):
    return np.trapezoid(v * v, t)


def decompose_boson(v, t, eta, beta):
    """Lambda = K + warp + fold + tip_warp + tip_sigma for a v-form eigenvector on the half; the full cell (both halves,
    mirrored about the fold) has the same quotients; Delta s on the full cell (mean 0 by symmetry), in units f L"""
    nv = norm_v(v, t)
    dv = np.gradient(v, t, edge_order=2)
    K = np.trapezoid(dv * dv, t) / nv
    warp = 9 * eta ** 2 / 4
    fold = -1.5 * eta * v[-1] ** 2 / nv
    tipw = 1.5 * eta * v[0] ** 2 / nv
    tips = beta * v[0] ** 2 / nv
    ds2 = np.trapezoid(t * t * v * v, t) / nv
    return {"K": K, "warp": warp, "fold": fold, "tip_warp": tipw, "tip_sigma": tips, "sum": K + warp + fold + tipw + tips,
            "Delta_s_full_cell_over_fL": math.sqrt(ds2), "uncertainty_product_full_cell": K * ds2}


def decompose_fermion(a, b, t, c):
    """eps^2 (f L)^2 = K + c^2 + fold + tip for a spin-1/2 block profile chi = (a, b) (flat measure of the record)"""
    n = np.trapezoid(a * a + b * b, t)
    da, db = np.gradient(a, t, edge_order=2), np.gradient(b, t, edge_order=2)
    K = np.trapezoid(da * da + db * db, t) / n
    fold = -c * (a[-1] ** 2 - b[-1] ** 2) / n
    tip = c * (a[0] ** 2 - b[0] ** 2) / n
    ds2 = np.trapezoid(t * t * (a * a + b * b), t) / n
    return {"K": K, "bulk_mass": c * c, "fold": fold, "tip": tip, "sum": K + c * c + fold + tip,
            "Delta_s_full_cell_over_fL": math.sqrt(ds2), "uncertainty_product_full_cell": K * ds2}


def coord_spread(rho, t, eta):
    """Delta x0 / ell0 over one period for a density rho(t) on the half (mirrored), x0 - x0_fold = (z - pi/2)/(6H),
    |sin z| = e^{6 eta t}; and the fraction of the probability with z within pi/8 of the tips"""
    zt = np.arcsin(np.clip(np.exp(6 * eta * t), 0, 1))
    n = np.trapezoid(rho, t)
    var = np.trapezoid((zt - math.pi / 2) ** 2 * rho, t) / n
    near_tip = np.trapezoid(np.where(zt < math.pi / 8, rho, 0.0), t) / n
    return math.sqrt(var) / math.pi, near_tip


def odd_psi_level(c):
    """the lowest odd-parity level of the Kohn-Sham block at k = 0: a(0) = 0 (odd fold), b(-1) = 0 (tip theta = 0);
    b = sin(q(t + 1)), tan q = -q/c; (eps f L)^2 = c^2 + q^2"""
    q = roots_tan(lambda q: math.sin(q) * c + q * math.cos(q), 1e-6, math.pi)[0]
    return q, math.sqrt(c * c + q * q)


def particle_table(ms, scales):
    """every particle of UM-1: the decomposition of m^2 and the Heisenberg comparison"""
    eta, f = ETA, F_VAC
    fl = scales["fL_GeV^-1"]
    rows = {}
    n = 4000
    t = np.linspace(-1.0, 0.0, n + 1)

    def boson_row(name, lam_exact, fold, tip, beta, idx, kind):
        w, V, tn = fem_v(eta, 1200, fold, tip, beta, nev=idx + 1)
        v = V[:, idx]
        d = decompose_boson(v, tn, eta, beta)
        # the dressed split Lambda = ||A v||^2 + sigma-field tip term, exact at the discrete level of the u-form
        wu, U, _ = fem_u(eta, 1200, fold, tip, beta, nev=idx + 1)
        uu = U[:, idx]
        h = 1.0 / 1200
        We = (np.exp(3 * eta * tn[1:]) - np.exp(3 * eta * tn[:-1])) / (3 * eta)
        Md = np.zeros(len(tn))
        Md[:-1] += We / 2
        Md[1:] += We / 2
        nrm = float(np.sum(Md * uu * uu))
        dressed = float(np.sum(We * (np.diff(uu) / h) ** 2)) / nrm
        tipu = beta * math.exp(-3 * eta) * uu[0] ** 2 / nrm
        d.update({"dressed_kinetic": dressed, "dressed_tip_sigma": tipu, "Lambda_fem_u": float(wu[idx])})
        lam = lam_exact if lam_exact is not None else float(w[idx])
        mass = math.sqrt(max(lam, 0.0)) / fl
        ds = d["Delta_s_full_cell_over_fL"] * fl
        dx0, near_tip = coord_spread(v * v, tn, eta)
        rows[name] = {"kind": kind, "Lambda": lam, "Lambda_fem": float(w[idx]), "m_GeV": mass, **d,
                      "Delta_s_m": ds * MS.HBARC_GEV_M, "heisenberg_GeV": 1 / (2 * ds),
                      "m_over_heisenberg": mass * 2 * ds, "kinetic_share": d["K"] / lam if lam > 1e-12 else None,
                      "Delta_x0_over_period": dx0, "prob_within_pi_over_8_of_tips": near_tip}

    boson_row("photon_gluon_graviton_zero_mode", 0.0, "N", "N", 0.0, 0, "massless (unbroken gauge, 4D diffeomorphisms)")
    boson_row("W", ms["gauge"]["Lambda_W"], "N", "N", ms["gauge"]["beta_W"], 0, "massive (tip sigma field)")
    boson_row("Z", ms["gauge"]["Lambda_Z"], "N", "N", ms["gauge"]["beta_Z"], 0, "massive (tip sigma field)")
    boson_row("KK_even_n1", MS.neumann_exact(eta, 1), "N", "N", 0.0, 1, "massive (x0 excitation, m_KK)")
    boson_row("KK_odd_n1", exact_levels(eta, "D", "N", 1)[0], "D", "N", 0.0, 0, "massive (odd under the fold reflection)")
    for s in ("e", "u", "d", "nu"):
        c = ms["fermions"][s]["c_f"]
        a, b = np.exp(c * t), np.zeros_like(t)
        dd = decompose_fermion(a, b, t, c)
        ds = dd["Delta_s_full_cell_over_fL"] * fl
        dx0, near_tip = coord_spread(a * a, t, eta)
        mass = ms["fermions"][s]["m_obs_GeV"]
        rows["fermion_" + s] = {"kind": "chiral zero mode, mass from the tip Yukawa m = m_KK zeta(c)^2", "c_f": c, "m_GeV": mass,
                                **dd, "Delta_s_m": ds * MS.HBARC_GEV_M, "heisenberg_GeV": 1 / (2 * ds),
                                "m_over_heisenberg": mass * 2 * ds,
                                "heisenberg_half_cell_GeV_of_masses_json": ms["fermions"][s]["heisenberg_mass_GeV"],
                                "Delta_x0_over_period": dx0, "prob_within_pi_over_8_of_tips": near_tip}
    # Psi (record units H = m = 1, L = 3, f = 8^{-1/2}): c_Psi = f m L
    cps = f * 1.0 * eta
    a, b = np.exp(cps * t), np.zeros_like(t)
    dd = decompose_fermion(a, b, t, cps)
    ds = dd["Delta_s_full_cell_over_fL"] * fl
    rows["Psi_fold_band"] = {"kind": "massless chiral zero mode of Psi (dark radiation)", "c": cps, "m_GeV": 0.0, **dd,
                             "Delta_s_m": ds * MS.HBARC_GEV_M, "heisenberg_GeV": 1 / (2 * ds), "m_over_heisenberg": 0.0}
    q, efl = odd_psi_level(cps)
    th = q * (t + 1)
    bb = np.sin(th)
    aa = (q * np.cos(th) + cps * np.sin(th)) / efl        # from eps a = -i(b'/fL + m b): |a| up to the phase -i
    dd = decompose_fermion(aa, bb, t, cps)
    ds = dd["Delta_s_full_cell_over_fL"] * fl
    mdm = efl / fl
    rows["Psi_dark_matter_odd"] = {"kind": "lowest odd bulk level of Psi (the dark-matter candidate)", "c": cps, "q": q,
                                   "eps_fL": efl, "eps_over_m_record": efl / (f * eta), "m_GeV": mdm, **dd,
                                   "Lambda": efl ** 2, "x0_momentum_share": q * q / efl ** 2, "bulk_mass_share": cps * cps / efl ** 2,
                                   "Delta_s_m": ds * MS.HBARC_GEV_M, "heisenberg_GeV": 1 / (2 * ds), "m_over_heisenberg": mdm * 2 * ds,
                                   "fold_density_normalised": float(bb[-1] ** 2 / np.trapezoid(aa * aa + bb * bb, t))}
    # even bulk level: b(0) = 0 and b(-1) = 0, q = pi
    efl2 = math.sqrt(cps * cps + math.pi ** 2)
    th = math.pi * (t + 1)
    bb = np.sin(th)
    aa = (math.pi * np.cos(th) + cps * np.sin(th)) / efl2
    dd = decompose_fermion(aa, bb, t, cps)
    ds = dd["Delta_s_full_cell_over_fL"] * fl
    rows["Psi_even_bulk"] = {"kind": "lowest even bulk level of Psi", "c": cps, "eps_fL": efl2, "eps_over_m_record": efl2 / (f * eta),
                             "m_GeV": efl2 / fl, **dd, "Lambda": efl2 ** 2, "Delta_s_m": ds * MS.HBARC_GEV_M,
                             "heisenberg_GeV": 1 / (2 * ds), "m_over_heisenberg": efl2 / fl * 2 * ds}
    rows["Psi_fold_band"]["fold_density_normalised"] = float(2 * cps / (-math.expm1(-2 * cps)))
    return rows


def sensitivities(ms):
    """d ln m / d ln f at fixed eight-dimensional parameters (mu_f, m, v_Sigma, couplings, coordinate L, H)"""
    eta = ETA
    out = {"photon_gluon_graviton": 0.0, "KK_tower": -1.0, "alpha_em": -4.0, "G_Newton": -4.0}
    bW = ms["gauge"]["beta_W"]
    d = 1e-4
    for nm, bb in (("W", bW), ("Z", ms["gauge"]["beta_Z"])):
        lp, lm = MS.lowest_robin(eta, bb * (1 + d)), MS.lowest_robin(eta, bb * (1 - d))
        dl = (math.log(lp) - math.log(lm)) / (math.log(1 + d) - math.log(1 - d))
        out[nm] = -1.0 + 0.5 * dl                      # beta proportional to f (A1_tip_parameter_scaling)
        out[nm + "_dlnLambda_dlnbeta"] = dl
    for s in ("e", "u", "d", "nu"):
        c = ms["fermions"][s]["c_f"]
        z2 = lambda cc: math.log(MS.zeta2(cc))
        dz = (z2(c * (1 + d)) - z2(c * (1 - d))) / (math.log(1 + d) - math.log(1 - d))
        out["fermion_" + s] = -1.0 + dz
        out["fermion_" + s + "_closed_form"] = -1.0 + 1 - 2 * c - 2 * c * math.exp(-2 * c) / (-math.expm1(-2 * c))
    cps = F_VAC * eta

    def lneps(fac):
        c = cps * fac
        return math.log(odd_psi_level(c)[1] / fac)       # eps = (eps f L)/(f L), f L proportional to f
    out["Psi_dark_matter_odd"] = (lneps(1 + d) - lneps(1 - d)) / (math.log(1 + d) - math.log(1 - d))
    # QCD: Lambda_QCD = m_KK exp(-2 pi/(b0 alpha_s(m_KK))), one loop, n_f = 2 (u, d: one generation), alpha_s(m_Z) = 0.1180
    b0 = 11 - 2 * 2 / 3
    ainv = 1 / 0.1180 + b0 / (2 * math.pi) * math.log(ms["inputs"]["m_KK_GeV"] / 91.1880)
    out["Lambda_QCD_proton"] = -1.0 - 8 * math.pi * ainv / b0
    out["Lambda_QCD_inputs"] = {"b0": b0, "alpha_s_mKK": 1 / ainv, "alpha_s_mZ": 0.1180, "label": "ESTIMATE (one loop, STANDARD formula)"}
    out["mp_over_me"] = out["Lambda_QCD_proton"] - out["fermion_e"]
    return out


def deflation_bound(sens, late):
    """atomic-clock bounds (FROM MEMORY, Lange et al. 2021, PRL 126, 011102): d ln alpha/dt = (1.0 +- 1.1) e-18 /yr,
    d ln(m_p/m_e)/dt = (-8 +- 36) e-18 /yr; 2 sigma ranges -> |d ln f/dt| -> |h4|/H0 (H0 = 67.36 km/s/Mpc)"""
    yr = 365.25 * 86400
    H0_per_yr = 67.36 / 3.0856775814913673e19 * yr
    a_lim = (abs(1.0) + 2 * 1.1) * 1e-18
    mu_lim = (abs(-8) + 2 * 36) * 1e-18
    h_alpha = a_lim / abs(sens["alpha_em"])
    h_mu = mu_lim / abs(sens["mp_over_me"])
    best = min(h_alpha, h_mu)
    return {"H0_per_yr": H0_per_yr, "alpha_bound_per_yr": a_lim, "mu_bound_per_yr": mu_lim,
            "h4_bound_from_alpha_per_yr": h_alpha, "h4_bound_from_mu_per_yr": h_mu,
            "h4_over_H0_bound": best / H0_per_yr, "h4_over_A_model_today": late["h4_over_A_today"],
            "source": "FROM MEMORY: Lange et al. 2021 (Yb+ clocks); used as orders of magnitude"}


def no_cutoff_limit():
    """eta = 3, 6, 12, 24: the zero mode stays at 0, the first excitation of either parity tends to the gap 9 eta^2/4 from
    above (m_1 f/H -> 3/2), the weighted volume (1 - e^{-3 eta})/(3 eta) L -> 1/(3H)"""
    out = []
    for eta in (3.0, 6.0, 12.0, 24.0):
        we, _, _ = fem_v(eta, 2400, "N", "N", nev=2)
        wo, _, _ = fem_v(eta, 2400, "D", "N", nev=1)
        out.append({"eta": eta, "zero_mode_Lambda": float(we[0]), "m1_even_f_over_H": math.sqrt(we[1]) / eta,
                    "m1_odd_f_over_H": math.sqrt(wo[0]) / eta,
                    "m1_even_exact_f_over_H": math.sqrt(MS.neumann_exact(eta, 1)) / eta,
                    "weighted_volume_H": (1 - math.exp(-3 * eta)) / 3})
    return out


def gap_theorem(eta=ETA):
    """count levels below 9 eta^2/4: even fold, any tip beta >= 0 -> exactly one; odd fold -> none"""
    gap = 9 * eta ** 2 / 4
    res = []
    for beta in (0.0, 1e-3, 0.0119, 1.0, 1e2, 1e6):
        we = fem_v(eta, 1200, "N", "N", beta, nev=4)[0]
        wo = fem_v(eta, 1200, "D", "N", beta, nev=4)[0]
        res.append({"beta": beta, "even_below_gap": int(np.sum(we < gap * (1 - 1e-6))),
                    "odd_below_gap": int(np.sum(wo < gap * (1 - 1e-6))), "even_lowest": float(we[0]), "odd_lowest": float(wo[0])})
    return res


def figures(tab, spectra, sens):
    FIG.mkdir(parents=True, exist_ok=True)
    eta = ETA
    # figA1: v-profiles on the full cell (proper coordinate s/(fL) in [-1, 1]) and the potential
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
    for (fold, tip, beta, idx, lab, ls) in (("N", "N", 0.0, 0, "zero mode (photon, gluon, graviton)", "-"),
                                            ("N", "N", 0.0, 1, "first even excitation (m_KK)", "-"),
                                            ("D", "N", 0.0, 0, "first odd mode", "-"),
                                            ("N", "D", 0.0, 0, "Dirichlet-tip level (the largest W)", "--")):
        w, V, tn = fem_v(eta, 1200, fold, tip, beta, nev=idx + 1)
        v = V[:, idx] / math.sqrt(2 * norm_v(V[:, idx], tn))
        if v[np.argmax(np.abs(v))] < 0:
            v = -v
        sgn = -1 if fold == "D" else 1
        s = np.concatenate([tn, -tn[::-1]])
        vv = np.concatenate([v, sgn * v[::-1]])
        ax[0].plot(s, vv, ls=ls, label="%s, (m f L)^2 = %.4g (exact)" % (lab, exact_levels(eta, fold, tip, idx + 1)[idx]))
    ax[0].set_xlabel("proper hidden coordinate s/(fL)   (fold at 0, tips at -1 and 1)")
    ax[0].set_ylabel("v = e^{3Hy/2} u (flat measure)")
    ax[0].legend(fontsize=7)
    ax[0].set_title("x0 wave functions on one period (both halves)")
    ss = np.linspace(-1, 1, 801)
    ax[1].plot(ss, np.full_like(ss, 9 * eta ** 2 / 4), "k-", label="warp potential 9 eta^2/4 = (3H/2f)^2 (fL)^2")
    ax[1].annotate("", xy=(0, -1.5), xytext=(0, 9 * eta ** 2 / 4), arrowprops=dict(arrowstyle="-|>", color="C3", lw=2))
    for sx in (-1, 1):
        ax[1].annotate("", xy=(sx, 40), xytext=(sx, 9 * eta ** 2 / 4), arrowprops=dict(arrowstyle="-|>", color="C1", lw=2))
    ax[1].annotate("fold: attractive delta -3 eta delta(s)", xy=(0, 20.25), xytext=(-0.9, 8), arrowprops=dict(arrowstyle="->"), fontsize=8)
    ax[1].annotate("tips: repulsive delta +3 eta delta(s -+ 1)", xy=(1, 20.25), xytext=(0.05, 32), arrowprops=dict(arrowstyle="->"), fontsize=8)
    for lev in spectra["fold_N_tip_N"]["exact"][:3]:
        ax[1].axhline(lev, color="C0", ls=":", lw=1)
    for lev in spectra["fold_D_tip_N"]["exact"][:2]:
        ax[1].axhline(lev, color="C2", ls="--", lw=1)
    ax[1].set_ylim(-2, 70)
    ax[1].set_xlabel("s/(fL)")
    ax[1].set_ylabel("(m f L)^2")
    ax[1].set_title("the mass operator -d_s^2 + V(s): levels (even dotted, odd dashed)")
    ax[1].legend(fontsize=7, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG / "figA1_x0_wave_functions_and_potential.png", dpi=130)
    plt.close(fig)
    # figA2: decomposition
    names = ["photon_gluon_graviton_zero_mode", "W", "KK_even_n1", "KK_odd_n1", "fermion_e", "fermion_nu", "Psi_fold_band",
             "Psi_dark_matter_odd", "Psi_even_bulk"]
    lab = ["photon/gluon/\ngraviton", "W", "KK even 1", "KK odd 1", "electron\n(zero mode)", "neutrino\n(zero mode)",
           "Psi fold\nband", "Psi DM\n(odd)", "Psi even\nbulk"]
    fig, ax = plt.subplots(figsize=(11, 4.6))
    xs = np.arange(len(names))
    parts = [("K", "hidden kinetic <p^2>"), ("warp", "warp / bulk mass"), ("fold", "fold term"), ("tip", "tip terms"),
             ("sum", "(m f L)^2")]
    for j, (key, lb) in enumerate(parts):
        vals = []
        for nm in names:
            r = tab[nm]
            if key == "warp":
                vals.append(r.get("warp", r.get("bulk_mass")))
            elif key == "tip":
                vals.append(r.get("tip_warp", 0) + r.get("tip_sigma", 0) + r.get("tip", 0))
            elif key == "sum":
                vals.append(r.get("Lambda", 0.0))
            else:
                vals.append(r[key])
        ax.bar(xs + (j - 2) * 0.16, vals, width=0.16, label=lb)
    ax.axhline(0, color="k", lw=0.8)
    ax.set_yscale("symlog", linthresh=1e-2)
    ax.set_xticks(xs)
    ax.set_xticklabels(lab, fontsize=8)
    ax.set_ylabel("term of (m f L)^2  (symmetric log scale)")
    ax.set_title("m^2 = <p^2> + warp + fold + tip: zero modes are localised but massless (the fold term cancels)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "figA2_mass_decomposition.png", dpi=130)
    plt.close(fig)
    # figA3: actual mass against the Heisenberg estimate
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    pts = [("W", "W"), ("Z", "Z"), ("KK_even_n1", "KK even 1"), ("KK_odd_n1", "KK odd 1"), ("fermion_e", "e"),
           ("fermion_u", "u"), ("fermion_d", "d"), ("fermion_nu", "nu"), ("Psi_dark_matter_odd", "Psi DM"), ("Psi_even_bulk", "Psi even bulk")]
    offs = {"W": (4, -10), "Z": (4, 4), "KK_even_n1": (-50, 6), "KK_odd_n1": (-48, -10), "Psi_dark_matter_odd": (6, -10),
            "Psi_even_bulk": (6, 4), "fermion_nu": (6, 2)}
    for nm, lb in pts:
        r = tab[nm]
        ax.loglog(r["heisenberg_GeV"], r["m_GeV"], "o")
        ax.annotate(lb, (r["heisenberg_GeV"], r["m_GeV"]), fontsize=8, xytext=offs.get(nm, (4, 2)), textcoords="offset points")
    r0 = tab["photon_gluon_graviton_zero_mode"]
    ax.axvline(r0["heisenberg_GeV"], color="grey", ls=":", label="photon zero mode: hbar c/(2 Delta s) = %.0f TeV, m = 0" % (r0["heisenberg_GeV"] / 1e3))
    xx = np.logspace(4.0, 6.3, 10)
    ax.loglog(xx, xx, "k--", label="m c^2 = hbar c/(2 Delta s) (the author's estimate)")
    ax.set_ylim(1e-11, 3e6)
    ax.set_xlabel("hbar c/(2 Delta s)  [GeV], Delta s on the full period")
    ax.set_ylabel("mass [GeV]")
    ax.set_title("the Heisenberg estimate holds for x0 excitations, fails for zero modes")
    ax.legend(fontsize=7, loc="lower left")
    fig.tight_layout()
    fig.savefig(FIG / "figA3_mass_vs_heisenberg.png", dpi=130)
    plt.close(fig)
    # figA4: proper vs coordinate density of the zero mode over two periods of x0
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    z = np.linspace(1e-4, 2 * math.pi - 1e-4, 6001)
    sz = np.abs(np.sin(z))
    rho_z = 0.5 * np.abs(np.cos(z)) / np.sqrt(sz)        # e^{3Hy} |dy/dz| normalised per half
    ax[0].plot(z / math.pi, rho_z / 2)
    ax[0].set_ylim(0, 3)
    ax[0].set_xlabel("x0 / (pi/(6H))   (folds at 1/2, 3/2; tips at 0, 1, 2)")
    ax[0].set_ylabel("probability per unit z")
    ax[0].set_title("zero mode in the coordinate x0: piled up at the TIPS")
    s = np.linspace(-1, 1, 2001)
    ax[1].plot(s, 1.5 * eta * np.exp(-3 * eta * np.abs(s)) / (2 * (1 - math.exp(-3 * eta))))
    ax[1].set_xlabel("proper coordinate s/(fL)")
    ax[1].set_ylabel("probability per unit s/(fL)")
    ax[1].set_title("the same mode in proper length: localised at the FOLD")
    fig.tight_layout()
    fig.savefig(FIG / "figA4_coordinate_vs_proper.png", dpi=130)
    plt.close(fig)
    # figA5: sensitivities
    keys = [("KK_tower", "KK, gap"), ("W", "W"), ("Z", "Z"), ("fermion_e", "e"), ("fermion_u", "u"), ("fermion_d", "d"),
            ("fermion_nu", "nu"), ("Psi_dark_matter_odd", "Psi DM"), ("alpha_em", "alpha"), ("G_Newton", "G_N"),
            ("Lambda_QCD_proton", "m_p (QCD)")]
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.bar(range(len(keys)), [sens[k] for k, _ in keys])
    ax.set_xticks(range(len(keys)))
    ax.set_xticklabels([lb for _, lb in keys], fontsize=8)
    ax.set_ylabel("d ln X / d ln f")
    ax.set_title("sensitivity to the block size f: a deflating block makes every x0-generated mass drift")
    fig.tight_layout()
    fig.savefig(FIG / "figA5_sensitivity_to_f.png", dpi=130)
    plt.close(fig)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    REP.mkdir(parents=True, exist_ok=True)
    ms = json.loads((UM / "solution" / "outputs" / "masses.json").read_text(encoding="utf-8"))
    late = json.loads((UM / "solution" / "outputs" / "late_time.json").read_text(encoding="utf-8"))
    spec_ks = json.loads((UM / "solution" / "outputs" / "ks" / "spectrum.json").read_text(encoding="utf-8"))
    res = {"units": "H = 1 (cell), eta = H L = 3, f = 8^{-1/2}, t = y/L; Lambda = (m f L)^2"}
    res["exact"] = part_a1()
    spectra, worst = spectra_two_ways()
    res["spectra"] = spectra
    check("A2_spectra_two_discretisations", worst < 2e-6,
          "the four boundary classes (fold N/D x tip N/D): flat v-form and weighted u-form finite elements (600, 1200 elements, "
          "Richardson) agree with the exact levels to %.1e relative" % worst)
    gap = gap_theorem()
    res["gap_theorem"] = gap
    ok_gap = all(r["even_below_gap"] == 1 and r["odd_below_gap"] == 0 for r in gap)
    check("A2_gap_theorem", ok_gap,
          "for tip parameters beta in {0, 1e-3, 0.0119, 1, 1e2, 1e6}: exactly one level below the warp gap 9 eta^2/4 in the "
          "even sector (the zero mode, lifted only by the tip) and none in the odd sector (Dirichlet at the fold removes the "
          "attractive fold term): every odd mode and every excitation has m >= 3H/(2f)")
    lim = no_cutoff_limit()
    res["no_cutoff_limit"] = lim
    # the flat-form zero mode carries the discretisation error h^2 (3 eta/2)^4/12 of its sharp profile e^{3 eta t/2}; it is
    # measured against the scale of the spectrum, the gap 9 eta^2/4 (the weighted u-form has the zero mode exactly)
    ok_lim = all(abs(r["zero_mode_Lambda"]) < 1e-4 * 9 * r["eta"] ** 2 / 4 for r in lim) and \
        all(lim[i + 1]["m1_even_exact_f_over_H"] < lim[i]["m1_even_exact_f_over_H"] for i in range(3)) and \
        abs(lim[-1]["m1_even_exact_f_over_H"] - 1.5) < 0.01 and all(r["m1_odd_f_over_H"] > 1.5 for r in lim)
    check("A2_no_cutoff_limit", ok_lim,
          "eta = 3, 6, 12, 24: the zero mode stays massless, the first even and odd excitations fall toward the gap 3H/(2f) "
          "from above (m_1 f/H = %.4f, %.4f, %.4f, %.4f even), the weighted volume tends to 1/(3H)"
          % tuple(r["m1_even_exact_f_over_H"] for r in lim))
    tab = particle_table(ms, ms["scales"])
    res["particles"] = tab
    sums = [abs(r["sum"] - r["Lambda"]) / max(1.0, r["Lambda"]) for k, r in tab.items() if isinstance(r, dict) and "Lambda" in r]
    ferm_zero = [abs(tab["fermion_" + s]["sum"]) / tab["fermion_" + s]["bulk_mass"] for s in ("e", "u", "d", "nu")] + \
        [abs(tab["Psi_fold_band"]["sum"]) / tab["Psi_fold_band"]["bulk_mass"]]
    check("A2_decomposition_sum_rule", max(sums) < 5e-4 and max(ferm_zero) < 1e-4,
          "for every boson and Psi level K + warp + fold + tip = (m f L)^2 to %.1e (finite elements, 1200 elements), for every "
          "chiral zero mode K + c^2 + fold + tip = 0 to %.1e of c^2" % (max(sums), max(ferm_zero)))
    z0 = tab["photon_gluon_graviton_zero_mode"]
    ok_zero = abs(z0["sum"]) < 1e-3 and z0["fold"] < -0.9 * z0["K"] and z0["heisenberg_GeV"] > 5e4
    check("A2_localised_massless_modes", ok_zero,
          "the photon/gluon/graviton zero mode is localised at the fold (Delta s = %.3g fL) with hidden kinetic energy K = %.4g, "
          "cancelled by warp %.4g and fold %.4g: m = 0 while hbar c/(2 Delta s) = %.0f GeV; the uncertainty product on the period "
          "is %.3f >= 1/4" % (z0["Delta_s_full_cell_over_fL"], z0["K"], z0["warp"], z0["fold"], z0["heisenberg_GeV"],
                              z0["uncertainty_product_full_cell"]))
    heavy = ["KK_even_n1", "KK_odd_n1", "Psi_dark_matter_odd", "Psi_even_bulk"]
    ok_heavy = all(tab[k]["m_over_heisenberg"] >= 1.0 for k in heavy)
    check("A2_heisenberg_holds_for_excitations", ok_heavy,
          "for the x0 excitations the author's estimate is a true lower bound: m/(hbar c/(2 Delta s)) = "
          + ", ".join("%s %.3f" % (k, tab[k]["m_over_heisenberg"]) for k in heavy))
    light = ["W", "Z", "fermion_e", "fermion_u", "fermion_d", "fermion_nu"]
    ok_light = all(tab[k]["m_over_heisenberg"] < 1e-2 for k in light)
    check("A2_heisenberg_fails_for_light_particles", ok_light,
          "for the light particles the actual mass is far below the estimate: m/(hbar c/(2 Delta s)) = "
          + ", ".join("%s %.2e" % (k, tab[k]["m_over_heisenberg"]) for k in light)
          + "; their masses come from the tip (sigma field, Yukawa), not from localisation")
    dm = tab["Psi_dark_matter_odd"]
    rec = spec_ks["vacuum"]["lowest_odd_bulk_analytic"]
    ok_dm = abs(dm["eps_over_m_record"] - rec) < 1e-10 and dm["x0_momentum_share"] > 0.7 and dm["fold"] > 0 and dm["tip"] > 0
    check("A2_dark_matter_mass_is_x0_momentum", ok_dm,
          "the lowest odd Psi level eps = %.12f m (record %.12f): the x0 standing wave carries %.1f %% of eps^2 and the bulk mass "
          "%.1f %%; its fold and tip terms are positive, so m^2 >= <p^2> + m^2_bulk" % (dm["eps_over_m_record"], rec,
                                                                                       100 * dm["x0_momentum_share"], 100 * dm["bulk_mass_share"]))
    wW = tab["W"]
    lu = wW["dressed_kinetic"] + wW["dressed_tip_sigma"]
    check("A2_W_mass_is_a_tip_term", wW["dressed_tip_sigma"] / lu > 0.99 and wW["dressed_kinetic"] / lu < 0.01
          and abs(wW["Lambda_fem_u"] / wW["Lambda"] - 1) < 1e-3,
          "W: in the dressed split m^2 = ||A v||^2 + tip the x0 dependence of the profile gives %.2e of m_W^2 and the sigma-field "
          "tip term %.6f (SOLUTION.md check M3: bulk part %.2e); in the flat form its kinetic energy K = %.4f is %.2e times m_W^2 "
          "and is cancelled by warp + fold" % (wW["dressed_kinetic"] / lu, wW["dressed_tip_sigma"] / lu,
                                              ms["gauge"]["rayleigh_W"]["bulk_hidden_momentum"] / ms["gauge"]["Lambda_W"],
                                              wW["K"], wW["K"] / wW["Lambda"]))
    e = tab["fermion_e"]
    check("A2_localisation_lowers_fermion_masses", e["heisenberg_GeV"] > 1e5 and e["m_over_heisenberg"] < 1e-8,
          "electron: c = %.3f, Delta s = %.3g m, hbar c/(2 Delta s) = %.0f GeV, m_e = %.3e GeV: m_f = m_KK zeta(c)^2 ~ 2c e^{-2c} m_KK "
          "FALLS as the localisation 1/(2c) sharpens (d ln m_f/d ln c = 1 - 2c - ...), the reverse of the Heisenberg argument"
          % (e["c_f"], e["Delta_s_m"], e["heisenberg_GeV"], e["m_GeV"]))
    co = [tab[k]["Delta_x0_over_period"] for k in ("photon_gluon_graviton_zero_mode", "fermion_e")]
    check("A2_coordinate_localisation_is_not_physical", tab["photon_gluon_graviton_zero_mode"]["prob_within_pi_over_8_of_tips"] > 0.3,
          "in the coordinate x0 the zero mode, localised at the fold in proper length, has %.0f %% of its probability within pi/8 "
          "of the TIPS (Delta x0/period = %.3f; electron %.3f): g_00 = f^2 cot^2 z vanishes at the fold, so a coordinate "
          "uncertainty relation says nothing about the mass; only the proper form Delta s Delta p >= hbar/2 does"
          % (100 * tab["photon_gluon_graviton_zero_mode"]["prob_within_pi_over_8_of_tips"], co[0], co[1]))
    sens = sensitivities(ms)
    res["sensitivity_dln_dlnf"] = sens
    ok_s = abs(sens["fermion_e"] - sens["fermion_e_closed_form"]) < 1e-6 and -0.6 < sens["W"] < -0.4 and sens["Psi_dark_matter_odd"] < -0.5
    check("A2_sensitivities", ok_s,
          "d ln m/d ln f: KK -1, W %.4f, Z %.4f (beta proportional to f), e %.3f (closed form %.3f), u %.3f, d %.3f, nu %.3f, Psi DM %.4f, "
          "alpha -4, G_N -4, Lambda_QCD %.1f (ESTIMATE), m_p/m_e %.1f" % (sens["W"], sens["Z"], sens["fermion_e"], sens["fermion_e_closed_form"],
                                                                         sens["fermion_u"], sens["fermion_d"], sens["fermion_nu"],
                                                                         sens["Psi_dark_matter_odd"], sens["Lambda_QCD_proton"], sens["mp_over_me"]))
    dm_ks = json.loads((UM / "solution" / "outputs" / "ks" / "dm_lam0.json").read_text(encoding="utf-8"))
    p0r = dm_ks["cases"]["lam0"]["richardson"]["p0_over_rho_dm"][0]
    ptr = dm_ks["cases"]["lam0"]["1200"]["pt_over_rho_dm"]
    res["hidden_pressure_identity"] = {"minus_dln_eps_dln_f": -sens["Psi_dark_matter_odd"], "p0_over_rho_KS": p0r,
                                       "pt_over_rho_KS": ptr, "abs_dev": abs(-sens["Psi_dark_matter_odd"] - p0r)}
    check("A2_hidden_pressure_is_the_x0_mass", abs(-sens["Psi_dark_matter_odd"] - p0r) < 1e-8 and ptr == 0.0,
          "the hidden pressure of the dark-matter quanta in the Kohn-Sham energy-momentum tensor (solution/outputs/ks/dm_lam0.json, "
          "Richardson) p0/rho = %.10f equals -d ln eps/d ln f = %.10f of the x0-generated mass (deviation %.1e; p_t = 0): the pressure "
          "of a quantum on the hidden direction is -dE/d ln(proper length), so the EMT of the record confirms independently that "
          "the dark-matter mass is generated by x0 (1 for a pure x0 momentum, 0 for a bulk mass)" % (p0r, -sens["Psi_dark_matter_odd"],
                                                                                                  abs(-sens["Psi_dark_matter_odd"] - p0r)))
    bound = deflation_bound(sens, late)
    res["deflation_bound_today"] = bound
    check("A2_deflation_bound_today", abs(bound["h4_over_A_model_today"]) < bound["h4_over_H0_bound"],
          "atomic clocks (FROM MEMORY) bound |h4|/H0 < %.1e today; UM-1 has h4/A = %.2e (SOLUTION.md section 3.4); the "
          "primordial h4 = -H/3 would change m_e by a factor e every %.1e s and must end before nucleosynthesis"
          % (bound["h4_over_H0_bound"], bound["h4_over_A_model_today"], 3.0 / abs(sens["fermion_e"]) / ms["scales"]["H_GeV"] * 6.582119569e-25))
    figures(tab, spectra, sens)
    (OUT / "x0_mass.json").write_text(json.dumps(res, indent=1, default=float, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    rep = {"checks": CHECKS, "pass": sum(c["verdict"] == "PASS" for c in CHECKS), "total": len(CHECKS)}
    (REP / "x0-mass-checks.json").write_text(json.dumps(rep, indent=1) + "\n", encoding="utf-8", newline="\n")
    print("%d of %d checks PASS" % (rep["pass"], rep["total"]))
    return 0 if rep["pass"] == rep["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
