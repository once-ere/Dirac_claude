#!/usr/bin/env python3
"""UM-2 background gravity: the Einstein-Lovelock equations in curvature-class form, the static block with the
author's weights and Lambda, the block vacuum energy that stabilises it, the effective four-dimensional theory,
and the linear stability of the homogeneous modes.

Curvature classes of the order-0 metric (exact; um2_geometry.py checks them against the full Riemann tensor):
  K_ij = A^2 (3-space pairs, 3 pairs),        K_i4 = A^2 + A' (3 pairs),
  K_ib = A h (3-space with block, 12 pairs),   K_4b = h^2 + h' (4 pairs),
  K_bb' = h^2 - H^2 k (block pairs, 6 pairs),
with A = a4', h = f'/f = b4'/(2 b4) - a4' (the block rate), k = e^{2 a4}/b4 = 1/f^2, the block {x0, x5, x6, x7}.

Results (checked):
  B1  E_(k)^h_h (h = x0 = x5 = x6 = x7, x1 = x2 = x3, x4) as polynomials in the classes; equal to the geometry module.
  B2  static block (h = 0, A = const): x4: -3 G(k) A^2 + 6 H^2 k (1 - 2 w2 k) + Lambda + kappa rho = 0,
      x0: 6 (12 w2 k - 1) A^2 - 12 (w2 - 18 w3 k) A^4/H^2 + 3 H^2 k + Lambda - kappa p0 = 0,
      G(k) = 1 - 24 w2 k + 72 w3 k^2 (the coefficient of the 4D Einstein-Hilbert term; dimensional reduction).
  B3  author's weights w = (1, 1/32, 1/1152), Lambda = -10 H^2: no static vacuum; a block vacuum energy with
      p3 = -rho, p0 = nu rho (nu = 1 for a Casimir-type energy ~ f^{-8}) gives static blocks k*(nu); for nu = 1
      k* = 12 +- (4/3) sqrt(51); G(k*) > 0 (attractive 4D gravity) on the upper root.
  B4  linear stability of (A, h, k) about the static block with the stabiliser (rho_b ~ k^{2(1+nu)}): eigenvalues.
  B5  dimensional reduction of sum_k alpha_k L_k on M4 x (block of constant curvature K = -H^2 k):
      L_k = sum_{j+m=k} k!/(j! m!) L_j^(4) L_m^(int),  L_m^(int) = (1, 12 K, 24 K^2, 0): coefficient of R4 = G(k).
Writes outputs/background.json and reports/background-checks.json.
"""
import itertools
import math
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, Report, read_json, write_json  # noqa: E402

H = sp.Symbol('H', positive=True)
A, Ad, h, hd, k = sp.symbols('A Adot h hdot k', real=True)
w1, w2, w3, Lam, kappa = sp.symbols('w1 w2 w3 Lambda kappa', real=True)
rho, p3, p0 = sp.symbols('rho p3 p0', real=True)
AUTHOR = {w1: 1, w2: sp.Rational(1, 32), w3: sp.Rational(1, 1152)}
LAM_AUTHOR = -10 * H ** 2


def classes():
    """Index classes and the sectional curvature of every pair."""
    S = [1, 2, 3]
    T = [4]
    Bk = [0, 5, 6, 7]
    K = {}
    for a in range(8):
        for b in range(a + 1, 8):
            pa = 'S' if a in S else ('T' if a in T else 'B')
            pb = 'S' if b in S else ('T' if b in T else 'B')
            key = ''.join(sorted(pa + pb))
            K[(a, b)] = {'SS': A ** 2, 'ST': A ** 2 + Ad, 'BS': A * h, 'BT': h ** 2 + hd,
                         'BB': h ** 2 - H ** 2 * k}[key]
    return K


def lovelock(K, kk, hidx):
    pairs = [p for p in K if hidx not in p]
    tot = 0
    for combo in itertools.combinations(pairs, kk):
        used = [i for p in combo for i in p]
        if len(set(used)) == 2 * kk:
            term = 1
            for p in combo:
                term *= K[p]
            tot += term
    return sp.expand(-(2 ** (kk - 1)) * sp.factorial(kk) * tot)


def main():
    rep = Report('background-checks', 'UM-2: background Einstein-Lovelock equations, the static block with the author\'s '
                 'weights, the block vacuum energy (stabiliser), dimensional reduction, linear stability')
    out = {}
    K = classes()
    E = {kk: {hh: lovelock(K, kk, hh) for hh in (0, 1, 4, 5)} for kk in (1, 2, 3)}
    for kk in (1, 2, 3):
        rep.check('hidden_equals_extra_times_k%d' % kk, sp.simplify(E[kk][0] - E[kk][5]) == 0,
                  'E_(%d)^x0_x0 = E_(%d)^x5_x5 in the class form' % (kk, kk))
    # compare with the geometry module (record symbols: ad1 = A, ad2 = A', uu = 2(h + A), vv = 2(h' + A'), kk = k)
    geo = read_json(os.path.join(OUT, 'geometry.json'))['lovelock_record_symbols']
    ad1, ad2, uu, vv, kks = sp.symbols('ad1 ad2 uu vv kk', real=True)
    sub = {ad1: A, ad2: Ad, uu: 2 * (h + A), vv: 2 * (hd + Ad), kks: k}
    names = {0: 'x0 (= x5 = x6 = x7)', 1: 'x1 (= x2 = x3)', 4: 'x4'}
    ok = True
    for kk in (1, 2, 3):
        for hh, nm in names.items():
            g = sp.sympify(geo[str(kk)][nm], locals={'H': H, 'ad1': ad1, 'ad2': ad2, 'uu': uu, 'vv': vv, 'kk': kks})
            if sp.simplify(sp.expand(g.subs(sub)) - E[kk][hh]) != 0:
                ok = False
                print('mismatch', kk, hh)
    rep.check('class_form_equals_full_tensor', ok, 'the class-form E_(k) (k = 1, 2, 3; components x0, x1, x4) equal the '
              'components computed from the full Riemann tensor (um2_geometry.py)')
    out['E_class_form'] = {str(kk): {names[hh]: str(sp.factor(E[kk][hh])) for hh in names} for kk in (1, 2, 3)}

    al = {1: 1, 2: w2 / H ** 2, 3: w3 / H ** 4}
    LHS = {hh: sp.expand(sum(al[kk] * E[kk][hh] for kk in (1, 2, 3)) + Lam) for hh in (0, 1, 4)}
    # field equations: LHS[4] = -kappa rho, LHS[1] = kappa p3, LHS[0] = kappa p0
    out['field_equations_class_form'] = {
        'x4 (constraint)': str(LHS[4]) + ' = -kappa rho',
        'x1 = x2 = x3': str(LHS[1]) + ' = kappa p3',
        'x0 = x5 = x6 = x7': str(LHS[0]) + ' = kappa p0'}

    # ---- static block ----
    st = {h: 0, hd: 0, Ad: 0}
    G = 1 - 24 * w2 * k + 72 * w3 * k ** 2
    F4 = sp.expand(LHS[4].subs(st) + kappa * rho)
    F0 = sp.expand(LHS[0].subs(st) - kappa * p0)
    rep.check('static_block_x4', sp.simplify(F4 - (-3 * G * A ** 2 + 6 * H ** 2 * k * (1 - 2 * w2 * k) + Lam + kappa * rho)) == 0,
              'x4 at h = 0, A\' = 0: -3 G(k) A^2 + 6 H^2 k (1 - 2 w2 k) + Lambda + kappa rho = 0')
    rep.check('static_block_x0', sp.simplify(F0 - (6 * (12 * w2 * k - 1) * A ** 2 - 12 * (w2 - 18 * w3 * k) * A ** 4 / H ** 2
                                                + 3 * H ** 2 * k + Lam - kappa * p0)) == 0,
              'x0 at h = 0, A\' = 0: 6(12 w2 k - 1) A^2 - 12 (w2 - 18 w3 k) A^4/H^2 + 3 H^2 k + Lambda - kappa p0 = 0')
    # vacuum
    sol = sp.solve([F4.subs({A: 0, rho: 0}), F0.subs({A: 0, p0: 0})], [k, Lam], dict=True)
    sol = [s for s in sol if s[k] != 0]
    rep.check('static_vacuum_general', len(sol) == 1 and sp.simplify(sol[0][k] - 1 / (4 * w2)) == 0 and
              sp.simplify(sol[0][Lam] + 3 * H ** 2 / (4 * w2)) == 0,
              'the only sourceless static block with k != 0: k0 = 1/(4 w2), Lambda0 = -3 H^2/(4 w2)')
    Gk0 = sp.simplify(G.subs(k, 1 / (4 * w2)))
    rep.check('newton_factor_at_vacuum', sp.simplify(Gk0 - (-5 + 9 * w3 / (2 * w2 ** 2))) == 0,
              'G(k0) = -5 + 9 w3/(2 w2^2); author\'s weights: G(k0) = %s (repulsive), Lambda0 = -24 H^2 != -10 H^2' % Gk0.subs(AUTHOR))
    GA = sp.expand(G.subs(AUTHOR))
    roots = sp.solve(GA, k)
    out['G_author'] = str(GA)
    out['G_author_roots'] = [str(r) for r in roots]
    rep.check('newton_factor_author_roots', set(sp.nsimplify(r) for r in roots) == {6 - 2 * sp.sqrt(5), 6 + 2 * sp.sqrt(5)},
              'author\'s weights: G(k) = (k^2 - 12 k + 16)/16 > 0 only for k < 6 - 2 sqrt5 = 1.528 or k > 6 + 2 sqrt5 = 10.472')

    # ---- B3: the block vacuum energy (stabiliser): p3 = -rho_b, p0 = nu rho_b ----
    nu = sp.Symbol('nu', real=True)
    eq4 = (F4.subs(AUTHOR).subs({A: 0, Lam: LAM_AUTHOR}))          # 6H^2k(1-k/16) - 10H^2 + kappa rho = 0
    eq0 = (F0.subs(AUTHOR).subs({A: 0, Lam: LAM_AUTHOR}))          # 3H^2k - 10H^2 - kappa p0 = 0
    krho = sp.solve(eq4, rho)[0] * kappa
    kp0 = sp.solve(eq0, p0)[0] * kappa
    out['stabiliser_requirement'] = {'kappa rho_b': str(sp.simplify(krho)), 'kappa p0_b': str(sp.simplify(kp0)),
                                     'kappa p3_b': str(sp.simplify(-krho))}
    rep.check('stabiliser_requirement', sp.simplify(krho - (10 * H ** 2 - 6 * H ** 2 * k + sp.Rational(3, 8) * H ** 2 * k ** 2)) == 0
              and sp.simplify(kp0 - (3 * H ** 2 * k - 10 * H ** 2)) == 0,
              'a static block with A = 0 and the author\'s weights and Lambda needs kappa rho_b = 10 H^2 - 6 H^2 k + (3/8) H^2 k^2, '
              'kappa p3_b = -kappa rho_b, kappa p0_b = 3 H^2 k - 10 H^2')
    # Casimir-type nu = 1
    ks = sp.solve(sp.Eq(kp0, krho), k)
    ks = sorted(ks, key=lambda r: float(r))
    rep.check('casimir_type_static_blocks', len(ks) == 2 and sp.simplify(ks[1] - (12 + sp.Rational(4, 3) * sp.sqrt(51))) == 0
              and sp.simplify(ks[0] - (12 - sp.Rational(4, 3) * sp.sqrt(51))) == 0,
              'nu = 1 (p0 = rho, a vacuum energy ~ f^-8): k* = 12 -+ (4/3) sqrt(51) = %.6f, %.6f' % (float(ks[0]), float(ks[1])))
    kstar = ks[1]
    Gstar = sp.nsimplify(sp.expand(GA.subs(k, kstar)))
    krho_star = sp.simplify(krho.subs(k, kstar))
    rep.check('casimir_type_attractive_gravity', float(Gstar) > 0 and float(GA.subs(k, ks[0])) < 0,
              'G(k*) = %s = %.6f > 0 on the upper root (attractive 4D gravity, G_N = kappa/(V_perp G(k*))); '
              'the lower root has G = %.6f < 0' % (sp.simplify(Gstar), float(Gstar), float(GA.subs(k, ks[0]))))
    rep.check('casimir_type_positive_energy', float(krho_star / H ** 2) > 0,
              'at k* the block vacuum energy is positive: kappa rho_b = %s = %.6f H^2 (p0 = rho_b, p3 = -rho_b)' % (
                  sp.simplify(krho_star / H ** 2), float(krho_star / H ** 2)))
    out['casimir_type'] = {'k_star': str(kstar), 'k_star_value': float(kstar), 'f_star': float(1 / sp.sqrt(kstar)),
                           'G_k_star': str(sp.simplify(Gstar)), 'G_k_star_value': float(Gstar),
                           'kappa_rho_b_over_H2': float(krho_star / H ** 2),
                           'lower_root': float(ks[0]), 'G_lower_root': float(GA.subs(k, ks[0]))}
    # general nu: k*(nu) curve
    tab = []
    for nuv in [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 3.0]:
        sols = sp.solve(sp.Eq(kp0, nuv * krho), k)
        rr = []
        for s in sols:
            sv = complex(s)
            if abs(sv.imag) < 1e-12 and sv.real > 0:
                kv = sv.real
                rr.append({'k': kv, 'G': float(GA.subs(k, kv)), 'kappa_rho_over_H2': float((krho / H ** 2).subs(k, kv))})
        tab.append({'nu': nuv, 'roots': rr})
    out['stabiliser_family'] = tab

    # ---- B4: linear stability about the static blocks of the stabiliser family ----
    # dynamical system: the x1 and x0 components give A' and h' (both are linear in A', h'); k' = -2 k h.
    # The stabiliser kappa rho_b = R(k) is conserved: rho' = -3A(rho + p3) - 4 h (rho + p0) = -4 h (1 + nu) rho,
    # i.e. R(k) ~ k^{2(1+nu)}; the Jacobian needs only R(k*) and R'(k*) = 2 (1 + nu) R(k*)/k*.
    Rf = sp.Function('R')(k)
    src = {rho: Rf / kappa, p3: -Rf / kappa}
    eq1g = sp.expand((LHS[1] - kappa * p3).subs(src).subs(AUTHOR).subs(Lam, LAM_AUTHOR))
    solvg = None
    vars_ = [A, h, k]
    fam = []
    for nuq in [sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(3, 4), 1, sp.Rational(5, 4), sp.Rational(3, 2), 2, 3]:
        eq0g = sp.expand((LHS[0] - nuq * Rf).subs(AUTHOR).subs(Lam, LAM_AUTHOR))
        sq = sp.solve([eq1g, eq0g], [Ad, hd], dict=True)
        if nuq == 1:
            rep.check('second_order_system_solvable', len(sq) == 1, 'the x1 and x0 components solve uniquely for A\' and h\' '
                      '(non-degenerate Jacobian at the static block)')
        sq = sq[0]
        ksq = [r for r in sp.solve(sp.Eq(kp0, nuq * krho), k) if float(r) > 10.472]
        kq = ksq[0]
        Rq = sp.simplify(krho.subs(k, kq))
        dRq = 2 * (1 + nuq) * Rq / kq
        rhs = [sq[Ad], sq[hd], -2 * k * h]
        Jq = sp.zeros(3, 3)
        for i, r in enumerate(rhs):
            for j, v in enumerate(vars_):
                d = sp.diff(r, v)
                d = d.subs(sp.Derivative(Rf, k), dRq).subs(Rf, Rq).subs({A: 0, h: 0}).subs(k, kq)
                Jq[i, j] = sp.simplify(d)
        # residual of the static point (all three components)
        e4g = sp.expand((LHS[4] + Rf).subs(AUTHOR).subs(Lam, LAM_AUTHOR))
        res = [sp.simplify(x.subs(Rf, Rq).subs({A: 0, h: 0, Ad: 0, hd: 0}).subs(k, kq)) for x in (eq1g, eq0g, e4g)]
        evq = [complex(sp.N(e / H, 12)) for e in Jq.eigenvals(multiple=True)]
        fam.append({'nu': float(nuq), 'k_star': float(kq), 'G': float(GA.subs(k, kq)),
                    'static_point_residuals': [str(r) for r in res],
                    'eigenvalues_over_H': [[e.real, e.imag] for e in evq],
                    'stable': all(e.real <= 1e-10 for e in evq)})
        if nuq == 1:
            J = Jq
            rep.check('static_point_is_a_solution', all(r == 0 for r in res), 'A = 0, h = 0, k = k* with kappa rho_b(k*) is an '
                      'exact solution of all three components (x1, x0 dynamical, x4 constraint)')
            out['block_mode_jacobian'] = [[str(J[i, j]) for j in range(3)] for i in range(3)]
            out['block_mode_eigenvalues_over_H'] = [[v.real, v.imag] for v in evq]
            nullv = J.nullspace()
            out['zero_mode_direction'] = [str(sp.simplify(x)) for x in nullv[0]] if nullv else []
            om = max(abs(v.imag) for v in evq)
            out['radion_frequency_over_H'] = om
            out['radion_frequency_squared_over_H2_exact'] = str(sp.nsimplify(sp.simplify(-sp.Matrix(J[1:, 1:]).det() / H ** 2)))
            rep.check('block_stable_nu1', all(v.real <= 1e-10 for v in evq) and om > 0,
                      'eigenvalues of the linearised (A, h, k) system about the nu = 1 static block: %s (units H); no growing mode: '
                      'the block oscillates about k* with omega = %.6f H (the radion mass); the zero eigenvalue is the A direction '
                      '(a small 4D cosmological term)' % (', '.join('%.6f%+.6fi' % (v.real, v.imag) for v in evq), om))
    out['stabiliser_family_stability'] = fam
    rep.check('block_stable_family', all(x['stable'] for x in fam) and all(all(r == '0' for r in x['static_point_residuals']) for x in fam),
              'for every nu in {1/4, ..., 3} the attractive-gravity static block solves all components and is linearly stable; '
              'radion masses / H: %s' % ', '.join('%.3f' % max(abs(e[1]) for e in x['eigenvalues_over_H']) for x in fam))

    # ---- B5: dimensional reduction ----
    Kint = sp.Symbol('K', real=True)
    Lint = {0: 1, 1: 12 * Kint, 2: 24 * Kint ** 2, 3: 0}
    # verify L_m^(int) for a 4-dim maximally symmetric space with the pairing Lagrangian
    pairs4 = [(a, b) for a in range(4) for b in range(a + 1, 4)]
    ok = True
    for m in (1, 2, 3):
        tot = 0
        for combo in itertools.combinations(pairs4, m):
            used = [i for p in combo for i in p]
            if len(set(used)) == 2 * m:
                tot += Kint ** m
        if sp.simplify(2 ** m * sp.factorial(m) * tot - Lint[m]) != 0:
            ok = False
    rep.check('internal_lovelock_densities', ok, 'L_m of a 4-dim space of constant curvature K: L_1 = 12 K, L_2 = 24 K^2, L_3 = 0')
    R4, GB4 = sp.symbols('R4 GB4', real=True)
    L4 = {0: 1, 1: R4, 2: GB4, 3: 0}
    Ltot = 0
    alk = {1: 1, 2: w2 / H ** 2, 3: w3 / H ** 4}
    for kk in (1, 2, 3):
        for j in range(kk + 1):
            m = kk - j
            Ltot += alk[kk] * sp.factorial(kk) / (sp.factorial(j) * sp.factorial(m)) * L4[j] * Lint[m]
    Ltot = sp.expand((Ltot - 2 * Lam).subs(Kint, -H ** 2 * k))
    coefR = sp.simplify(Ltot.coeff(R4))
    const = sp.simplify(Ltot.subs({R4: 0, GB4: 0}))
    rep.check('reduction_newton_factor', sp.simplify(coefR - G) == 0,
              'dimensional reduction on the static block: the coefficient of the 4D Einstein-Hilbert term is G(k) = '
              '1 - 24 w2 k + 72 w3 k^2 (the same factor as in the x4 component)')
    Lam4 = sp.simplify(-const / (2 * G))
    rep.check('reduction_cosmological_term', sp.simplify(Lam4 - (6 * H ** 2 * k * (1 - 2 * w2 * k) + Lam) / G) == 0,
              'the 4D cosmological term of the reduced action, Lambda4 = (6 H^2 k (1 - 2 w2 k) + Lambda)/G(k), equals A^2/3 x 3 from '
              'the x4 component (3 G A^2 = 6 H^2 k (1 - 2 w2 k) + Lambda)')
    out['reduction'] = {'L_eff': str(Ltot), 'coefficient_R4': str(coefR), 'Lambda4': str(Lam4)}
    write_json(os.path.join(OUT, 'background.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
