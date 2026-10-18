#!/usr/bin/env python3
"""UM-2 flavour: three generations of quarks and leptons, their masses and mixing from the x0 mechanism (version of
2026-10-18: three neutrino flavours with mixing; three quark generations).

Units: t = y/L in [-1, 0] (fold t = 0, regular tip t = -1), fermion eigenvalues e = eps f L, bulk masses c = f mu L.

F1  The exact three-generation tip condition.  In a sector with doublet bulk masses c_D (one per generation, the same for
    both members of a doublet), right-handed bulk masses c_R,i and a tip matrix kappa (3 x 3), the doublet and singlet
    solutions of the block equations a' = c a - e b, b' = e a - c b (k = 0, j = +1) that satisfy the fold conditions reach the
    tip with (a_L, b_L) = (C - c s, -s e) and (a_R, b_R) = (s e, C + c s), s = sinh(w)/w, C = cosh(w), w = sqrt(c^2 - e^2).  The tip
    mixing conditions b_L = kappa b_R, a_R = -kappa^dagger a_L (matrix form) give
        [diag(b_L,alpha) + kappa diag(b_R,i/a_R,i) kappa^dagger diag(a_L,alpha)] A = 0,
    so the masses are the roots of det[...] = 0 and A (the doublet flavour vector) the left-handed mixing.  For a COMMON doublet
    bulk mass and a UNITARY kappa the determinant factorises into the one-generation conditions with kappa_f = 1:
        det = prod_i (b_L a_R,i + a_L b_R,i)/a_R,i,  A_i = kappa e_i  (exact),
    hence the masses of um2_spectra.py are exact and the mixing matrix equals the tip matrix.  Verified with mpmath: the roots of
    the 3 x 3 determinant and its null vectors for kappa_nu = U_PMNS (NuFIT 6.0, normal ordering) and kappa_d = V_CKM (PDG).
F2  A general (non-unitary, random complex) tip matrix: the exact roots agree with the first-order prediction, the singular
    values of zeta(c_D) kappa diag(zeta(-c_R,i)); the left-handed mixing is the left singular basis.
F3  The PMNS matrix (standard parametrisation, Dirac phase), its unitarity and Jarlskog invariant
    J = c12 s12 c23 s23 c13^2 s13 sin(delta); the CKM matrix likewise (J = 3.12e-5).
F4  No tree-level flavour-changing neutral currents from the Kaluza-Klein gauge bosons: the coupling of the first even KK
    mode to a zero mode is the overlap int |chi_c|^2 u_1 dt (u_1 normalised like the zero mode with the weight e^{3 eta t});
    with a common doublet bulk mass the left-handed couplings are flavour universal, and the right-handed rotations are the
    identity, so the KK couplings are diagonal in the mass basis (off-diagonal elements computed: zero to round-off).  The
    counterfactual with the one-generation rule c_L = -c_R per fermion would give non-universal couplings (computed).
F5  Charged-lepton flavour violation through neutrino mixing (Dirac neutrinos): BR(mu -> e gamma) =
    (3 alpha/(32 pi)) |sum_i U*_mu i U_e i m_i^2/m_W^2|^2.
F6  Universality: the W couples every charged lepton to its neutrino with the same strength (common c_L).
Writes outputs/flavour.json and reports/flavour-checks.json.
"""
import cmath
import math
import os
import sys

import mpmath as mp
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import CKM_PDG2024, CKM_SOURCE, ETA, NUFIT60_NO, NUFIT60_SOURCE, val  # noqa: E402
from um2_spectra import fermion_D, fermion_mass  # noqa: E402

mp.mp.dps = 50


def mixing_matrix(s12, s13, s23, delta):
    """Standard parametrisation U = R23 U13(delta) R12 (PDG convention)."""
    c12, c13, c23 = math.sqrt(1 - s12 ** 2), math.sqrt(1 - s13 ** 2), math.sqrt(1 - s23 ** 2)
    ed = cmath.exp(-1j * delta)
    return np.array([
        [c12 * c13, s12 * c13, s13 * ed],
        [-s12 * c23 - c12 * s23 * s13 / ed, c12 * c23 - s12 * s23 * s13 / ed, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 / ed, -c12 * s23 - s12 * c23 * s13 / ed, c23 * c13]], dtype=complex)


def mixing_matrix_mp(s12, s13, s23, delta):
    """The same matrix in mpmath at the working precision (exactly unitary to 50 digits)."""
    s12, s13, s23, delta = mp.mpf(s12), mp.mpf(s13), mp.mpf(s23), mp.mpf(delta)
    c12, c13, c23 = mp.sqrt(1 - s12 ** 2), mp.sqrt(1 - s13 ** 2), mp.sqrt(1 - s23 ** 2)
    ed = mp.expj(-delta)
    return mp.matrix([
        [c12 * c13, s12 * c13, s13 * ed],
        [-s12 * c23 - c12 * s23 * s13 / ed, c12 * c23 - s12 * s23 * s13 / ed, s23 * c13],
        [s12 * s23 - c12 * c23 * s13 / ed, -c12 * s23 - s12 * c23 * s13 / ed, c23 * c13]])


def tip_values(c, e):
    """(a_L, b_L) of a doublet and (a_R, b_R) of a singlet at the tip (exact; mpmath)."""
    c, e = mp.mpf(c), mp.mpf(e)
    w = mp.sqrt(c * c - e * e)
    s = mp.sinh(w) / w
    C = mp.cosh(w)
    return (C - c * s, -s * e), (s * e, C + c * s)


def tip_matrix(e, cD, cR, kappa):
    """The 3 x 3 matrix [diag(b_L) + kappa diag(b_R/a_R) kappa^dagger diag(a_L)] of the three-generation tip condition."""
    aL = [tip_values(c, e)[0][0] for c in cD]
    bL = [tip_values(c, e)[0][1] for c in cD]
    rR = [tip_values(c, e)[1][1] / tip_values(c, e)[1][0] for c in cR]
    if isinstance(kappa, mp.matrix):
        K = kappa
    else:
        K = mp.matrix([[mp.mpc(complex(kappa[i, j])) for j in range(3)] for i in range(3)])
    Kd = K.H
    M = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            M[i, j] = (bL[i] if i == j else 0) + sum(K[i, k] * rR[k] * Kd[k, j] for k in range(3)) * aL[j]
    return M


def tip_det(e, cD, cR, kappa):
    return mp.det(tip_matrix(e, cD, cR, kappa))


def root_near(e0, cD, cR, kappa, rel=mp.mpf(10) ** (-40)):
    """The root of the 3 x 3 tip determinant in [0.98 e0, 1.02 e0] by the Illinois method on the real, normalised function
    g(e) = Re(det(e)/p)/|det(e_lo)| (the determinant is real up to a constant phase p; it is tiny in absolute terms, so the
    iteration stops on the relative width of the bracket, never on |g|)."""
    f = lambda e: tip_det(e, cD, cR, kappa)
    lo, hi = e0 * mp.mpf('0.98'), e0 * mp.mpf('1.02')
    flo = f(lo)
    ph = flo / abs(flo)
    scale = abs(flo)
    g = lambda e: mp.re(f(e) / ph) / scale
    glo, ghi = g(lo), g(hi)
    if glo * ghi > 0:
        raise RuntimeError('no sign change of the tip determinant near %s' % mp.nstr(e0, 10))
    side = 0
    for _ in range(400):
        x = (lo * ghi - hi * glo) / (ghi - glo)
        gx = g(x)
        if gx * ghi < 0:
            lo, glo = hi, ghi
            hi, ghi = x, gx
            side = 0
        else:
            hi, ghi = x, gx
            if side == 1:
                glo /= 2
            side = 1
        if abs(hi - lo) < rel * abs(x):
            return x
    return x


def root_1gen(cD, cR, rel=mp.mpf(10) ** (-40)):
    """The one-generation root (kappa_f = 1) refined by the same Illinois iteration on the normalised D(e) (fermion_mass stops on
    |D|, which is tiny in absolute terms for sharply localised modes)."""
    e0 = fermion_mass(cD, cR, 1.0)[0]
    cD, cR = mp.mpf(cD), mp.mpf(cR)
    lo, hi = e0 * mp.mpf('0.98'), e0 * mp.mpf('1.02')
    scale = abs(fermion_D(lo, cD, cR, 1))
    g = lambda e: fermion_D(e, cD, cR, 1) / scale
    glo, ghi = g(lo), g(hi)
    side = 0
    for _ in range(400):
        x = (lo * ghi - hi * glo) / (ghi - glo)
        gx = g(x)
        if gx * ghi < 0:
            lo, glo = hi, ghi
            hi, ghi = x, gx
            side = 0
        else:
            hi, ghi = x, gx
            if side == 1:
                glo /= 2
            side = 1
        if abs(hi - lo) < rel * abs(x):
            return x
    return x


def null_vector(M):
    """Unit null vector of a (nearly singular) 3 x 3 mpmath matrix: the right singular vector of the smallest singular value."""
    A = np.array([[complex(M[i, j]) for j in range(3)] for i in range(3)])
    # scale rows for conditioning
    u, s, vh = np.linalg.svd(A)
    v = vh.conj().T[:, -1]
    return v / np.linalg.norm(v), s


def zero_mode_density(c, t):
    """|chi|^2 of a chiral zero mode with bulk mass |c| on t in [-1, 0], normalised to 1 (localised at the fold)."""
    c = abs(c)
    return 2 * c * np.exp(2 * c * t) / (1 - math.exp(-2 * c))


def kk_profile(t, eta, Lam):
    """First even KK mode of the unbroken gauge operator, u = e^{-3 eta t/2} [cos(q t) + (g/q) sin(q t)], q^2 = Lam - g^2."""
    g = 1.5 * eta
    q = math.sqrt(Lam - g * g)
    return np.exp(-1.5 * eta * t) * (np.cos(q * t) + (g / q) * np.sin(q * t))


def main():
    rep = Report('flavour-checks', 'UM-2 flavour: three generations, the exact three-generation tip condition, PMNS and CKM from the '
                 'tip matrices, no tree-level FCNC from the KK gauge bosons, mu -> e gamma, universality')
    out = {}
    masses = read_json(os.path.join(OUT, 'masses.json'))
    F = masses['fermions']
    dc = masses['doublet_c']
    fL = masses['scales']['fL_GeV_inv']
    # ---------------- F3: the mixing matrices ----------------
    nu = {k: v[0] for k, v in NUFIT60_NO.items()}
    s12, s13, s23 = math.sqrt(nu['sin2_theta12']), math.sqrt(nu['sin2_theta13']), math.sqrt(nu['sin2_theta23'])
    dl = math.radians(nu['delta_CP_deg'])
    U = mixing_matrix(s12, s13, s23, dl)
    ck = {k: v[0] for k, v in CKM_PDG2024.items()}
    V = mixing_matrix(ck['s12'], ck['s13'], ck['s23'], ck['delta_rad'])
    JU = float(np.imag(U[0, 1] * U[1, 2] * np.conj(U[0, 2]) * np.conj(U[1, 1])))
    JU_formula = math.sqrt(1 - s12 ** 2) * s12 * math.sqrt(1 - s23 ** 2) * s23 * (1 - s13 ** 2) * s13 * math.sin(dl)
    JV = float(np.imag(V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])))
    unitU = float(np.max(np.abs(U @ U.conj().T - np.eye(3))))
    unitV = float(np.max(np.abs(V @ V.conj().T - np.eye(3))))
    out['PMNS'] = {'source': NUFIT60_SOURCE, 'abs': np.abs(U).tolist(), 're': U.real.tolist(), 'im': U.imag.tolist(),
                   'J': JU, 'J_max': JU_formula / math.sin(dl), 'angles_deg': {'theta12': math.degrees(math.asin(s12)),
                   'theta13': math.degrees(math.asin(s13)), 'theta23': math.degrees(math.asin(s23)), 'delta': nu['delta_CP_deg']}}
    out['CKM'] = {'source': CKM_SOURCE, 'abs': np.abs(V).tolist(), 're': V.real.tolist(), 'im': V.imag.tolist(), 'J': JV}
    rep.check('PMNS_unitary_and_Jarlskog', unitU < 1e-15 and abs(JU - JU_formula) < 1e-15 and abs(JU_formula / math.sin(dl) - 0.0333) < 0.0007,
              'U = R23 U13(delta) R12 with NuFIT 6.0 NO (theta12 %.2f deg, theta13 %.2f, theta23 %.2f, delta %.0f): unitary to %.1e; '
              'J = Im(U_e2 U_mu3 U*_e3 U*_mu2) = %.5f = c12 s12 c23 s23 c13^2 s13 sin(delta); J_max = %.4f (NuFIT: 0.0333 +- 0.0007)' % (
                  out['PMNS']['angles_deg']['theta12'], out['PMNS']['angles_deg']['theta13'], out['PMNS']['angles_deg']['theta23'],
                  nu['delta_CP_deg'], unitU, JU, JU_formula / math.sin(dl)))
    rep.check('CKM_unitary_and_Jarlskog', unitV < 1e-15 and abs(JV - ck['J']) < CKM_PDG2024['J'][1],
              'V = R23 U13(delta) R12 with the PDG global fit (s12 %.5f, s13 %.6f, s23 %.5f, delta %.3f rad): unitary to %.1e; '
              'J = %.3e (PDG 3.12e-5 +- 0.13e-5); |V| = %s' % (ck['s12'], ck['s13'], ck['s23'], ck['delta_rad'], unitV, JV,
                                                               np.array2string(np.abs(V), precision=5)))
    # ---------------- F1: exactness of the three-generation tip condition ----------------
    Ump = mixing_matrix_mp(s12, s13, s23, dl)
    Vmp = mixing_matrix_mp(ck['s12'], ck['s13'], ck['s23'], ck['delta_rad'])
    sectors = {
        'neutrinos (kappa = U_PMNS)': ([dc['leptons']] * 3, [F['nu1']['c_R'], F['nu2']['c_R'], F['nu3']['c_R']], U,
                                       ['nu1', 'nu2', 'nu3'], Ump),
        'charged leptons (kappa = 1)': ([dc['leptons']] * 3, [F['e']['c_R'], F['mu']['c_R'], F['tau']['c_R']], np.eye(3),
                                        ['e', 'mu', 'tau'], mp.eye(3)),
        'up quarks (kappa = 1)': ([dc['quarks']] * 3, [F['u']['c_R'], F['c']['c_R'], F['t']['c_R']], np.eye(3), ['u', 'c', 't'],
                                  mp.eye(3)),
        'down quarks (kappa = V_CKM)': ([dc['quarks']] * 3, [F['d']['c_R'], F['s']['c_R'], F['b']['c_R']], V, ['d', 's', 'b'], Vmp),
    }
    exact = {}
    worst_mass = 0.0
    worst_vec = 0.0
    for name, (cD, cR, kap, labels, kmp) in sectors.items():
        roots = []
        vecs = []
        for i, lab in enumerate(labels):
            e0 = root_1gen(cD[i], cR[i])                    # the one-generation root at full precision (same c values)
            r = root_near(e0, cD, cR, kmp)
            roots.append(r)
            M = tip_matrix(r, cD, cR, kmp)
            v, sv = null_vector(M)
            # compare with column i of kappa up to a phase
            col = kap[:, i]
            ov = abs(np.vdot(col, v))
            vecs.append(1 - ov)
            worst_mass = max(worst_mass, float(abs(r / e0 - 1)))
            worst_vec = max(worst_vec, 1 - ov)
        exact[name] = {'roots': [float(x) for x in roots], 'one_generation_roots': [F[l]['e_exact'] for l in labels],
                       'null_vector_deviation_from_kappa_columns': vecs}
    out['three_generation_tip_condition'] = exact
    rep.check('three_generation_tip_condition_exact', worst_mass < 1e-35 and worst_vec < 1e-12,
              'the roots of the exact 3 x 3 tip determinant det[diag(b_L) + kappa diag(b_R/a_R) kappa^dagger diag(a_L)] (mpmath, 50 digits) '
              'equal the one-generation roots with kappa_f = 1 to %.1e (relative) in all four sectors (neutrinos with kappa = U_PMNS, charged '
              'leptons, up quarks, down quarks with kappa = V_CKM), and the null vectors are the columns of the tip matrix to %.1e: with a '
              'common doublet bulk mass the masses of um2_spectra.py are exact and the mixing matrices ARE the tip matrices' % (
                  worst_mass, worst_vec))
    # ---------------- F2: a general tip matrix ----------------
    rng = np.random.default_rng(20261018)
    Kr = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2)
    cD = [dc['leptons']] * 3
    cR = [-6.0, -9.0, -12.0]
    from um2_spectra import zeta2
    Zr = np.diag([float(mp.sqrt(zeta2(c))) for c in cR])
    zL = float(mp.sqrt(zeta2(cD[0])))
    Mfo = zL * Kr @ Zr
    uf, sf, vf = np.linalg.svd(Mfo)
    gen = []
    for i in range(3):
        r = root_near(mp.mpf(sf[i]), cD, cR, Kr)
        v, _ = null_vector(tip_matrix(r, cD, cR, Kr))
        gen.append({'first_order': float(sf[i]), 'exact': float(r), 'rel_dev': float(abs(r / sf[i] - 1)),
                    'left_vector_overlap': float(abs(np.vdot(uf[:, i], v)))})
    out['general_tip_matrix_example'] = gen
    rep.check('general_tip_matrix', all(g['rel_dev'] < 1e-3 and g['left_vector_overlap'] > 1 - 1e-6 for g in gen),
              'for a random complex O(1) tip matrix (common c_L = %.4f, c_R = -6, -9, -12) the exact roots agree with the singular values '
              'of zeta(c_L) kappa diag(zeta(-c_R)) to %s and the null vectors with its left singular vectors (overlaps %s): masses and '
              'left-handed mixing follow from the tip matrix and the wave functions at the tip' % (
                  cD[0], ', '.join('%.1e' % g['rel_dev'] for g in gen), ', '.join('%.9f' % g['left_vector_overlap'] for g in gen)))
    # ---------------- F4: no tree-level FCNC from the KK gauge bosons ----------------
    eta = ETA
    Lam1 = masses['unbroken']['Lambda1']
    t = np.linspace(-1.0, 0.0, 400001)
    u1 = kk_profile(t, eta, Lam1)
    w = np.exp(3 * eta * t)
    norm0 = np.trapezoid(w, t)
    u1 = u1 * math.sqrt(norm0 / np.trapezoid(w * u1 * u1, t))

    def g1(c):
        return float(np.trapezoid(zero_mode_density(c, t) * u1, t))
    couplings = {}
    offdiag = 0.0
    for sector, (cD, cR, kap, labels, kmp) in sectors.items():
        gL = np.diag([g1(c) for c in cD]).astype(complex)
        gR = np.diag([g1(c) for c in cR]).astype(complex)
        # mass basis: left-handed fields rotate with kappa (the null vectors), right-handed with the identity
        gL_mass = kap.conj().T @ gL @ kap
        offdiag = max(offdiag, float(np.max(np.abs(gL_mass - np.diag(np.diag(gL_mass))))))
        couplings[sector] = {'left_KK1_over_zero_mode': [float(np.real(gL_mass[i, i])) for i in range(3)],
                             'right_KK1_over_zero_mode': [float(np.real(gR[i, i])) for i in range(3)]}
    out['KK1_couplings'] = couplings
    # counterfactual: doublets with different c_L (one-generation rule c_L = -c_R per fermion) in the neutrino sector
    cf_cD = [abs(F['e']['c_R']), abs(F['mu']['c_R']), abs(F['tau']['c_R'])]
    gLc = np.diag([g1(c) for c in cf_cD]).astype(complex)
    gLc_mass = U.conj().T @ gLc @ U
    cf_off = float(np.max(np.abs(gLc_mass - np.diag(np.diag(gLc_mass)))))
    out['KK1_counterfactual_noncommon_cL'] = {'c_L': cf_cD, 'max_offdiagonal': cf_off}
    rep.check('no_tree_level_FCNC_from_KK', offdiag < 1e-12 and cf_off > 1e-3,
              'the coupling of the first even KK gauge mode to the zero modes, relative to the zero mode: left-handed leptons %.5f '
              '(universal: common c_L), left-handed quarks %.5f; in the mass basis the largest off-diagonal element is %.1e: no tree-level '
              'flavour-changing neutral current from the KK gauge bosons. With different doublet bulk masses (here |c_R| of e, mu, tau used as '
              'c_L) the PMNS rotation would create off-diagonal KK couplings up to %.3f' % (
                  couplings['charged leptons (kappa = 1)']['left_KK1_over_zero_mode'][0],
                  couplings['up quarks (kappa = 1)']['left_KK1_over_zero_mode'][0], offdiag, cf_off))
    # ---------------- F5: mu -> e gamma ----------------
    mW = val('m_W_GeV')
    alpha = 1 / val('alpha_inv_0')
    mnu = masses['neutrino_masses_eV']
    mi = np.array([mnu['m1'], mnu['m2'], mnu['m3']]) * 1e-9
    amp = sum(np.conj(U[1, i]) * U[0, i] * mi[i] ** 2 for i in range(3)) / mW ** 2
    br = 3 * alpha / (32 * math.pi) * abs(amp) ** 2
    out['mu_to_e_gamma'] = {'BR': br, 'MEG_II_limit_FROM_MEMORY': 3.1e-13}
    rep.check('mu_to_e_gamma', br < 1e-50,
              'BR(mu -> e gamma) = (3 alpha/(32 pi)) |sum_i U*_mu i U_e i m_i^2/m_W^2|^2 = %.1e (Dirac neutrinos, GIM-suppressed): '
              'charged-lepton flavour violation is unobservable, as in the Standard Model with neutrino masses' % br)
    # ---------------- F6: universality ----------------
    univ = [F[n]['c_L'] for n in ('e', 'mu', 'tau', 'nu1', 'nu2', 'nu3')]
    univq = [F[n]['c_L'] for n in ('u', 'c', 't', 'd', 's', 'b')]
    rep.check('lepton_universality', max(univ) - min(univ) == 0 and max(univq) - min(univq) == 0,
              'every lepton doublet has c_L = %.6f and every quark doublet c_Q = %.6f: the W and Z zero modes couple to all generations '
              'with the same strength (lepton universality; the CKM and PMNS matrices carry the whole flavour structure of the charged '
              'currents)' % (univ[0], univq[0]))
    out['doublet_c'] = dc
    write_json(os.path.join(OUT, 'flavour.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
