#!/usr/bin/env python3
"""UM-2 geometry: the order-0 metric, its curvature, the Einstein-Lovelock tensors, the
background field equations, and the canonical spin connection of dirac16complex.

Metric (the author's coordinates x0..x7; z = 6 H x0 real; the corrected primordial metric):
  g = diag(f^2 cot^2 z, e^{2a4}, e^{2a4}, e^{2a4}, -1, -f^2 (sin^2 z)^{1/6} (x3)),
  f = e^{-a4} b4^{1/2},  a4 = a4(x4), b4 = b4(x4) > 0.
The hidden coordinate y = ln|sin z|/(6H) (dy = cot z dx0) gives the chart
  g = diag(f^2, e^{2a4} (x3), -1, -f^2 e^{2Hy} (x3)).

Computed and checked here (sympy, exact):
  A  the Christoffel symbols and Riemann tensor in BOTH charts; the mixed components agree;
     the curvature is pair-diagonal (R^{ab}_{cd} = 0 unless {a,b} = {c,d});
  B  the Lovelock tensors E_(k), k = 1,2,3, from the pairing formula
       E_(k)^h_h = -(2^{k-1} k!) sum over sets of k disjoint index pairs not containing h of prod K_pair
     (K_ab = R^{ab}_{ab}, exact for pair-diagonal curvature), checked against
       k = 1: the Einstein tensor from the Ricci tensor (independent),
       k = 2: the Gauss-Bonnet tensor from its explicit Riemann formula (independent),
       k = 1,2,3: the Bianchi identity nabla_M E_(k)^M_N = 0 (independent),
       k = 1,2,3: the Euler-Lagrange equations of the minisuperspace action int sqrt|g| L_k with a lapse
                  (an independent route: variation of the action instead of the tensor formula),
       k = 1,2,3: the record's equations Revision/field_equations_a4/a4-equations.json (generalSource);
  C  the background equations sum alpha_k E_(k) + Lambda delta = kappa T with the author's weights
     alpha_k = w_k H^{2-2k}, w = (1, 1/32, 1/1152), Lambda = -10 H^2 (record sign convention);
  D  the canonical spin connection Omega_mu = (1/2) omega_mu ab S^ab with the author's gammas,
     covariant constancy of gamma^mu, and gamma^mu Omega_mu = (3/2)(H/f) gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4).
Writes outputs/geometry.json and reports/geometry-checks.json.
"""
import itertools
import os
import sys
import time

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, ROOT, Report, read_json, write_json  # noqa: E402

N = 8
X = sp.symbols('x0:8', real=True)
H = sp.Symbol('H', positive=True)
Y = sp.Symbol('y', real=True)
x4 = X[4]
a4 = sp.Function('a4')(x4)
b4 = sp.Function('b4')(x4)
# record symbols
ad1, ad2, uu, vv, kk = sp.symbols('ad1 ad2 uu vv kk', real=True)
alpha1, alpha2, alpha3, Lam, kappa = sp.symbols('alpha1 alpha2 alpha3 Lam kappa', real=True)
rho, p3, p0, pt = sp.symbols('rho p3 p0 pt', real=True)


def to_record_symbols(e):
    """Replace a4', a4'', b4'/b4, (b4'/b4)', e^{2a4}/b4 by the record's symbols."""
    e = sp.sympify(e)
    b1 = sp.Derivative(b4, x4)
    b2 = sp.Derivative(b4, (x4, 2))
    a1d = sp.Derivative(a4, x4)
    a2d = sp.Derivative(a4, (x4, 2))
    e = e.subs(b2, (vv + uu ** 2) * b4).subs(b1, uu * b4)
    e = e.subs(a2d, ad2).subs(a1d, ad1)
    e = sp.expand(sp.powsimp(sp.expand(e), force=True))
    e = e.subs(sp.exp(2 * a4), kk * b4)
    e = e.subs(sp.exp(-2 * a4), 1 / (kk * b4))
    e = sp.simplify(e)
    return sp.expand(e)


def christoffel(g, coords):
    n = len(coords)
    ginv = sp.diag(*[1 / g[i, i] for i in range(n)])
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = 0
                for d in (a,):
                    s += ginv[a, d] * (sp.diff(g[d, c], coords[b]) + sp.diff(g[d, b], coords[c]) - sp.diff(g[b, c], coords[d]))
                Gam[a][b][c] = sp.simplify(s / 2)
    return Gam, ginv


def riemann_updown(Gam, coords):
    """R^a_{bcd} = d_c Gam^a_{bd} - d_d Gam^a_{bc} + Gam^a_{ce} Gam^e_{bd} - Gam^a_{de} Gam^e_{bc} (MTW)."""
    n = len(coords)
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(c + 1, n):
                    s = sp.diff(Gam[a][b][d], coords[c]) - sp.diff(Gam[a][b][c], coords[d])
                    for e in range(n):
                        s += Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c]
                    s = sp.simplify(s)
                    if s != 0:
                        R[(a, b, c, d)] = s
                        R[(a, b, d, c)] = -s
    return R


def riemann_upup(Rud, ginv):
    """R^{ab}_{cd} = g^{bb} R^a_{bcd} for a diagonal metric."""
    return {(a, b, c, d): sp.simplify(ginv[b, b] * v) for (a, b, c, d), v in Rud.items()}


def pairing_lovelock(K, n, k):
    """E_(k)^h_h = -(2^{k-1} k!) sum_{k disjoint pairs avoiding h} prod K (pair-diagonal curvature)."""
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    res = []
    for h in range(n):
        idx = [i for i in range(n) if i != h]
        total = 0
        for combo in itertools.combinations([p for p in pairs if h not in p], k):
            used = [i for p in combo for i in p]
            if len(set(used)) == 2 * k:
                term = 1
                for p in combo:
                    term *= K[p]
                total += term
        res.append(sp.simplify(-(2 ** (k - 1)) * sp.factorial(k) * total))
    return res


def pairing_lagrangian(K, n, k):
    """L_k = 2^k k! sum over sets of k disjoint pairs of prod K."""
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    total = 0
    for combo in itertools.combinations(pairs, k):
        used = [i for p in combo for i in p]
        if len(set(used)) == 2 * k:
            term = 1
            for p in combo:
                term *= K[p]
            total += term
    return sp.simplify(2 ** k * sp.factorial(k) * total)


def main():
    t0 = time.time()
    rep = Report('geometry-checks', 'UM-2: curvature of the order-0 metric, Lovelock tensors (four routes), the '
                 'background equations with the author\'s weights, the canonical spin connection')
    out = {}
    f2 = sp.exp(-2 * a4) * b4

    # ---------------- A: the y chart ----------------
    cy = [Y] + list(X[1:])
    gy = sp.diag(f2, sp.exp(2 * a4), sp.exp(2 * a4), sp.exp(2 * a4), -1,
                 -f2 * sp.exp(2 * H * Y), -f2 * sp.exp(2 * H * Y), -f2 * sp.exp(2 * H * Y))
    Gy, ginvy = christoffel(gy, cy)
    Rudy = riemann_updown(Gy, cy)
    Ruuy = riemann_upup(Rudy, ginvy)
    nonpair = [key for key, v in Ruuy.items() if set(key[:2]) != set(key[2:])]
    rep.check('y_chart_pair_diagonal', len(nonpair) == 0,
              'R^{ab}_{cd} = 0 unless {a,b} = {c,d}: %d non-pair components' % len(nonpair))
    Ky = {}
    for a in range(N):
        for b in range(a + 1, N):
            Ky[(a, b)] = sp.simplify(Ruuy.get((a, b, a, b), 0))
    # sectional curvatures in record symbols
    Krec = {str(kp): str(to_record_symbols(v)) for kp, v in Ky.items() if v != 0}
    out['sectional_curvatures_y_chart'] = Krec
    print('sectional curvatures:', Krec)

    # ---------------- A': the author's chart (0 < z < pi, z != pi/2) ----------------
    z = 6 * H * X[0]
    gx = sp.diag(f2 * sp.cot(z) ** 2, sp.exp(2 * a4), sp.exp(2 * a4), sp.exp(2 * a4), -1,
                 -f2 * sp.sin(z) ** sp.Rational(1, 3), -f2 * sp.sin(z) ** sp.Rational(1, 3),
                 -f2 * sp.sin(z) ** sp.Rational(1, 3))
    Gx, ginvx = christoffel(gx, list(X))
    Rudx = riemann_updown(Gx, list(X))
    Ruux = riemann_upup(Rudx, ginvx)
    nonpairx = [key for key, v in Ruux.items() if set(key[:2]) != set(key[2:])]
    rep.check('author_chart_pair_diagonal', len(nonpairx) == 0,
              'in the chart x0..x7 with (sin^2 z)^{1/6} = sin(z)^{1/3} on 0 < z < pi: %d non-pair components' % len(nonpairx))
    sub_y = {sp.sin(z): sp.exp(6 * H * Y)}
    agree = True
    for a in range(N):
        for b in range(a + 1, N):
            kx = Ruux.get((a, b, a, b), 0)
            kxy = sp.simplify(sp.simplify(kx).rewrite(sp.sin).subs(sp.cos(z) ** 2, 1 - sp.sin(z) ** 2).subs(sub_y))
            if sp.simplify(kxy - Ky[(a, b)]) != 0:
                agree = False
                print('chart mismatch', a, b, kxy, Ky[(a, b)])
    rep.check('charts_agree', agree, 'every sectional curvature K_ab is the same in the chart x0..x7 and in the y chart '
              '(substituting sin z = e^{6Hy}): the curvature is free of x0 and holds on both halves of a cell')

    # ---------------- B: Lovelock tensors ----------------
    E = {}
    for k in (1, 2, 3):
        E[k] = pairing_lovelock(Ky, N, k)
    # B1: Einstein tensor from Ricci
    Ric = sp.zeros(N, N)
    for (a, b, c, d), v in Rudy.items():
        if a == c:
            Ric[b, d] += v
    Ric = Ric.applyfunc(sp.simplify)
    Rmix = sp.diag(*[ginvy[i, i] for i in range(N)]) * Ric
    Rs = sp.simplify(sum(Rmix[i, i] for i in range(N)))
    Gmix = [sp.simplify(Rmix[i, i] - Rs / 2) for i in range(N)]
    offd = all(sp.simplify(Rmix[i, j]) == 0 for i in range(N) for j in range(N) if i != j)
    rep.check('einstein_from_ricci_equals_pairing_k1', all(sp.simplify(Gmix[i] - E[1][i]) == 0 for i in range(N)) and offd,
              'G^a_a = R^a_a - R/2 equals E_(1)^a_a of the pairing formula; Ricci is diagonal')
    # B2: Gauss-Bonnet tensor explicit formula (mixed components, diagonal metric)
    # H^mu_nu = 2(R R^mu_nu - 2 R^mu_a R^a_nu - 2 R^{ab} R^mu_{a nu b} + R^{mu abc} R_{nu abc}) - 1/2 delta GB
    gdiag = [gy[i, i] for i in range(N)]
    ginv_d = [ginvy[i, i] for i in range(N)]
    Rdddd = {}
    for (a, b, c, d), v in Rudy.items():
        Rdddd[(a, b, c, d)] = gdiag[a] * v
    def Rlow(a, b, c, d):
        return Rdddd.get((a, b, c, d), 0)
    Ric_ud = Rmix
    Ric_uu = sp.Matrix(N, N, lambda i, j: ginv_d[i] * Ric[i, j] * ginv_d[j])
    RR = sp.simplify(sum(Rmix[i, j] * Rmix[j, i] for i in range(N) for j in range(N)))
    Riem2 = 0
    for (a, b, c, d), v in Rdddd.items():
        Riem2 += v * v * ginv_d[a] * ginv_d[b] * ginv_d[c] * ginv_d[d]
    Riem2 = sp.simplify(Riem2)
    GB = sp.simplify(Rs ** 2 - 4 * RR + Riem2)
    Hmix = []
    for mu in range(N):
        t1 = Rs * Ric_ud[mu, mu]
        t2 = sum(Ric_ud[mu, a] * Ric_ud[a, mu] for a in range(N))
        t3 = 0
        for a in range(N):
            for b in range(N):
                # R^{ab} R^mu_{a mu b} = R^{ab} g^{mu mu} R_{mu a mu b}
                t3 += Ric_uu[a, b] * ginv_d[mu] * Rlow(mu, a, mu, b)
        t4 = 0
        for a in range(N):
            for b in range(N):
                for c in range(N):
                    v1 = Rlow(mu, a, b, c)
                    if v1 != 0:
                        t4 += ginv_d[mu] * v1 * Rlow(mu, a, b, c) * ginv_d[a] * ginv_d[b] * ginv_d[c]
        Hmix.append(sp.simplify(2 * (t1 - 2 * t2 - 2 * t3 + t4) - GB / 2))
    rep.check('gauss_bonnet_tensor_equals_pairing_k2', all(sp.simplify(Hmix[i] - E[2][i]) == 0 for i in range(N)),
              'the explicit Gauss-Bonnet tensor H^a_a = 2(R R^a_a - 2 R^a_b R^b_a - 2 R^{bc} R^a_{b a c} + R^{a bcd} R_{a bcd}) '
              '- GB/2 equals E_(2)^a_a of the pairing formula')
    # B3: Bianchi identity nabla_M E^M_N = 0 (diagonal mixed tensor, depends on y and x4)
    for k in (1, 2, 3):
        ok = True
        for nu in range(N):
            # nabla_mu T^mu_nu = d_mu T^mu_nu + Gam^mu_{mu l} T^l_nu - Gam^l_{mu nu} T^mu_l; for a diagonal
            # mixed tensor T^mu_nu = E_mu delta^mu_nu this is d_nu E_nu + sum_mu Gam^mu_{mu nu} (E_nu - E_mu)
            div = sp.diff(E[k][nu], cy[nu])
            for m in range(N):
                div += Gy[m][m][nu] * (E[k][nu] - E[k][m])
            div = sp.simplify(div)
            if div != 0:
                ok = False
                print('Bianchi fails', k, nu, div)
        rep.check('bianchi_identity_k%d' % k, ok, 'nabla_M E_(%d)^M_N = 0 identically for every N' % k)
    # B4: minisuperspace action with a lapse: ds^2 = A^2 dx_i^2 - Nl^2 dx4^2 + F^2 (dy^2 - e^{2Hy} dx_t^2)
    t = sp.Symbol('t', real=True)
    Af = sp.Function('A')(t)
    Ff = sp.Function('F')(t)
    Nf = sp.Function('Nl')(t)
    cm = [Y, X[1], X[2], X[3], t, X[5], X[6], X[7]]
    gm = sp.diag(Ff ** 2, Af ** 2, Af ** 2, Af ** 2, -Nf ** 2, -Ff ** 2 * sp.exp(2 * H * Y), -Ff ** 2 * sp.exp(2 * H * Y),
                 -Ff ** 2 * sp.exp(2 * H * Y))
    Gm, ginvm = christoffel(gm, cm)
    Rudm = riemann_updown(Gm, cm)
    Ruum = riemann_upup(Rudm, ginvm)
    nonpairm = [key for key, v in Ruum.items() if set(key[:2]) != set(key[2:])]
    rep.check('lapse_metric_pair_diagonal', len(nonpairm) == 0, 'the minisuperspace metric with a lapse is pair-diagonal')
    Km = {}
    for a in range(N):
        for b in range(a + 1, N):
            Km[(a, b)] = sp.simplify(Ruum.get((a, b, a, b), 0))
    sqrtg = Nf * Af ** 3 * Ff ** 4 * sp.exp(3 * H * Y)
    Em = {k: pairing_lovelock(Km, N, k) for k in (1, 2, 3)}
    for k in (1, 2, 3):
        Lk = pairing_lagrangian(Km, N, k)
        dens = sp.expand(sqrtg * Lk)
        # Euler-Lagrange: delta S / delta Nl = -sqrt|g| (2/Nl^2)... use the general identity
        #   delta(int sqrt|g| L_k) = -2 int sqrt|g| E_(k)^{mu nu} delta g_{mu nu}/2 ... ; check the contractions:
        #   dS/dNl  = -2 sqrt|g|/Nl * E^4_4 * (-1) ... derived generally below by direct comparison
        def EL(q):
            return sp.simplify(sp.diff(dens, q) - sp.diff(sp.diff(dens, sp.diff(q, t)), t)
                               + sp.diff(sp.diff(dens, sp.diff(q, t, 2)), t, 2))
        eN = EL(Nf)
        eA = EL(Af)
        eF = EL(Ff)
        # delta S = -int sqrt|g| E^{mu nu} delta g_mu nu (E = Lovelock tensor, sign of the record's E_(1) = G):
        # g_44 = -Nl^2: delta g_44 = -2 Nl dNl -> eN = -sqrt|g| E^{44} (-2 Nl) = 2 sqrt|g| Nl g^44 g^44 E_44 ...
        # In mixed form: E^{44} delta g_44 = E^4_4 g^44 delta g_44 = E^4_4 (2 dNl/Nl)
        predN = -sqrtg * Em[k][4] * 2 / Nf
        predA = -sqrtg * 3 * Em[k][1] * 2 / Af
        predF = -sqrtg * (Em[k][0] + 3 * Em[k][5]) * 2 / Ff
        okN = sp.simplify(eN - predN) == 0
        okA = sp.simplify(eA - predA) == 0
        okF = sp.simplify(eF - predF) == 0
        rep.check('minisuperspace_variation_k%d' % k, okN and okA and okF,
                  'Euler-Lagrange equations of int sqrt|g| L_%d with respect to the lapse, the 3-space scale A and the block '
                  'scale F equal -2 sqrt|g| (E^4_4/Nl, 3 E^1_1/A, (E^0_0 + 3 E^5_5)/F) of the pairing tensor' % k)
    # B5: hidden = extra times, no y dependence
    for k in (1, 2, 3):
        rep.check('hidden_equals_extra_times_k%d' % k, sp.simplify(E[k][0] - E[k][5]) == 0 and
                  all(sp.diff(E[k][i], Y) == 0 for i in range(N)),
                  'E_(%d)^0_0 = E_(%d)^5_5 and no component depends on y (hence on x0)' % (k, k))

    # record symbols and the record comparison
    Erec = {k: [to_record_symbols(E[k][i]) for i in range(N)] for k in (1, 2, 3)}
    rec = read_json(os.path.join(ROOT, 'Revision', 'field_equations_a4', 'a4-equations.json'))
    gs = rec['generalSource']
    loc = {'ad1': ad1, 'ad2': ad2, 'uu': uu, 'vv': vv, 'kk': kk, 'H': H, 'alpha1': alpha1, 'alpha2': alpha2,
           'alpha3': alpha3, 'Lam': Lam, 'kappa': kappa, 'rho': rho, 'p3': p3, 'p0': p0}
    def parse_eq(s):
        lhs, rhs = s.split('==')
        return sp.sympify(lhs.replace('^', '**'), locals=loc) - sp.sympify(rhs.replace('^', '**'), locals=loc)
    mine = {
        'constraint_x4': alpha1 * Erec[1][4] + alpha2 * Erec[2][4] + alpha3 * Erec[3][4] + Lam + kappa * rho,
        'space_x1_eq_x2_eq_x3': alpha1 * Erec[1][1] + alpha2 * Erec[2][1] + alpha3 * Erec[3][1] + Lam - kappa * p3,
        'hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7': alpha1 * Erec[1][0] + alpha2 * Erec[2][0] + alpha3 * Erec[3][0] + Lam - kappa * p0,
    }
    for key, expr in mine.items():
        theirs = parse_eq(gs[key]['input'])
        diff = sp.simplify(sp.expand(expr - theirs))
        rep.check('record_equation ' + key, diff == 0, 'sum_k alpha_k E_(k) + Lambda delta = kappa T equals the record\'s '
                  'generalSource.%s (Revision/field_equations_a4/a4-equations.json)' % key)
    out['lovelock_record_symbols'] = {str(k): {'x0 (= x5 = x6 = x7)': str(Erec[k][0]), 'x1 (= x2 = x3)': str(Erec[k][1]),
                                                'x4': str(Erec[k][4])} for k in (1, 2, 3)}

    # ---------------- C: static-block reduction, author's weights ----------------
    A, k_, w2, w3 = sp.symbols('A k w2 w3', real=True)
    stat = {ad1: A, ad2: 0, uu: 2 * A, vv: 0, kk: k_}
    al = {alpha1: 1, alpha2: w2 / H ** 2, alpha3: w3 / H ** 4}
    F4 = sp.expand((mine['constraint_x4']).subs(stat).subs(al))
    F1 = sp.expand((mine['space_x1_eq_x2_eq_x3']).subs(stat).subs(al))
    F0 = sp.expand((mine['hidden_and_extraTimes_x0_eq_x5_eq_x6_eq_x7']).subs(stat).subs(al))
    G = 1 - 24 * w2 * k_ + 72 * w3 * k_ ** 2
    rep.check('static_block_constraint', sp.simplify(F4 - (-3 * G * A ** 2 + 6 * H ** 2 * k_ * (1 - 2 * w2 * k_) + Lam + kappa * rho)) == 0,
              'static block (a4\' = A, a4\'\' = 0, b4\'/b4 = 2A): x4 component = -3 G(k) A^2 + 6 H^2 k (1 - 2 w2 k) + Lambda + kappa rho, '
              'G(k) = 1 - 24 w2 k + 72 w3 k^2')
    rep.check('static_block_space', sp.simplify(F1 - (-3 * G * A ** 2 + 6 * H ** 2 * k_ * (1 - 2 * w2 * k_) + Lam - kappa * p3)) == 0,
              'static block: x1 component = the x4 component with -kappa p3 in place of kappa rho')
    F0_target = 6 * (12 * w2 * k_ - 1) * A ** 2 - 12 * (w2 - 18 * w3 * k_) * A ** 4 / H ** 2 + 3 * H ** 2 * k_ + Lam - kappa * p0
    rep.check('static_block_hidden', sp.simplify(F0 - F0_target) == 0,
              'static block: x0 component = 6(12 w2 k - 1) A^2 - 12 (w2 - 18 w3 k) A^4/H^2 + 3 H^2 k + Lambda - kappa p0')
    out['static_block'] = {'F4': str(F4), 'F1': str(F1), 'F0': str(F0), 'G(k)': str(G)}

    # ---------------- D: spin connection with the author's gammas ----------------
    alg = read_json(os.path.join(OUT, 'algebra.json'))
    gam = [sp.Matrix(alg['gamma'][a]) for a in range(N)]
    eta = alg['eta']
    S = [[(gam[a] * gam[b] - gam[b] * gam[a]) / 4 for b in range(N)] for a in range(N)]
    # signed vielbein in the author's chart: e^0_0 = f cot z, e^i_i = e^{a4}, e^4_4 = 1, e^t_t = f sin(z)^{1/6}
    fz = sp.exp(-a4) * sp.sqrt(b4)
    evec = [fz * sp.cot(z), sp.exp(a4), sp.exp(a4), sp.exp(a4), sp.Integer(1),
            fz * sp.sin(z) ** sp.Rational(1, 6), fz * sp.sin(z) ** sp.Rational(1, 6), fz * sp.sin(z) ** sp.Rational(1, 6)]
    einv = [1 / e for e in evec]   # e_a^mu (diagonal)
    ok_viel = all(sp.simplify(evec[m] ** 2 * eta[m] - gx[m, m]) == 0 for m in range(N))
    rep.check('vielbein', ok_viel, 'g_mu mu = eta_aa (e^a_mu)^2 with e^0_0 = f cot z (signed), e^i_i = e^{a4}, e^4_4 = 1, '
              'e^t_t = f sin(z)^{1/6}')
    # omega_mu^a_b = e^a_nu (d_mu e^nu_b + Gam^nu_{mu l} e^l_b)
    Omega = []
    for mu in range(N):
        Om = sp.zeros(16, 16)
        for a in range(N):
            for b in range(N):
                # e^a_nu with nu = a (diagonal), e^nu_b with nu = b
                w = evec[a] * ((sp.diff(einv[b], X[mu]) if a == b else 0) + Gx[a][mu][b] * einv[b])
                w = sp.simplify(w)
                if w != 0:
                    w_ab = eta[a] * w     # omega_mu ab = eta_ac omega_mu^c_b
                    Om += sp.Rational(1, 2) * w_ab * S[a][b]
        Omega.append(Om.applyfunc(sp.simplify))
    # covariant constancy of gamma^nu = e^nu_a gamma^a: d_mu gamma^nu + Gam^nu_{mu l} gamma^l + [Omega_mu, gamma^nu] = 0
    gup = [einv[n] * gam[n] for n in range(N)]
    ok_cc = True
    for mu in range(N):
        for n in range(N):
            M = sp.diff(gup[n], X[mu]) + sum((Gx[n][mu][l] * gup[l] for l in range(N)), sp.zeros(16, 16)) \
                + Omega[mu] * gup[n] - gup[n] * Omega[mu]
            if M.applyfunc(sp.simplify) != sp.zeros(16, 16):
                ok_cc = False
    rep.check('gamma_covariantly_constant', ok_cc, 'd_mu gamma^nu + Gamma^nu_{mu l} gamma^l + [Omega_mu, gamma^nu] = 0 for all mu, nu: '
              'Omega_mu = (1/2) omega_mu ab S^ab is the canonical (metric-compatible, torsion-free) spin connection')
    gO = sp.zeros(16, 16)
    for mu in range(N):
        gO += gup[mu] * Omega[mu]
    gO = gO.applyfunc(sp.simplify)
    target = sp.Rational(3, 2) * H / fz * gam[0] + (sp.diff(b4, x4) / b4 - sp.diff(a4, x4) / 2) * gam[4]
    rep.check('gamma_mu_Omega_mu', (gO - target).applyfunc(sp.simplify) == sp.zeros(16, 16),
              'gamma^mu Omega_mu = (3/2)(H/f) gamma^(x0) + (b4\'/b4 - a4\'/2) gamma^(x4), f = e^{-a4} b4^{1/2} (0 < z < pi)')
    flat = target.subs(H, 0).subs({sp.Derivative(b4, x4): 0, sp.Derivative(a4, x4): 0})
    rep.check('nontrivial_unless_flat', flat == sp.zeros(16, 16) and target.subs(H, 1) != sp.zeros(16, 16),
              'gamma^mu Omega_mu vanishes only for H = 0 with constant a4, b4 (flat 4+4 space): the canonical spin connection is non-trivial')
    out['gamma_mu_Omega_mu'] = '(3/2) (H/f) gamma^(x0) + (b4\'/b4 - a4\'/2) gamma^(x4)'
    out['runtime_s'] = round(time.time() - t0, 1)
    write_json(os.path.join(OUT, 'geometry.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
