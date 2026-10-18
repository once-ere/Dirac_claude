#!/usr/bin/env python3
"""UM-2 masses: every four-dimensional mass as an eigenvalue of an x0 operator on the periodic cell.

Units: t = y/L in [-1, 0] (fold t = 0, regular tip t = -1), eta = H L, eigenvalues Lambda = (m f L)^2 (bosons) and
e = eps f L (fermions).  The cell is one period of x0, pi/(6H); every eigenfunction is a function of
y(z) = ln|sin z|/(6H), z = 6 H x0, hence periodic in x0 with period pi/(6H).

Bosons (gauge fields, transverse-traceless graviton in Einstein gravity): -e^{-3 eta t} (e^{3 eta t} u')' = Lambda u,
fold u'(0) = 0 (even) or u(0) = 0 (odd), tip u'(-1) = beta u(-1) (beta >= 0: the tip sigma field; beta = 0 for unbroken
generators).  W and Z: beta_Z = beta_W/cos^2(theta_W) with theta_W the angle of the gauge couplings,
cos^2 = g^2/(g^2 + g'^2); rho = Lambda_W/(Lambda_Z cos^2) is fitted to the measured rho0 (the custodial violation beyond the
Standard-Model loops) and cos^2 is fixed by the measured masses, rho = m_W^2/(m_Z^2 cos^2) = rho0, i.e.
cos^2 = (m_W/m_Z)^2/rho0, so that the model reproduces both m_W and m_Z.  With u = e^{-3 eta t/2} w, q^2 = Lambda - 9 eta^2/4, the exact conditions are
  even: [q^2 + (3 eta/2)(beta + 3 eta/2)] sin q - beta q cos q = 0,   odd: q cos q + (beta + 3 eta/2) sin q = 0
(q = i kappa below the gap 9 eta^2/4).  Cross-checked by quadratic finite elements.
Fermions (doublet L with c_L = f mu_L L > 0, singlet R with c_R < 0, in the selected blocks; tip mixing kappa_f):
  D(e) = e^2 s_L s_R - kappa_f^2 (C_L - c_L s_L)(C_R + c_R s_R) = 0,  s = sinh(w)/w, C = cosh(w), w = sqrt(c^2 - e^2);
first order: e = kappa_f zeta(c_L) zeta(-c_R), zeta(c)^2 = c e^{-c}/sinh c (c_L > 0, c_R < 0: both zero modes at the fold;
the code evaluates zeta at |c|).  Cross-checked by direct ODE shooting.
Three generations (version of 2026-10-18, three neutrino flavours with mixing): the bulk mass of an SU(2) doublet is one
number for both of its members, and in each sector the three doublets share ONE bulk mass, fixed by the heaviest charged
fermion of the sector with equal left and right localisation (ASSUMED): c_L(leptons) by the tau, c_R(tau) = -c_L; c_Q(quarks)
by the top, c_R(t) = -c_Q.  The right-handed bulk masses of the other fermions are then fitted: e, mu; u, c; d, s, b; and the
three right-handed neutrinos to m_1 (chosen), m_2 = sqrt(m_1^2 + dm2_21), m_3 = sqrt(m_1^2 + dm2_31) of NuFIT 6.0 (normal
ordering).  With a common doublet bulk mass and unitary tip matrices the three-generation tip condition separates exactly
into three one-generation conditions with kappa_f = 1 (um2_flavour.py), so these roots are the exact masses, the neutrino tip
matrix is the PMNS matrix and the down-quark tip matrix is the CKM matrix.
Writes outputs/masses.json, reports/masses-checks.json.
"""
import math
import os
import sys

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import eigh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import ETA, M_NU_LIGHTEST_EV, NUFIT60_NO, val  # noqa: E402

mp.mp.dps = 60


# ---------------- bosons ----------------
def boson_levels(eta, beta, parity, nmax=4):
    """Lowest nmax eigenvalues Lambda of the gauge x0 operator (exact transcendental conditions)."""
    eta = mp.mpf(eta)
    beta = mp.mpf(beta)
    g = 3 * eta / 2
    levels = []
    if parity == 'even':
        # below the gap: F(kappa) = [g (beta + g) - kappa^2] sinh kappa - beta kappa cosh kappa, kappa in (0, g]
        F = lambda kp: (g * (beta + g) - kp ** 2) * mp.sinh(kp) - beta * kp * mp.cosh(kp)
        if beta == 0:
            levels.append(mp.mpf(0))
        else:
            # F(0+) ~ (g(beta+g) - beta) kp > 0 ... find a sign change on (0, g]
            grid = [g * mp.mpf(i) / 4000 for i in range(1, 4001)]
            vals = [F(x) for x in grid]
            for i in range(len(grid) - 1):
                if vals[i] == 0 or vals[i] * vals[i + 1] < 0:
                    kp = mp.findroot(F, (grid[i], grid[i + 1]), solver='anderson')
                    levels.append(g ** 2 - kp ** 2)
                    break
        Dq = lambda q: (q ** 2 + g * (beta + g)) * mp.sin(q) - beta * q * mp.cos(q)
    else:
        Dq = lambda q: q * mp.cos(q) + (beta + g) * mp.sin(q)
    # above the gap: real q
    q = mp.mpf('1e-6')
    step = mp.mpf('0.01')
    prev = Dq(q)
    while len(levels) < nmax:
        qn = q + step
        cur = Dq(qn)
        if prev * cur < 0:
            r = mp.findroot(Dq, (q, qn), solver='anderson')
            levels.append(g ** 2 + r ** 2)
        q, prev = qn, cur
    return [float(x) for x in levels[:nmax]], levels[:nmax]


def boson_fem(eta, beta, parity, ne=400, nlev=3, refine=False):
    """Quadratic finite elements for a(u,v) = int e^{3 eta t} u'v' + beta e^{-3 eta} u(-1) v(-1), m(u,v) = int e^{3 eta t} u v."""
    nodes = np.linspace(-1.0, 0.0, 2 * ne + 1)
    n = len(nodes)
    K = np.zeros((n, n))
    Mm = np.zeros((n, n))
    xg, wg = np.polynomial.legendre.leggauss(6)
    for e in range(ne):
        idx = [2 * e, 2 * e + 1, 2 * e + 2]
        a, b = nodes[idx[0]], nodes[idx[2]]
        hlen = b - a
        for xi, wi in zip(xg, wg):
            s = (xi + 1) / 2
            t = a + s * hlen
            N = np.array([2 * (s - 0.5) * (s - 1), -4 * s * (s - 1), 2 * s * (s - 0.5)])
            dN = np.array([4 * s - 3, -8 * s + 4, 4 * s - 1]) / hlen
            wt = math.exp(3 * eta * t) * wi * hlen / 2
            K[np.ix_(idx, idx)] += wt * np.outer(dN, dN)
            Mm[np.ix_(idx, idx)] += wt * np.outer(N, N)
    K[0, 0] += beta * math.exp(-3 * eta)
    keep = list(range(n))
    if parity == 'odd':
        keep = keep[:-1]          # u(0) = 0
    if beta == math.inf:
        keep = keep[1:]
    Kk = K[np.ix_(keep, keep)]
    Mk = Mm[np.ix_(keep, keep)]
    ev, vec = eigh(Kk, Mk)
    if not refine:
        return list(ev[:nlev])
    # Rayleigh quotient of the lowest eigenvector in the gradient form (sum of positive terms: no cancellation; the
    # eigenvalue error of LAPACK, ~ eps ||K||, is too large for Lambda_W ~ 1e-5)
    full = np.zeros(n)
    full[keep] = vec[:, 0]
    num = 0.0
    den = 0.0
    for e in range(ne):
        idx = [2 * e, 2 * e + 1, 2 * e + 2]
        a, b = nodes[idx[0]], nodes[idx[2]]
        hlen = b - a
        for xi, wi in zip(xg, wg):
            s = (xi + 1) / 2
            t = a + s * hlen
            N = np.array([2 * (s - 0.5) * (s - 1), -4 * s * (s - 1), 2 * s * (s - 0.5)])
            dN = np.array([4 * s - 3, -8 * s + 4, 4 * s - 1]) / hlen
            wt = math.exp(3 * eta * t) * wi * hlen / 2
            num += wt * (dN @ full[idx]) ** 2
            den += wt * (N @ full[idx]) ** 2
    if beta != math.inf:
        num += beta * math.exp(-3 * eta) * full[0] ** 2
    return [num / den]


# ---------------- fermions ----------------
def fermion_D(e, cL, cR, kf):
    e = mp.mpf(e)
    wL = mp.sqrt(cL ** 2 - e ** 2)
    wR = mp.sqrt(cR ** 2 - e ** 2)
    sL = mp.sinh(wL) / wL if wL != 0 else mp.mpf(1)
    sR = mp.sinh(wR) / wR if wR != 0 else mp.mpf(1)
    CL = mp.cosh(wL)
    CR = mp.cosh(wR)
    return e ** 2 * sL * sR - kf ** 2 * (CL - cL * sL) * (CR + cR * sR)


def zeta2(c):
    c = mp.mpf(abs(c))
    return c * mp.exp(-c) / mp.sinh(c)


def fermion_mass(cL, cR, kf):
    """Lowest positive root e of D(e) (exact); starts from the first-order value."""
    cL, cR, kf = mp.mpf(cL), mp.mpf(cR), mp.mpf(kf)
    e1 = kf * mp.sqrt(zeta2(cL) * zeta2(cR))
    f = lambda e: fermion_D(e, cL, cR, kf)
    # bracket around e1
    lo, hi = e1 / 4, e1 * 4
    hi = min(hi, min(abs(cL), abs(cR)) * mp.mpf('0.999'))
    flo, fhi = f(lo), f(hi)
    if flo * fhi > 0:
        r = mp.findroot(f, e1)
    else:
        r = mp.findroot(f, (lo, hi), solver='anderson')
    return r, e1


def fermion_shoot(e, cL, cR, kf):
    """Independent check: integrate the (L, R) block equations from the fold to the tip numerically (j = +1)."""
    def rhs(t, Y, c):
        a, b = Y
        return [c * a - e * b, e * a - c * b]
    solL = solve_ivp(rhs, [0, -1], [1.0, 0.0], args=(cL,), rtol=1e-13, atol=1e-15, method='DOP853')
    solR = solve_ivp(rhs, [0, -1], [0.0, 1.0], args=(cR,), rtol=1e-13, atol=1e-15, method='DOP853')
    aL, bL = solL.y[:, -1]
    aR, bR = solR.y[:, -1]
    # conditions bL = kf bR' and aR' = -kf aL with R scaled by beta': determinant
    return bL * aR + kf ** 2 * aL * bR


def main():
    rep = Report('masses-checks', 'UM-2: x0 eigenvalue spectra of gauge bosons, graviton and fermions; massless zero modes; '
                 'W, Z from the tip; fermion masses as exact x0 eigenvalues; fits to the measured masses')
    out = {'eta': ETA}
    eta = ETA
    g = 1.5 * eta
    # --- unbroken generators: exact spectrum ---
    lev_even, _ = boson_levels(eta, 0.0, 'even', 4)
    lev_odd, _ = boson_levels(eta, 0.0, 'odd', 3)
    exact_even = [0.0] + [g ** 2 + (n * math.pi) ** 2 for n in (1, 2, 3)]
    rep.check('unbroken_spectrum_exact', all(abs(a - b) < 1e-10 * max(1, b) for a, b in zip(lev_even, exact_even)),
              'beta = 0 (photon, gluons, graviton): Lambda = 0, 9 eta^2/4 + n^2 pi^2 (n = 1, 2, 3) = %s' % ['%.10f' % x for x in lev_even])
    fem_even = boson_fem(eta, 0.0, 'even', 400, 3)
    fem_odd = boson_fem(eta, 0.0, 'odd', 400, 3)
    dev = max(abs(a - b) / max(1, b) for a, b in zip(fem_even, lev_even[:3]))
    dev2 = max(abs(a - b) / max(1, b) for a, b in zip(fem_odd, lev_odd[:3]))
    rep.check('fem_crosscheck_unbroken', dev < 1e-8 and dev2 < 1e-8,
              'quadratic finite elements (400 elements) reproduce the even and odd levels to %.1e, %.1e' % (dev, dev2))
    rep.check('massless_zero_mode', abs(lev_even[0]) < 1e-12 and abs(fem_even[0]) < 1e-9,
              'the flat profile u = const is an exact eigenfunction with Lambda = 0: photon, gluons and graviton are massless')
    gap_ok = min(lev_odd) > g ** 2 and lev_even[1] > g ** 2
    rep.check('gap', gap_ok, 'every excitation lies above the gap 9 eta^2/4 = %.4f: first even %.6f, first odd %.6f' % (g ** 2, lev_even[1], lev_odd[0]))
    Lam1 = lev_even[1]
    out['unbroken'] = {'even': lev_even, 'odd': lev_odd, 'gap': g ** 2, 'Lambda1': Lam1}
    # --- Dirichlet tip: the largest W a positive tip term can give ---
    FD = lambda kp: g * mp.sinh(kp) - kp * mp.cosh(kp)
    kD = mp.findroot(FD, (mp.mpf('0.01'), g), solver='anderson')
    LamD = float(g ** 2 - kD ** 2)
    rep.check('dirichlet_tip_bound', abs(boson_levels(eta, 1e9, 'even', 1)[0][0] - LamD) < 1e-6 and
              abs(boson_fem(eta, math.inf, 'even', 400, 1)[0] - LamD) < 1e-7,
              'beta -> infinity: tanh(kappa) = 2 kappa/(3 eta), Lambda_D = %.8f; m_W <= sqrt(Lambda_D/Lambda_1) m_KK = %.6f m_KK' % (
                  LamD, math.sqrt(LamD / Lam1)))
    out['Lambda_D'] = LamD
    # --- W and Z ---
    mW, mZ = val('m_W_GeV'), val('m_Z_GeV')
    rho_t = val('rho0_minus_1')
    c2os = (mW / mZ) ** 2         # on-shell angle of the measured masses
    # angle of the gauge couplings, cos^2 = g^2/(g^2 + g'^2): with the measured masses, rho = m_W^2/(m_Z^2 cos^2) = rho0
    c2 = c2os / (1 + rho_t)

    def LamW(b):
        return boson_levels(eta, b, 'even', 1)[0][0]

    def rho_minus_1(bW):
        return LamW(bW) / (LamW(bW / c2) * c2) - 1.0
    # small-beta check: rho -> 1
    r_small = rho_minus_1(1e-6)
    rep.check('custodial_leading_order', abs(r_small) < 1e-5, 'beta_Z = beta_W/cos^2(theta_W) gives rho - 1 = %.2e at beta_W = 1e-6 '
              '(rho = 1 at leading order: custodial symmetry of the tip sigma field)' % r_small)
    # fit beta_W to rho - 1 = rho0 - 1
    lo, hi = 1e-4, 1.0
    for _ in range(80):
        mid = math.sqrt(lo * hi)
        if rho_minus_1(mid) > rho_t:
            hi = mid
        else:
            lo = mid
    bW = math.sqrt(lo * hi)
    bZ = bW / c2
    LW, LZ = LamW(bW), LamW(bZ)
    mKK = mW * math.sqrt(Lam1 / LW)
    mZpred = mW * math.sqrt(LZ / LW)
    out['WZ'] = {'cos2_theta_onshell': c2os, 'cos2_theta_couplings': c2, 'sin2_theta_couplings': 1 - c2, 'beta_W': bW,
                 'beta_Z': bZ, 'Lambda_W': LW, 'Lambda_Z': LZ, 'rho_minus_1': rho_minus_1(bW), 'm_KK_GeV': mKK,
                 'm_Z_pred_GeV': mZpred}
    rep.check('rho_fit', abs(rho_minus_1(bW) - rho_t) < 1e-8,
              'beta_W = %.6f gives rho_tree - 1 = %.6f (target rho0 - 1 = %.5f) with the angle of the couplings cos^2 = (m_W/m_Z)^2/rho0 '
              '= %.6f (on-shell %.6f); m_KK = m_W sqrt(Lambda_1/Lambda_W) = %.1f GeV' % (bW, rho_minus_1(bW), rho_t, c2, c2os, mKK))
    rep.check('mZ_reproduced', abs(mZpred - mZ) / mZ < 1e-8,
              'the model reproduces both masses: m_W = %.4f GeV (input) and m_Z = m_W sqrt(Lambda_Z/Lambda_W) = %.6f GeV (measured %.4f)' % (
                  mW, mZpred, mZ))
    # FEM cross-check of the W level
    fW = [boson_fem(eta, bW, 'even', ne, 1, refine=True)[0] for ne in (100, 200, 400)]
    femW = (16 * fW[2] - fW[1]) / 15          # P2 eigenvalue error O(h^4): Richardson
    order = math.log(abs(fW[0] - fW[1]) / abs(fW[1] - fW[2])) / math.log(2)
    rep.check('fem_crosscheck_W', abs(femW - LW) / LW < 1e-7,
              'quadratic finite elements on 100/200/400 elements, eigenvalue from the gradient-form Rayleigh quotient (observed order %.2f, '
              'Richardson) reproduce Lambda_W = %.10e to %.1e' % (
                  order, LW, abs(femW - LW) / LW))
    # rho - 1 as a function of m_KK (scan)
    scan = []
    for b in [0.002, 0.005, 0.01, 0.02, 0.05, 0.1]:
        scan.append({'beta_W': b, 'rho_minus_1': rho_minus_1(b), 'm_KK_GeV': mW * math.sqrt(Lam1 / LamW(b))})
    out['rho_scan'] = scan
    # --- scales ---
    bg = read_json(os.path.join(OUT, 'background.json'))
    fstar = bg['casimir_type']['f_star']
    fL_GeVinv = math.sqrt(Lam1) / mKK                 # f L in GeV^-1
    Hgev = fstar * eta / fL_GeVinv                     # H = eta f / (f L)
    hbarc = val('hbar_c_GeV_m')
    out['scales'] = {'f_star': fstar, 'fL_GeV_inv': fL_GeVinv, 'fL_m': fL_GeVinv * hbarc, 'H_GeV': Hgev,
                     'period_x0_GeV_inv': math.pi / (6 * Hgev), 'period_x0_m': math.pi / (6 * Hgev) * hbarc,
                     'gap_GeV': g / fL_GeVinv, 'm_KK_GeV': mKK, 'radion_mass_GeV': bg['radion_frequency_over_H'] * Hgev}
    rep.check('scales', Hgev > 0, 'H = %.1f GeV, f* = %.6f, proper half-cell f L = %.3e m, x0 period pi/(6H) = %.3e m, gap 3H/(2f) = %.1f GeV, '
              'radion %.1f GeV' % (Hgev, fstar, fL_GeVinv * hbarc, math.pi / (6 * Hgev) * hbarc, g / fL_GeVinv,
                                   bg['radion_frequency_over_H'] * Hgev))
    # --- fermions ---
    kf = 1.0

    def fit_c_symmetric(e_target):
        """c with c_L = c, c_R = -c such that the exact root equals e_target."""
        g_of_c = lambda c: mp.log(fermion_mass(c, -c, kf)[0]) - mp.log(e_target)
        return mp.findroot(g_of_c, mp.mpf(10))

    def fit_c_right(cL, e_target):
        """c_R < 0 at fixed c_L such that the exact root equals e_target (start: the first-order value)."""
        z = e_target / mp.sqrt(zeta2(cL))                       # zeta(|c_R|) at first order
        c0 = mp.findroot(lambda c: mp.log(zeta2(c)) - 2 * mp.log(z), mp.mpf(5) if z < 0.5 else mp.mpf('0.5'))
        g_of_c = lambda cR: mp.log(fermion_mass(cL, cR, kf)[0]) - mp.log(e_target)
        return mp.findroot(g_of_c, -c0)

    def record(m, cL, cR):
        r, e1 = fermion_mass(cL, cR, kf)
        return {'m_GeV': m, 'c_L': float(cL), 'c_R': float(cR), 'mu_L_over_H': float(cL) / (fstar * eta),
                'mu_R_over_H': float(cR) / (fstar * eta), 'e_exact': float(r), 'e_first_order': float(e1),
                'zeta2_L': float(zeta2(cL)), 'zeta2_R': float(zeta2(cR)), 'width_L_t': 1.0 / (2 * float(cL)),
                'width_R_t': 1.0 / (2 * abs(float(cR))), 'width_L_m': fL_GeVinv * hbarc / (2 * float(cL)),
                'width_R_m': fL_GeVinv * hbarc / (2 * abs(float(cR)))}

    nu = {k: v[0] for k, v in NUFIT60_NO.items()}
    m1 = M_NU_LIGHTEST_EV
    m2 = math.sqrt(m1 ** 2 + nu['dm2_21_eV2'])
    m3 = math.sqrt(m1 ** 2 + nu['dm2_31_eV2'])
    targets = {'e': val('m_e_MeV') * 1e-3, 'mu': val('m_mu_MeV') * 1e-3, 'tau': val('m_tau_MeV') * 1e-3,
               'nu1': m1 * 1e-9, 'nu2': m2 * 1e-9, 'nu3': m3 * 1e-9,
               'u': val('m_u_MeV_2GeV') * 1e-3, 'c': val('m_c_GeV_mc'), 't': val('m_t_GeV'),
               'd': val('m_d_MeV_2GeV') * 1e-3, 's': val('m_s_MeV_2GeV') * 1e-3, 'b': val('m_b_GeV_mb')}
    sectors = {'leptons': ('tau', ['e', 'mu', 'nu1', 'nu2', 'nu3']),
               'quarks': ('t', ['u', 'c', 'd', 's', 'b'])}
    ferm = {}
    doublet_c = {}
    for sector, (heaviest, others) in sectors.items():
        cD = fit_c_symmetric(mp.mpf(targets[heaviest]) * fL_GeVinv)      # c_L of the three doublets of the sector
        doublet_c[sector] = float(cD)
        ferm[heaviest] = record(targets[heaviest], cD, -cD)
        for name in others:
            ferm[name] = record(targets[name], cD, fit_c_right(cD, mp.mpf(targets[name]) * fL_GeVinv))
    out['fermions'] = ferm
    out['kappa_f'] = kf
    out['doublet_c'] = doublet_c
    out['neutrino_masses_eV'] = {'m1': m1, 'm2': m2, 'm3': m3, 'sum': m1 + m2 + m3, 'ordering': 'normal',
                                 'source': 'NuFIT 6.0 IC24 NO splittings; m1 ASSUMED'}
    order = ['e', 'mu', 'tau', 'nu1', 'nu2', 'nu3', 'u', 'c', 't', 'd', 's', 'b']
    first_vs_exact = {n: abs(ferm[n]['e_first_order'] / ferm[n]['e_exact'] - 1) for n in ferm}
    rep.check('fermion_fit', all(abs(ferm[n]['e_exact'] / (targets[n] * fL_GeVinv) - 1) < 1e-12 for n in targets),
              'with the universal tip mixing kappa_f = 1 the exact x0 eigenvalues reproduce all twelve masses: the three lepton doublets '
              'share c_L = %.4f (fixed by the tau, c_R(tau) = -c_L), the three quark doublets share c_Q = %.4f (fixed by the top, '
              'c_R(t) = -c_Q); right-handed bulk masses c_R = %s; neutrino masses %.4e, %.4e, %.4e eV (normal ordering, m1 chosen)' % (
                  doublet_c['leptons'], doublet_c['quarks'], ', '.join('%s %.4f' % (n, ferm[n]['c_R']) for n in order), m1, m2, m3))
    worst = max(first_vs_exact, key=first_vs_exact.get)
    rep.check('first_order_formula', max(first_vs_exact.values()) < 0.05,
              'the first-order formula e = kappa_f zeta(c_L) zeta(-c_R) agrees with the exact root to %s; the largest deviation, %.1e '
              '(%s), belongs to the broadest profiles; every quoted mass is the exact root' % (
                  ', '.join('%s %.1e' % (n, first_vs_exact[n]) for n in order), first_vs_exact[worst], worst))
    # ODE shooting cross-check for the electron, the tau, the top and a broad mode
    sh = []
    for (ca, cb, kk) in [(ferm['e']['c_L'], ferm['e']['c_R'], kf), (ferm['tau']['c_L'], ferm['tau']['c_R'], kf),
                         (ferm['t']['c_L'], ferm['t']['c_R'], kf), (1.0, -1.0, 1.0)]:
        r, _ = fermion_mass(ca, cb, kk)
        val_at = fermion_shoot(float(r), ca, cb, kk)
        scale = abs(fermion_shoot(float(r) * 1.01, ca, cb, kk) - val_at)
        sh.append(abs(val_at) / scale if scale > 0 else abs(val_at))
    rep.check('shooting_crosscheck', all(s < 1e-6 for s in sh),
              'direct ODE integration (DOP853, rtol 1e-13) of the coupled (L, R) problem: the determinant vanishes at the transfer-'
              'matrix root (relative residuals %s for e, tau, t and a broad mode c = 1)' % ['%.1e' % s for s in sh])
    r1, e11 = fermion_mass(1.0, -1.0, 1.0)
    out['broad_mode_c1'] = {'exact': float(r1), 'first_order': float(e11)}
    # hierarchy statement: at a common doublet c_L, a sharper right-handed localisation gives a lighter fermion
    lep = sorted(['e', 'mu', 'tau', 'nu1', 'nu2', 'nu3'], key=lambda n: targets[n], reverse=True)
    up = ['t', 'c', 'u']
    dn = ['b', 's', 'd']
    mono = all(all(abs(ferm[a]['c_R']) < abs(ferm[b]['c_R']) for a, b in zip(s, s[1:])) for s in (lep, up, dn))
    rep.check('localisation_lowers_mass', mono,
              'the lighter the fermion, the sharper its right-handed x0 localisation at the fold (at the common doublet bulk mass of its '
              'sector): |c_R| = %s' % ', '.join('%s %.3f' % (n, abs(ferm[n]['c_R'])) for n in lep + up + dn))
    write_json(os.path.join(OUT, 'masses.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
