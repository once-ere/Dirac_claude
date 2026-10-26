#!/usr/bin/env python3
"""um4_gammas.py - the author's eight real 16 x 16 Dirac matrices of 4+4.nb, transcribed cell by cell.

Every function below transcribes one input cell of the author's notebook `universe_model_3/author_inputs/4+4.nb` (the cell label and
its text are quoted).  The transcription is checked against the notebook's own stored outputs by
`um4_dirac_matrices.py`; every other UM-4 computation imports its matrices from here, so that UM-4 uses exactly one
set of Dirac matrices.  Indices are counted from 0 as in the notebook: T16A[A1] for A1 = 0..7 (the frame directions of
the author's coordinates x0..x7) and T16A[8] = T16A[0].T16A[1]...T16A[7].
"""
from __future__ import annotations

import sympy as sp

I4 = sp.eye(4)
I8 = sp.eye(8)
I16 = sp.eye(16)
Z4 = sp.zeros(4, 4)
Z8 = sp.zeros(8, 8)


def block(rows):
    """ArrayFlatten of a 2 x 2 block matrix; a 0 entry is a zero block of the right size."""
    n = max(m.shape[0] for r in rows for m in r if not (isinstance(m, int) and m == 0))
    rr = [[(sp.zeros(n, n) if (isinstance(m, int) and m == 0) else m) for m in r] for r in rows]
    return sp.Matrix(sp.BlockMatrix(rr).as_explicit())


def signature(seq):
    """Signature[{...}] of Mathematica: the sign of the permutation, 0 if an element repeats."""
    seq = list(seq)
    if len(set(seq)) != len(seq):
        return 0
    s = 1
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def eta4488():
    """In[9]:  (eta4488 = ArrayFlatten[{{IdentityMatrix[4], 0}, {0, -IdentityMatrix[4]}}]) // MatrixForm"""
    return block([[I4, 0], [0, -I4]])


def sigma88():
    """In[18]: sigma = sigma88 = ArrayFlatten[{{ConstantArray[0,{4,4}], IdentityMatrix[4]},
                                              {IdentityMatrix[4], ConstantArray[0,{4,4}]}}]"""
    return block([[Z4, I4], [I4, Z4]])


def s4by4_t4by4():
    """In[29]: Qa[h_,p_,q_] := Signature[{h,p,q,4}];
               Qb[h_,p_,q_] := ID4[[p,4]]*ID4[[q,h]] - ID4[[p,h]]*ID4[[q,4]];
               SelfDualAntiSymmetric[h_,p_,q_] := Qa[h,p,q] - Qb[h,p,q];
               AntiSelfDualAntiSymmetric[h_,p_,q_] := (Qa[h,p,q] + Qb[h,p,q]);
       In[35]: Do[s4by4[h] = Table[Table[SelfDualAntiSymmetric[h,p,q], {q, 4}], {p, 4}], {h, 1, 3}]
       In[36]: Do[t4by4[h] = Table[Table[AntiSelfDualAntiSymmetric[h,p,q], {q, 4}], {p, 4}], {h, 1, 3}]
    (indices h, p, q run from 1 as in Mathematica; Table[Table[f, {q,4}], {p,4}] has row p and column q)."""
    def kd(i, j):
        return 1 if i == j else 0

    def Qa(h, p, q):
        return signature([h, p, q, 4])

    def Qb(h, p, q):
        return kd(p, 4) * kd(q, h) - kd(p, h) * kd(q, 4)

    s4 = {h: sp.Matrix(4, 4, lambda r, c: Qa(h, r + 1, c + 1) - Qb(h, r + 1, c + 1)) for h in (1, 2, 3)}
    t4 = {h: sp.Matrix(4, 4, lambda r, c: Qa(h, r + 1, c + 1) + Qb(h, r + 1, c + 1)) for h in (1, 2, 3)}
    return s4, t4


def zeta():
    """In[60]: zeta[0] = ID8;
               Table[zeta[7-h] = ArrayFlatten[{{0, t4by4[h]}, {-t4by4[h], 0}}], {h, 1, 3}];
               Table[zeta[h] = ArrayFlatten[{{0, s4by4[h]}, {s4by4[h], 0}}], {h, 1, 3}];
               (zeta[7] = zeta[1].zeta[2].zeta[3].zeta[4].zeta[5].zeta[6]) // MatrixForm"""
    s4, t4 = s4by4_t4by4()
    z = {0: I8}
    for h in (1, 2, 3):
        z[7 - h] = block([[Z4, t4[h]], [-t4[h], Z4]])
    for h in (1, 2, 3):
        z[h] = block([[Z4, s4[h]], [s4[h], Z4]])
    z[7] = z[1] * z[2] * z[3] * z[4] * z[5] * z[6]
    return z


def tau():
    """In[70]: tau[0] = ID8;  Do[{tau[A] = FullSimplify[ExpandAll[(zeta[A])]]}, {A, 1, 7}]
    (the commented-out alternative of the same cell is not evaluated)."""
    z = zeta()
    return {A: z[A] for A in range(8)}


def taubar():
    """In[74]: taubar[0] = ID8;  Do[{taubar[A] = FullSimplify[ExpandAll[(sigma.Transpose[tau[A]].sigma)]]}, {A, 1, 7}]"""
    t = tau()
    s = sigma88()
    tb = {0: I8}
    for A in range(1, 8):
        tb[A] = s * t[A].T * s
    return tb


def T16A():
    """In[97]: Table[T16^A[A1] = ArrayFlatten[{{0, taubar[A1]}, {tau[A1], 0}}], {A1, 0, 7}];
       In[98]: (T16^A[8] = T16^A[0].T16^A[1].T16^A[2].T16^A[3].T16^A[4].T16^A[5].T16^A[6].T16^A[7]) // MatrixForm
    Returns the dict {0..8: Matrix}."""
    t = tau()
    tb = taubar()
    T = {A1: block([[Z8, tb[A1]], [t[A1], Z8]]) for A1 in range(8)}
    P = sp.eye(16)
    for A1 in range(8):
        P = P * T[A1]
    T[8] = P
    return T


def sigma16():
    """In[96]: (sigma16 = T16^A[0].T16^A[1].T16^A[2].T16^A[3]) // MatrixForm
    (evaluated before In[97] in the notebook, so sigma16 holds the unevaluated product, which takes the value below as
    soon as T16^A is defined; In[105] checks sigma16 == ArrayFlatten[{{-sigma, 0}, {0, sigma}}])."""
    T = T16A()
    return T[0] * T[1] * T[2] * T[3]


def projectors():
    """In[111]: (P_L = 1/2 (ID16 - T16^A[8])) // MatrixForm;   In[112]: (P_R = 1/2 (ID16 + T16^A[8])) // MatrixForm"""
    T = T16A()
    PL = (I16 - T[8]) / 2
    PR = (I16 + T[8]) / 2
    return PL, PR


def SAB():
    """The scaled commutators S^AB = (1/4)[T16^A[A], T16^A[B]] (A, B = 0..7), the spin(4,4) generators."""
    T = T16A()
    return {(A, B): (T[A] * T[B] - T[B] * T[A]) / 4 for A in range(8) for B in range(8)}


def as_int_lists(M):
    return [[int(M[r, c]) for c in range(M.shape[1])] for r in range(M.shape[0])]


if __name__ == '__main__':
    T = T16A()
    for A in range(9):
        print('T16^A[%d] =' % A)
        for r in as_int_lists(T[A]):
            print(' '.join('%2d' % x for x in r))
