#!/usr/bin/env python3
"""Lead's independent checks: the MATRIX charge-conjugation operators of the theory and the U(1) charge.

Written from scratch; imports no other Revision code (reads only the fixture Revision/algebra/gammas.json).
Conventions of the Revision record (Revision/theory/field-theory.json, keys Lagrangian and current):
Psibar = Psi^dagger C with C = gamma^(x8) gamma^(x1) gamma^(x2) gamma^(x3) (the author's sigma16), S = Psibar Psi,
J^mu = -i Psibar gamma^mu Psi, J^x4 = Psi^dagger B Psi, B = -i C gamma^(x4), field equation
(gamma^mu D_mu - V) Psi = 0 with V = m + U'(S) real.

Why a MATRIX is needed: the author's gammas are REAL, so for a REAL field (Psi* = Psi) plain complex conjugation
is the identity and cannot be charge conjugation.  Charge conjugation is defined by a matrix calC acting as
    Psi^c = calC Psibar^T = calC C Psi*        (C^T = C)
and must map every solution of (gamma^mu D_mu - V) Psi = 0 to a solution of (gamma^mu D_mu - s V) Psi^c = 0,
s = +1 (same mass) or s = -1 (mass reversed).  Writing M = calC C, this requires M (gamma^a)* M^-1 = s gamma^a for
every a (the spinor connection is built from products of two gammas, so it then follows automatically).

Checks:
 1. reality of the representation: gamma^a, C real; B purely imaginary Hermitian; S^ab and Omega_mu real.
 2. ALL solutions M of M (gamma^a)* = s gamma^a M, a = x1..x8, solved exactly as linear equations
    (256 unknowns): s = +1 gives the 1-dimensional space spanned by the identity, s = -1 the 1-dimensional
    space spanned by Gamma = gamma^(x8) gamma^(x1) ... gamma^(x7).
 3. the two charge-conjugation matrices calC_+ = M C^-1 = C and calC_- = Gamma C, with
    calC_+^-1 gamma^a calC_+ = -(gamma^a)^T and calC_-^-1 gamma^a calC_- = +(gamma^a)^T (the two matrices C_+-
    every even dimension has), both real, calC_+ symmetric, and the Majorana consistency conditions
    (M M* = 1) for both: a REAL field can be imposed with either.
 4. action on the bilinears, as exact matrix identities for commuting (eps = +1) and Grassmann (eps = -1)
    components: under Psi -> M Psi*, S and J^a transform with the effective matrices eps (M^dagger K M)^T, K = the
    matrix of the bilinear: calC_+ keeps m and S and reverses J for commuting components (J^c = -J), while for
    Grassmann components S^c = -S and J^c = +J classically (normal ordering in the quantum theory supplies one more
    sign for each, giving the standard S^c = S, J^c = -J); calC_- reverses the mass term (s = -1).
 5. REAL fields: for real commuting components J^a = 0 identically (C gamma^a is antisymmetric) and calC_+ acts
    as the identity (a real field is its own charge conjugate: no U(1) charge); the nontrivial REAL matrix map is
    Psi -> Gamma Psi (= calC_- C Psi for real Psi), which maps (m, lambda) to (-m, -lambda) and reverses J and the
    kinetic term (theorem T1 of the Revision record): for real fields the matter <-> antimatter map is the matrix
    Gamma together with m -> -m.
 6. U(1) charge conservation in the author's metric (general a4(x4), real V): the field-level identity
    d_mu(cos z J^mu) = -i cos z (Psi^dagger C E - E^dagger C Psi), E = (gamma^mu D_mu - V) Psi, reduces exactly
    (derivation in the detail string) to the 16 x 16 matrix identity
    sum_mu d_mu(cos z C gamma^mu) = cos z sum_mu (C gamma^mu Omega_mu - Omega_mu^T (gamma^mu)^T C),
    verified exactly; on shell Q = Int cos z Psi^dagger B Psi d^7x is conserved.

Usage (from the repository root):  python Revision/lead_checks/charge_conjugation_and_u1.py
Output (deterministic, LF): Revision/lead_checks/reports/charge-conjugation-and-u1.json
"""
import json
import os
from fractions import Fraction

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
I16 = sp.eye(16)
assert all(gam[a] * gam[b] + gam[b] * gam[a] == 2 * eta[a, b] * I16 for a in range(N) for b in range(N))
C = gam[7] * gam[0] * gam[1] * gam[2]           # the author's sigma16
B = -sp.I * C * gam[3]
Gam = gam[7] * gam[0] * gam[1] * gam[2] * gam[3] * gam[4] * gam[5] * gam[6]
S = [[(gam[a] * gam[b] - gam[b] * gam[a]) / 4 for b in range(N)] for a in range(N)]
real = lambda M: all(sp.im(e) == 0 for e in M)

# ---- 1. reality ----
check('representation_real', all(real(g) for g in gam) and real(C) and C == C.T and C * C == I16
      and all(real(S[a][b]) for a in range(N) for b in range(N)),
      'gamma^a, C (= sigma16, symmetric, C^2 = 1) and S^ab are real: plain complex conjugation is the identity on a real field')
check('B_imaginary_hermitian', all(sp.re(e) == 0 for e in B) and B == B.H and B * B == I16,
      'B = -i C gamma^(x4) is purely imaginary and Hermitian, B^2 = 1')


# ---- 2. all intertwiners M (gamma^a)* = s gamma^a M, exact Gaussian elimination over Q ----
def nullspace_rational(rows, ncols):
    """Exact reduced row echelon form over Q; returns a basis of the null space as lists of Fractions."""
    piv_rows, pivots = [], []
    for r in rows:
        r = [Fraction(v) for v in r]
        for pr, pc in zip(piv_rows, pivots):
            if r[pc] != 0:
                fct = r[pc]
                r = [ri - fct * pi for ri, pi in zip(r, pr)]
        lead = next((j for j, v in enumerate(r) if v != 0), None)
        if lead is None:
            continue
        inv = 1 / r[lead]
        r = [v * inv for v in r]
        for k, pr in enumerate(piv_rows):  # keep fully reduced
            if pr[lead] != 0:
                fct = pr[lead]
                piv_rows[k] = [a - fct * b for a, b in zip(pr, r)]
        piv_rows.append(r)
        pivots.append(lead)
    free = [j for j in range(ncols) if j not in pivots]
    basis = []
    for fcol in free:
        vec = [Fraction(0)] * ncols
        vec[fcol] = Fraction(1)
        for pr, pc in zip(piv_rows, pivots):
            vec[pc] = -pr[fcol]
        basis.append(vec)
    return basis


def intertwiners(s):
    # unknown M (16 x 16 real or complex; the equations are real because the gammas are real, so solve over Q)
    rows = []
    for a in range(N):
        G = gam[a]
        for i in range(16):
            for j in range(16):
                # (M G - s G M)_ij = sum_k M_ik G_kj - s sum_k G_ik M_kj
                row = [0] * 256
                for k in range(16):
                    row[i * 16 + k] += int(G[k, j])
                    row[k * 16 + j] -= s * int(G[i, k])
                if any(row):
                    rows.append(row)
    return [sp.Matrix(16, 16, [sp.Rational(v.numerator, v.denominator) for v in b]) for b in nullspace_rational(rows, 256)]


Mp, Mm = intertwiners(+1), intertwiners(-1)
prop = lambda X, Y: X != sp.zeros(16, 16) and Y != sp.zeros(16, 16) and sp.Matrix.hstack(X.reshape(256, 1), Y.reshape(256, 1)).rank() == 1
check('intertwiners_same_mass', len(Mp) == 1 and prop(Mp[0], I16),
      f'M (gamma^a)* = + gamma^a M for all a: solution space of dimension {len(Mp)}, spanned by the identity '
      '(Pin(4,4) irreducible): Psi -> Psi* (times a phase) is the only same-mass conjugation in the Psi* form')
check('intertwiners_reversed_mass', len(Mm) == 1 and prop(Mm[0], Gam),
      f'M (gamma^a)* = - gamma^a M for all a: solution space of dimension {len(Mm)}, spanned by Gamma = '
      'gamma^(x8) gamma^(x1) ... gamma^(x7): the mass-reversing conjugation Psi -> Gamma Psi*')

# ---- 3. the two charge-conjugation matrices ----
Cp = C.inv()          # calC_+ = M C^-1 with M = 1  -> equals C
Cm = Gam * C.inv()    # calC_- = Gamma C^-1
check('charge_conjugation_matrix_plus', Cp == C and all(Cp.inv() * gam[a] * Cp == -gam[a].T for a in range(N))
      and real(Cp) and Cp == Cp.T,
      'calC_+ = C (= sigma16): calC_+^-1 gamma^a calC_+ = -(gamma^a)^T for every a; real symmetric; Psi^c = calC_+ Psibar^T = Psi*')
check('charge_conjugation_matrix_minus', all(Cm.inv() * gam[a] * Cm == gam[a].T for a in range(N)) and real(Cm),
      'calC_- = Gamma C: calC_-^-1 gamma^a calC_- = +(gamma^a)^T for every a; real; Psi^c = calC_- Psibar^T = Gamma Psi* '
      '(solves the equation with V -> -V)')
check('majorana_conditions_consistent', (I16 * I16.conjugate()) == I16 and (Gam * Gam.conjugate()) == I16,
      'M M* = 1 for M = 1 and M = Gamma: the reality conditions Psi = Psi* (calC_+) and Psi = Gamma Psi* (calC_-) are both consistent')

# ---- 4. bilinears under Psi -> M Psi*, exact matrix identities ----
K_S = C
K_J = [-sp.I * C * gam[a] for a in range(N)]
eff = lambda M, K, eps: eps * (M.H * K * M).T   # Psi*_A K_AB Psi_B for Psi -> M Psi*, reordered with sign eps
res = {}
for nameM, M in (('plus', I16), ('minus', Gam)):
    for eps in (1, -1):
        sS = 1 if eff(M, K_S, eps) == K_S else (-1 if eff(M, K_S, eps) == -K_S else 0)
        sJ = [1 if eff(M, K, eps) == K else (-1 if eff(M, K, eps) == -K else 0) for K in K_J]
        res[(nameM, eps)] = (sS, sJ)
ok4 = (res[('plus', 1)] == (1, [-1] * 8) and res[('plus', -1)] == (-1, [1] * 8)
       and res[('minus', 1)] == (1, [1] * 8) and res[('minus', -1)] == (-1, [-1] * 8))
check('bilinears_under_charge_conjugation', ok4,
      'S -> sS S, J^a -> sJ J^a under Psi -> M Psi*: calC_+ commuting (S, J) -> (S, -J); calC_+ Grassmann (S, J) -> (-S, +J) '
      'classically (in the quantum theory normal ordering supplies one more sign for each bilinear, giving the standard (S, J) -> (S, -J)); calC_- commuting (S, J) -> (S, +J); '
      'calC_- Grassmann (S, J) -> (-S, -J); measured: ' + json.dumps({f'{k[0]},eps={k[1]}': v for k, v in res.items()}))

# ---- 5. real fields ----
ok5 = all((C * gam[a]).T == -(C * gam[a]) for a in range(N))
x_real = sp.Matrix(sp.symbols('r1:17', real=True))
Jreal = [sp.expand((-sp.I * x_real.T * C * gam[a] * x_real)[0, 0]) for a in range(N)]
ok5 = ok5 and all(j == 0 for j in Jreal)
Sg = sp.expand(((Gam * x_real).T * C * (Gam * x_real))[0, 0] - (x_real.T * C * x_real)[0, 0])
kin = [sp.expand((Gam.T * C * gam[a] * Gam) + C * gam[a]) for a in range(N)]
ok5 = ok5 and Sg == 0 and all(k == sp.zeros(16, 16) for k in kin) and real(Gam)
check('real_fields_charge_conjugation', ok5,
      'real commuting Psi: J^a = -i Psi^T C gamma^a Psi = 0 identically and calC_+ acts as the identity (a real field is its own '
      'conjugate, no U(1) charge); the REAL matrix Gamma maps real fields to real fields, keeps S = Psi^T C Psi and reverses every '
      'kinetic matrix C gamma^a (Gamma^T C gamma^a Gamma = -C gamma^a): with m -> -m (and lambda -> -lambda) it maps solutions to '
      'solutions (T1) - for real fields the matter <-> antimatter map is the matrix Gamma with the mass reversed')

# ---- 6. U(1): exact matrix identity equivalent to the Noether identity ----
x = sp.symbols('x1:9', real=True)
H = sp.symbols('H', positive=True)
a4 = sp.Function('a4', real=True)(x[3])
z = 6 * H * x[7]
E = [sp.exp(a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.Integer(1)] + \
    [sp.exp(-a4) * sp.sin(z) ** sp.Rational(1, 6)] * 3 + [sp.cot(z)]
g = sp.diag(*[eta[a, a] * E[a] ** 2 for a in range(N)])
gi = g.inv()
Gm = [[[sp.simplify(sum(gi[l, m] * (sp.diff(g[m, i], x[j]) + sp.diff(g[m, j], x[i]) - sp.diff(g[i, j], x[m]))
                        for m in range(N)) / 2) for j in range(N)] for i in range(N)] for l in range(N)]
e_up = [1 / v for v in E]
Omega = []
for mu in range(N):
    om = sp.zeros(N, N)
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
check('spinor_connection_real', all(not e.has(sp.I) for Om in Omega for e in Om) and any(Om != sp.zeros(16, 16) for Om in Omega),
      'every entry of Omega_mu = (1/2) omega_mu,ab S^ab is a real expression on the patch 0 < z < pi/2 (built from real gammas, '
      'exp(+-a4), sin z > 0, cot z; no imaginary unit): gamma^mu D_mu is a REAL operator')
sqg = sp.cos(z)
gup = [gam[mu] * e_up[mu] for mu in range(N)]
lhs = sum((sp.diff(sqg * e_up[mu], x[mu]) * C * gam[mu] for mu in range(N)), sp.zeros(16, 16))
rhs = sum((sqg * (C * gup[mu] * Omega[mu] - Omega[mu].T * gup[mu].T * C) for mu in range(N)), sp.zeros(16, 16))
check('u1_noether_matrix_identity', (lhs - rhs).applyfunc(sp.simplify) == sp.zeros(16, 16),
      'd_mu(cos z J^mu) = Psi^dagger [d_mu(cos z K^mu)] Psi + cos z [(d Psi)^dagger K^mu Psi + Psi^dagger K^mu d Psi], K^mu = -i C gamma^mu; '
      '-i cos z (Psi^dagger C E - E^dagger C Psi) gives the same derivative terms (i (gamma^mu)^T C = -i C gamma^mu, gamma and Omega real), '
      'the V terms cancel (V real), and the remaining terms agree iff sum_mu d_mu(cos z C gamma^mu) = cos z sum_mu (C gamma^mu Omega_mu '
      '- Omega_mu^T (gamma^mu)^T C): verified exactly for general a4(x4); on shell the charge Q = Int cos z Psi^dagger B Psi d^7x is conserved')

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
