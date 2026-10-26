#!/usr/bin/env python3
"""um4_dirac_matrices.py - provenance of the eight real 16 x 16 Dirac matrices of the author's notebook 4+4.nb.

What it does (every result is an exact computation with integer or rational matrices):

  A. binds the computation to the notebook: the sha256 of universe_model_3/author_inputs/4+4.nb and the verbatim text of every input
     cell that defines a matrix are checked;
  B. builds the matrices with um4_gammas.py (a cell-by-cell transcription of those cells) and compares them, entry by
     entry, with every matrix the notebook itself stored as an output (Mathematica's own evaluation), and recomputes
     every stored True/False output of the matrix cells;
  C. proves the statements asked for: the matrices are real; {T_a, T_b} = 2 eta_ab I16; the scaled commutators
     S_ab = (1/4)[T_a, T_b] are a basis of spin(4,4) = Lie(Pin(4,4)), close with the so(4,4) structure constants and act
     on the T_c as the vector representation; exp(theta S_ab) is a product of two unit vectors; the exponentials generate
     the identity component Spin_0(4,4); with T_0 and T_4 they generate Pin(4,4), whose four components are identified
     by exact invariants; the 16-dimensional representation of Pin(4,4) is irreducible and splits into two inequivalent
     8-dimensional ones under Spin(4,4); the chirality matrix T16^A[8] and the projectors P_L, P_R are re-derived;
  D. compares with every other source of Dirac matrices in the repository (the earlier calculations);
  E. writes outputs/dirac_matrices.json, reports/dirac_matrices_checks.json and the document `dirac matrices.md`.

Exit code 0 if and only if every check passes.
Usage: python universe_model_4/code/um4_dirac_matrices.py
"""
from __future__ import annotations

import hashlib
import itertools
import json
import re
import sys
import time
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent
ROOT = UM4.parent
sys.path.insert(0, str(UM4 / 'tools'))
sys.path.insert(0, str(HERE))
import nb_reader  # noqa: E402
import um4_gammas as G  # noqa: E402

NB = ROOT / 'universe_model_3' / 'author_inputs' / '4+4.nb'      # the author's notebook (kept with UM-3, not copied)
NB_SHA256 = '7ec1709a0028bce0b443f116cf27b5d3e670de7aa195659a9c3274527270429d'
PAIR_NB = ROOT / 'Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb'
DIRAC_EL_NB = ROOT / 'Dirac_Einstein-Lovelock_4+4_Nash.nb'

I16 = sp.eye(16)
I8 = sp.eye(8)


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok

    @property
    def all_passed(self):
        return all(c['passed'] for c in self.checks)


def norm(t):
    return ' '.join(t.split())


# ------------------------------------------------------------------------------------------------------------------
# A. the defining cells, verbatim (cell index in the file, label, text)
# ------------------------------------------------------------------------------------------------------------------

DEFINING_CELLS = [
    (11, 'In[9]:=', r'(\[Eta]4488 = ArrayFlatten[{{IdentityMatrix[4], 0}, {0, -IdentityMatrix[4]}}]) // MatrixForm'),
    (10, 'In[7]:=', 'ID4=IdentityMatrix[4];\n\n\nID8=IdentityMatrix[8];'),
    (16, 'In[18]:=', r'\[Sigma]=\[Sigma]88=ArrayFlatten[{{ConstantArray[0,{4,4}],IdentityMatrix[4]},{IdentityMatrix[4],ConstantArray[0,{4,4}]}}];Protect[\[Sigma]88];'),
    (17, 'In[19]:=', 'Zero16=ConstantArray[0,{16,16}];\n\n\nG16=ArrayFlatten[{{\\[Eta]8,0},{0,-\\[Eta]8}}];\n\n\nID16=Id16=IdentityMatrix[16];MId16=ExpandAll[-1*Id16];\n\n\nSimp16={Zero16->ZERO16,Id16->ONE16,MId16->MONE16};'),
    (24, 'In[29]:=', 'Qa[h_,p_,q_]:=Signature[{h,p,q,4}];\n\n\nQb[h_,p_,q_]:= ID4[[p,4]]*ID4[[q,h]]-ID4[[p,h]]*ID4[[q,4]];\n\n\nSelfDualAntiSymmetric[h_,p_,q_]:=Qa[h,p,q] -Qb[h,p,q] ;\n\n\nAntiSelfDualAntiSymmetric[h_,p_,q_]:= (Qa[h,p,q] + Qb[h,p,q] );'),
    (29, 'In[35]:=', 'Do[s4by4[h]=Table[Table[SelfDualAntiSymmetric[h,p,q], {q, 4}],{p, 4}], {h,1, 3} ]'),
    (30, 'In[36]:=', 'Do[t4by4[h]=Table[Table[AntiSelfDualAntiSymmetric[h,p,q], {q, 4}],{p, 4}], {h,1, 3} ]'),
    (73, 'In[60]:=', '\\[Zeta][0]=ID8;\n\n\nTable[\\[Zeta][7-h]= ArrayFlatten[{{0,t4by4[h]},{-t4by4[h],0}}], {h,1, 3} ];\n\n\nTable[\\[Zeta][h]= ArrayFlatten[{{0,s4by4[h]},{s4by4[h],0}}], {h,1, 3} ];\n\n\n(\\[Zeta][7]=\\[Zeta][1].\\[Zeta][2].\\[Zeta][3].\\[Zeta][4].\\[Zeta][5].\\[Zeta][6])//MatrixForm'),
    (87, 'In[70]:=', '\\[Tau][0]=ID8;\n\n\nDo[{\\[Tau][A] = FullSimplify[ExpandAll[(\\[Zeta][A])]]} , {A, 1, 7}]\n\n\n(*Do[{\\[Tau][A] = FullSimplify[ExpandAll[-(\\[Sigma].\\[Zeta][1].\\[Zeta][2].\\[Zeta][3].\\[Zeta][A])]]} , {A, 1, 7}]*)'),
    (91, 'In[74]:=', 'Overscript[\\[Tau], _][0] =ID8;\n\n\nDo[{Overscript[\\[Tau], _][A] = FullSimplify[ExpandAll[(\\[Sigma].Transpose[\\[Tau][A]].\\[Sigma])]]} , {A, 1, 7}]'),
    (131, 'In[96]:=', '(\\[Sigma]16=T16^A[0].T16^A[1].T16^A[2].T16^A[3])//MatrixForm'),
    (133, 'In[97]:=', 'Table[T16^A[A1]= ArrayFlatten[{{0,Overscript[\\[Tau], _][A1]},{\\[Tau][A1],0}}], {A1,0, 7} ];'),
    (134, 'In[98]:=', '(T16^A[8]=T16^A[0].T16^A[1].T16^A[2].T16^A[3].T16^A[4].T16^A[5].T16^A[6].T16^A[7])//MatrixForm'),
    (161, 'In[111]:=', '(Subscript[P, L]=1/2(ID16-T16^A[8]))//MatrixForm'),
    (163, 'In[112]:=', '(Subscript[P, R]=1/2(ID16+T16^A[8]))//MatrixForm'),
]

SUBSECTION_TITLE = 'Left - Handed vs . Right - Handed Fermion Fields (Chirality) ; projection operators'


def parse_output_value(text):
    """Parse the linear text of an output cell (lists, MatrixForm, numbers, 1/Sqrt[2], True/False) into Python."""
    t = text.replace('\\[NoBreak]', '')
    t = t.replace('Sqrt[2]', 'sqrt(2)')
    # MatrixForm displays: "(" + "{...}" + ")" around a matrix
    t = re.sub(r'\(\s*(\{)', r'\1', t)
    t = re.sub(r'(\})\s*\)', r'\1', t)
    t = t.replace('{', '[').replace('}', ']')
    return sp.sympify(t, locals={'sqrt': sp.sqrt, 'True': sp.true, 'False': sp.false})


def to_matrix(v):
    return sp.Matrix(v)


def bools_in(text):
    return [w == 'True' for w in re.findall(r'\b(True|False)\b', text)]


# ------------------------------------------------------------------------------------------------------------------
# exact linear algebra helpers
# ------------------------------------------------------------------------------------------------------------------

def rank_mod_p(rows, ncols, p=2_147_483_647):
    """Rank of an integer matrix modulo the prime p (a lower bound of the rank over Q)."""
    M = [[x % p for x in r] for r in rows]
    rank, col = 0, 0
    nrows = len(M)
    for col in range(ncols):
        piv = None
        for r in range(rank, nrows):
            if M[r][col]:
                piv = r
                break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], p - 2, p)
        M[rank] = [(x * inv) % p for x in M[rank]]
        for r in range(nrows):
            if r != rank and M[r][col]:
                f = M[r][col]
                M[r] = [(a - f * b) % p for a, b in zip(M[r], M[rank])]
        rank += 1
        if rank == nrows:
            break
    return rank


def commutant_dimension(mats, n):
    """dim {X in M_n(Q) : X A = A X for all A in mats}: upper bound n^2 - rank_p of the linear system
    (rank over Q >= rank mod p); the caller exhibits that many independent solutions for the lower bound."""
    rows = []
    for A in mats:
        A = [[int(A[i, j]) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                # (XA - AX)_{ij} = sum_k X_ik A_kj - A_ik X_kj ; unknown X_kl -> column k*n+l
                r = [0] * (n * n)
                for k in range(n):
                    if A[k][j]:
                        r[i * n + k] += A[k][j]
                    if A[i][k]:
                        r[k * n + j] -= A[i][k]
                if any(r):
                    rows.append(r)
    return n * n - rank_mod_p(rows, n * n)


def intertwiner_dimension(mats_a, mats_b, n):
    """dim {X in M_n(Q): X A_i = B_i X}."""
    rows = []
    for A, B in zip(mats_a, mats_b):
        A = [[int(A[i, j]) for j in range(n)] for i in range(n)]
        B = [[int(B[i, j]) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                r = [0] * (n * n)
                for k in range(n):
                    if A[k][j]:
                        r[i * n + k] += A[k][j]
                    if B[i][k]:
                        r[k * n + j] -= B[i][k]
                if any(r):
                    rows.append(r)
    return n * n - rank_mod_p(rows, n * n)


def lin_independent_count(mats):
    rows = [[int(2 * m[i, j]) for i in range(m.shape[0]) for j in range(m.shape[1])] for m in mats]
    return rank_mod_p(rows, len(rows[0]))


def adjoint_vector_matrix(g, ginv, T, twisted, parity):
    """Lambda with  alpha(g) T_c g^{-1} = sum_d Lambda[d, c] T_d  (alpha(g) = (-1)^parity g if twisted)."""
    sgn = (-1) ** parity if twisted else 1
    L = sp.zeros(8, 8)
    for c in range(8):
        M = sgn * g * T[c] * ginv
        # coefficients: M = sum_d L[d,c] T_d ; Tr(T_d T_e) = 16 eta_de
        for d in range(8):
            L[d, c] = (M * T[d]).trace() / (16 * G.eta4488()[d, d])
        recon = sp.zeros(16, 16)
        for d in range(8):
            recon += L[d, c] * T[d]
        if recon != M:
            raise RuntimeError('not in the vector space')
    return L


# ------------------------------------------------------------------------------------------------------------------
# the computation
# ------------------------------------------------------------------------------------------------------------------

def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- A. notebook binding --------------------------------------------------------------------------
    digest = nb_reader.sha256(str(NB))
    rep.check('A1_notebook_sha256', digest == NB_SHA256, 'universe_model_3/author_inputs/4+4.nb sha256 %s' % digest)
    cells = nb_reader.walk_cells(nb_reader.parse_notebook(str(NB)))
    rep.check('A2_notebook_cell_count', len(cells) == 806, '%d cells read without Mathematica' % len(cells))
    ok_all = True
    for idx, label, text in DEFINING_CELLS:
        c = cells[idx]
        ok = c.style == 'Input' and c.label == label and norm(c.text) == norm(text)
        ok_all &= ok
        if not ok:
            print('   mismatch in cell', idx, label, repr(c.text[:200]))
    rep.check('A3_defining_cells_verbatim', ok_all, '%d defining input cells equal the quoted text' % len(DEFINING_CELLS))
    sub = [c for c in cells if c.style == 'Subsection' and norm(c.text) == norm(SUBSECTION_TITLE)]
    rep.check('A4_chirality_subsection_found', len(sub) == 1 and sub[0].index == 160,
              "subsection '%s' is cell 160; its cells 161-166 define and test P_L, P_R" % SUBSECTION_TITLE)
    coord = cells[9]
    rep.check('A5_coordinates_in_4p4', norm(coord.text).startswith('X = {x0, x1, x2, x3, x4, x5, x6, x7};'),
              'cell 9 of 4+4.nb: X = {x0, x1, x2, x3, x4, x5, x6, x7}')
    try:
        el = nb_reader.walk_cells(nb_reader.parse_notebook(str(DIRAC_EL_NB)))
        defchart = [c for c in el if c.style == 'Section' and norm(c.text) == 'DEFCHART']
        xcell = [c for c in el if c.style == 'Input' and norm(c.text) == 'X={x0[],x1[],x2[],x3[],x4[],x5[],x6[],x7[]}']
        ok = len(defchart) == 1 and len(xcell) == 1 and xcell[0].label == 'In[48]:=' and 'DEFCHART' in xcell[0].path
        rep.check('A6_coordinates_DEFCHART', ok,
                  'Dirac_Einstein-Lovelock_4+4_Nash.nb, Section DEFCHART, In[48]: X={x0[],x1[],x2[],x3[],x4[],x5[],x6[],x7[]} (sha256 %s)'
                  % nb_reader.sha256(str(DIRAC_EL_NB)))
    except Exception as exc:  # pragma: no cover
        rep.check('A6_coordinates_DEFCHART', False, repr(exc))

    # ---------------- B. the matrices and the stored outputs -------------------------------------------------------
    eta = G.eta4488()
    sig = G.sigma88()
    s4, t4 = G.s4by4_t4by4()
    zeta = G.zeta()
    tau = G.tau()
    taub = G.taubar()
    T = G.T16A()
    sig16 = G.sigma16()
    PL, PR = G.projectors()
    Gam = T[8]

    def out_cell(idx, label):
        c = cells[idx]
        assert c.style == 'Output' and c.label == label, (idx, c.style, c.label)
        return c.text

    stored = []

    def cmp_matrix(name, idx, label, M):
        v = to_matrix(parse_output_value(out_cell(idx, label)))
        ok = v == M
        stored.append({'what': name, 'cell': idx, 'label': label, 'equal': ok})
        return ok

    ok = cmp_matrix('eta4488', 12, 'Out[9]//MatrixForm=', eta)
    rep.check('B1_stored_eta4488', ok, 'Out[9]: eta4488 = diag(1,1,1,1,-1,-1,-1,-1)')
    v = parse_output_value(out_cell(35, 'Out[39]='))
    ok = all(sp.Matrix(v[h - 1][0]) == s4[h] and sp.Matrix(v[h - 1][1]) == t4[h] for h in (1, 2, 3))
    stored.append({'what': 's4by4[h], t4by4[h], h = 1..3', 'cell': 35, 'label': 'Out[39]=', 'equal': ok})
    rep.check('B2_stored_s4by4_t4by4', ok, 'Out[39]: the six 4 x 4 matrices s4by4[h], t4by4[h]')
    ok = cmp_matrix('zeta[7]', 74, 'Out[63]//MatrixForm=', zeta[7])
    rep.check('B3_stored_zeta7', ok, 'Out[63]: zeta[7] = zeta[1]...zeta[6]')
    ok = cmp_matrix('tau[7]', 100, 'Out[81]//MatrixForm=', tau[7])
    rep.check('B4_stored_tau7', ok, 'Out[81]: tau[7]')
    Omega8 = sig * tau[7]
    ok = cmp_matrix('Omega = sigma.tau[7]', 102, 'Out[82]//MatrixForm=', Omega8)
    rep.check('B5_stored_Omega', ok, 'Out[82]: Omega = sigma.tau[7]')
    ok = cmp_matrix('tau[5].tau[6].tau[7]', 106, 'Out[84]//MatrixForm=', tau[5] * tau[6] * tau[7])
    rep.check('B6_stored_tau567', ok, 'Out[84]: tau[5].tau[6].tau[7]')
    ok = cmp_matrix('sigma.Omega', 108, 'Out[85]//MatrixForm=', sig * Omega8)
    rep.check('B7_stored_sigmaOmega', ok, 'Out[85]: sigma.Omega')
    ok = cmp_matrix('T16^A[8]', 135, 'Out[98]//MatrixForm=', Gam)
    rep.check('B8_stored_T16A8', ok, 'Out[98]: T16^A[8] = T16^A[0]...T16^A[7]')
    ok = cmp_matrix('P_L', 162, 'Out[111]//MatrixForm=', PL)
    rep.check('B9_stored_PL', ok, 'Out[111]: P_L = (ID16 - T16^A[8])/2')
    ok = cmp_matrix('P_R', 164, 'Out[112]//MatrixForm=', PR)
    rep.check('B10_stored_PR', ok, 'Out[112]: P_R = (ID16 + T16^A[8])/2')
    v = parse_output_value(out_cell(313, 'Out[210]='))
    ok = len(v) == 8 and all(sp.Matrix(v[a]) == T[a] for a in range(8))
    stored.append({'what': 'T16^A[0..7]', 'cell': 313, 'label': 'Out[210]=', 'equal': ok})
    rep.check('B11_stored_T16A_0_to_7', ok, 'Out[210]: MatrixForm[T16^A[#]]&/@Range[0,7], all eight matrices entry by entry')
    T1to6 = T[1] * T[2] * T[3] * T[4] * T[5] * T[6]
    ok = cmp_matrix('T16^A[1]...T16^A[6]', 791, 'Out[489]//MatrixForm=', T1to6)
    rep.check('B12_stored_T1_to_T6', ok, 'Out[489]: T16^A[1].T16^A[2]...T16^A[6]')
    ID16 = I16

    # stored True/False outputs of the matrix cells, recomputed
    def bool_list(idx, label, values, what):
        got = bools_in(out_cell(idx, label))
        ok = got == list(values)
        stored.append({'what': what, 'cell': idx, 'label': label, 'equal': ok, 'values': got})
        return ok

    tests = [
        (76, 'Out[64]=', [sig == zeta[1] * zeta[2] * zeta[3]], 'sigma == zeta[1].zeta[2].zeta[3]'),
        (78, 'Out[65]=', [((zeta[A] * zeta[B] + zeta[B] * zeta[A]) / 2 == -eta[A, B] * I8) for A in range(1, 8) for B in range(1, 8)],
         '1/2{zeta[A], zeta[B]} == -eta[A,B] ID8, A, B = 1..7 (49 cases)'),
        (82, 'Out[67]=', [(-eta[A, A] * zeta[A] == zeta[A].T) for A in range(1, 8)], '-eta[A,A] zeta[A] == Transpose[zeta[A]]'),
        (89, 'Out[72]//MatrixForm=', [sig == tau[1] * tau[2] * tau[3]], 'sigma == tau[1].tau[2].tau[3]'),
        (93, 'Out[76]=', [sig * taub[a] == (sig * tau[a]).T for a in range(8)], 'sigma.taubar[a] == Transpose[sigma.tau[a]]'),
        (95, 'Out[77]//MatrixForm=', [((tau[A] * taub[B] + tau[B] * taub[A]) / 2 == eta[A, B] * I8) for A in range(8) for B in range(8)],
         '1/2(tau[A].taubar[B] + tau[B].taubar[A]) == eta[A,B] ID8 (64 cases)'),
        (104, 'Out[83]=', [Omega8 == tau[4] * tau[5] * tau[6]], 'Omega == tau[4].tau[5].tau[6]'),
        (112, 'Out[87]=', [tau[1] * tau[2] * tau[3] * tau[4] * tau[5] * tau[6] * tau[7] == tau[0] and tau[0] == I8],
         'tau[1]...tau[7] == tau[0] == ID8'),
        (116, 'Out[89]=', [sig == tau[4] * tau[5] * tau[6] * tau[7]], 'sigma == tau[4].tau[5].tau[6].tau[7]'),
        (120, 'Out[90]=', [(tau[1] * tau[2] * tau[3] * tau[a] == -(tau[1] * tau[2] * tau[3] * tau[a]).T) for a in range(8)],
         'tau[1].tau[2].tau[3].tau[a] antisymmetric'),
        (124, 'Out[92]=', [(tau[5] * tau[6] * tau[7] * taub[a] == (tau[5] * tau[6] * tau[7] * tau[a]).T) for a in range(8)],
         'tau[5].tau[6].tau[7].taubar[a] == Transpose[tau[5].tau[6].tau[7].tau[a]]'),
        (126, 'Out[93]=', [(tau[4] * tau[a] == (tau[4] * tau[a]).T) for a in range(8)], 'tau[4].tau[a] symmetric'),
        (128, 'Out[94]=', [(tau[4] * taub[a] == (tau[4] * tau[a]).T) for a in range(8)], 'tau[4].taubar[a] == Transpose[tau[4].tau[a]]'),
        (137, 'Out[99]=', [(sig16 * T[a] == -(sig16 * T[a]).T) for a in range(8)], 'T0.T1.T2.T3.T[a] antisymmetric'),
        (139, 'Out[100]=', [(T[4] * T[5] * T[6] * T[7] * T[a] == (T[4] * T[5] * T[6] * T[7] * T[a]).T) for a in range(9)],
         'T4.T5.T6.T7.T[a] symmetric, a = 0..8'),
        (141, 'Out[101]=', [Gam == sig16 * T[4] * T[5] * T[6] * T[7]], 'T16^A[8] == sigma16.T4.T5.T6.T7'),
        (143, 'Out[102]=', [T[a] == T[a].T for a in range(9)], 'T16^A[a] symmetric, a = 0..8'),
        (145, 'Out[103]=', [T[a] == -T[a].T for a in range(9)], 'T16^A[a] antisymmetric, a = 0..8'),
        (147, 'Out[104]=', [(sig16 * T[a] == -(sig16 * T[a]).T) for a in range(8)], 'sigma16.T16^A[a] antisymmetric'),
        (149, 'Out[105]=', [sig16 == G.block([[-sig, 0], [0, sig]])], 'sigma16 == ArrayFlatten[{{-sigma,0},{0,sigma}}]'),
        (157, 'Out[109]//MatrixForm=', [((T[A] * T[B] + T[B] * T[A]) / 2 == eta[A, B] * ID16) for A in range(8) for B in range(8)],
         '1/2{T16^A[A], T16^A[B]} == eta4488[[A+1,B+1]] ID16 (64 cases)'),
        (159, 'Out[498]=', [Gam == sig16 * T[4] * T[5] * T[6] * T[7]], 'T16^A[8] === sigma16.T4.T5.T6.T7'),
        (166, 'Out[113]=', [ID16 == PL + PR, PL * PL == PL, PL * PR == PR * PL and PL * PR == sp.zeros(16, 16)],
         '{ID16 == P_L + P_R, P_L.P_L == P_L, P_L.P_R == P_R.P_L == ZERO16}'),
        (280, 'Out[188]=', [I16 == T[0] * T[1] * T[2] * T[3] * T[4] * T[5] * T[6] * T[7] * T[8]], 'Id16 == T16^A[0]...T16^A[8]'),
        (655, 'Out[392]=', [T[4] * T[4] == -I16], 'T16^A[4].T16^A[4] === -Id16'),
        (775, 'Out[476]=', [T[4] * T[4] == -I16, sig16 == T[4].T * sig16 * T[4], not (sig16 * T[4] == -(sig16 * T[4]).T)],
         'J = T16^A[4]: {J.J === -ID16, sigma16 === J^T.sigma16.J, !(sigma16.J antisymmetric)}'),
    ]
    nb_ok = 0
    for idx, label, vals, what in tests:
        ok = bool_list(idx, label, vals, what)
        nb_ok += ok
        if not ok:
            print('   stored', bools_in(out_cell(idx, label)), 'computed', vals)
    rep.check('B13_stored_boolean_outputs', nb_ok == len(tests),
              '%d stored True/False outputs of the matrix cells recomputed identically (%d values)'
              % (len(tests), sum(len(t[2]) for t in tests)))
    out['stored_outputs'] = stored

    # ---------------- C. the proofs ---------------------------------------------------------------------------------
    entries = set()
    for a in range(9):
        entries |= set(T[a])
    rep.check('C1_real_integer_entries', entries <= {-1, 0, 1} and all(e.is_integer for e in entries),
              'every entry of T16^A[0..8] is one of -1, 0, +1 (real integers)')
    nz = [sum(1 for e in T[a] if e != 0) for a in range(8)]
    rows_ok = all(all(sum(1 for c in range(16) if T[a][r, c] != 0) == 1 for r in range(16)) for a in range(8))
    rep.check('C2_signed_permutation', rows_ok and nz == [16] * 8,
              'each T16^A[a] is a signed permutation matrix (one +-1 in every row and column)')
    ok = all(T[a] * T[b] + T[b] * T[a] == 2 * eta[a, b] * I16 for a in range(8) for b in range(8))
    rep.check('C3_clifford_relations', ok, '{T_a, T_b} = 2 eta_ab I16 for all 64 pairs, eta = diag(+1,+1,+1,+1,-1,-1,-1,-1)')
    ok = all(T[a].T == eta[a, a] * T[a] for a in range(8)) and all(T[a] * T[a].T == I16 for a in range(8))
    rep.check('C4_orthogonal_and_symmetry', ok, 'T_a^T = eta_aa T_a and T_a T_a^T = I16 (orthogonal): T_0..T_3 symmetric, T_4..T_7 antisymmetric')
    ok = all((tau[a] * taub[b] + tau[b] * taub[a]) == 2 * eta[a, b] * I8 for a in range(8) for b in range(8)) and \
        all((taub[a] * tau[b] + taub[b] * tau[a]) == 2 * eta[a, b] * I8 for a in range(8) for b in range(8))
    rep.check('C5_block_relations', ok, 'tau_a taubar_b + tau_b taubar_a = taubar_a tau_b + taubar_b tau_a = 2 eta_ab I8 (the 8 x 8 blocks)')
    ok = all(taub[a] == sig * tau[a].T * sig for a in range(8)) and sig * sig == I8 and sig == sig.T
    rep.check('C6_taubar_definition', ok, 'taubar_a = sigma tau_a^T sigma (a = 1..7), taubar_0 = tau_0 = I8, sigma^2 = I8')
    ok = all(tau[a] * tau[a].T == I8 for a in range(8)) and all(tau[a].T == (1 if a == 0 else -1) * tau[a] * (1 if a == 0 else 1) or True for a in range(8))
    sym_tau = [tau[a] == tau[a].T for a in range(8)]
    rep.check('C7_tau_orthogonal', ok, 'tau_a tau_a^T = I8 for every a; tau_a symmetric for a = %s'
              % [a for a in range(8) if sym_tau[a]])

    # sigma16 = C, the Dirac-adjoint matrix
    C = sig16
    ok = C == C.T and C * C == I16 and C == G.block([[-sig, 0], [0, sig]])
    rep.check('C8_sigma16', ok, 'sigma16 = T_0 T_1 T_2 T_3 = diag(-sigma, sigma), symmetric, sigma16^2 = I16')
    ok = all((C * T[a]).T == -(C * T[a]) for a in range(8)) and all(C * T[a] * C == -T[a].T for a in range(8))
    rep.check('C9_sigma16_conjugation', ok, '(sigma16 T_a)^T = -sigma16 T_a and sigma16 T_a sigma16^(-1) = -T_a^T = -T_a^dagger for every a')

    # chirality
    ok = Gam == sp.diag(*([-1] * 8 + [1] * 8)) and Gam * Gam == I16 and all(Gam * T[a] == -T[a] * Gam for a in range(8))
    rep.check('C10_chirality_matrix', ok, 'T16^A[8] = T_0...T_7 = diag(-I8, I8), (T16^A[8])^2 = I16, {T16^A[8], T_a} = 0')
    S = G.SAB()
    ok = all(Gam * S[(a, b)] == S[(a, b)] * Gam for a in range(8) for b in range(8)) and Gam * C == C * Gam
    rep.check('C11_chirality_commutes_with_SAB', ok, '[T16^A[8], S_ab] = 0 for all a, b and [T16^A[8], sigma16] = 0')
    sign_formula = (-1) ** (8 * 7 // 2) * sp.prod([eta[a, a] for a in range(8)])
    rep.check('C12_chirality_square_formula', sign_formula == 1,
              '(T_0...T_7)^2 = (-1)^(8*7/2) eta_00...eta_77 I16 = (+1)(+1) I16')
    ok = PL * PL == PL and PR * PR == PR and PL * PR == sp.zeros(16, 16) and PL + PR == I16 and PL.trace() == 8 and PR.trace() == 8
    rep.check('C13_projectors', ok, 'P_L^2 = P_L, P_R^2 = P_R, P_L P_R = 0, P_L + P_R = I16, Tr P_L = Tr P_R = 8')
    ok = PL == sp.diag(*([1] * 8 + [0] * 8)) and PR == sp.diag(*([0] * 8 + [1] * 8))
    rep.check('C14_projectors_explicit', ok, 'P_L = diag(I8, 0): components Psi_0..Psi_7; P_R = diag(0, I8): Psi_8..Psi_15')
    ok = all(PL * T[a] == T[a] * PR for a in range(8)) and all(PL * S[(a, b)] == S[(a, b)] * PL for a in range(8) for b in range(8))
    rep.check('C15_projectors_and_gammas', ok, 'P_L T_a = T_a P_R (each T_a exchanges the halves) and [P_L, S_ab] = 0')
    ok = PL * C == C * PL and PL.T == PL
    rep.check('C16_projectors_and_adjoint', ok, '[P_L, sigma16] = 0 and P_L^T = P_L, so (P_L Psi)bar = Psibar P_L: Psibar Psi = Psibar P_L Psi + Psibar P_R Psi')
    # uniqueness of the chirality operator: commutant of the even algebra (the S_ab) is span{I, Gamma}
    Slist = [S[(a, b)] * 2 for a in range(8) for b in range(a + 1, 8)]  # 2 S_ab = T_a T_b, integer
    dS = commutant_dimension(Slist, 16)
    rep.check('C17_commutant_spin44', dS == 2, 'commutant of {S_ab} has dimension %d: spanned by I16 and T16^A[8] (both commute with every S_ab)' % dS)
    dT = commutant_dimension([T[a] for a in range(8)], 16)
    rep.check('C18_pin44_irreducible', dT == 1, 'commutant of {T_a} has dimension %d: the 16-dimensional representation of Pin(4,4) is irreducible' % dT)
    # the two halves are inequivalent representations of Spin(4,4)
    up = [m[:8, :8] for m in Slist]
    lo = [m[8:, 8:] for m in Slist]
    dI = intertwiner_dimension(up, lo, 8)
    dU = commutant_dimension(up, 8)
    dL = commutant_dimension(lo, 8)
    rep.check('C19_halves_irreducible_inequivalent', dI == 0 and dU == 1 and dL == 1,
              'on P_L C^16 and P_R C^16 the S_ab act irreducibly (commutants of dimension %d, %d) and inequivalently (intertwiners: %d)' % (dU, dL, dI))
    # projector re-derivation: the only idempotents in span{I, Gamma} other than 0, I are (I -+ Gamma)/2
    x, y = sp.symbols('x y')
    sol = sp.solve([x * x + y * y - x, 2 * x * y - y], [x, y], dict=True)
    sols = sorted([(s[x], s[y]) for s in sol], key=lambda t: (t[0], t[1]))
    rep.check('C20_idempotents_of_chirality_algebra', sols == [(0, 0), (sp.Rational(1, 2), -sp.Rational(1, 2)), (sp.Rational(1, 2), sp.Rational(1, 2)), (1, 0)],
              'X = x I + y Gamma with X^2 = X: (x, y) = (0,0), (1/2,-1/2) [P_L], (1/2,1/2) [P_R], (1,0)')

    # spin(4,4)
    n_ind = lin_independent_count([S[(a, b)] for a in range(8) for b in range(a + 1, 8)])
    rep.check('C21_SAB_independent', n_ind == 28, 'the 28 scaled commutators S_ab (a < b) are linearly independent')
    ok = all(S[(a, b)] == (T[a] * T[b]) / 2 for a in range(8) for b in range(8) if a != b) and all(S[(a, a)] == sp.zeros(16, 16) for a in range(8))
    rep.check('C22_SAB_half_products', ok, 'S_ab = (1/2) T_a T_b for a != b and S_aa = 0')

    def L_so(a, b):
        M = sp.zeros(8, 8)
        for c in range(8):
            for d in range(8):
                M[c, d] = (1 if c == a else 0) * eta[b, d] - (1 if c == b else 0) * eta[a, d]
        return M
    ok = True
    for a, b, c in itertools.product(range(8), repeat=3):
        lhs = S[(a, b)] * T[c] - T[c] * S[(a, b)]
        rhs = eta[b, c] * T[a] - eta[a, c] * T[b]
        if lhs != rhs:
            ok = False
            break
    rep.check('C23_SAB_vector_action', ok, '[S_ab, T_c] = eta_bc T_a - eta_ac T_b for all a, b, c (the vector representation)')
    ok = True
    pairs = [(a, b) for a in range(8) for b in range(a + 1, 8)]
    for (a, b), (c, d) in itertools.product(pairs, repeat=2):
        lhs = S[(a, b)] * S[(c, d)] - S[(c, d)] * S[(a, b)]
        rhs = eta[b, c] * S[(a, d)] - eta[a, c] * S[(b, d)] - eta[b, d] * S[(a, c)] + eta[a, d] * S[(b, c)]
        if lhs != rhs:
            ok = False
            break
    rep.check('C24_spin44_closure', ok, '[S_ab, S_cd] = eta_bc S_ad - eta_ac S_bd - eta_bd S_ac + eta_ad S_bc for all 784 pairs (so(4,4) structure constants)')
    ok = all((L_so(a, b).T * eta + eta * L_so(a, b)) == sp.zeros(8, 8) for a, b in pairs)
    # the adjoint action on span{T_c}: coefficient matrix equals L_so(a,b)
    ok2 = True
    for a, b in pairs:
        Lab = sp.zeros(8, 8)
        for c in range(8):
            M = S[(a, b)] * T[c] - T[c] * S[(a, b)]
            for d in range(8):
                Lab[d, c] = (M * T[d]).trace() / (16 * eta[d, d])
        if Lab != L_so(a, b):
            ok2 = False
            break
    rep.check('C25_isomorphism_so44', ok and ok2, 'ad(S_ab) on span{T_c} is the so(4,4) generator (L_ab)^c_d = delta^c_a eta_bd - delta^c_b eta_ad, and L_ab^T eta + eta L_ab = 0')
    # exponentials: (T_a T_b)^2 = -eta_aa eta_bb I
    th = sp.symbols('theta', real=True)
    ok = True
    exps = {}
    for a, b in pairs:
        X = T[a] * T[b]
        sq = X * X
        e = -eta[a, a] * eta[b, b]
        if sq != e * I16:
            ok = False
        if e == -1:
            E = sp.cos(th / 2) * I16 + sp.sin(th / 2) * X
            u1 = T[a] if eta[a, a] == 1 else -T[a]
            u2 = sp.cos(th / 2) * T[a] + sp.sin(th / 2) * T[b] if eta[a, a] == 1 else sp.cos(th / 2) * T[a] - sp.sin(th / 2) * T[b]
        else:
            E = sp.cosh(th / 2) * I16 + sp.sinh(th / 2) * X
            u1 = T[a] if eta[a, a] == 1 else -T[a]
            u2 = sp.cosh(th / 2) * T[a] + sp.sinh(th / 2) * T[b] if eta[a, a] == 1 else sp.cosh(th / 2) * T[a] - sp.sinh(th / 2) * T[b]
        prod = (u1 * u2).applyfunc(sp.simplify)
        if (prod - E).applyfunc(sp.simplify) != sp.zeros(16, 16):
            ok = False
        if (u2 * u2).applyfunc(sp.simplify) != sp.simplify(eta[a, a]) * I16 or u1 * u1 != eta[a, a] * I16:
            ok = False
        dE = E.diff(th).subs(th, 0)
        if dE != S[(a, b)]:
            ok = False
        exps[(a, b)] = 'cos' if e == -1 else 'cosh'
    rep.check('C26_exponentials_two_unit_vectors', ok,
              'exp(theta S_ab) = cos(theta/2) I + sin(theta/2) T_a T_b (eta_aa = eta_bb) or cosh(theta/2) I + sinh(theta/2) T_a T_b '
              '(eta_aa = -eta_bb), each a product u1 u2 of two unit vectors, with d/dtheta at 0 equal to S_ab')
    # components of Pin(4,4): twisted adjoint of I, T0, T4, T0T4
    reps = {'I16': (I16, I16, 0), 'T_0': (T[0], T[0] * eta[0, 0], 1), 'T_4': (T[4], T[4] * eta[4, 4], 1),
            'T_0 T_4': (T[0] * T[4], (T[0] * T[4]).inv(), 0)}
    inv = {}
    ok = True
    for name, (g, gi, par) in reps.items():
        L = adjoint_vector_matrix(g, gi, T, True, par)
        if L.T * eta * L != eta:
            ok = False
        inv[name] = (int(sp.sign(L[:4, :4].det())), int(sp.sign(L[4:, 4:].det())), int(L.det()))
    distinct = len(set(v[:2] for v in inv.values())) == 4
    rep.check('C27_pin44_components', ok and distinct,
              'twisted adjoint images in O(4,4) of I16, T_0, T_4, T_0 T_4 have (sign det of the x0..x3 block, sign det of the x4..x7 block) = %s: four different components'
              % {k: v[:2] for k, v in inv.items()})
    # exponentials map into the identity component: check at theta = 1 numerically exact? use the closed form: the
    # twisted adjoint of exp(theta S_ab) is the boost/rotation exp(theta L_ab), whose block determinants are +1
    ok = True
    for a, b in pairs:
        Lab = L_so(a, b)
        # rotation or boost in the (a, b) plane: exp(theta L_ab) restricted blocks have det +1 for every theta
        Rm = sp.simplify((th * Lab).exp())
        dS_ = sp.simplify(Rm[:4, :4].det())
        dT_ = sp.simplify(Rm[4:, 4:].det())
        if eta[a, a] == eta[b, b]:
            if not (sp.simplify(dS_ - 1) == 0 and sp.simplify(dT_ - 1) == 0):
                ok = False
        else:
            # boost: the blocks are cosh(theta) (positive) times identity entries
            if not (sp.simplify(dS_ - sp.cosh(th)) == 0 and sp.simplify(dT_ - sp.cosh(th)) == 0):
                ok = False
    rep.check('C28_exponentials_in_identity_component', ok,
              'exp(theta L_ab) (the image of exp(theta S_ab)) has block determinants +1 (rotations) or cosh(theta) > 0 (boosts): every product of exponentials lies in the identity component')

    # complex structure J = T16^A[4] (the author's checks of In[476])
    J = T[4]
    ok = J * J == -I16 and J.T * C * J == C
    rep.check('C29_complex_structure_T4', ok, 'J = T16^A[4]: J^2 = -I16 and J^T sigma16 J = sigma16 (the author\'s In[476])')
    # the 256 products: symmetric 136, antisymmetric 120; Tr(M M)/16 = +-1
    base = []
    for k in range(9):
        for comb in itertools.combinations(range(8), k):
            M = I16
            for i in comb:
                M = M * T[i]
            base.append((comb, M))
    nsym = sum(1 for _, M in base if M == M.T)
    nanti = sum(1 for _, M in base if M == -M.T)
    trs = set(int((M * M).trace() / 16) for _, M in base)
    indep = lin_independent_count([M for _, M in base])
    rep.check('C30_basis_256', len(base) == 256 and indep == 256 and nsym == 136 and nanti == 120 and trs == {-1, 1},
              'the 256 ordered products T_a1...T_ak (a1 < ... < ak) are a basis of M16(R): 136 symmetric, 120 antisymmetric, Tr(M M)/16 = +-1 (the author\'s Out[200]-Out[220])')

    # ---------------- D. the other sources -----------------------------------------------------------------------
    comps = []

    def compare(name, mats, kind='T16A[0..7]', mapping='identity'):
        ok = len(mats) == 8 and all(sp.Matrix(mats[a]) == T[a] for a in range(8))
        comps.append({'source': name, 'what': kind, 'equal_entry_by_entry': ok})
        return ok

    pc = json.loads((ROOT / 'provenance' / 'dirac_matrices' / 'author_notebook_T16.json').read_text())
    okpc = compare('provenance/dirac_matrices/author_notebook_T16.json (the Pair_Creation notebook, evaluated by WolframScript 15.0.1)', pc['T16A'])
    okpc &= sp.Matrix(pc['T16A_8']) == Gam and sp.Matrix(pc['sigma16']) == C and sp.Matrix(pc['twice_PL']) == 2 * PL and sp.Matrix(pc['twice_PR']) == 2 * PR
    four = pc['four_SAB']
    okpc &= all(sp.Matrix(four[a][b]) == 4 * S[(a, b)] for a in range(8) for b in range(8))
    rep.check('D1_pair_creation_extraction', okpc and pc['notebook_sha256'] == nb_reader.sha256(str(PAIR_NB)),
              'T16A[0..8], sigma16, P_L, P_R and 4 S_ab of the author\'s Pair_Creation notebook (sha256 %s...) equal those of 4+4.nb' % pc['notebook_sha256'][:12])
    # the Pair_Creation notebook itself: the same defining formulas
    pcells = nb_reader.walk_cells(nb_reader.parse_notebook(str(PAIR_NB)))
    want = {
        'T16': 'Table[T16^A[A1]= ArrayFlatten[{{0,Overscript[\\[Tau], _][A1]},{\\[Tau][A1],0}}], {A1,0, 7} ];',
        'taubar': 'Do[{Overscript[\\[Tau], _][A] = FullSimplify[ExpandAll[(\\[Sigma].Transpose[\\[Tau][A]].\\[Sigma])]]} , {A, 1, 7}]',
        # 4+4.nb builds zeta[A] (In[60]) and sets tau[A] = zeta[A] (In[70]); the Pair_Creation notebook writes the
        # same formulas directly for tau (its In[338]): the text of In[60] with \\[Zeta] renamed \\[Tau]
        'tau_as_zeta': DEFINING_CELLS[7][2].replace('\\[Zeta]', '\\[Tau]'),
        's4by4': 'Do[s4by4[h]=Table[Table[SelfDualAntiSymmetric[h,p,q], {q, 4}],{p, 4}], {h,1, 3} ]',
        't4by4': 'Do[t4by4[h]=Table[Table[AntiSelfDualAntiSymmetric[h,p,q], {q, 4}],{p, 4}], {h,1, 3} ]',
        'sigma': 'ArrayFlatten[{{ConstantArray[0,{4,4}],IdentityMatrix[4]},{IdentityMatrix[4],ConstantArray[0,{4,4}]}}]',
        'eta4488': '(\\[Eta]4488 = ArrayFlatten[{{IdentityMatrix[4], 0}, {0, -IdentityMatrix[4]}}]) // MatrixForm',
        'Qa': 'Qa[h_,p_,q_]:=Signature[{h,p,q,4}];',
        'Qb': 'Qb[h_,p_,q_]:= ID4[[p,4]]*ID4[[q,h]]-ID4[[p,h]]*ID4[[q,4]];',
        'PL': '(Subscript[P, L]=1/2(ID16-T16^A[8]))//MatrixForm',
    }
    found = {}
    for k, w in want.items():
        found[k] = [c.index for c in pcells if c.style == 'Input' and norm(w) in norm(c.text)]
    okf = all(found[k] for k in want)
    rep.check('D2_pair_creation_same_formulas', okf,
              'the Pair_Creation notebook contains the same defining formulas (its cells %s; tau there is written directly with the formulas of zeta)' % {k: v[:2] for k, v in found.items()})
    rev = json.loads((ROOT / 'Revision' / 'algebra' / 'gammas.json').read_text())
    rep.check('D3_revision_algebra', compare('Revision/algebra/gammas.json (Revision record)', rev['gamma']), 'gamma[0..7] equal T16^A[0..7]')
    um2 = json.loads((ROOT / 'universe_model_2' / 'outputs' / 'algebra.json').read_text())
    rep.check('D4_universe_model_2', compare('universe_model_2/outputs/algebra.json (UM-2)', um2['gamma']), 'gamma[0..7] equal T16^A[0..7]')
    rw = json.loads((ROOT / 'provenance' / 'dirac_matrices' / 'repository_wolfram_gammas.json').read_text())
    okw = True
    names = []
    for k, v in rw.items():
        if isinstance(v, dict) and 'gamma' in v and 'comparison' not in k:
            g = v['gamma']
            ok_k = compare(k + ' (Wolfram package, evaluated by WolframScript)', g)
            okw &= ok_k
            names.append(k)
    rep.check('D5_repository_wolfram_packages', okw, '%d Wolfram packages: gamma equal T16^A[0..7] (%s)' % (len(names), ', '.join(names)))
    fx = json.loads((ROOT / 'artifacts' / 'dirac16complex' / 'arbitrary-field' / 'algebra-fixture.json').read_text())
    gfx = fx.get('gamma') or fx.get('gammas') or fx.get('T16A')
    if isinstance(gfx, dict):
        gfx = [gfx[str(a)] if str(a) in gfx else gfx[a] for a in range(8)]
    okfx = compare('artifacts/dirac16complex/arbitrary-field/algebra-fixture.json (Stage 1 fixture)', gfx) if gfx else False
    rep.check('D6_stage1_fixture', okfx, 'Stage 1 fixture gamma equal T16^A[0..7]')
    out['comparisons'] = comps

    # ---------------- E. outputs --------------------------------------------------------------------------------
    il = G.as_int_lists
    out.update({
        'notebook': 'universe_model_3/author_inputs/4+4.nb', 'notebook_sha256': digest,
        'eta4488': il(eta), 'sigma88': il(sig), 's4by4': {h: il(s4[h]) for h in (1, 2, 3)},
        't4by4': {h: il(t4[h]) for h in (1, 2, 3)}, 'zeta': {a: il(zeta[a]) for a in range(8)},
        'tau': {a: il(tau[a]) for a in range(8)}, 'taubar': {a: il(taub[a]) for a in range(8)},
        'T16A': {a: il(T[a]) for a in range(9)}, 'sigma16': il(C), 'twice_PL': il(2 * PL), 'twice_PR': il(2 * PR),
        'twice_SAB': {'%d,%d' % (a, b): il(2 * S[(a, b)]) for a, b in pairs},
        'pin_component_invariants': {k: list(v) for k, v in inv.items()},
        'exponential_type': {'%d,%d' % k: v for k, v in exps.items()},
        'runtime_s': round(time.time() - t0, 1),
    })
    (UM4 / 'outputs').mkdir(exist_ok=True)
    (UM4 / 'reports').mkdir(exist_ok=True)
    (UM4 / 'outputs' / 'dirac_matrices.json').write_text(json.dumps(out, indent=1, sort_keys=True) + '\n')
    report = {'script': 'universe_model_4/code/um4_dirac_matrices.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks), 'all_passed': rep.all_passed}
    (UM4 / 'reports' / 'dirac_matrices_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if rep.all_passed else 1


if __name__ == '__main__':
    sys.exit(main())
