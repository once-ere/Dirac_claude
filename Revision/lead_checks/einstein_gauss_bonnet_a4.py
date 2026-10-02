#!/usr/bin/env python3
"""Lead's independent check of the a4 field equations (Revision/field_equations_a4/a4-equations.json).

Written from scratch; imports no Revision code.  For the author's metric (SPEC section 1):

1. The Einstein tensor G^mu_nu with a general a4(x4), from this file's own Christoffel symbols and the MTW
   Riemann tensor, compared component by component with the record's Einstein equations
   (constraint_x4, space_x1, extraTime_x5, hidden_x8, evolution, nullEnergy) for the source
   T^mu_nu = diag(p3, p3, p3, -rho, p_t, p_t, p_t, p8) and G^mu_nu + Lambda delta^mu_nu = kappa T^mu_nu;
   x8-independence of G; vanishing of every off-diagonal component.
2. noVacuum: T = 0 has no solution for H > 0, for any Lambda and any a4.
3. The Gauss-Bonnet (Lanczos) tensor from the CLASSICAL formula
     H_mu nu = 2 (R R_mu nu - 2 R_mu a R^a_nu - 2 R_mu a nu b R^ab + R_mu^abc R_nu abc)
               - (1/2) g_mu nu (R^2 - 4 R_ab R^ab + R_abcd R^abcd)
   (independent of the GKD route) for the linear member a4 = A H x4, compared with the alpha_2 terms of the
   record's linearMember.rho and linearMember.p (E_(2) = H by the Lovelock normalisation of the record).

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
x = sp.symbols('x1:9', real=True)
H, A, Lam, kappa = sp.symbols('H A Lam kappa', real=True)
rho, p3, pt, p8 = sp.symbols('rho p3 pt p8', real=True)
ad1, ad2 = sp.symbols('ad1 ad2', real=True)
alpha1, alpha2, alpha3 = sp.symbols('alpha1 alpha2 alpha3', real=True)
z = 6 * H * x[7]
checks = []


def check(name, ok, detail):
    checks.append({'name': name, 'verdict': 'PASS' if ok else 'FAIL', 'detail': detail})


def metric(a4):
    s6 = sp.sin(z) ** sp.Rational(1, 3)
    return sp.diag(*([sp.exp(2 * a4) * s6] * 3 + [-1] + [-sp.exp(-2 * a4) * s6] * 3 + [sp.cot(z) ** 2]))


def curvature(g):
    gi = g.inv()
    Gm = [[[sp.simplify(sum(gi[l, m] * (sp.diff(g[m, i], x[j]) + sp.diff(g[m, j], x[i]) - sp.diff(g[i, j], x[m]))
                            for m in range(N)) / 2) for j in range(N)] for i in range(N)] for l in range(N)]
    # MTW: R^a_bcd = d_c Gamma^a_bd - d_d Gamma^a_bc + Gamma^a_ce Gamma^e_bd - Gamma^a_de Gamma^e_bc
    Rie = {}
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(c + 1, N):
                    v = sp.simplify(sp.diff(Gm[a][b][d], x[c]) - sp.diff(Gm[a][b][c], x[d])
                                    + sum(Gm[a][c][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][c] for e in range(N)))
                    if v != 0:
                        Rie[(a, b, c, d)] = v
                        Rie[(a, b, d, c)] = -v
    Ric = sp.zeros(N, N)  # R_bd = R^a_bad
    for (a, b, c, d), v in Rie.items():
        if a == c:
            Ric[b, d] += v
    Ric = Ric.applyfunc(sp.simplify)
    return gi, Rie, Ric


def to_symbols(expr, a4):
    return sp.simplify(expr.subs(sp.Derivative(a4, (x[3], 2)), ad2).subs(sp.Derivative(a4, x[3]), ad1))


rec = json.load(open(REC, encoding='utf-8'))
P = lambda s: sp.parse_expr(s.replace('^', '**'), local_dict={'ad1': ad1, 'ad2': ad2, 'H': H, 'Lam': Lam, 'kappa': kappa, 'rho': rho,
                                           'p3': p3, 'pt': pt, 'p8': p8, 'AA': A, 'alpha1': alpha1,
                                           'alpha2': alpha2, 'alpha3': alpha3})


def eq(rec_entry):
    lhs, rhs = rec_entry['input'].split('==')
    return P(lhs) - P(rhs)


# ---- 1. Einstein tensor with a general a4 ----
a4 = sp.Function('a4')(x[3])
g = metric(a4)
gi, Rie, Ric = curvature(g)
Rs = sp.simplify(sum(gi[i, i] * Ric[i, i] for i in range(N)))
Gmix = (gi * Ric - Rs / 2 * sp.eye(N)).applyfunc(sp.simplify)  # G^mu_nu
Gs = Gmix.applyfunc(lambda e: to_symbols(e, a4))
check('einstein_x8_independent', all(sp.diff(Gs[i, j], x[7]) == 0 for i in range(N) for j in range(N)),
      'every component of G^mu_nu is independent of x8 (z)')
check('einstein_off_diagonal_zero', all(Gs[i, j] == 0 for i in range(N) for j in range(N) if i != j),
      'G^mu_nu is diagonal (in particular G^x4_x8 = G^x8_x4 = 0)')
check('einstein_isotropy', Gs[0, 0] == Gs[1, 1] == Gs[2, 2] and Gs[4, 4] == Gs[5, 5] == Gs[6, 6],
      'G^x1_x1 = G^x2_x2 = G^x3_x3 and G^x5_x5 = G^x6_x6 = G^x7_x7')
T = {3: -rho, 0: p3, 4: pt, 7: p8}
mine = {k: Gs[k, k] + Lam - kappa * v for k, v in T.items()}  # = 0 are the field equations
E = rec['einstein']
for key, k in (('constraint_x4', 3), ('space_x1', 0), ('extraTime_x5', 4), ('hidden_x8', 7)):
    r = eq(E[key])
    ratio = sp.simplify(mine[k] / r)
    check('einstein_' + key, ratio in (1, -1),
          f"G^{k + 1}_{k + 1} + Lambda = kappa T: mine = {sp.sstr(mine[k])}; record: {E[key]['input']}; ratio {ratio}")
check('einstein_evolution', sp.simplify((mine[0] - mine[4]) - (-eq(E['evolution']))) == 0
      or sp.simplify((mine[0] - mine[4]) - eq(E['evolution'])) == 0,
      'space minus extra-time component: ' + sp.sstr(sp.simplify(mine[0] - mine[4])) + ' = 0; record ' + E['evolution']['input'])
null_mine = sp.solve(mine[3], rho)[0] + sp.solve(mine[7], p8)[0]
null_rec = sp.solve(eq(E['nullEnergy']), p8)[0] + rho
check('einstein_null_energy', sp.simplify(kappa * null_mine - kappa * null_rec) == 0,
      'kappa (rho + p8) = ' + sp.sstr(sp.simplify(kappa * null_mine)) + ' (< 0 for H > 0): the null energy condition fails along x8')

# ---- 2. no vacuum ----
vac = [Gs[k, k] + Lam for k in (0, 3, 4, 7)]
sol = sp.solve(vac, [Lam, ad1, ad2], dict=True)
check('no_vacuum_for_H_positive',
      sp.simplify(vac[1] + vac[3] - (Gs[3, 3] + Gs[7, 7] + 2 * Lam)) == 0
      and sp.simplify((Gs[3, 3] - Gs[7, 7]) - (6 * ad1 ** 2 + 6 * H ** 2)) == 0
      and all(any(sp.simplify(v.subs(H, 1)).has(sp.I) for v in s.values()) for s in sol),
      'G^x4_x4 - G^x8_x8 = 6 a4\'^2 + 6 H^2 > 0 for H > 0, so T = 0 (G + Lambda = 0) is impossible for every Lambda; '
      'solutions of the vacuum system: ' + sp.sstr(sol))

# ---- 3. Gauss-Bonnet tensor for the linear member ----
a4l = A * H * x[3]
gl = metric(a4l)
gil, Riel, Ricl = curvature(gl)
Rl = sp.simplify(sum(gil[i, i] * Ricl[i, i] for i in range(N)))
diag_g = [gl[i, i] for i in range(N)]
inv_g = [gil[i, i] for i in range(N)]
# all-lower Riemann R_abcd = g_aa R^a_bcd (diagonal metric)
Rlow = {k: sp.simplify(diag_g[k[0]] * v) for k, v in Riel.items()}
RicUp = [inv_g[i] * inv_g[i] * Ricl[i, i] for i in range(N)]  # R^ii (Ricci is diagonal here)
assert all(Ricl[i, j] == 0 for i in range(N) for j in range(N) if i != j)
Kret = sp.simplify(sum(v * v * inv_g[a] * inv_g[b] * inv_g[c] * inv_g[d] for (a, b, c, d), v in Rlow.items()))
RicSq = sp.simplify(sum(Ricl[i, i] * RicUp[i] for i in range(N)))
GBscalar = sp.simplify(Rl ** 2 - 4 * RicSq + Kret)
Hmix = []
for m in range(N):
    # H_mm (lower), then H^m_m = g^mm H_mm
    t1 = Rl * Ricl[m, m]
    t2 = Ricl[m, m] * inv_g[m] * Ricl[m, m]
    t3 = sum(Rlow.get((m, a, m, b), 0) * (RicUp[a] if a == b else 0) for a in range(N) for b in range(N))
    t4 = sum(Rlow.get((m, a, b, c), 0) * Rlow.get((m, a, b, c), 0) * inv_g[a] * inv_g[b] * inv_g[c]
             for a in range(N) for b in range(N) for c in range(N))
    Hmm = 2 * (t1 - 2 * t2 - 2 * t3 + t4) - diag_g[m] * GBscalar / 2
    Hmix.append(sp.simplify(inv_g[m] * Hmm))
check('gauss_bonnet_constant', all(not Hm.has(x[3]) and not Hm.has(x[7]) for Hm in Hmix),
      'for a4 = A H x4 the Gauss-Bonnet tensor H^mu_nu is constant: ' + sp.sstr([Hmix[i] for i in (0, 3, 4, 7)]))
check('gauss_bonnet_isotropic_pressure', sp.simplify(Hmix[0] - Hmix[4]) == 0 and sp.simplify(Hmix[0] - Hmix[7]) == 0,
      'H^x1_x1 = H^x5_x5 = H^x8_x8 for the linear member (so p3 = p_t = p8 = p)')
L = rec['linearMember']
rho_rec, p_rec = P(L['rho']['input']), P(L['p']['input'])
# alpha2 part of the record: coefficient of alpha2 in kappa*rho and kappa*p
a2_rho = sp.simplify(sp.diff(kappa * rho_rec, alpha2))
a2_p = sp.simplify(sp.diff(kappa * p_rec, alpha2))
# field equations: alpha2 H^4_4 = kappa T^4_4 = -kappa rho -> kappa rho = -alpha2 H^4_4; kappa p = alpha2 H^1_1
check('gauss_bonnet_rho_alpha2', sp.simplify(a2_rho - (-Hmix[3])) == 0,
      'alpha_2 part of kappa rho: record ' + sp.sstr(a2_rho) + ', classical Gauss-Bonnet -H^x4_x4 = ' + sp.sstr(sp.simplify(-Hmix[3])))
check('gauss_bonnet_p_alpha2', sp.simplify(a2_p - Hmix[0]) == 0,
      'alpha_2 part of kappa p: record ' + sp.sstr(a2_p) + ', classical Gauss-Bonnet H^x1_x1 = ' + sp.sstr(sp.simplify(Hmix[0])))
a1_rho = sp.simplify(sp.diff(kappa * rho_rec, alpha1))
Gl = [sp.simplify(sum(gil[m, k] * Ricl[k, m] for k in range(N)) - Rl / 2) for m in range(N)]
check('einstein_linear_rho_alpha1', sp.simplify(a1_rho - (-Gl[3])) == 0,
      'alpha_1 part of kappa rho: record ' + sp.sstr(a1_rho) + ', -G^x4_x4 = ' + sp.sstr(sp.simplify(-Gl[3])))

report = {
    'producer': 'Revision/lead_checks/einstein_gauss_bonnet_a4.py (lead, independent; no Revision code imported; '
                'reads the record Revision/field_equations_a4/a4-equations.json to compare)',
    'summary': {'passed': sum(c['verdict'] == 'PASS' for c in checks), 'total': len(checks)},
    'checks': checks,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(report, f, indent=1)
    f.write('\n')
print(json.dumps(report['summary']))
for c in checks:
    print(c['verdict'], c['name'])
raise SystemExit(0 if report['summary']['passed'] == report['summary']['total'] else 1)
