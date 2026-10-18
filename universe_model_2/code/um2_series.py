#!/usr/bin/env python3
"""UM-2 metric power series (version 3, 2026-10-18): the terms of

    g_MN = gbar_MN + eps h^(1)_MN + eps^2 h^(2)_MN + ...,     h^(1)_MN(x^mu, x0) = sum_n h^(1,n)_MN(x^mu) u_n(x0),

and their magnitudes, from the computed solution.

S1  Order 0: the stabilised background (block scale f*, warp e^{2Hy} of the extra times, Friedmann 3-space); magnitude 1.
S2  Order 1, n = 0 (the four-dimensional perturbations: CMB, CNB, BAO): the rms Newtonian potential per logarithmic k today,
    Delta_Phi(k), and sigma_8 (um2_cosmology.py); the potentials of bound objects, Phi = G_N M/(R c^2), from the Earth to a
    neutron star (where the series converges slowly and full nonlinear general relativity is needed).
S3  Order 1, n >= 1 (the Kaluza-Klein gravitons): masses m_n and Yukawa strengths alpha_n of the even graviton tower for a
    source at the fold (alpha_n = N_0/N_n, u_n(0) = 1), for the quark-doublet and lepton-doublet zero-mode profiles and for a
    source with the flat (zero-mode) profile (which excites no Kaluza-Klein graviton: orthogonality); exact eigenfunctions
    checked against finite elements; the deviation from Newton's law at laboratory distances.
S4  The radion sigma (the relative fluctuation of the block size): its static response to matter in the environments of
    um2_coupled.py, its range, and the decay of the primordial oscillation (um2_analysis.py).
S5  Order 2: magnitude eps^2 (the squares of the first-order terms).
S6  Tensor modes h^TT: not predicted (the primordial spectrum is an input of UM-2); the observational bound.
S7  The terms ordered by magnitude, with the regime in which each matters.
Writes outputs/series.json and reports/series-checks.json.
"""
import math
import os
import sys

import numpy as np
from scipy.linalg import eigh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import ETA, val  # noqa: E402


def graviton_even_exact(eta, n):
    """Even graviton levels with beta = 0: q_n = n pi, Lambda_n = 9 eta^2/4 + q_n^2, u_n = e^{-a xi}(cos q xi + (a/q) sin q xi),
    a = 3 eta/2, u_n(0) = 1; N_n = int_{-1}^{0} e^{3 eta xi} u_n^2 dxi = (1 + a^2/q^2)/2 (n >= 1), N_0 = (1 - e^{-3 eta})/(3 eta)."""
    a = 1.5 * eta
    if n == 0:
        return 0.0, (1 - math.exp(-3 * eta)) / (3 * eta)
    q = n * math.pi
    return a * a + q * q, 0.5 * (1 + a * a / (q * q))


def u_even(eta, n, xi):
    a = 1.5 * eta
    if n == 0:
        return np.ones_like(xi)
    q = n * math.pi
    return np.exp(-a * xi) * (np.cos(q * xi) + (a / q) * np.sin(q * xi))


def fem_levels(eta, beta, ne=400, nlev=6):
    """Quadratic finite elements for int e^{3 eta xi} u'^2 + beta e^{-3 eta} u(-1)^2 = Lambda int e^{3 eta xi} u^2 (even: free at 0)."""
    nodes = np.linspace(-1.0, 0.0, 2 * ne + 1)
    n = len(nodes)
    K = np.zeros((n, n))
    M = np.zeros((n, n))
    xg, wg = np.polynomial.legendre.leggauss(6)
    for e in range(ne):
        idx = [2 * e, 2 * e + 1, 2 * e + 2]
        a, b = nodes[idx[0]], nodes[idx[2]]
        hl = b - a
        for xi_, wi in zip(xg, wg):
            s = (xi_ + 1) / 2
            t = a + s * hl
            N = np.array([2 * (s - 0.5) * (s - 1), -4 * s * (s - 1), 2 * s * (s - 0.5)])
            dN = np.array([4 * s - 3, -8 * s + 4, 4 * s - 1]) / hl
            wt = math.exp(3 * eta * t) * wi * hl / 2
            K[np.ix_(idx, idx)] += wt * np.outer(dN, dN)
            M[np.ix_(idx, idx)] += wt * np.outer(N, N)
    K[0, 0] += beta * math.exp(-3 * eta)
    ev = eigh(K, M, eigvals_only=True, subset_by_index=[0, nlev - 1])
    return ev


def main():
    rep = Report('series-checks', 'UM-2 metric power series: the terms of g = gbar + eps h1 + eps^2 h2 + ... and their magnitudes')
    out = {}
    masses = read_json(os.path.join(OUT, 'masses.json'))
    cos = read_json(os.path.join(OUT, 'cosmology.json'))
    cpl = read_json(os.path.join(OUT, 'coupled.json'))
    ana = read_json(os.path.join(OUT, 'analysis.json'))
    sc = masses['scales']
    fL_m = sc['fL_m']
    hbarc = val('hbar_c_GeV_m')
    eta = ETA

    # ---------------- S1 order 0 ----------------
    out['order0'] = {'f_star': sc['f_star'], 'proper_half_cell_m': fL_m, 'x0_period_m': sc['period_x0_m'],
                     'statement': 'gbar: diag(e^{-2a4} b4 cot^2 z, e^{2a4} x3, -1, -e^{-2a4} b4 (sin^2 z)^(1/6) x3) on the stabilised block; '
                                  'magnitude 1'}

    # ---------------- S2 order 1, n = 0 ----------------
    um2 = cos['models'][1]
    v3 = cos['model_without_freeze_in']
    dphi = um2['Delta_Phi_z0']
    GN_SI = 6.67430e-11
    c_SI = 299792458.0
    Msun = 1.98892e30
    bodies = {'Earth (surface)': (5.9722e24, 6.371e6), 'Sun (surface)': (Msun, 6.957e8), 'white dwarf (0.6 Msun, 8700 km)': (0.6 * Msun, 8.7e6),
              'neutron star (1.4 Msun, 12 km)': (1.4 * Msun, 1.2e4)}
    pots = {k: GN_SI * M / (R * c_SI ** 2) for k, (M, R) in bodies.items()}
    # galaxies and clusters: Phi ~ (v/c)^2 with circular / dispersion velocities 220 and 1000 km/s
    pots['Milky Way (v = 220 km/s)'] = (220e3 / c_SI) ** 2
    pots['galaxy cluster (sigma_v = 1000 km/s)'] = (1000e3 / c_SI) ** 2
    out['order1_n0'] = {'Delta_Phi_today': dphi, 'sigma8_UM2': um2['sigma8'], 'sigma8_without_freeze_in': v3['sigma8'],
                        'sigma8_LCDM': cos['models'][0]['sigma8'], 'potentials_of_bound_objects': pots,
                        'growth_suppression_g0': cos['growth_suppression_g0']}
    dmax = max(r['Delta_Phi_Weyl'] for r in dphi)
    mono = all(dphi[i]['Delta_Phi_Weyl'] > dphi[i + 1]['Delta_Phi_Weyl'] for i in range(len(dphi) - 1))
    rep.check('S2_first_order_n0', dmax < 3e-5 and mono and pots['neutron star (1.4 Msun, 12 km)'] > 0.1,
              'the first-order four-dimensional term: rms Newtonian potential per logarithmic k today Delta_Phi = %s at k = %s Mpc^-1 '
              '(decreasing with k; sigma_8 = %.4f for UM-2 (version 3), %.4f without the freeze-in fold bands); bound objects: Phi = %s (%s): the series in eps converges '
              'quickly everywhere except near neutron stars (Phi = %.2f) and black holes, where the full nonlinear equations apply' % (
                  ', '.join('%.2e' % r['Delta_Phi_Weyl'] for r in dphi), ', '.join('%g' % r['k_Mpc-1'] for r in dphi), um2['sigma8'],
                  v3['sigma8'], ', '.join('%.1e' % v for v in pots.values()), ', '.join(pots.keys()), pots['neutron star (1.4 Msun, 12 km)']))

    # ---------------- S3 Kaluza-Klein gravitons ----------------
    lev = []
    _, N0 = graviton_even_exact(eta, 0)
    fem = fem_levels(eta, 0.0, ne=400, nlev=6)
    xi = np.linspace(-1.0, 0.0, 200001)
    wq = np.full_like(xi, xi[1] - xi[0])
    wq[0] *= 0.5
    wq[-1] *= 0.5
    cQ = masses['doublet_c']['quarks']
    cL = masses['doublet_c']['leptons']

    def prof(c):
        return 2 * c * np.exp(2 * c * xi) / (1 - math.exp(-2 * c))
    pq, pl = prof(cQ), prof(cL)
    w3 = np.exp(3 * eta * xi)
    for n in range(0, 6):
        Ln, Nn = graviton_even_exact(eta, n)
        u = u_even(eta, n, xi)
        Nnum = float(np.sum(wq * w3 * u * u))
        flat = float(np.sum(wq * w3 * u)) / float(np.sum(wq * w3))         # source with the flat (zero-mode) profile
        cq = float(np.sum(wq * pq * u))
        cl = float(np.sum(wq * pl * u))
        mn = math.sqrt(Ln) / sc['fL_GeV_inv'] if n > 0 else 0.0
        lev.append({'n': n, 'Lambda_n': Ln, 'Lambda_n_fem': float(fem[n]), 'N_n': Nn, 'N_n_numerical': Nnum,
                    'alpha_fold_point': N0 / Nn, 'alpha_quark_doublet': (N0 / Nnum) * cq * cq, 'alpha_lepton_doublet': (N0 / Nnum) * cl * cl,
                    'flat_source_overlap': flat, 'm_GeV': mn, 'range_m': hbarc / mn if mn > 0 else None})
    out['kaluza_klein_gravitons'] = lev
    devL = max(abs(l_['Lambda_n'] - l_['Lambda_n_fem']) / max(l_['Lambda_n'], 1.0) for l_ in lev)
    devN = max(abs(l_['N_n'] / l_['N_n_numerical'] - 1) for l_ in lev)
    flat = max(abs(l_['flat_source_overlap']) for l_ in lev[1:])
    l1 = lev[1]
    r_lab = 50e-6
    expo = r_lab / l1['range_m']
    out['newton_law'] = {'r_m': r_lab, 'm1_r': expo, 'statement': 'V = -G m1 m2/r [1 + sum_n alpha_n e^{-m_n r}]'}
    rep.check('S3_kaluza_klein_gravitons', devL < 1e-7 and devN < 1e-6 and flat < 1e-9 and abs(l1['m_GeV'] / sc['m_KK_GeV'] - 1) < 1e-9,
              'even graviton tower (beta = 0): Lambda_n = 9 eta^2/4 + (n pi)^2 = %s agrees with finite elements to %.1e; norms (1 + a^2/q^2)/2 to '
              '%.1e; m_1 = %.2f TeV (= m_KK), range hbar c/m_1 = %.2e m; Yukawa strengths for a source at the fold alpha_n = N_0/N_n = %s, for '
              'the quark-doublet profile %s, for the lepton-doublet profile %s; a source with the flat zero-mode profile (e.g. gluon field '
              'energy) excites none (overlap %.1e); at r = 50 micrometres e^{-m_1 r} = e^{-%.1e}: Newton\'s law is exact at every '
              'measurable distance' % (
                  ', '.join('%.4f' % l_['Lambda_n'] for l_ in lev[1:4]), devL, devN, l1['m_GeV'] / 1e3, l1['range_m'],
                  ', '.join('%.4f' % l_['alpha_fold_point'] for l_ in lev[1:4]), ', '.join('%.4f' % l_['alpha_quark_doublet'] for l_ in lev[1:4]),
                  ', '.join('%.4f' % l_['alpha_lepton_doublet'] for l_ in lev[1:4]), flat, expo))

    # ---------------- S4 the radion ----------------
    envs = cpl['environments']
    rad = {k: {'delta_ln_f': v['delta_ln_f'], 'delta_ln_m_p': v['delta_ln_m_p']} for k, v in envs.items()}
    mr = sc['radion_mass_GeV']
    rdec = ana['radion_decay_estimate']
    out['radion'] = {'static_response': rad, 'mass_GeV': mr, 'range_m': hbarc / mr, 'decay': rdec}
    worst = max(abs(v['delta_ln_f']) for v in rad.values())
    worst_env = max(rad, key=lambda k: abs(rad[k]['delta_ln_f']))
    rep.check('S4_radion', worst < 1e-10,
              'the radion term sigma = delta ln f: the static response to matter is at most %.1e (%s); its range hbar c/m_r = %.2e m '
              '(m_r = %.1f TeV); the primordial oscillation decays with lifetime %.2f s/C_r (um2_analysis.py): the radion term is '
              'negligible in every observable regime after nucleosynthesis (if C_r > 6.5)' % (
                  worst, worst_env, hbarc / mr, mr / 1e3, rdec['cases'][1]['tau_s']))

    # ---------------- S5, S6 ----------------
    o2 = {'cosmological (Delta_Phi^2 at k = 1e-4 Mpc^-1)': dphi[0]['Delta_Phi_Weyl'] ** 2,
          'Sun (surface)': pots['Sun (surface)'] ** 2, 'neutron star': pots['neutron star (1.4 Msun, 12 km)'] ** 2}
    As = math.exp(3.044) * 1e-10
    r_bound = 0.036
    out['order2'] = o2
    out['tensor'] = {'r_bound_95': r_bound, 'Delta_h_bound': math.sqrt(r_bound * As), 'statement': 'not predicted by UM-2 (input)'}

    # ---------------- S7 ordering ----------------
    terms = [('order 0: gbar (background, stabilised block)', 1.0, 'always'),
             ('order 1, n = 0: Newtonian potentials of bound objects (neutron star .. Earth)', pots['neutron star (1.4 Msun, 12 km)'],
              'astrophysics; nonlinear near neutron stars'),
             ('order 1, n = 0: cosmological potential Delta_Phi (largest scales)', dphi[0]['Delta_Phi_Weyl'], 'CMB, CNB, BAO, structure'),
             ('order 1, tensor modes (bound)', math.sqrt(r_bound * As), 'CMB B modes'),
             ('order 2: cosmological Delta_Phi^2 (largest scales)', o2['cosmological (Delta_Phi^2 at k = 1e-4 Mpc^-1)'], 'CMB second-order effects'),
             ('radion sigma (static response, largest environment)', worst, 'none'),
             ('order 1, n >= 1: Kaluza-Klein gravitons at r = 50 micrometres, alpha_1 e^{-m_1 r}', 0.0, 'none below 1e-21 m')]
    out['ordering'] = [{'term': a, 'magnitude': b, 'where': c_} for a, b, c_ in terms]
    cosmo_seq = [1.0, dphi[0]['Delta_Phi_Weyl'], o2['cosmological (Delta_Phi^2 at k = 1e-4 Mpc^-1)'], worst, 0.0]
    rep.check('S7_decreasing_magnitudes', all(cosmo_seq[i] > cosmo_seq[i + 1] for i in range(len(cosmo_seq) - 1)),
              'on cosmological scales the terms decrease: order 0 (1), order 1 (Delta_Phi = %.1e), order 2 (%.1e), radion (%.1e), '
              'Kaluza-Klein (0 at any measurable distance); tensor modes below %.1e (r < 0.036, FROM MEMORY): the metric of UM-2 is a power series '
              'of terms of decreasing magnitude, with the n = 0 term carrying the CMB, CNB and BAO' % (
                  dphi[0]['Delta_Phi_Weyl'], o2['cosmological (Delta_Phi^2 at k = 1e-4 Mpc^-1)'], worst, math.sqrt(r_bound * As)))
    write_json(os.path.join(OUT, 'series.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
