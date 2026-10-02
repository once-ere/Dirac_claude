#!/usr/bin/env python3
"""Lead's independent checks for the matter-antimatter chapter (Revision/lead_checks).

Written from scratch; imports no other Revision code (reads only the fixture Revision/algebra/gammas.json).
Conventions of the Revision record (Revision/theory/field-theory.json, keys Lagrangian and current):
Psibar = Psi^dagger C, S = Psibar Psi, J^mu = -i Psibar gamma^mu Psi, J^x4 = Psi^dagger B Psi,
B = -i C gamma^(x4), field equation (gamma^mu D_mu - V) Psi = 0 with V = m + U'(S) real.

Checks (commuting components, i.e. dirac16complex00, and the classical bilinears of dirac16complex):
 1. reality: every gamma^a and C are real; B is purely imaginary and Hermitian; S^ab and the spinor
    connection Omega_mu of the author's metric are real.
 2. charge conjugation by complex conjugation: for random exact complex spinors, S(Psi*) = S(Psi) (and S
    is real), J^mu(Psi*) = -J^mu(Psi) for every mu, J^mu is real; since gamma^mu D_mu is a REAL operator
    and V is real, Psi* solves the same equation with the same m and lambda: an exact C symmetry of the
    theory that reverses the charge.
 3. the chirality map of T1: S(Gamma Psi) = S(Psi), J^mu(Gamma Psi) = -J^mu(Psi).
 4. the U(1) Noether identity in the author's metric with general a4(x4) and a general real V(x):
    d_mu(cos z J^mu) = -i cos z (Psi^dagger C E - E^dagger C Psi), E = (gamma^mu D_mu - V) Psi, for 16
    generic complex component functions of x1..x8: the charge Q = Int cos z J^x4 d^7x is conserved on
    shell (exact U(1) charge conservation: no net charge can be created inside one universe).

Usage (from the repository root):  python Revision/lead_checks/charge_conjugation_and_u1.py
Output (deterministic, LF): Revision/lead_checks/reports/charge-conjugation-and-u1.json
"""
import json
import os
import random

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, 'reports', 'charge-conjugation-and-u1.json')
N = 8
checks = []


def check(name, ok, detail):
    checks.append({'name': name, 'verdict': 'PASS' if ok else 'FAIL', 'detail': detail})


with open(os.path.join(ROOT, 'Revision', 'algebra', 'gammas.json'), encoding='utf-8') as f:
    fx = json.load(f)
gam = [sp.Matrix(m) for m in fx['gamma']]  # gamma^a, a = x1..x8
eta = sp.diag(1, 1, 1, -1, -1, -1, -1, 1)
assert all(gam[a] * gam[b] + gam[b] * gam[a] == 2 * eta[a, b] * sp.eye(16) for a in range(N) for b in range(N))
C = gam[7] * gam[0] * gam[1] * gam[2]           # C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3)
B = -sp.I * C * gam[3]                           # B = -i C gamma^(x4)
G5 = gam[7] * gam[0] * gam[1] * gam[2] * gam[3] * gam[4] * gam[5] * gam[6]  # Gamma
S = [[(gam[a] * gam[b] - gam[b] * gam[a]) / 4 for b in range(N)] for a in range(N)]

# ---- 1. reality ----
real = lambda M: all(sp.im(e) == 0 for e in M)
check('gammas_and_C_real', all(real(g) for g in gam) and real(C) and C == C.T and C * C == sp.eye(16),
      'every gamma^a is real; C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) is real symmetric with C^2 = 1')
check('B_imaginary_hermitian', all(sp.re(e) == 0 for e in B) and B == B.H and B * B == sp.eye(16),
      'B = -i C gamma^(x4) is purely imaginary and Hermitian with B^2 = 1, hence B^T = -B')
check('Sab_real', all(real(S[a][b]) for a in range(N) for b in range(N)), 'S^ab = (1/4)[gamma^a, gamma^b] are real')

x = sp.symbols('x1:9', real=True)
H = sp.symbols('H', positive=True)
a4 = sp.Function('a4', real=True)(x[3])
z = 6 * H * x[7]
E = [sp.exp(a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + \
    [sp.exp(-a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.cot(z)]           # e^a_mu = E_a delta^a_mu
g = sp.diag(*[eta[a, a] * E[a] ** 2 for a in range(N)])
gi = g.inv()
Gm = [[[sp.simplify(sum(gi[l, m] * (sp.diff(g[m, i], x[j]) + sp.diff(g[m, j], x[i]) - sp.diff(g[i, j], x[m]))
                        for m in range(N)) / 2) for j in range(N)] for i in range(N)] for l in range(N)]
e_up = [1 / v for v in E]  # e_a^mu (diagonal)
Omega = []
for mu in range(N):
    om = sp.zeros(N, N)  # omega_mu^a_b = e^a_nu (d_mu e_b^nu + Gamma^nu_mu_lambda e_b^lambda)
    for a in range(N):
        for b in range(N):
            om[a, b] = sp.simplify(E[a] * (sp.diff(e_up[b] if a == b else 0, x[mu]) + Gm[a][mu][b] * e_up[b]))
    om_ab = eta * om
    Om = sp.zeros(16, 16)
    for a in range(N):
        for b in range(N):
            if om_ab[a, b] != 0:
                Om += om_ab[a, b] * S[a][b] / 2
    Omega.append(Om.applyfunc(sp.simplify))
check('spinor_connection_real', all(all(sp.simplify(sp.im(e)) == 0 for e in Om) for Om in Omega),
      'Omega_mu = (1/2) omega_mu,ab S^ab is real for every mu (real vielbein, real S^ab): gamma^mu D_mu is a real operator')

# ---- 2. and 3. bilinears under conjugation and chirality, random exact spinors ----
rng = random.Random(20261002)
def rand_spinor():
    return sp.Matrix([sp.Rational(rng.randint(-9, 9), rng.randint(1, 5)) + sp.I * sp.Rational(rng.randint(-9, 9), rng.randint(1, 5))
                      for _ in range(16)])
Sbil = lambda P: sp.expand((P.H * C * P)[0, 0])
Jbil = lambda P, a: sp.expand((-sp.I * P.H * C * gam[a] * P)[0, 0])
ok_c = ok_g = ok_real = True
for trial in range(25):
    P = rand_spinor()
    Pc = P.conjugate()
    ok_c &= sp.simplify(Sbil(Pc) - Sbil(P)) == 0 and sp.im(Sbil(P)) == 0
    ok_c &= all(sp.simplify(Jbil(Pc, a) + Jbil(P, a)) == 0 for a in range(N))
    ok_real &= all(sp.im(Jbil(P, a)) == 0 for a in range(N))
    ok_c &= sp.simplify((P.H * B * P)[0, 0] - Jbil(P, 3)) == 0     # J^x4 = Psi^dagger B Psi
    Pg = G5 * P
    ok_g &= sp.simplify(Sbil(Pg) - Sbil(P)) == 0 and all(sp.simplify(Jbil(Pg, a) + Jbil(P, a)) == 0 for a in range(N))
check('charge_conjugation_reverses_current', ok_c,
      '25 random exact spinors: S(Psi*) = S(Psi) real, J^a(Psi*) = -J^a(Psi) for a = x1..x8, J^x4 = Psi^dagger B Psi')
check('current_real', ok_real, 'J^a = -i Psi^dagger (C gamma^a) Psi is real (C gamma^a real antisymmetric)')
check('chirality_map_reverses_current', ok_g, 'S(Gamma Psi) = S(Psi), J^a(Gamma Psi) = -J^a(Psi) (T1)')
check('C_gamma_real_antisymmetric', all(real(C * gam[a]) and (C * gam[a]).T == -(C * gam[a]) for a in range(N)),
      'C gamma^a is real antisymmetric for every a (the reason J is real and odd under conjugation)')

# ---- 4. U(1) Noether identity with generic components ----
u = [sp.Function(f'u{A}', real=True)(*x) for A in range(16)]
v = [sp.Function(f'v{A}', real=True)(*x) for A in range(16)]
V = sp.Function('V', real=True)(*x)
Psi = sp.Matrix([u[A] + sp.I * v[A] for A in range(16)])
PsiH = sp.Matrix([[u[A] - sp.I * v[A] for A in range(16)]])
gup = [gam[a] * e_up[a] for a in range(N)]  # gamma^mu = e_a^mu gamma^a (diagonal vielbein)
Eres = sp.zeros(16, 1)
for mu in range(N):
    Eres += gup[mu] * (Psi.diff(x[mu]) + Omega[mu] * Psi)
Eres -= V * Psi
EresH = Eres.H
sqg = sp.cos(z)
lhs = sum(sp.diff(sqg * (-sp.I * (PsiH * C * gup[mu] * Psi)[0, 0]), x[mu]) for mu in range(N))
rhs = -sp.I * sqg * ((PsiH * C * Eres)[0, 0] - (EresH * C * Psi)[0, 0])
diff = sp.simplify(sp.expand(lhs - rhs))
check('u1_noether_identity', diff == 0,
      'd_mu(cos z J^mu) = -i cos z (Psi^dagger C E - E^dagger C Psi) with E = (gamma^mu D_mu - V) Psi, for 16 generic complex '
      'components of x1..x8, general a4(x4) and real V(x): on shell d_mu(cos z J^mu) = 0, so Q = Int cos z Psi^dagger B Psi d^7x '
      'is conserved')

report = {
    'producer': 'Revision/lead_checks/charge_conjugation_and_u1.py (lead, independent; no Revision code imported)',
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
