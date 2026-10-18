#!/usr/bin/env python3
"""UM-2 analysis: (A) the x0 mass mechanism and the uncertainty relation; (B) dirac16complex as dark matter;
(C) dirac16complex as dark energy.

Units: t = y/L in [-1, 0] on each half of a period (fold t = 0, regular tip t = -1), eta = H L, lengths in units of the proper
half cell f L, masses in units 1/(f L).

A1  exact identity: for u = e^{-3 eta t/2} v, e^{3 eta t} u'^2 = v'^2 + (9 eta^2/4) v^2 - (3 eta/2)(v^2)' (the warp of the three
    extra times is a constant potential, the fold an attractive point term, the tip a repulsive one);
A2  gap theorem: for every tip parameter beta >= 0 the even sector has exactly one level below 9 eta^2/4 and the odd sector none;
A3  decomposition of (m f L)^2 of every particle into hidden kinetic energy <p^2>, warp (or bulk mass), fold and tip terms, and the
    comparison of m with the author's uncertainty estimate m_H = hbar c/(2 Delta s) (Delta s on one full period); the twelve
    fermions of the three generations each consist of a doublet zero mode (c_L for leptons, c_Q for quarks) and a singlet zero
    mode (c_R), mixed at the tip;
A4  localisation in the coordinate x0 versus proper localisation;
A5  sensitivities d ln m / d ln f and the constancy of the masses today;
B   dark matter: the lowest odd Dirac fermions of the two halves Psi_A and Psi_B (degenerate; both stable since UM-2 has no tip Z
    portal): mass, coldness, neutrality, stability, the relic requirement for the gauge-kinetic portal I12 (p-wave), unitarity,
    direct detection;
C   dark energy: positive-energy Kohn-Sham states, the lambda < 0 condensate, the vacuum energy, the tuning of Lambda4.
Writes outputs/analysis.json, figures/fig_analysis_*.png, reports/analysis-checks.json.
"""
import math
import os
import sys

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import brentq

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import ETA, M_PSI_OVER_H, val  # noqa: E402

FERMIONS = ['nu1', 'nu2', 'nu3', 'e', 'mu', 'tau', 'u', 'c', 't', 'd', 's', 'b']
SECTOR = {'nu1': 'leptons', 'nu2': 'leptons', 'nu3': 'leptons', 'e': 'leptons', 'mu': 'leptons', 'tau': 'leptons',
          'u': 'quarks', 'c': 'quarks', 't': 'quarks', 'd': 'quarks', 's': 'quarks', 'b': 'quarks'}


def dlnzeta2(c, h=1e-6):
    """d ln zeta(c)^2 / d ln c (zeta^2 = tip density of the zero mode with localisation c > 0)"""
    return float((mp.log(zeta2(c * (1 + h))) - mp.log(zeta2(c * (1 - h)))) / (math.log(1 + h) - math.log(1 - h)))
from um2_spectra import boson_levels, zeta2  # noqa: E402

KS = os.path.join(OUT, 'ks')
NT = 200001
T = np.linspace(-1.0, 0.0, NT)


def trap(yv):
    return float(np.trapezoid(yv, T))


def boson_profile(Lam, eta, parity):
    """v(t) = e^{3 eta t/2} u(t) for the gauge x0 operator with eigenvalue Lam."""
    g = 1.5 * eta
    q2 = Lam - g * g
    if parity == 'even':
        if abs(q2) < 1e-14:
            return 1 + g * T
        if q2 > 0:
            q = math.sqrt(q2)
            return np.cos(q * T) + (g / q) * np.sin(q * T)
        kp = math.sqrt(-q2)
        return np.cosh(kp * T) + (g / kp) * np.sinh(kp * T)
    q = math.sqrt(q2)
    return np.sin(q * T)


def decomp_boson(Lam, beta, eta, parity):
    g = 1.5 * eta
    v = boson_profile(Lam, eta, parity)
    vp = np.gradient(v, T, edge_order=2)
    nrm = trap(v * v)
    p2 = trap(vp * vp) / nrm
    rho0 = v[-1] ** 2 / nrm
    rhot = v[0] ** 2 / nrm
    warp = g * g
    fold = -g * rho0
    tip = g * rhot + beta * rhot
    dt = math.sqrt(trap(T * T * v * v) / nrm)       # full period: symmetric about the fold, mean zero
    return {'Lambda': Lam, 'p2': p2, 'warp': warp, 'fold': fold, 'tip': tip, 'sum': p2 + warp + fold + tip,
            'Delta_t': dt, 'mfL': math.sqrt(max(Lam, 0)), 'mH_fL': 1 / (2 * dt), 'p2_Dt2': p2 * dt * dt, 'rho_tip': rhot}


def decomp_fermion_zero(c):
    # exact: rho(t) = 2c e^{2ct}/(1 - e^{-2c}) on [-1, 0]; kinetic <|chi'|^2> = c^2; bulk mass c^2; boundary -c[rho]_{-1}^{0} = -2c^2
    cm = mp.mpf(c)
    nrm = (1 - mp.exp(-2 * cm)) / (2 * cm)
    rho0 = 1 / nrm
    rhot = mp.exp(-2 * cm) / nrm
    kin = c * c
    bulk = c * c
    fold_tip = float(-cm * (rho0 - rhot))
    dt = float(mp.sqrt(mp.quad(lambda t: t * t * mp.exp(2 * cm * t), [-1, -mp.mpf(1) / (2 * cm), 0]) / nrm))
    return {'p2': kin, 'bulk': bulk, 'boundary': fold_tip, 'sum': kin + bulk + fold_tip, 'Delta_t': dt, 'mH_fL': 1 / (2 * dt),
            'p2_Dt2': kin * dt * dt, 'rho_tip': float(rhot)}


def decomp_psi_odd(c, pfl):
    """lowest odd Psi orbital in t-units: a = sin(P t), b = (c sin(P t) - P cos(P t))/E, E^2 = c^2 + P^2 (P = p f L)."""
    E = math.sqrt(c * c + pfl * pfl)
    a = np.sin(pfl * T)
    b = (c * np.sin(pfl * T) - pfl * np.cos(pfl * T)) / E
    nrm = trap(a * a + b * b)
    ap = np.gradient(a, T, edge_order=2)
    bp = np.gradient(b, T, edge_order=2)
    kin = trap(ap * ap + bp * bp) / nrm
    bulk = c * c
    bnd = -c * ((a[-1] ** 2 - b[-1] ** 2) - (a[0] ** 2 - b[0] ** 2)) / nrm
    dt = math.sqrt(trap(T * T * (a * a + b * b)) / nrm)
    return {'E2': E * E, 'p2': kin, 'bulk': bulk, 'boundary': bnd, 'sum': kin + bulk + bnd, 'Delta_t': dt, 'mfL': E,
            'mH_fL': 1 / (2 * dt), 'x0_momentum_fraction': pfl * pfl / (E * E), 'rho_tip': (a[0] ** 2 + b[0] ** 2) / nrm}


def main():
    rep = Report('analysis-checks', 'UM-2 analysis: the x0 mass mechanism and the uncertainty relation; dirac16complex as dark matter and '
                 'as dark energy')
    out = {}
    eta = ETA
    g = 1.5 * eta
    masses = read_json(os.path.join(OUT, 'masses.json'))
    sc = masses['scales']
    fL_GeV = sc['fL_GeV_inv']
    hbarc = val('hbar_c_GeV_m')

    # ---------------- A1 ----------------
    tt, et = sp.symbols('t eta', real=True)
    vf = sp.Function('v')(tt)
    uf = sp.exp(-3 * et * tt / 2) * vf
    ident = sp.simplify(sp.exp(3 * et * tt) * sp.diff(uf, tt) ** 2 - (sp.diff(vf, tt) ** 2 + sp.Rational(9, 4) * et ** 2 * vf ** 2
                                                                      - sp.Rational(3, 2) * et * sp.diff(vf ** 2, tt)))
    rep.check('A1_flat_form_identity', ident == 0,
              'with xi = y/L: e^{3 eta xi} u\'^2 = ut\'^2 + (9 eta^2/4) ut^2 - (3 eta/2)(ut^2)\' for u = e^{-3 eta xi/2} ut (the flat-measure '
              'profile ut): (m f L)^2 = <p^2> + 9 eta^2/4 - (3 eta/2) varrho(fold) + (3 eta/2 + beta) varrho(tip), varrho = ut^2/int ut^2')

    # ---------------- A2 gap theorem ----------------
    gap_ok = True
    rows = []
    for beta in (0.0, 1e-3, 1e-2, 0.1, 1.0, 10.0, 1e3, 1e6):
        ev, _ = boson_levels(eta, beta, 'even', 2)
        od, _ = boson_levels(eta, beta, 'odd', 1)
        nb_even = sum(1 for x in ev if x < g * g)
        nb_odd = sum(1 for x in od if x < g * g)
        rows.append({'beta': beta, 'even_levels': ev, 'odd_level': od[0], 'even_below_gap': nb_even, 'odd_below_gap': nb_odd})
        if nb_even != 1 or nb_odd != 0:
            gap_ok = False
    out['gap_theorem'] = rows
    rep.check('A2_gap_theorem', gap_ok, 'for beta in {0, ..., 1e6}: exactly one even level below the gap 9 eta^2/4 = %.2f (the zero mode, lifted only '
              'by the tip) and no odd level: every odd mode and every excitation of the boson operator (gauge fields, graviton) has '
              'm >= 3H/(2f) = %.1f GeV (the Dirac operator of Psi has no such gap)' % (g * g, sc['gap_GeV']))

    # ---------------- A3 decomposition ----------------
    Lam1 = masses['unbroken']['Lambda1']
    LamO = masses['unbroken']['odd'][0]
    LW, LZ = masses['WZ']['Lambda_W'], masses['WZ']['Lambda_Z']
    bW, bZ = masses['WZ']['beta_W'], masses['WZ']['beta_Z']
    table = {}
    table['photon, gluons, graviton (zero mode)'] = decomp_boson(0.0, 0.0, eta, 'even')
    table['W'] = decomp_boson(LW, bW, eta, 'even')
    table['Z'] = decomp_boson(LZ, bZ, eta, 'even')
    table['first even KK mode'] = decomp_boson(Lam1, 0.0, eta, 'even')
    table['first odd mode'] = decomp_boson(LamO, 0.0, eta, 'odd')
    sumrule = max(abs(v['sum'] - v['Lambda']) / max(1, v['Lambda']) for v in table.values())
    # chiral zero modes: one doublet zero mode per sector (common to the three generations) and one singlet zero mode per fermion;
    # each zero mode alone is massless (sum rule 0); the masses come from their mixing at the tip (um2_spectra.py)
    F = masses['fermions']
    cD = masses['doublet_c']
    table['lepton doublet zero mode (c_L = %.4f, chiral zero mode)' % cD['leptons']] = decomp_fermion_zero(cD['leptons'])
    table['quark doublet zero mode (c_Q = %.4f, chiral zero mode)' % cD['quarks']] = decomp_fermion_zero(cD['quarks'])
    for name in FERMIONS:
        table['%s singlet zero mode (c = -c_R = %.4f, chiral zero mode)' % (name, -F[name]['c_R'])] = decomp_fermion_zero(-F[name]['c_R'])
    sp_ = read_json(os.path.join(KS, 'spectrum.json'))
    cpsi = sp_['c_psi']
    dfold = decomp_fermion_zero(cpsi)
    dfold['mfL'] = 0.0
    table['Psi fold band (both halves)'] = dfold
    ddm = decomp_psi_odd(cpsi, sp_['p_dm'] * sp_['fL'])
    table['Psi lowest odd level (dark matter)'] = ddm
    fz = max(abs(v['sum']) for k, v in table.items() if 'zero mode' in k or 'fold band' in k)
    rep.check('A3_sum_rules', sumrule < 1e-6 and fz < 1e-6 and abs(ddm['sum'] - ddm['E2']) / ddm['E2'] < 1e-6,
              'the decompositions reproduce the eigenvalues: bosons to %.1e, chiral zero modes sum to %.1e (exactly 0: kinetic c^2 + bulk c^2 + '
              'boundary -2c^2), the dark-matter level to %.1e' % (sumrule, fz, abs(ddm['sum'] - ddm['E2']) / ddm['E2']))
    for k, v in table.items():
        v['m_over_mH'] = v.get('mfL', 0.0) / v['mH_fL']
        v['Delta_s_m'] = v['Delta_t'] * fL_GeV * hbarc
        v['mH_GeV'] = v['mH_fL'] / fL_GeV
    # the twelve fermions: mass against the uncertainty estimate of the broader (smaller m_H) of their two zero modes
    ferm = {}
    for name in FERMIONS:
        dL = table['%s doublet zero mode (c_%s = %.4f, chiral zero mode)' % ('lepton' if SECTOR[name] == 'leptons' else 'quark',
                                                                          'L' if SECTOR[name] == 'leptons' else 'Q', cD[SECTOR[name]])]
        dR = table['%s singlet zero mode (c = -c_R = %.4f, chiral zero mode)' % (name, -F[name]['c_R'])]
        mH = min(dL['mH_GeV'], dR['mH_GeV'])
        ferm[name] = {'m_GeV': F[name]['m_GeV'], 'c_L': F[name]['c_L'], 'c_R': F[name]['c_R'], 'mH_doublet_GeV': dL['mH_GeV'],
                      'mH_singlet_GeV': dR['mH_GeV'], 'mH_GeV': mH, 'm_over_mH': F[name]['m_GeV'] / mH}
    out['fermions_vs_uncertainty_estimate'] = ferm
    # the uncertainty relation on the cell: with rho normalised on [-1, 0], int rho dt = [t rho]_{-1}^{0} - int t rho' dt
    # = rho(tip) - int t rho' dt (the fold end t = 0 contributes nothing), and rho' = 2 v v' (bosons) or 2 Re chi^+ chi' (fermions);
    # Cauchy-Schwarz gives sqrt(<p^2>) Delta t >= (1 - rho(tip))/2, which reduces to <p^2> Delta t^2 >= 1/4 only when rho(tip) -> 0
    for k, v in table.items():
        v['p2_Dt2'] = v['p2'] * v['Delta_t'] ** 2
        v['uncertainty_lhs'] = math.sqrt(v['p2']) * v['Delta_t']
        v['uncertainty_bound'] = (1 - v['rho_tip']) / 2
    margins = {k: v['uncertainty_lhs'] - v['uncertainty_bound'] for k, v in table.items()}
    kmin = min(margins, key=margins.get)
    out['decomposition'] = table
    z0 = table['photon, gluons, graviton (zero mode)']
    fb = table['Psi fold band (both halves)']
    rep.check('A3_uncertainty_relation_on_the_cell', margins[kmin] > 0 and fb['p2_Dt2'] < 0.25 <= z0['p2_Dt2'],
              'on the cell, which ends at the tips, the uncertainty relation reads sqrt(<p^2>) Delta xi >= (1 - varrho(tip))/2 (from int varrho '
              '= varrho(tip) - int xi varrho\' dxi and the Cauchy-Schwarz inequality); it holds for every tabulated state (smallest margin %.4f, '
              '%s); <p^2> Delta xi^2 >= 1/4 is guaranteed only for profiles negligible at the tip: photon zero mode %.4f (varrho(tip) = %.5f), '
              'broad Psi fold zero mode %.4f < 1/4 (varrho(tip) = %.4f)' % (margins[kmin], kmin, z0['p2_Dt2'], z0['rho_tip'], fb['p2_Dt2'],
                                                                       fb['rho_tip']))
    rep.check('A3_zero_mode_localised_but_massless', z0['mfL'] == 0 and z0['p2'] > 1 and abs(z0['sum']) < 1e-6 and z0['p2_Dt2'] >= 0.25,
              'the photon/gluon/graviton zero mode has <p^2> = %.3f, Delta s = %.2e m, m_H = %.0f GeV, yet m = 0: warp %.2f, fold %.3f and tip %.4f '
              'cancel its hidden kinetic energy exactly; <p^2> Delta xi^2 = %.3f >= 1/4 (the uncertainty relation holds but does not bound the mass)' % (
                  z0['p2'], z0['Delta_s_m'], z0['mH_GeV'], z0['warp'], z0['fold'], z0['tip'], z0['p2_Dt2']))
    Wt = table['W']
    rep.check('A3_W_mass_from_the_tip', Wt['tip'] > 0 and Wt['m_over_mH'] < 0.01,
              'W: (m f L)^2 = %.3e = <p^2> %.3f + warp %.2f + fold %.3f + tip %.3f; m_W/m_H = %.2e: the W is light although its profile carries '
              'the photon\'s hidden momentum; its mass is the small tip-induced bending' % (Wt['Lambda'], Wt['p2'], Wt['warp'], Wt['fold'],
                                                                                         Wt['tip'], Wt['m_over_mH']))
    ex = [table['first even KK mode'], table['first odd mode'], ddm]
    rep.check('A3_heisenberg_bounds_excitations', all(v['m_over_mH'] > 1 for v in ex),
              'for the computed x0 excitations the uncertainty estimate lies below the mass: m/m_H = %.2f (first even KK), %.2f (first odd), %.2f '
              '(Psi dark matter, x0-momentum fraction of eps^2 = %.3f)' % (ex[0]['m_over_mH'], ex[1]['m_over_mH'], ex[2]['m_over_mH'],
                                                                         ddm['x0_momentum_fraction']))
    rmax = max(v['m_over_mH'] for v in ferm.values())
    rep.check('A3_fermions_far_below_heisenberg', rmax < 0.01,
              'fermions: m/m_H = %s (%s; m_H of the broader of the two zero modes, %.0f TeV for the leptons, %.0f TeV for the quarks): every '
              'fermion lies far below the uncertainty estimate, the top quark by a factor %.0f: the masses come from the tip mixing of chiral '
              'zero modes, not from localisation' % (
                  ', '.join('%.1e' % ferm[n]['m_over_mH'] for n in FERMIONS), ', '.join(FERMIONS), ferm['e']['mH_GeV'] / 1e3,
                  ferm['u']['mH_GeV'] / 1e3, 1 / ferm['t']['m_over_mH']))
    # fermion mass versus localisation: with m ~ kappa zeta(c_L) zeta(-c_R), d ln m/d ln c_L = (1/2) d ln zeta^2(c_L)/d ln c_L (doublet)
    # and d ln m/d ln(-c_R) = (1/2) d ln zeta^2(-c_R)/d ln(-c_R) (singlet)
    dl = {'lepton doublet': 0.5 * dlnzeta2(cD['leptons']), 'quark doublet': 0.5 * dlnzeta2(cD['quarks'])}
    for n in FERMIONS:
        dl[n + ' singlet'] = 0.5 * dlnzeta2(-F[n]['c_R'])
    out['dlnm_dlnc_zero_modes'] = dl
    rep.check('A3_sharper_localisation_lighter_fermion', all(x < 0 for x in dl.values()),
              'd ln m_f/d ln c = %s < 0 (lepton doublet, quark doublet, then the singlets of %s): a sharper x0 localisation (larger c) of '
              'either zero mode gives a LIGHTER fermion, the reverse of the Heisenberg intuition' % (
                  ', '.join('%.2f' % x for x in dl.values()), ', '.join(FERMIONS)))

    # ---------------- A4 coordinate localisation ----------------
    # the flat zero mode u = 1: proper weight e^{3Hy} dy; in the coordinate z = 6 H x0 (0 < z < pi/2 on one half): dy = cot z dz/(6H),
    # e^{3Hy} = (sin z)^{1/2}: density in z ~ cos z (sin z)^{-1/2}, cut at sin z >= e^{-6 eta}
    zc = math.asin(math.exp(-6 * eta))
    w_all = 2 * (1 - math.sqrt(math.sin(zc)))                 # int_zc^{pi/2} cos z sin^{-1/2} z dz = 2 [sqrt(sin z)]
    w_tip = 2 * (math.sqrt(math.sin(math.pi / 8)) - math.sqrt(math.sin(zc)))
    frac = w_tip / w_all
    out['coordinate_localisation_fraction_within_pi_over_8_of_tip'] = frac
    rep.check('A4_coordinate_vs_proper', frac > 0.5,
              'the zero mode, localised at the fold in proper length (Delta s = %.2e m), has %.1f %% of its probability within pi/8 of the TIPS in '
              'the coordinate z = 6 H x0: localisation in the coordinate x0 is chart-dependent; only the proper hidden length enters the masses' % (
                  z0['Delta_s_m'], 100 * frac))

    # ---------------- A5 sensitivities ----------------
    sens = {'KK masses and the gap 3H/(2f)': -1.0}
    h = 1e-4
    LWp = boson_levels(eta, bW * (1 + h), 'even', 1)[0][0]
    LWm = boson_levels(eta, bW * (1 - h), 'even', 1)[0][0]
    sens['m_W'] = -1.0 + 0.5 * (math.log(LWp) - math.log(LWm)) / (math.log(1 + h) - math.log(1 - h))
    # m_f = e_f/(f L) with e_f = kappa zeta(c_L) zeta(-c_R) and both localisations c = mu f L proportional to f
    for n in FERMIONS:
        sens['m_' + n] = -1.0 + 0.5 * (dlnzeta2(F[n]['c_L']) + dlnzeta2(-F[n]['c_R']))
    sens['M_DM'] = sp_['dln_eps_dm_dln_f']
    # 8 pi G_N = kappa/(G(k) V_perp) with V_perp ~ f^4 and k = 1/f^2: d ln G_N/d ln f = -4 + 2 k G'(k)/G(k);
    # the gauge couplings g^2 = ghat^2/V_perp: d ln alpha/d ln f = -4
    bgd = read_json(os.path.join(OUT, 'background.json'))['casimir_type']
    kst, Gst = bgd['k_star_value'], bgd['G_k_star_value']
    w2a, w3a = 1.0 / 32.0, 1.0 / 1152.0
    dG = -24 * w2a + 144 * w3a * kst
    sens['G_N'] = -4.0 + 2 * kst * dG / Gst
    sens['alpha and the gauge couplings (1/V_perp)'] = -4.0
    out['sensitivities_dlnX_dlnf'] = sens
    # the neutrino mass splittings measured by flavour conversion: d ln(m_j^2 - m_i^2)/d ln f = 2 (m_j^2 s_j - m_i^2 s_i)/(m_j^2 - m_i^2)
    mnu = {n: F[n]['m_GeV'] for n in ('nu1', 'nu2', 'nu3')}
    def dsplit(j, i):
        return 2 * (mnu[j] ** 2 * sens['m_' + j] - mnu[i] ** 2 * sens['m_' + i]) / (mnu[j] ** 2 - mnu[i] ** 2)
    out['neutrino_splitting_sensitivities'] = {'dln_dm2_21_dlnf': dsplit('nu2', 'nu1'), 'dln_dm2_31_dlnf': dsplit('nu3', 'nu1'),
                                               'dln_dm2_32_dlnf': dsplit('nu3', 'nu2')}
    # ESTIMATE: the light modes mix with the Kaluza-Klein excitations at relative order (m/m_KK)^2 (non-unitarity of the mixing matrices)
    out['kk_mixing_estimate'] = {n: (F[n]['m_GeV'] / sc['m_KK_GeV']) ** 2 for n in FERMIONS}
    prim = read_json(os.path.join(OUT, 'primordial.json'))
    rep.check('A5_sensitivities', sens['m_e'] < -15 and -1.2 < sens['M_DM'] < 0,
              'd ln X/d ln f: KK -1, m_W %.3f, fermions %s (%s), M_DM %.3f, alpha and the gauge couplings -4, '
              'G_N %+.3f (= -4 + 2 k* G\'(k*)/G(k*): the Lovelock factor of the 4D Newton constant also varies with the block): the masses '
              'track the block; the stabilised block (radion mass %.0f GeV) freezes them after the primordial era' % (
                  sens['m_W'], ', '.join('%.1f' % sens['m_' + n] for n in FERMIONS), ', '.join(FERMIONS), sens['M_DM'], sens['G_N'],
                  sc['radion_mass_GeV']))

    # ---------------- B dark matter ----------------
    ew = read_json(os.path.join(OUT, 'electroweak.json'))
    dm = read_json(os.path.join(KS, 'darkmatter.json'))
    Hgev = sc['H_GeV']
    MDM = sp_['eps_dm'] * M_PSI_OVER_H * Hgev
    out['M_DM_GeV'] = MDM
    zB = [v for k, v in ew['tip_charge_dm_by_block'].items() if eval(k)[0] * eval(k)[1] == 1]
    zA = [v for k, v in ew['tip_charge_dm_by_block'].items() if eval(k)[0] * eval(k)[1] == -1]
    rep.check('B1_mass_cold_neutral', abs(dm['0']['w_dm']) < 1e-12 and all(abs(x) < 1e-14 for x in zB) and min(zA) > 0.1 and
              'dropped' in ew['Z_portal']['I9'],
              'the lowest odd Dirac fermions of Psi_A and of Psi_B (the same orbital in all eight blocks: degenerate): M_DM = %.4f m = '
              '%.2f TeV (m = H), w = 0 at rest; gauge singlets; Psi_B has zero chiral tip charge and zero transition currents at the tip '
              '(exact); Psi_A has a non-zero chiral tip charge (%.3f), but UM-2 has no tip Z portal (dropped in the three-generation '
              'version, um2_electroweak.py), so neither half couples to the Z' % (sp_['eps_dm'], MDM / 1e3, min(zA)))
    # relic: p-wave from the gauge-kinetic portal I12: sigma v = (M^4 v_rel^2/pi) (8 G_g^2 + 3 G_W^2 + G_B^2)
    # verify the polarisation sum and spin trace numerically
    rng = np.random.default_rng(1)
    Mx = 1.0
    vrel = 0.3
    E = Mx / math.sqrt(1 - (vrel / 2) ** 2)
    pz = math.sqrt(E * E - Mx * Mx)
    s = 4 * E * E
    p1 = np.array([E, 0, 0, pz])
    p2 = np.array([E, 0, 0, -pz])
    metric = np.diag([1, -1, -1, -1])
    dot = lambda a, b: a @ metric @ b
    tr = 4 * (dot(p1, p2) - Mx * Mx)
    rep.check('B2_spin_trace', abs(tr - 2 * (s - 4 * Mx * Mx)) < 1e-12, 'sum over spins |vbar(p2) u(p1)|^2 = Tr[(p1slash + M)(p2slash - M)] = 2 (s - 4 M^2)')
    th = rng.uniform(0, math.pi)
    k1 = (math.sqrt(s) / 2) * np.array([1, math.sin(th), 0, math.cos(th)])
    k2 = (math.sqrt(s) / 2) * np.array([1, -math.sin(th), 0, -math.cos(th)])
    def pols(k):
        n = k[1:] / np.linalg.norm(k[1:])
        a = np.cross(n, [0, 1, 0]) if abs(n[1]) < 0.9 else np.cross(n, [1, 0, 0])
        a /= np.linalg.norm(a)
        b = np.cross(n, a)
        return [np.concatenate([[0], a]), np.concatenate([[0], b])]
    tot = 0.0
    for e1 in pols(k1):
        for e2 in pols(k2):
            amp = dot(k1, k2) * dot(e1, e2) - dot(k1, e2) * dot(k2, e1)
            tot += amp * amp
    rep.check('B2_polarisation_sum', abs(tot - 2 * dot(k1, k2) ** 2) < 1e-10,
              'sum over photon polarisations |(k1.k2)(e1.e2) - (k1.e2)(k2.e1)|^2 = 2 (k1.k2)^2 = s^2/2 (the F F vertex is 4 times the bracket)')
    # sigma v = |M|^2_avg S/(8 pi s), |M|^2_sum = G^2 (4)^2 (s^2/2) 2 (s - 4M^2) = 16 G^2 s^2 (s - 4 M^2), avg /4, S = 1/2
    # -> sigma v = G^2 s (s - 4 M^2)/(4 pi) ~ G^2 M^4 v_rel^2/pi
    sv_exact = 16 * s * s * (s - 4 * Mx * Mx) / 4 * 0.5 / (8 * math.pi * s)
    sv_nr = Mx ** 4 * vrel ** 2 / math.pi
    rep.check('B2_cross_section_formula', abs(sv_exact - s * (s - 4 * Mx * Mx) / (4 * math.pi)) < 1e-12 and abs(sv_exact / sv_nr - 1) < 0.1,
              'L = G chibar chi F F: sigma v = G^2 s (s - 4 M^2)/(4 pi) -> G^2 M^4 v_rel^2/pi (p-wave) per abelian channel; total '
              '(M^4 v^2/pi)(8 G_g^2 + 3 G_W^2 + G_B^2) for the gluon, W^a and B channels')
    # freeze-out (Kolb-Turner), Dirac: Omega_tot h^2 = 2 x 1.07e9 x_f/(sqrt(g*) M_Pl (a + 3 b/x_f)), <sigma v> = a + 6 b/x.
    # Two degenerate Dirac species (the lowest odd states of Psi_A and Psi_B) with the same I12 couplings; Psibar Psi = S_A + S_B does
    # not mix the halves, so each species freezes out separately and contributes half of the dark matter.
    # g* at T_f = M/x_f ~ 1.5 TeV: the Standard Model without a Higgs particle, three generations (right-handed neutrinos and the
    # fold bands of dirac16complex are never thermalised): 105.75
    MPl = val('M_Pl_GeV')
    gst = 105.75
    n_species = 2
    def omega(b_GeV, M):
        xf = 25.0
        for _ in range(50):
            xf = math.log(0.038 * 0.5 * 2.5 * 2 * MPl * M * (6 * b_GeV / xf) / math.sqrt(gst * xf))
        return 2 * 1.07e9 * xf / (math.sqrt(gst) * MPl * (3 * b_GeV / xf)), xf
    target_total = 0.120          # Planck 2018 omega_c (the value used in um2_cosmology.py)
    target = target_total / n_species
    lo, hi = 1e-30, 1e-5
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        om, xf = omega(mid, MDM)
        if om > target:
            lo = mid
        else:
            hi = mid
    breq = math.sqrt(lo * hi)
    om, xf = omega(breq, MDM)
    GeV2_to_cm3s = 1.1663e-17
    svreq = 6 * breq / xf * GeV2_to_cm3s
    G_eff = math.sqrt(breq * math.pi / MDM ** 4)          # equivalent single-channel coefficient (8 G_g^2 + 3 G_W^2 + G_B^2 = G_eff^2)
    unit = 4 * math.pi / MDM ** 2 * math.sqrt(xf / math.pi) * GeV2_to_cm3s   # s-wave estimate of version 1 (one helicity channel)
    # partial-wave unitarity for this operator: chibar chi F F annihilates a Dirac pair only from J = 0, P = + (3P0); for unpolarised
    # fermions sigma <= pi/(4 p^2) (p the CM momentum, p = M v/2 for v << 1), i.e. sigma v <= pi/(M^2 v); its thermal average over the
    # Maxwell-Boltzmann distribution of the relative velocity, f(v) ~ v^2 exp(-x v^2/4), is sqrt(pi x)/M^2
    from scipy.integrate import quad as _q
    fv = lambda v: v * v * math.exp(-xf * v * v / 4)
    nrm = _q(fv, 0, 60 / math.sqrt(xf))[0]
    inv_v = _q(lambda v: fv(v) / v, 0, 60 / math.sqrt(xf))[0] / nrm
    unit3P0 = math.pi / MDM ** 2 * inv_v * GeV2_to_cm3s
    unit3P0_formula = math.sqrt(math.pi * xf) / MDM ** 2 * GeV2_to_cm3s
    vc = (math.pi / (G_eff * MDM ** 3)) ** (2.0 / 3.0)      # G^2 M^4 v^2/pi = pi/(M^2 v)
    frac_vc = _q(fv, vc, 60 / math.sqrt(xf))[0] / nrm
    # for comparison: a single species carrying all the dark matter (the one-generation version, where the odd Psi_A states decayed)
    lo1, hi1 = 1e-30, 1e-5
    for _ in range(200):
        mid = math.sqrt(lo1 * hi1)
        if omega(mid, MDM)[0] > target_total:
            lo1 = mid
        else:
            hi1 = mid
    b1 = math.sqrt(lo1 * hi1)
    G1 = math.sqrt(b1 * math.pi / MDM ** 4)
    out['relic'] = {'g_star': gst, 'n_species': n_species, 'Omega_h2_per_species': om, 'Omega_h2_total': n_species * om, 'x_f': xf,
                    'b_required_GeV-2': breq, 'sigma_v_required_cm3_s': svreq, 'G_eff_required_GeV-3': G_eff,
                    'Lambda_eff_TeV': G_eff ** (-1.0 / 3.0) / 1e3, 'unitarity_scale_swave_estimate_cm3_s': unit,
                    'unitarity_bound_3P0_cm3_s': unit3P0, 'required_over_3P0_bound': svreq / unit3P0, 'v_crossing': vc,
                    'fraction_of_pairs_above_v_crossing': frac_vc, 'single_species_Lambda_eff_TeV': G1 ** (-1.0 / 3.0) / 1e3}
    rep.check('B3_relic_requirement_and_unitarity', abs(om - target) < 1e-6 and abs(unit3P0 / unit3P0_formula - 1) < 1e-6
              and abs(G_eff ** 2 * MDM ** 4 * vc ** 2 / math.pi - math.pi / (MDM ** 2 * vc)) < 1e-9 * math.pi / (MDM ** 2 * vc),
              'freeze-out formula for the two degenerate Dirac fermions (each freezing out separately through I12, p-wave, Omega h^2 = %.3f '
              'each): x_f = %.2f, g* = %.2f, <sigma v>(x_f) = %.2e cm^3/s per species, (8 G_g^2 + 3 G_W^2 + G_B^2)^{1/2} = (%.1f TeV)^-3 (a '
              'single species: (%.1f TeV)^-3). Unitarity: the operator annihilates only from 3P0 (J = 0), sigma <= pi/(4 p^2) for unpolarised '
              'Dirac fermions, whose thermal average <pi/(M^2 v)> = sqrt(pi x_f)/M^2 = %.2e cm^3/s (numerical average %.2e); the requirement '
              'exceeds it %.2f times (the s-wave estimate %.2e cm^3/s used in version 1 counted one helicity channel); the effective '
              'cross-section exceeds the bound for v > %.3f, i.e. for %.0f %% of the pairs at freeze-out: the relic cannot be produced by '
              'I12 within perturbative unitarity (OPEN)' % (
                  om, xf, gst, svreq, G_eff ** (-1.0 / 3.0) / 1e3, G1 ** (-1.0 / 3.0) / 1e3, unit3P0_formula, unit3P0,
                  svreq / unit3P0, unit, vc, 100 * frac_vc))
    # direct detection through the gluon portal only (trace anomaly): f_N = -(8 pi/9 alpha_s)... use G_g * (8 pi/9) * m_N f_TG / ...
    # sigma_SI = (4 mu^2/pi) f_N^2, f_N = G_g (16 pi/9)(m_N f_TG)/alpha_s... ESTIMATE with f_TG = 0.92 and alpha_s(2 GeV) = 0.3
    mN = 0.939
    mu = mN * MDM / (mN + MDM)
    fTG = 0.92
    alphas = 0.3
    def sigSI(Gg):
        # trace anomaly: <N| G^a G^a |N> = -(8 pi/(9 alpha_s)) m_N f_TG (three light flavours); L_eff = f_N chibar chi Nbar N,
        # sigma_SI = mu^2 f_N^2/pi (Dirac) (ESTIMATE: alpha_s and f_TG at a low scale, no running of G_g)
        fN = Gg * (8 * math.pi / (9 * alphas)) * mN * fTG
        return mu * mu / math.pi * fN * fN * 0.3894e-27
    lz = 2.2e-48 * MDM / 40.0
    Gg_max = math.sqrt(lz / sigSI(1.0))
    out['direct_detection'] = {'LZ_limit_cm2_linear_extrapolation': lz, 'sigma_SI_if_gluon_dominated_cm2': sigSI(G_eff / math.sqrt(8)),
                               'G_g_max_GeV-3': Gg_max, 'fraction_of_relic_coupling_allowed_in_gluons': (Gg_max * math.sqrt(8) / G_eff) ** 2}
    rep.check('B4_direct_detection', sigSI(G_eff / math.sqrt(8)) < lz,
              'even if the relic annihilation went only into gluons, the trace-anomaly coupling gives sigma_SI = %.1e cm^2 for each half (the two '
              'halves have the same cross-section and together the full local density, so the limit applies as for one species), far below '
              'the LZ limit '
              '%.1e cm^2 at %.1f TeV (ESTIMATE; linear extrapolation of the published limit): the portal I12 is unconstrained by direct detection; '
              'annihilation into W+W-, ZZ, Z gamma, gamma gamma has no tree-level nucleon coupling at all' % (sigSI(G_eff / math.sqrt(8)), lz, MDM / 1e3))
    # B5: which bilinears and operators preserve the halves Psi_A (B = -1) and Psi_B (B = +1)?  A term Psi^dagger X Psi (or the
    # Dirac operator acting on Psi) keeps the halves apart iff X commutes with B.  Computed with the author's matrices.
    from um2_algebra import author_gammas
    T16 = [sp.Matrix(g) for g in author_gammas()[0]]
    Cm = T16[0] * T16[1] * T16[2] * T16[3]
    Bm = -sp.I * Cm * T16[4]
    comm = lambda X: (Bm * X - X * Bm).is_zero_matrix
    acomm = lambda X: (Bm * X + X * Bm).is_zero_matrix
    cg_comm = [comm(Cm * T16[a]) for a in range(8)]
    cg_acomm = [acomm(Cm * T16[a]) for a in range(8)]
    g_comm = [comm(T16[a]) for a in range(8)]
    S_ok = all(comm(T16[a] * T16[b]) for a in range(8) for b in range(8)
               if (a <= 4 and b <= 4) or (a >= 5 and b >= 5))
    S_mix = all(acomm(T16[a] * T16[b]) for a in range(5) for b in range(5, 8))
    keeps = all(cg_comm[a] for a in range(5)) and all(cg_acomm[a] for a in range(5, 8)) and all(g_comm[a] for a in range(5)) \
        and comm(Cm) and S_ok and S_mix
    out['halves'] = {'B_commutes_with_C_gamma_a': cg_comm, 'B_anticommutes_with_C_gamma_a': cg_acomm,
                     'B_commutes_with_gamma_a': g_comm}
    rep.check('B5_stability_and_neutrality', keeps,
              'with the author\'s matrices: B commutes with C, with gamma^a and C gamma^a for a = x0..x4 and with S^ab inside {x0..x4} and '
              'inside {x5, x6, x7}, and anticommutes with gamma^a, C gamma^a for a = x5, x6, x7: in the good sector (no extra-time '
              'momenta) the Dirac operator gamma^M D_M (with gamma^M Omega_M = (3/2)(H/f) gamma^(x0) + (...) gamma^(x4)), the mass and '
              'contact terms (Psibar Psi), I11 and I12 (4D currents, Psibar Psi) all commute with B (so would a chiral tip current with '
              'P_+ = (1 - B gamma^(x0))/2), so N_A and N_B are separately conserved; extra-time momenta (outside the good sector, OPEN) '
              'would mix the halves. The bulk is reflection symmetric and UM-2 has no oriented tip operator (the tip Z portal of the '
              'one-generation version, whose oriented part let the odd Psi_A states decay, is dropped), so the fold parity is exact in '
              'both halves and the lowest odd states of Psi_A and Psi_B are both stable (their chiral tip charges would be %.3f times '
              'that of the Psi_A fold band, and 0 for Psi_B)' % ew['ratio_dm_to_fold_band_Psi_A'])

    # ---------------- C dark energy ----------------
    # Kohn-Sham states on the static block: w = P3/E
    g8 = read_json(os.path.join(KS, 'ground8.json'))
    g592 = read_json(os.path.join(KS, 'ground592.json'))
    ws = {'dark matter (lambda = 0)': dm['0']['w_dm'], 'dark matter (lambda_B)': dm['p']['w_dm'],
          'fold band gas N = 592 (lambda = 0)': g592['N592_lam0']['int_p3'] / g592['N592_lam0']['int_rho'],
          'fold band gas N = 592 (lambda_B)': g592['N592_lamp']['int_p3'] / g592['N592_lamp']['int_rho'],
          'fold band gas N = 592 (-lambda_B)': g592['N592_lamm']['int_p3'] / g592['N592_lamm']['int_rho']}
    out['w_KS_states'] = ws
    rep.check('C1_no_positive_energy_state_accelerates', all(w >= -1e-9 for w in ws.values()),
              'on the static block every computed Kohn-Sham state of Psi has w = P3/E >= 0: %s' % (', '.join('%.4f' % w for w in ws.values())))
    # condensate on the static block: S ~ a^-3, w = x/(1 + x), x = lambda S/(2m) = x0 a^-3
    cond = []
    for w0 in (-1.2, -1.0, -0.9, -0.861, -0.764, -0.5, -0.3):
        x0 = w0 / (1 - w0)
        # w(a) = x0 a^-3/(1 + x0 a^-3); CPL tangent w(a) = w0 + w_a (1 - a): w_a = -dw/da at a = 1 = 3 x0/(1 + x0)^2
        wa = 3 * x0 / (1 + x0) ** 2
        a_zero = (-x0) ** (1.0 / 3.0) if x0 < 0 else None
        cond.append({'w0': w0, 'x0': x0, 'wa_tangent': wa, 'energy_zero_at_z': (1 / a_zero - 1) if a_zero and a_zero < 1 else None})
    out['condensate'] = cond
    rep.check('C2_condensate_not_dark_energy', all(c['wa_tangent'] < -1 and c['energy_zero_at_z'] is not None and c['energy_zero_at_z'] < 1.5 for c in cond),
              'the lambda < 0 condensate tuned to w0 runs away: w0 = -1 gives w_a = %.2f and an energy density that turns negative at z = %.3f; for the '
              'Union-like w0 = -0.764: w_a = %.2f, zero at z = %.3f; the measured (w0, w_a) = (-0.861, -0.60) of the author\'s file is not reproduced' % (
                  cond[1]['wa_tangent'], cond[1]['energy_zero_at_z'], cond[4]['wa_tangent'], cond[4]['energy_zero_at_z']))
    mKK = sc['m_KK_GeV']
    rhoDE = 2.5e-47
    vac = mKK ** 4 / (16 * math.pi ** 2)
    H0 = 67.43 * 1e3 / 3.0857e22 * 6.582119569e-25        # GeV
    out['vacuum_energy'] = {'natural_GeV4': vac, 'dark_energy_GeV4': rhoDE, 'ratio': vac / rhoDE, 'H0_over_H_squared': (H0 / Hgev) ** 2}
    rep.check('C3_vacuum_energy_and_tuning', vac / rhoDE > 1e60,
              'a natural vacuum energy of the cell m_KK^4/(16 pi^2) = %.1e GeV^4 exceeds the dark-energy density by %.0e; the 4D cosmological term of UM-2 is '
              'the residual of the stabiliser balance, Lambda4/H^2 ~ (H0/H)^2 = %.1e: tuned (the cosmological-constant problem)' % (
                  vac, vac / rhoDE, (H0 / Hgev) ** 2))

    # C4: the radion left over from the primordial deflation (ESTIMATE): a Planck-suppressed modulus of mass m_r decays with
    # Gamma = C_r m_r^3/(4 pi Mbar_Pl^2) (C_r an order-one coupling factor, reduced Planck mass Mbar_Pl = 2.435e18 GeV) and reheats to
    # T_RH = (90/(pi^2 g*))^{1/4} sqrt(Gamma Mbar_Pl) with g* = 10.75; nucleosynthesis needs T_RH >~ 4.7 MeV (FROM MEMORY).
    mr = sc['radion_mass_GeV']
    MP = 2.435e18
    hbar_s = 6.582119569e-25
    rad = []
    for Cc in (0.1, 1.0, 10.0):
        Gam = Cc * mr ** 3 / (4 * math.pi * MP ** 2)
        TRH = (90 / (math.pi ** 2 * 10.75)) ** 0.25 * math.sqrt(Gam * MP)
        rad.append({'C': Cc, 'Gamma_GeV': Gam, 'tau_s': hbar_s / Gam, 'T_RH_MeV': TRH * 1e3})
    Cmin = (4.7e-3 / rad[1]['T_RH_MeV'] * 1e3) ** 2
    out['radion_decay_estimate'] = {'m_r_GeV': mr, 'cases': rad, 'C_needed_for_T_RH_4p7MeV': Cmin}
    rep.check('C4_radion_moduli_problem', rad[1]['T_RH_MeV'] < 4.7,
              'ESTIMATE: the radion (m_r = %.0f GeV) left over from the deflation decays with Gamma = C_r m_r^3/(4 pi Mbar_Pl^2) (Mbar_Pl = '
              '2.435e18 GeV, the reduced Planck mass): tau = %.2f s/C_r, reheating to T_RH = %.2f sqrt(C_r) MeV, below the 4.7 MeV that '
              'nucleosynthesis needs unless C_r > %.1f: the cosmological moduli '
              'problem of UM-2 (OPEN)' % (mr, rad[1]['tau_s'], rad[1]['T_RH_MeV'], Cmin))

    # A6: how static must the block be today?  Every mass and coupling depends on f (A5); a block rate h = f'/f today changes
    # alpha by d ln alpha/dx4 = -4 h, G_N by (d ln G_N/d ln f) h and m_e by (d ln m_e/d ln f) h.  Atomic-clock bound |d ln alpha/dx4| < 1e-17
    # per year and lunar-laser-ranging bound |d ln G_N/dx4| < 1e-13 per year (FROM MEMORY) -> bounds on |h| (ESTIMATE).
    H0_per_yr = 67.43 * 1e3 / 3.0857e22 * 3.15576e7
    h_alpha = 1e-17 / abs(sens['alpha and the gauge couplings (1/V_perp)'])
    h_G = 1e-13 / abs(sens['G_N'])
    out['block_rate_today_bound'] = {'H0_per_yr': H0_per_yr, 'h_max_from_alpha_per_yr': h_alpha, 'h_max_from_G_per_yr': h_G,
                                     'h_max_over_H0_alpha': h_alpha / H0_per_yr, 'h_max_over_H0_G': h_G / H0_per_yr,
                                     'm_e_drift_if_h_equals_H0_per_yr': abs(sens['m_e']) * H0_per_yr}
    rep.check('A6_block_frozen_today', h_alpha / H0_per_yr < 1e-6,
              'ESTIMATE: with d ln alpha/d ln f = -4 and d ln G_N/d ln f = %+.2f, the atomic-clock bound |d ln alpha/dx4| < 1e-17/yr (x4 the time) and the '
              'lunar-ranging bound |d ln G_N/dx4| < 1e-13/yr (FROM MEMORY) require |h| < %.1e/yr = %.1e H0 and |h| < %.1e/yr = %.1e H0 today; '
              'a block deflating at the Hubble rate would change m_e by %.1e per year: the extra times (and x0) must be frozen today, '
              'their exponential deflation confined to the primordial era' % (
                  sens['G_N'], h_alpha, h_alpha / H0_per_yr, h_G, h_G / H0_per_yr, abs(sens['m_e']) * H0_per_yr))

    # figures
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    names = []
    m_ = []
    mh_ = []
    for k, v in table.items():
        if v.get('mfL', 0) > 0:
            names.append(k.split(' (')[0])
            m_.append(v['mfL'] / fL_GeV)
            mh_.append(v['mH_GeV'])
    ax.loglog(mh_, m_, 'o', color='C0', label='gauge bosons, x0 excitations, dark matter')
    fn = list(ferm.keys())
    ax.loglog([ferm[n]['mH_GeV'] for n in fn], [ferm[n]['m_GeV'] for n in fn], 's', color='C3', ms=4,
              label='fermions (m_H of the broader zero mode)')
    # label placement chosen to avoid overlaps (the KK pair and the W, Z pair sit almost on top of each other)
    lab = {'first even KK mode': ('first even KK', (-62, 7)), 'first odd mode': ('first odd', (6, 7)),
           'Psi lowest odd level': ('Psi_A, Psi_B dark matter', (6, -11)), 'W': ('W+, W-', (7, -9)), 'Z': ('Z', (7, 4))}
    foff = {'u': (6, -6), 'd': (6, 3), 'c': (6, -6), 'b': (6, 2)}
    for n_, x_, y_ in zip(names, mh_, m_):
        t_, off = lab.get(n_, (n_, (4, 2)))
        ax.annotate(t_, (x_, y_), fontsize=7, xytext=off, textcoords='offset points')
    for n_ in fn:
        ax.annotate(n_, (ferm[n_]['mH_GeV'], ferm[n_]['m_GeV']), fontsize=7, xytext=foff.get(n_, (6, -2)), textcoords='offset points')
    xx = np.logspace(3.5, 6, 10)
    ax.loglog(xx, xx, 'k--', lw=0.8, label='m = hbar c/(2 Delta s)')
    ax.set_xlabel('uncertainty estimate hbar c/(2 Delta s) [GeV]')
    ax.set_ylabel('actual mass [GeV]')
    ax.legend(fontsize=8)
    ax.set_title('x0 mass mechanism: excitations above the line, light masses far below')
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_analysis_heisenberg.png'), dpi=130)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(7, 4))
    a = np.linspace(0.5, 1.0, 200)
    for c_ in cond:
        x0 = c_['x0']
        w = x0 * a ** -3 / (1 + x0 * a ** -3)
        w = np.where(np.abs(w) > 50, np.nan, w)          # w diverges where the energy density crosses zero
        ax.plot(1 / a - 1, w, label='w0 = %g' % c_['w0'])
    ax.set_ylim(-6, 1)
    ax.set_xlabel('z')
    ax.set_ylabel('w of the lambda < 0 condensate')
    ax.legend(fontsize=7)
    ax.set_title('the condensate is not dark energy: w runs away (energy density crosses zero)')
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_analysis_condensate.png'), dpi=130)
    plt.close(fig)
    write_json(os.path.join(OUT, 'analysis.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
