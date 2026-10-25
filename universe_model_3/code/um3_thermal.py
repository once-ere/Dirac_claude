#!/usr/bin/env python3
"""um3_thermal.py - the thermal history of UM-3: the relic density of the bound states chi of dirac16complex, their
couplings to the Standard Model and the right-handed neutrinos (SOLUTION.md; FE-47 and FE-59 to FE-62 of FIELD_EQUATIONS.md).

Units GeV (1 GeV^-2 = 3.894e-28 cm^2, times c: 1.1674e-17 cm^3/s).  The particles chi are the bound level of
dirac16complex: four particle states (one (2,2) multiplet of the rotations of ordinary space and of the extra times: two
Dirac fermions chi_a, a = 1, 2, of mass omega_b) and their four antiparticles, g_chi = 8 in n_chi of FE-61.  With two Dirac
species, FE-61 written for n_chi = sum over a of (n_a + nbar_a) has <sigma_ann v> = (sigma v)_{chi chibar}/4, where
(sigma v)_{chi chibar} is the spin-averaged annihilation of one chi_a with one chibar_a summed over the final states.
  T1  the radiation of the Standard Model (FE-60): g_rho(T) and g_s(T) from the exact Bose and Fermi integrals of every
      particle (quarks and gluons above the QCD transition at T_c = 0.155 GeV, the light hadrons below; neutrinos decoupled
      below 1 MeV with T_nu = (4/11)^{1/3} T after e+e- annihilation): 106.75 above the electroweak scale, 10.75 between
      the muon and the electron thresholds, 3.909 (g_s) and 3.363 (g_rho) today;
  T2  the relic density (FE-61): the Boltzmann equation for Y = n_chi/s solved numerically from x = 1 (with the
      relativistic equilibrium density g m^2 T K_2(m/T)/(2 pi^2)) to x = 1000 for an s-wave <sigma_ann v>; the value that gives
      Omega_chi h^2 = 0.1200 (Planck 2018) for omega_b = 10 GeV ... 10 TeV, compared with the analytic estimate of FE-61;
  T3  the current portals (FE-22, FE-47): the coupling g_f of a vector contact interaction (chibar gamma chi)(fbar gamma f)
      of a chiral fermion f gives (sigma v)_{chi chibar -> f fbar} = g_f^2 omega_b^2/(2 pi) per chiral state (massless f,
      s-wave); a relic density through quark portals implies a coherent scattering on nuclei sigma_SI = mu_N^2 f_N^2/pi with
      f_N = 3 g_q, excluded by LZ (2.1e-48 cm^2 at 36 GeV, limit ~ omega_b at high mass) by many orders of magnitude;
      through lepton portals (6 + 3 + 3 chiral lepton states) the scattering arises at one loop through the photon,
      g_p = (alpha/(3 pi)) g_l sum over e, mu, tau of ln(Lambda^2/max(m_l^2, q^2)) (Lambda = omega_b, q = 50 MeV), and LZ
      allows it only above a mass of order a TeV (ESTIMATE);
  T4  the Higgs portal (FE-47): g_hchi = -2 q_b^2/(omega_b v) is fixed by the binding q_b of the bound state; the Higgs
      exchange gives sigma_SI = mu_N^2 (g_hchi f_H m_N/(v m_h^2))^2/pi (f_H = 0.30), so LZ requires q_b/omega_b below a few
      per cent: the dark-matter particles chi are weakly bound (ESTIMATE);
  T5  the right-handed neutrinos (FE-62): their Yukawa production is negligible (Gamma/H ~ y^2 M_Pl/T << 1 for y = m_nu/v);
      if the lepton portal includes them (c^nu != 0) they stay in equilibrium with chi until n_chi,eq^2 (sigma v)_nu/n_nuR,eq
      = H, decouple at T_dec ~ omega_b/13 and add Delta N_eff = 3 (10.75/g_s(T_dec))^{4/3} = 0.14 ... 0.19; compared with
      Planck 2018 (N_eff = 2.99 +- 0.17) and ACT DR6 (2.86 +- 0.13; 2.89 +- 0.11 with BBN): the portal of the right-handed
      neutrinos must be weak enough that they never thermalise (c^nu << c^l), and then N_eff = 3.044;
  T6  the ad hoc vacuum before nucleosynthesis: G_F,loc = 1/(sqrt2 (v^2 + A^2)) (FE-49) changes the weak rates; requiring
      A^2/v^2 < 0.01 at x_4 = 1 s bounds a_40 from below in terms of the amplitude v_A of almightyAdHoc.
Writes outputs/thermal.json and reports/thermal_checks.json.
Usage: python universe_model_3/code/um3_thermal.py
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import kn

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

GEV2_CM2 = 3.894e-28           # (1 GeV^-1)^2 in cm^2
GEV2_CM3S = 1.1674e-17         # 1 GeV^-2 times c in cm^3/s
M_PL = 1.22089e19              # G_N^{-1/2} in GeV (FE-60)
V_EW = 246.22
M_H = 125.25
M_N = 0.9389
ALPHA = 1 / 137.036
S0_CM3 = 2891.2                # entropy density today (T0 = 2.7255 K)
RHOC_H2 = 1.05371e-5           # GeV/cm^3
OMEGA_DM_H2 = 0.1200           # Planck 2018
LZ_MIN = (2.1e-48, 36.0)       # cm^2 at GeV (LZ 2024, 4.2 tonne-years)
T_QCD = 0.155


def lz_limit(m):
    """The LZ 2024 limit approximated above its minimum by the 1/number-density scaling sigma_lim ~ m (weaker than the
    measured curve between the minimum and a few hundred GeV, so the exclusions drawn from it are conservative)."""
    return LZ_MIN[0] * max(1.0, m / LZ_MIN[1])


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


# ---------------------------------------------------------------- T1: the degrees of freedom
# (name, mass in GeV, internal degrees of freedom, +1 fermion / -1 boson)
SM_HIGH = [('t', 172.69, 12, 1), ('b', 4.18, 12, 1), ('c', 1.27, 12, 1), ('s', 0.093, 12, 1), ('d', 0.0047, 12, 1),
           ('u', 0.0022, 12, 1), ('g', 0.0, 16, -1)]
SM_LOW_HADRONS = [('pi+-', 0.13957, 2, -1), ('pi0', 0.13498, 1, -1), ('K', 0.4937, 4, -1), ('eta', 0.5479, 1, -1),
                  ('rho', 0.7753, 9, -1), ('omega', 0.7827, 3, -1), ('N', 0.9389, 8, 1)]
SM_COMMON = [('W', 80.37, 6, -1), ('Z', 91.19, 3, -1), ('h', 125.25, 1, -1), ('gamma', 0.0, 2, -1), ('tau', 1.777, 4, 1),
             ('mu', 0.10566, 4, 1), ('e', 0.000511, 4, 1)]
NU_L = ('nu_L', 0.0, 6, 1)


def _rho_s(y, stat):
    """(rho, s) of one internal degree of freedom in units of (pi^2/30) T^4 and (2 pi^2/45) T^3."""
    if y > 60:
        return 0.0, 0.0
    f = (lambda u: 1.0 / (math.exp(math.sqrt(u * u + y * y)) + 1)) if stat > 0 else \
        (lambda u: 1.0 / math.expm1(math.sqrt(u * u + y * y)) if u * u + y * y > 0 else 0.0)
    rho = quad(lambda u: u * u * math.sqrt(u * u + y * y) * f(u), 0, 80, limit=200)[0] * 15 / math.pi ** 4
    p = quad(lambda u: u ** 4 / math.sqrt(u * u + y * y) * f(u) if u > 0 else 0.0, 0, 80, limit=200)[0] * 5 / math.pi ** 4
    return rho, 0.75 * (rho + p)


def g_star(T):
    """g_rho(T) and g_s(T) of the Standard Model plasma (with the neutrinos; after their decoupling at 1 MeV they carry
    T_nu = (4/11)^{1/3} T, the instantaneous approximation)."""
    parts = SM_COMMON + (SM_HIGH if T > T_QCD else SM_LOW_HADRONS)
    gr = gs = 0.0
    for _, m, g, st in parts:
        r, s = _rho_s(m / T, st)
        gr += g * r
        gs += g * s
    if T > 1e-3:
        gr += 6 * 7 / 8
        gs += 6 * 7 / 8
    else:
        x = (4 / 11) ** (1 / 3)
        gr += 6 * 7 / 8 * x ** 4
        gs += 6 * 7 / 8 * x ** 3
        # after e+e- annihilation the photon temperature T is the reference; the e+e- entropy has gone to the photons
    return gr, gs


_LT = np.linspace(math.log(1e-5), math.log(2e4), 260)
_GT = np.array([g_star(math.exp(t)) for t in _LT])


def g_interp(T):
    lt = math.log(T)
    return float(np.interp(lt, _LT, _GT[:, 0])), float(np.interp(lt, _LT, _GT[:, 1]))


def dlngs_dlnT(T):
    lt = math.log(T)
    d = np.gradient(np.log(_GT[:, 1]), _LT)
    return float(np.interp(lt, _LT, d))


def hubble(T):
    gr, _ = g_interp(T)
    return math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / M_PL          # FE-60


def entropy(T):
    return 2 * math.pi ** 2 / 45 * g_interp(T)[1] * T ** 3


# ---------------------------------------------------------------- T2: the relic density
G_CHI = 8


def n_eq(m, T, g=G_CHI):
    x = m / T
    return g * m * m * T * kn(2, x) / (2 * math.pi ** 2) if x < 600 else 0.0


def relic(m, sv, g=G_CHI, x0=1.0, x1=1000.0):
    """Omega h^2 from FE-61 for the s-wave <sigma_ann v> = sv (GeV^-2); returns (Omega h^2, x_f, Y_inf)."""
    def Yeq(x):
        T = m / x
        return n_eq(m, T, g) / entropy(T)

    def rhs(lx, W):
        # W = ln Y; dY/dx = -(s sv/(x H)) (1 + dln g_s/dln T/3) (Y^2 - Yeq^2)
        x = math.exp(lx)
        T = m / x
        Y = math.exp(W[0])
        fac = entropy(T) * sv / (x * hubble(T)) * (1 + dlngs_dlnT(T) / 3)
        return [-x * fac * (Y * Y - Yeq(x) ** 2) / Y]
    sol = solve_ivp(rhs, (math.log(x0), math.log(x1)), [math.log(Yeq(x0))], method='Radau', rtol=1e-8, atol=1e-10,
                    dense_output=True)
    Yinf = math.exp(sol.y[0, -1])
    # freeze-out: where Y exceeds Y_eq by the factor 2.5 (the conventional delta = 1.5)
    xs = np.geomspace(x0, 200, 2000)
    Ys = np.exp(sol.sol(np.log(xs))[0])
    Ye = np.array([Yeq(x) for x in xs])
    k = int(np.argmax(Ys > 2.5 * Ye))
    xf = float(xs[k]) if k > 0 else float('nan')
    return m * Yinf * S0_CM3 / RHOC_H2, xf, Yinf


def sv_for_relic(m, target=OMEGA_DM_H2):
    f = lambda lsv: math.log(relic(m, math.exp(lsv))[0] / target)
    lsv = brentq(f, math.log(1e-11), math.log(1e-7), xtol=1e-10)
    return math.exp(lsv)


def main():
    t0 = time.time()
    rep = Report()
    out = {'conventions': {'g_chi': G_CHI, 'sigma_ann_v_FE61': '(sigma v)_{chi chibar}/4 for the two Dirac species',
                           'GeV^-2_in_cm^3/s': GEV2_CM3S}}

    # ---------------- T1
    pts = {}
    for T in (1e4, 300.0, 50.0, 5.0, 1.0, 0.2, 0.1, 0.01, 1e-3, 1e-5):
        gr, gs = g_interp(T)
        pts['%g GeV' % T] = {'g_rho': gr, 'g_s': gs}
    gr0, gs0 = g_star(1e-5)
    out['T1'] = pts
    ok1 = (abs(pts['10000 GeV']['g_rho'] - 106.75) < 0.05 and abs(pts['0.01 GeV']['g_s'] - 10.75) < 0.1
           and abs(gs0 - 3.909) < 0.01 and abs(gr0 - 3.363) < 0.01)
    rep.check('T1_degrees_of_freedom', ok1,
              'g_rho, g_s of the Standard Model: %s; above the electroweak scale 106.75 (three right-handed neutrinos in '
              'equilibrium would add 5.25), 10.75 between the muon and electron thresholds, today g_s = %.3f, g_rho = %.3f' % (
                  ', '.join('%s: %.2f/%.2f' % (k, v['g_rho'], v['g_s']) for k, v in pts.items()), gs0, gr0))

    # ---------------- T2
    rows = []
    for m in (10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 10000.0):
        sv = sv_for_relic(m)
        Oh2, xf, Y = relic(m, sv)
        gstar = g_interp(m / xf)[0]
        approx = 1.07e9 * xf / (math.sqrt(gstar) * M_PL * sv)          # FE-61
        rows.append({'omega_b_GeV': m, 'sv_FE61_GeV-2': sv, 'sv_FE61_cm3_s': sv * GEV2_CM3S,
                     'sv_chichibar_cm3_s': 4 * sv * GEV2_CM3S, 'x_f': xf, 'g_star_f': gstar, 'Omega_h2': Oh2,
                     'Omega_h2_FE61_estimate': approx})
        print('  relic m = %7.0f GeV: <sigma v>_FE61 = %.3e cm^3/s, x_f = %.1f, estimate %.4f' % (m, sv * GEV2_CM3S, xf, approx),
              flush=True)
    out['T2'] = rows
    ok2 = all(1.6e-26 < r['sv_FE61_cm3_s'] < 2.6e-26 for r in rows) and all(18 < r['x_f'] < 32 for r in rows) and all(
        abs(r['Omega_h2_FE61_estimate'] / OMEGA_DM_H2 - 1) < 0.25 for r in rows)
    rep.check('T2_relic_density', ok2,
              'Omega_chi h^2 = 0.1200 from the numerical solution of FE-61 for an s-wave annihilation requires <sigma_ann v> = '
              '%s cm^3/s (FE-61 normalisation, n_chi with g_chi = 8; (sigma v)_{chi chibar} is four times larger) with freeze-out '
              'at x_f = %s; the analytic estimate of FE-61 agrees within 25%%' % (
                  ', '.join('%.2e (%g GeV)' % (r['sv_FE61_cm3_s'], r['omega_b_GeV']) for r in rows),
                  ', '.join('%.1f' % r['x_f'] for r in rows)))

    # ---------------- T3: current portals
    dd = []
    for r in rows:
        m = r['omega_b_GeV']
        svcc = 4 * r['sv_FE61_GeV-2']                                   # (sigma v)_{chi chibar}
        # quark portals: 36 chiral quark states (6 flavours x 3 colours x 2 chiralities), equal g_q
        gq = math.sqrt(2 * math.pi * svcc / (36 * m * m))
        mu = m * M_N / (m + M_N)
        sig_q = mu * mu * (3 * gq) ** 2 / math.pi * GEV2_CM2
        # lepton portals: 6 + 3 + 3 chiral lepton states, equal g_l
        gl = math.sqrt(2 * math.pi * svcc / (12 * m * m))
        L = sum(math.log(m * m / max(ml * ml, 0.05 ** 2)) for ml in (0.000511, 0.10566, 1.777))
        gp = ALPHA / (3 * math.pi) * gl * L
        sig_l = mu * mu * gp ** 2 / math.pi * GEV2_CM2 * (54 / 131) ** 2        # per nucleon in xenon (Z/A)^2
        dd.append({'omega_b_GeV': m, 'g_quark_GeV-2': gq, 'sigma_SI_quark_cm2': sig_q, 'g_lepton_GeV-2': gl,
                   'loop_log_sum': L, 'sigma_SI_lepton_loop_cm2': sig_l, 'LZ_limit_cm2': lz_limit(m),
                   'quark_excluded_by_factor': sig_q / lz_limit(m), 'lepton_ratio_to_limit': sig_l / lz_limit(m)})
    out['T3'] = dd
    allowed = [d['omega_b_GeV'] for d in dd if d['lepton_ratio_to_limit'] < 1]
    m_min = None
    # the crossing mass of the lepton-loop scattering and the limit (log interpolation)
    for a, b in zip(dd[:-1], dd[1:]):
        if a['lepton_ratio_to_limit'] >= 1 > b['lepton_ratio_to_limit']:
            la, lb = math.log(a['lepton_ratio_to_limit']), math.log(b['lepton_ratio_to_limit'])
            m_min = math.exp(math.log(a['omega_b_GeV']) + la / (la - lb) * (math.log(b['omega_b_GeV']) - math.log(a['omega_b_GeV'])))
    ok3 = all(d['quark_excluded_by_factor'] > 1 for d in dd) and m_min is not None and allowed and max(allowed) == 10000.0
    rep.check('T3_current_portals', ok3,
              'a thermal relic through the quark current portals has sigma_SI = %s cm^2, above the LZ limit by factors %s: '
              'the quark portals cannot set the relic density at any mass up to 10 TeV (their couplings must be smaller than the '
              'relic value by the square roots of these factors); through the '
              'lepton portals the scattering is loop-induced, sigma_SI = %s cm^2 per nucleon, above the limit below about %.0f '
              'GeV and allowed above (ESTIMATE: the loop cut-off Lambda = omega_b and the scaling of the LZ limit enter): a '
              'leptophilic chi of a TeV or more can be the thermal relic' % (
                  ', '.join('%.1e' % d['sigma_SI_quark_cm2'] for d in dd),
                  ', '.join('%.0e' % d['quark_excluded_by_factor'] for d in dd),
                  ', '.join('%.1e (%g GeV)' % (d['sigma_SI_lepton_loop_cm2'], d['omega_b_GeV']) for d in dd),
                  m_min if m_min else float('nan')))

    # ---------------- T4: the Higgs portal
    fH = 0.30
    hp = []
    for m in (100.0, 300.0, 1000.0, 3000.0, 10000.0):
        mu = m * M_N / (m + M_N)
        gmax = math.sqrt(lz_limit(m) / GEV2_CM2 * math.pi) / (mu * fH * M_N / (V_EW * M_H ** 2))
        qmax = math.sqrt(gmax * m * V_EW / 2)                            # g_hchi = 2 q_b^2/(omega_b v)
        hp.append({'omega_b_GeV': m, 'g_hchi_max': gmax, 'q_b_max_GeV': qmax, 'q_b_over_omega_b_max': qmax / m})
    out['T4'] = hp
    ok4 = all(h['q_b_over_omega_b_max'] < 0.1 for h in hp)
    rep.check('T4_higgs_portal_binding', ok4,
              'the Higgs-portal Yukawa coupling of FE-47, g_hchi = -2 q_b^2/(omega_b v), gives sigma_SI = mu_N^2 (g_hchi f_H '
              'm_N/(v m_h^2))^2/pi; LZ then requires |g_hchi| < %s and q_b/omega_b < %s for omega_b = %s GeV (ESTIMATE): the '
              'dark-matter particles chi must be weakly bound to the fold' % (
                  ', '.join('%.1e' % h['g_hchi_max'] for h in hp), ', '.join('%.3f' % h['q_b_over_omega_b_max'] for h in hp),
                  ', '.join('%g' % h['omega_b_GeV'] for h in hp)))

    # ---------------- T5: the right-handed neutrinos
    nr = []
    for r in rows:
        m = r['omega_b_GeV']
        svcc = 4 * r['sv_FE61_GeV-2']
        sv_nu = svcc * 3 / 12                                           # the 3 right-handed neutrino states of 12

        def f(x):
            T = m / x
            n_nu = 3 * 2 * 3 * 1.2020569 / (4 * math.pi ** 2) * T ** 3        # 3 Weyl states (nu_R and its antiparticle)
            return math.log(n_eq(m, T) ** 2 / 4 * sv_nu / n_nu / hubble(T))
        xdec = brentq(f, 1.5, 60)
        Tdec = m / xdec
        dN = 3 * (10.75 / g_interp(Tdec)[1]) ** (4 / 3)                  # FE-62
        nr.append({'omega_b_GeV': m, 'x_dec': xdec, 'T_dec_GeV': Tdec, 'g_s_dec': g_interp(Tdec)[1], 'Delta_N_eff': dN,
                   'N_eff': 3.044 + dN, 'pull_Planck2018': (3.044 + dN - 2.99) / 0.17,
                   'pull_ACT_DR6_BBN': (3.044 + dN - 2.89) / 0.11})
    yuk = (0.05e-9 / V_EW) ** 2 * M_PL / 100.0                           # Gamma/H ~ y^2 M_Pl/T, y = 0.05 eV/v, T = 100 GeV
    out['T5'] = {'portal_thermalised': nr, 'yukawa_Gamma_over_H_at_100GeV': yuk}
    ok5 = all(0.13 < x['Delta_N_eff'] < 0.30 for x in nr) and yuk < 1e-6
    rep.check('T5_right_handed_neutrinos', ok5,
              'the Yukawa production of nu_R is negligible (Gamma/H ~ %.0e at 100 GeV); through the portal they decouple at '
              'x_dec = %s and add Delta N_eff = %s (FE-62), i.e. N_eff = %s against Planck 2018 2.99 +- 0.17 (pulls %s) and '
              'ACT DR6 with BBN 2.89 +- 0.11 (pulls %s): the right-handed neutrinos must not thermalise (c^nu << c^l, then '
              'N_eff = 3.044)' % (yuk, ', '.join('%.1f' % x['x_dec'] for x in nr), ', '.join('%.3f' % x['Delta_N_eff'] for x in nr),
                                   ', '.join('%.2f' % x['N_eff'] for x in nr),
                                   ', '.join('%.1f' % x['pull_Planck2018'] for x in nr),
                                   ', '.join('%.1f' % x['pull_ACT_DR6_BBN'] for x in nr)))

    # ---------------- T6: the ad hoc vacuum before nucleosynthesis
    # A(x4) = v_A exp(-2 a40 x4); A^2/v^2 < 0.01 at x4 = 1 s  <=>  a40 > ln(v_A/(0.1 v))/(2 s) (if v_A > 0.1 v)
    bounds = []
    for ratio in (0.1, 1.0, 10.0, 1e3, 1e6):
        vA = ratio * V_EW
        a40min = max(0.0, math.log(vA / (0.1 * V_EW)) / 2.0)            # in 1/s
        bounds.append({'v_A_over_v': ratio, 'a40_min_per_s': a40min, 'a40_min_GeV': a40min * 6.582e-25})
    out['T6'] = bounds
    ok6 = abs(bounds[2]['a40_min_per_s'] - math.log(100) / 2) < 1e-12
    rep.check('T6_ad_hoc_vacuum_before_BBN', ok6,
              'G_F,loc = 1/(sqrt2 (v^2 + A^2)) (FE-49): the weak rates of nucleosynthesis need A^2/v^2 < 0.01 at x_4 = 1 s, so '
              'a_40 > ln(v_A/(0.1 v))/(2 s): %s' % (', '.join('v_A = %g v: a_40 > %.2f /s' % (b['v_A_over_v'], b['a40_min_per_s'])
                                                             for b in bounds)))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs' / 'thermal.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=float) + '\n')
    report = {'script': 'universe_model_3/code/um3_thermal.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'thermal_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
