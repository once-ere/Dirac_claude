#!/usr/bin/env python3
"""UM-2 algebra: the author's gamma matrices of Cl(4,4), rebuilt from the author's formulas.

Rebuilds the real 16x16 matrices T16[A] (A = 0..7, the author's coordinates x0..x7) from
the formulas of the author's notebooks (Dirac_Einstein-Lovelock_4+4_Nash.nb and
WaveFunctionUniverse-4+4-Einstein-Lovelock.nb):

  Qa[h,p,q] = Signature[{h,p,q,4}],  Qb[h,p,q] = d(p,4) d(q,h) - d(p,h) d(q,4)
  s4by4[h] = Qa - Qb (self-dual),     t4by4[h] = Qa + Qb (anti-self-dual), p,q = 1..4
  zeta[0] = I8, zeta[7-h] = {{0, t4by4[h]}, {-t4by4[h], 0}}, zeta[h] = {{0, s4by4[h]}, {s4by4[h], 0}}
  zeta[7] = zeta[1]...zeta[6],  sigma = {{0, I4}, {I4, 0}}
  tau[0] = I8, tau[A] = zeta[A],  taubar[A] = sigma . tau[A]^T . sigma
  T16[A] = {{0, taubar[A]}, {tau[A], 0}},  sigma16 = {{-sigma, 0}, {0, sigma}}

and verifies exactly: the Clifford relations, C = sigma16 = g0 g1 g2 g3, the chirality, B,
irreducibility under Pin(4,4), the splitting into two inequivalent 8-dim irreps of Spin(4,4),
and the 2x2 block basis used by the Kohn-Sham reduction (the commuting set J = g0 g1 g4,
K1 = g2 g3, K2 = g5 g6), including the forms of every matrix the reduction needs.
Writes outputs/algebra.json and reports/algebra-checks.json.
"""
import itertools
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, ROOT, Report, read_json, write_json  # noqa: E402

I = sp.I


def kd(a, b):
    return 1 if a == b else 0


def author_gammas():
    Qa = lambda h, p, q: sp.LeviCivita(h, p, q, 4)
    Qb = lambda h, p, q: kd(p, 4) * kd(q, h) - kd(p, h) * kd(q, 4)
    s4 = {h: sp.Matrix(4, 4, lambda p, q: Qa(h, p + 1, q + 1) - Qb(h, p + 1, q + 1)) for h in (1, 2, 3)}
    t4 = {h: sp.Matrix(4, 4, lambda p, q: Qa(h, p + 1, q + 1) + Qb(h, p + 1, q + 1)) for h in (1, 2, 3)}
    Z4 = sp.zeros(4, 4)
    I4 = sp.eye(4)
    I8 = sp.eye(8)
    zeta = {0: I8}
    for h in (1, 2, 3):
        zeta[7 - h] = sp.BlockMatrix([[Z4, t4[h]], [-t4[h], Z4]]).as_explicit()
    for h in (1, 2, 3):
        zeta[h] = sp.BlockMatrix([[Z4, s4[h]], [s4[h], Z4]]).as_explicit()
    zeta[7] = zeta[1] * zeta[2] * zeta[3] * zeta[4] * zeta[5] * zeta[6]
    sigma = sp.BlockMatrix([[Z4, I4], [I4, Z4]]).as_explicit()
    tau = {0: I8}
    for A in range(1, 8):
        tau[A] = zeta[A]
    taubar = {A: sigma * tau[A].T * sigma for A in range(8)}
    Z8 = sp.zeros(8, 8)
    T16 = [sp.BlockMatrix([[Z8, taubar[A]], [tau[A], Z8]]).as_explicit() for A in range(8)]
    sigma16 = sp.BlockMatrix([[-sigma, Z8], [Z8, sigma]]).as_explicit()
    return T16, sigma16, tau, taubar, sigma, s4, t4


def commutant_dim(mats, n):
    """Dimension of {X : X M = M X for all M in mats} over C."""
    xs = sp.symbols('x0:%d' % (n * n))
    X = sp.Matrix(n, n, xs)
    eqs = []
    for M in mats:
        eqs.extend(list(X * M - M * X))
    A, _ = sp.linear_eq_to_matrix(eqs, xs)
    return n * n - A.rank()


def intertwiner_dim(mats_a, mats_b, n):
    """Dimension of {X (n x n) : X A_i = B_i X}."""
    xs = sp.symbols('y0:%d' % (n * n))
    X = sp.Matrix(n, n, xs)
    eqs = []
    for Ma, Mb in zip(mats_a, mats_b):
        eqs.extend(list(X * Ma - Mb * X))
    A, _ = sp.linear_eq_to_matrix(eqs, xs)
    return n * n - A.rank()


def main():
    rep = Report('algebra-checks', 'UM-2: the author\'s Cl(4,4) gamma matrices rebuilt from the author\'s formulas; '
                 'Clifford relations, C, chirality, B, Pin(4,4)/Spin(4,4) representation content, Kohn-Sham block basis')
    T16, sigma16, tau, taubar, sigma, s4, t4 = author_gammas()
    eta = [1, 1, 1, 1, -1, -1, -1, -1]
    I16 = sp.eye(16)
    I8 = sp.eye(8)

    # tau relations of the notebook: (1/2)(tau[A] taubar[B] + tau[B] taubar[A]) = eta_AB I8
    ok = all(sp.simplify((tau[A] * taubar[B] + tau[B] * taubar[A]) / 2 - kd(A, B) * eta[A] * I8) == sp.zeros(8, 8)
             for A in range(8) for B in range(8))
    rep.check('tau_relations_of_the_notebook', ok, '(1/2)(tau[A].taubar[B] + tau[B].taubar[A]) = eta_AB I8 for A, B = 0..7')
    ok = (sigma == tau[1] * tau[2] * tau[3]) and (sigma == tau[4] * tau[5] * tau[6] * tau[7]) \
        and (tau[1] * tau[2] * tau[3] * tau[4] * tau[5] * tau[6] * tau[7] == I8)
    rep.check('notebook_identities_sigma', ok, 'sigma = tau1 tau2 tau3 = tau4 tau5 tau6 tau7, tau1...tau7 = I8 (notebook Out[323], Out[324], Out[322])')

    # Clifford
    ok = all(T16[a] * T16[b] + T16[b] * T16[a] == 2 * kd(a, b) * eta[a] * I16 for a in range(8) for b in range(8))
    rep.check('clifford_relations', ok, '{gamma^a, gamma^b} = 2 eta^ab I16, eta = diag(+,+,+,+,-,-,-,-) in the order x0..x7')
    real = all(all(e.is_real for e in T16[a]) for a in range(8))
    rep.check('gammas_real', real, 'every gamma^a is a real 16x16 matrix')

    # comparison with the record's matrices (Revision/algebra/gammas.json)
    rec = read_json(os.path.join(ROOT, 'Revision', 'algebra', 'gammas.json'))
    same = all(sp.Matrix(rec['gamma'][a]) == T16[a] for a in range(8))
    rep.check('identical_to_record_gammas', same, 'the rebuilt T16[a] equal Revision/algebra/gammas.json gamma[a] entry by entry')

    C = T16[0] * T16[1] * T16[2] * T16[3]
    rep.check('C_is_sigma16', C == sigma16, 'C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3) = sigma16 = {{-sigma,0},{0,sigma}}')
    rep.check('C_real_symmetric_involution', C == C.T and C * C == I16, 'C^T = C, C^2 = I16')
    ok = all((C * T16[a]).T == -(C * T16[a]) for a in range(8))
    rep.check('C_gamma_antisymmetric', ok, '(C gamma^a)^T = -C gamma^a for every a (the author\'s sigma16.T16[a] antisymmetric)')
    Gam = T16[0]
    for a in range(1, 8):
        Gam = Gam * T16[a]
    rep.check('chirality_diag', Gam == sp.diag(*([-1] * 8 + [1] * 8)), 'Gamma = gamma^(x0)...gamma^(x7) = diag(-I8, I8)')
    B = -I * C * T16[4]
    rep.check('B_hermitian_involution', B == B.H and B * B == I16, 'B = -i C gamma^(x4): B^dagger = B, B^2 = 1')
    evB = B.eigenvals()
    rep.check('B_signature_8_8', evB == {1: 8, -1: 8}, 'eigenvalues of B: +1 (8 times), -1 (8 times): the Krein metric is indefinite')
    ok = all((B * T16[4] * T16[a]).H == B * T16[4] * T16[a] for a in range(8) if a != 4)
    rep.check('B_gamma4_gamma_a_hermitian', ok, 'B gamma^(x4) gamma^a is Hermitian for a != 4 (Hermitian Dirac Hamiltonian in the Krein metric)')

    S = [[(T16[a] * T16[b] - T16[b] * T16[a]) / 4 for b in range(8)] for a in range(8)]
    # Pin(4,4): commutant of the gammas
    dpin = commutant_dim(T16, 16)
    rep.check('pin44_irreducible', dpin == 1, 'commutant of {gamma^a} has complex dimension %d: the 16-dim representation of Pin(4,4) is irreducible' % dpin)
    gens = [S[a][b] for a in range(8) for b in range(a + 1, 8)]
    dspin = commutant_dim(gens, 16)
    rep.check('spin44_commutant_dim_2', dspin == 2, 'commutant of {S^ab} has dimension %d (= span{I, Gamma})' % dspin)
    Pm = [S[a][b][:8, :8] for a in range(8) for b in range(a + 1, 8)]
    Pp = [S[a][b][8:, 8:] for a in range(8) for b in range(a + 1, 8)]
    blockdiag = all(S[a][b][:8, 8:] == sp.zeros(8, 8) and S[a][b][8:, :8] == sp.zeros(8, 8) for a in range(8) for b in range(8))
    rep.check('spin44_preserves_chiral_halves', blockdiag, 'every S^ab is block diagonal in the Gamma = -1, +1 halves')
    dm = commutant_dim(Pm, 8)
    dp = commutant_dim(Pp, 8)
    rep.check('chiral_halves_irreducible', dm == 1 and dp == 1, 'commutants of Spin(4,4) on the two 8-dim halves: %d, %d' % (dm, dp))
    dint = intertwiner_dim(Pm, Pp, 8)
    rep.check('chiral_halves_inequivalent', dint == 0, 'intertwiners from the Gamma = -1 half to the Gamma = +1 half: dimension %d' % dint)

    # Kohn-Sham block basis (commuting set J = g0 g1 g4, K1 = g2 g3, K2 = g5 g6)
    J = T16[0] * T16[1] * T16[4]
    K1 = T16[2] * T16[3]
    K2 = T16[5] * T16[6]
    rep.check('commuting_set', J * J == I16 and K1 * K1 == -I16 and K2 * K2 == -I16 and J * K1 == K1 * J
              and J * K2 == K2 * J and K1 * K2 == K2 * K1, 'J^2 = 1, K1^2 = K2^2 = -1, mutually commuting')
    ks = read_json(os.path.join(ROOT, 'Revision', 'kohn_sham', 'ks-theory.json'))
    cols = ks['blockBasis']['unnormalisedColumns2Sqrt2V']
    V = sp.Matrix(16, 16, lambda r, c: sp.sympify(cols[r][c])) / (2 * sp.sqrt(2))
    rep.check('block_basis_unitary', sp.simplify(V.H * V - I16) == sp.zeros(16, 16), 'V^dagger V = I16 for the record\'s block basis')
    labels = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]
    s1 = sp.Matrix([[0, 1], [1, 0]])
    s2 = sp.Matrix([[0, -I], [I, 0]])
    s3 = sp.Matrix([[1, 0], [0, -1]])
    e2 = sp.eye(2)

    def blk(f):
        return sp.diag(*[f(j, a, b) for (j, a, b) in labels])
    targets = {
        'gamma^(x0) = sigma3': (T16[0], blk(lambda j, a, b: s3)),
        'gamma^(x0)gamma^(x1) = -i sigma2': (T16[0] * T16[1], blk(lambda j, a, b: -I * s2)),
        'gamma^(x0)gamma^(x4) = j sigma1': (T16[0] * T16[4], blk(lambda j, a, b: j * s1)),
        'B = j s2 (number)': (B, blk(lambda j, a, b: j * a * e2)),
        'C = s2 sigma2': (C, blk(lambda j, a, b: a * s2)),
        'J = j': (J, blk(lambda j, a, b: j * e2)),
        'K1 = i s2': (K1, blk(lambda j, a, b: I * a * e2)),
        'K2 = i s3': (K2, blk(lambda j, a, b: I * b * e2)),
        'gamma^(x4)gamma^(x1) = -j sigma3': (T16[4] * T16[1], blk(lambda j, a, b: -j * s3)),
        'B gamma^(x0) = j s2 sigma3': (B * T16[0], blk(lambda j, a, b: j * a * s3)),
    }
    for name, (M, target) in targets.items():
        ok = sp.simplify(V.H * M * V - target) == sp.zeros(16, 16)
        rep.check('block_form ' + name, ok, 'V^dagger M V in the 8 blocks (j, s2, s3)')

    # the 4D chirality and internal chirality (needed for the zero-mode count of the SM fermions)
    G4 = T16[1] * T16[2] * T16[3] * T16[4]
    Gint = T16[0] * T16[5] * T16[6] * T16[7]
    rep.check('product_of_4D_and_internal_chirality', G4 * Gint == -Gam or G4 * Gint == Gam,
              'Gamma = (g1 g2 g3 g4)(g0 g5 g6 g7) up to sign: sign %s' % ('+' if G4 * Gint == Gam else '-'))
    rep.check('chirality_squares', G4 * G4 == -I16 and Gint * Gint == -I16,
              '(g1 g2 g3 g4)^2 = -1 and (g0 g5 g6 g7)^2 = -1, so Gamma4 = i g1 g2 g3 g4 and Gamma_int = i g0 g5 g6 g7 are involutions')

    out = {
        'description': 'the author\'s gamma matrices gamma^(x_a) = T16[a] (a = 0..7), C, Gamma, B; integers',
        'gamma': [[[int(e) for e in T16[a].row(r)] for r in range(16)] for a in range(8)],
        'C': [[int(e) for e in C.row(r)] for r in range(16)],
        'Gamma': [[int(e) for e in Gam.row(r)] for r in range(16)],
        'eta': eta,
        'tau': {str(A): [[int(e) for e in tau[A].row(r)] for r in range(8)] for A in range(8)},
        'sigma': [[int(e) for e in sigma.row(r)] for r in range(8)],
        's4by4': {str(h): [[int(e) for e in s4[h].row(r)] for r in range(4)] for h in (1, 2, 3)},
        't4by4': {str(h): [[int(e) for e in t4[h].row(r)] for r in range(4)] for h in (1, 2, 3)},
    }
    write_json(os.path.join(OUT, 'algebra.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
