#!/usr/bin/env python3
"""UM-2 coupled solution (version 3, 2026-10-18): Kohn-Sham theory for dirac16complex coupled to gravity and to every
Standard-Model field, solved self-consistently in representative environments.

Conventions (as in um2_ks_jobs.py; H = 1 in the Kohn-Sham units): an orbital (a, b) of h_j is normalised on one half of
the cell, int_{-L}^{0} (a^2 + b^2) dy = 1; a 4D particle of density n (per 3-volume) in an orbital or zero mode with the
normalised profile rho(y) (int_{-L}^{0} rho dy = 1) has the 8D proper density n rho(y) e^{-3Hy}/(2 f^4 v_t) on each half of
the period (proper transverse volume element f^4 e^{3Hy} dy d^3x_t, two halves).  The 8D contact interaction
(c_V/Lambda*^6)(i Psibar gamma^M Psi)(i psibar gamma_M psi) then gives the 4D coupling between a Psi state o and a
Standard-Model chirality component f
    G_of = G_V q_f Itilde_of,   Itilde_of = int_{-L}^{0} (a_o^2 + b_o^2) rho_f(y) e^{-3Hy} dy   (in units of H),
    G_V = c_V H/(2 f^4 v_t Lambda*^6)   (the 4D strength of I11, a GeV^-2 parameter),
and Itilde_of is exactly the response d eps_o/de of the Kohn-Sham level to the mean field v(y) = e rho_f(y) e^{-3Hy}.

C1  Overlaps Itilde_of of the dark-matter level, the fold band and the first even bulk level with the zero modes of every
    Standard-Model multiplet of three generations (doublets Q, L; singlets u_R, c_R, t_R, d_R, s_R, b_R, e_R, mu_R, tau_R,
    nu_R1, nu_R2, nu_R3); checked against full self-consistent Kohn-Sham solutions at finite amplitude (Richardson in the
    amplitude); the screened response of the dark-matter level in the interacting state (benchmark self-coupling).
C2  I11 with the B - L charges (quarks 1/3, leptons -1): the freeze-in of the fold bands, f fbar -> Psi_fold Psibar_fold,
    sigma = G^2 s/(12 pi) per Dirac pair, from the Standard-Model plasma below T_max: Delta N_eff(G_V, T_max); the benchmark
    G_V for Delta N_eff = 1e-3 at T_max = 10 TeV (ASSUMED); the fold bands are never in equilibrium (Gamma/H << 1).
C3  Direct detection through I11: coherent vector coupling to the quarks of the nucleus, against the LZ limit.
C8  The x0-chiral vector portal I13, (c_A/Lambda*^6) sum_{M != x0} (i Psibar gamma^M P_b Psi) J^B_M with P_b = (1 - gamma^(x0))/2
    and the baryon-number current J^B_M = (1/3) sum_i sum_{Q_i, u_Ri, d_Ri} i psibar gamma_M psi (the sum runs over the seven
    directions M = x1, ..., x7: for M = x0 the bilinear would not be Hermitian, (i C gamma^(x0) P_b)^dagger = i C gamma^(x0) P_a): the
    bilinear is Hermitian and a 4D vector (P_a gamma^M = gamma^M P_b for M != x0, C P_b C^-1 = P_a; checked with the author's
    matrices, together with the B structure of its components) and vanishes identically on the fold band (b = 0); its overlaps
    Itilde^(b)_of = int b_o^2 rho_f e^{-3Hy} dy (checked by self-consistent Kohn-Sham solutions with a b-component potential); the
    s-wave annihilation chi chibar -> q qbar (3S1), the relic of the two species together with the unitarity-safe I12 benchmark
    (numerical Boltzmann equation, exact thermal averages), the J = 1 unitarity bound sigma <= 3 pi/(4 p^2), and direct detection.
C9  Why I13 couples to J^B and not to J^(B-L): with the B - L current the annihilation chi chibar <-> nu_R nubar_R would bring the
    three right-handed neutrinos into equilibrium above the dark-matter freeze-out (number-changing and elastic rates against the
    Hubble rate, Boltzmann equation for nu_R from zero abundance), and they would decouple as three thermal Weyl species with
    Delta N_eff = 3 (10.75/g_s)^(4/3) F_h, about 0.14, in tension with ACT DR6; with J^B they are never thermalised (their
    production through I11 is computed and compared with the I13 annihilation rate).
C10 The self-interaction channel: -(lambda/2)(Psibar Psi)^2 couples the dark matter to the fold bands through the transition
    scalar density s_DF = a_D b_F + b_D a_F (even under the fold reflection when squared), with the 4D strength
    G_lambda = lambda H Itilde_lambda/(2 f^4 v_t), Itilde_lambda = int s_DF^2 e^{-3Hy} dy; the annihilation chi chibar -> fold pairs
    (ESTIMATE of the s-wave cross-section) would thermalise the fold bands for large G_lambda; the bound on G_lambda for
    Delta N_eff <= 1e-3 from this channel, and what it means for lambda/v_t (the Kohn-Sham benchmark lambda_B is a numerical value).
C4  The Standard-Model fields acting on Psi (mean fields of the Kohn-Sham equations) in environments: I11 from the B - L
    densities of quarks and electrons (each chirality with its own x0 profile), I12 from the gauge condensates (the QCD
    vacuum condensate, the thermal QCD interaction measure, the thermal W and Z condensates: the free massive-vector part
    <F^2> = -2(rho - 3p) and the O(alpha) interaction part <g^2 F^2> = 4 g^2 p_2 by the Feynman-Hellmann theorem).
C5  Psi acting on the Standard-Model fields: the I12 shift of the gauge kinetic functions by the scalar density of the
    dark matter (delta alpha_i/alpha_i = -4 G_i n_DM), the W and Z masses from the x0 eigenvalue problem with the
    y-dependent kinetic function (perturbative and direct finite elements); the photon stays massless.
C6  Gravity: the full adiabatic block response dk = (c_rho kappa drho + c_3 kappa dp3 + c_p kappa dpbar)/H^2 (background.json) to every
    species: the plasma (ideal gases with the x0 masses, the QCD interaction measure, the O(alpha) electroweak pressure), the net
    nucleons and electrons (degenerate Fermi gases at T = 0) and the dark matter, with the hidden pressure pbar = (1/4) dp/d ln f
    (masses: -(rho - 3p) d ln m/d ln f; QCD: -(rho - 3p)_QCD d ln Lambda/d ln f; electroweak: p_2 d ln alpha/d ln f); the induced
    mass shifts, the gain of the loop mass -> source -> block -> mass, and the iteration.
C7  The domain of validity of the coupled effective description.
Writes outputs/coupled.json, figures/fig_coupled.png and reports/coupled-checks.json.
"""
import math
import os
import sys

import numpy as np
from scipy.linalg import eigh
from scipy.special import kn

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import ETA, M_PSI_OVER_H, val  # noqa: E402
from um2_kohnsham import Cell, KSState  # noqa: E402
from um2_thermal import Cosmo, gas, omega_h2, rate_fraction_above, relic, sigma_I12, sigma_unitarity, sigmav_thermal, species  # noqa: E402

H = 1.0
L = ETA / H
DK = 0.25
VT = 1.0
LAM_B = 7.0e-5
HBARC_CM = None   # set in main
GEV2_CM2 = 0.389379e-27


def sm_profile(c, y):
    return (2 * c / L) * np.exp(2 * c * y / L) / (1 - math.exp(-2 * c))


def vol7(f):
    return (2 * math.pi / DK) ** 3 * VT * f ** 4


def fixed_dm(nq_per_j=4):
    def sel(secs):
        out = []
        for si, s in enumerate(secs):
            if s['n2'] != 0:
                continue
            if s['parity'] == 'even':
                out.append((si, s['nneg'], s['g']))
            else:
                out.append((si, s['nneg'], nq_per_j))
        return out
    return sel


def free_orbital(c, j, parity, rank):
    """The rank-th particle orbital (a, b) of the free problem (lambda = 0, no fields) at k = 0 in block j."""
    bs = c.basis[(j, parity)]
    E = bs['E']
    idx = bs['nneg'] + rank
    return bs['A'][idx], bs['B'][idx], float(E[idx])


def level_energy(st, j, parity, n2=0, rank=0):
    for s in st.secs:
        if s['n2'] == n2 and s['parity'] == parity and s['j'] == j:
            return float(s['eps'][s['nneg'] + rank])
    raise KeyError


# ----------------------------------------------------------------------------------------------------------------------
def boson_fem_K(eta, beta, Kfun, ne=300):
    """Lowest eigenvalue of -(1/(K e^{3 eta t}))(K e^{3 eta t} u')' = Lambda u (t = y/L in [-1, 0]), u'(0) = 0, tip Robin
    K(-1) u'(-1) = beta u(-1) (the tip term is not multiplied by K): quadratic finite elements, Rayleigh quotient."""
    nodes = np.linspace(-1.0, 0.0, 2 * ne + 1)
    n = len(nodes)
    Km = np.zeros((n, n))
    Mm = np.zeros((n, n))
    xg, wg = np.polynomial.legendre.leggauss(6)
    for e in range(ne):
        idx = [2 * e, 2 * e + 1, 2 * e + 2]
        a, b = nodes[idx[0]], nodes[idx[2]]
        hl = b - a
        for xi, wi in zip(xg, wg):
            s = (xi + 1) / 2
            t = a + s * hl
            N = np.array([2 * (s - 0.5) * (s - 1), -4 * s * (s - 1), 2 * s * (s - 0.5)])
            dN = np.array([4 * s - 3, -8 * s + 4, 4 * s - 1]) / hl
            wt = math.exp(3 * eta * t) * Kfun(t) * wi * hl / 2
            Km[np.ix_(idx, idx)] += wt * np.outer(dN, dN)
            Mm[np.ix_(idx, idx)] += wt * np.outer(N, N)
    Km[0, 0] += beta * math.exp(-3 * eta)
    ev, vec = eigh(Km, Mm)
    u = vec[:, 0]
    num = float(u @ Km @ u)
    den = float(u @ Mm @ u)
    return num / den, nodes, u


def main():
    global HBARC_CM
    rep = Report('coupled-checks', 'UM-2 coupled solution: Kohn-Sham theory for dirac16complex coupled to gravity and to every '
                 'Standard-Model field, in environments from the laboratory to neutron stars and the early Universe')
    out = {}
    HBARC_CM = val('hbar_c_GeV_m') * 100.0
    cm3 = HBARC_CM ** 3                       # GeV^3 per cm^-3: n[GeV^3] = n[cm^-3] * cm3
    masses = read_json(os.path.join(OUT, 'masses.json'))
    bg = read_json(os.path.join(OUT, 'background.json'))
    spec = read_json(os.path.join(OUT, 'ks', 'spectrum.json'))
    ana = read_json(os.path.join(OUT, 'analysis.json'))
    th = read_json(os.path.join(OUT, 'thermal.json'))
    f = bg['casimir_type']['f_star']
    kst = bg['casimir_type']['k_star_value']
    krho = bg['casimir_type']['kappa_rho_b_over_H2']
    Gk = bg['casimir_type']['G_k_star_value']
    HG = masses['scales']['H_GeV']
    F = masses['fermions']
    cL = masses['doublet_c']['leptons']
    cQ = masses['doublet_c']['quarks']
    MDM = spec['eps_dm'] * M_PSI_OVER_H * HG
    O = 0.7072        # d eps_DM/dm for a uniform mass shift (um2_ks_jobs.py portals: 0.707196)

    # ---------------- C1 overlaps ----------------
    nb = 80
    c = Cell(f=f, L=L, H=H, m=M_PSI_OVER_H, nb=nb, nq=10 * nb)
    y = c.y
    w = c.wq
    orb = {'dark matter (lowest odd level)': free_orbital(c, 1, 'odd', 0),
           'fold band (zero mode)': free_orbital(c, 1, 'even', 0),
           'first even bulk level': free_orbital(c, 1, 'even', 1)}
    zero_modes = {'Q (quark doublets)': cQ, 'L (lepton doublets)': cL}
    for n_ in ('u', 'c', 't', 'd', 's', 'b', 'e', 'mu', 'tau', 'nu1', 'nu2', 'nu3'):
        zero_modes['%s_R' % n_] = -F[n_]['c_R']
    I = {}
    for on, (a, b, eo) in orb.items():
        I[on] = {}
        for zn, cz in zero_modes.items():
            I[on][zn] = float(np.sum(w * (a * a + b * b) * sm_profile(cz, y) * np.exp(-3 * H * y)))
    out['overlaps_Itilde'] = I
    Ib = {}
    for on, (a, b, eo) in orb.items():
        Ib[on] = {}
        for zn, cz in zero_modes.items():
            Ib[on][zn] = float(np.sum(w * (b * b) * sm_profile(cz, y) * np.exp(-3 * H * y)))
    out['overlaps_Itilde_b'] = Ib
    out['orbital_energies_over_H'] = {k: v[2] for k, v in orb.items()}
    # finite-amplitude check: full self-consistent Kohn-Sham solutions with v = e rho_f e^{-3Hy} (dark matter in the N = 16 state)
    checks = []
    for zn in ('Q (quark doublets)', 'e_R', 'L (lepton doublets)'):
        shp = sm_profile(zero_modes[zn], y) * np.exp(-3 * H * y)
        eps = {}
        for e in (-2e-4, -1e-4, 1e-4, 2e-4):
            st = KSState(c, dk=DK, N=16, lam=0.0, n2max=4, vol7=vol7(f), fixed=fixed_dm(4), ext_v=e * shp).scf()
            eps[e] = level_energy(st, 1, 'odd')
        d1 = (eps[1e-4] - eps[-1e-4]) / 2e-4
        d2 = (eps[2e-4] - eps[-2e-4]) / 4e-4
        rich = (4 * d1 - d2) / 3
        checks.append((zn, rich, I['dark matter (lowest odd level)'][zn]))
    out['overlap_checks_finite_amplitude'] = [{'zero_mode': a, 'finite_difference': b, 'overlap': c_} for a, b, c_ in checks]
    dev = max(abs(b / c_ - 1) for a, b, c_ in checks)
    rep.check('C1_overlaps', dev < 1e-8,
              'the overlap Itilde = int (a^2 + b^2) rho_f e^{-3Hy} dy of the dark-matter level with the Standard-Model zero modes equals '
              'the derivative of the self-consistent Kohn-Sham level with respect to the I11 amplitude (finite differences at 1e-4 and '
              '2e-4, Richardson) to %.1e: Q %.6f, e_R %.6f, L %.6f; fold band: Q %.6f, L %.6f, e_R %.4e' % (
                  dev, I['dark matter (lowest odd level)']['Q (quark doublets)'], I['dark matter (lowest odd level)']['e_R'],
                  I['dark matter (lowest odd level)']['L (lepton doublets)'], I['fold band (zero mode)']['Q (quark doublets)'],
                  I['fold band (zero mode)']['L (lepton doublets)'], I['fold band (zero mode)']['e_R']))
    # screened response in the interacting state (N = 8 fold zero modes + 8 dark-matter quanta, lambda_B)
    shp = sm_profile(cQ, y) * np.exp(-3 * H * y)
    epsS = {}
    for e in (-1e-4, 1e-4):
        st = KSState(c, dk=DK, N=16, lam=LAM_B, n2max=4, vol7=vol7(f), fixed=fixed_dm(4), ext_v=e * shp).scf(tol=1e-13, mix=0.5)
        epsS[e] = level_energy(st, 1, 'odd')
    screened = (epsS[1e-4] - epsS[-1e-4]) / 2e-4
    out['screened_response_Q'] = {'interacting': screened, 'bare': I['dark matter (lowest odd level)']['Q (quark doublets)']}
    rep.check('C1_screened_response', abs(screened / I['dark matter (lowest odd level)']['Q (quark doublets)'] - 1) < 0.05,
              'in the interacting Kohn-Sham state (8 fold zero modes and 8 dark-matter quanta, lambda_B) the response of the dark-matter '
              'level to the quark-doublet I11 field is %.6f against the bare overlap %.6f (relative %.2e): the self-consistent '
              'screening by the Psi gas is small' % (screened, I['dark matter (lowest odd level)']['Q (quark doublets)'],
                                                     screened / I['dark matter (lowest odd level)']['Q (quark doublets)'] - 1))
    # the fold band stays massless under every I11 field (exact: chi = (e^{f int M dy}, 0) for any M; v shifts all levels rigidly
    # at k = 0 only through its expectation value, which for the zero mode is the overlap)
    shp = sm_profile(cL, y) * np.exp(-3 * H * y)
    gaps = {}
    disp = {}
    for e in (-1e-3, 0.0, 1e-3):
        st = KSState(c, dk=DK, N=16, lam=0.0, n2max=4, vol7=vol7(f), fixed=fixed_dm(4), ext_v=e * shp).scf()
        e0 = level_energy(st, 1, 'even', 0)
        e1 = level_energy(st, 1, 'even', 1)
        e4 = level_energy(st, 1, 'even', 4)
        gaps[e] = e1 - e0
        disp[e] = (e4 - e0) / (e1 - e0)
    lin = (gaps[1e-3] - gaps[-1e-3]) / 2e-3
    quad2 = (gaps[1e-3] + gaps[-1e-3] - 2 * gaps[0.0]) / (1e-3) ** 2
    out['fold_band_under_I11'] = {'d_gap_de_linear': lin, 'd2_gap_de2': quad2, 'dispersion_ratio_k2_over_k1': disp}
    rep.check('C1_fold_band_massless', abs(lin) < 1e-6 and all(abs(v - 2.0) < 1e-6 for v in disp.values()),
              'with the lepton-doublet I11 field the spacing between the k = 0 fold zero mode and the first momentum shell changes by '
              '%.1e per unit amplitude at first order (second order %.3f e^2, a change of the group velocity: the ratio of the energies of '
              'the shells |k| = 2 dk and dk above the zero mode stays %s, i.e. the dispersion stays linear); at the physical amplitudes '
              '(below 1e-40 in these units) the fold band is massless' % (lin, quad2, ', '.join('%.9f' % v for v in disp.values())))

    # ---------------- C2 freeze-in of the fold bands through I11 (B - L) ----------------
    Ifold = I['fold band (zero mode)']
    # Weyl components: (overlap of the chirality profile, B-L charge, multiplicity N_c x components)
    comps = []
    for gen, (uq, dq, lq, nq) in enumerate([('u', 'd', 'e', 'nu1'), ('c', 's', 'mu', 'nu2'), ('t', 'b', 'tau', 'nu3')]):
        comps.append(('Q%d' % (gen + 1), Ifold['Q (quark doublets)'], 1 / 3., 6))
        comps.append((uq + '_R', Ifold[uq + '_R'], 1 / 3., 3))
        comps.append((dq + '_R', Ifold[dq + '_R'], 1 / 3., 3))
        comps.append(('L%d' % (gen + 1), Ifold['L (lepton doublets)'], -1.0, 2))
        comps.append((lq + '_R', Ifold[lq + '_R'], -1.0, 1))
        # nu_R: never in the plasma
    Sfi = sum(mult * (q * It) ** 2 for (_, It, q, mult) in comps)     # sum N_c (q Itilde)^2 over Weyl components
    Nchi = 2          # the fold bands of Psi_A and Psi_B: two massless Dirac fermions
    # MB rates: gamma = (4/pi^5) N_chi Sfi G_V^2 T^8 (pairs per volume and time), energy rate P = 8 T gamma
    # check the Bessel moments: int_0^inf x^6 K1 = 384, int x^7 K2 = 3072
    from scipy.integrate import quad
    m6 = quad(lambda x: x ** 6 * kn(1, x), 0, 200, limit=400)[0]
    m7 = quad(lambda x: x ** 7 * kn(2, x), 0, 200, limit=400)[0]
    MPl = val('M_Pl_GeV')
    curve = th['g_star_curve']
    lnT = np.log(curve['T_GeV'])
    grho = np.array(curve['g_rho'])
    gsv = np.array(curve['g_s'])

    def g_of(T):
        lt = math.log(T)
        return float(np.interp(lt, lnT, grho)), float(np.interp(lt, lnT, gsv))

    def dNeff(GV, Tmax, Tend=1.0):
        """Delta N_eff of the fold-band quanta produced by freeze-in from Tmax: integrate d(rho a^4)/dT with a ~ g_s^(-1/3)/T."""
        Ts = np.logspace(math.log10(Tend), math.log10(Tmax), 600)
        acc = 0.0
        prev = None
        for T in Ts[::-1]:
            gr, gs = g_of(T)
            Hh = math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / MPl
            Prate = 8 * T * (4 / math.pi ** 5) * Nchi * Sfi * GV ** 2 * T ** 8
            a4 = (gs ** (-1 / 3.) / T) ** 4
            val_ = Prate * a4 / (Hh * T)          # d(rho a^4) / d ln(1/T) ~ ... (dt = -dT/(H T))
            if prev is not None:
                acc += 0.5 * (val_ + prev[1]) * (prev[0] - T)
            prev = (T, val_)
        # late time: rho_fold = acc/a^4, a = gs0^(-1/3)/T0 ; rho_nu (one flavour) = (7/8)(pi^2/15) T_nu^4, T_nu = (4/11)^(1/3) T0
        gs0 = th['today']['g_s']
        T0 = 1.0
        rho_fold = acc / (gs0 ** (-1 / 3.) / T0) ** 4
        rho_nu1 = 7 / 8 * math.pi ** 2 / 15 * ((4 / 11) ** (1 / 3.) * T0) ** 4
        return rho_fold / rho_nu1

    Tmax_b = 1.0e4
    dN1 = dNeff(1.0, Tmax_b)               # Delta N_eff per G_V^2 (G_V in GeV^-2)
    GVb = math.sqrt(1e-3 / dN1)
    tab = {}
    for Tm in (2e3, 5e3, 1e4, 2e4):
        tab['%.0f GeV' % Tm] = dNeff(GVb, Tm)
    # equilibrium test at T_max: Gamma_fold = (production rate per fold quantum in equilibrium) vs H
    gr, gs = g_of(Tmax_b)
    neq_fold = Nchi * 4 * 3 * 1.2020569 / (4 * math.pi ** 2) * Tmax_b ** 3      # 2 Dirac x 4 dof x (3/4) zeta(3) T^3/pi^2
    gam = (4 / math.pi ** 5) * Nchi * Sfi * GVb ** 2 * Tmax_b ** 8
    Hmax = math.sqrt(8 * math.pi ** 3 * gr / 90) * Tmax_b ** 2 / MPl
    ratio = 2 * gam / neq_fold / Hmax
    out['freeze_in'] = {'sum_Nc_q2_I2': Sfi, 'components': [{'name': a, 'Itilde': b, 'q': q, 'mult': m_} for (a, b, q, m_) in comps],
                        'Bessel_x6K1': m6, 'Bessel_x7K2': m7, 'Delta_Neff_per_GV2': dN1, 'T_max_GeV': Tmax_b,
                        'G_V_benchmark_GeV-2': GVb, 'Delta_Neff_vs_Tmax': tab, 'Gamma_over_H_at_Tmax': ratio}
    rep.check('C2_freeze_in_benchmark', abs(m6 - 384) < 1e-6 and abs(m7 - 3072) < 1e-5 and ratio < 0.05,
              'f fbar -> Psi_fold Psibar_fold through I11 (B - L): gamma = (4/pi^5) N_chi sum N_c (q Itilde)^2 G_V^2 T^8 (Maxwell-Boltzmann; '
              'Bessel moments 384 and 3072 checked), each pair carrying 8T; sum N_c (q Itilde)^2 = %.4e over the Weyl components of three '
              'generations; Delta N_eff = %.3e G_V^2 GeV^4 for T_max = 10 TeV, so the benchmark Delta N_eff = 1e-3 means G_V = %.3e GeV^-2 '
              '(%.1e G_F); Delta N_eff = %s for T_max = 2, 5, 10, 20 TeV; at T_max the production rate per fold quantum is %.1e of the Hubble '
              'rate: the fold bands are never in equilibrium' % (
                  Sfi, dN1, GVb, GVb / val('G_F_GeV-2'), ', '.join('%.2e' % v for v in tab.values()), ratio))

    # ---------------- C3 direct detection through I11 ----------------
    Idm = I['dark matter (lowest odd level)']
    Gu = GVb * (1 / 3.) * 0.5 * (Idm['Q (quark doublets)'] + Idm['u_R'])
    Gd = GVb * (1 / 3.) * 0.5 * (Idm['Q (quark doublets)'] + Idm['d_R'])
    fp, fn = 2 * Gu + Gd, Gu + 2 * Gd
    Z, A = 54, 131
    fN = (Z * fp + (A - Z) * fn) / A
    mN = 0.9389
    mu_n = MDM * mN / (MDM + mN)
    sig_n = mu_n ** 2 * fN ** 2 / math.pi * GEV2_CM2
    lz = ana['direct_detection']['LZ_limit_cm2_linear_extrapolation']
    out['direct_detection_I11'] = {'G_u_GeV-2': Gu, 'G_d_GeV-2': Gd, 'f_p': fp, 'f_n': fn, 'sigma_n_cm2': sig_n, 'LZ_cm2': lz}
    rep.check('C3_direct_detection_I11', sig_n < 1e-6 * lz,
              'the benchmark I11 couples the dark matter coherently to the quark vector currents (f_p = 2 G_u + G_d = %.3e GeV^-2, '
              'f_n = %.3e GeV^-2): sigma_n = mu^2 f^2/pi = %.1e cm^2 for xenon, against the LZ limit %.1e cm^2' % (fp, fn, sig_n, lz))

    # ---------------- C8 the x0-chiral vector portal I13 ----------------
    # (0) the bilinear i Psibar gamma^M P_b Psi = Psi^dagger (i C gamma^M P_b) Psi with the author's 16 x 16 matrices (exact sympy):
    # Hermitian for M = x1..x7, not for M = x0 ((i C g0 P_b)^dagger = i C g0 P_a); C P_b C^-1 = P_a; P_b commutes with the 4D Lorentz
    # generators; C gamma^M P_b commutes with B for M = x1..x4 and anticommutes for M = x5, x6, x7; the extra-time components
    # Psi^dagger C gamma^M Psi (M = x5, x6, x7) vanish for every spinor in one half B = -1 or B = +1 (Q C gamma^M Q = 0 with the
    # projectors Q = (1 -+ B)/2), so the extra-time currents J^B_(x5,6,7) vanish on the Standard-Model zero modes (all in B = -1).
    import sympy as sp
    from um2_algebra import author_gammas
    T16 = [sp.Matrix(g_) for g_ in author_gammas()[0]]
    I16 = sp.eye(16)
    Cm = T16[0] * T16[1] * T16[2] * T16[3]
    Bm = -sp.I * Cm * T16[4]
    Pa_ = (I16 + T16[0]) / 2
    Pb_ = (I16 - T16[0]) / 2
    zero = lambda X: X.applyfunc(sp.expand).is_zero_matrix
    herm = [zero((sp.I * Cm * T16[M] * Pb_).H - sp.I * Cm * T16[M] * Pb_) for M in range(8)]
    x0_conj = zero((sp.I * Cm * T16[0] * Pb_).H - sp.I * Cm * T16[0] * Pa_)
    b_comm = [zero(Bm * Cm * T16[M] * Pb_ - Cm * T16[M] * Pb_ * Bm) for M in range(8)]
    b_acomm = [zero(Bm * Cm * T16[M] * Pb_ + Cm * T16[M] * Pb_ * Bm) for M in range(8)]
    lorentz_ok = all(zero(T16[a_] * T16[b_] * Pb_ - Pb_ * T16[a_] * T16[b_]) for a_ in range(1, 5) for b_ in range(1, 5))
    cpc = zero(Cm * Pb_ * Cm.inv() - Pa_)
    QA, QB = (I16 - Bm) / 2, (I16 + Bm) / 2
    extra_time_zero = all(zero(Q_ * Cm * T16[M] * Q_) for Q_ in (QA, QB) for M in (5, 6, 7))
    alg_ok = (herm == [False] + [True] * 7 and x0_conj and all(b_comm[1:5]) and all(b_acomm[5:8]) and lorentz_ok and cpc
              and extra_time_zero)
    out['I13_algebra'] = {'hermitian_x0_to_x7': herm, 'x0_component_conjugate_is_P_a': x0_conj, 'B_commutes_x0_to_x7': b_comm,
                          'B_anticommutes_x0_to_x7': b_acomm, 'P_b_commutes_with_4D_Lorentz': lorentz_ok, 'C_Pb_Cinv_equals_Pa': cpc,
                          'extra_time_currents_vanish_in_each_half': extra_time_zero}
    rep.check('C8_I13_algebra', alg_ok,
              'with the author\'s matrices (exact): i C gamma^M P_b is Hermitian for M = x1, ..., x7 and not for M = x0, where '
              '(i C gamma^(x0) P_b)^dagger = i C gamma^(x0) P_a (so the action sums over M != x0); C P_b C^-1 = P_a; P_b commutes with the 4D '
              'Lorentz generators gamma^mu gamma^nu (the components mu = x1..x4 form a 4D vector); C gamma^M P_b commutes with B for '
              'M = x1..x4 and anticommutes for M = x5, x6, x7; Q C gamma^M Q = 0 for M = x5, x6, x7 and Q = (1 - B)/2, (1 + B)/2: the '
              'extra-time currents vanish for spinors in one half, in particular J^B_(x5,6,7) on the Standard-Model zero modes (B = -1), '
              'so I13 does not mix Psi_A and Psi_B on the zero modes')

    # (a) algebra in block form: gamma^(x0) = sigma3 in every block (um2_algebra.py), so P_b = (1 - sigma3)/2 projects on the
    # b-component; the fold zero modes are (e^{f m y}, 0): P_b Psi_fold = 0 identically.  The Kohn-Sham check: a potential acting
    # on the b-component only shifts the dark-matter level by Itilde^(b) and leaves every fold-band level unchanged.
    IbD = Ib['dark matter (lowest odd level)']
    chk = []
    for zn in ('Q (quark doublets)', 'L (lepton doublets)', 'u_R'):
        shp = sm_profile(zero_modes[zn], y) * np.exp(-3 * H * y)
        epsd = {}
        foldd = {}
        for e in (-2e-4, -1e-4, 1e-4, 2e-4):
            st = KSState(c, dk=DK, N=16, lam=0.0, n2max=4, vol7=vol7(f), fixed=fixed_dm(4), ext_vb=e * shp).scf()
            epsd[e] = level_energy(st, 1, 'odd')
            foldd[e] = (level_energy(st, 1, 'even', 0, 0), level_energy(st, 1, 'even', 1, 0))
        d1 = (epsd[1e-4] - epsd[-1e-4]) / 2e-4
        d2 = (epsd[2e-4] - epsd[-2e-4]) / 4e-4
        rich = (4 * d1 - d2) / 3
        fshift = max(abs(foldd[e][0]) + abs(foldd[e][1] - foldd[-e][1]) for e in (1e-4, 2e-4))
        chk.append((zn, rich, IbD[zn], fshift))
    devb = max(abs(r / i_ - 1) for (_, r, i_, _) in chk)
    fsh = max(fs for (_, _, _, fs) in chk)
    out['I13_checks'] = [{'zero_mode': a_, 'finite_difference': r, 'overlap_b': i_, 'fold_band_shift': fs} for (a_, r, i_, fs) in chk]
    rep.check('C8_I13_overlaps_and_fold_band', devb < 1e-8 and fsh < 1e-12,
              'a mean field on the b-component, (1 - gamma^(x0))/2 v_b(y) = (1 - sigma3)/2 v_b(y), shifts the dark-matter level by '
              'Itilde^(b) = int b^2 rho_f e^{-3Hy} dy (self-consistent Kohn-Sham solutions, Richardson in the amplitude, agreement %.1e: '
              'Q %.6f, L %.6f, u_R %.6f) and leaves the fold zero mode and the first fold shell unchanged to %.1e: I13 does not act on '
              'the fold bands' % (devb, IbD['Q (quark doublets)'], IbD['L (lepton doublets)'], IbD['u_R'], fsh))
    # (b) s-wave annihilation chi chibar -> f fbar through G_f (chibar gamma chi)(fbar_chi gamma f_chi) per Weyl component f_chi:
    # sigma = N_c G_f^2 s (1 + 2 M^2/s)/(24 pi beta_i) (half of the Dirac value), beta_i = sqrt(1 - 4M^2/s);
    # final states: every quark Weyl component (baryon number 1/3); the B - L alternative (leptons -1, nu_R -1) is C9
    comps13 = []
    comps13_BL = []
    for gen, (uq, dq, lq, nq) in enumerate([('u', 'd', 'e', 'nu1'), ('c', 's', 'mu', 'nu2'), ('t', 'b', 'tau', 'nu3')]):
        for lst in (comps13, comps13_BL):
            lst.append(('Q%d' % (gen + 1), IbD['Q (quark doublets)'], 1 / 3., 6, (F[uq]['m_GeV'] + F[dq]['m_GeV']) / 2))
            lst.append((uq + '_R', IbD[uq + '_R'], 1 / 3., 3, F[uq]['m_GeV']))
            lst.append((dq + '_R', IbD[dq + '_R'], 1 / 3., 3, F[dq]['m_GeV']))
        comps13_BL.append(('L%d' % (gen + 1), IbD['L (lepton doublets)'], -1.0, 2, F[lq]['m_GeV']))
        comps13_BL.append((lq + '_R', IbD[lq + '_R'], -1.0, 1, F[lq]['m_GeV']))
        comps13_BL.append((nq + '_R', IbD[nq + '_R'], -1.0, 1, 0.0))
    S13 = sum(mult * (q * It) ** 2 for (_, It, q, mult, _) in comps13)
    S13_BL = sum(mult * (q * It) ** 2 for (_, It, q, mult, _) in comps13_BL)
    sp_ = species(masses, MDM)
    cosmo = Cosmo(sp_)
    s0 = th['s0_cm3']
    # the unitarity-safe I12 benchmark (um2_thermal.py)
    G12 = th['I12_universal_benchmark']['G_combination_GeV-3']
    sig12 = lambda s_: sigma_I12(s_, MDM, G12 ** 2)

    def sig13(s_, GA):
        bi = math.sqrt(max(1 - 4 * MDM * MDM / s_, 1e-300))
        return S13 * GA ** 2 * s_ * (1 + 2 * MDM * MDM / s_) / (24 * math.pi * bi)
    XT = np.logspace(math.log10(5.0), math.log10(2000.0), 200)
    from scipy.interpolate import CubicSpline
    sv12 = CubicSpline(np.log(XT), np.log([sigmav_thermal(xx, MDM, sig12) for xx in XT]))
    sv13u = CubicSpline(np.log(XT), np.log([sigmav_thermal(xx, MDM, lambda s_: sig13(s_, 1.0)) for xx in XT]))

    def omega_A(GA):
        sv = lambda x: math.exp(float(sv12(math.log(min(max(x, 5.0), 2000.0))))) + GA ** 2 * math.exp(
            float(sv13u(math.log(min(max(x, 5.0), 2000.0)))))
        Y, h, xf = relic(MDM, sv, cosmo, MPl=MPl)
        return omega_h2(MDM, Y, s0), xf, h
    from scipy.optimize import brentq as _brentq
    lgA = _brentq(lambda lg: omega_A(math.exp(lg))[0] - 0.060, math.log(1e-12), math.log(1e-7), xtol=1e-7)
    GA = math.exp(lgA)
    omA, xfA, histA = omega_A(GA)
    sv13_xf = GA ** 2 * math.exp(float(sv13u(math.log(xfA)))) * GEV2_CM2 * 2.99792458e10
    sv12_xf = math.exp(float(sv12(math.log(xfA)))) * GEV2_CM2 * 2.99792458e10
    # J = 1 (3S1) unitarity: sigma <= 3 pi/(4 p^2); fraction of the annihilation rate at x_f from collisions above the crossing
    sc13 = _brentq(lambda s_: sig13(s_, GA) - 3 * math.pi / (4 * (s_ / 4 - MDM * MDM)), 4 * MDM * MDM * (1 + 1e-9), 400 * MDM * MDM)
    from scipy.special import k1e
    zc = sc13 / (4 * MDM * MDM) - 1.0
    frac13 = rate_fraction_above(lambda s_: sig13(s_, GA), MDM, xfA, zc)
    vc13 = 2 * math.sqrt(zc / (1 + zc))      # CM relative velocity 2 beta at the crossing
    # the same with the I13 cross-section capped at the J = 1 bound (a unitarity-respecting completion that saturates the bound)
    def omega_A_cap(GA_):
        scx = _brentq(lambda s_: sig13(s_, GA_) - 3 * math.pi / (4 * (s_ / 4 - MDM * MDM)), 4 * MDM * MDM * (1 + 1e-9), 1e4 * MDM * MDM)
        zbx = (scx / (4 * MDM * MDM) - 1.0,)
        tab = CubicSpline(np.log(XT), np.log([sigmav_thermal(xx, MDM, lambda s_: min(sig13(s_, GA_), 3 * math.pi / (4 * (s_ / 4 - MDM * MDM))),
                                                             zbx) for xx in XT]))
        sv = lambda x: math.exp(float(sv12(math.log(min(max(x, 5.0), 2000.0))))) + math.exp(float(tab(math.log(min(max(x, 5.0), 2000.0)))))
        Y, h, xf = relic(MDM, sv, cosmo, MPl=MPl)
        return omega_h2(MDM, Y, s0), xf
    lgAc = _brentq(lambda lg: omega_A_cap(math.exp(lg))[0] - 0.060, math.log(GA), math.log(5 * GA), xtol=1e-6)
    GAc = math.exp(lgAc)
    omAc, xfAc = omega_A_cap(GAc)
    sc13c = _brentq(lambda s_: sig13(s_, GAc) - 3 * math.pi / (4 * (s_ / 4 - MDM * MDM)), 4 * MDM * MDM * (1 + 1e-9), 400 * MDM * MDM)
    zcc = sc13c / (4 * MDM * MDM) - 1.0
    frac13c = rate_fraction_above(lambda s_: min(sig13(s_, GAc), 3 * math.pi / (4 * (s_ / 4 - MDM * MDM))), MDM, xfAc, zcc)
    GA_eff = GA
    GA = GAc            # the benchmark: the unitarity-respecting value
    # direct detection through I13 (+ I11): vector couplings to the quark currents (each chirality half of the nucleon's current)
    Gu13 = GA * (1 / 3.) * 0.5 * (IbD['Q (quark doublets)'] + IbD['u_R'])
    Gd13 = GA * (1 / 3.) * 0.5 * (IbD['Q (quark doublets)'] + IbD['d_R'])
    fp13, fn13 = 2 * Gu13 + Gd13 + fp, Gu13 + 2 * Gd13 + fn
    fN13 = (Z * fp13 + (A - Z) * fn13) / A
    sig_n13 = mu_n ** 2 * fN13 ** 2 / math.pi * GEV2_CM2
    # annihilation today (galactic velocities v ~ 1e-3: the s-wave limit; the J = 1 bound pi 3/(4 p^2) is far above)
    sv_today = S13 * GA ** 2 * MDM ** 2 / (2 * math.pi) * GEV2_CM2 * 2.99792458e10
    out['I13'] = {'sum_Nc_q2_Ib2': S13, 'G_A_GeV-2': GA, 'G_A_over_G_F': GA / val('G_F_GeV-2'), 'G_A_effective_operator_GeV-2': GA_eff,
                  'sigma_v_today_cm3_s': sv_today,
                  'Omega_h2_per_species_effective': omA, 'x_f_effective': xfA, 'Omega_h2_per_species_capped': omAc, 'x_f_capped': xfAc,
                  'fraction_of_rate_saturated_capped': frac13c, 'v_crossing_capped': 2 * math.sqrt(zcc / (1 + zcc)),
                  'sigma_v_I13_at_xf_cm3_s': sv13_xf, 'sigma_v_I12_at_xf_cm3_s': sv12_xf, 'sqrt_s_unitarity_crossing_GeV': math.sqrt(sc13),
                  'v_crossing': vc13, 'fraction_of_rate_above_crossing_at_xf': frac13, 'f_p_GeV-2': fp13, 'f_n_GeV-2': fn13,
                  'sigma_n_xenon_cm2': sig_n13, 'LZ_cm2': lz,
                  'components': [{'name': a_, 'Itilde_b': b_, 'q': q_, 'mult': m_} for (a_, b_, q_, m_, _) in comps13]}
    rep.check('C8_I13_relic', abs(omA - 0.060) < 1e-4 and abs(omAc - 0.060) < 1e-4 and frac13c < 0.5,
              'with the unitarity-safe I12 benchmark and the s-wave portal I13 (baryon-number current, sum N_c (q Itilde^(b))^2 = %.3f over '
              'the quark Weyl components) each species leaves Omega h^2 = 0.060 for G_A = %.3e GeV^-2 if the effective cross-section held at every '
              'energy (x_f = %.2f; <sigma v>(x_f): I13 %.3e, I12 %.3e cm^3/s); that cross-section reaches the J = 1 bound '
              'sigma <= 3 pi/(4 p^2) (one channel, 3S1) above v = %.2f, which carries %.1f %% of the rate at freeze-out; with the cross-section '
              'capped at the bound the relic needs G_A = %.3e GeV^-2 (%.1e G_F; x_f = %.2f), and %.1f %% of the freeze-out rate then comes '
              'from collisions at the bound (v > %.2f): the relic is reached with most annihilations in the perturbative regime' % (
                  S13, GA_eff, xfA, sv13_xf, sv12_xf, vc13, 100 * frac13, GAc, GAc / val('G_F_GeV-2'), xfAc, 100 * frac13c,
                  2 * math.sqrt(zcc / (1 + zcc))))
    rep.check('C8_I13_direct_detection', sig_n13 < lz,
              'I13 and I11 couple the dark matter coherently to the quark vector currents: f_p = %.3e, f_n = %.3e GeV^-2, '
              'sigma_n = mu^2 f^2/pi = %.2e cm^2 for xenon, %.2f of the LZ limit %.2e cm^2 at %.1f TeV: allowed, and within reach of the next '
              'generation of xenon detectors; annihilation today (s-wave, into quark pairs) sigma v = sum N_c G_f^2 M^2/(2 pi) = %.2e cm^3/s' % (
                  fp13, fn13, sig_n13, sig_n13 / lz, lz, MDM / 1e3, sv_today))

    # ---------------- C9 the B - L alternative of I13 thermalises the right-handed neutrinos ----------------
    # relic coupling with the B - L current: the effective cross-section scales with S13, so G_A(B-L) = G_A_eff sqrt(S13/S13_BL)
    GA_BL = GA_eff * math.sqrt(S13 / S13_BL)
    Inu = [IbD['nu1_R'], IbD['nu2_R'], IbD['nu3_R']]
    zeta3 = 1.2020569
    gs_curve = th['g_star_curve']
    lnTg = np.log(gs_curve['T_GeV'])
    grv = np.array(gs_curve['g_rho'])
    gsv_ = np.array(gs_curve['g_s'])

    def g_at(T):
        lt = math.log(T)
        return float(np.interp(lt, lnTg, grv)), float(np.interp(lt, lnTg, gsv_))

    Ibar = math.sqrt(sum(I_ * I_ for I_ in Inu) / 3.0)          # the three overlaps differ by 2 %: one representative flavour

    def rates_nuR(x):
        """For one nu_R flavour: the pair-production rate density gamma = sum_{A,B} n_chi n_chibar <sigma v> (chi chibar <-> nu_R nubar_R,
        s-wave <sigma v> = G^2 M^2/(2 pi) per Weyl component, G = G_A Itilde^(b)), the equilibrium density of nu_R particles
        n_eq = (3/4) zeta(3) T^3/pi^2, and the elastic rate per nu_R, Gamma_el = sum_{A,B} (n_chi + n_chibar) G^2 E^2/(2 pi) with E ~ 3T
        (a Weyl nu_R scattering on a heavy Dirac fermion; ESTIMATE), with the Hubble rate"""
        T = MDM / x
        gr_, gs_ = g_at(T)
        Hh = math.sqrt(8 * math.pi ** 3 * gr_ / 90) * T * T / MPl
        nchi = 2 * (MDM * T / (2 * math.pi)) ** 1.5 * math.exp(-x)            # one Dirac species: particles (2 spin states)
        n_nu = 0.75 * zeta3 / math.pi ** 2 * T ** 3
        G2 = (GA_BL * Ibar) ** 2
        gam = 2 * nchi * nchi * G2 * MDM ** 2 / (2 * math.pi)
        Gel = 2 * 2 * nchi * G2 * (3 * T) ** 2 / (2 * math.pi)
        return gam, n_nu, Hh, Gel
    # chemical (number-changing) decoupling and kinetic decoupling
    xs = np.linspace(1.0, 60.0, 5901)
    xchem = None
    xkin = None
    for x in xs:
        gam, n_nu, Hh, Gel = rates_nuR(x)
        if xchem is None and gam / (n_nu * Hh) < 1.0:
            xchem = float(x)
        if xkin is None and Gel / Hh < 1.0:
            xkin = float(x)
    # Boltzmann equation for the nu_R number (one flavour, particles) from zero abundance at x = 2: dY/dx = gamma/(s H x) (1 - Y^2/Y_eq^2)
    from scipy.integrate import solve_ivp as _ivp

    def rhs(x, Y):
        gam, n_nu, Hh, Gel = rates_nuR(x)
        T = MDM / x
        gr_, gs_ = g_at(T)
        sden = 2 * math.pi ** 2 / 45 * gs_ * T ** 3
        Yeq = n_nu / sden
        return [gam / (sden * Hh * x) * (1 - (Y[0] / Yeq) ** 2)]
    solY = _ivp(rhs, (2.0, 40.0), [0.0], method='Radau', rtol=1e-8, atol=1e-30, dense_output=True)
    Yend = float(solY.y[0][-1])
    gam, n_nu, Hh, Gel = rates_nuR(40.0)
    gr_, gs_ = g_at(MDM / 40.0)
    Yeq_end = n_nu / (2 * math.pi ** 2 / 45 * gs_ * (MDM / 40.0) ** 3)
    Fh = 1.0095
    gs_dec = g_at(MDM / xkin)[1]
    dNeff_BL = 3 * (10.75 / gs_dec) ** (4.0 / 3.0) * Fh
    # with J^B: nu_R are produced only through I11 (B - L charge -1): chi chibar -> nu_R nubar_R with G = G_V Itilde (I11 overlap of the
    # dark-matter orbital with the nu_R profile), against the I13 annihilation into quarks (s-wave, the same Dirac structure)
    S_nuR_I11 = sum(Idm[n_ + '_R'] ** 2 for n_ in ('nu1', 'nu2', 'nu3'))
    ratio_nuR_I11 = (GVb ** 2 * S_nuR_I11) / (GA_eff ** 2 * S13)
    out['I13_B_minus_L_alternative'] = {'S13_BL': S13_BL, 'G_A_BL_GeV-2': GA_BL, 'x_chemical_decoupling': xchem, 'x_kinetic_decoupling': xkin,
                                        'nuR_production_I11_over_I13_annihilation_JB': ratio_nuR_I11,
                                        'T_kinetic_decoupling_GeV': MDM / xkin, 'Y_nuR_over_Yeq_at_x40': Yend / Yeq_end, 'g_s_at_decoupling': gs_dec,
                                        'Delta_Neff': dNeff_BL, 'nuR_share_of_annihilation': sum((I_ ** 2) for I_ in Inu) / S13_BL}
    Neff_act, sNeff = 2.86, 0.13
    rep.check('C9_B_minus_L_alternative_thermalises_nuR', abs(Yend / Yeq_end - 1) < 0.05 and dNeff_BL > 0.1,
              'with the B - L current instead of J^B, I13 would need G_A = %.3e GeV^-2 (sum N_c (q Itilde^(b))^2 = %.2f; the three nu_R carry %.1f %% '
              'of the annihilation) and chi chibar <-> nu_R nubar_R would bring the right-handed neutrinos into equilibrium: from zero abundance at '
              'M/T = 2 they reach %.4f of the equilibrium number by M/T = 40; the number-changing rate falls below the Hubble rate at M/T = %.1f '
              'and elastic scattering on the dark matter at M/T = %.1f (T = %.0f GeV, g_s = %.2f); the three nu_R would then add Delta N_eff = '
              '3 (10.75/g_s)^(4/3) F_h = %.3f, N_eff = %.3f, %.1f standard deviations above ACT DR6 (2.86 +- 0.13): hence I13 couples to the '
              'baryon-number current, which leaves the nu_R untouched (with J^B the annihilation into nu_R pairs goes only through I11, at '
              '%.1e of the I13 rate into quarks)' % (
                  GA_BL, S13_BL, 100 * out['I13_B_minus_L_alternative']['nuR_share_of_annihilation'], Yend / Yeq_end, xchem, xkin, MDM / xkin,
                  gs_dec, dNeff_BL, 3.0432 + dNeff_BL, (3.0432 + dNeff_BL - Neff_act) / sNeff, ratio_nuR_I11))


    # ---------------- C10 the self-interaction channel chi chibar -> fold pairs ----------------
    # -(lambda/2)(Psibar Psi)^2 contains -lambda (chibar_D chi_F)(chibar_F chi_D) s_DF(y)^2 with the transition scalar density
    # s_DF = a_D b_F + b_D a_F of the dark-matter orbital (a_D, b_D) and the fold zero mode (a_F, b_F = 0); its square is even under the
    # fold reflection, so the channel is allowed.  With the normalisation of C1 the 4D strength is G_lambda = lambda H Itilde_lambda/(2 f^4 v_t),
    # Itilde_lambda = int s_DF^2 e^{-3Hy} dy (units of H).  The s-wave annihilation is estimated as sigma v = G_lambda^2 M^2/(2 pi) per
    # final fold species (the value of one vector channel; the Fierz coefficients are not computed: ESTIMATE), N_F = 2 final species.
    aD, bD, _ = orb['dark matter (lowest odd level)']
    aF, bF, _ = orb['fold band (zero mode)']
    sDF = aD * bF + bD * aF
    Ilam = float(np.sum(w * sDF * sDF * np.exp(-3 * H * y)))
    NF = 2

    def Glam_of(lam_H6, vt_H3):
        """G_lambda in GeV^-2 for lambda in units H^-6 and v_t in units H^-3."""
        return lam_H6 * Ilam / (2 * f ** 4 * vt_H3) / HG ** 2

    def lam_rates(Gl, T):
        x_ = MDM / T
        gr_, gs_ = g_of(T)
        Hh = math.sqrt(8 * math.pi ** 3 * gr_ / 90) * T * T / MPl
        nchi = 2 * (MDM * T / (2 * math.pi)) ** 1.5 * math.exp(-x_)      # particles of one dark-matter species
        sv = Gl ** 2 * MDM ** 2 / (2 * math.pi)
        gam = 2 * nchi * nchi * sv * NF                                    # annihilations into fold pairs per volume and time
        nF = NF * 4 * 0.75 * zeta3 / math.pi ** 2 * T ** 3                 # fold quanta in equilibrium (two Dirac species)
        return gam, nF, Hh

    def dNeff_lam(Gl, xf_):
        """Delta N_eff of the fold quanta made by chi chibar -> fold pairs while the dark matter is in equilibrium (T_max .. M/x_f),
        each annihilation carrying 2M into the fold bands (not thermalised: the produced fold quanta never annihilate back)."""
        Ts = np.logspace(math.log10(MDM / xf_), math.log10(Tmax_b), 800)
        acc = 0.0
        prev = None
        for T in Ts[::-1]:
            gam, nF, Hh = lam_rates(Gl, T)
            gr_, gs_ = g_of(T)
            a4 = (gs_ ** (-1 / 3.) / T) ** 4
            val_ = 2 * MDM * gam * a4 / (Hh * T)
            if prev is not None:
                acc += 0.5 * (val_ + prev[1]) * (prev[0] - T)
            prev = (T, val_)
        gs0 = th['today']['g_s']
        return (acc / (gs0 ** (-1 / 3.)) ** 4) / (7 / 8 * math.pi ** 2 / 15 * ((4 / 11) ** (1 / 3.)) ** 4)

    def lam_equilibrium(Gl, xf_):
        """Largest production rate per fold quantum in equilibrium over the Hubble rate, and the lowest temperature at which it is >= 1."""
        best, Tlow = 0.0, None
        for T in np.logspace(math.log10(MDM / xf_), math.log10(Tmax_b), 600):
            gam, nF, Hh = lam_rates(Gl, T)
            r = 2 * gam / nF / Hh
            best = max(best, r)
            if r >= 1.0 and (Tlow is None or T < Tlow):
                Tlow = float(T)
        return best, Tlow

    # C10 evaluation: the bound on G_lambda (Delta N_eff <= 1e-3 from this channel) and the Kohn-Sham benchmark lambda_B with v_t = H^-3
    dN_lam_unit = dNeff_lam(1.0, xfAc)                    # Delta N_eff per G_lambda^2 (GeV^-4) in the non-thermal regime
    G_lam_max = math.sqrt(1e-3 / dN_lam_unit)
    eq_max, _ = lam_equilibrium(G_lam_max, xfAc)
    G_lam_B = Glam_of(LAM_B, 1.0)
    eq_B, Tlow_B = lam_equilibrium(G_lam_B, xfAc)
    Fh_ = 1.0095
    if eq_B >= 1.0:
        dN_B = 4 * (10.75 / g_of(Tlow_B)[1]) ** (4.0 / 3.0) * Fh_     # four Weyl species decoupling at T_low (thermalised)
    else:
        dN_B = dN_lam_unit * G_lam_B ** 2
    vt_min = G_lam_B / G_lam_max                         # v_t in units H^-3 for which lambda_B satisfies the bound
    lam_max_vt1 = LAM_B * G_lam_max / G_lam_B            # lambda in units H^-6 allowed for v_t = H^-3
    out['self_interaction_channel'] = {'Itilde_lambda': Ilam, 'N_F': NF, 'Delta_Neff_per_Glam2': dN_lam_unit,
                                       'G_lambda_max_GeV-2': G_lam_max, 'equilibrium_ratio_at_max': eq_max,
                                       'G_lambda_benchmark_vt1_GeV-2': G_lam_B, 'equilibrium_ratio_benchmark': eq_B,
                                       'T_low_benchmark_GeV': Tlow_B, 'Delta_Neff_benchmark_vt1': dN_B,
                                       'v_t_min_for_lambda_B_H-3': vt_min, 'lambda_max_for_vt1_H-6': lam_max_vt1,
                                       'G_lambda_over_G_A_at_max': G_lam_max / GA}
    rep.check('C10_self_interaction_channel', eq_max < 0.05 and dN_lam_unit > 0 and Ilam > 0,
              'the self-interaction -(lambda/2)(Psibar Psi)^2 lets the dark matter annihilate into the fold bands through the transition '
              'scalar density s_DF = a_D b_F + b_D a_F (Itilde_lambda = int s_DF^2 e^{-3Hy} dy = %.4f): G_lambda = lambda H Itilde_lambda/(2 f^4 v_t); '
              'with sigma v = G_lambda^2 M^2/(2 pi) per fold species (ESTIMATE) the channel adds Delta N_eff = %.3e G_lambda^2 GeV^4 while the '
              'dark matter is in equilibrium (T_max = 10 TeV to x_f = %.2f), so Delta N_eff <= 1e-3 requires G_lambda <= %.2e GeV^-2 (%.1e G_A; '
              'the fold bands then stay out of equilibrium, production rate at most %.1e of the Hubble rate); the Kohn-Sham benchmark '
              'lambda_B = 7e-5 H^-6 with v_t = H^-3 would give G_lambda = %.2e GeV^-2, %s; UM-2 therefore ASSUMES G_lambda <= %.1e GeV^-2, '
              'i.e. lambda <= %.1e H^-6 for v_t = H^-3 or v_t >= %.1e H^-3 for lambda = lambda_B (lambda_B is a numerical value of the '
              'Kohn-Sham tests)' % (
                  Ilam, dN_lam_unit, xfAc, G_lam_max, G_lam_max / GA, eq_max, G_lam_B,
                  ('thermalise the fold bands (production rate up to %.1e of the Hubble rate, coupled down to T = %.0f GeV) and add '
                   'Delta N_eff = %.3f' % (eq_B, Tlow_B, dN_B)) if eq_B >= 1.0 else ('Delta N_eff = %.2e' % dN_B),
                  G_lam_max, lam_max_vt1, vt_min))

    # ---------------- C4/C5/C6 environments ----------------
    # densities in cm^-3 (net particle numbers: antiparticles of a symmetric plasma do not contribute to I11), T in GeV
    mu_ = 1.66053907e-24      # atomic mass unit, g
    rho_c_h2 = 1.05368e-5     # GeV cm^-3
    ob, oc = 0.02237, 0.1200
    nb0 = ob * rho_c_h2 / 0.93827
    Yp = 0.24566
    T_fo = MDM / xfAc
    fo_name = 'dark-matter freeze-out (T = %.2f TeV)' % (T_fo / 1e3)
    env = {
        'cosmic mean today': {'n_p': nb0 * (1 - Yp / 2), 'n_n': nb0 * Yp / 2, 'n_e': nb0 * (1 - Yp / 2), 'rho_DM': oc * rho_c_h2, 'T': 0.0},
        'Milky Way at the Sun': {'n_p': 1.0, 'n_n': 0.0, 'n_e': 1.0, 'rho_DM': 0.4, 'T': 0.0},
        'Earth (mean density 5.51 g/cm^3)': {'n_p': 0.48 * 5.51 / mu_, 'n_n': 0.52 * 5.51 / mu_, 'n_e': 0.48 * 5.51 / mu_, 'rho_DM': 0.4, 'T': 0.0},
        'centre of the Sun (150 g/cm^3)': {'n_p': 0.66 * 150 / mu_, 'n_n': 0.32 * 150 / mu_, 'n_e': 0.66 * 150 / mu_, 'rho_DM': 0.4, 'T': 0.0},
        'white dwarf (1e6 g/cm^3, C/O)': {'n_p': 0.5e6 / mu_, 'n_n': 0.5e6 / mu_, 'n_e': 0.5e6 / mu_, 'rho_DM': 0.4, 'T': 0.0},
        'neutron star core (0.3 fm^-3)': {'n_p': 0.03e39, 'n_n': 0.27e39, 'n_e': 0.03e39, 'rho_DM': 0.4, 'T': 0.0},
        'nucleosynthesis (T = 1 MeV)': {'n_p': None, 'n_n': None, 'n_e': None, 'rho_DM': None, 'T': 1e-3},
        'QCD crossover (T = 200 MeV)': {'n_p': None, 'n_n': None, 'n_e': None, 'rho_DM': None, 'T': 0.2},
        'electroweak era (T = 100 GeV)': {'n_p': None, 'n_n': None, 'n_e': None, 'rho_DM': None, 'T': 100.0},
        fo_name: {'n_p': None, 'n_n': None, 'n_e': None, 'rho_DM': None, 'T': T_fo},
    }
    # early-Universe net densities from the baryon asymmetry: n_b = eta n_gamma, eta = 6.1e-10 (STANDARD); the net baryon number is
    # shared between protons and neutrons in weak equilibrium, n_n/n_p = exp(-Q/T), Q = 1.293 MeV (above the QCD crossover this is the
    # isospin-symmetric net quark content, n_u = n_d); electrons = protons (charge neutrality)
    zeta3 = 1.2020569
    eta_b = 6.1e-10
    Qnp = 1.29333e-3
    for k_, e_ in env.items():
        if e_['n_p'] is None:
            T = e_['T']
            ngam = 2 * zeta3 / math.pi ** 2 * T ** 3 / (HBARC_CM ** 3)        # cm^-3
            rnp = math.exp(-Qnp / T)
            e_['n_p'] = eta_b * ngam / (1 + rnp)
            e_['n_n'] = eta_b * ngam * rnp / (1 + rnp)
            e_['n_e'] = e_['n_p']
            # dark matter: thermal equilibrium (both species, Dirac, g = 4 each) at the temperature, or the relic density scaled
            x = MDM / T
            if x < 40:
                n_eq = 2 * 4 * (MDM * T / (2 * math.pi)) ** 1.5 * math.exp(-x) / (HBARC_CM ** 3)
                e_['n_DM'] = n_eq
            else:
                s_T = 2 * math.pi ** 2 / 45 * g_of(T)[1] * T ** 3 / HBARC_CM ** 3
                e_['n_DM'] = (oc * rho_c_h2 / MDM) / th['s0_cm3'] * s_T
            e_['rho_DM'] = e_['n_DM'] * MDM
        else:
            e_['n_DM'] = e_['rho_DM'] / MDM
    # running couplings (one loop, MS-bar inputs at m_Z, no Higgs particle: b_3 = 11 - 2 n_f/3, b_2 = 10/3, b_Y = -20/3 with
    # d(1/alpha)/d ln mu = b/(2 pi)); the thermal couplings at mu = 2 pi T; the block dependence alpha(m_KK) proportional to f^-4
    # (bulk gauge fields: 1/g_4^2 = V_perp/g_8^2) and m_KK proportional to 1/f
    a_s = val('alpha_s_mZ')
    mZ0 = val('m_Z_GeV')
    a_em = 1 / 127.95
    s2ms = val('sin2_theta_W_MSbar')
    mKK = masses['scales']['m_KK_GeV']
    B2, BY = 10.0 / 3.0, -20.0 / 3.0

    def alpha_ew(mu_s):
        Lm = math.log(mu_s / mZ0) / (2 * math.pi)
        return 1 / (s2ms / a_em + B2 * Lm), 1 / ((1 - s2ms) / a_em + BY * Lm)

    a2KK, aYKK = alpha_ew(mKK)

    def dlnalpha_dlnf(al, alKK, b):
        return -al * (4.0 / alKK + b / (2 * math.pi))

    GG_vac = 0.012 * math.pi / a_s * 4 * math.pi * a_s        # g_s^2 <G G>_can = 4 pi alpha_s (pi/alpha_s) 0.012 = 0.048 pi^2 GeV^4
    mW = val('m_W_GeV')
    mZ = masses['WZ']['m_Z_pred_GeV']
    s2 = masses['WZ']['sin2_theta_couplings']
    bench = th['I12_universal_benchmark']
    cL3 = bench['c_over_Lambda_star3_GeV-3']          # c/Lambda*^3 (universal c_G = c_W = c_B)
    a2Z, aYZ = alpha_ew(mZ0)
    GiW = O * cL3 * 4 * math.pi * a2Z
    GiB = O * cL3 * 4 * math.pi * aYZ
    Gig = O * cL3 * bench['couplings_squared']['g_s^2']

    def interaction_measure_vector(m, T):
        r, p, s_ = gas(m, T, 3, False)
        return r - 3 * p

    def n_flavours(T):
        return 3 if T < 1.27 else (4 if T < 4.18 else (5 if T < 172.56 else 6))

    def qcd_measure(T, dlnL=0.0):
        """(rho - 3p) of QCD: lattice-like value near the crossover (ESTIMATE, FROM MEMORY: I/T^4 = 4.0 at 200 MeV), leading-order
        perturbation theory above, I/T^4 = (b/3)(1 + 5 n_f/12) alpha_s^2 with alpha_s at mu = 2 pi T (one loop), zero far below;
        dlnL shifts Lambda_QCD by e^dlnL (for the loop gain)."""
        if T < 0.05:
            return 0.0
        if T < 1.0:
            return 4.0 * T ** 4 * math.exp(-((math.log(T * math.exp(-dlnL) / 0.2)) ** 2) / 0.5)
        nf = n_flavours(T)
        b = 11 - 2 * nf / 3
        inv = 1 / a_s + b / (2 * math.pi) * (math.log(2 * math.pi * T / mZ0) - dlnL)
        al = 1 / inv
        return (b / 3) * (1 + 5 * nf / 12) * al ** 2 * T ** 4

    def ew_pressure2(T):
        """The O(alpha) pressure of the electroweak plasma in the massless limit (no scalars; ESTIMATE), p_2 = -(g^2 T^4/144) d_A
        [C_A + (5/2) T_F N_f]: SU(2): d_A = 3, C_A = 2, twelve Weyl doublets (T_F N_f = 3); U(1)_Y: (5/2) sum_Dirac Y^2 = (5/2) 5;
        below m_W multiplied by the thermal suppression of a massive vector, rho(m_W, T)/rho(0, T)."""
        if T <= 0:
            return 0.0, 0.0, 0.0, 0.0
        a2, aY = alpha_ew(2 * math.pi * T)
        supp = gas(mW, T, 3, False)[0] / gas(0.0, T, 3, False)[0]
        p2W = -(4 * math.pi * a2 * T ** 4 / 144.0) * 3 * (2 + 2.5 * 3) * supp
        p2Y = -(4 * math.pi * aY * T ** 4 / 144.0) * 2.5 * 5 * supp
        return p2W, p2Y, a2, aY

    stiff = 3.0 - 4.0 * krho / kst                  # units H^2
    sens = ana['sensitivities_dlnX_dlnf']
    # the proton: m_p = C Lambda_QCD^(3) + sigma terms; one-loop running with thresholds (ESTIMATE)
    b6 = 7.0
    inv_mKK = 1 / a_s + b6 / (2 * math.pi) * math.log(mKK / mZ0)      # alpha_s(m_KK), six flavours above m_t (one loop)
    as_KK = 1 / inv_mKK
    dlnL6 = -1.0 + (2 * math.pi / (b6 * as_KK)) * (-4.0)
    dlnL3 = (21 / 27.) * dlnL6 + (2 / 27.) * (sens['m_t'] + sens['m_b'] + sens['m_c'])
    dlnLnf = {6: dlnL6, 5: (21 / 23.) * dlnL6 + (2 / 23.) * sens['m_t'],
              4: (21 / 25.) * dlnL6 + (2 / 25.) * (sens['m_t'] + sens['m_b']), 3: dlnL3}
    sig_ud, sig_s, mp = 0.045, 0.040, 0.93827       # sigma terms (FROM MEMORY)
    dlnmp = (1 - (sig_ud + sig_s) / mp) * dlnL3 + sig_ud / mp * 0.5 * (sens['m_u'] + sens['m_d']) + sig_s / mp * sens['m_s']
    out['proton_sensitivity'] = {'alpha_s_mKK': as_KK, 'dlnLambda6_dlnf': dlnL6, 'dlnLambda5_dlnf': dlnLnf[5],
                                 'dlnLambda4_dlnf': dlnLnf[4], 'dlnLambda3_dlnf': dlnL3, 'dln_mp_dlnf': dlnmp,
                                 'quark_inputs_dlnm_dlnf': {q: sens['m_' + q] for q in ('u', 'd', 's', 'c', 'b', 't')}}
    rep.check('C6_proton_sensitivity', dlnmp < -30,
              'the QCD scale tracks the block exponentially: with alpha_s(m_KK) = %.4f proportional to f^-4 and m_KK ~ 1/f, '
              'd ln Lambda^(6)/d ln f = -1 - (2 pi/(7 alpha_s)) 4 = %.1f; through the c, b, t thresholds (d ln m_q/d ln f = %.2f, %.2f, %.2f) '
              'd ln Lambda^(3)/d ln f = %.1f; with the sigma terms (d ln m_q/d ln f = %.2f, %.2f, %.2f for u, d, s) d ln m_p/d ln f = %.1f '
              '(ESTIMATE, one loop): the nucleon mass is the most block-sensitive mass of UM-2' % (
                  as_KK, dlnL6, sens['m_c'], sens['m_b'], sens['m_t'], dlnL3, sens['m_u'], sens['m_d'], sens['m_s'], dlnmp))
    GN = 1.0 / MPl ** 2
    kV = 8 * math.pi * GN * Gk                      # kappa/V_perp = 8 pi G_N G(k*) in GeV^-2
    lr = bg['linear_response_static_dk']
    c_rho, c_3, c_p = lr['per_kappa_drho_H2'], lr['per_kappa_dp3_H2'], lr['per_kappa_dpbar_H2']
    # the plasma species of um2_thermal.py with their block sensitivities (the dark matter is treated separately)
    sp_all = [s_ for s_ in species(masses, MDM) if s_[4] != 'dm']
    sens_sp = {'u': sens['m_u'], 'd': sens['m_d'], 's': sens['m_s'], 'c': sens['m_c'], 'b': sens['m_b'], 't': sens['m_t'],
               'e': sens['m_e'], 'mu': sens['m_mu'], 'tau': sens['m_tau'], 'W+ W-': sens['m_W'], 'Z': sens['m_W']}
    baryons = ('N', 'Lambda', 'Sigma', 'Delta')
    for (n_, m_, g_, fe_, grp_) in sp_all:
        if grp_ == 'hrg':
            sens_sp[n_] = dlnmp if n_ in baryons else (0.5 * (0.5 * (sens['m_u'] + sens['m_d']) + dlnL3) if n_ == 'pi' else dlnL3)
    from um2_thermal import w_qgp

    def fermi_gas_T0(n, m):
        """rho, p of a free degenerate Fermi gas (2 spin states) of number density n (GeV^3) and mass m at T = 0."""
        if n <= 0:
            return 0.0, 0.0
        kf = (3 * math.pi ** 2 * n) ** (1 / 3.)
        x_ = kf / m
        if x_ < 1e-3:                                   # non-relativistic: rho = n m + (3/5) n kf^2/(2m), p = (2/5) n kf^2/(2m)
            return n * m + 0.3 * n * kf * kf / m, 0.2 * n * kf * kf / m
        sq = math.sqrt(1 + x_ * x_)
        rho_ = m ** 4 / (8 * math.pi ** 2) * (x_ * (2 * x_ * x_ + 1) * sq - math.asinh(x_))
        p_ = m ** 4 / (24 * math.pi ** 2) * (x_ * (2 * x_ * x_ - 3) * sq + 3 * math.asinh(x_))
        return rho_, p_

    def sources(env_, nn, dl):
        """Block-averaged 4D sources (rho, p3, pbar) in GeV^4 of an environment, every mass scaled by e^(s dl) (s = d ln m/d ln f)
        and Lambda_QCD and the gauge couplings with their block dependence (dl = delta ln f, for the loop gain); pbar = (1/4) dp/d ln f."""
        T = env_['T']
        rho_t = p3_t = 0.0
        dpdlnf = 0.0
        if T > 0:
            for (n_, m_, g_, fe_, grp_) in sp_all:
                s_ = sens_sp.get(n_, 0.0)
                mm = m_ * math.exp(s_ * dl) if m_ > 0 else 0.0
                r_, pp_, _ = gas(mm, T, g_, fe_)
                wgt = w_qgp(T) if grp_ == 'qgp' else ((1 - w_qgp(T)) if grp_ == 'hrg' else 1.0)
                rho_t += wgt * r_
                p3_t += wgt * pp_
                dpdlnf += -wgt * (r_ - 3 * pp_) * s_
            nf = n_flavours(T)
            dlnL = dlnLnf[nf]
            Iq = qcd_measure(T, dlnL * dl)
            rho_t += Iq                                 # the interaction measure enters rho - 3 p3 (radiation drops out)
            dpdlnf += -Iq * dlnL
            p2W, p2Y, a2, aY = ew_pressure2(T)
            dW, dY = dlnalpha_dlnf(a2, a2KK, B2), dlnalpha_dlnf(aY, aYKK, BY)
            fW, fY = math.exp(dW * dl), math.exp(dY * dl)
            rho_t += -(B2 * a2 / (2 * math.pi)) * p2W * fW * fW - (BY * aY / (2 * math.pi)) * p2Y * fY * fY   # LO trace anomaly
            dpdlnf += p2W * fW * dW + p2Y * fY * dY
        # net nucleons and electrons (degenerate at T = 0, non-relativistic thermal gases otherwise), dark matter
        mN_ = mp * math.exp(dlnmp * dl)
        me_ = F['e']['m_GeV'] * math.exp(sens['m_e'] * dl)
        MD_ = MDM * math.exp(sens['M_DM'] * dl)
        for (nk, mm, s_) in (('n_p', mN_, dlnmp), ('n_n', mN_, dlnmp), ('n_e', me_, sens['m_e'])):
            if T == 0:
                r_, pp_ = fermi_gas_T0(nn[nk], mm)
            else:
                r_, pp_ = nn[nk] * mm, nn[nk] * T
            rho_t += r_
            p3_t += pp_
            dpdlnf += -(r_ - 3 * pp_) * s_
        if T > 0 and MDM / T < 40:
            r_, pp_, _ = gas(MD_, T, 8, True)
        else:
            r_, pp_ = nn['n_DM'] * MD_, 0.0
        rho_t += r_
        p3_t += pp_
        dpdlnf += -(r_ - 3 * pp_) * sens['M_DM']
        return rho_t, p3_t, 0.25 * dpdlnf

    def block_response(env_, nn, dl=0.0):
        rr, pp3, ppb = sources(env_, nn, dl)
        dk_ = (c_rho * kV * rr + c_3 * kV * pp3 + c_p * kV * ppb) / HG ** 2
        return -0.5 * dk_ / kst, dk_, rr, pp3, ppb

    res_env = {}
    for k_, e_ in env.items():
        T = e_['T']
        nn = {kk: e_[kk] * cm3 for kk in ('n_p', 'n_n', 'n_e', 'n_DM')}      # GeV^3
        nu_ = 2 * nn['n_p'] + nn['n_n']
        nd_ = nn['n_p'] + 2 * nn['n_n']
        # I11 mean field on the dark-matter level (each chirality half of the unpolarised density)
        dI11 = GVb * ((1 / 3.) * nu_ * 0.5 * (Idm['Q (quark doublets)'] + Idm['u_R']) +
                      (1 / 3.) * nd_ * 0.5 * (Idm['Q (quark doublets)'] + Idm['d_R']) -
                      1.0 * nn['n_e'] * 0.5 * (Idm['L (lepton doublets)'] + Idm['e_R']))
        dI13 = GA * ((1 / 3.) * nu_ * 0.5 * (IbD['Q (quark doublets)'] + IbD['u_R']) +
                     (1 / 3.) * nd_ * 0.5 * (IbD['Q (quark doublets)'] + IbD['d_R']))
        # I12 mean field: c (<GG> + <WW> + <BB>)/Lambda*^3 in geometric normalisation
        GG = GG_vac                 # <G G>_T = <G G>_0 - (8/b)(rho - 3p)_T (trace anomaly, vacuum subtracted)
        Iq = qcd_measure(T)
        bq = 11 - 2 * n_flavours(T) / 3 if T > 0 else 9.0
        GG += -(8 / bq) * Iq * (4 * math.pi ** 2)     # g_s^2 <G G>_can = 4 pi^2 <(alpha_s/pi) G G>
        WW = 0.0
        BB = 0.0
        WWint = BBint = 0.0
        if T > 0:
            IW = interaction_measure_vector(mW, T)
            IZ = interaction_measure_vector(mZ, T)
            c2 = 1 - s2
            a2T, aYT = alpha_ew(2 * math.pi * T)
            g2W, g2B = 4 * math.pi * a2T, 4 * math.pi * aYT
            p2W, p2Y, _, _ = ew_pressure2(T)
            WWint = 4 * g2W * p2W                         # Feynman-Hellmann: <F_geo^2> = -4 dp/d(1/g^2) = 4 g^2 p_2
            BBint = 4 * g2B * p2Y
            WW = g2W * (2 * (-2 * IW) + c2 * (-2 * IZ)) + WWint
            BB = g2B * (s2 * (-2 * IZ)) + BBint
        dM = cL3 * (GG + WW + BB)
        dI12 = O * dM
        # Psi on the Standard Model: gauge couplings from the dark-matter scalar density
        nDM = nn['n_DM']
        dag = -4 * Gig * nDM
        daW = -4 * GiW * nDM
        daB = -4 * GiB * nDM
        # gravity: the full adiabatic block response to every species
        dlnf, dk, rr, pp3, ppb = block_response(e_, nn)
        eps_g = 1e-3
        gain = abs(block_response(e_, nn, eps_g)[0] - block_response(e_, nn, -eps_g)[0]) / (2 * eps_g)
        # iterate the loop mass -> source -> block -> mass
        dl = 0.0
        hist = []
        for it in range(60):
            dl_new = block_response(e_, nn, dl)[0]
            hist.append(dl_new)
            if abs(dl_new - dl) <= 1e-12 * max(abs(dl_new), 1e-300):
                dl = dl_new
                break
            dl = dl_new
        res_env[k_] = {'T_GeV': T, 'densities_cm3': {kk: e_[kk] for kk in ('n_p', 'n_n', 'n_e', 'n_DM')},
                       'd_eps_DM_I11_GeV': dI11, 'd_eps_DM_I13_GeV': dI13, 'd_eps_DM_I12_GeV': dI12,
                       'd_eps_DM_over_M': (dI11 + dI13 + dI12) / MDM,
                       'dM_I12_GeV': dM, 'condensates_GeV4': {'GG': GG, 'WW': WW, 'BB': BB, 'WW_interaction': WWint, 'BB_interaction': BBint},
                       'dalpha_over_alpha': {'strong': dag, 'SU2': daW, 'U1': daB},
                       'sources_GeV4': {'rho': rr, 'p3': pp3, 'pbar': ppb, 'rho_minus_3p3': rr - 3 * pp3},
                       'kappa_pbar_GeV2': kV * ppb, 'delta_k': dk, 'delta_ln_f': dlnf, 'delta_ln_m_p': dlnmp * dlnf,
                       'delta_ln_m_e': sens['m_e'] * dlnf, 'loop_gain': gain, 'iterations': len(hist), 'delta_ln_f_self_consistent': dl}
    out['environments'] = res_env
    out['block_response_coefficients'] = {'c_rho': c_rho, 'c_3': c_3, 'c_p': c_p, 'kappa_over_Vperp_GeV-2': kV,
                                          'radiation_cancels': abs(c_3 + 3 * c_rho) < 1e-12}
    worst = max(abs(v['d_eps_DM_over_M']) for v in res_env.values())
    worst_env = max(res_env, key=lambda k_: abs(res_env[k_]['d_eps_DM_over_M']))
    late = max(abs(v['d_eps_DM_over_M']) for k_, v in res_env.items() if v['T_GeV'] < 1e-3 * 1.0001)
    worst_gain = max(v['loop_gain'] for v in res_env.values())
    worst_dm = max(abs(v['delta_ln_m_p']) for v in res_env.values())
    worst_f = max(abs(v['delta_ln_f']) for v in res_env.values())
    worst_f_env = max(res_env, key=lambda k_: abs(res_env[k_]['delta_ln_f']))
    late_f = max(abs(v['delta_ln_f']) for k_, v in res_env.items() if v['T_GeV'] < 1e-3 * 1.0001)
    fo = res_env[fo_name]
    # the Feynman-Hellmann form <F_geo^2> = 4 g^2 p_2 of the O(alpha) pressure against the trace anomaly for QCD (d_A = 8, C_A = 3,
    # T_F = 1/2): an identity at leading order, which checks the normalisation of p_2 used for SU(2) and U(1)_Y
    fh_dev = 0.0
    for T_ in (10.0, 100.0, T_fo):
        nf_ = n_flavours(T_)
        b_ = 11 - 2 * nf_ / 3
        als = 1 / (1 / a_s + b_ / (2 * math.pi) * math.log(2 * math.pi * T_ / mZ0))
        p2s = -(4 * math.pi * als * T_ ** 4 / 144.0) * 8 * (3 + 2.5 * 0.5 * nf_)
        fh_dev = max(fh_dev, abs((4 * (4 * math.pi * als) * p2s) / (-(8 / b_) * qcd_measure(T_) * 4 * math.pi ** 2) - 1))
    out['feynman_hellmann_qcd_rel_dev'] = fh_dev
    rep.check('C4_mean_fields_in_environments', worst < 1e-4 and fh_dev < 1e-12,
              'the Standard-Model mean fields shift the dark-matter level by at most %.1e of its mass over the ten environments (largest: '
              '%s, where the thermal gauge condensates are of order T^4: g_s^2 <GG> = %.2e, g^2 <WW> = %.2e (O(alpha) part %.2e), '
              'g\'^2 <BB> = %.2e GeV^4; at most %.1e from nucleosynthesis to today) '
              '(I11 from the quark and electron B - L densities, I13 from the quark baryon-number densities, each with its x0 profiles; I12 '
              'from the QCD vacuum condensate, the thermal QCD interaction measure and the thermal W, Z condensates, free massive-vector '
              'and O(alpha) parts; for QCD the Feynman-Hellmann form 4 g^2 p_2 reproduces the trace-anomaly condensate to %.0e); the fold '
              'band stays massless' % (
                  worst, worst_env, fo['condensates_GeV4']['GG'], fo['condensates_GeV4']['WW'], fo['condensates_GeV4']['WW_interaction'],
                  fo['condensates_GeV4']['BB'], late, max(fh_dev, 1e-16)))
    rep.check('C6_gravity_loop', worst_gain < 1e-6 and all(v['iterations'] < 10 for v in res_env.values())
              and out['block_response_coefficients']['radiation_cancels'],
              'the full adiabatic block response dk = (%.6f kappa drho %+.6f kappa dp3 %+.6f kappa dpbar)/H^2 (radiation drops out exactly: '
              'c_3 = -3 c_rho) to the plasma (ideal gases with the x0 masses, the QCD interaction measure with d ln Lambda/d ln f, the O(alpha) '
              'electroweak pressure with d ln alpha/d ln f), the net nucleons (d ln m_p/d ln f = %.1f) and electrons and the dark matter '
              'shifts the block by at most delta ln f = %.1e (%s: pbar = %.2e GeV^4, rho - 3p3 = %.2e GeV^4), at most %.1e from '
              'nucleosynthesis to today (nucleon mass at most %.1e); the gain of the loop mass -> source -> block -> mass is at most %.1e, so '
              'the self-consistent iteration converges at once' % (
                  c_rho, c_3, c_p, dlnmp, worst_f, worst_f_env, res_env[worst_f_env]['sources_GeV4']['pbar'],
                  res_env[worst_f_env]['sources_GeV4']['rho_minus_3p3'], late_f, worst_dm, worst_gain))

    # ---------------- C5 W and Z masses with the y-dependent kinetic function ----------------
    a, b, eo = orb['dark matter (lowest odd level)']
    sprof = 2 * a * b                                         # scalar density shape of the dark-matter orbital (j = +1)
    Oint = float(np.sum(w * sprof))
    tq = y / L
    def Kfun_factory(amp):
        return lambda t: 1.0 + amp * float(np.interp(t * L, y, sprof))
    bW = masses['WZ']['beta_W']
    LW0, nodes, uW = boson_fem_K(ETA, bW, lambda t: 1.0)
    out_wz = {}
    for amp in (1e-3, 2e-3):
        LWa, _, _ = boson_fem_K(ETA, bW, Kfun_factory(amp))
        LWm, _, _ = boson_fem_K(ETA, bW, Kfun_factory(-amp))
        out_wz[amp] = (LWa - LWm) / (2 * amp) / LW0
    rich = (4 * out_wz[1e-3] - out_wz[2e-3]) / 3
    # first-order perturbation: d ln Lambda_W/d amp = [int s (u'^2 - Lambda u^2) e^{3 eta t} dt]/[int (u'^2 + ...)...] evaluated on FEM
    Lph, _, _ = boson_fem_K(ETA, 0.0, Kfun_factory(1e-2))
    e_amp = {k_: max(abs(v_) for v_ in res_env[k_]['dalpha_over_alpha'].values()) for k_ in res_env}
    e_fo = e_amp[fo_name]
    e_today = e_amp['cosmic mean today']
    e_late = max(v_ for k_, v_ in e_amp.items() if res_env[k_]['T_GeV'] < 1e-3 * 1.0001)
    out['WZ_kinetic_shift'] = {'dlnLambdaW_damp': rich, 'Lambda_W_fem': LW0, 'photon_Lambda_with_K': Lph, 'O_integral': Oint,
                               'amplitude_e_by_environment': e_amp}
    rep.check('C5_WZ_and_photon', abs(Lph) < 1e-10 and rich < 0,
              'with the kinetic function 1 + e s_DM(y) (s_DM = 2ab of the dark-matter orbital) the W eigenvalue changes by d ln Lambda_W/de = '
              '%.4f (finite elements, Richardson in e), i.e. m_W follows the 4D coupling, while the photon (and gluon) zero mode stays exactly '
              'massless (Lambda = %.1e with e = 0.01); the amplitude in the environments, e ~ 4 c g^2 n_DM/Lambda*^3 = |delta alpha/alpha|, is '
              '%.1e at the dark-matter freeze-out, at most %.1e from nucleosynthesis on and %.1e for the cosmic mean today' % (
                  rich, Lph, e_fo, e_late, e_today))

    # ---------------- C7 validity domain ----------------
    Tv = None
    for T in np.logspace(2, 4.6, 400):
        x = MDM / T
        n_eq = 2 * 4 * (MDM * T / (2 * math.pi)) ** 1.5 * math.exp(-x)
        if 4 * Gig * n_eq > 0.1:
            Tv = float(T)
            break
    out['validity'] = {'T_at_which_dalpha_s_over_alpha_s_reaches_0.1_GeV': Tv, 'M_over_T': MDM / Tv if Tv else None,
                       'unitarity_velocity_relic_strength_I12': th['unitarity']['v_crossing_exact'],
                       'I12_benchmark_unitarity_crossing_sqrt_s_over_M': th['I12_universal_benchmark']['sqrt_s_unitarity_crossing_GeV'] / MDM,
                       'I13_capped_crossing_velocity': out['I13']['v_crossing_capped']}
    rep.check('C7_validity_domain', Tv is not None and MDM / Tv < xfAc,
              'the gauge-kinetic portal of the benchmark changes the strong coupling by 10 %% through the thermal dark-matter density at '
              'T = %.0f GeV (M/T = %.2f): the coupled effective description holds below this temperature, i.e. through dark-matter freeze-out '
              '(M/T = %.2f) and everything later; the benchmark I12 respects the 3P0 unitarity bound up to sqrt(s) = %.2f M (an I12 of the '
              'relic strength of version 2 would violate it above v = %.3f), and I13 reaches its J = 1 bound only above v = %.2f' % (
                  Tv, MDM / Tv, xfAc, th['I12_universal_benchmark']['sqrt_s_unitarity_crossing_GeV'] / MDM, th['unitarity']['v_crossing_exact'],
                  out['I13']['v_crossing_capped']))

    # ---------------- figure ----------------
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
        a_, b_, _ = orb['dark matter (lowest odd level)']
        af, bf_, _ = orb['fold band (zero mode)']
        ax[0].plot(y, a_ * a_ + b_ * b_, label='dark-matter orbital $a^2+b^2$')
        ax[0].plot(y, af * af + bf_ * bf_, label='fold band')
        for zn in ('Q (quark doublets)', 'L (lepton doublets)', 'e_R', 'u_R'):
            pr = sm_profile(zero_modes[zn], y)
            ax[0].plot(y, pr / pr.max() * 1.5, '--', lw=1, label=zn + ' (scaled)')
        ax[0].set_xlabel('y (units 1/H; fold at 0, tip at -3)')
        ax[0].set_title('x0 profiles entering the I11 overlaps')
        ax[0].legend(fontsize=7)
        names = list(res_env.keys())
        vals = [abs(res_env[n]['d_eps_DM_over_M']) + 1e-300 for n in names]
        ax[1].barh(range(len(names)), np.log10(vals))
        ax[1].set_yticks(range(len(names)))
        ax[1].set_yticklabels(names, fontsize=7)
        ax[1].set_xlabel('log10 |shift of the dark-matter level / M|')
        ax[1].set_title('Standard-Model mean fields on dirac16complex')
        fig.tight_layout()
        fig.savefig(os.path.join(FIG, 'fig_coupled.png'), dpi=130)
        plt.close(fig)
    except Exception as exc:     # pragma: no cover
        print('figure failed:', exc)

    write_json(os.path.join(OUT, 'coupled.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
