#!/usr/bin/env python3
"""UM-2 thermal history and the dark-matter relic from the Boltzmann equation (version 3, 2026-10-18).

T1  The particle content of UM-2 at temperature T with its x0 masses (three generations, massive W+, W-, Z and no Higgs
    particle, massless gluons and photon, the dark-matter fermions of both halves of dirac16complex, 44.35 TeV; the fold
    bands of dirac16complex and the right-handed neutrinos are never thermalised; the radion and the Kaluza-Klein modes
    are not thermalised below 10 TeV): g_rho(T), g_s(T) from the exact ideal-gas integrals.  The QCD crossover is
    modelled by a smooth switch between the quark-gluon plasma and a hadron resonance gas (ASSUMED model); neutrinos
    decouple instantaneously at 2 MeV and are not heated by the e+e- annihilation (their temperature then follows from
    the separate conservation of the photon-electron entropy).
T2  The thermal average of the I12 annihilation cross-section, the exact relativistic (Gondolo-Gelmini) integral, and its
    non-relativistic limit <sigma v> = 6 b/x.
T3  The Boltzmann equation of one Dirac species (particle + antiparticle), solved numerically with g_rho(T), g_s(T);
    validation against the late-time integral and against the freeze-out formula for an s-wave and a p-wave process.
T4  The portal strength for Omega_c h^2 = 0.120 (two species, 0.060 each) from the numerical solution, compared with the
    freeze-out formula of version 2.
T5  Partial-wave unitarity.  The I12 operator G chibar chi F F annihilates a fermion-antifermion pair only from the J = 0,
    P = + state (3P0); for unpolarised Dirac fermions the inelastic cross-section is bounded by sigma <= pi/(4 p^2)
    (p the centre-of-mass momentum), i.e. sigma v <= pi/(M^2 v) for v << 1.  The velocity above which the effective
    cross-section exceeds the bound, the relic with the cross-section capped at the bound for every portal strength,
    and the smallest relic that any annihilation from the 3P0 channel can give.
T6  The I12 benchmark with universal coefficients c_G = c_W = c_B and one-loop gauge couplings at the annihilation scale.
Writes outputs/thermal.json, figures/fig_thermal_relic.png and reports/thermal-checks.json.
"""
import math
import os
import sys

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.interpolate import CubicSpline
from scipy.special import k1e, kve

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import M_PSI_OVER_H, val  # noqa: E402

GEV2_TO_CM3S = 0.389379e-27 * 2.99792458e10      # 1 GeV^-2 times c, in cm^3/s
RHO_C_H2 = 1.05368e-5                              # critical density / h^2 in GeV/cm^3 (STANDARD)


# ----------------------------------------------------------------------------------------------------------------------
# ideal-gas thermodynamics
_U, _WU = np.polynomial.legendre.leggauss(160)


def gas(m, T, g, fermion):
    """rho, p, s of an ideal gas of g internal states, mass m, temperature T, zero chemical potential (exact integrals,
    Gauss-Legendre on u = p/T in [0, umax], umax = sqrt((x + 60)^2 - x^2))."""
    x = m / T
    if x > 200.0:
        return 0.0, 0.0, 0.0
    umax = math.sqrt((x + 60.0) ** 2 - x * x)
    u = 0.5 * umax * (_U + 1.0)
    w = 0.5 * umax * _WU
    E = np.sqrt(u * u + x * x) if x > 0 else u
    occ = 1.0 / (np.exp(E) + (1.0 if fermion else -1.0))
    rho = g / (2 * math.pi ** 2) * float(np.sum(w * u * u * E * occ)) * T ** 4
    p = g / (6 * math.pi ** 2) * float(np.sum(w * u ** 4 / np.maximum(E, 1e-300) * occ)) * T ** 4
    return rho, p, (rho + p) / T


def species(masses, dm_mass):
    """The thermalised species of UM-2: (name, mass GeV, g, fermion, group); group 'qgp' (quarks, gluons), 'hrg' (hadrons),
    'nu' (neutrinos), 'eg' (photon, electrons), 'other'."""
    F = masses['fermions']
    sp = [('photon', 0.0, 2, False, 'eg'), ('gluons', 0.0, 16, False, 'qgp'),
          ('W+ W-', val('m_W_GeV'), 6, False, 'other'), ('Z', masses['WZ']['m_Z_pred_GeV'], 3, False, 'other')]
    for q in ('u', 'd', 's', 'c', 'b', 't'):
        sp.append((q, F[q]['m_GeV'], 12, True, 'qgp'))
    sp.append(('e', F['e']['m_GeV'], 4, True, 'eg'))
    for l in ('mu', 'tau'):
        sp.append((l, F[l]['m_GeV'], 4, True, 'other'))
    for n in ('nu1', 'nu2', 'nu3'):
        sp.append((n, 0.0, 2, True, 'nu'))      # m_nu << T in every era in which they are thermal
    # the dark-matter fermions of the two halves (Dirac: 2 spin states, particle and antiparticle)
    sp.append(('dark matter Psi_A', dm_mass, 4, True, 'dm'))
    sp.append(('dark matter Psi_B', dm_mass, 4, True, 'dm'))
    # hadron resonance gas below the QCD crossover (lightest states; PDG masses, from memory)
    hrg = [('pi', 0.1380, 3, False), ('K', 0.4956, 4, False), ('eta', 0.5479, 1, False), ('rho', 0.7753, 9, False),
           ('omega', 0.7827, 3, False), ('K*', 0.8917, 12, False), ('N', 0.9389, 8, True), ('eta prime', 0.9578, 1, False),
           ('phi', 1.0195, 3, False), ('Lambda', 1.1157, 4, True), ('Sigma', 1.1932, 12, True), ('Delta', 1.232, 32, True)]
    for (n, m, g, fe) in hrg:
        sp.append((n, m, g, fe, 'hrg'))
    return sp


T_QCD, DT_QCD = 0.155, 0.015      # crossover temperature and width of the switch (ASSUMED)
T_NU_DEC = 0.002                  # instantaneous neutrino decoupling (ASSUMED; the full computation is in um2_neutrino.py)


def w_qgp(T):
    return 0.5 * (1.0 + math.tanh((T - T_QCD) / DT_QCD))


def thermo(T, sp, include_dm=True):
    """g_rho(T), g_s(T) with rho = (pi^2/30) g_rho T^4, s = (2 pi^2/45) g_s T^3."""
    rho = 0.0
    s = 0.0
    # photon + electron entropy, for the neutrino temperature after decoupling
    for (n, m, g, fe, grp) in sp:
        if grp == 'nu' or (grp == 'dm' and not include_dm):
            continue
        r, p, se = gas(m, T, g, fe)
        wgt = 1.0
        if grp == 'qgp':
            wgt = w_qgp(T)
        elif grp == 'hrg':
            wgt = 1.0 - w_qgp(T)
        rho += wgt * r
        s += wgt * se
    # neutrinos: thermal above T_NU_DEC; afterwards T_nu/T = (g_s,eg(T)/(11/2))^(1/3): instantaneous decoupling while the
    # electrons are relativistic (g_s,eg = 2 + 7/8 4 = 11/2), the photon-electron entropy conserved separately
    if T >= T_NU_DEC:
        Tnu = T
    else:
        tot = 0.0
        for (n, m, g, fe, grp) in sp:
            if grp == 'eg':
                tot += gas(m, T, g, fe)[2]
        gs_eg = tot / (2 * math.pi ** 2 / 45 * T ** 3)
        Tnu = T * (gs_eg / 5.5) ** (1.0 / 3.0)
    for (n, m, g, fe, grp) in sp:
        if grp == 'nu':
            r, p, se = gas(m, Tnu, g, fe)
            rho += r
            s += se
    return rho / (math.pi ** 2 / 30 * T ** 4), s / (2 * math.pi ** 2 / 45 * T ** 3), Tnu / T


# ----------------------------------------------------------------------------------------------------------------------
# annihilation: L = G chibar chi F F per abelian channel, total G^2 = 8 G_g^2 + 3 G_W^2 + G_B^2
def sigma_I12(s, M, G2):
    """Total cross-section (spin averaged, summed over channels): sigma v_Mol(CM) = G^2 s (s - 4M^2)/(4 pi),
    v_Mol = 2 sqrt(1 - 4M^2/s): sigma = G^2 s^(3/2) (s - 4M^2)^(1/2)/(8 pi)."""
    return G2 * s ** 1.5 * math.sqrt(max(s - 4 * M * M, 0.0)) / (8 * math.pi)


def sigma_unitarity(s, M):
    """J = 0 (3P0) bound for unpolarised Dirac fermions: sigma <= pi/(4 p^2), p^2 = s/4 - M^2."""
    p2 = s / 4.0 - M * M
    return math.pi / (4.0 * p2) if p2 > 0 else float('inf')


def sigmav_thermal(x, M, sig, zbreaks=()):
    """Gondolo-Gelmini <sigma v_Mol> = [1/(8 M^4 T K2(x)^2)] int_{4M^2}^inf sigma(s) (s - 4M^2) sqrt(s) K1(sqrt(s)/T) ds.
    With s = 4M^2 (1 + z), z = (v_cm-like) kinetic variable; exponentially scaled Bessel functions for stability."""
    T = M / x

    def integrand(z):
        s = 4 * M * M * (1.0 + z)
        rs = math.sqrt(s)
        # K1(rs/T) / K2(x)^2 = k1e(rs/T) e^{-rs/T} / (kve(2,x)^2 e^{-2x}) = k1e kve^-2 e^{2x - rs/T}
        expo = 2 * x - rs / T
        return sig(s) * (s - 4 * M * M) * rs * k1e(rs / T) * math.exp(expo) * 4 * M * M
    # the integrand is concentrated at z ~ 1/x
    zmax = 200.0 / x
    pts = sorted(set([1.0 / x, 5.0 / x, 20.0 / x] + [zb for zb in zbreaks if 0 < zb < zmax]))
    val_, err = quad(integrand, 0.0, zmax, points=pts, limit=400, epsabs=0.0, epsrel=1e-11)
    K2s = kve(2, x)
    return val_ / (8 * M ** 4 * T * K2s ** 2)


# ----------------------------------------------------------------------------------------------------------------------
# Boltzmann equation of one Dirac species (Y = Y_chi + Y_chibar), x = M/T
class Cosmo:
    def __init__(self, sp, Tgrid=None):
        if Tgrid is None:
            Tgrid = np.logspace(-4.5, 4.3, 360)
        self.lnT = np.log(Tgrid)
        gr, gs = [], []
        for T in Tgrid:
            a, b, _ = thermo(T, sp, include_dm=False)
            gr.append(a)
            gs.append(b)
        self.gr = np.array(gr)
        self.gs = np.array(gs)
        self.dlngs = np.gradient(np.log(self.gs), self.lnT)

    def g(self, T):
        lt = math.log(T)
        return (float(np.interp(lt, self.lnT, self.gr)), float(np.interp(lt, self.lnT, self.gs)),
                float(np.interp(lt, self.lnT, self.dlngs)))


def relic(M, sigv, cosmo, gdof=2, x0=5.0, x1=2000.0, MPl=None, dirac=True):
    """Solve dY/dx = -(1 + delta) s <sigma v>/(c x H) (Y^2 - Y_eq^2), delta = (1/3) d ln g_s/d ln T, c = 2 for a Dirac species
    (Y total, <sigma v> of chi chibar), c = 1 for a Majorana species; Y_eq (total) = n_eq/s with n_eq = n_states g M^2 T K2(x)/(2 pi^2).
    Integrates ln Y (implicit Radau).  Returns Y(x1), the history and x_f (where Y = 2.5 Y_eq)."""
    if MPl is None:
        MPl = val('M_Pl_GeV')
    nst = 2 if dirac else 1
    c = 2.0 if dirac else 1.0

    def parts(x):
        T = M / x
        gr, gs, dl = cosmo.g(T)
        s = 2 * math.pi ** 2 / 45 * gs * T ** 3
        H = math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / MPl
        neq = nst * gdof * M * M * T * kve(2, x) * math.exp(-x) / (2 * math.pi ** 2)
        return s, H, neq / s, (1.0 + dl / 3.0)

    def rhs(x, ly):
        s, H, yeq, fac = parts(x)
        Y = math.exp(ly[0])
        return [-fac * s * sigv(x) / (c * x * H) * (Y - yeq * yeq / Y)]

    s0, H0, yeq0, _ = parts(x0)
    sol = solve_ivp(rhs, (x0, x1), [math.log(yeq0)], method='Radau', rtol=1e-10, atol=1e-12, dense_output=True)
    xs = np.logspace(math.log10(x0), math.log10(x1), 400)
    Ys = np.exp(sol.sol(xs)[0])
    yeqs = np.array([parts(xx)[2] for xx in xs])
    xf = None
    for xx, Y, ye in zip(xs, Ys, yeqs):
        if Y > 2.5 * ye:
            xf = float(xx)
            break
    return float(np.exp(sol.y[0][-1])), {'x': xs.tolist(), 'Y': Ys.tolist(), 'Yeq': yeqs.tolist()}, xf


def omega_h2(M, Y, s0):
    return M * Y * s0 / RHO_C_H2


def main():
    rep = Report('thermal-checks', 'UM-2 thermal history (x0 masses, three generations, no Higgs) and the dark-matter relic from the '
                 'Boltzmann equation; partial-wave unitarity of the gauge-kinetic portal')
    out = {}
    masses = read_json(os.path.join(OUT, 'masses.json'))
    spec = read_json(os.path.join(OUT, 'ks', 'spectrum.json'))
    H_GeV = masses['scales']['H_GeV']
    M = spec['eps_dm'] * M_PSI_OVER_H * H_GeV
    out['M_DM_GeV'] = M
    sp = species(masses, M)
    MPl = val('M_Pl_GeV')

    # ---------------- T1 thermal history ----------------
    probe = {}
    for T in (5000.0, 1460.0, 200.0, 10.0, 1.0, 0.3, 0.155, 0.1, 0.01, 0.003, 0.001, 1e-4, 1e-5):
        gr, gs, tr = thermo(T, sp, include_dm=False)
        probe['%.6g GeV' % T] = {'g_rho': gr, 'g_s': gs, 'Tnu_over_T': tr}
    out['g_star_table'] = probe
    # today: T0 = 2.7255 K
    kB = val('k_B_eV_per_K') * 1e-9
    T0 = val('T_CMB_K') * kB
    g0r, g0s, tr0 = thermo(T0 * 1e6, sp, include_dm=False)      # any T << m_e gives the asymptotic values
    out['today'] = {'g_rho': g0r, 'g_s': g0s, 'Tnu_over_T': tr0}
    hbarc_cm = val('hbar_c_GeV_m') * 100.0
    s0 = 2 * math.pi ** 2 / 45 * g0s * T0 ** 3 / hbarc_cm ** 3          # cm^-3
    out['s0_cm3'] = s0
    g5 = probe['5000 GeV']
    g10 = probe['10 GeV']
    g1m = probe['0.003 GeV']
    rep.check('T1_degrees_of_freedom', abs(g5['g_rho'] - 105.75) < 0.05 and abs(g10['g_rho'] - 86.25) < 0.6
              and abs(g1m['g_rho'] - 10.75) < 0.1 and abs(g0s - 43.0 / 11.0) < 1e-3
              and abs(g0r - (2 + 7.0 / 8 * 6 * (4.0 / 11) ** (4.0 / 3))) < 1e-3,
              'ideal-gas sums with the x0 masses: g_rho = %.3f at 5 TeV (105.75: three generations, massive W+, W-, Z, no Higgs particle; '
              'no right-handed neutrinos, no fold bands), %.3f at 10 GeV (86.25 without t, W, Z), %.3f at 3 MeV (10.75), today g_s = %.4f '
              '(43/11 = 3.9091) and g_rho = %.4f (3.3626); s0 = %.1f cm^-3' % (g5['g_rho'], g10['g_rho'], g1m['g_rho'], g0s, g0r, s0))

    cosmo = Cosmo(sp)
    out['g_star_curve'] = {'T_GeV': np.exp(cosmo.lnT).tolist(), 'g_rho': cosmo.gr.tolist(), 'g_s': cosmo.gs.tolist()}

    # ---------------- T2 thermal average ----------------
    G2_test = 1e-26
    sig = lambda s: sigma_I12(s, M, G2_test)
    nr = []
    for x in (10.0, 30.0, 100.0, 1000.0):
        exact = sigmav_thermal(x, M, sig)
        b = G2_test * M ** 4 / math.pi
        nr.append((x, exact, 6 * b / x))
    out['thermal_average_check'] = [{'x': x, 'exact': e, 'nonrel_6b_over_x': a} for (x, e, a) in nr]
    rel = [e / a - 1 for (x, e, a) in nr]
    xr = [r * x for r, (x, e, a) in zip(rel, nr)]
    rep.check('T2_thermal_average', abs(rel[-1]) < 5e-3 and all(2.5 < v < 4.5 for v in xr[1:]),
              'Gondolo-Gelmini average of sigma = G^2 s^(3/2) (s - 4M^2)^(1/2)/(8 pi) against the non-relativistic 6 b/x (b = G^2 M^4/pi): '
              'relative excess %s at x = 10, 30, 100, 1000, i.e. x times the excess = %s: the expansion <sigma v> = (6b/x)(1 + c1/x + ...) '
              'with c1 ~ 3 (the momentum dependence s(s - 4M^2) = 16 (M^2 + p^2) p^2 gives 2.5/x from <p^4>/<p^2>); at freeze-out the '
              'non-relativistic formula used in version 2 underestimates <sigma v> by about 10 %%' % (
                  ', '.join('%.3e' % r for r in rel), ', '.join('%.2f' % v for v in xr)))
    out['thermal_average_relativistic_coefficient'] = xr

    # ---------------- T3 Boltzmann solver validation ----------------
    # (a) s-wave Dirac species, <sigma v> = sigma0: late-time integral 1/Y_inf - 1/Y(x*) = int_{x*} (1+delta) s sigma0/(2 x H) dx
    sigma0 = 4.4e-26 / GEV2_TO_CM3S
    Yinf, hist, xf_s = relic(M, lambda x: sigma0, cosmo, MPl=MPl)
    xs = np.array(hist['x'])
    Ys = np.array(hist['Y'])
    istar = int(np.searchsorted(xs, 3 * (xf_s or 30)))
    xstar = xs[istar]

    def lam(x):
        T = M / x
        gr, gs, dl = cosmo.g(T)
        s = 2 * math.pi ** 2 / 45 * gs * T ** 3
        H = math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / MPl
        return (1 + dl / 3) * s * sigma0 / (2 * x * H)
    integral = quad(lam, xstar, 2000.0, limit=200)[0]
    late = 1.0 / Ys[-1] - 1.0 / Ys[istar]
    om_s = omega_h2(M, Yinf, s0)
    # freeze-out formula (Kolb-Turner) for the same s-wave Dirac species
    gst = cosmo.g(M / 25.0)[0]
    xf_ft = 25.0
    for _ in range(50):
        xf_ft = math.log(0.038 * 0.5 * 2.5 * 2 * MPl * M * sigma0 / math.sqrt(gst * xf_ft))
    om_ft = 2 * 1.07e9 * xf_ft / (math.sqrt(gst) * MPl * sigma0)
    out['validation_s_wave'] = {'sigma0_cm3_s': 4.4e-26, 'Omega_h2_numerical': om_s, 'Omega_h2_freeze_out_formula': om_ft, 'x_f_numerical': xf_s,
                                'x_f_formula': xf_ft, 'late_time_integral_check': abs(late / integral - 1)}
    rep.check('T3_boltzmann_solver', abs(late / integral - 1) < 1e-4 and abs(om_s / om_ft - 1) < 0.08,
              's-wave Dirac species with <sigma v> = 4.4e-26 cm^3/s at M = %.0f GeV: numerical Omega h^2 = %.4f (particle + antiparticle), '
              'freeze-out formula %.4f (x_f %.1f against %.1f); the late-time integral 1/Y(inf) - 1/Y(x*) = int lambda dx is reproduced to '
              '%.1e (the standard result: about 4.4e-26 cm^3/s for Omega h^2 = 0.12, FROM MEMORY)' % (
                  M, om_s, om_ft, xf_s, xf_ft, abs(late / integral - 1)))

    # ---------------- T4 relic of the two species through I12 (effective operator, no cap) ----------------
    XT = np.logspace(math.log10(5.0), math.log10(2000.0), 260)

    def sv_table(sg, zb=()):
        """<sigma v>(x) on a log grid, interpolated by a cubic spline in (ln x, ln <sigma v>)."""
        vals = np.array([sigmav_thermal(xx, M, sg, zb) for xx in XT])
        cs = CubicSpline(np.log(XT), np.log(vals))
        return lambda x: math.exp(float(cs(math.log(min(max(x, XT[0]), XT[-1])))))

    sv_unit_G = sv_table(lambda s: sigma_I12(s, M, 1.0))      # effective operator: <sigma v> is exactly proportional to G^2

    def omega_of(G2, cap=False):
        if cap:
            scx = brentq(lambda s: sigma_I12(s, M, G2) - sigma_unitarity(s, M), 4 * M * M * (1 + 1e-12), 1e4 * M * M)
            sv = sv_table(lambda s: min(sigma_I12(s, M, G2), sigma_unitarity(s, M)), (scx / (4 * M * M) - 1.0,))
        else:
            sv = lambda x: G2 * sv_unit_G(x)
        Y, h, xf = relic(M, sv, cosmo, MPl=MPl)
        return omega_h2(M, Y, s0), xf, h
    target = 0.060
    lo, hi = math.log(1e-27), math.log(1e-24)
    f = lambda lg: omega_of(math.exp(lg))[0] - target
    lgsol = brentq(f, lo, hi, xtol=1e-6)
    G2req = math.exp(lgsol)
    om_req, xf_req, hist_req = omega_of(G2req)
    Greq = math.sqrt(G2req)
    ana = read_json(os.path.join(OUT, 'analysis.json'))['relic']
    out['relic_effective_operator'] = {'G_eff_GeV-3': Greq, 'Lambda_eff_TeV': Greq ** (-1.0 / 3.0) / 1e3, 'x_f': xf_req,
                                       'Omega_h2_per_species': om_req, 'formula_v2_Lambda_eff_TeV': ana['Lambda_eff_TeV'],
                                       'sigma_v_at_xf_cm3_s': sigmav_thermal(xf_req, M, lambda s: sigma_I12(s, M, G2req)) * GEV2_TO_CM3S}
    rep.check('T4_relic_numerical', abs(om_req - target) < 1e-4 and abs(Greq ** (-1 / 3.) / 1e3 / ana['Lambda_eff_TeV'] - 1) < 0.1,
              'numerical Boltzmann solution (exact thermal average, g_rho(T), g_s(T)): each species gives Omega h^2 = 0.060 for '
              '(8 G_g^2 + 3 G_W^2 + G_B^2)^(1/2) = %.4e GeV^-3 = (%.3f TeV)^-3 (x_f = %.2f, <sigma v>(x_f) = %.3e cm^3/s), against '
              '(%.2f TeV)^-3 from the freeze-out formula of version 2 (if the effective operator held at every energy)' % (
                  Greq, Greq ** (-1 / 3.) / 1e3, xf_req, out['relic_effective_operator']['sigma_v_at_xf_cm3_s'], ana['Lambda_eff_TeV']))

    # ---------------- T5 partial-wave unitarity ----------------
    # crossing velocity v_c (non-relativistic): G^2 M^4 v^2/pi = pi/(M^2 v)  ->  v_c = (pi/(G M^3))^(2/3)
    vc = (math.pi / (Greq * M ** 3)) ** (2.0 / 3.0)
    xfr = xf_req
    frac_above = quad(lambda v: v * v * math.exp(-xfr * v * v / 4), vc, 50 / math.sqrt(xfr))[0] / quad(
        lambda v: v * v * math.exp(-xfr * v * v / 4), 0, 50 / math.sqrt(xfr))[0]
    # exact crossing in s
    sc = brentq(lambda s: sigma_I12(s, M, G2req) - sigma_unitarity(s, M), 4 * M * M * (1 + 1e-12), 40 * M * M)
    # unitarity-limited thermal average and relic: sigma = pi/(4 p^2) at every s (the largest annihilation from 3P0)
    sv_u = sv_table(lambda s: sigma_unitarity(s, M))
    nr_u = math.sqrt(math.pi * xfr) / M ** 2
    Yu, hu, xfu = relic(M, sv_u, cosmo, MPl=MPl)
    om_unit = omega_h2(M, Yu, s0)
    # capped effective operator: Omega(G) for increasing G
    capped = []
    for fac in (1.0, 3.0, 10.0, 100.0, 1e4):
        omc, xfc, _ = omega_of(G2req * fac, cap=True)
        capped.append({'G2_over_G2req': fac, 'Omega_h2_per_species': omc, 'x_f': xfc})
    omin = om_unit
    out['unitarity'] = {'bound': 'sigma <= pi/(4 p^2) (J = 0, P = +, unpolarised Dirac fermions)', 'v_crossing': vc,
                        'sqrt_s_crossing_GeV': math.sqrt(sc), 'fraction_of_pairs_above_vc_at_xf': frac_above,
                        'sigma_v_bound_at_xf_cm3_s': sv_u(xfr) * GEV2_TO_CM3S, 'sigma_v_bound_nonrel_at_xf_cm3_s': nr_u * GEV2_TO_CM3S,
                        'Omega_h2_per_species_unitarity_limited': om_unit, 'x_f_unitarity_limited': xfu, 'capped': capped,
                        'swave_estimate_v2_cm3_s': ana['unitarity_scale_swave_estimate_cm3_s']}
    rep.check('T5_unitarity_violated_by_effective_operator', vc < 1.0 and frac_above > 0.5,
              'the effective cross-section of the relic strength exceeds the J = 0 (3P0) unitarity bound sigma <= pi/(4 p^2) above the '
              'relative velocity v_c = %.3f (sqrt(s) = %.1f GeV, %.1f GeV above threshold); at freeze-out (x = %.1f) %.0f %% of the annihilating '
              'pairs have v > v_c: the effective operator I12 cannot be used for the relic' % (vc, math.sqrt(sc), math.sqrt(sc) - 2 * M, xfr,
                                                                                               100 * frac_above))
    rep.check('T5_unitarity_limited_relic', om_unit > 0 and all(c_['Omega_h2_per_species'] >= om_unit * 0.999 for c_ in capped),
              'with sigma = pi/(4 p^2) at every energy (the largest annihilation any interaction can give from the 3P0 channel) each species '
              'leaves Omega h^2 = %.4f (x_f = %.2f; <sigma v>(x_f) = %.3e cm^3/s, non-relativistic sqrt(pi x)/M^2 = %.3e; version 2 compared '
              'with the s-wave estimate %.3e); the capped effective operator gives %s for G^2/G^2_relic = 1, 3, 10, 100, 1e4: %s' % (
                  om_unit, xfu, sv_u(xfr) * GEV2_TO_CM3S, nr_u * GEV2_TO_CM3S, ana['unitarity_scale_swave_estimate_cm3_s'],
                  ', '.join('%.4f' % c_['Omega_h2_per_species'] for c_ in capped),
                  'a relic of 0.060 per species is reachable only near the unitarity limit' if om_unit < target else
                  'NO portal strength reaches 0.060 per species: thermal freeze-out through the 3P0 channel overproduces the dark matter'))

    # ---------------- T6 the I12 benchmark: unitarity-safe strength, universal coefficients ----------------
    # The effective operator respects the 3P0 bound for all v < v_c = (pi/(G M^3))^(2/3); the benchmark G = pi/(2 M^3) puts the
    # crossing beyond the non-relativistic range (v_c = 2^(2/3)); its exact crossing in s is computed.  Then I12 alone cannot give
    # the relic (it would leave far too much dark matter); the relic needs an s-wave channel (I13, um2_coupled.py).
    G12 = math.pi / (2 * M ** 3)
    sc12 = brentq(lambda s: sigma_I12(s, M, G12 ** 2) - sigma_unitarity(s, M), 4 * M * M * (1 + 1e-12), 400 * M * M)
    om12, xf12, _ = omega_of(G12 ** 2)
    # fraction of the annihilation rate at freeze-out (x = 30) coming from collisions above the crossing
    zc = sc12 / (4 * M * M) - 1.0
    wfun = lambda z: sigma_I12(4 * M * M * (1 + z), M, G12 ** 2) * z * math.sqrt(1 + z) * k1e(2 * 30.0 * math.sqrt(1 + z)) * math.exp(
        -2 * 30.0 * (math.sqrt(1 + z) - 1))
    frac12 = quad(wfun, zc, 50.0, limit=200)[0] / quad(wfun, 0.0, 50.0, points=[1 / 30., 5 / 30.], limit=200)[0]
    mZ = val('m_Z_GeV')
    a_s = val('alpha_s_mZ')
    a_em = 1.0 / 127.95            # alpha(m_Z), MS-bar (FROM MEMORY)
    s2 = val('sin2_theta_W_MSbar')
    mu = 2 * M
    L_ = math.log(mu / mZ) / (2 * math.pi)
    inv3 = 1 / a_s + 7.0 * L_
    inv2 = s2 / a_em + (10.0 / 3.0) * L_
    inv1 = (1 - s2) / a_em - (20.0 / 3.0) * L_
    g2 = {'g_s^2': 4 * math.pi / inv3, 'g^2': 4 * math.pi / inv2, "g'^2": 4 * math.pi / inv1}
    comb = math.sqrt(8 * g2['g_s^2'] ** 2 + 3 * g2['g^2'] ** 2 + g2["g'^2"] ** 2)
    O = 0.7072
    c_over_L3 = G12 / (O * comb)
    out['I12_universal_benchmark'] = {'G_combination_GeV-3': G12, 'Lambda_eff_TeV': G12 ** (-1 / 3.) / 1e3,
                                      'sqrt_s_unitarity_crossing_GeV': math.sqrt(sc12), 'gamma_cm_at_crossing': math.sqrt(sc12) / (2 * M),
                                      'Omega_h2_per_species_I12_alone': om12, 'mu_GeV': mu, 'couplings_squared': g2,
                                      'combination': comb, 'c_over_Lambda_star3_GeV-3': c_over_L3,
                                      'Lambda_star_over_c13_TeV': c_over_L3 ** (-1 / 3.) / 1e3, 'O': O,
                                      'G_g': O * c_over_L3 * g2['g_s^2'], 'G_W': O * c_over_L3 * g2['g^2'], 'G_B': O * c_over_L3 * g2["g'^2"]}
    out['I12_universal_benchmark']['fraction_of_rate_above_crossing_at_x30'] = frac12
    rep.check('T6_I12_benchmark', frac12 < 1e-3 and om12 > 1.0,
              'benchmark (8 G_g^2 + 3 G_W^2 + G_B^2)^(1/2) = pi/(2 M^3) = %.3e GeV^-3 = (%.1f TeV)^-3: the effective cross-section stays below '
              'the 3P0 bound up to sqrt(s) = %.0f GeV (%.2f M; a fraction %.1e of the annihilation rate at x = 30 comes from collisions above '
              'it); alone it would leave Omega h^2 = %.1f per '
              'species (the relic needs the s-wave portal I13); with c_G = c_W = c_B = c and one-loop couplings at 2 M = %.0f GeV '
              '(g_s^2 = %.3f, g^2 = %.3f, g\'^2 = %.3f; sqrt(8 g_s^4 + 3 g^4 + g\'^4) = %.3f): c/Lambda*^3 = %.3e GeV^-3, '
              'Lambda*/c^(1/3) = %.1f TeV' % (G12, G12 ** (-1 / 3.) / 1e3, math.sqrt(sc12), math.sqrt(sc12) / M, frac12, om12, mu,
                                              g2['g_s^2'], g2['g^2'], g2["g'^2"], comb, c_over_L3, c_over_L3 ** (-1 / 3.) / 1e3))

    # ---------------- figure ----------------
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        Tg = np.exp(cosmo.lnT)
        ax[0].semilogx(Tg, cosmo.gr, label=r'$g_\rho$')
        ax[0].semilogx(Tg, cosmo.gs, '--', label=r'$g_s$')
        ax[0].set_xlabel('T (GeV)')
        ax[0].set_ylabel('degrees of freedom')
        ax[0].set_title('UM-2 thermal history (x0 masses, no Higgs)')
        ax[0].legend()
        xs_ = np.array(hist_req['x'])
        ax[1].loglog(xs_, hist_req['Y'], label='effective I12 (relic strength)')
        ax[1].loglog(xs_, hu['Y'], label='unitarity limit $\\pi/(4p^2)$')
        ax[1].loglog(xs_, hist_req['Yeq'], ':', label='equilibrium')
        ax[1].set_ylim(1e-15, 1e-6)
        ax[1].set_xlabel('x = M/T')
        ax[1].set_ylabel('Y (one species)')
        ax[1].set_title('dark-matter freeze-out, M = %.2f TeV' % (M / 1e3))
        ax[1].legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(os.path.join(FIG, 'fig_thermal_relic.png'), dpi=130)
        plt.close(fig)
    except Exception as exc:     # pragma: no cover
        print('figure failed:', exc)

    out['history_effective'] = {k: v for k, v in hist_req.items()}
    out['history_unitarity_limited'] = hu
    write_json(os.path.join(OUT, 'thermal.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
