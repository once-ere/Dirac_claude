#!/usr/bin/env python3
"""Lead's independent checks (Revision/lead_checks): written from scratch, imports no other Revision code.

The metric is the corrected primordial metric of 2026-10-16 (version 2; Revision/SPEC.md section 1,
Revision/metric_warped/), for GENERAL functions a4(x4) and b4(x4) > 0 and EVERY real z = 6 H x0 with sin z cos z != 0
(x0 is space-like, x4 the time; (sin^2 z)^(1/6) is the positive branch):
    g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)).
(Until 2026-10-16 these checks used the metric of 2026-10-14, now withdrawn.)

1. nabla_mu T^mu_nu for a diagonal source T^mu_nu = diag(p0, p3, p3, p3, -rho, p_t, p_t, p_t) in the author's order
   x0, x1, ..., x7, all functions of x4 and x0:
     x4 component:  -d rho/d x4 - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0),  h4 = b4'/(2 b4) - a4'
     x0 component:   d p0/d x0 + 3 H cot z (p0 - p_t)        (z = 6 H x0)
     all other components identically zero.
2. The x0 component in the coordinate y = ln|sin z|/(6H) (dy/dx0 = cot z) is cot z times p0'(y) + 3 H (p0 - p_t).
3. gamma^mu Omega_mu for the diagonal vielbein (e^x0 = e^{-a4} b4^{1/2} cot z, signed), with the canonical spin
   connection omega_mu^a_b = e^a_nu (d_mu e^nu_b + Gamma^nu_mu_lambda e^lambda_b), Omega_mu = (1/2) omega_mu ab S^ab,
   S^ab = (1/4)[gamma^a, gamma^b], built from the Revision fixture Revision/algebra/gammas.json:
   gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) exactly, and the same from the
   divergence formula (1/2) gamma^a (1/sqrt|g|) d_mu (sqrt|g| e_a^mu).
Every statement is computed twice, once for each sign s of sin z, with (sin^2 z)^(1/6) written as (s sin z)^(1/3) (the
positive branch, s sin z > 0), so no Abs or sign function appears; every zero test is sympy's simplify to 0; the two
cases cover every real z with sin z cos z != 0 (the sign of cot z enters only through e^x0 = e^{-a4} b4^{1/2} cot z, which
is kept signed).

Usage (from the repository root):  python Revision/lead_checks/emt_divergence_and_spin_connection.py
Output (deterministic, LF): Revision/lead_checks/reports/emt-divergence-and-spin-connection.json
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, 'reports', 'emt-divergence-and-spin-connection.json')

x = sp.symbols('x0:8', real=True)  # the author's coordinates; x[k] = xk
H = sp.symbols('H', positive=True)
a4 = sp.Function('a4', real=True)(x[4])
b4 = sp.Function('b4', positive=True)(x[4])
u = sp.diff(b4, x[4]) / b4  # b4'/b4
h4 = u / 2 - sp.diff(a4, x[4])
z = 6 * H * x[0]
N = 8
SIGNS = (1, -1)  # the sign s of sin z: (sin^2 z)^(1/6) = (s sin z)^(1/3) with s sin z > 0


def christoffel(metric, metric_inv):
    return [[[sp.simplify(sum(metric_inv[l, m] * (sp.diff(metric[m, i], x[j]) + sp.diff(metric[m, j], x[i])
                                                  - sp.diff(metric[i, j], x[m])) for m in range(N)) / 2)
              for j in range(N)] for i in range(N)] for l in range(N)]


def zero(e):
    return sp.simplify(sp.sympify(e)) == 0


def zero_matrix(m):
    return all(zero(v) for v in m)


with open(os.path.join(ROOT, 'Revision', 'algebra', 'gammas.json'), encoding='utf-8') as f:
    fixture = json.load(f)
gam = [sp.Matrix(m) for m in fixture['gamma']]  # order x0..x7: gam[k] = gamma^(xk)
eta = sp.diag(1, 1, 1, 1, -1, -1, -1, -1)
S = [[(gam[a] * gam[b] - gam[b] * gam[a]) / 4 for b in range(N)] for a in range(N)]
ZERO16 = sp.zeros(16, 16)
rho, p3, pt, p0 = [sp.Function(n)(x[4], x[0]) for n in ('rho', 'p3', 'pt', 'p0')]
T = sp.diag(p0, p3, p3, p3, -rho, pt, pt, pt)  # T^mu_nu, order x0, x1, ..., x7
ex4 = -sp.diff(rho, x[4]) - 3 * sp.diff(a4, x[4]) * (rho + p3) - 3 * h4 * (rho + pt) - h4 * (rho + p0)
ex0 = sp.diff(p0, x[0]) + 3 * H * sp.cot(z) * (p0 - pt)
cg = sp.Rational(3, 2) * H * sp.exp(a4) / sp.sqrt(b4)
vg = u - sp.diff(a4, x[4]) / 2


def metric_of(s, sign_block):
    """The metric for one sign s of sin z; sign_block = -1: the corrected metric (the block x0, x5, x6, x7 shrinks with
    e^{-a4}); +1: negative control (the block grows with e^{+a4})."""
    w2 = (s * sp.sin(z)) ** sp.Rational(1, 3)  # = (sin^2 z)^(1/6) where s sin z > 0
    f2 = sp.exp(2 * sign_block * a4) * b4
    return sp.diag(*([f2 * sp.cot(z) ** 2] + [sp.exp(2 * a4)] * 3 + [-1] + [-f2 * w2] * 3))


def vielbein(s, sign_block):
    f = sp.exp(sign_block * a4) * sp.sqrt(b4)
    return [f * sp.cot(z)] + [sp.exp(a4)] * 3 + [sp.Integer(1)] + [f * (s * sp.sin(z)) ** sp.Rational(1, 6)] * 3


def gamma_omega(metric, E):
    """gamma^mu Omega_mu from the canonical spin connection, and (1/2) gamma^a (1/sqrt|g|) d_mu (sqrt|g| e_a^mu)."""
    gim = metric.inv()
    Gm = christoffel(metric, gim)
    e_dn = sp.diag(*E)                   # e^a_mu
    e_up = sp.diag(*[1 / v for v in E])  # e_a^mu (row a, column mu)
    total = ZERO16
    for mu in range(N):
        # omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_mu_lambda e_b^lambda)
        om = sp.zeros(N, N)
        for a in range(N):
            for b in range(N):
                om[a, b] = sp.simplify(sum(e_dn[a, nu] * (sp.diff(e_up[b, nu], x[mu])
                                                          + sum(Gm[nu][mu][lam] * e_up[b, lam] for lam in range(N)))
                                           for nu in range(N)))
        om_ab = eta * om  # lower the first index
        Omega = ZERO16
        for a in range(N):
            for b in range(N):
                if om_ab[a, b] != 0:
                    Omega = Omega + om_ab[a, b] * S[a][b] / 2
        total = total + sum((e_up[c, mu] * gam[c] for c in range(N)), ZERO16) * Omega
    # sqrt|g| = |prod E_a|; prod E_a carries the constant sign of cot z (e^x0 is signed), which cancels in
    # (1/sqrt|g|) d_mu (sqrt|g| e_a^mu), so the signed product is used; its square is det g (> 0, signature (4,4))
    sq = sp.Mul(*E)
    assert zero(sq ** 2 - metric.det())
    divf = sum((gam[a] * sp.simplify(sp.diff(sq * e_up[a, a], x[a]) / sq) / 2 for a in range(N)), ZERO16)
    return total.applyfunc(sp.simplify), divf.applyfunc(sp.simplify)


res = {}
for s in SIGNS:
    r = {}
    g = metric_of(s, -1)
    G = christoffel(g, g.inv())

    def div(nu):
        return (sum(sp.diff(T[m, nu], x[m]) for m in range(N))
                + sum(G[m][m][l] * T[l, nu] for m in range(N) for l in range(N))
                - sum(G[l][m][nu] * T[m, l] for m in range(N) for l in range(N)))

    d = [div(n) for n in range(N)]
    r['div4'] = zero(d[4] - ex4)
    r['div0'] = zero(d[0] - ex0)
    r['divrest'] = all(zero(d[n]) for n in (1, 2, 3, 5, 6, 7))
    # the coordinate y = ln(s sin z)/(6H) = ln|sin z|/(6H)
    yx = sp.log(s * sp.sin(z)) / (6 * H)
    r['jac'] = zero(sp.diff(yx, x[0]) - sp.cot(z))
    y = sp.symbols('y', real=True)
    P0, PT = [sp.Function(n)(y) for n in ('P0', 'PT')]
    lhs = sp.diff(P0.subs(y, yx), x[0]) + 3 * H * sp.cot(z) * (P0.subs(y, yx) - PT.subs(y, yx))
    rhs = sp.cot(z) * (sp.diff(P0, y).subs(y, yx) + 3 * H * (P0.subs(y, yx) - PT.subs(y, yx)))
    r['yform'] = zero(lhs - rhs)
    E = vielbein(s, -1)
    r['vielbein'] = all(zero(eta[a, a] * E[a] ** 2 - g[a, a]) for a in range(N))
    total, divf = gamma_omega(g, E)
    r['gO'] = zero_matrix(total - cg * gam[0] - vg * gam[4])
    r['gOdiv'] = zero_matrix(total - divf)
    g_nc = metric_of(s, +1)
    E_nc = vielbein(s, +1)
    total_nc, divf_nc = gamma_omega(g_nc, E_nc)
    coef4 = sp.simplify((total_nc * gam[4]).trace() / (gam[4] * gam[4]).trace())  # coefficient of gamma^(x4)
    coef0 = sp.simplify((total_nc * gam[0]).trace() / (gam[0] * gam[0]).trace())  # coefficient of gamma^(x0)
    r['nc'] = (all(zero(eta[a, a] * E_nc[a] ** 2 - g_nc[a, a]) for a in range(N)) and zero_matrix(total_nc - divf_nc)
               and zero_matrix(total_nc - coef0 * gam[0] - coef4 * gam[4])
               and zero(coef4 - (u + sp.Rational(7, 2) * sp.diff(a4, x[4])))
               and zero(coef0 - sp.Rational(3, 2) * H * sp.exp(-a4) / sp.sqrt(b4)))
    res[s] = r

checks = []


def check(name, ok, detail):
    checks.append({'name': name, 'verdict': 'PASS' if ok else 'FAIL', 'detail': detail})


BOTH = ' (both signs of sin z, i.e. every real z with sin z cos z != 0)'
check('divergence_x4_component', all(res[s]['div4'] for s in SIGNS),
      "nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0), h4 = b4'/(2 b4) - a4'" + BOTH)
check('divergence_x0_component', all(res[s]['div0'] for s in SIGNS),
      'nabla_mu T^mu_x0 = d p0/d x0 + 3 H cot z (p0 - p_t), z = 6 H x0' + BOTH)
check('divergence_other_components_zero', all(res[s]['divrest'] for s in SIGNS),
      'nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7' + BOTH)
check('ks_coordinate_jacobian', all(res[s]['jac'] for s in SIGNS), 'y = ln|sin z|/(6H) gives dy/dx0 = cot z' + BOTH)
check('ks_coordinate_form', all(res[s]['yform'] for s in SIGNS),
      "x0 component = cot z [p0'(y) + 3 H (p0 - p_t)]: for p0 = p_t (the field equations) it is cot z p0'(y), so p0 must not depend on y" + BOTH)
cliff = all(gam[a] * gam[b] + gam[b] * gam[a] == 2 * eta[a, b] * sp.eye(16) for a in range(N) for b in range(N))
check('fixture_clifford', cliff, 'gammas.json satisfies {gamma^a, gamma^b} = 2 eta^ab with eta = diag(+,+,+,+,-,-,-,-) (order x0..x7)')
check('vielbein_reproduces_metric', all(res[s]['vielbein'] for s in SIGNS),
      'g_mu nu = e^a_mu e^b_nu eta_ab for the diagonal vielbein (e^x0 = e^{-a4} b4^{1/2} cot z signed, e^xt = e^{-a4} b4^{1/2} (sin^2 z)^{1/12})' + BOTH)
check('gamma_Omega_equals_hidden_block_terms', all(res[s]['gO'] for s in SIGNS),
      "gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) exactly: the x0 term comes from the warp of the "
      "three extra times along x0, the x4 term from the rates of x0 (-a4' + u/2), 3-space (3 a4') and the extra times (3 (-a4' + u/2))" + BOTH)
check('gamma_Omega_divergence_formula', all(res[s]['gOdiv'] for s in SIGNS),
      'gamma^mu Omega_mu = (1/2) gamma^a (1/sqrt|g|) d_mu (sqrt|g| e_a^mu) for the diagonal vielbein, computed independently '
      '(sqrt|g| = e^{-a4} b4^2 |cot z| (sin^2 z)^{1/4})' + BOTH)
check('negative_control_growing_block', all(res[s]['nc'] for s in SIGNS),
      "negative control: with the block (x0, x5, x6, x7) GROWING like 3-space (scale factor e^{+a4} b4^{1/2}) gamma^mu Omega_mu = "
      "(3/2) H e^{-a4} b4^{-1/2} gamma^(x0) + (b4'/b4 + (7/2) a4') gamma^(x4): the a4' coefficient is +7/2 instead of -1/2, so the "
      "check sees the direction of the block's scale factor" + BOTH)

report = {
    'producer': 'Revision/lead_checks/emt_divergence_and_spin_connection.py (lead, independent; no Revision code imported)',
    'metric': 'the corrected metric of 2026-10-16 (version 2): diag(e^{-2a4} b4 cot^2 z, e^{2a4} (x3), -1, -e^{-2a4} b4 (sin^2 z)^{1/6} (x3)), every real z',
    'summary': {'passed': sum(c['verdict'] == 'PASS' for c in checks), 'total': len(checks)},
    'checks': checks,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(report, f, indent=1, sort_keys=False)
    f.write('\n')
print(json.dumps(report['summary']))
raise SystemExit(0 if report['summary']['passed'] == report['summary']['total'] else 1)
