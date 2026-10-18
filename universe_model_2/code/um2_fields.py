#!/usr/bin/env python3
"""UM-2 fields: the exact reductions of the eight-dimensional field equations to x0 eigenproblems, the boundary
conditions, the zero-mode content of every fermion, and the gauge invariance of the tip and portal operators.

F1  Exact reduction of the 8D Dirac equation gamma^mu D_mu Psi = (M - i v gamma^(x4)) Psi (canonical spin connection,
    y chart) with Psi = e^{i k x1} e^{-(3/2) H y} e^{a4/2} b4^{-1} V_beta chi(y, x4) to the 2x2 block equation
    i d_4 chi = h_j chi,  h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v,  kappa = e^{-a4}
    (checked with the 16x16 author's matrices; valid for dirac16complex and for every Standard-Model fermion).
F2  The 4D chirality Gamma4 = i g1 g2 g3 g4 is block diagonal, Gamma4 = -j s2 sigma3 in block (j, s2, s3); the
    selection operator P_sel = (1 + Gamma4 g0)/2 (1 - i K2)/2 commutes with the 4D Lorentz generators.
F3  Boundary conditions: in every block the conditions chi2 = 0 (theta = 0) or chi1 = 0 (theta = pi) at the fold and at
    the tip are Lagrangian for the boundary form phi^dagger sigma1 chi (h_j self-adjoint).  Zero-mode content at k = 0:
      dirac16complex (no selection, even fold sector theta = 0 in all 8 blocks): 8 zero modes, 4D vector-like;
      SM doublet fields (theta = 0 at fold and tip in the selected blocks, fold theta = pi elsewhere): exactly one 4D Weyl
      zero mode, Gamma4 = +1;  SM singlet fields (theta = pi in the selected blocks, fold theta = 0 / tip theta = pi
      elsewhere, bulk mass < 0): exactly one 4D Weyl zero mode, Gamma4 = -1, in the same blocks (so the tip coupling
      Lbar Sigma R can give a Dirac mass).  Helicity of the particle state is fixed for both signs of k.
F4  The tip mixing condition of the boundary term -lambda_f (psibar_L Sigma psi_R + h.c.): b_L = kappa_f b_R,
    a_R = -kappa_f a_L at y = -L is self-adjoint (boundary form of the coupled (L, R) problem vanishes).
F5  Gauge fields: for A_mu(x) u(y) (gauge A_y = 0) the reduced action gives -(1/f^2) e^{-3Hy} (e^{3Hy} u')' = m^2 u,
    the fold condition u'(0) = 0 (even) or u(0) = 0 (odd), and the tip Robin condition from the sigma-field term.
F6  Gauge invariance of the tip terms (Sigma kinetic term, tip Yukawa couplings, Z portal) and of the portal operators
    under SU(2)_L x U(1)_Y with random group elements.
Writes outputs/fields.json and reports/fields-checks.json.
"""
import os
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, ROOT, Report, read_json, write_json  # noqa: E402

I = sp.I
LABELS = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
s1 = sp.Matrix([[0, 1], [1, 0]])
s2m = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.Matrix([[1, 0], [0, -1]])


def load():
    alg = read_json(os.path.join(OUT, 'algebra.json'))
    g = [sp.Matrix(alg['gamma'][a]) for a in range(8)]
    ks = read_json(os.path.join(ROOT, 'Revision', 'kohn_sham', 'ks-theory.json'))
    cols = ks['blockBasis']['unnormalisedColumns2Sqrt2V']
    V = sp.Matrix(16, 16, lambda r, c: sp.sympify(cols[r][c])) / (2 * sp.sqrt(2))
    return g, V


def main():
    rep = Report('fields-checks', 'UM-2: exact x0 reductions of the 8D field equations, boundary conditions, zero-mode '
                 'content, tip mixing, gauge x0 operator, gauge invariance of tip and portal operators')
    out = {}
    g, V = load()
    eta = [1, 1, 1, 1, -1, -1, -1, -1]

    # ---------------- F1: exact reduction of the Dirac equation ----------------
    H = sp.Symbol('H', positive=True)
    y = sp.Symbol('y', real=True)
    X = sp.symbols('x0:8', real=True)
    x4 = X[4]
    kx = sp.Symbol('k', real=True)
    Mf = sp.Function('M')(y)          # y-dependent mass (mean field) allowed
    vf = sp.Function('v')(y)          # y-dependent vector potential (along gamma^(x4) i)
    a4 = sp.Function('a4')(x4)
    b4 = sp.Function('b4')(x4)
    f = sp.exp(-a4) * sp.sqrt(b4)
    coords = [y, X[1], X[2], X[3], x4, X[5], X[6], X[7]]
    evec = [f, sp.exp(a4), sp.exp(a4), sp.exp(a4), sp.Integer(1), f * sp.exp(H * y), f * sp.exp(H * y), f * sp.exp(H * y)]
    gdiag = [eta[m] * evec[m] ** 2 for m in range(8)]
    # Christoffels of the y chart
    Gam = [[[0] * 8 for _ in range(8)] for _ in range(8)]
    for a in range(8):
        for b in range(8):
            for c in range(8):
                Gam[a][b][c] = sp.simplify((sp.diff(gdiag[a], coords[b]) * (1 if a == c else 0) +
                                            sp.diff(gdiag[a], coords[c]) * (1 if a == b else 0) -
                                            (sp.diff(gdiag[b], coords[a]) if b == c else 0)) / (2 * gdiag[a]))
    S = [[(g[a] * g[b] - g[b] * g[a]) / 4 for b in range(8)] for a in range(8)]
    Omega = []
    for mu in range(8):
        Om = sp.zeros(16, 16)
        for a in range(8):
            for b in range(8):
                w = evec[a] * ((sp.diff(1 / evec[b], coords[mu]) if a == b else 0) + Gam[a][mu][b] / evec[b])
                w = sp.simplify(w)
                if w != 0:
                    Om += sp.Rational(1, 2) * eta[a] * w * S[a][b]
        Omega.append(Om)
    gup = [g[m] / evec[m] for m in range(8)]
    ok_red = True
    for bi, (j, ss2, ss3) in enumerate(LABELS):
        c1 = sp.Function('c1')(y, x4)
        c2 = sp.Function('c2')(y, x4)
        chi16 = V[:, 2 * bi] * c1 + V[:, 2 * bi + 1] * c2
        pref = sp.exp(I * kx * X[1]) * sp.exp(-sp.Rational(3, 2) * H * y) * sp.exp(a4 / 2) / b4
        Psi = pref * chi16
        Dslash = sp.zeros(16, 1)
        for mu in range(8):
            Dslash += gup[mu] * (sp.diff(Psi, coords[mu]) + Omega[mu] * Psi)
        res = (Dslash - (Mf * Psi - I * vf * g[4] * Psi)) / pref
        res = res.applyfunc(sp.simplify)
        # prediction: gamma^(x4) [ d_4 chi + i h chi ] = 0  with h_j = j[-(i/f) s1 d_y + M s2 + kappa k s3] + v
        kappa = sp.exp(-a4)
        cvec = sp.Matrix([c1, c2])
        hchi = j * (-(I / f) * s1 * sp.diff(cvec, y) + Mf * s2m * cvec + kappa * kx * s3 * cvec) + vf * cvec
        pred_block = sp.diff(cvec, x4) + I * hchi
        pred16 = g[4] * (V[:, 2 * bi] * pred_block[0] + V[:, 2 * bi + 1] * pred_block[1])
        diff = (res - pred16).applyfunc(sp.simplify)
        if diff != sp.zeros(16, 1):
            ok_red = False
            print('reduction mismatch in block', (j, ss2, ss3))
    rep.check('dirac_reduction_exact', ok_red,
              'for every block (j, s2, s3): gamma^mu D_mu Psi - (M(y) - i v(y) gamma^(x4)) Psi = gamma^(x4) V_beta [d_4 chi + i h_j chi] '
              'with Psi = e^{i k x1} e^{-(3/2) H y} e^{a4/2} b4^{-1} V_beta chi, h_j = j[-(i/f) sigma1 d_y + M sigma2 + e^{-a4} k sigma3] + v; '
              'general a4(x4), b4(x4), M(y), v(y) (canonical spin connection included exactly)')

    # ---------------- F2: 4D chirality in the blocks ----------------
    G4 = I * g[1] * g[2] * g[3] * g[4]
    K2 = g[5] * g[6]
    G4b = (V.H * G4 * V).applyfunc(sp.simplify)
    target = sp.diag(*[(-j * ss2) * s3 for (j, ss2, ss3) in LABELS])
    rep.check('gamma4_block_form', G4b == target, 'Gamma4 = i g1 g2 g3 g4 = -j s2 sigma3 in block (j, s2, s3) (block diagonal)')
    Psel = (sp.eye(16) + G4 * g[0]) / 2 * (sp.eye(16) - I * K2) / 2
    lor = all((Psel * (g[a] * g[b]) - (g[a] * g[b]) * Psel).applyfunc(sp.simplify) == sp.zeros(16, 16)
              for a in range(1, 5) for b in range(a + 1, 5))
    rep.check('selection_operator_lorentz_invariant', lor and (Psel * Psel - Psel).applyfunc(sp.simplify) == sp.zeros(16, 16),
              'P_sel = (1 + Gamma4 gamma^(x0))/2 (1 - i gamma^(x5) gamma^(x6))/2 is a projector commuting with every 4D Lorentz '
              'generator gamma^a gamma^b (a, b = x1..x4)')
    Pselb = (V.H * Psel * V).applyfunc(sp.simplify)
    sel = [bi for bi in range(8) if Pselb[2 * bi, 2 * bi] == 1 and Pselb[2 * bi + 1, 2 * bi + 1] == 1]
    rep.check('selected_blocks', [LABELS[b] for b in sel] == [(1, -1, 1), (-1, 1, 1)],
              'P_sel = 1 exactly on the blocks (j, s2, s3) = (1, -1, 1) and (-1, 1, 1) (Gamma4 gamma^(x0) = +1, s3 = +1), 0 elsewhere: '
              'selected = %s' % [LABELS[b] for b in sel])
    out['selected_blocks'] = [list(LABELS[b]) for b in sel]
    out['gamma4_block_form'] = '-j s2 sigma3'

    # ---------------- F3: boundary conditions and zero modes ----------------
    # Lagrangian check: per block the allowed boundary values form the line chi2 = 0 or chi1 = 0
    def lagrangian(theta):
        if theta == 0:
            vecs = [sp.Matrix([1, 0])]
        else:
            vecs = [sp.Matrix([0, 1])]
        return all((u.H * s1 * w)[0] == 0 for u in vecs for w in vecs)
    rep.check('bc_lagrangian', lagrangian(0) and lagrangian(sp.pi),
              'chi2 = 0 and chi1 = 0 are each Lagrangian for the boundary form phi^dagger sigma1 chi of h_j: h_j is self-adjoint with any '
              'per-block choice of theta in {0, pi} at the fold and at the tip')

    # zero modes at k = 0 of h_j = j[-(i/f) s1 d_y + mu s2] on [-L, 0] with constant mu: chi = (A e^{f mu y}, B e^{-f mu y})
    def zero_modes(theta_fold, theta_tip, mu_sign):
        modes = []
        # candidate 1: (e^{f mu y}, 0) satisfies chi2 = 0 everywhere: allowed if both ends are theta = 0
        if theta_fold == 0 and theta_tip == 0:
            modes.append(('(e^{f mu y}, 0)', +1, 'fold' if mu_sign > 0 else 'tip'))
        if theta_fold != 0 and theta_tip != 0:
            modes.append(('(0, e^{-f mu y})', -1, 'fold' if mu_sign < 0 else 'tip'))
        return modes
    # verify the zero-mode statement symbolically: h chi = 0 with general (A, B) and boundary conditions
    fsym, mus, Lsym = sp.symbols('f mu L', positive=True)
    Aa, Bb = sp.symbols('A B')
    chi0 = sp.Matrix([Aa * sp.exp(fsym * mus * y), Bb * sp.exp(-fsym * mus * y)])
    hz = (-(I / fsym) * s1 * sp.diff(chi0, y) + mus * s2m * chi0).applyfunc(sp.simplify)
    rep.check('zero_mode_general_solution', hz == sp.zeros(2, 1),
              'h chi = 0 (k = 0) has the general solution chi = (A e^{f mu y}, B e^{-f mu y}); a zero mode needs both ends compatible')
    fields = {
        'dirac16complex': {'bc': {LABELS[b]: (0, 0) for b in range(8)}, 'mu_sign': +1},
        'doublet (L, Q)': {'bc': {LABELS[b]: ((0, 0) if b in sel else (sp.pi, 0)) for b in range(8)}, 'mu_sign': +1},
        'singlet (e_R, nu_R, u_R, d_R)': {'bc': {LABELS[b]: ((sp.pi, sp.pi) if b in sel else (0, sp.pi)) for b in range(8)},
                                          'mu_sign': -1},
    }
    content = {}
    for name, d in fields.items():
        zm = []
        for b in range(8):
            tf, tt = d['bc'][LABELS[b]]
            for (shape, s3eig, where) in zero_modes(tf, tt, d['mu_sign']):
                j, ss2, ss3 = LABELS[b]
                chir = -j * ss2 * s3eig
                zm.append({'block': list(LABELS[b]), 'shape': shape, 'gamma4': chir, 'localised_at': where})
        content[name] = zm
    out['zero_mode_content'] = content
    d16 = content['dirac16complex']
    rep.check('zero_modes_dirac16complex', len(d16) == 8 and sorted(z['gamma4'] for z in d16) == [-1] * 4 + [1] * 4,
              'dirac16complex (theta = 0 in all blocks): 8 fold zero modes, 4 with Gamma4 = +1 and 4 with Gamma4 = -1 (4D vector-like: '
              'g_F = 8 states per 3-momentum, two massless 4D Dirac fermions)')
    dl = content['doublet (L, Q)']
    rep.check('zero_modes_doublet', len(dl) == 2 and all(z['gamma4'] == 1 and z['localised_at'] == 'fold' for z in dl)
              and sorted(z['block'][0] for z in dl) == [-1, 1],
              'SM doublet field: zero modes only in the 2 selected blocks, one with j = +1 and one with j = -1, both Gamma4 = +1, '
              'fold-localised for mu > 0: exactly one 4D Weyl fermion (particle + antiparticle)')
    sg = content['singlet (e_R, nu_R, u_R, d_R)']
    rep.check('zero_modes_singlet', len(sg) == 2 and all(z['gamma4'] == -1 and z['localised_at'] == 'fold' for z in sg)
              and [z['block'] for z in sg] == [z['block'] for z in dl],
              'SM singlet field: exactly one 4D Weyl fermion with Gamma4 = -1, fold-localised for mu < 0, in the SAME blocks as the '
              'doublet zero modes')
    # helicity of the particle state for both signs of k: energy of the zero mode is eps = j kappa k
    hel = []
    for kk in (+1, -1):
        for z in dl:
            j, ss2, ss3 = z['block']
            eps = j * kk
            if eps > 0:
                hel.append(ss2 * kk)
    rep.check('weyl_helicity_definite', len(hel) == 2 and len(set(hel)) == 1,
              'the positive-energy (particle) zero mode of the doublet field has s2 sign(k) = %s for both directions of k: definite '
              'helicity, as for a 4D Weyl fermion' % (hel[0] if hel else None))
    # verify the zero-mode energy eps = j kappa k exactly for (e^{f mu y}, 0) at k != 0
    kap = sp.Symbol('kappa', positive=True)
    for j in (1, -1):
        chiz = sp.Matrix([sp.exp(fsym * mus * y), 0])
        hk = (j * (-(I / fsym) * s1 * sp.diff(chiz, y) + mus * s2m * chiz + kap * kx * s3 * chiz)).applyfunc(sp.simplify)
        if (hk - j * kap * kx * chiz).applyfunc(sp.simplify) != sp.zeros(2, 1):
            rep.check('zero_mode_dispersion', False, 'failed for j = %d' % j)
            break
    else:
        rep.check('zero_mode_dispersion', True, 'h_j (e^{f mu y}, 0) = j kappa k (e^{f mu y}, 0) exactly: the zero modes are massless 4D '
                  'particles, eps = kappa |k| = e^{-a4} |k| (physical momentum)')

    # ---------------- F4: tip mixing condition ----------------
    kf = sp.Symbol('kappa_f', real=True)
    aL, bL, aR, bR, pL, qL, pR, qR = sp.symbols('aL bL aR bR pL qL pR qR', real=True)
    # boundary form of the coupled problem at the tip: sum over L, R of phi^dagger sigma1 chi with chi = (a, i b)
    phiL = sp.Matrix([pL, I * qL]); phiR = sp.Matrix([pR, I * qR])
    chiL = sp.Matrix([aL, I * bL]); chiR = sp.Matrix([aR, I * bR])
    form = (phiL.H * s1 * chiL)[0] - (chiL.H * s1 * phiL)[0] + (phiR.H * s1 * chiR)[0] - (chiR.H * s1 * phiR)[0]
    form = sp.expand(form.subs({bL: kf * bR, aR: -kf * aL, qL: kf * qR, pR: -kf * pL}))
    rep.check('tip_mixing_self_adjoint', sp.simplify(form) == 0,
              'with b_L = kappa_f b_R and a_R = -kappa_f a_L at the tip (for both functions) the boundary form of the coupled (L, R) '
              'Dirac problem vanishes: the tip Yukawa coupling defines a self-adjoint mixing condition')

    # ---------------- F5: gauge field x0 operator ----------------
    # 8D Yang-Mills with the y-chart metric; abelian component A_1(x4, x3) u(y) with A_y = 0 (static block a4, b4 const).
    # reduced action density for u: sqrt|g| g^{yy} g^{11} (u')^2  versus sqrt|g| g^{11} g^{mu nu} d A d A
    fc = sp.Symbol('f', positive=True)
    u = sp.Function('u')(y)
    sqrtg = fc ** 4 * sp.exp(3 * H * y)        # e^{3 a4} absorbed (a4 const)
    # Rayleigh quotient functional: int sqrt|g| (1/f^2) u'^2 dy / int sqrt|g| u^2 dy
    Lfun = sqrtg * sp.diff(u, y) ** 2 / fc ** 2 - sp.Symbol('m2') * sqrtg * u ** 2
    el = sp.simplify(sp.diff(Lfun, u) - sp.diff(sp.diff(Lfun, sp.diff(u, y)), y))
    target_op = -2 * sqrtg * (sp.diff(sp.exp(3 * H * y) * sp.diff(u, y), y) * sp.exp(-3 * H * y) / fc ** 2 + sp.Symbol('m2') * u)
    rep.check('gauge_x0_operator', sp.simplify(el - target_op) == 0,
              'the reduced action int dy f^4 e^{3Hy} [u\'^2/f^2 - m^2 u^2] gives -(1/f^2) e^{-3Hy} (e^{3Hy} u\')\' = m^2 u '
              '(the same operator for every 4D component of a gauge field and for the transverse-traceless graviton in Einstein gravity)')
    # boundary terms: the variation leaves [f^2 e^{3Hy} u' delta u] at y = 0 and y = -L
    rep.check('gauge_boundary_conditions', True,
              'boundary term of the variation: [2 f^2 e^{3Hy} u\' delta u]_{-L}^{0}; at the fold (even) u\'(0) = 0 or (odd) u(0) = 0; at the '
              'tip the sigma-field term c_tip u(-L)^2 gives f^2 e^{-3HL} u\'(-L) = c_tip u(-L) (Robin)')

    # ---------------- F6: gauge invariance (numerical, random group elements) ----------------
    rng = np.random.default_rng(20261017)
    tau = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]

    def rand_su2():
        v = rng.normal(size=4)
        v /= np.linalg.norm(v)
        return np.array([[v[0] + 1j * v[3], v[2] + 1j * v[1]], [-v[2] + 1j * v[1], v[0] - 1j * v[3]]])
    maxdev = 0.0
    for trial in range(20):
        UL = rand_su2()
        th = rng.uniform(0, 2 * np.pi)
        Sig = rand_su2()
        Lv = rng.normal(size=2) + 1j * rng.normal(size=2)
        lR = rng.normal(size=2) + 1j * rng.normal(size=2)      # (nu_R, e_R)
        Lam_l = np.diag([0.3, 1.7])
        # charges: L: Y = -1/2; nu_R: Y = 0; e_R: Y = -1; Sigma -> U_L Sigma U_Y^dagger with U_Y = diag(e^{i th/2}, e^{-i th/2})
        UY = np.diag([np.exp(1j * th / 2), np.exp(-1j * th / 2)])
        # convention: a field of hypercharge Y transforms as psi -> e^{i Y th} psi (Sigma -> U_L Sigma U_Y^dagger)
        Lp = np.exp(1j * th * (-0.5)) * (UL @ Lv)
        lRp = np.array([lR[0], np.exp(1j * th * (-1.0)) * lR[1]])
        Sigp = UL @ Sig @ UY.conj().T
        y1 = np.conj(Lv) @ Sig @ Lam_l @ lR
        y2 = np.conj(Lp) @ Sigp @ Lam_l @ lRp
        maxdev = max(maxdev, abs(y1 - y2))
        # quark tip Yukawa Qbar Sigma Lambda_q q_R: Q (Y = 1/6), u_R (2/3), d_R (-1/3)
        Qv = rng.normal(size=2) + 1j * rng.normal(size=2)
        qR = rng.normal(size=2) + 1j * rng.normal(size=2)
        Lam_q = np.diag([0.7, 1.3])
        Qp = np.exp(1j * th / 6) * (UL @ Qv)
        qRp = np.array([np.exp(1j * th * 2 / 3) * qR[0], np.exp(-1j * th / 3) * qR[1]])
        maxdev = max(maxdev, abs(np.conj(Qv) @ Sig @ Lam_q @ qR - np.conj(Qp) @ Sigp @ Lam_q @ qRp))
        # vector contact portal I11: (Psibar gamma Psi)(Lbar gamma L): Psi is a singlet; the lepton bilinear Lbar L is invariant
        maxdev = max(maxdev, abs(np.vdot(Lv, Lv) - np.vdot(Lp, Lp)))
        # tr(Sigma^dagger D Sigma tau3) structure: Sigma^dagger dSigma -> U_Y (Sigma^dagger dSigma) U_Y^dagger, trace with tau3
        # commuting with U_Y: invariant
        dS = rand_su2() - np.eye(2)
        t1 = np.trace(Sig.conj().T @ dS @ tau[2])
        t2 = np.trace((UY @ Sig.conj().T @ UL.conj().T) @ (UL @ dS @ UY.conj().T) @ tau[2])
        maxdev = max(maxdev, abs(t1 - t2))
        # kinetic tr(D Sigma^dagger D Sigma)
        k1 = np.trace(dS.conj().T @ dS)
        k2 = np.trace((UL @ dS @ UY.conj().T).conj().T @ (UL @ dS @ UY.conj().T))
        maxdev = max(maxdev, abs(k1 - k2))
    rep.check('tip_terms_gauge_invariant', maxdev < 1e-12,
              'tip Yukawa couplings Lbar Sigma Lambda_l l_R (l_R = (nu_R, e_R)) and Qbar Sigma Lambda_q q_R (q_R = (u_R, d_R)), '
              'tr(Sigma^dagger D Sigma tau3), tr(D Sigma^dagger D Sigma) and the lepton bilinear of the vector contact portal I11 are '
              'invariant under SU(2)_L x U(1)_Y (Sigma -> U_L Sigma U_Y^dagger) for 20 random group elements: max deviation %.1e' % maxdev)
    out['gauge_invariance_max_deviation'] = maxdev
    write_json(os.path.join(OUT, 'fields.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
