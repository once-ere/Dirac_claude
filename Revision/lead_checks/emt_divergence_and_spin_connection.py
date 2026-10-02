#!/usr/bin/env python3
"""Lead's independent checks (Revision/lead_checks): written from scratch, imports no other Revision code.

1. nabla_mu T^mu_nu for the author's metric (SPEC section 1) and a homogeneous diagonal source
   T^mu_nu = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8), all functions of x4 and x8:
     x4 component:  -d rho/d x4 - 3 a4' (p3 - p_t)
     x8 component:   d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t)        (z = 6 H x8)
     all other components identically zero.
2. The x8 component in the Kohn-Sham coordinate y = ln(sin z)/(6H) (dy/dx8 = cot z) is cot z times
   p8'(y) + 6 H p8 - 3 H (p3 + p_t), the form checked by the Kohn-Sham solver (emt_y_conservation_*).
3. gamma^mu Omega_mu for the diagonal vielbein, with the canonical spin connection
   omega_mu^a_b = e^a_nu (d_mu e^nu_b + Gamma^nu_mu_lambda e^lambda_b), Omega_mu = (1/2) omega_mu ab S^ab,
   S^ab = (1/4)[gamma^a, gamma^b], built from the Revision fixture Revision/algebra/gammas.json:
   gamma^mu Omega_mu = 3 H gamma^(x8) exactly (the x4-direction terms of the three inflating and the
   three deflating directions cancel).

Usage (from the repository root):  python Revision/lead_checks/emt_divergence_and_spin_connection.py
Output (deterministic, LF): Revision/lead_checks/reports/emt-divergence-and-spin-connection.json
"""
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, 'reports', 'emt-divergence-and-spin-connection.json')

x = sp.symbols('x1:9', real=True)
H = sp.symbols('H', positive=True)
a4 = sp.Function('a4')(x[3])
z = 6 * H * x[7]
s6 = sp.sin(z) ** sp.Rational(1, 3)
g = sp.diag(*([sp.exp(2 * a4) * s6] * 3 + [-1] + [-sp.exp(-2 * a4) * s6] * 3 + [sp.cot(z) ** 2]))
gi = g.inv()
N = 8


def christoffel():
    return [[[sp.simplify(sum(gi[l, m] * (sp.diff(g[m, i], x[j]) + sp.diff(g[m, j], x[i]) - sp.diff(g[i, j], x[m]))
                              for m in range(N)) / 2) for j in range(N)] for i in range(N)] for l in range(N)]


G = christoffel()
checks = []


def check(name, ok, detail):
    checks.append({'name': name, 'verdict': 'PASS' if ok else 'FAIL', 'detail': detail})


# ---- 1. divergence of the homogeneous diagonal source ----
rho, p3, pt, p8 = [sp.Function(n)(x[3], x[7]) for n in ('rho', 'p3', 'pt', 'p8')]
T = sp.diag(p3, p3, p3, -rho, pt, pt, pt, p8)  # T^mu_nu


def div(nu):
    return sp.simplify(sum(sp.diff(T[m, nu], x[m]) for m in range(N))
                       + sum(G[m][m][l] * T[l, nu] for m in range(N) for l in range(N))
                       - sum(G[l][m][nu] * T[m, l] for m in range(N) for l in range(N)))


d = [div(n) for n in range(N)]
ex4 = -sp.diff(rho, x[3]) - 3 * sp.diff(a4, x[3]) * (p3 - pt)
ex8 = sp.diff(p8, x[7]) + 3 * H * sp.cot(z) * (2 * p8 - p3 - pt)
check('divergence_x4_component', sp.simplify(d[3] - ex4) == 0,
      "nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t)")
check('divergence_x8_component', sp.simplify(d[7] - ex8) == 0,
      'nabla_mu T^mu_x8 = d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t), z = 6 H x8')
check('divergence_other_components_zero', all(sp.simplify(d[n]) == 0 for n in (0, 1, 2, 4, 5, 6)),
      'nabla_mu T^mu_nu = 0 identically for nu = x1, x2, x3, x5, x6, x7')

# ---- 2. the x8 component in the Kohn-Sham coordinate y ----
y = sp.symbols('y', real=True)
zy = sp.asin(sp.exp(6 * H * y))  # sin z = e^{6 H y}, z in (0, pi/2)
dydx8 = sp.simplify(sp.diff(sp.log(sp.sin(z)) / (6 * H), x[7]))
check('ks_coordinate_jacobian', sp.simplify(dydx8 - sp.cot(z)) == 0, 'y = ln(sin z)/(6H) gives dy/dx8 = cot z')
P8, P3, PT = [sp.Function(n)(y) for n in ('P8', 'P3', 'PT')]
lhs = sp.cot(zy) * sp.diff(P8, y) + 3 * H * sp.cot(zy) * (2 * P8 - P3 - PT)
rhs = sp.cot(zy) * (sp.diff(P8, y) + 6 * H * P8 - 3 * H * (P3 + PT))
check('ks_coordinate_form', sp.simplify(lhs - rhs) == 0,
      "x8 component = cot z [p8'(y) + 6 H p8 - 3 H (p3 + p_t)], i.e. (e^{6Hy} p8)' = 3 H e^{6Hy} (p3 + p_t)")

# ---- 3. gamma^mu Omega_mu from the canonical spin connection ----
with open(os.path.join(ROOT, 'Revision', 'algebra', 'gammas.json'), encoding='utf-8') as f:
    fixture = json.load(f)
gam = [sp.Matrix(m) for m in fixture['gamma']]  # order x1..x8
eta = sp.diag(1, 1, 1, -1, -1, -1, -1, 1)
cliff = all(gam[a] * gam[b] + gam[b] * gam[a] == 2 * eta[a, b] * sp.eye(16) for a in range(N) for b in range(N))
check('fixture_clifford', cliff, 'gammas.json satisfies {gamma^a, gamma^b} = 2 eta^ab with eta = diag(+,+,+,-,-,-,-,+)')
S = [[(gam[a] * gam[b] - gam[b] * gam[a]) / 4 for b in range(N)] for a in range(N)]
ZERO16 = sp.zeros(16, 16)


def vielbein(sign_extra):
    """e^a_mu = E_a delta^a_mu; sign_extra = -1: the author's deflating extra times; +1: negative control."""
    return [sp.exp(a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + \
        [sp.exp(sign_extra * a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.cot(z)]


def gamma_omega(metric, E):
    """gamma^mu Omega_mu from the canonical spin connection, and (1/2) gamma^a (1/sqrt|g|) d_mu (sqrt|g| e_a^mu)."""
    gim = metric.inv()
    Gm = [[[sp.simplify(sum(gim[l, m] * (sp.diff(metric[m, i], x[j]) + sp.diff(metric[m, j], x[i])
                                         - sp.diff(metric[i, j], x[m])) for m in range(N)) / 2)
            for j in range(N)] for i in range(N)] for l in range(N)]
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
    # sqrt|g| = |det e| = prod E_a (every E_a > 0 on the patch 0 < z < pi/2); det g > 0 (signature (4,4))
    sq = sp.Mul(*E)
    assert sp.simplify(sq ** 2 - metric.det()) == 0
    divf = sum((gam[a] * sp.simplify(sp.diff(sq * e_up[a, a], x[a]) / sq) / 2 for a in range(N)), ZERO16)
    return total.applyfunc(sp.simplify), divf.applyfunc(sp.simplify)


E = vielbein(-1)
check('vielbein_reproduces_metric', all(sp.simplify(eta[a, a] * E[a] ** 2 - g[a, a]) == 0 for a in range(N)),
      'g_mu nu = e^a_mu e^b_nu eta_ab for the diagonal vielbein')
total, divf = gamma_omega(g, E)
check('gamma_Omega_equals_3H_gamma8', (total - 3 * H * gam[7]).applyfunc(sp.simplify) == sp.zeros(16, 16),
      'gamma^mu Omega_mu = 3 H gamma^(x8) exactly; no a4 or a4\' survives (inflating and deflating terms cancel)')
check('gamma_Omega_divergence_formula', (total - divf).applyfunc(sp.simplify) == sp.zeros(16, 16),
      'gamma^mu Omega_mu = (1/2) gamma^a (1/sqrt|g|) d_mu (sqrt|g| e_a^mu) for the diagonal vielbein, computed independently '
      '(sqrt|g| = cos z is x4-independent; (1/cos z) d_x8 (cos z tan z) = 6 H)')
# negative control: extra times INFLATING like 3-space -> the x4 terms no longer cancel
g_nc = sp.diag(*([sp.exp(2 * a4) * s6] * 3 + [-1] + [-sp.exp(2 * a4) * s6] * 3 + [sp.cot(z) ** 2]))
E_nc = vielbein(+1)
total_nc, divf_nc = gamma_omega(g_nc, E_nc)
rest = (total_nc - 3 * H * gam[7]).applyfunc(sp.simplify)
coef = sp.simplify((rest * gam[3]).trace() / (gam[3] * gam[3]).trace())  # coefficient of gamma^(x4)
check('negative_control_inflating_extra_times',
      all(sp.simplify(eta[a, a] * E_nc[a] ** 2 - g_nc[a, a]) == 0 for a in range(N))
      and (total_nc - divf_nc).applyfunc(sp.simplify) == ZERO16
      and (rest - coef * gam[3]).applyfunc(sp.simplify) == ZERO16
      and sp.simplify(coef / sp.diff(a4, x[3])) in (3, -3),
      'with INFLATING extra times (g_tt = -e^{2 a4} sin^{1/3} z) gamma^mu Omega_mu = 3 H gamma^(x8) + ('
      + sp.sstr(coef) + ') gamma^(x4): an a4\' term survives, so the cancellation in the author\'s metric is due to the deflation')

report = {
    'producer': 'Revision/lead_checks/emt_divergence_and_spin_connection.py (lead, independent; no Revision code imported)',
    'summary': {'passed': sum(c['verdict'] == 'PASS' for c in checks), 'total': len(checks)},
    'checks': checks,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(report, f, indent=1, sort_keys=False)
    f.write('\n')
print(json.dumps(report['summary']))
raise SystemExit(0 if report['summary']['passed'] == report['summary']['total'] else 1)
