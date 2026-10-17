#!/usr/bin/env python3
"""Lead's independent check of the a4 and b4 field equations (Revision/field_equations_a4/a4-equations.json).

Written from scratch; imports no Revision code.  For the corrected primordial metric of 2026-10-16 (version 2;
Revision/SPEC.md section 1, Revision/metric_warped/)
    g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)),   z = 6 H x0 real,
for GENERAL functions a4(x4) and b4(x4) > 0 and every real z with sin z cos z != 0 (until 2026-10-16 this check used the
metric of 2026-10-14, now withdrawn):

1. The Einstein tensor G^mu_nu with general a4 and b4, from this file's own Christoffel symbols and the MTW Riemann
   tensor: it is diagonal, independent of x0, isotropic in 3-space and equal on x0 and the three extra times, and
   depends on b4 only through u = b4'/b4, v = u' and k = e^{2 a4}/b4; its components are compared with the record's
   Einstein equations (constraint_x4, space_x1, hidden_x0, nullEnergy_x0, nullEnergy_x1) for the source
   T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) and G^mu_nu + Lambda delta^mu_nu = kappa T^mu_nu.
2. Vacuum: the flat member a4 = 0, b4 = H^2 (x4 - c)^2 solves G = 0; no exponential history a4 = A H x4 + a0,
   b4 = b4(0) e^(beta A H x4) is a vacuum solution of the Einstein equations, for any Lambda.
3. The Gauss-Bonnet (Lanczos) tensor from the CLASSICAL formula
     H_mu nu = 2 (R R_mu nu - 2 R_mu a R^a_nu - 2 R_mu a nu b R^ab + R_mu^abc R_nu abc)
               - (1/2) g_mu nu (R^2 - 4 R_ab R^ab + R_abcd R^abcd)
   (independent of the GKD route; all index sums written out) for the exponential history, compared with the alpha_2
   terms of the record's exponentialHistory.requiredSource (rho, p3, p0, p_t; E_(2) = H by the Lovelock normalisation
   of the record), and the Einstein tensor with its alpha_1 terms.

Exact calculus (no simplification heuristics), computed twice, once for each sign sigma of sin z: the metric functions
are rational expressions in the symbols t = |sin z|^(1/6) > 0 (so sin z = sigma t^6, (sin^2 z)^(1/6) = t^2), c = cos z
(signed; c^2 = 1 - t^12), e = e^(a4), q = b4^(1/2) and the derivatives a1 = a4', a2 = a4'', a3 = a4''', u = b4'/b4, v = u',
w = v', with d/dx0: t -> sigma H c/t^5, c -> -6 H sigma t^6 and d/dx4: e -> a1 e, q -> u q/2, a1 -> a2 -> a3, u -> v -> w.
Every expression is reduced to numerator/denominator with the numerator and the denominator taken modulo
c^2 = 1 - t^12, the denominator made free of c; the two signs cover every real z with sin z cos z != 0.

Usage (from the repository root):  python Revision/lead_checks/einstein_gauss_bonnet_a4.py
Output (deterministic, LF): Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, 'reports', 'einstein-gauss-bonnet-a4.json')
REC = os.path.join(ROOT, 'Revision', 'field_equations_a4', 'a4-equations.json')
N = 8
H, A, Lam, kappa, beta = sp.symbols('H A Lam kappa beta', real=True)
rho, p3, pt, p0 = sp.symbols('rho p3 pt p0', real=True)
t, e, q = sp.symbols('t e q', positive=True)
c = sp.symbols('c', real=True)
a1, a2, a3, u, v, w = sp.symbols('a1 a2 a3 u v w', real=True)
alpha1, alpha2, alpha3 = sp.symbols('alpha1 alpha2 alpha3', real=True)
SIGNS = (1, -1)
checks = []


def check(name, ok, detail):
    checks.append({'name': name, 'verdict': 'PASS' if ok else 'FAIL', 'detail': detail})


def make_deriv(rule4, sigma):
    """d/dx_mu on the ring; rule4 gives the x4 derivatives of the x4 symbols; sigma = the sign of sin z."""
    rule0 = {t: sigma * H * c / t**5, c: -6 * H * sigma * t**6}

    def d(expr, mu):
        rule = rule4 if mu == 4 else rule0 if mu == 0 else None
        if rule is None:
            return sp.Integer(0)
        return sp.Add(*[sp.diff(expr, s) * val for s, val in rule.items() if expr.has(s)])
    return d


def _modc(p):
    p = sp.expand(p)
    return sp.expand(sp.rem(sp.Poly(p, c), sp.Poly(c**2 - 1 + t**12, c)).as_expr()) if p.has(c) else p


def red(expr):
    """canonical form: numerator and denominator reduced modulo c^2 = 1 - t^12, the denominator made free of c
    (multiplied with its conjugate d0 - d1 c), so the form is unique: zero iff the expression is zero, and a
    quantity that does not depend on x0 shows no t and no c."""
    n, dd = sp.fraction(sp.cancel(sp.together(expr)))
    n, dd = _modc(n), _modc(dd)
    if dd.has(c):
        d1 = dd.coeff(c, 1)
        d0 = sp.expand(dd - d1 * c)
        n, dd = _modc(n * (d0 - d1 * c)), _modc(dd * (d0 - d1 * c))
    n1 = n.coeff(c, 1) if n.has(c) else sp.Integer(0)
    n0 = sp.expand(n - n1 * c)
    return sp.cancel(n0 / dd) + c * sp.cancel(n1 / dd)


def curvature(gd, d):
    """Christoffel, Riemann R^a_bcd (MTW), Ricci R_bd for a diagonal metric gd (list)."""
    gi = [1 / x for x in gd]
    Gm = [[[sp.Integer(0)] * N for _ in range(N)] for _ in range(N)]
    for l in range(N):
        for i in range(N):
            for j in range(N):
                val = 0
                if l == j:
                    val += d(gd[l], i)
                if l == i:
                    val += d(gd[l], j)
                if i == j:
                    val -= d(gd[i], l)
                if val != 0:
                    Gm[l][i][j] = red(gi[l] * val / 2)
    Rie = {}
    for a in range(N):
        for b in range(N):
            for cc_ in range(N):
                for dd in range(cc_ + 1, N):
                    val = d(Gm[a][b][dd], cc_) - d(Gm[a][b][cc_], dd) + \
                        sum(Gm[a][cc_][k] * Gm[k][b][dd] - Gm[a][dd][k] * Gm[k][b][cc_] for k in range(N))
                    val = red(val)
                    if val != 0:
                        Rie[(a, b, cc_, dd)] = val
                        Rie[(a, b, dd, cc_)] = -val
    Ric = [[sp.Integer(0)] * N for _ in range(N)]
    for (a, b, cc_, dd), val in Rie.items():
        if a == cc_:
            Ric[b][dd] += val
    Ric = [[red(x) for x in row] for row in Ric]
    return gi, Rie, Ric


def metric():
    """the corrected metric in the ring: cot z = c/(sigma t^6), so cot^2 z = c^2/t^12; (sin^2 z)^(1/6) = t^2."""
    return [q**2 * c**2 / (e**2 * t**12)] + [e**2] * 3 + [sp.Integer(-1)] + [-(q**2) * t**2 / e**2] * 3


rec = json.load(open(REC, encoding='utf-8'))
ad1, ad2, uu, vv, kk = sp.symbols('ad1 ad2 uu vv kk', real=True)
LOC = {'ad1': ad1, 'ad2': ad2, 'uu': uu, 'vv': vv, 'kk': kk, 'H': H, 'Lam': Lam, 'kappa': kappa, 'rho': rho,
       'p3': p3, 'pt': pt, 'p0': p0, 'AA': A, 'be': beta, 'alpha1': alpha1, 'alpha2': alpha2, 'alpha3': alpha3}
TOREC = {ad1: a1, ad2: a2, uu: u, vv: v, kk: e**2 / q**2}   # the record's symbols in this file's ring


def P(s):
    return sp.parse_expr(s.replace('^', '**'), local_dict=LOC).subs(TOREC)


def eq(rec_entry):
    lhs, rhs = rec_entry['input'].split('==')
    return P(lhs) - P(rhs)


E = rec['einstein']
L = rec['exponentialHistory']['requiredSource']
rs = {k: P(L[k]['input']) for k in ('rho', 'p3', 'p0', 'pt')}
res = {}
for sigma in SIGNS:
    r = {}
    # ---- 1. Einstein tensor with general a4 and b4 ----
    d = make_deriv({e: a1 * e, q: u * q / 2, a1: a2, a2: a3, u: v, v: w}, sigma)
    gd = metric()
    gi, Rie, Ric = curvature(gd, d)
    Rs = red(sum(gi[i] * Ric[i][i] for i in range(N)))
    Gs = [[red(gi[m] * Ric[m][n] - (Rs / 2 if m == n else 0)) for n in range(N)] for m in range(N)]   # G^m_n
    Gk = [sp.cancel(Gs[i][i].subs(e, sp.sqrt(kk) * q)) for i in range(N)]  # in k = e^2/q^2
    r['x0free'] = all(not Gs[i][i].has(t) and not Gs[i][i].has(c) and not Gk[i].has(q) and not Gk[i].has(e) for i in range(N))
    r['offdiag'] = all(Gs[i][j] == 0 for i in range(N) for j in range(N) if i != j)
    r['iso'] = Gs[1][1] == Gs[2][2] == Gs[3][3] and Gs[0][0] == Gs[5][5] == Gs[6][6] == Gs[7][7]
    T = {4: -rho, 1: p3, 0: p0}             # index k = xk
    mine = {k: Gs[k][k] + Lam - kappa * val for k, val in T.items()}  # = 0 are the field equations
    r['rec'] = {}
    for key, k in (('constraint_x4', 4), ('space_x1', 1), ('hidden_x0', 0)):
        rr = eq(E[key])
        r['rec'][key] = (red(mine[k] - rr) == 0 or red(mine[k] + rr) == 0, sp.sstr(sp.expand(Gk[k])))
    null0 = sp.expand(Gs[0][0] - Gs[4][4])          # kappa (rho + p0)
    null3 = sp.expand(Gs[1][1] - Gs[4][4])          # kappa (rho + p3)
    n0r = sp.solve(eq(E['nullEnergy_x0']), p0)[0] + rho
    n3r = sp.solve(eq(E['nullEnergy_x1']), p3)[0] + rho
    r['null'] = (red(null0 - kappa * n0r) == 0 and red(null3 - kappa * n3r) == 0
                 and red(null0 + sp.Rational(3, 2) * (2 * H**2 * e**2 / q**2 + 4 * a1**2 - a1 * u + v)) == 0)
    # ---- 2. vacuum ----
    X = sp.symbols('X', positive=True)  # x4 - c0
    flat = {a1: 0, a2: 0, e: 1, q: H * X, u: 2 / X, v: -2 / X**2}
    r['flat'] = all(sp.simplify(Gs[i][i].subs(flat)) == 0 for i in range(N))
    expo = {a1: A * H, a2: 0, u: beta * A * H, v: 0}
    kk_ = sp.Symbol('kk_', positive=True)
    g4, g1, g0 = (sp.expand(sp.cancel(Gs[k][k].subs(expo).subs(e, sp.sqrt(kk_) * q))) for k in (4, 1, 0))
    d1 = sp.factor(g4 - g1)
    sol = sp.solve(sp.expand(g4 - g0), kk_)
    r['novac'] = (sp.expand(d1 - A**2 * H**2 * (beta - 2) * (beta - 4)) == 0 and len(sol) == 1
                  and sp.expand(sol[0] - A**2 * (beta - 4) / 2) == 0)
    # ---- 3. Gauss-Bonnet tensor for the exponential history ----
    dl = make_deriv({e: A * H * e, q: beta * A * H * q / 2}, sigma)
    gl = metric()
    gil, Riel, Ricl = curvature(gl, dl)
    Rl = red(sum(gil[i] * Ricl[i][i] for i in range(N)))
    Rlow = {k_: red(gl[k_[0]] * val) for k_, val in Riel.items()}         # R_abcd = g_aa R^a_bcd
    RicUp = [[gil[a] * gil[b] * Ricl[a][b] for b in range(N)] for a in range(N)]
    Kret = red(sum(val * val * gil[a] * gil[b] * gil[cc_] * gil[dd] for (a, b, cc_, dd), val in Rlow.items()))
    RicSq = red(sum(Ricl[a][b] * RicUp[a][b] for a in range(N) for b in range(N)))
    GBscalar = red(Rl**2 - 4 * RicSq + Kret)

    def Hlow(m, n):
        t1 = Rl * Ricl[m][n]
        t2 = sum(Ricl[m][a] * gil[a] * Ricl[a][n] for a in range(N))
        t3 = sum(Rlow.get((m, a, n, b), 0) * RicUp[a][b] for a in range(N) for b in range(N))
        t4 = sum(Rlow.get((m, a, b, cc_), 0) * Rlow.get((n, a, b, cc_), 0) * gil[a] * gil[b] * gil[cc_]
                 for a in range(N) for b in range(N) for cc_ in range(N))
        return 2 * (t1 - 2 * t2 - 2 * t3 + t4) - (gl[m] * GBscalar / 2 if m == n else 0)

    Hmix = {(m, n): red(gil[m] * Hlow(m, n)) for m, n in [(1, 1), (4, 4), (5, 5), (0, 0), (4, 0), (0, 4), (1, 5)]}
    r['gbdiag'] = (all(not Hmix[(i, i)].has(t) and not Hmix[(i, i)].has(c) for i in (1, 4, 5, 0))
                   and Hmix[(4, 0)] == 0 and Hmix[(0, 4)] == 0 and Hmix[(1, 5)] == 0 and red(Hmix[(0, 0)] - Hmix[(5, 5)]) == 0)
    a2part = {k_: sp.expand(sp.diff(sp.expand(kappa * val), alpha2)) for k_, val in rs.items()}
    r['gb'] = (red(a2part['rho'] + Hmix[(4, 4)]) == 0 and red(a2part['p3'] - Hmix[(1, 1)]) == 0
               and red(a2part['p0'] - Hmix[(0, 0)]) == 0 and red(a2part['pt'] - Hmix[(5, 5)]) == 0)
    r['gbtext'] = sp.sstr(sp.factor(sp.cancel(Hmix[(4, 4)].subs(e, sp.sqrt(kk) * q))))
    a1part = {k_: sp.expand(sp.diff(sp.expand(kappa * val), alpha1)) for k_, val in rs.items()}
    Gl = {m: red(gil[m] * Ricl[m][m] - Rl / 2) for m in (4, 1, 5, 0)}
    r['ein_alpha1'] = (red(a1part['rho'] + Gl[4]) == 0 and red(a1part['p3'] - Gl[1]) == 0 and red(a1part['p0'] - Gl[0]) == 0
                       and red(a1part['pt'] - Gl[5]) == 0)
    res[sigma] = r

BOTH = ' (computed for both signs of sin z: every real z with sin z cos z != 0)'
check('einstein_diagonal_x0_independent', all(res[s]['x0free'] for s in SIGNS),
      "every diagonal component of G^mu_nu is independent of x0 (z) and depends on a4 and b4 only through a4', a4'', u = b4'/b4, v = u' "
      "and k = e^(2 a4)/b4" + BOTH)
check('einstein_off_diagonal_vanish', all(res[s]['offdiag'] for s in SIGNS),
      'every off-diagonal component of G^mu_nu vanishes identically (in the metric of 2026-10-14 G^x4_x0 = (3/2) H cot z b4\'/b4 did not)' + BOTH)
check('einstein_isotropy', all(res[s]['iso'] for s in SIGNS),
      'G^x1_x1 = G^x2_x2 = G^x3_x3 and G^x0_x0 = G^x5_x5 = G^x6_x6 = G^x7_x7 (so p0 = p_t)' + BOTH)
for key in ('constraint_x4', 'space_x1', 'hidden_x0'):
    check('einstein_' + key, all(res[s]['rec'][key][0] for s in SIGNS),
          f"G + Lambda = kappa T, component {key}: mine G = {res[1]['rec'][key][1]} (k = e^(2a4)/b4); record: {E[key]['input']}" + BOTH)
check('einstein_null_energy', all(res[s]['null'] for s in SIGNS),
      "kappa (rho + p0) = -(3/2)(2 H^2 k + 4 a4'^2 - a4' u + v) and kappa (rho + p3) equal the record's nullEnergy_x0 and nullEnergy_x1" + BOTH)
check('einstein_flat_vacuum', all(res[s]['flat'] for s in SIGNS),
      'a4 = 0, b4 = H^2 (x4 - c)^2: every component of G vanishes (the flat member is a vacuum with Lambda = 0)' + BOTH)
check('einstein_no_exponential_vacuum', all(res[s]['novac'] for s in SIGNS),
      'exponential histories a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4): G^x4_x4 - G^x1_x1 = A^2 H^2 (beta - 2)(beta - 4) and G^x4_x4 - G^x0_x0 = 0 '
      'needs k = A^2 (beta - 4)/2: beta = 4 or A = 0 give k = 0, beta = 2 gives k = -A^2; no vacuum with k > 0 for any Lambda' + BOTH)
check('gauss_bonnet_diagonal', all(res[s]['gbdiag'] for s in SIGNS),
      'for a4 = A H x4, b4 = b4(0) e^(beta A H x4) the classical Gauss-Bonnet tensor H^mu_nu is diagonal (H^x4_x0 = H^x0_x4 = H^x1_x5 = 0), free of x0, '
      'with H^x0_x0 = H^x5_x5; H^x4_x4 = ' + res[1]['gbtext'] + BOTH)
check('gauss_bonnet_source_alpha2', all(res[s]['gb'] for s in SIGNS),
      'the alpha_2 parts of kappa rho, kappa p3, kappa p0, kappa p_t in the record (exponentialHistory.requiredSource) equal -H^x4_x4, H^x1_x1, '
      'H^x0_x0, H^x5_x5 of the classical Gauss-Bonnet tensor' + BOTH)
check('einstein_exponential_source_alpha1', all(res[s]['ein_alpha1'] for s in SIGNS),
      'the alpha_1 parts of kappa rho, p3, p0 and p_t in the record equal -G^x4_x4, G^x1_x1, G^x0_x0 and G^x5_x5 on the history' + BOTH)

report = {
    'producer': 'Revision/lead_checks/einstein_gauss_bonnet_a4.py (lead, independent; no Revision code imported; '
                'reads the record Revision/field_equations_a4/a4-equations.json to compare)',
    'metric': 'the corrected metric of 2026-10-16 (version 2): diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), every real z',
    'summary': {'passed': sum(c_['verdict'] == 'PASS' for c_ in checks), 'total': len(checks)},
    'checks': checks,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(report, f, indent=1)
    f.write('\n')
print(json.dumps(report['summary']))
for c_ in checks:
    print(c_['verdict'], c_['name'])
raise SystemExit(0 if report['summary']['passed'] == report['summary']['total'] else 1)
