#!/usr/bin/env python3
"""Lead's independent check of the a4 and b4 field equations (Revision/field_equations_a4/a4-equations.json).

Written from scratch; imports no Revision code.  For the author's metric with b4(x4) (SPEC section 1; the change of
2026-10-14), for GENERAL functions a4(x4) and b4(x4) > 0 (since 2026-10-15, the user's orders "b4 is a function of
x4; b4 is NEVER 1" and "move everything to b4(x4)"; until then this check used the withdrawn metric b4 = 1):

1. The Einstein tensor G^mu_nu with general a4 and b4, from this file's own Christoffel symbols and the MTW Riemann
   tensor, compared component by component with the record's Einstein equations (constraint_x4, space_x1,
   extraTime_x5, hidden_x0, offDiagonal_x4x0, nullEnergy) for the source T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t,
   p_t, p_t) + q40 (x4, x0) + q04 (x0, x4) (order x0, x1, ..., x7) and G^mu_nu + Lambda delta^mu_nu = kappa T^mu_nu;
   the diagonal is independent of x0; the only nonzero off-diagonal components are G^x4_x0 and G^x0_x4.
2. noVacuum: T = 0 has no solution for H > 0, for any Lambda and any a4, b4.
3. The Gauss-Bonnet (Lanczos) tensor from the CLASSICAL formula
     H_mu nu = 2 (R R_mu nu - 2 R_mu a R^a_nu - 2 R_mu a nu b R^ab + R_mu^abc R_nu abc)
               - (1/2) g_mu nu (R^2 - 4 R_ab R^ab + R_abcd R^abcd)
   (independent of the GKD route; all index sums written out, since the Ricci tensor is not diagonal when b4 is not
   constant) for the exponential history a4 = A H x4, b4 = b4(0) e^(beta A H x4), compared with the alpha_2 terms of
   the record's exponentialHistory.requiredSource (rho, p3, p_t, p0 and q40; E_(2) = H by the Lovelock normalisation
   of the record), and the Einstein tensor with its alpha_1 terms.

Exact calculus (no simplification heuristics): the metric functions are polynomial/rational expressions in the
symbols t = sin(z)^(1/6), c = cos z (z = 6 H x0; c^2 = 1 - t^12), e = e^(a4), q = b4^(1/2) and the derivatives
a1 = a4', a2 = a4'', a3 = a4''', u = b4'/b4, v = u', w = v', with d/dx0: t -> H c/t^5, c -> -6 H t^6 and d/dx4:
e -> a1 e, q -> u q/2, a1 -> a2 -> a3, u -> v -> w.  Every expression is reduced to numerator/denominator with the
numerator taken modulo c^2 = 1 - t^12.  (A first version of 2026-10-15 used sympy's general simplification on the
functions a4(x4), b4(x4) and did not finish within 7 min 3 s: claude_failures.md G5.)

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
rho, p3, pt, p0, q40, q04 = sp.symbols('rho p3 pt p0 q40 q04', real=True)
t, c, e, q = sp.symbols('t c e q', positive=True)
a1, a2, a3, u, v, w = sp.symbols('a1 a2 a3 u v w', real=True)
alpha1, alpha2, alpha3 = sp.symbols('alpha1 alpha2 alpha3', real=True)
checks = []


def check(name, ok, detail):
    checks.append({'name': name, 'verdict': 'PASS' if ok else 'FAIL', 'detail': detail})


def make_deriv(rule4):
    """d/dx_mu on the ring; rule4 gives the x4 derivatives of the x4 symbols."""
    rule0 = {t: H * c / t**5, c: -6 * H * t**6}

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


def metric(warp4, warp5):
    """g = diag(cot^2 z, warp4^2 sin^(1/3) z (x3), -1, -warp5^2 sin^(1/3) z (x3)) in the ring (sin^(1/3) = t^2)."""
    return [c**2 / t**12] + [warp4**2 * t**2] * 3 + [sp.Integer(-1)] + [-(warp5**2) * t**2] * 3


rec = json.load(open(REC, encoding='utf-8'))
ad1, ad2, uu, vv, cc = sp.symbols('ad1 ad2 uu vv cc', real=True)
LOC = {'ad1': ad1, 'ad2': ad2, 'uu': uu, 'vv': vv, 'cc': cc, 'H': H, 'Lam': Lam, 'kappa': kappa, 'rho': rho,
       'p3': p3, 'pt': pt, 'p0': p0, 'q40': q40, 'q04': q04, 'AA': A, 'be': beta, 'alpha1': alpha1,
       'alpha2': alpha2, 'alpha3': alpha3}
TOREC = {ad1: a1, ad2: a2, uu: u, vv: v, cc: c / t**6}   # the record's symbols in this file's ring


def P(s):
    return sp.parse_expr(s.replace('^', '**'), local_dict=LOC).subs(TOREC)


def eq(rec_entry):
    lhs, rhs = rec_entry['input'].split('==')
    return P(lhs) - P(rhs)


# ---- 1. Einstein tensor with general a4 and b4 ----
d = make_deriv({e: a1 * e, q: u * q / 2, a1: a2, a2: a3, u: v, v: w})
gd = metric(e, q / e)
gi, Rie, Ric = curvature(gd, d)
Rs = red(sum(gi[i] * Ric[i][i] for i in range(N)))
Gs = [[red(gi[m] * Ric[m][n] - (Rs / 2 if m == n else 0)) for n in range(N)] for m in range(N)]   # G^m_n
check('einstein_diagonal_x0_independent', all(not Gs[i][i].has(t) and not Gs[i][i].has(c) and not Gs[i][i].has(e)
                                              and not Gs[i][i].has(q) for i in range(N)),
      'every diagonal component of G^mu_nu is independent of x0 (z) and of e^(a4), and depends on b4 only through u = b4\'/b4 and v = u\'')
check('einstein_off_diagonal', all(Gs[i][j] == 0 for i in range(N) for j in range(N) if i != j and (i, j) not in ((4, 0), (0, 4)))
      and red(Gs[4][0] - sp.Rational(3, 2) * H * u * c / t**6) == 0 and red(Gs[0][4] + sp.Rational(3, 2) * H * u * t**6 / c) == 0,
      'the only nonzero off-diagonal components are G^x4_x0 = (3/2) H cot z b4\'/b4 and G^x0_x4 = -(3/2) H tan z b4\'/b4')
check('einstein_isotropy', Gs[1][1] == Gs[2][2] == Gs[3][3] and Gs[5][5] == Gs[6][6] == Gs[7][7],
      'G^x1_x1 = G^x2_x2 = G^x3_x3 and G^x5_x5 = G^x6_x6 = G^x7_x7')
T = {4: -rho, 1: p3, 5: pt, 0: p0}             # index k = xk
mine = {k: Gs[k][k] + Lam - kappa * val for k, val in T.items()}  # = 0 are the field equations
E = rec['einstein']
for key, k in (('constraint_x4', 4), ('space_x1', 1), ('extraTime_x5', 5), ('hidden_x0', 0)):
    r = eq(E[key])
    check('einstein_' + key, red(mine[k] - r) == 0 or red(mine[k] + r) == 0,
          f"G^x{k}_x{k} + Lambda = kappa T: mine = {sp.sstr(sp.expand(mine[k]))}; record: {E[key]['input']}")
off_mine = Gs[4][0] - kappa * q40
check('einstein_offDiagonal_x4x0', red(off_mine - eq(E['offDiagonal_x4x0'])) == 0,
      'G^x4_x0 = kappa q40: mine ' + sp.sstr(off_mine) + ' = 0; record ' + E['offDiagonal_x4x0']['input'])
null_mine = sp.expand(Gs[0][0] - Gs[4][4])          # kappa (rho + p0)
null_rec = sp.solve(eq(E['nullEnergy']), p0)[0] + rho
check('einstein_null_energy', sp.expand(null_mine - kappa * null_rec) == 0
      and sp.expand(null_mine - (-6 * H**2 - 3 * a1**2 - sp.Rational(3, 4) * (u - 2 * a1)**2 - sp.Rational(3, 2) * v)) == 0,
      'kappa (rho + p0) = ' + sp.sstr(null_mine) + ' = -6 H^2 - 3 a4\'^2 - (3/4)(u - 2 a4\')^2 - (3/2) v: negative wherever v = (b4\'/b4)\' >= 0')

# ---- 2. no vacuum ----
sol_u = sp.solve(red(Gs[4][0] * t**6 / c), u)
vac0 = [sp.expand(Gs[k][k].subs({u: 0, v: 0})) for k in (4, 0)]
check('no_vacuum_for_H_positive',
      sol_u == [0] and sp.expand(vac0[0] - vac0[1] - (6 * a1**2 + 6 * H**2)) == 0,
      'T = 0: the x4-x0 component (3/2) H cot z b4\'/b4 = 0 forces b4\'/b4 = 0, and then G^x4_x4 - G^x0_x0 = 6 a4\'^2 + 6 H^2 > 0 for H > 0: '
      'no vacuum solution for any Lambda, a4 and b4')

# ---- 3. Gauss-Bonnet tensor for the exponential history a4 = A H x4, b4 = b4(0) e^(beta A H x4) ----
dl = make_deriv({e: A * H * e, q: beta * A * H * q / 2})
gl = metric(e, q / e)
gil, Riel, Ricl = curvature(gl, dl)
Rl = red(sum(gil[i] * Ricl[i][i] for i in range(N)))
Rlow = {k: red(gl[k[0]] * val) for k, val in Riel.items()}         # R_abcd = g_aa R^a_bcd
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


Hmix = {(m, n): red(gil[m] * Hlow(m, n)) for m, n in [(1, 1), (4, 4), (5, 5), (0, 0), (4, 0)]}
check('gauss_bonnet_diagonal_constant', all(not Hmix[(i, i)].has(t) and not Hmix[(i, i)].has(c) and not Hmix[(i, i)].has(e)
                                            and not Hmix[(i, i)].has(q) for i in (1, 4, 5, 0)),
      'for a4 = A H x4, b4 = b4(0) e^(beta A H x4) the diagonal of the Gauss-Bonnet tensor H^mu_nu is constant: '
      + sp.sstr([sp.factor(Hmix[(i, i)]) for i in (1, 4, 5, 0)]))
L = rec['exponentialHistory']['requiredSource']
rs = {k: P(L[k]['input']) for k in ('rho', 'p3', 'pt', 'p0', 'q40')}
# field equations: alpha2 H^4_4 = -kappa rho, alpha2 H^1_1 = kappa p3, alpha2 H^5_5 = kappa p_t, alpha2 H^0_0 = kappa p0,
# alpha2 H^4_0 = kappa q40
a2part = {k: sp.expand(sp.diff(sp.expand(kappa * val), alpha2)) for k, val in rs.items()}
okd = (red(a2part['rho'] + Hmix[(4, 4)]) == 0 and red(a2part['p3'] - Hmix[(1, 1)]) == 0
       and red(a2part['pt'] - Hmix[(5, 5)]) == 0 and red(a2part['p0'] - Hmix[(0, 0)]) == 0)
check('gauss_bonnet_source_alpha2', okd,
      'alpha_2 parts of kappa rho, kappa p3, kappa p_t, kappa p0 in the record equal -H^x4_x4, H^x1_x1, H^x5_x5, H^x0_x0 of the classical '
      'Gauss-Bonnet tensor (record rho: ' + sp.sstr(sp.factor(a2part['rho'])) + ')')
check('gauss_bonnet_offdiagonal_alpha2', red(a2part['q40'] - Hmix[(4, 0)]) == 0,
      'alpha_2 part of kappa q40 in the record equals H^x4_x0 of the classical Gauss-Bonnet tensor: ' + sp.sstr(sp.factor(Hmix[(4, 0)])))
a1part = {k: sp.expand(sp.diff(sp.expand(kappa * val), alpha1)) for k, val in rs.items()}
Gl = {m: red(gil[m] * Ricl[m][m] - Rl / 2) for m in (4, 1, 5, 0)}
Gl40 = red(gil[4] * Ricl[4][0])
check('einstein_exponential_source_alpha1',
      red(a1part['rho'] + Gl[4]) == 0 and red(a1part['p3'] - Gl[1]) == 0 and red(a1part['pt'] - Gl[5]) == 0
      and red(a1part['p0'] - Gl[0]) == 0 and red(a1part['q40'] - Gl40) == 0,
      'alpha_1 parts of kappa rho, p3, p_t, p0 and q40 in the record equal -G^x4_x4, G^x1_x1, G^x5_x5, G^x0_x0 and G^x4_x0 on the history: '
      + sp.sstr([sp.factor(-Gl[4]), sp.factor(Gl[1]), sp.factor(Gl[5]), sp.factor(Gl[0])]))

report = {
    'producer': 'Revision/lead_checks/einstein_gauss_bonnet_a4.py (lead, independent; no Revision code imported; '
                'reads the record Revision/field_equations_a4/a4-equations.json to compare)',
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
