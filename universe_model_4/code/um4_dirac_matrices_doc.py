#!/usr/bin/env python3
"""um4_dirac_matrices_doc.py - writes the provenance document `universe_model_4/dirac matrices.md`.

It reads only what um4_dirac_matrices.py computed (outputs/dirac_matrices.json, reports/dirac_matrices_checks.json)
and the author's notebook (for the verbatim cells), so every matrix printed in the document is machine-produced and
every statement is backed by a named check.  Run um4_dirac_matrices.py first.
Usage: python universe_model_4/code/um4_dirac_matrices_doc.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UM4 = HERE.parent
sys.path.insert(0, str(UM4 / 'tools'))
sys.path.insert(0, str(HERE))
import nb_reader  # noqa: E402
from um4_dirac_matrices import DEFINING_CELLS, NB  # noqa: E402

OUT = json.loads((UM4 / 'outputs' / 'dirac_matrices.json').read_text())
REP = json.loads((UM4 / 'reports' / 'dirac_matrices_checks.json').read_text())
CHK = {c['name']: c for c in REP['checks']}

# ------------------------------------------------------------------------------------------------------------------
# symbols of this document: key -> (symbol in TeX, meaning)
# ------------------------------------------------------------------------------------------------------------------
SYM = {
    'a': (r'$a, b, c, d$', 'Frame (orthonormal) indices running over $0, 1, \\dots, 7$; the value $k$ belongs to the '
          "author's coordinate $x_k$ ($x_0$ the hidden space-like direction, $x_1, x_2, x_3$ ordinary space, $x_4$ the time, "
          '$x_5, x_6, x_7$ the extra time-like directions). No sum over a repeated frame index unless a sum is written.'),
    'x': (r'$x_0, \dots, x_7$', "The author's coordinates $X = \\{x_0, x_1, \\dots, x_7\\}$ (notebook "
          '`Dirac_Einstein-Lovelock_4+4_Nash.nb`, Section DEFCHART, `X = {x0[], x1[], ..., x7[]}`).'),
    'eta': (r'$\eta_{ab}$', 'The flat frame metric, $\\eta = \\mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$ in the order '
            "$x_0, \\dots, x_7$ (the author's `eta4488`); $\\eta^{ab}$ is the same matrix."),
    'In': (r'$I_n$', 'The $n \\times n$ identity matrix ($n = 4, 8, 16$; the author\'s `ID4`, `ID8`, `ID16`).'),
    'Zn': (r'$0$', 'The zero matrix of the size required by its position (in a block matrix: a zero block).'),
    'sigma': (r'$\sigma$', 'The real symmetric $8 \\times 8$ matrix $\\sigma = \\begin{pmatrix} 0 & I_4 \\\\ I_4 & 0 '
              "\\end{pmatrix}$ (the author's `sigma88`), with $\\sigma^2 = I_8$."),
    'eps': (r'$\varepsilon_{hpqr}$', 'The Levi-Civita symbol of four indices $1, \\dots, 4$ (the author\'s `Signature[{h,p,q,r}]`): '
            '$+1$ for an even permutation of $(1, 2, 3, 4)$, $-1$ for an odd one, $0$ if an index repeats.'),
    'delta': (r'$\delta_{pq}$', 'The Kronecker delta: $1$ if $p = q$, else $0$ (the author\'s `ID4[[p,q]]`).'),
    's4': (r'$s_h,\ t_h$', "The author's $4 \\times 4$ matrices `s4by4[h]` and `t4by4[h]` ($h = 1, 2, 3$): real, antisymmetric, "
           'self-dual ($s_h$) and anti-self-dual ($t_h$) in the four-dimensional sense.'),
    'hpq': (r'$h, p, q$', 'Integer labels of the notebook: $h = 1, 2, 3$ numbers the matrices $s_h$, $t_h$; $p, q = 1, \\dots, 4$ '
            'are their row and column (counted from 1 as in Mathematica).'),
    'zeta': (r'$\zeta_A$', 'The author\'s intermediate $8 \\times 8$ matrices `zeta[A]` ($A = 0, \\dots, 7$), built from $s_h$ and $t_h$.'),
    'tau': (r'$\tau_a$', "The author's real $8 \\times 8$ matrices `tau[a]` ($a = 0, \\dots, 7$), $\\tau_a = \\zeta_a$."),
    'taubar': (r'$\bar\tau_a$', "The author's `taubar[a]` (written $\\overline{\\tau}$ in the notebook), "
               '$\\bar\\tau_0 = I_8$, $\\bar\\tau_a = \\sigma\\,\\tau_a^{\\mathsf T}\\,\\sigma$ for $a = 1, \\dots, 7$ (not a complex conjugate).'),
    'T': (r'$T_a$', "The author's eight real $16 \\times 16$ Dirac matrices `T16^A[a]` ($a = 0, \\dots, 7$), the gamma matrix of the "
          'frame direction of $x_a$: $\\gamma^{(x_a)} = T_a$.'),
    'Gamma': (r'$\Gamma$', "The chirality matrix, the author's `T16^A[8]` $= T_0 T_1 \\cdots T_7$."),
    'C': (r'$\sigma_{16}$', "The author's `sigma16` $= T_0 T_1 T_2 T_3$, the matrix of the Dirac adjoint "
          '$\\bar\\Psi = \\Psi^\\dagger\\sigma_{16}$.'),
    'PL': (r'$P_L,\ P_R$', "The author's chiral projection operators `P_L` $= \\tfrac12(I_{16} - \\Gamma)$ and "
           '`P_R` $= \\tfrac12(I_{16} + \\Gamma)$ (left-handed and right-handed).'),
    'S': (r'$S_{ab}$', 'The scaled commutator $S_{ab} = \\tfrac14[T_a, T_b]$ ($[X, Y] = XY - YX$), the generators of spin(4,4).'),
    'comm': (r'$[X, Y],\ \{X, Y\}$', 'The commutator $XY - YX$ and the anticommutator $XY + YX$ of two matrices.'),
    'transpose': (r'$X^{\mathsf T},\ X^\dagger$', 'The transpose of a matrix and its Hermitian conjugate (transpose of the complex '
                  'conjugate); for the real matrices of this document they coincide.'),
    'theta': (r'$\theta$', 'A real parameter (an angle for a rotation, a rapidity for a boost).'),
    'L': (r'$L_{ab}$', 'The generator of $O(4,4)$ on vectors in the plane $(a, b)$: $(L_{ab})^c{}_d = \\delta^c_a\\eta_{bd} - '
          '\\delta^c_b\\eta_{ad}$.'),
    'Lam': (r'$\Lambda$', 'An $8 \\times 8$ real matrix of $O(4,4)$: $\\Lambda^{\\mathsf T}\\eta\\Lambda = \\eta$.'),
    'u': (r'$u_1, u_2$', 'Unit vectors of the Clifford algebra: real combinations $u = u^a T_a$ with $u^2 = \\pm I_{16}$.'),
    'g': (r'$g$', 'An element of the group $\\mathrm{Pin}(4,4)$ (an invertible $16 \\times 16$ real matrix).'),
    'alpha': (r'$\alpha(g)$', 'The parity automorphism: $\\alpha(g) = g$ for an even element (a product of an even number of '
              'vectors), $\\alpha(g) = -g$ for an odd one.'),
    'rho': (r'$\rho(g)$', 'The twisted adjoint action of $g$ on vectors, $\\rho(g)v = \\alpha(g)\\,v\\,g^{-1}$, an element of $O(4,4)$.'),
    'Psi': (r'$\Psi$', 'The 16-component dirac16complex spinor field (components $\\Psi_0, \\dots, \\Psi_{15}$), on which the matrices act.'),
    'Psibar': (r'$\bar\Psi$', 'The Dirac adjoint $\\bar\\Psi = \\Psi^\\dagger\\sigma_{16}$.'),
    'J': (r'$J$', "The author's complex structure $J = T_4$ (the Dirac matrix of the time $x_4$), $J^2 = -I_{16}$."),
    'v': (r'$v,\ v^a$', 'A vector of the Clifford algebra, $v = v^a T_a$ with real components $v^a$.'),
}


def symbols(keys):
    lines = ['', '**Symbols in this equation.**', '']
    for k in keys:
        s, m = SYM[k]
        lines.append('- %s: %s' % (s, m))
    lines.append('')
    return '\n'.join(lines)


def tex_matrix(M, small=True, zero='0'):
    rows = []
    for r in M:
        rows.append(' & '.join(('-1' if x == -1 else ('1' if x == 1 else (zero if x == 0 else str(x)))) if isinstance(x, int)
                               else str(x) for x in r))
    body = ' \\\\ '.join(rows)
    pre = '\\scriptstyle ' if small and len(M) > 8 else ''
    return pre + '\\begin{pmatrix} ' + body + ' \\end{pmatrix}'


def frac_matrix(M2, denom):
    """M2 holds denom * M as integers: print the entries as fractions."""
    out = []
    for r in M2:
        row = []
        for x in r:
            if x == 0:
                row.append('0')
            elif x % denom == 0:
                row.append(str(x // denom))
            else:
                row.append(('-' if x < 0 else '') + '\\tfrac{%d}{%d}' % (abs(x), denom))
        out.append(row)
    return out


def perm_description(M):
    """For a signed permutation matrix: the list 'row r: sign column c'."""
    parts = []
    for r, row in enumerate(M):
        for c, x in enumerate(row):
            if x != 0:
                parts.append('%d:%s%d' % (r, '+' if x > 0 else '-', c))
    return ', '.join(parts)


def chk(name):
    c = CHK[name]
    return '`%s` (%s)' % (name, 'passed' if c['passed'] else 'FAILED')


def main():
    if not REP['all_passed']:
        print('not every check passed; run um4_dirac_matrices.py and fix it first')
        return 1
    cells = nb_reader.walk_cells(nb_reader.parse_notebook(str(NB)))
    T = {int(k): v for k, v in OUT['T16A'].items()}
    tau = {int(k): v for k, v in OUT['tau'].items()}
    taub = {int(k): v for k, v in OUT['taubar'].items()}
    s4 = {int(k): v for k, v in OUT['s4by4'].items()}
    t4 = {int(k): v for k, v in OUT['t4by4'].items()}
    eta = OUT['eta4488']
    sig = OUT['sigma88']
    C = OUT['sigma16']
    PL2 = OUT['twice_PL']
    PR2 = OUT['twice_PR']
    S2 = OUT['twice_SAB']
    inv = OUT['pin_component_invariants']
    npass, ntot = REP['passed'], REP['total']

    L = []
    w = L.append
    w('---')
    w('title: "dirac matrices: the eight real 16 x 16 Dirac matrices of the author\'s notebook 4+4.nb"')
    w('subtitle: "Provenance file of the model UM-4 (universe_model_4): construction, reality, anticommutation relations, '
      'spin(4,4), Spin(4,4) and Pin(4,4), the chiral projection operators, and the proof that every calculation uses these '
      'matrices"')
    w('author:')
    w('  - "Matrices and notebook: Patrick L. Nash"')
    w('  - "Provenance: Claude (Anthropic), 2026-10-24"')
    w('---')
    w('')
    w('# The answer')
    w('')
    w('This file was generated by the program `um4_dirac_matrices_doc.py` of UM-4 from the results of `um4_dirac_matrices.py`. '
      'It proves, with exact computations whose results are printed here, the statements the author asked for on '
      '2026-10-24 about the eight real $16 \\times 16$ Dirac matrices. It is self-contained: every equation it uses is written '
      'here and every symbol is defined right below the equation in which it appears. All %d named checks of the program '
      '`universe_model_4/code/um4_dirac_matrices.py` pass; each statement below names the check that proves it.' % ntot)
    w('')
    w('1. **They are the matrices of `4+4.nb`.** The eight matrices $T_a$ = `T16^A[a]` ($a = 0, \\dots, 7$) were rebuilt '
      'cell by cell from the author\'s own input cells (quoted verbatim in Section 2) and are equal, entry by entry, to every '
      'matrix that the notebook itself stored as an output when Mathematica evaluated those cells: the eight $T_a$ '
      '(`Out[210]`), $T_0 T_1 \\cdots T_7$ (`Out[98]`), $P_L$ and $P_R$ (`Out[111]`, `Out[112]`) and seven more; 26 stored '
      'True/False outputs (283 values) of the matrix cells are reproduced identically. %s, %s, %s.'
      % (chk('B11_stored_T16A_0_to_7'), chk('B8_stored_T16A8'), chk('B13_stored_boolean_outputs')))
    w('2. **They are the matrices used in this repository\'s calculations.** The same eight matrices, entry by entry, are '
      'used by the author\'s notebook `Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb` '
      '(the same defining formulas), the Revision record, the universe model UM-2, nine Wolfram packages and the Stage-1 '
      'fixture (Section 11); every UM-4 computation takes them from one module, `universe_model_4/code/um4_gammas.py`. '
      '%s, %s, %s.' % (chk('D1_pair_creation_extraction'), chk('D2_pair_creation_same_formulas'), chk('D5_repository_wolfram_packages')))
    w('3. **They are real.** Every entry is $-1$, $0$ or $+1$; each $T_a$ is a signed permutation matrix and an orthogonal '
      'matrix, symmetric for $a = 0, 1, 2, 3$ and antisymmetric for $a = 4, 5, 6, 7$. %s, %s, %s.'
      % (chk('C1_real_integer_entries'), chk('C2_signed_permutation'), chk('C4_orthogonal_and_symmetry')))
    w('4. **They satisfy the anticommutation relations** $\\{T_a, T_b\\} = 2\\eta_{ab}I_{16}$ with '
      '$\\eta = \\mathrm{diag}(+1, +1, +1, +1, -1, -1, -1, -1)$: they generate the real Clifford algebra of signature $(4,4)$, '
      'which is the full algebra of real $16 \\times 16$ matrices. %s, %s.' % (chk('C3_clifford_relations'), chk('C30_basis_256')))
    w('5. **Their scaled commutators generate Pin(4,4).** The 28 matrices $S_{ab} = \\tfrac14[T_a, T_b]$ ($a < b$) are linearly '
      'independent, close under commutation with the structure constants of $so(4,4)$ and act on the $T_c$ as the vector '
      'representation: they are a basis of the Lie algebra $spin(4,4) \\cong so(4,4)$, which is the Lie algebra of Pin(4,4) '
      '(and of Spin(4,4)). Each exponential $\\exp(\\theta S_{ab})$ is a product of two unit vectors, so it lies in Pin(4,4); '
      'the exponentials generate the identity component $\\mathrm{Spin}_0(4,4)$; together with the two reflections $T_0$ and '
      '$T_4$ they generate all of Pin(4,4), whose four components are identified by exact invariants. Precisely stated: the '
      'scaled commutators generate Pin(4,4) as its Lie algebra and, by exponentiation, its identity component; no product of '
      'exponentials leaves that component, so the reflections are needed for the other three. %s, %s, %s, %s, %s.'
      % (chk('C21_SAB_independent'), chk('C24_spin44_closure'), chk('C26_exponentials_two_unit_vectors'),
         chk('C28_exponentials_in_identity_component'), chk('C27_pin44_components')))
    w('6. **The chiral projection operators of the subsection "Left - Handed vs . Right - Handed Fermion Fields (Chirality) ; '
      'projection operators" are re-derived and confirmed.** The only matrices that commute with every $S_{ab}$ are the '
      'combinations of $I_{16}$ and $\\Gamma = T_0 T_1 \\cdots T_7$; $\\Gamma^2 = I_{16}$; the only non-trivial projectors in '
      'that algebra are $\\tfrac12(I_{16} \\mp \\Gamma)$, which are the author\'s $P_L$ and $P_R$, entry by entry; '
      '$\\Gamma = \\mathrm{diag}(-I_8, I_8)$, so $P_L$ projects on $\\Psi_0, \\dots, \\Psi_7$ and $P_R$ on $\\Psi_8, \\dots, \\Psi_{15}$. '
      '%s, %s, %s, %s.' % (chk('C17_commutant_spin44'), chk('C20_idempotents_of_chirality_algebra'), chk('B9_stored_PL'), chk('B10_stored_PR')))
    w('7. **The coordinates are the author\'s** $\\{x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7\\}$: the input cell `In[48]` of the '
      'Section DEFCHART of `Dirac_Einstein-Lovelock_4+4_Nash.nb` is `X={x0[], x1[], x2[], x3[], x4[], x5[], x6[], x7[]}` '
      '(spaces added after the commas), and `4+4.nb` uses the same '
      'list (its cell 9). The frame index $a$ of $T_a$ is the index of the coordinate $x_a$. %s, %s.'
      % (chk('A6_coordinates_DEFCHART'), chk('A5_coordinates_in_4p4')))
    w('')
    w('Each of the eight matrices, the chirality matrix, the Dirac-adjoint matrix, the projectors, the complex structure and '
      'the 28 generators is displayed in full below.')
    w('')

    # ---------------- 1. notation
    w('# Notation')
    w('')
    w('The frame metric of the eight-dimensional space is')
    w('')
    w('$$')
    w('\\eta_{ab} = \\mathrm{diag}(+1,\\ +1,\\ +1,\\ +1,\\ -1,\\ -1,\\ -1,\\ -1)_{ab},\\qquad a, b = 0, 1, \\dots, 7')
    w('$$')
    w(symbols(['eta', 'a']))
    w('Four directions are space-like ($x_0$, $x_1$, $x_2$, $x_3$) and four are time-like ($x_4$, $x_5$, $x_6$, $x_7$), in the order '
      'of the author\'s coordinates:')
    w('')
    w('$$')
    w('X = \\{x_0,\\ x_1,\\ x_2,\\ x_3,\\ x_4,\\ x_5,\\ x_6,\\ x_7\\}')
    w('$$')
    w(symbols(['x']))
    w('Matrices act on columns $\\Psi = (\\Psi_0, \\dots, \\Psi_{15})^{\\mathsf T}$; rows and columns of a $16 \\times 16$ matrix are '
      'counted from 0 in the text and in the displays (the notebook counts them from 1). A block matrix '
      '$\\begin{pmatrix} A & B \\\\ C & D \\end{pmatrix}$ is the author\'s `ArrayFlatten[{{A, B}, {C, D}}]`.')
    w('')

    # ---------------- 2. source
    w('# The source: the author\'s notebook 4+4.nb')
    w('')
    w('The notebook `universe_model_3/author_inputs/4+4.nb` ("eight, real-valued, 16 by 16, Dirac Matrices", Wolfram 15.0) has '
      'the sha256 `%s` and 806 cells; it is read without Mathematica by `universe_model_4/tools/nb_reader.py`, which parses '
      'the notebook file (a Wolfram Language expression) and converts every cell to linear text. %s, %s.'
      % (OUT['notebook_sha256'], chk('A1_notebook_sha256'), chk('A2_notebook_cell_count')))
    w('')
    w('The matrices are defined by the following input cells, quoted verbatim (cell number in the file, label, text; '
      '%s):' % chk('A3_defining_cells_verbatim'))
    w('')
    w('```')
    for idx, label, text in sorted(DEFINING_CELLS, key=lambda t: t[0]):
        w('cell %d  %s' % (idx, label))
        for line in text.split('\n'):
            if line.strip():
                w('    ' + line)
    w('```')
    w('')
    w('The cells 160 to 166 form the subsection "%s" (%s): cell 161 defines $P_L$, cell 163 defines $P_R$ and cell 165 '
      'tests them; Section 9 below re-derives them.' % ('Left - Handed vs . Right - Handed Fermion Fields (Chirality) ; projection operators',
                                                        chk('A4_chirality_subsection_found')))
    w('')
    w('In cell 131 (`In[96]`) the author assigns `sigma16 = T16^A[0].T16^A[1].T16^A[2].T16^A[3]` before the matrices are '
      'defined in cell 133 (`In[97]`): the symbol then holds the unevaluated product, which takes its value as soon as the '
      '`T16^A` exist; cell 148 (`In[105]`) confirms the value $\\mathrm{diag}(-\\sigma, \\sigma)$. In cell 87 (`In[70]`) the line '
      'inside `(* ... *)` is a comment and is not evaluated.')
    w('')

    # ---------------- 3. construction
    w('# The construction, step by step')
    w('')
    w('## The two $8 \\times 8$ metrics')
    w('')
    w('$$')
    w('\\eta = \\begin{pmatrix} I_4 & 0 \\\\ 0 & -I_4 \\end{pmatrix} = %s,\\qquad \\sigma = \\begin{pmatrix} 0 & I_4 \\\\ I_4 & 0 \\end{pmatrix} = %s'
      % (tex_matrix(eta, False), tex_matrix(sig, False)))
    w('$$')
    w(symbols(['eta', 'sigma', 'In', 'Zn']))
    w('(%s.) The matrix $\\sigma$ has the eigenvalues $+1$ and $-1$, four times each, so it is also a metric of signature $(4,4)$.'
      % chk('B1_stored_eta4488'))
    w('')
    w('## The self-dual and anti-self-dual $4 \\times 4$ matrices')
    w('')
    w('The author\'s cell 24 defines, for $h = 1, 2, 3$ and $p, q = 1, \\dots, 4$,')
    w('')
    w('$$')
    w('(s_h)_{pq} = \\varepsilon_{hpq4} - \\big(\\delta_{p4}\\delta_{qh} - \\delta_{ph}\\delta_{q4}\\big),\\qquad '
      '(t_h)_{pq} = \\varepsilon_{hpq4} + \\big(\\delta_{p4}\\delta_{qh} - \\delta_{ph}\\delta_{q4}\\big)')
    w('$$')
    w(symbols(['s4', 'hpq', 'eps', 'delta']))
    w('which gives (%s)' % chk('B2_stored_s4by4_t4by4'))
    w('')
    w('$$')
    w(',\\quad '.join('s_%d = %s' % (h, tex_matrix(s4[h], False)) for h in (1, 2, 3)))
    w('$$')
    w('')
    w('$$')
    w(',\\quad '.join('t_%d = %s' % (h, tex_matrix(t4[h], False)) for h in (1, 2, 3)))
    w('$$')
    w(symbols(['s4']))
    w('Each $s_h$ equals its four-dimensional dual, $\\tfrac12\\sum_{j_1, j_2}\\varepsilon_{pqj_1j_2}(s_h)_{j_1j_2} = (s_h)_{pq}$, and '
      'each $t_h$ minus its dual (the author\'s cells 67 and 70, both giving zero matrices).')
    w('')
    w('## The $8 \\times 8$ matrices $\\tau_a$ and $\\bar\\tau_a$')
    w('')
    w('The author\'s cells 73 and 87 define')
    w('')
    w('$$')
    w('\\begin{aligned}')
    w('&\\tau_0 = I_8,\\qquad \\tau_h = \\begin{pmatrix} 0 & s_h \\\\ s_h & 0 \\end{pmatrix},\\qquad '
      '\\tau_{7-h} = \\begin{pmatrix} 0 & t_h \\\\ -t_h & 0 \\end{pmatrix}\\qquad (h = 1, 2, 3),\\\\')
    w('&\\tau_7 = \\tau_1\\tau_2\\tau_3\\tau_4\\tau_5\\tau_6')
    w('\\end{aligned}')
    w('$$')
    w(symbols(['tau', 'zeta', 's4', 'In', 'Zn']))
    w('(the author first names them $\\zeta_A$ and then sets $\\tau_A = \\zeta_A$), and cell 91 defines')
    w('')
    w('$$')
    w('\\bar\\tau_0 = I_8,\\qquad \\bar\\tau_a = \\sigma\\,\\tau_a^{\\mathsf T}\\,\\sigma\\quad (a = 1, \\dots, 7)')
    w('$$')
    w(symbols(['taubar', 'tau', 'sigma', 'transpose', 'In']))
    w('(%s, %s). Explicitly:' % (chk('B4_stored_tau7'), chk('C6_taubar_definition')))
    w('')
    for a in range(8):
        w('$$')
        w('\\tau_%d = %s,\\qquad \\bar\\tau_%d = %s' % (a, tex_matrix(tau[a], False), a, tex_matrix(taub[a], False)))
        w('$$')
        w('')
    w(symbols(['tau', 'taubar']))
    w('They satisfy, for all $a, b = 0, \\dots, 7$ (%s),' % chk('C5_block_relations'))
    w('')
    w('$$')
    w('\\tau_a\\bar\\tau_b + \\tau_b\\bar\\tau_a = 2\\eta_{ab}I_8,\\qquad \\bar\\tau_a\\tau_b + \\bar\\tau_b\\tau_a = 2\\eta_{ab}I_8')
    w('$$')
    w(symbols(['tau', 'taubar', 'eta', 'In']))
    w('and each $\\tau_a$ is orthogonal, $\\tau_a\\tau_a^{\\mathsf T} = I_8$ (%s).' % chk('C7_tau_orthogonal'))
    w('')
    w('## The eight $16 \\times 16$ Dirac matrices')
    w('')
    w('The author\'s cell 133 (`In[97]`) defines, for $a = 0, \\dots, 7$,')
    w('')
    w('$$')
    w('T_a = \\begin{pmatrix} 0 & \\bar\\tau_a \\\\ \\tau_a & 0 \\end{pmatrix}')
    w('$$')
    w(symbols(['T', 'tau', 'taubar', 'Zn']))
    w('Here they are, every entry (%s). Below each matrix, its action as a signed permutation is listed in the form '
      '"row:sign column" (the only non-zero entry of each row; for example 0:+8 means that row 0 has the entry $+1$ in column 8).' % chk('B11_stored_T16A_0_to_7'))
    w('')
    kinds = {0: 'the hidden space-like direction', 1: 'ordinary space', 2: 'ordinary space', 3: 'ordinary space',
             4: 'the time', 5: 'an extra time-like direction', 6: 'an extra time-like direction', 7: 'an extra time-like direction'}
    for a in range(8):
        w('**$T_%d$ = `T16^A[%d]`, the Dirac matrix of the direction $x_%d$ (%s); $T_%d^2 = %sI_{16}$.**'
          % (a, a, a, kinds[a], a, '' if eta[a][a] == 1 else '-'))
        w('')
        w('$$')
        w('T_%d = %s' % (a, tex_matrix(T[a])))
        w('$$')
        w('')
        w('Signed permutation of $T_%d$: %s.' % (a, perm_description(T[a])))
        w('')
    w(symbols(['T', 'In']))

    # ---------------- 4. real
    w('# Proof that the eight matrices are real')
    w('')
    w('Every step of the construction (integer entries $0, \\pm1$ of $\\varepsilon$ and $\\delta$, block assembly, transposition, '
      'products of integer matrices, multiplication by $\\sigma$) maps integer matrices to integer matrices, so the $T_a$ are '
      'real (indeed integer) matrices. The computed entries are only $-1$, $0$ and $+1$ (%s); each row and each column of '
      'each $T_a$ holds exactly one non-zero entry, so every $T_a$ is a signed permutation matrix (%s), hence orthogonal, and '
      '(%s)' % (chk('C1_real_integer_entries'), chk('C2_signed_permutation'), chk('C4_orthogonal_and_symmetry')))
    w('')
    w('$$')
    w('T_a^{\\mathsf T} = \\eta_{aa}\\,T_a,\\qquad T_a T_a^{\\mathsf T} = I_{16}\\qquad (a = 0, \\dots, 7)')
    w('$$')
    w(symbols(['T', 'transpose', 'eta', 'In']))
    w('so $T_0$, $T_1$, $T_2$, $T_3$ are symmetric and $T_4$, $T_5$, $T_6$, $T_7$ antisymmetric (the author\'s `Out[102]`, '
      '`Out[103]`). Because the matrices are real, $T_a^\\dagger = T_a^{\\mathsf T}$.')
    w('')

    # ---------------- 5. anticommutation
    w('# Proof of the anticommutation relations')
    w('')
    w('**Theorem.** For all $a, b = 0, \\dots, 7$')
    w('')
    w('$$')
    w('\\{T_a, T_b\\} = T_aT_b + T_bT_a = 2\\,\\eta_{ab}\\,I_{16}')
    w('$$')
    w(symbols(['T', 'comm', 'eta', 'In']))
    w('**Proof.** With the block form of $T_a$,')
    w('')
    w('$$')
    w('T_aT_b + T_bT_a = \\begin{pmatrix} \\bar\\tau_a\\tau_b + \\bar\\tau_b\\tau_a & 0 \\\\ 0 & \\tau_a\\bar\\tau_b + \\tau_b\\bar\\tau_a \\end{pmatrix}')
    w('$$')
    w(symbols(['T', 'tau', 'taubar', 'Zn']))
    w('and the two diagonal blocks are $2\\eta_{ab}I_8$ by the $8 \\times 8$ relations of the previous section (%s). Those relations '
      'are finitely many identities between explicit integer matrices; they were verified by exact matrix multiplication for '
      'every one of the 64 pairs $(a, b)$, and so were the 64 relations of the theorem directly (%s). An exhaustive exact '
      'verification of a finite set of identities between explicit integer matrices is a complete proof. The author\'s cell 156 '
      '(`In[109]`) states the same relations and its stored output is True in all 64 places (%s). $\\square$'
      % (chk('C5_block_relations'), chk('C3_clifford_relations'), chk('B13_stored_boolean_outputs')))
    w('')
    w('In particular $T_a^2 = +I_{16}$ for the space-like directions $x_0, x_1, x_2, x_3$ and $T_a^2 = -I_{16}$ for the time-like '
      'directions $x_4, x_5, x_6, x_7$, and different $T_a$ anticommute. The $2^8 = 256$ ordered products $T_{a_1}\\cdots T_{a_k}$ '
      '($a_1 < \\dots < a_k$, the empty product being $I_{16}$) are linearly independent (%s): the real algebra generated by the '
      '$T_a$ is the whole algebra of real $16 \\times 16$ matrices, the Clifford algebra $Cl(4,4) \\cong M_{16}(\\mathbb R)$; of the '
      '256 products 136 are symmetric and 120 antisymmetric, as the author found (`Out[205]`, `Out[217]`, `Out[220]`).'
      % chk('C30_basis_256'))
    w('')

    # ---------------- 6. adjoint
    w('# The Dirac-adjoint matrix $\\sigma_{16}$')
    w('')
    w('The author\'s `sigma16` is')
    w('')
    w('$$')
    w('\\sigma_{16} = T_0T_1T_2T_3 = \\begin{pmatrix} -\\sigma & 0 \\\\ 0 & \\sigma \\end{pmatrix} = %s' % tex_matrix(C))
    w('$$')
    w(symbols(['C', 'T', 'sigma', 'Zn']))
    w('It is real, symmetric and its own inverse, and (%s, %s)' % (chk('C8_sigma16'), chk('C9_sigma16_conjugation')))
    w('')
    w('$$')
    w('(\\sigma_{16}T_a)^{\\mathsf T} = -\\sigma_{16}T_a,\\qquad \\sigma_{16}\\,T_a\\,\\sigma_{16}^{-1} = -T_a^{\\mathsf T} = -T_a^\\dagger\\qquad (a = 0, \\dots, 7)')
    w('$$')
    w(symbols(['C', 'T', 'transpose']))
    w('which is the author\'s check `In[104]` (all True). The second relation is what makes $\\bar\\Psi = \\Psi^\\dagger\\sigma_{16}$ '
      'the Dirac adjoint: under $\\Psi \\to g\\Psi$ with $g = \\exp(\\tfrac12\\omega^{ab}S_{ab})$ the bilinear $\\bar\\Psi\\Psi$ is '
      'invariant and $\\bar\\Psi T_a\\Psi$ transforms as a vector (because $\\sigma_{16}S_{ab}\\sigma_{16}^{-1} = -S_{ab}^\\dagger$ follows '
      'from it).')
    w('')
    w('$$')
    w('\\bar\\Psi = \\Psi^\\dagger\\,\\sigma_{16}')
    w('$$')
    w(symbols(['Psibar', 'Psi', 'C', 'transpose']))

    # ---------------- 7. spin and pin
    w('# The scaled commutators: spin(4,4), Spin(4,4) and Pin(4,4)')
    w('')
    w('## Definitions')
    w('')
    w('A **vector** of the Clifford algebra is $v = v^aT_a$ with real $v^a$; then $v^2 = \\eta_{ab}v^av^b\\,I_{16}$, and $v$ is a '
      '**unit vector** if $v^2 = \\pm I_{16}$.')
    w('')
    w('$$')
    w('v = \\sum_{a=0}^{7}v^aT_a,\\qquad v^2 = \\Big(\\sum_{a,b}\\eta_{ab}v^av^b\\Big)I_{16}')
    w('$$')
    w(symbols(['v', 'T', 'eta', 'In']))
    w('**Pin(4,4)** is the group generated by the unit vectors (products $u_1u_2\\cdots u_k$ of unit vectors); **Spin(4,4)** is its '
      'subgroup of products of an even number of unit vectors. The **twisted adjoint action**')
    w('')
    w('$$')
    w('\\rho(g)\\,v = \\alpha(g)\\,v\\,g^{-1}')
    w('$$')
    w(symbols(['rho', 'g', 'alpha', 'v']))
    w('maps vectors to vectors and preserves $v^2$, so $\\rho(g) \\in O(4,4)$; for a unit vector $u$ it is the reflection in the '
      'hyperplane orthogonal to $u$, and $\\rho$ is a two-to-one homomorphism of Pin(4,4) onto $O(4,4)$ (a standard theorem: '
      'Cartan-Dieudonne together with $\\ker\\rho = \\{\\pm I_{16}\\}$). The Lie algebra of Pin(4,4), of Spin(4,4) and of their '
      'identity component $\\mathrm{Spin}_0(4,4)$ is the same, $spin(4,4)$, of dimension $\\dim O(4,4) = 28$.')
    w('')
    w('## The scaled commutators are a basis of spin(4,4)')
    w('')
    w('$$')
    w('S_{ab} = \\tfrac14[T_a, T_b] = \\tfrac12T_aT_b\\quad (a \\ne b),\\qquad S_{aa} = 0,\\qquad S_{ba} = -S_{ab}')
    w('$$')
    w(symbols(['S', 'T', 'comm', 'a']))
    w('(%s). The 28 matrices $S_{ab}$ with $a < b$ are linearly independent (%s) and satisfy, for all indices (%s, %s),'
      % (chk('C22_SAB_half_products'), chk('C21_SAB_independent'), chk('C23_SAB_vector_action'), chk('C24_spin44_closure')))
    w('')
    w('$$')
    w('\\begin{aligned}')
    w('&[S_{ab}, T_c] = \\eta_{bc}T_a - \\eta_{ac}T_b,\\\\')
    w('&[S_{ab}, S_{cd}] = \\eta_{bc}S_{ad} - \\eta_{ac}S_{bd} - \\eta_{bd}S_{ac} + \\eta_{ad}S_{bc}')
    w('\\end{aligned}')
    w('$$')
    w(symbols(['S', 'T', 'comm', 'eta', 'a']))
    w('The first relation follows from the theorem of the previous section in one line: $[T_aT_b, T_c] = T_a\\{T_b, T_c\\} - \\{T_a, T_c\\}T_b '
      '= 2\\eta_{bc}T_a - 2\\eta_{ac}T_b$. It says that $\\mathrm{ad}(S_{ab})$ acts on the span of the $T_c$ by the matrix')
    w('')
    w('$$')
    w('(L_{ab})^c{}_d = \\delta^c_a\\,\\eta_{bd} - \\delta^c_b\\,\\eta_{ad},\\qquad L_{ab}^{\\mathsf T}\\eta + \\eta L_{ab} = 0')
    w('$$')
    w(symbols(['L', 'delta', 'eta', 'a']))
    w('the generator of $O(4,4)$ in the plane $(a, b)$ (%s). The second relation, with the structure constants of $so(4,4)$, '
      'shows that $S_{ab} \\mapsto L_{ab}$ is an isomorphism of Lie algebras $\\mathrm{span}\\{S_{ab}\\} \\cong so(4,4)$. Since '
      'every $\\exp(\\theta S_{ab})$ lies in Pin(4,4) (next paragraph) and $\\tfrac{\\mathrm{d}}{\\mathrm{d}\\theta}\\exp(\\theta S_{ab})|_0 = S_{ab}$, '
      'the 28 independent $S_{ab}$ lie in the 28-dimensional Lie algebra of Pin(4,4) and are a basis of it: '
      '$spin(4,4) = \\mathrm{span}_{\\mathbb R}\\{S_{ab}\\}$.' % chk('C25_isomorphism_so44'))
    w('')
    w('## The exponentials are products of two unit vectors')
    w('')
    w('$(T_aT_b)^2 = -T_a^2T_b^2 = -\\eta_{aa}\\eta_{bb}I_{16}$ for $a \\ne b$, so the exponential series sums to (%s)'
      % chk('C26_exponentials_two_unit_vectors'))
    w('')
    w('$$')
    w('\\exp(\\theta S_{ab}) = \\begin{cases} \\cos\\tfrac\\theta2\\,I_{16} + \\sin\\tfrac\\theta2\\,T_aT_b, & \\eta_{aa} = \\eta_{bb}\\ \\text{(a rotation)},\\\\'
      ' \\cosh\\tfrac\\theta2\\,I_{16} + \\sinh\\tfrac\\theta2\\,T_aT_b, & \\eta_{aa} = -\\eta_{bb}\\ \\text{(a boost)} \\end{cases}')
    w('$$')
    w(symbols(['S', 'T', 'theta', 'eta', 'In']))
    w('and each is a product $u_1u_2$ of two unit vectors: for $\\eta_{aa} = +1$, $u_1 = T_a$ and $u_2 = \\cos\\tfrac\\theta2T_a + '
      '\\sin\\tfrac\\theta2T_b$ (rotation) or $u_2 = \\cosh\\tfrac\\theta2T_a + \\sinh\\tfrac\\theta2T_b$ (boost); for $\\eta_{aa} = -1$, '
      '$u_1 = -T_a$ and the sign of the $T_b$ term reversed. Hence $\\exp(\\theta S_{ab}) \\in \\mathrm{Spin}(4,4) \\subset \\mathrm{Pin}(4,4)$.')
    w('')
    w('## What the exponentials generate')
    w('')
    w('**Theorem.** The group generated by $\\{\\exp(\\theta S_{ab}) : \\theta \\in \\mathbb R,\\ 0 \\le a < b \\le 7\\}$ is the identity '
      'component $\\mathrm{Spin}_0(4,4)$ of Pin(4,4).')
    w('')
    w('**Proof.** (i) Every $\\exp(\\theta S_{ab})$ is joined to $I_{16}$ by the path $\\theta\' \\mapsto \\exp(\\theta\' S_{ab})$, '
      '$0 \\le \\theta\' \\le \\theta$, inside Pin(4,4), so it and every product of such elements lie in the identity component; '
      'their images $\\rho = \\exp(\\theta L_{ab})$ in $O(4,4)$ have the determinants of both diagonal blocks (the space-like block '
      '$x_0..x_3$ and the time-like block $x_4..x_7$) equal to $+1$ for rotations and $\\cosh\\theta > 0$ for boosts, i.e. they lie in '
      'the identity component $SO_0(4,4)$ (%s). (ii) The map $(\\theta_1, \\dots, \\theta_{28}) \\mapsto \\prod_k\\exp(\\theta_kS_k)$, '
      '$S_k$ running over the 28 basis elements, has at $0$ the differential $(\\theta_k) \\mapsto \\sum_k\\theta_kS_k$, an isomorphism '
      'onto the Lie algebra; by the inverse function theorem its image contains a neighbourhood of $I_{16}$ in '
      '$\\mathrm{Spin}_0(4,4)$. A connected group is generated by any neighbourhood of its identity, so the generated group is all '
      'of $\\mathrm{Spin}_0(4,4)$. $\\square$' % chk('C28_exponentials_in_identity_component'))
    w('')
    w('**The four components of Pin(4,4).** The twisted adjoint images of $I_{16}$, $T_0$, $T_4$ and $T_0T_4$ in $O(4,4)$ have '
      'the following signs of the determinants of the space-like block ($x_0..x_3$) and of the time-like block ($x_4..x_7$) (%s):'
      % chk('C27_pin44_components'))
    w('')
    w('| element $g$ | sign det (space-like block) | sign det (time-like block) | det $\\rho(g)$ | component |')
    w('| --- | --- | --- | --- | --- |')
    comp_name = {'I16': '$\\mathrm{Spin}_0(4,4)$', 'T_0': '$\\mathrm{Spin}_0(4,4)\\,T_0$', 'T_4': '$\\mathrm{Spin}_0(4,4)\\,T_4$',
                 'T_0 T_4': '$\\mathrm{Spin}_0(4,4)\\,T_0T_4$'}
    for k in ('I16', 'T_0', 'T_4', 'T_0 T_4'):
        vv = inv[k]
        w('| $%s$ | %+d | %+d | %+d | %s |' % (k.replace('I16', 'I_{16}').replace('T_0 T_4', 'T_0T_4'), vv[0], vv[1], vv[2], comp_name[k]))
    w('')
    w('The four sign pairs are different, and the block signs are constant on connected pieces of $O(4,4)$, so the four elements '
      'lie in the four different components of Pin(4,4), each of which is a coset of the identity component:')
    w('')
    w('$$')
    w('\\mathrm{Pin}(4,4) = \\mathrm{Spin}_0(4,4)\\ \\cup\\ \\mathrm{Spin}_0(4,4)\\,T_0\\ \\cup\\ \\mathrm{Spin}_0(4,4)\\,T_4\\ \\cup\\ '
      '\\mathrm{Spin}_0(4,4)\\,T_0T_4 = \\big\\langle \\exp(\\theta S_{ab}),\\ T_0,\\ T_4\\big\\rangle')
    w('$$')
    w(symbols(['S', 'T', 'theta']))
    w('($\\langle\\cdots\\rangle$ is the group generated). Spin(4,4) is the union of the first and the last coset. So the scaled '
      'commutators generate Pin(4,4) as its Lie algebra and, through their exponentials, its identity component; the reflections '
      '$T_0$ (space-like) and $T_4$ (time-like) supply the other three components, which no product of exponentials can reach.')
    w('')
    w('**Irreducibility.** The only matrices commuting with all eight $T_a$ are the multiples of $I_{16}$ (%s): $\\mathbb C^{16}$ is an '
      'irreducible representation of Pin(4,4). The matrices commuting with all $S_{ab}$ form the two-dimensional algebra spanned by '
      '$I_{16}$ and $\\Gamma$ (%s); under Spin(4,4) the space splits into the two halves $P_L\\mathbb C^{16}$ and $P_R\\mathbb C^{16}$, '
      'each irreducible, and the two are inequivalent (no non-zero intertwiner; %s).'
      % (chk('C18_pin44_irreducible'), chk('C17_commutant_spin44'), chk('C19_halves_irreducible_inequivalent')))
    w('')

    # ---------------- 8/9. chirality
    w('# Chirality: re-derivation of the projection operators')
    w('')
    w('The author\'s subsection "Left - Handed vs . Right - Handed Fermion Fields (Chirality) ; projection operators" (cells 160 '
      'to 166) reads, verbatim:')
    w('')
    w('```')
    for idx in range(160, 167):
        c = cells[idx]
        t = c.text if c.style != 'Output' else (c.text[:120] + ' ...')
        w('cell %d  %s %s' % (idx, c.style, c.label))
        for line in t.split('\n'):
            if line.strip():
                w('    ' + line)
    w('```')
    w('')
    w('**Step 1: the chirality matrix.** A chirality operator must commute with every Lorentz generator $S_{ab}$ (so that it '
      'is the same in every frame), square to the identity, and not be a multiple of $I_{16}$. The commutant of the $S_{ab}$ is '
      '$\\{xI_{16} + y\\Gamma\\}$ with (%s, %s, %s)' % (chk('C17_commutant_spin44'), chk('C10_chirality_matrix'), chk('C11_chirality_commutes_with_SAB')))
    w('')
    w('$$')
    w('\\Gamma = T_0T_1T_2T_3T_4T_5T_6T_7,\\qquad \\Gamma^2 = (-1)^{8\\cdot7/2}\\,\\eta_{00}\\eta_{11}\\cdots\\eta_{77}\\,I_{16} = I_{16},\\qquad '
      '\\Gamma T_a = -T_a\\Gamma')
    w('$$')
    w(symbols(['Gamma', 'T', 'eta', 'In']))
    w('(moving the eight factors of $\\Gamma\\Gamma$ past each other gives the sign $(-1)^{28} = +1$, and the product of the squares '
      'is $(+1)^4(-1)^4 = +1$; %s). $\\Gamma$ anticommutes with every $T_a$ because $T_a$ anticommutes with the seven other factors '
      'and commutes with itself (seven sign changes). Explicitly (%s)' % (chk('C12_chirality_square_formula'), chk('B8_stored_T16A8')))
    w('')
    w('$$')
    w('\\Gamma = \\begin{pmatrix} -I_8 & 0 \\\\ 0 & I_8 \\end{pmatrix} = %s' % tex_matrix(T[8]))
    w('$$')
    w(symbols(['Gamma', 'In', 'Zn']))
    w('**Step 2: the projectors.** A projector $X = xI_{16} + y\\Gamma$ satisfies $X^2 = X$, i.e. $x^2 + y^2 = x$ and $2xy = y$; '
      'the solutions are $(x, y) = (0, 0)$, $(1, 0)$, $(\\tfrac12, -\\tfrac12)$ and $(\\tfrac12, \\tfrac12)$ (%s). The two non-trivial '
      'ones are the author\'s' % chk('C20_idempotents_of_chirality_algebra'))
    w('')
    w('$$')
    w('P_L = \\tfrac12\\big(I_{16} - \\Gamma\\big) = \\begin{pmatrix} I_8 & 0 \\\\ 0 & 0 \\end{pmatrix},\\qquad '
      'P_R = \\tfrac12\\big(I_{16} + \\Gamma\\big) = \\begin{pmatrix} 0 & 0 \\\\ 0 & I_8 \\end{pmatrix}')
    w('$$')
    w(symbols(['PL', 'Gamma', 'In', 'Zn']))
    w('equal, entry by entry, to the matrices the notebook stored (%s, %s):' % (chk('B9_stored_PL'), chk('B10_stored_PR')))
    w('')
    w('$$')
    w('P_L = %s' % tex_matrix(frac_matrix(PL2, 2)))
    w('$$')
    w('')
    w('$$')
    w('P_R = %s' % tex_matrix(frac_matrix(PR2, 2)))
    w('$$')
    w(symbols(['PL']))
    w('**Step 3: their properties** (%s, %s, %s, %s): the author\'s three tests of cell 165 and more,'
      % (chk('C13_projectors'), chk('C14_projectors_explicit'), chk('C15_projectors_and_gammas'), chk('C16_projectors_and_adjoint')))
    w('')
    w('$$')
    w('\\begin{aligned}')
    w('&P_L + P_R = I_{16},\\quad P_L^2 = P_L,\\quad P_R^2 = P_R,\\quad P_LP_R = P_RP_L = 0,\\quad \\mathrm{Tr}\\,P_L = \\mathrm{Tr}\\,P_R = 8,\\\\')
    w('&P_LT_a = T_aP_R,\\qquad [P_L, S_{ab}] = 0,\\qquad [P_L, \\sigma_{16}] = 0,\\qquad P_L^{\\mathsf T} = P_L')
    w('\\end{aligned}')
    w('$$')
    w(symbols(['PL', 'T', 'S', 'C', 'comm', 'transpose', 'In']))
    w('So the left-handed part $P_L\\Psi$ consists of the components $\\Psi_0, \\dots, \\Psi_7$ and the right-handed part $P_R\\Psi$ '
      'of $\\Psi_8, \\dots, \\Psi_{15}$; each is an irreducible representation of Spin(4,4), the two inequivalent; every Dirac '
      'matrix exchanges them. Two consequences matter for every Lagrangian built with these matrices: because $\\sigma_{16}$ '
      'commutes with $P_L$,')
    w('')
    w('$$')
    w('\\overline{P_L\\Psi} = \\bar\\Psi P_L,\\qquad \\bar\\Psi\\Psi = \\bar\\Psi P_L\\Psi + \\bar\\Psi P_R\\Psi,\\qquad '
      '\\bar\\Psi T_a\\Psi = \\bar\\Psi P_LT_aP_R\\Psi + \\bar\\Psi P_RT_aP_L\\Psi')
    w('$$')
    w(symbols(['Psibar', 'Psi', 'PL', 'T']))
    w('a bilinear with an even number of Dirac matrices (such as the mass term $\\bar\\Psi\\Psi$) never mixes the two chiralities, '
      'while one with an odd number (such as the kinetic term $\\bar\\Psi T_a\\partial\\Psi$) always connects the left-handed with the '
      'right-handed part. In this signature the Dirac adjoint is built with the even matrix $\\sigma_{16}$; in four-dimensional '
      'Minkowski space it is built with the odd $\\gamma^0$, which is why there the mass term mixes the chiralities and the '
      'kinetic term does not.')
    w('')

    # ---------------- 9. others
    w('# Other important $16 \\times 16$ matrices of the notebook')
    w('')
    w('**The complex structure** $J = T_4$ (the author\'s cells 654 to 669): $J^2 = -I_{16}$ and $J^{\\mathsf T}\\sigma_{16}J = \\sigma_{16}$, '
      'the author\'s `In[476]` (%s); the author notes that he uses $x_4$ (not the periodic $x_0$) for it.' % chk('C29_complex_structure_T4'))
    w('')
    w('$$')
    w('J = T_4,\\qquad J^2 = -I_{16},\\qquad J^{\\mathsf T}\\sigma_{16}J = \\sigma_{16}')
    w('$$')
    w(symbols(['J', 'T', 'C', 'transpose', 'In']))
    w('**The product** $T_1T_2T_3T_4T_5T_6$ stored by the author (`Out[489]`) is reproduced (%s); the products $T_4T_5T_6T_7T_a$ are '
      'symmetric (`Out[100]`) and $\\Gamma = \\sigma_{16}T_4T_5T_6T_7$ (`Out[101]`, `Out[498]`), all reproduced (%s).'
      % (chk('B12_stored_T1_to_T6'), chk('B13_stored_boolean_outputs')))
    w('')
    w('**The basis of all real $16 \\times 16$ matrices** is the set of the 256 ordered products of the $T_a$, with '
      '$\\mathrm{Tr}(MM)/16 = \\pm1$ for each (the author\'s `Out[202]`) and 136 symmetric, 120 antisymmetric members (%s).'
      % chk('C30_basis_256'))
    w('')

    # ---------------- 10. stored outputs
    w('# Agreement with every stored output of the matrix cells')
    w('')
    w('The notebook file keeps the outputs that Mathematica computed when the author evaluated the cells. Each was parsed and '
      'compared with the rebuilt matrices (matrices entry by entry; True/False lists value by value):')
    w('')
    w('| cell | label | what | agrees |')
    w('| --- | ------------ | ----------------------------- | ------ |')
    for s in OUT['stored_outputs']:
        w('| %d | `%s` | %s | %s |' % (s['cell'], s['label'], s['what'].replace('|', '\\|'), 'yes' if s['equal'] else 'NO'))
    w('')

    # ---------------- 11. the same matrices
    w('# The same matrices in every calculation')
    w('')
    w('The author asked to verify that the Dirac matrices used in the calculations are those of `4+4.nb`. Every other source '
      'of Dirac matrices in this repository was compared with them, entry by entry:')
    w('')
    w('| source | equal to the $T_a$ of 4+4.nb |')
    w('| ------------------------------ | ---------- |')
    for c in OUT['comparisons']:
        w('| %s | %s |' % (c['source'].replace('|', '\\|'), 'yes, all eight' if c['equal_entry_by_entry'] else 'NO'))
    w('')
    w('`Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb`, the author\'s notebook of the primordial '
      'field, builds the matrices with the same formulas (there $\\tau$ is written directly with the formulas that `4+4.nb` gives to its intermediate $\\zeta$; %s), '
      'and its evaluation by WolframScript in an earlier session gave $T_0, \\dots, T_7$, $\\Gamma$, $\\sigma_{16}$, $P_L$, $P_R$ and all '
      '$S_{ab}$ equal to those of `4+4.nb` (%s). In UM-4 every computation imports its matrices from '
      '`universe_model_4/code/um4_gammas.py`, the cell-by-cell transcription checked here, so UM-4 uses exactly these matrices.'
      % (chk('D2_pair_creation_same_formulas'), chk('D1_pair_creation_extraction')))
    w('')

    # ---------------- 12. reproduce
    w('# How to reproduce')
    w('')
    w('Requirements: Python 3 with sympy (`python -m pip install sympy`); for the PDF, pandoc and a TeX distribution. From the '
      'repository root:')
    w('')
    w('```')
    w('python universe_model_4/code/um4_dirac_matrices.py       # %d checks; writes outputs/dirac_matrices.json and reports/dirac_matrices_checks.json' % ntot)
    w('python universe_model_4/code/um4_dirac_matrices_doc.py   # writes "universe_model_4/dirac matrices.md"')
    w('python universe_model_4/tools/build_docs.py "dirac matrices"   # writes the .tex and the .pdf')
    w('```')
    w('')
    w('The first program needs no Mathematica: it reads the notebook file with `universe_model_4/tools/nb_reader.py`. Its run '
      'time was %.0f s.' % OUT['runtime_s'])
    w('')

    # ---------------- appendix
    w('# Appendix: the 28 generators')
    w('')
    w('Each $2S_{ab} = T_aT_b$ ($a < b$) is a signed permutation matrix; it is listed by its non-zero entries "row:sign column". '
      'Rotations ($\\eta_{aa} = \\eta_{bb}$, 12 of them) satisfy $(T_aT_b)^2 = -I_{16}$, boosts ($\\eta_{aa} = -\\eta_{bb}$, 16) '
      '$(T_aT_b)^2 = +I_{16}$.')
    w('')
    w('$$')
    w('2S_{ab} = T_aT_b\\qquad (0 \\le a < b \\le 7)')
    w('$$')
    w(symbols(['S', 'T', 'a']))
    for key in sorted(S2, key=lambda k: tuple(int(x) for x in k.split(','))):
        a, b = (int(x) for x in key.split(','))
        kind = 'rotation' if eta[a][a] == eta[b][b] else 'boost'
        w('- $2S_{%d%d} = T_%dT_%d$ (%s): %s.' % (a, b, a, b, kind, perm_description(S2[key])))
    w('')
    text = '\n'.join(L) + '\n'
    (UM4 / 'dirac matrices.md').write_text(text, encoding='utf-8')
    print('wrote dirac matrices.md (%d lines, %d characters)' % (len(L), len(text)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
