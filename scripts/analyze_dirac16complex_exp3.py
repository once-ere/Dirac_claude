"""EXP-3 analysis: CPL fits, distance-modulus fits, fine x0 scan, Unite comparison.

numpy + standard library only (Nelder-Mead implemented here; no scipy).
Everything is computed from the closed forms of NUMERICS_CONTRACT EXP-3; the
Rust CVODE output is used only for an independent cross-check of the
comoving-distance quadrature (state column D_C).

Model (units H0 = c = 1, flat, Omega_r = 0.00009, Omega_m = 0.305):
  dirac16complex:  rho_psi = A sigma (1 + x0 sigma), A = Omega_psi/(1 + x0),
                   sigma = a^-n (n = 3: stabilised extra dimensions; the
                   deflation-index variant has n = 3 (1 - gamma)),
                   w = p/rho = x0 sigma/(1 + x0 sigma),
                   w_eff = -1 - (1/3) dln rho/dln a = -1 + (n/3)(1 + 2 x0 sigma)/(1 + x0 sigma)
                   (w_eff = w for n = 3; w_eff is what distances measure).
  CPL:             w(a) = w0 + wa (1 - a)  (wa = -dw/da),
                   rho_DE = Omega_DE a^{-3(1 + w0 + wa)} exp(-3 wa (1 - a)),
                   Omega_DE = 1 - Omega_m - Omega_r = 0.69491.
  distance modulus mu(z) = 5 log10((1 + z) D_C(z)) + const, D_C = int_0^z dz'/E.
                   The constant (H0 and the SN absolute magnitude) is either
                   profiled analytically ("offsetProfiled", the H0-free fit) or
                   set to zero ("offsetZero", same H0 for model and fit).

Fits (as in the contract):
  (1) tangent CPL at a = 1: w0 = w(1), wa = -dw/da|_1 (closed form);
  (2) least-squares CPL fit of w(a) on a in [1/3.26, 1]: uniform a grid of
      1001 points, equal weights; linear least squares (CPL is linear in
      (w0, wa)), cross-checked by Nelder-Mead;
  (3) least-squares CPL and constant-w fits of mu(z) on z in [0.01, 2.26]:
      uniform z grid, step 0.005 (451 points), equal weights, Nelder-Mead.
  Domains: for x0 < 0, w(a) has a pole at a = |x0|^(1/3) (rho_psi = 0) and
  E^2 = 0 at the bounce a_b; a fit whose range contains the pole (2) or the
  bounce (3) is UNDEFINED (divergent least-squares integral, resp. no
  redshift beyond z_b) and is reported as such.  Supplementary restricted
  fits, clearly labelled: (2r) a in [max(1/3.26, a(w = -3)), 1] with
  a(w = -3) = (4|x0|/3)^(1/n); (3r) z in [0.01, min(2.26, z_b)].
  Also: the Unite CPL model's own mu(z) and its best constant-w projection,
  both with Omega_m fixed at 0.305 (the value assumed by the numerical
  programme; the reference PDF gives no Omega_m) and with Omega_m free (flat
  wCDM, (w, Omega_m) fitted together, as an SN-only wCDM fit would do);
  the deflation-index gamma reproducing the Unite tangent (w0, wa) with the
  physical objections.

Outputs (artifacts/dirac16complex/numerics/exp3/): fits.json (fixed key
order, 2-space indent, floats as C %.17e), fits_scan.csv (fine scan
x0 in [-0.49, 0], step 0.001, closed forms + w(a) fits) and
fits_mu_scan.csv (step 0.01, distance-modulus fits).  Prints
check_<name>=true/false for the internal validations and exits 1 on failure.

Usage: python scripts/analyze_dirac16complex_exp3.py [--output ROOT]
"""

import argparse
import math
import os
import sys

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_ROOT = os.path.join(REPO, "artifacts", "dirac16complex", "numerics")
EXPERIMENT = "exp3"

OMEGA_R, OMEGA_M, OMEGA_PSI = 0.00009, 0.305, 0.69491
OMEGA_DE = 1.0 - OMEGA_M - OMEGA_R
UNITE_W0, UNITE_WA, UNITE_WCONST = -0.861, -0.60, -0.764
X0_CANONICAL = [-0.462654, -0.433107, -0.3, -0.2, 0.0]
A_FIT_MIN = 1.0 / 3.26
Z_FIT_MIN, Z_FIT_MAX, Z_FIT_STEP = 0.01, 2.26, 0.005
A_FIT_POINTS = 1001
W_FLOOR = -3.0
SCAN_STEP_MILLI = 1          # fine scan x0 = k / 1000, k = -490 .. 0
MU_SCAN_STEP_CENTI = 1       # mu-fit scan x0 = k / 100, k = -49 .. 0
GL_NODES, GL_WEIGHTS = np.polynomial.legendre.leggauss(8)
H0_PER_YEAR = 67.4 / 3.0856775814913673e19 * 3.15576e7   # 67.4 km/s/Mpc in 1/yr
LLR_GDOT_BOUND = 1.0e-13                                 # |Gdot/G| per yr, order of magnitude


# ---------------------------------------------------------------- models

class Dirac16:
    """4D-effective dirac16complex condensate, sigma = a^-n."""

    def __init__(self, x0, n=3.0):
        self.x0, self.n = x0, n
        self.amp = OMEGA_PSI / (1.0 + x0)

    def sigma(self, a):
        return a ** (-self.n)

    def rho(self, a):
        s = self.sigma(a)
        return self.amp * s * (1.0 + self.x0 * s)

    def e2(self, z):
        a = 1.0 / (1.0 + z)
        return OMEGA_R * (1.0 + z) ** 4 + OMEGA_M * (1.0 + z) ** 3 + self.rho(a)

    def w(self, a):
        s = self.sigma(a)
        return self.x0 * s / (1.0 + self.x0 * s)

    def w_eff(self, a):
        s = self.sigma(a)
        return -1.0 + (self.n / 3.0) * (1.0 + 2.0 * self.x0 * s) / (1.0 + self.x0 * s)

    def tangent(self):
        """(w0, wa) of w = p/rho: wa = n x0/(1 + x0)^2."""
        return self.x0 / (1.0 + self.x0), self.n * self.x0 / (1.0 + self.x0) ** 2

    def tangent_eff(self):
        """(w0, wa) of w_eff: w0 = -1 + (n/3)(1+2x0)/(1+x0), wa = (n^2/3) x0/(1+x0)^2."""
        return (-1.0 + (self.n / 3.0) * (1.0 + 2.0 * self.x0) / (1.0 + self.x0),
                self.n * self.n / 3.0 * self.x0 / (1.0 + self.x0) ** 2)

    def a_zero(self):
        return abs(self.x0) ** (1.0 / self.n) if self.x0 < 0.0 else None

    def a_cross(self):
        return (2.0 * abs(self.x0)) ** (1.0 / self.n) if self.x0 < 0.0 else None

    def a_w(self, w_value):
        """a where w = w_value (< w0): x0 sigma = w/(1 - w)."""
        if self.x0 >= 0.0:
            return None
        y = w_value / (1.0 - w_value)
        return (self.x0 / y) ** (1.0 / self.n)

    def bounce(self):
        """Largest a in (0, 1) with E^2 = 0 (scan in ln a, then bisection); None if E^2 > 0."""
        if self.x0 >= 0.0:
            return None
        grid = np.exp(np.linspace(0.0, math.log(1e-4), 40001))
        e2 = self.e2(1.0 / grid - 1.0)
        bad = np.flatnonzero(e2 <= 0.0)
        if len(bad) == 0:
            return None
        hi, lo = grid[bad[0] - 1], grid[bad[0]]
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if mid <= lo or mid >= hi:
                break
            if self.e2(1.0 / mid - 1.0) > 0.0:
                hi = mid
            else:
                lo = mid
        return 0.5 * (lo + hi)

    def q0(self):
        """q = -1 - dlnE/dN at a = 1 with drho/dN = -n A sigma (1 + 2 x0 sigma) (E(1) = 1);
        for n = 3 this equals (2 Omega_r + Omega_m + rho + 3 p)/2."""
        return -1.0 + (4.0 * OMEGA_R + 3.0 * OMEGA_M + self.n * self.amp * (1.0 + 2.0 * self.x0)) / 2.0

    def cs2_today(self):
        return 2.0 * self.x0 / (1.0 + 2.0 * self.x0)


class CPL:
    def __init__(self, w0, wa):
        self.w0, self.wa = w0, wa

    def e2(self, z):
        zp = 1.0 + z
        de = OMEGA_DE * zp ** (3.0 * (1.0 + self.w0 + self.wa)) * np.exp(-3.0 * self.wa * z / zp)
        return OMEGA_R * zp ** 4 + OMEGA_M * zp ** 3 + de

    def w(self, a):
        return self.w0 + self.wa * (1.0 - a)


class WCDMFreeOmegaM:
    """Flat wCDM with its own Omega_m (radiation Omega_r fixed): the family of an
    SN-only constant-w fit, in which Omega_m is not fixed."""

    def __init__(self, w, omega_m):
        self.w, self.omega_m = w, omega_m

    def e2(self, z):
        zp = 1.0 + z
        omega_de = 1.0 - self.omega_m - OMEGA_R
        return OMEGA_R * zp ** 4 + self.omega_m * zp ** 3 + omega_de * zp ** (3.0 * (1.0 + self.w))


# ---------------------------------------------------------------- distances

def comoving_distance(e2, z_grid, z_bounce=None):
    """D_C(z_i) = int_0^{z_i} dz/E, composite 8-point Gauss-Legendre per grid panel.

    With a bounce z_b (E^2 ~ (z_b - z)), the integral is done in s = sqrt(z_b - z),
    dz = -2 s ds, whose integrand 2 s/E is smooth up to s = 0."""
    z = np.concatenate([[0.0], np.asarray(z_grid, dtype=float)])
    if z_bounce is None:
        left, right = z[:-1], z[1:]
        half, mid = 0.5 * (right - left), 0.5 * (right + left)
        pts = mid[:, None] + half[:, None] * GL_NODES[None, :]
        panel = half * ((1.0 / np.sqrt(e2(pts))) @ GL_WEIGHTS)
    else:
        s = np.sqrt(np.maximum(z_bounce - z, 0.0))
        left, right = s[:-1], s[1:]
        half, mid = 0.5 * (right - left), 0.5 * (right + left)
        pts = mid[:, None] + half[:, None] * GL_NODES[None, :]
        integrand = -2.0 * pts / np.sqrt(e2(z_bounce - pts * pts))
        panel = half * (integrand @ GL_WEIGHTS)
    return np.cumsum(panel)


def distance_modulus(e2, z_grid, z_bounce=None):
    z = np.asarray(z_grid, dtype=float)
    return 5.0 * np.log10((1.0 + z) * comoving_distance(e2, z, z_bounce))


def z_fit_grid(z_max=Z_FIT_MAX):
    count = int(round((Z_FIT_MAX - Z_FIT_MIN) / Z_FIT_STEP))
    grid = Z_FIT_MIN + Z_FIT_STEP * np.arange(count + 1)
    if z_max < Z_FIT_MAX:
        grid = np.concatenate([grid[grid < z_max], [z_max]])
    return grid


# ---------------------------------------------------------------- Nelder-Mead

def nelder_mead(f, start, step, xatol=1e-11, fatol=1e-14, max_iter=20000):
    """Standard Nelder-Mead (reflection 1, expansion 2, contraction 1/2, shrink 1/2)."""
    dim = len(start)
    simplex = [np.array(start, dtype=float)]
    for i in range(dim):
        vertex = np.array(start, dtype=float)
        vertex[i] += step
        simplex.append(vertex)
    values = [f(x) for x in simplex]
    iterations = 0
    while iterations < max_iter:
        order = sorted(range(dim + 1), key=lambda i: (values[i], i))
        simplex = [simplex[i] for i in order]
        values = [values[i] for i in order]
        spread_f = max(abs(v - values[0]) for v in values[1:])
        spread_x = max(float(np.max(np.abs(x - simplex[0]))) for x in simplex[1:])
        if (spread_x <= xatol and spread_f <= fatol * (1.0 + abs(values[0]))) or spread_x <= 1e-15:
            break
        iterations += 1
        centroid = np.mean(simplex[:-1], axis=0)
        worst = simplex[-1]
        xr = centroid + (centroid - worst)
        fr = f(xr)
        if values[0] <= fr < values[-2]:
            simplex[-1], values[-1] = xr, fr
            continue
        if fr < values[0]:
            xe = centroid + 2.0 * (centroid - worst)
            fe = f(xe)
            simplex[-1], values[-1] = (xe, fe) if fe < fr else (xr, fr)
            continue
        if fr < values[-1]:
            xc = centroid + 0.5 * (xr - centroid)
            fc = f(xc)
            if fc <= fr:
                simplex[-1], values[-1] = xc, fc
                continue
        else:
            xc = centroid + 0.5 * (worst - centroid)
            fc = f(xc)
            if fc < values[-1]:
                simplex[-1], values[-1] = xc, fc
                continue
        best = simplex[0]
        simplex = [best] + [best + 0.5 * (x - best) for x in simplex[1:]]
        values = [values[0]] + [f(x) for x in simplex[1:]]
    return simplex[0], values[0], iterations


def minimise(f, start, step):
    """Nelder-Mead followed by one restart from the optimum (standard safeguard)."""
    x, value, it1 = nelder_mead(f, start, step)
    x, value, it2 = nelder_mead(f, x, step / 10.0)
    return x, value, it1 + it2


def mu_fit(target_mu, z, family, offset_profiled):
    """Least-squares fit of the CPL ('cpl') or constant-w ('wconst') mu(z) to target_mu."""
    def residual(theta):
        model = CPL(theta[0], theta[1] if family == "cpl" else 0.0)
        r = distance_modulus(model.e2, z) - target_mu
        return r - np.mean(r) if offset_profiled else r

    def chi2(theta):
        r = residual(theta)
        return float(r @ r)

    start = [-1.0, 0.0] if family == "cpl" else [-1.0]
    theta, value, iterations = minimise(chi2, start, 0.1)
    model = CPL(theta[0], theta[1] if family == "cpl" else 0.0)
    raw = distance_modulus(model.e2, z) - target_mu
    result = {"w0": float(theta[0])} if family == "cpl" else {"w": float(theta[0])}
    if family == "cpl":
        result["wa"] = float(theta[1])
    result["offset"] = float(-np.mean(raw)) if offset_profiled else 0.0
    result["rmsResidualMag"] = math.sqrt(value / len(z))
    result["maxAbsResidualMag"] = float(np.max(np.abs(residual(theta))))
    result["iterations"] = iterations
    return result


def mu_fit_free_omega(target_mu, z, offset_profiled):
    """Least-squares fit of flat wCDM with (w, Omega_m) both free to target_mu."""
    def residual(theta):
        r = distance_modulus(WCDMFreeOmegaM(theta[0], theta[1]).e2, z) - target_mu
        return r - np.mean(r) if offset_profiled else r

    def chi2(theta):
        if not 0.0 < theta[1] < 1.0 - OMEGA_R:
            return 1.0e30
        r = residual(theta)
        return float(r @ r)

    theta, value, iterations = minimise(chi2, [-1.0, OMEGA_M], 0.1)
    raw = distance_modulus(WCDMFreeOmegaM(theta[0], theta[1]).e2, z) - target_mu
    return {"w": float(theta[0]), "OmegaM": float(theta[1]),
            "offset": float(-np.mean(raw)) if offset_profiled else 0.0,
            "rmsResidualMag": math.sqrt(value / len(z)),
            "maxAbsResidualMag": float(np.max(np.abs(residual(theta)))),
            "iterations": iterations}


def w_fit(w_func, a_lo, a_hi=1.0):
    """Linear least squares of w0 + wa (1 - a) to w(a) on a uniform a grid."""
    a = np.linspace(a_lo, a_hi, A_FIT_POINTS)
    design = np.stack([np.ones_like(a), 1.0 - a], axis=1)
    target = w_func(a)
    coefficients, *_ = np.linalg.lstsq(design, target, rcond=None)
    residual = design @ coefficients - target
    return {"w0": float(coefficients[0]), "wa": float(coefficients[1]),
            "rmsResidual": float(math.sqrt(np.mean(residual ** 2))),
            "maxAbsResidual": float(np.max(np.abs(residual)))}


def w_fit_nm(w_func, a_lo, a_hi=1.0):
    a = np.linspace(a_lo, a_hi, A_FIT_POINTS)
    target = w_func(a)
    theta, _, _ = minimise(lambda t: float(np.sum((t[0] + t[1] * (1.0 - a) - target) ** 2)),
                           [-1.0, 0.0], 0.1)
    return float(theta[0]), float(theta[1])


def z_of(a):
    return None if a is None else 1.0 / a - 1.0


# ---------------------------------------------------------------- analysis blocks

def model_block(x0, n=3.0, with_mu=True):
    model = Dirac16(x0, n)
    w0, wa = model.tangent()
    a0, ac, ab = model.a_zero(), model.a_cross(), model.bounce()
    block = {
        "x0": x0, "n": n, "amplitudeA": model.amp,
        "tangentCPL": {"w0": w0, "wa": wa},
        "aZero": a0, "zZero": z_of(a0), "aPhantomCrossing": ac, "zPhantomCrossing": z_of(ac),
        "aBounce": ab, "zBounce": z_of(ab), "q0": model.q0(), "cs2Today": model.cs2_today(),
    }
    pole_in_range = a0 is not None and a0 >= A_FIT_MIN
    bounce_in_range = ab is not None and ab >= A_FIT_MIN
    if pole_in_range:
        block["wFitRequested"] = {
            "range": [A_FIT_MIN, 1.0], "status": "undefined",
            "reason": "w(a) has a pole at a = |x0|^(1/n) = %.6f inside [1/3.26, 1] (rho_psi = 0); "
                      "the least-squares integral diverges" % a0}
    else:
        fit = w_fit(model.w, A_FIT_MIN)
        block["wFitRequested"] = dict({"range": [A_FIT_MIN, 1.0], "status": "ok"}, **fit)
    a_floor = model.a_w(W_FLOOR)
    a_lo = A_FIT_MIN if a_floor is None else max(A_FIT_MIN, a_floor)
    fit = w_fit(model.w, a_lo)
    block["wFitRestricted"] = dict({
        "range": [a_lo, 1.0],
        "rule": "a >= max(1/3.26, a(w = -3)), a(w = -3) = (4|x0|/3)^(1/n): pole-avoiding truncation "
                "(supplementary, not the contract's fit)"}, **fit)
    if not with_mu:
        return block, None
    if bounce_in_range:
        block["muFitRequested"] = {
            "range": [Z_FIT_MIN, Z_FIT_MAX], "status": "undefined",
            "reason": "E^2 = 0 at the bounce z_b = %.6f < 2.26: the model has no redshift beyond z_b "
                      "(a >= a_b)" % z_of(ab)}
    else:
        z = z_fit_grid()
        target = distance_modulus(model.e2, z)
        block["muFitRequested"] = {"range": [Z_FIT_MIN, Z_FIT_MAX], "status": "ok",
                                   "cplOffsetProfiled": mu_fit(target, z, "cpl", True),
                                   "wConstantOffsetProfiled": mu_fit(target, z, "wconst", True),
                                   "cplOffsetZero": mu_fit(target, z, "cpl", False),
                                   "wConstantOffsetZero": mu_fit(target, z, "wconst", False)}
    z_max = Z_FIT_MAX if not bounce_in_range else z_of(ab)
    z = z_fit_grid(z_max)
    target = distance_modulus(model.e2, z, z_of(ab) if bounce_in_range else None)
    block["muFitRestricted"] = {
        "range": [Z_FIT_MIN, z_max],
        "rule": "z in [0.01, min(2.26, z_b)] (supplementary when z_b < 2.26)",
        "points": int(len(z)),
        "cplOffsetProfiled": mu_fit(target, z, "cpl", True),
        "wConstantOffsetProfiled": mu_fit(target, z, "wconst", True),
    }
    unite = distance_modulus(CPL(UNITE_W0, UNITE_WA).e2, z)
    diff = target - unite
    block["muVsUniteCPL"] = {"range": [Z_FIT_MIN, z_max],
                             "maxAbsDifferenceMag": float(np.max(np.abs(diff))),
                             "maxAbsDifferenceOffsetProfiledMag": float(np.max(np.abs(diff - np.mean(diff))))}
    return block, (z, target)


def gamma_variant():
    x0 = UNITE_W0 / (1.0 - UNITE_W0)
    n = UNITE_WA * (1.0 + x0) ** 2 / x0
    gamma = 1.0 - n / 3.0
    block, _ = model_block(x0, n)
    model = Dirac16(x0, n)
    w0e, wae = model.tangent_eff()
    fit_eff = w_fit(model.w_eff, A_FIT_MIN)
    constraint = 1.0 - 3.0 * gamma + gamma * gamma
    gdot = 3.0 * gamma
    continuity_today = (3.0 - n) * model.amp * (1.0 + 2.0 * x0)
    return {
        "definition": "c ~ a^-gamma (b static) => V ~ a^{3(1-gamma)}, sigma = a^{-n}, n = 3(1 - gamma); "
                      "x0 from w0 = x0/(1+x0), n from wa = n x0/(1+x0)^2",
        "x0": x0, "n": n, "gamma": gamma,
        "tangentCPLofPressureRatio": block["tangentCPL"],
        "tangentCPLofEffectiveW": {"w0": w0e, "wa": wae},
        "effectiveWFitRequested": dict({"range": [A_FIT_MIN, 1.0]}, **fit_eff),
        "model": block,
        "objections": [
            {"id": "continuity",
             "statement": "For n != 3 the condensate does not obey the 4D continuity equation: "
                          "drho/dN + 3(rho + p) = (3 - n) A sigma (1 + 2 x0 sigma) != 0, i.e. energy "
                          "is exchanged with the extra dimensions. Distances measure w_eff = "
                          "-1 - (1/3) dln rho/dln a, not p/rho, so the model reproduces the Unite "
                          "tangent only for w = p/rho; its distance-inferred tangent is "
                          "(w0, wa)_eff = (%.4f, %.4f)." % (w0e, wae),
             "value": continuity_today,
             "valueMeaning": "drho/dN + 3(rho + p) at a = 1 in units of 3 H0^2/kappa_4"},
            {"id": "newtonConstant",
             "statement": "G_N = G_8 / V_extra with V_extra = b c^3 ~ a^{-3 gamma}: G_N ~ a^{3 gamma}, "
                          "Gdot/G = 3 gamma H0 today (%.3f H0, about %.1e per yr for H0 = 67.4 km/s/Mpc) "
                          "versus lunar-laser-ranging bounds of order 1e-13 per yr; G_N(z)/G_N(0) = "
                          "(1+z)^{-3 gamma} = %.3f at z = 1. The 4D Friedmann equation with a constant "
                          "G_N used here is itself inconsistent with this variation."
                          % (gdot, gdot * H0_PER_YEAR, 2.0 ** (-3.0 * gamma)),
             "value": gdot, "valueMeaning": "Gdot/G in units of H0",
             "gdotPerYear": gdot * H0_PER_YEAR, "llrBoundPerYearOrderOfMagnitude": LLR_GDOT_BOUND,
             "ratioToBound": gdot * H0_PER_YEAR / LLR_GDOT_BOUND},
            {"id": "einstein8D",
             "statement": "8D Hamiltonian constraint (EXP-2): sum_{i<j} H_i H_j = kappa rho_8 with H_b = 0, "
                          "H_c = -gamma H_a gives kappa rho_8 = 3 H_a^2 (1 - 3 gamma + gamma^2) = %.4f H_a^2 < 0 "
                          "for gamma = %.4f: a sustained deflation with gamma in ((3 - sqrt 5)/2, (3 + sqrt 5)/2) "
                          "= (0.382, 2.618) needs a negative total 8D energy density (equivalently it violates "
                          "Theta^2 - 3 H_a^2 - 2 kappa rho >= 0 with rho >= 0), and the EXP-2 dynamics has no "
                          "mechanism that keeps the extra times deflating." % (3.0 * constraint, gamma),
             "value": 3.0 * constraint, "valueMeaning": "kappa rho_8 / H_a^2"},
        ],
    }


def unite_block():
    z = z_fit_grid()
    target = distance_modulus(CPL(UNITE_W0, UNITE_WA).e2, z)
    projection = mu_fit(target, z, "wconst", True)
    projection_zero = mu_fit(target, z, "wconst", False)
    self_fit = mu_fit(target, z, "cpl", True)
    z_log = np.exp(np.linspace(math.log(Z_FIT_MIN), math.log(Z_FIT_MAX), len(z)))
    target_log = distance_modulus(CPL(UNITE_W0, UNITE_WA).e2, z_log)
    projection_log = mu_fit(target_log, z_log, "wconst", True)
    free = mu_fit_free_omega(target, z, True)
    free_zero = mu_fit_free_omega(target, z, False)
    free_log = mu_fit_free_omega(target_log, z_log, True)
    return {
        "w0": UNITE_W0, "wa": UNITE_WA, "wConstantBenchmark": UNITE_WCONST,
        "w0PlusWa": UNITE_W0 + UNITE_WA,
        "phantomCrossingA": 1.0 - (-1.0 - UNITE_W0) / UNITE_WA,
        "constantWProjectionOffsetProfiled": projection,
        "constantWProjectionOffsetZero": projection_zero,
        "projectionMinusBenchmark": projection["w"] - UNITE_WCONST,
        "constantWProjectionLogGridOffsetProfiled": dict(
            {"grid": "uniform in ln z on [0.01, 2.26], same point count (weights low z like a "
                     "supernova sample)"}, **projection_log),
        "projectionLogGridMinusBenchmark": projection_log["w"] - UNITE_WCONST,
        "selfFitCPL": self_fit,
        "constantWProjectionOmegaMFreeOffsetProfiled": free,
        "constantWProjectionOmegaMFreeOffsetZero": free_zero,
        "constantWProjectionOmegaMFreeLogGridOffsetProfiled": dict(
            {"grid": "uniform in ln z on [0.01, 2.26], same point count"}, **free_log),
        "projectionOmegaMFreeMinusBenchmark": free["w"] - UNITE_WCONST,
        "projectionOmegaMFreeLogGridMinusBenchmark": free_log["w"] - UNITE_WCONST,
        "omegaMAssumption": "Omega_m = 0.305 is an input of the numerical programme (EXP-3); the "
                            "reference PDF gives no Omega_m, and the Omega_m of the Unite fits is not "
                            "known here. The Unite CPL distances (the target) always use Omega_m = "
                            "0.305; the constantWProjection* fits hold Omega_m at 0.305, the "
                            "constantWProjectionOmegaMFree* fits let it vary (flat wCDM).",
        "note": "The -0.764 benchmark is a direct constant-w fit to the Unite supernovae (Omega_m not "
                "fixed, likelihood with the real errors), not a projection of the CPL posterior; the "
                "projections here use the CPL best fit as noise-free data with equal weights. With "
                "Omega_m fixed at the assumed 0.305 the best constant w is far from -0.764; with "
                "Omega_m free (the w - Omega_m degeneracy) it moves most of the way towards it. The "
                "remaining difference cannot be judged without the Unite likelihood.",
    }, (z, target)


def fine_scan():
    rows = []
    for k in range(-490, 1, SCAN_STEP_MILLI):
        x0 = k / 1000.0
        block, _ = model_block(x0, with_mu=False)
        req = block["wFitRequested"]
        res = block["wFitRestricted"]
        rows.append([x0, block["tangentCPL"]["w0"], block["tangentCPL"]["wa"],
                     nan(block["aZero"]), nan(block["zZero"]),
                     nan(block["aPhantomCrossing"]), nan(block["zPhantomCrossing"]),
                     nan(block["aBounce"]), nan(block["zBounce"]), block["q0"], block["cs2Today"],
                     1.0 if req["status"] == "ok" else 0.0,
                     req.get("w0", float("nan")), req.get("wa", float("nan")),
                     res["range"][0], res["w0"], res["wa"]])
    header = ["x0", "w0_tangent", "wa_tangent", "a_zero", "z_zero", "a_cross", "z_cross",
              "a_bounce", "z_bounce", "q0", "cs2_today", "wfit_requested_defined",
              "wfit_requested_w0", "wfit_requested_wa", "wfit_restricted_a_lo",
              "wfit_restricted_w0", "wfit_restricted_wa"]
    return header, rows


def mu_scan():
    rows = []
    for k in range(-49, 1, MU_SCAN_STEP_CENTI):
        x0 = k / 100.0
        block, _ = model_block(x0)
        req = block["muFitRequested"]
        res = block["muFitRestricted"]
        cpl = res["cplOffsetProfiled"]
        wc = res["wConstantOffsetProfiled"]
        ok = req["status"] == "ok"
        rows.append([x0, res["range"][1], cpl["w0"], cpl["wa"], cpl["rmsResidualMag"], wc["w"],
                     wc["rmsResidualMag"], 1.0 if ok else 0.0,
                     req["cplOffsetProfiled"]["w0"] if ok else float("nan"),
                     req["cplOffsetProfiled"]["wa"] if ok else float("nan"),
                     req["wConstantOffsetProfiled"]["w"] if ok else float("nan")])
    header = ["x0", "z_max_restricted", "cpl_w0", "cpl_wa", "cpl_rms_mag", "wconst", "wconst_rms_mag",
              "requested_defined", "requested_cpl_w0", "requested_cpl_wa", "requested_wconst"]
    return header, rows


def critical_x0_bounce(a_target):
    """x0 < 0 whose bounce is exactly at a_target: (Omega_m + A) a^3 + Omega_r a^2 + A x0 = 0."""
    def f(x0):
        amp = OMEGA_PSI / (1.0 + x0)
        return (OMEGA_M + amp) * a_target ** 3 + OMEGA_R * a_target ** 2 + amp * x0
    lo, hi = -0.49, -1e-12          # f(lo) < 0 < f(hi)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid <= lo or mid >= hi:
            break
        if f(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def nan(value):
    return float("nan") if value is None else value


# ---------------------------------------------------------------- output

def fmt(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    value = float(value)
    if not math.isfinite(value):
        return "null"
    return "%.17e" % (value + 0.0)


def to_json(value, depth=0):
    pad, inner = "  " * depth, "  " * (depth + 1)
    if value is None:
        return "null"
    if isinstance(value, (bool, np.bool_)):
        return "true" if value else "false"
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        return fmt(float(value))
    if isinstance(value, str):
        text = value.replace("\\", "\\\\").replace('"', '\\"')
        return '"' + "".join(c if 0x20 <= ord(c) <= 0x7e else "\\u%04x" % ord(c) for c in text) + '"'
    if isinstance(value, dict):
        if not value:
            return "{}"
        items = [inner + to_json(k) + ": " + to_json(v, depth + 1) for k, v in value.items()]
        return "{\n" + ",\n".join(items) + "\n" + pad + "}"
    if isinstance(value, (list, tuple)):
        if not value:
            return "[]"
        items = [inner + to_json(v, depth + 1) for v in value]
        return "[\n" + ",\n".join(items) + "\n" + pad + "]"
    raise TypeError(type(value))


def write_csv(path, header, rows):
    lines = [",".join(header)]
    for row in rows:
        lines.append(",".join("nan" if not math.isfinite(v) else "%.17e" % (v + 0.0) for v in row))
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(lines) + "\n")


def curve(values):
    return [None if not math.isfinite(v) else float(v) for v in values]


def rust_distance_crosscheck(directory):
    """Max |D_C(CVODE) - D_C(quadrature)| over the backward rows of every Rust run."""
    import json
    with open(os.path.join(directory, "summary.json"), "r", encoding="utf-8") as handle:
        summary = json.load(handle)
    worst = 0.0
    for run in summary["runs"]:
        data = np.loadtxt(os.path.join(directory, run["file"]), delimiter=",", skiprows=1, ndmin=2)
        past = data[:, 3] < 0.0
        z = data[past, 2][::-1]
        dc = data[past, 5][::-1]
        model = Dirac16(run["x0"])
        ab = model.bounce()
        reference = comoving_distance(model.e2, z, z_of(ab))
        worst = max(worst, float(np.max(np.abs(dc - reference))))
    return worst


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", default=DEFAULT_ROOT)
    arguments = parser.parse_args(argv)
    directory = os.path.join(os.path.abspath(arguments.output), EXPERIMENT)
    if not os.path.exists(os.path.join(directory, "summary.json")):
        print("missing %s/summary.json: run the exp3 subcommand first" % directory)
        return 1
    checks, measurements = {}, {}

    # --- validations of the machinery
    z = z_fit_grid()
    synthetic = distance_modulus(CPL(-0.9, -0.3).e2, z) + 0.123
    recovered = mu_fit(synthetic, z, "cpl", True)
    measurements["nmSyntheticCplError"] = max(abs(recovered["w0"] + 0.9), abs(recovered["wa"] + 0.3),
                                              abs(recovered["offset"] - 0.123))
    checks["nelderMeadRecoversSyntheticCPL"] = measurements["nmSyntheticCplError"] <= 1e-6
    wc_target = distance_modulus(CPL(UNITE_WCONST, 0.0).e2, z)
    wc = mu_fit(wc_target, z, "wconst", True)
    measurements["nmSyntheticWconstError"] = abs(wc["w"] - UNITE_WCONST)
    checks["nelderMeadRecoversSyntheticWconst"] = measurements["nmSyntheticWconstError"] <= 1e-7
    free_target = distance_modulus(WCDMFreeOmegaM(-0.8, 0.28).e2, z) + 0.05
    free_fit = mu_fit_free_omega(free_target, z, True)
    measurements["nmSyntheticWcdmFreeOmegaMError"] = max(abs(free_fit["w"] + 0.8),
                                                         abs(free_fit["OmegaM"] - 0.28),
                                                         abs(free_fit["offset"] - 0.05))
    same_family = max(abs(WCDMFreeOmegaM(UNITE_WCONST, OMEGA_M).e2(zz_) - CPL(UNITE_WCONST, 0.0).e2(zz_))
                      for zz_ in (0.0, 0.5, 1.0, 2.26))
    checks["nelderMeadRecoversSyntheticWcdmFreeOmegaM"] = (
        measurements["nmSyntheticWcdmFreeOmegaMError"] <= 1e-6 and same_family <= 1e-12)
    dust = Dirac16(0.0)
    zz = np.linspace(0.0, 3.0, 31)
    measurements["dustEqualsWcdm0"] = float(np.max(np.abs(dust.e2(zz) - CPL(0.0, 0.0).e2(zz))))
    checks["dustModelIsWcdmZero"] = measurements["dustEqualsWcdm0"] <= 1e-12
    # quadrature: EdS-like closed form without radiation, D_C = 2 (1 - 1/sqrt(1+z)) / sqrt(Om_tot)
    eds = lambda zv: (1.0 + zv) ** 3
    exact = 2.0 * (1.0 - 1.0 / np.sqrt(1.0 + z))
    measurements["quadratureVsEdS"] = float(np.max(np.abs(comoving_distance(eds, z) - exact)))
    checks["quadratureExactEdS"] = measurements["quadratureVsEdS"] <= 1e-13
    # linear w(a) fit vs Nelder-Mead on a defined case (the Unite CPL itself and the gamma variant)
    gv = gamma_variant()
    model_g = Dirac16(gv["x0"], gv["n"])
    lin = w_fit(model_g.w, A_FIT_MIN)
    nm = w_fit_nm(model_g.w, A_FIT_MIN)
    measurements["wFitLinearVsNM"] = max(abs(lin["w0"] - nm[0]), abs(lin["wa"] - nm[1]))
    checks["wFitLinearMatchesNelderMead"] = measurements["wFitLinearVsNM"] <= 1e-6
    self_cpl = w_fit(CPL(UNITE_W0, UNITE_WA).w, A_FIT_MIN)
    measurements["wFitCplSelf"] = max(abs(self_cpl["w0"] - UNITE_W0), abs(self_cpl["wa"] - UNITE_WA))
    checks["wFitRecoversCPL"] = measurements["wFitCplSelf"] <= 1e-12
    measurements["gammaTangentVsUnite"] = max(abs(gv["tangentCPLofPressureRatio"]["w0"] - UNITE_W0),
                                              abs(gv["tangentCPLofPressureRatio"]["wa"] - UNITE_WA))
    checks["gammaVariantReproducesUniteTangent"] = measurements["gammaTangentVsUnite"] <= 1e-12
    # bounce: scan/bisection vs the cubic for n = 3
    worst = 0.0
    for x0 in X0_CANONICAL[:4]:
        m = Dirac16(x0)
        roots = np.roots([OMEGA_M + m.amp, OMEGA_R, 0.0, m.amp * x0])
        cubic = [r.real for r in roots if abs(r.imag) < 1e-12 and 0.0 < r.real < 1.0][0]
        worst = max(worst, abs(m.bounce() - cubic))
    measurements["bounceScanVsCubic"] = worst
    checks["bounceScanMatchesCubic"] = worst <= 1e-12
    measurements["rustDistanceVsQuadrature"] = rust_distance_crosscheck(directory)
    checks["rustDistanceMatchesQuadrature"] = measurements["rustDistanceVsQuadrature"] <= 1e-8

    # --- canonical models
    unite, (z_unite, mu_unite) = unite_block()
    models = []
    curves_z = np.round(0.02 * np.arange(1, 114), 12)
    curves = {"z": [float(v) for v in curves_z],
              "muUniteCPL": curve(distance_modulus(CPL(UNITE_W0, UNITE_WA).e2, curves_z)),
              "muUniteConstantWProjection": curve(distance_modulus(
                  CPL(unite["constantWProjectionOffsetProfiled"]["w"], 0.0).e2, curves_z)),
              "muLCDM": curve(distance_modulus(CPL(-1.0, 0.0).e2, curves_z)),
              "muModel": {}}
    a_curve = np.round(np.linspace(A_FIT_MIN, 1.0, 101), 15)
    curves["a"] = [float(v) for v in a_curve]
    curves["wUniteCPL"] = curve(CPL(UNITE_W0, UNITE_WA).w(a_curve))
    curves["wModel"] = {}
    curves["note"] = ("muModel is null for z >= z_b (no such redshift in a bouncing model); wModel is null "
                      "for a <= |x0|^(1/3) (pole of w where rho_psi = 0; below it rho_psi < 0).")
    for x0 in X0_CANONICAL:
        block, _ = model_block(x0)
        dw0 = block["tangentCPL"]["w0"] - UNITE_W0
        dwa = block["tangentCPL"]["wa"] - UNITE_WA
        block["tangentMinusUnite"] = {"w0": dw0, "wa": dwa}
        models.append(block)
        m = Dirac16(x0)
        ab = m.bounce()
        zb = z_of(ab)
        inside = curves_z < zb if zb is not None else np.ones_like(curves_z, dtype=bool)
        values = np.full(len(curves_z), np.nan)
        if np.any(inside):
            values[inside] = distance_modulus(m.e2, curves_z[inside], zb)
        curves["muModel"]["x0=%r" % x0] = curve(values)
        a0 = m.a_zero()
        wv = m.w(a_curve)
        if a0 is not None:
            wv = np.where(a_curve > a0, wv, np.nan)
        curves["wModel"]["x0=%r" % x0] = curve(wv)

    header, rows = fine_scan()
    write_csv(os.path.join(directory, "fits_scan.csv"), header, rows)
    mu_header, mu_rows = mu_scan()
    write_csv(os.path.join(directory, "fits_mu_scan.csv"), mu_header, mu_rows)
    scan = np.array(rows)
    defined = scan[:, 11] == 1.0
    mu_defined = np.array(mu_rows)[:, 7] == 1.0
    scan_summary = {
        "file": "fits_scan.csv", "columns": header, "x0Min": -0.49, "x0Max": 0.0, "step": 0.001,
        "count": len(rows),
        "wFitRequestedDefinedFor": "x0 > -(1/3.26)^3 = %.6f (pole a = |x0|^(1/3) below 1/3.26)"
                                   % (-(A_FIT_MIN ** 3)),
        "mostNegativeX0WithRequestedWFit": float(np.min(scan[defined, 0])),
        "mostNegativeX0WithoutBounceBelowZ226": float(np.min(np.array(mu_rows)[mu_defined, 0])),
        "muScanFile": "fits_mu_scan.csv", "muScanColumns": mu_header, "muScanStep": 0.01,
        "x0CriticalWFit": -(A_FIT_MIN ** 3),
        "x0CriticalWFitMeaning": "for x0 < -(1/3.26)^3 the pole a = |x0|^(1/3) lies in [1/3.26, 1]",
        "x0CriticalMuFit": critical_x0_bounce(A_FIT_MIN),
        "x0CriticalMuFitMeaning": "for x0 below this value the bounce lies at z_b < 2.26 (a_b > 1/3.26)",
        "tangentWaAtUniteW0": Dirac16(UNITE_W0 / (1.0 - UNITE_W0)).tangent()[1],
        "x0ForUniteW0": UNITE_W0 / (1.0 - UNITE_W0),
        "x0ForConstantW0764": UNITE_WCONST / (1.0 - UNITE_WCONST),
    }

    checks = {name: bool(value) for name, value in checks.items()}
    measurements = {name: float(value) for name, value in measurements.items()}
    failed = [k for k, v in checks.items() if not v]
    document = {
        "schemaVersion": 1,
        "producer": "scripts/analyze_dirac16complex_exp3.py",
        "experiment": EXPERIMENT,
        "conventions": {
            "units": "H0 = c = 1; D_C in units of c/H0; densities in units of 3 H0^2/kappa_4",
            "cpl": "w(a) = w0 + wa (1 - a), wa = -dw/da",
            "fixed": {"OmegaR": OMEGA_R, "OmegaM": OMEGA_M, "OmegaPsi": OMEGA_PSI, "OmegaDE": OMEGA_DE,
                      "flat": True},
            "distanceModulus": "mu = 5 log10((1+z) D_C) + const; offsetProfiled: const fitted "
                               "analytically (H0 and absolute magnitude free); offsetZero: const = 0",
            "wFit": {"range": [A_FIT_MIN, 1.0], "grid": "uniform in a", "points": A_FIT_POINTS,
                     "method": "linear least squares, equal weights"},
            "muFit": {"range": [Z_FIT_MIN, Z_FIT_MAX], "grid": "uniform in z", "step": Z_FIT_STEP,
                      "points": int(len(z_unite)), "method": "Nelder-Mead (numpy), equal weights, "
                      "restart from the optimum; D_C by 8-point Gauss-Legendre per grid panel"},
            "restricted": "Supplementary fits over the largest sub-range on which the model is defined "
                          "(w >= -3 for w(a); z < z_b for mu(z)); they are not the contract's fits.",
        },
        "unite": unite,
        "models": models,
        "gammaVariant": gv,
        "scan": scan_summary,
        "curves": curves,
        "validation": {"checks": checks, "measurements": measurements},
        "verdict": "SUCCESS" if not failed else "FAILURE",
    }
    with open(os.path.join(directory, "fits.json"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(to_json(document) + "\n")
    for name, value in checks.items():
        print("check_%s=%s" % (name, "true" if value else "false"))
    for name, value in measurements.items():
        print("measurement_%s=%r" % (name, value))
    print("measurement_uniteConstantWProjection=%r" % unite["constantWProjectionOffsetProfiled"]["w"])
    for block in models:
        print("model x0=%r tangent (w0, wa) = (%.6f, %.6f), zBounce = %s, wFitRequested = %s, "
              "muFitRequested = %s" % (block["x0"], block["tangentCPL"]["w0"], block["tangentCPL"]["wa"],
                                       block["zBounce"], block["wFitRequested"]["status"],
                                       block["muFitRequested"]["status"]))
    print("gamma variant: gamma = %.6f, n = %.6f, effective tangent = (%.6f, %.6f)"
          % (gv["gamma"], gv["n"], gv["tangentCPLofEffectiveW"]["w0"], gv["tangentCPLofEffectiveW"]["wa"]))
    print("check_count=%d" % len(checks))
    print("failed_check_count=%d" % len(failed))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
