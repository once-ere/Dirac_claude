"""Revision/universe_model/solution/masses.py - the x0 mass spectrum of UM-1 (FIELD_EQUATIONS.md part D), numerically,
and its fit to the observed masses.

Gauge fields: on each half of the cell, t = y/L in [-1, 0], the operator -(e^{-3 eta t} (e^{3 eta t} u')') = Lambda u with
eta = H L and Lambda = (m l)^2, l = f L the proper length of a half; fold u'(0) = 0; tip u'(-1) = beta u(-1)
(beta = c g^2 v_Sigma^2 f L, i.e. beta proportional to f, from matching the bulk gauge term to the tip mass term of the
sigma field, ANALYSIS.md section 3.3; beta = 0 for unbroken generators).
Exact Neumann spectrum (u = e^{-3 eta t/2} w): Lambda_0 = 0, Lambda_n = 9 eta^2/4 + n^2 pi^2 (n >= 1).
Solved by shooting (RK4, 4000 steps) and bisection.  Fermions: the chiral zero modes chi = e^{c t} (c = f mu L) with the
normalised tip value zeta(c)^2 = 2c e^{-2c}/(1 - e^{-2c}); the Dirac mass m_f = lam m_KK zeta(c_L) zeta(c_R)
(lam = 1 here, c_L = c_R = c_f).

Every profile is a function of y = ln|sin z|/(6H), z = 6 H x0, which is periodic in x0 with the period pi/(6H)
(|sin(z + pi)| = |sin z|): the masses are those of x0-periodic wave functions (checked in fit())."""
import math

import numpy as np

NSTEP = 4000
HBARC_GEV_M = 1.973269804e-16        # hbar c in GeV m (CODATA)
OBS = {                               # PDG 2024 central values (GeV); m_nu: one generation, chosen sqrt(dm^2_atm)
    "W": 80.3692, "Z": 91.1880, "e": 0.51099895e-3, "u": 2.16e-3, "d": 4.70e-3, "nu": 0.05e-9,
    "sin2_thetaW_MSbar": 0.23122, "rho0_minus_1": 0.00038, "rho0_sigma": 0.00020,
}


def shoot(lam, eta, n=NSTEP, profile=False):
    """integrate (e^{3 eta t} u')' = -lam e^{3 eta t} u from t = 0 (u = 1, u' = 0) to t = -1; return
    (u(-1), u'(-1)) and, if asked, the profile u on t = 0, -1/n, ..., -1"""
    h = -1.0 / n
    t, u, p = 0.0, 1.0, 0.0                 # p = e^{3 eta t} u'

    def rhs(t, u, p):
        return p * math.exp(-3.0 * eta * t), -lam * math.exp(3.0 * eta * t) * u
    us = [u] if profile else None
    for _ in range(n):
        k1 = rhs(t, u, p)
        k2 = rhs(t + h / 2, u + h / 2 * k1[0], p + h / 2 * k1[1])
        k3 = rhs(t + h / 2, u + h / 2 * k2[0], p + h / 2 * k2[1])
        k4 = rhs(t + h, u + h * k3[0], p + h * k3[1])
        u += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        p += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        t += h
        if profile:
            us.append(u)
    du = p * math.exp(3.0 * eta)            # u'(-1)
    return u, du, (np.array(us) if profile else None)


def mismatch(lam, eta, beta):
    u, du, _ = shoot(lam, eta)
    return du - beta * u


def neumann_exact(eta, n):
    return 0.0 if n == 0 else 9.0 * eta ** 2 / 4.0 + (n * math.pi) ** 2


def eigenvalues(eta, beta, nmax=3, lam_max=400.0, ngrid=800):
    """the lowest nmax eigenvalues Lambda >= 0 (bracketing on a grid, then bisection)"""
    grid = np.linspace(0.0, lam_max, ngrid)
    vals = [mismatch(l, eta, beta) for l in grid]
    out = []
    if abs(vals[0]) < 1e-14:
        out.append(0.0)
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            out.append(bisect(eta, beta, grid[i], grid[i + 1], vals[i]))
        if len(out) >= nmax:
            break
    return out


def bisect(eta, beta, lo, hi, flo, steps=80):
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        fm = mismatch(mid, eta, beta)
        if fm * flo <= 0:
            hi = mid
        else:
            lo, flo = mid, fm
    return 0.5 * (lo + hi)


def dirichlet_tip_level(eta):
    """the beta -> infinity limit (u(-1) = 0) of the lowest level: w = sinh(q (t + 1)), tanh q = 2q/(3 eta),
    Lambda_D = 9 eta^2/4 - q^2: the largest W mass a POSITIVE tip term can give"""
    lo, hi = 1e-9, 1.5 * eta
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if math.tanh(mid) - 2.0 * mid / (3.0 * eta) > 0:
            lo = mid
        else:
            hi = mid
    q = 0.5 * (lo + hi)
    return 9.0 * eta ** 2 / 4.0 - q * q


def beta_for(eta, lam_target):
    """the tip parameter beta whose lowest eigenvalue is lam_target (0 < lam_target < Lambda_D): one shot from the
    fold, beta = u'(-1)/u(-1); a target at or above Lambda_D needs beta < 0 (an unphysical tip term) and is refused"""
    if lam_target >= dirichlet_tip_level(eta):
        raise ValueError("target above the Dirichlet-tip level: no positive tip term gives it")
    u, du, _ = shoot(lam_target, eta)
    return du / u


def lowest_robin(eta, beta):
    """the lowest eigenvalue for a tip parameter beta > 0 (below the first Neumann level)"""
    hi = neumann_exact(eta, 1) * (1.0 - 1e-9)
    lo = 0.0
    flo = mismatch(lo, eta, beta)
    fhi = mismatch(hi, eta, beta)
    if flo * fhi > 0:
        # scan for the first sign change
        grid = np.linspace(0.0, hi, 200)
        vals = [mismatch(l, eta, beta) for l in grid]
        for i in range(len(grid) - 1):
            if vals[i] * vals[i + 1] < 0:
                return bisect(eta, beta, grid[i], grid[i + 1], vals[i])
        raise RuntimeError("no Robin level below the first Neumann level")
    return bisect(eta, beta, lo, hi, flo)


def rayleigh_split(lam, eta, beta):
    """Lambda = [int e^{3 eta t} u'^2 dt + beta e^{-3 eta} u(-1)^2] / int e^{3 eta t} u^2 dt for the eigenfunction:
    (bulk hidden-momentum part, tip part, their sum)"""
    u0, du0, us = shoot(lam, eta, profile=True)
    t = np.linspace(0.0, -1.0, len(us))
    du = np.gradient(us, t)
    w = np.exp(3.0 * eta * t)
    den = -np.trapezoid(w * us ** 2, t)
    bulk = -np.trapezoid(w * du ** 2, t) / den
    tip = beta * math.exp(-3.0 * eta) * u0 ** 2 / den
    return bulk, tip, bulk + tip


def zeta2(c):
    """normalised tip value of the zero mode e^{c t} on t in [-1, 0]"""
    if abs(c) < 1e-12:
        return 1.0
    return 2.0 * c * math.exp(-2.0 * c) / (-math.expm1(-2.0 * c))


def c_for(ratio):
    """c with zeta2(c) = ratio (0 < ratio < 1), by bisection on c in (0, 200)"""
    lo, hi = 0.0, 200.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if zeta2(mid) > ratio:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def width_t(c, n=200001):
    """standard deviation of t in the zero-mode density e^{2ct} on [-1, 0]"""
    t = np.linspace(-1.0, 0.0, n)
    w = np.exp(2.0 * c * t)
    wsum = np.trapezoid(w, t)
    mean = np.trapezoid(t * w, t) / wsum
    return math.sqrt(np.trapezoid((t - mean) ** 2 * w, t) / wsum)


def width_t_exact(c):
    """closed form of width_t for c > 0: Var t = 1/(4c^2) - e^{-2c}/(4 sinh(c)^2)"""
    return math.sqrt(1.0 / (4.0 * c * c) - math.exp(-2.0 * c) / (4.0 * math.sinh(c) ** 2)) if c > 0 else math.sqrt(1.0 / 12.0)


def delta_rho(eta, m_kk_gev, obs=OBS):
    """the tree-level custodial deviation rho - 1 = m_W^2/(m_Z,pred^2 c^2) - 1 with c^2 = (m_W/m_Z)^2 observed (the
    on-shell angle), beta_W from m_W, beta_Z = beta_W/c^2; returns (rho - 1, beta_W, Lambda_Z, fL)"""
    fl = math.sqrt(neumann_exact(eta, 1)) / m_kk_gev
    c2 = (obs["W"] / obs["Z"]) ** 2
    bW = beta_for(eta, (obs["W"] * fl) ** 2)
    lz = lowest_robin(eta, bW / c2)
    return obs["W"] ** 2 / (lz / fl ** 2 * c2) - 1.0, bW, lz, fl


def fit_mkk(eta, target, obs=OBS):
    """m_KK with delta_rho = target (delta_rho falls like m_KK^-2): bisection in ln m_KK"""
    lo, hi = math.log(obs["W"] / math.sqrt(dirichlet_tip_level(eta) / neumann_exact(eta, 1)) * 1.001), math.log(1e7)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if delta_rho(eta, math.exp(mid), obs)[0] > target:
            lo = mid
        else:
            hi = mid
    return math.exp(0.5 * (lo + hi))


def fit(eta=3.0, f=8.0 ** -0.5, m_kk_gev=None, obs=OBS):
    """fit the spectrum: m_KK (the first Neumann level of the photon/gluon tower) is fitted to the measured
    rho0 - 1 (or given); fL from it; beta_W from m_W; beta_Z = beta_W / cos^2 theta_W (custodial tip, c_tip(Z)/c_tip(W)
    = 1/cos^2, on-shell angle); m_Z and rho predicted; c_f of every fermion from m_f = m_KK zeta(c_f)^2; widths and the
    uncertainty estimate."""
    L1 = neumann_exact(eta, 1)
    LD = dirichlet_tip_level(eta)
    m_kk_min = obs["W"] / math.sqrt(LD / L1)
    fitted = m_kk_gev is None
    if fitted:
        m_kk_gev = fit_mkk(eta, obs["rho0_minus_1"], obs)
    out = {"inputs": {"eta_HL": eta, "f": f, "m_KK_GeV": m_kk_gev, "m_KK_fitted_to_rho0": fitted, "obs": obs},
           "dirichlet_tip": {"Lambda_D": LD, "mW_max_over_mKK": math.sqrt(LD / L1), "m_KK_min_GeV": m_kk_min,
                             "Lambda_D_numeric_beta_1e7": lowest_robin(eta, 1e7)},
           "rho_scan": [{"m_KK_GeV": mk, "rho_minus_1": delta_rho(eta, mk, obs)[0]} for mk in (5e3, 1e4, 3e4, 1e5, 3e5)]}
    num_neu = eigenvalues(eta, 0.0, nmax=3, lam_max=1.2 * neumann_exact(eta, 2), ngrid=600)
    out["neumann"] = {"numeric": num_neu, "exact": [neumann_exact(eta, n) for n in range(3)],
                      "max_rel_dev": max(abs(a - b) / max(1.0, b) for a, b in zip(num_neu, [neumann_exact(eta, n) for n in range(3)]))}
    fl = math.sqrt(L1) / m_kk_gev                         # proper half-cell length l = f L in GeV^-1
    Lc = fl / f                                           # coordinate L (GeV^-1)
    Hphys = eta / Lc                                      # GeV
    out["scales"] = {"fL_GeV^-1": fl, "fL_m": fl * HBARC_GEV_M, "L_GeV^-1": Lc, "H_GeV": Hphys,
                     "x0_period_pi_over_6H_GeV^-1": math.pi / (6.0 * Hphys),
                     "x0_period_m": math.pi / (6.0 * Hphys) * HBARC_GEV_M}
    lamW = (obs["W"] * fl) ** 2
    bW = beta_for(eta, lamW)
    lamW_back = lowest_robin(eta, bW)
    c2 = (obs["W"] / obs["Z"]) ** 2
    bZ = bW / c2
    lamZ = lowest_robin(eta, bZ)
    mZ = math.sqrt(lamZ) / fl
    rho = (obs["W"] ** 2) / (mZ ** 2 * c2)
    bulkW, tipW, sumW = rayleigh_split(lamW, eta, bW)
    lo_order = bW * 3.0 * eta * math.exp(-3.0 * eta) / (-math.expm1(-3.0 * eta))    # leading order Lambda(beta)
    # W and Z towers: the first excited levels
    W1 = eigenvalues(eta, bW, nmax=2, lam_max=1.6 * L1, ngrid=500)
    out["gauge"] = {"cos2_thetaW_onshell": c2, "beta_W": bW, "Lambda_W": lamW, "Lambda_W_back": lamW_back, "beta_Z": bZ, "Lambda_Z": lamZ,
                    "m_Z_pred_GeV": mZ, "m_Z_obs_GeV": obs["Z"], "m_Z_pred_minus_obs_GeV": mZ - obs["Z"],
                    "rho_tree": rho, "rho_minus_1": rho - 1.0,
                    "rho_pull_sigma": (rho - 1.0 - obs["rho0_minus_1"]) / obs["rho0_sigma"],
                    "Lambda_W_leading_order": lo_order, "leading_order_rel_dev": lo_order / lamW - 1.0,
                    "rayleigh_W": {"bulk_hidden_momentum": bulkW, "tip": tipW, "sum": sumW, "sum_rel_dev": sumW / lamW - 1.0},
                    "W_tower_GeV": [math.sqrt(x) / fl for x in W1],
                    "photon_gluon_graviton": {"Lambda_0": num_neu[0], "massless": abs(num_neu[0]) < 1e-12,
                                              "first_KK_GeV": math.sqrt(num_neu[1]) / fl}}
    ferm = {}
    for s in ("e", "u", "d", "nu"):
        ratio = obs[s] / m_kk_gev
        c = c_for(ratio)
        dt = width_t(c)
        ds = fl * dt                                     # proper width (GeV^-1)
        m_heis = 1.0 / (2.0 * ds)                        # hbar c/(2 Delta s), GeV
        ferm[s] = {"m_obs_GeV": obs[s], "ratio_to_mKK": ratio, "c_f": c, "zeta2": zeta2(c), "mu_f_over_H": c / (f * eta),
                   "width_t": dt, "width_t_exact": width_t_exact(c), "Delta_s_GeV^-1": ds, "Delta_s_m": ds * HBARC_GEV_M,
                   "heisenberg_mass_GeV": m_heis, "m_over_heisenberg": obs[s] / m_heis}
    out["fermions"] = ferm
    # the W profile as a function of x0 over two periods: periodic with pi/(6H) by construction (check)
    z = np.linspace(0.05, 2 * math.pi - 0.05, 4001)
    y = np.log(np.abs(np.sin(z))) / (6.0 * 1.0)          # units H = 1 of the cell
    tt = np.clip(y / eta, -1.0, 0.0)                     # t = y/L = H y/(H L)
    _, _, us = shoot(lamW, eta, profile=True)
    tg = np.linspace(0.0, -1.0, len(us))
    prof = np.interp(-tt, -tg, us)
    zs = z + math.pi
    ys = np.log(np.abs(np.sin(zs))) / 6.0
    prof_s = np.interp(-np.clip(ys / eta, -1.0, 0.0), -tg, us)
    out["periodicity"] = {"max_abs_u(x0+pi/6H)-u(x0)": float(np.max(np.abs(prof_s - prof)))}
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(fit(), indent=1, default=float))
