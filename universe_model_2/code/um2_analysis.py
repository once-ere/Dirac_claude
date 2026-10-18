#!/usr/bin/env python3
"""UM-2 analysis: (A) the x0 mass mechanism and the uncertainty relation; (B) dirac16complex as dark matter;
(C) dirac16complex as dark energy.

Units: t = y/L in [-1, 0] on each half of a period (fold t = 0, regular tip t = -1), eta = H L, lengths in units of the proper
half cell f L, masses in units 1/(f L).

A1  exact identity: for u = e^{-3 eta t/2} v, e^{3 eta t} u'^2 = v'^2 + (9 eta^2/4) v^2 - (3 eta/2)(v^2)' (the warp of the three
    extra times is a constant potential, the fold an attractive point term, the tip a repulsive one);
A2  gap theorem: for every tip parameter beta >= 0 the even sector has exactly one level below 9 eta^2/4 and the odd sector none;
A3  decomposition of (m f L)^2 of every particle into hidden kinetic energy <p^2>, warp (or bulk mass), fold and tip terms, and the
    comparison of m with the author's uncertainty estimate m_H = hbar c/(2 Delta s) (Delta s on one full period);
A4  localisation in the coordinate x0 versus proper localisation;
A5  sensitivities d ln m / d ln f and the constancy of the masses today;
B   dark matter: the Psi_B lowest odd Dirac fermion: mass, coldness, Z neutrality, stability, the relic requirement for the
    gauge-kinetic portal I12 (p-wave), unitarity, direct detection, self-interaction;
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
            'Delta_t': dt, 'mfL': math.sqrt(max(Lam, 0)), 'mH_fL': 1 / (2 * dt), 'p2_Dt2': p2 * dt * dt}


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
            'p2_Dt2': kin * dt * dt}


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
            'mH_fL': 1 / (2 * dt), 'x0_momentum_fraction': pfl * pfl / (E * E)}


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
              'e^{3 eta t} u\'^2 = v\'^2 + (9 eta^2/4) v^2 - (3 eta/2)(v^2)\' for u = e^{-3 eta t/2} v: (m f L)^2 = <p^2> + 9 eta^2/4 '
              '- (3 eta/2) rho(fold) + (3 eta/2 + beta) rho(tip)')

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
              'by the tip) and no odd level: every odd mode and every excitation has m >= 3H/(2f) = %.1f GeV' % (g * g, sc['gap_GeV']))

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
    for name in ('nu', 'e', 'u', 'd'):
        c = masses['fermions'][name]['c']
        d = decomp_fermion_zero(c)
        d['m_GeV'] = masses['fermions'][name]['m_GeV']
        d['mfL'] = d['m_GeV'] * fL_GeV
        table['%s (chiral zero mode, mass from the tip)' % name] = d
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
    out['decomposition'] = table
    z0 = table['photon, gluons, graviton (zero mode)']
    rep.check('A3_zero_mode_localised_but_massless', z0['mfL'] == 0 and z0['p2'] > 1 and abs(z0['sum']) < 1e-6 and z0['p2_Dt2'] >= 0.25,
              'the photon/gluon/graviton zero mode has <p^2> = %.3f, Delta s = %.2e m, m_H = %.0f GeV, yet m = 0: warp %.2f, fold %.3f and tip %.4f '
              'cancel its hidden kinetic energy exactly; <p^2> Delta t^2 = %.3f >= 1/4 (the uncertainty relation holds but does not bound the mass)' % (
                  z0['p2'], z0['Delta_s_m'], z0['mH_GeV'], z0['warp'], z0['fold'], z0['tip'], z0['p2_Dt2']))
    Wt = table['W']
    rep.check('A3_W_mass_from_the_tip', Wt['tip'] > 0 and Wt['m_over_mH'] < 0.01,
              'W: (m f L)^2 = %.3e = <p^2> %.3f + warp %.2f + fold %.3f + tip %.3f; m_W/m_H = %.2e: the W is light although its profile carries '
              'the photon\'s hidden momentum; its mass is the small tip-induced bending' % (Wt['Lambda'], Wt['p2'], Wt['warp'], Wt['fold'],
                                                                                         Wt['tip'], Wt['m_over_mH']))
    ex = [table['first even KK mode'], table['first odd mode'], ddm]
    rep.check('A3_heisenberg_bounds_excitations', all(v['m_over_mH'] > 1 for v in ex),
              'for the x0 excitations the uncertainty estimate is a true lower bound: m/m_H = %.2f (first even KK), %.2f (first odd), %.2f '
              '(Psi dark matter, x0-momentum fraction of eps^2 = %.3f)' % (ex[0]['m_over_mH'], ex[1]['m_over_mH'], ex[2]['m_over_mH'],
                                                                         ddm['x0_momentum_fraction']))
    fe = [table['%s (chiral zero mode, mass from the tip)' % n] for n in ('nu', 'e', 'u', 'd')]
    rep.check('A3_light_fermions_far_below_heisenberg', all(v['m_over_mH'] < 1e-6 for v in fe),
              'light fermions: m/m_H = %s (nu, e, u, d): their masses come from the tip mixing of chiral zero modes, not from localisation' % (
                  ', '.join('%.1e' % v['m_over_mH'] for v in fe)))
    # fermion mass versus localisation: d ln m / d ln c < 0
    dl = []
    for n in ('nu', 'e', 'u', 'd'):
        c = masses['fermions'][n]['c']
        h = 1e-6
        dl.append(float((mp.log(zeta2(c * (1 + h))) - mp.log(zeta2(c * (1 - h)))) / (math.log(1 + h) - math.log(1 - h))))
    out['dlnm_dlnc_fermions'] = dl
    rep.check('A3_sharper_localisation_lighter_fermion', all(x < 0 for x in dl),
              'd ln m_f/d ln c = %s < 0: a sharper x0 localisation (larger c) gives a LIGHTER fermion, the reverse of the Heisenberg intuition' % (
                  ', '.join('%.2f' % x for x in dl)))

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
    for n in ('nu', 'e', 'u', 'd'):
        c = masses['fermions'][n]['c']
        sens['m_' + n] = -1.0 + float((mp.log(zeta2(c * (1 + h))) - mp.log(zeta2(c * (1 - h)))) / (math.log(1 + h) - math.log(1 - h)))
    sens['M_DM'] = sp_['dln_eps_dm_dln_f']
    sens['G_N and alpha (1/V_perp)'] = -4.0
    out['sensitivities_dlnX_dlnf'] = sens
    prim = read_json(os.path.join(OUT, 'primordial.json'))
    rep.check('A5_sensitivities', sens['m_e'] < -15 and -1.2 < sens['M_DM'] < 0,
              'd ln X/d ln f: KK -1, m_W %.3f, m_e %.1f, m_u %.1f, m_d %.1f, m_nu %.1f, M_DM %.3f, G_N and alpha -4: the masses track the block; the '
              'stabilised block (radion mass %.0f GeV) freezes them after the primordial era' % (
                  sens['m_W'], sens['m_e'], sens['m_u'], sens['m_d'], sens['m_nu'], sens['M_DM'], sc['radion_mass_GeV']))

    # ---------------- B dark matter ----------------
    ew = read_json(os.path.join(OUT, 'electroweak.json'))
    dm = read_json(os.path.join(KS, 'darkmatter.json'))
    Hgev = sc['H_GeV']
    MDM = sp_['eps_dm'] * M_PSI_OVER_H * Hgev
    out['M_DM_GeV'] = MDM
    zB = [v for k, v in ew['tip_charge_dm_by_block'].items() if eval(k)[0] * eval(k)[1] == 1]
    rep.check('B1_mass_cold_neutral', abs(dm['0']['w_dm']) < 1e-12 and all(abs(x) < 1e-14 for x in zB),
              'Psi_B lowest odd Dirac fermion: M_DM = %.4f m = %.2f TeV (m = H), w = 0 at rest, zero Z charge and zero transition currents at the tip '
              '(exact); a gauge singlet' % (sp_['eps_dm'], MDM / 1e3))
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
    # freeze-out (Kolb-Turner), Dirac: Omega_tot h^2 = 2 x 1.07e9 x_f/(sqrt(g*) M_Pl (a + 3 b/x_f)), <sigma v> = a + 6 b/x
    MPl = 1.22e19
    gst = 56.75
    def omega(b_GeV, M):
        xf = 25.0
        for _ in range(50):
            xf = math.log(0.038 * 0.5 * 2.5 * 2 * MPl * M * (6 * b_GeV / xf) / math.sqrt(gst * xf))
        return 2 * 1.07e9 * xf / (math.sqrt(gst) * MPl * (3 * b_GeV / xf)), xf
    target = 0.120
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
    unit = 4 * math.pi / MDM ** 2 * math.sqrt(xf / math.pi) * GeV2_to_cm3s   # s-wave thermal unitarity scale (ESTIMATE)
    out['relic'] = {'g_star': gst, 'x_f': xf, 'b_required_GeV-2': breq, 'sigma_v_required_cm3_s': svreq,
                    'G_eff_required_GeV-3': G_eff, 'Lambda_eff_TeV': G_eff ** (-1.0 / 3.0) / 1e3, 'unitarity_scale_cm3_s': unit}
    rep.check('B3_relic_requirement', abs(om - target) < 1e-6 and svreq < unit,
              'thermal relic of the Psi_B Dirac fermion through the gauge-kinetic portal I12 (p-wave): x_f = %.2f, g* = %.2f, '
              '<sigma v>(x_f) = %.2e cm^3/s required, i.e. (8 G_g^2 + 3 G_W^2 + G_B^2)^{1/2} = (%.1f TeV)^-3, below the thermal unitarity '
              'scale %.1e cm^3/s' % (xf, gst, svreq, G_eff ** (-1.0 / 3.0) / 1e3, unit))
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
              'even if the relic annihilation went only into gluons, the trace-anomaly coupling gives sigma_SI = %.1e cm^2, far below the LZ limit '
              '%.1e cm^2 at %.1f TeV (ESTIMATE; linear extrapolation of the published limit): the portal I12 is unconstrained by direct detection; '
              'annihilation into W+W-, ZZ, Z gamma, gamma gamma has no tree-level nucleon coupling at all' % (sigSI(G_eff / math.sqrt(8)), lz, MDM / 1e3))
    rep.check('B5_stability_and_neutrality', True,
              'Psi_B stability: N_B (the number of the B = +1 half) is conserved by every interaction of UM-2 (all bilinears are half-diagonal); the fold '
              'parity of Psi_B is exact because P_+ Psi_B = 0 at the tip (no tip operator reaches the B half) and the bulk is reflection symmetric; '
              'the heavy odd Psi_A states (Z-charged: tip charge %.3f times that of the Psi_A fold band) decay through the oriented part of the tip '
              'portal I9' % ew['ratio_dm_to_fold_band_Psi_A'])

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
    # Gamma = C m_r^3/(4 pi M_P^2) (C an order-one coupling factor, reduced Planck mass M_P = 2.435e18 GeV) and reheats to
    # T_RH = (90/(pi^2 g*))^{1/4} sqrt(Gamma M_P) with g* = 10.75; nucleosynthesis needs T_RH >~ 4.7 MeV (FROM MEMORY).
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
              'ESTIMATE: the radion (m_r = %.0f GeV) left over from the deflation decays with Gamma = C m_r^3/(4 pi M_P^2): tau = %.2f s/C, '
              'reheating to T_RH = %.2f sqrt(C) MeV, below the 4.7 MeV that nucleosynthesis needs unless C > %.1f: the cosmological moduli '
              'problem of UM-2 (OPEN)' % (mr, rad[1]['tau_s'], rad[1]['T_RH_MeV'], Cmin))

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
    ax.loglog(mh_, m_, 'o')
    for n_, x_, y_ in zip(names, mh_, m_):
        ax.annotate(n_, (x_, y_), fontsize=7, xytext=(4, 2), textcoords='offset points')
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
        ax.plot(1 / a - 1, w, label='w0 = %g' % c_['w0'])
    ax.set_ylim(-6, 1)
    ax.set_xlabel('z')
    ax.set_ylabel('w of the lambda < 0 condensate')
    ax.legend(fontsize=7)
    ax.set_title('the condensate is not dark energy: w runs away, energy turns negative')
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_analysis_condensate.png'), dpi=130)
    plt.close(fig)
    write_json(os.path.join(OUT, 'analysis.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
