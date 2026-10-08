#!/usr/bin/env python3
"""Build and verify `provenance/dirac matrices.md`: the eight real 16 x 16 Dirac matrices of the author.

Source of truth: the author's notebook
  Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb (read only).
`extract_from_author_notebook.wls` evaluates the author's own input cells in a fresh Wolfram kernel (in
the author's In[n] order, with the author's Notation-package symbols emulated) and writes
`author_notebook_T16.json`, together with the author's stored outputs and a scan of where the matrices
are assigned and used.  `extract_repository_wolfram_gammas.wls` loads every repository Wolfram package
that builds its own copy of the matrices and writes `repository_wolfram_gammas.json`.  This script
reads both files and proves, in exact arithmetic,

  1. the evaluation reproduces the author's stored outputs, in the author's order;
  2. the eight matrices Gamma_A = T16A[A] (A = 0..7) are real (integer entries -1, 0, 1);
  3. {Gamma_A, Gamma_B} = 2 eta_AB I16 with eta = eta4488 = diag(+1,+1,+1,+1,-1,-1,-1,-1)  (Cl(4,4));
  4. the scaled commutators S^AB = (1/4)[Gamma_A, Gamma_B] close on so(4,4), act on the Gamma_C as
     so(4,4) acts on vectors, and their exponentials (closed forms, checked with sympy) are products
     of two unit vectors; these exponentials generate the identity component Spin_0(4,4) only.  The
     products Gamma_A Gamma_B = 2 S^AB reach a second component (Spin(4,4)); one Dirac matrix is
     needed for the two odd components of Pin(4,4) (component invariants computed exactly);
  5. the products (sigma16, T16A[8], all 256 ordered basis products), the projectors P_L, P_R,
     (I16 +- sigma16)/2 and the Krein matrix B = -i sigma16 Gamma_4 with (I16 +- B)/2 have the stated
     properties;
  6. where the author's Lagrangians and field equations use the matrices (scan of the notebook);
  7. every other copy of the matrices in the repository (JSON fixtures and reports, Python, Wolfram and
     Rust constructions, Revision and earlier stages) equals these entry by entry.

Every check is exact (Python integers / fractions.Fraction); the Clifford relation and the so(4,4)
closure are re-evaluated with sympy as a second engine, and the exponentials are verified
symbolically with sympy.  The run stops with exit code 1 if any check fails; the Markdown file is
written only when every check passes.  Output is deterministic (LF line endings, no time stamps) and
depends only on the files compared, never on a directory listing.

Usage (from the repository root):
  wolframscript -file provenance/dirac_matrices/extract_from_author_notebook.wls
  wolframscript -file provenance/dirac_matrices/extract_repository_wolfram_gammas.wls
  python provenance/dirac_matrices/build_dirac_matrices_md.py                    # check and write
  python provenance/dirac_matrices/build_dirac_matrices_md.py --check            # check and compare, write nothing
  python provenance/dirac_matrices/build_dirac_matrices_md.py --list-consumers   # print the files that read gammas.json
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import re
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import sympy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NB_JSON = HERE / "author_notebook_T16.json"
WL_JSON = HERE / "repository_wolfram_gammas.json"
OUT = ROOT / "provenance" / "dirac matrices.md"
NOTEBOOK = "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"

N = 16
IDX = range(8)
# author's coordinate x_k (k = 1..8) -> notebook index A (Revision/SPEC.md section 2)
COORD_OF_A = {0: "x8", 1: "x1", 2: "x2", 3: "x3", 4: "x4", 5: "x5", 6: "x6", 7: "x7"}
ROLE_OF_A = {0: "hidden space-like direction", 1: "space", 2: "space", 3: "space",
             4: "time", 5: "extra time, deflates exponentially", 6: "extra time, deflates exponentially",
             7: "extra time, deflates exponentially"}
COORD_TO_A = [1, 2, 3, 4, 5, 6, 7, 0]  # x1..x8 -> notebook index A


# --------------------------------------------------------------------------- exact helpers
def zeros(n=N, m=None):
    return [[0] * (n if m is None else m) for _ in range(n)]


def ident(n=N):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = [[0] * m for _ in range(n)]
    for i in range(n):
        for t in range(k):
            x = a[i][t]
            if x:
                bt = b[t]
                oi = out[i]
                for j in range(m):
                    if bt[j]:
                        oi[j] += x * bt[j]
    return out


def mulall(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = mul(out, m)
    return out


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scal(c, a):
    return [[c * x for x in r] for r in a]


def tr(a):
    return [list(r) for r in zip(*a)]


def eq(a, b):
    return (len(a) == len(b) and all(len(r) == len(s) for r, s in zip(a, b))
            and all(x == y for r, s in zip(a, b) for x, y in zip(r, s)))


def is_zero(a):
    return all(x == 0 for r in a for x in r)


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def comm(a, b):
    return sub(mul(a, b), mul(b, a))


def anti(a, b):
    return add(mul(a, b), mul(b, a))


def lin_comb(coeffs, mats):
    out = zeros(len(mats[0]))
    for c, m in zip(coeffs, mats):
        if c:
            out = add(out, scal(c, m))
    return out


def rank(rows):
    """Exact rank of a list of equal-length rows (Fraction Gaussian elimination)."""
    m = [[Fraction(x) for x in r] for r in rows]
    rk, col, ncol = 0, 0, len(m[0]) if m else 0
    while rk < len(m) and col < ncol:
        piv = next((i for i in range(rk, len(m)) if m[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        m[rk], m[piv] = m[piv], m[rk]
        p = m[rk][col]
        m[rk] = [x / p for x in m[rk]]
        for i in range(len(m)):
            if i != rk and m[i][col] != 0:
                f = m[i][col]
                m[i] = [x - f * y for x, y in zip(m[i], m[rk])]
        rk += 1
        col += 1
    return rk


def fdet(a):
    """Exact determinant (Fraction Gaussian elimination)."""
    m = [[Fraction(x) for x in r] for r in a]
    n, d = len(m), Fraction(1)
    for c in range(n):
        piv = next((i for i in range(c, n) if m[i][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            d = -d
        d *= m[c][c]
        for i in range(c + 1, n):
            if m[i][c] != 0:
                f = m[i][c] / m[c][c]
                m[i] = [x - f * y for x, y in zip(m[i], m[c])]
    return d


def sign(x):
    return (x > 0) - (x < 0)


def frac_matrix(m):
    """JSON matrix with integers or "p/q" strings -> Fraction matrix."""
    return [[Fraction(str(v)) for v in r] for r in m]


def int_matrix(m):
    out = []
    for r in m:
        row = []
        for v in r:
            f = Fraction(str(v)) if not isinstance(v, float) else Fraction(v)
            if f.denominator != 1:
                raise ValueError("non-integer entry")
            row.append(int(f))
        out.append(row)
    return out


def blocks_of(m, h=8):
    return ([r[:h] for r in m[:h]], [r[h:] for r in m[:h]], [r[:h] for r in m[h:]], [r[h:] for r in m[h:]])


# signed permutation matrices as (perm, signs): row i has signs[i] in column perm[i]
def to_sp(m):
    perm, sg = [], []
    for r in m:
        nz = [(j, x) for j, x in enumerate(r) if x]
        if len(nz) != 1 or nz[0][1] not in (1, -1):
            return None
        perm.append(nz[0][0])
        sg.append(nz[0][1])
    return tuple(perm), tuple(sg)


def sp_mul(p, q):
    pp, ps = p
    qp, qs = q
    return tuple(qp[pp[i]] for i in range(len(pp))), tuple(ps[i] * qs[pp[i]] for i in range(len(pp)))


def sp_inv(p):
    pp, ps = p
    ip, isg = [0] * len(pp), [0] * len(pp)
    for i, (j, s) in enumerate(zip(pp, ps)):
        ip[j], isg[j] = i, s
    return tuple(ip), tuple(isg)


def sp_neg(p):
    return p[0], tuple(-s for s in p[1])


def sp_to_mat(p):
    m = zeros(len(p[0]))
    for i, (j, s) in enumerate(zip(*p)):
        m[i][j] = s
    return m


# complex matrices as (real part, imaginary part)
def cmul(a, b):
    return sub(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))


def ceq(a, b):
    return eq(a[0], b[0]) and eq(a[1], b[1])


def rust_const(text, name):
    """The value of `pub const NAME: ... = [...];` in a generated Rust file, as nested lists of numbers."""
    i = text.index(f"pub const {name}:")
    k = text.index("[", text.index("=", i))
    depth = 0
    for pos in range(k, len(text)):
        if text[pos] == "[":
            depth += 1
        elif text[pos] == "]":
            depth -= 1
            if depth == 0:
                break
    body = re.sub(r"//[^\n]*", "", text[k:pos + 1])
    return json.loads(re.sub(r",\s*\]", "]", body))


# --------------------------------------------------------------------------- check registry
CHECKS: list[tuple[str, bool, str]] = []


def check(name, ok, detail):
    CHECKS.append((name, bool(ok), detail))
    if not ok:
        print(f"FAIL {name}: {detail}")
    return ok


# --------------------------------------------------------------------------- display helpers
def fmt_matrix(m):
    def cell(x):
        x = Fraction(x)
        s = str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
        return s.rjust(4 if any(Fraction(y).denominator != 1 for r in m for y in r) else 2)
    return "\n".join("[" + " ".join(cell(x) for x in r) + " ]" for r in m)


def signed_perm(m):
    """One-line form of a signed permutation matrix: entry i is +-j (row i has +-1 in column j)."""
    out = []
    for r in m:
        nz = [(j, x) for j, x in enumerate(r) if x]
        assert len(nz) == 1 and nz[0][1] in (1, -1)
        j, x = nz[0]
        out.append(("+" if x > 0 else "-") + str(j + 1))
    return " ".join(s.rjust(3) for s in out)


def cells_text(cells, labels):
    return ", ".join(f"{c} ({labels.get(str(c), '?')})" for c in cells)


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def list_consumers():
    """Files under Revision/, tests/ and scripts/ that mention gammas.json (live listing, NOT part of the .md)."""
    return sorted(str(p.relative_to(ROOT)).replace("\\", "/")
                  for base in ("Revision", "tests", "scripts")
                  for p in (ROOT / base).rglob("*")
                  if p.suffix in (".py", ".wl", ".wls", ".rs") and p.is_file()
                  and "gammas.json" in p.read_text(encoding="utf-8", errors="ignore"))


# role of each cell of the author's chain (the assignments and uses are measured by the .wls scan)
CHAIN_ROLE = {
    43: "the field: Psi16 = (f16[i][x0, x4]), i = 0..15: sixteen ordinary (commuting) functions",
    285: "sigma16 = T16A[0].T16A[1].T16A[2].T16A[3] (the bilinear form)",
    286: "the eight Dirac matrices T16A[0..7]",
    314: "the author's own check of {T16A[A1], T16A[B1]} = 2 eta4488 ID16 (stored output: 64 x True)",
    325: "the author's check of P_L + P_R = ID16, P_L^2 = P_L, P_L P_R = P_R P_L = 0 (stored output: {True, True, True})",
    326: "SAB = (1/4)[T16A[A1], T16A[B1]]: the scaled commutators (spin connection term)",
    361: "the curved matrices T16alpha[alpha] = sum_A e_A^alpha T16A[A] (vielbein times T16A)",
    362: "T16alpha[8] = T16alpha[0]...T16alpha[7]",
    367: "the author's check (1/2){T16alpha, T16beta} = g^(alpha beta) ID16 (curved Clifford relation)",
    451: "lists of the products of T16A (t16A, t16AB, ...)",
    453: "base16 = the 256 basis products of T16A",
    479: "the author's check T16A[8] == base16[[255]][[1]]",
    821: "usegT16 = simplified T16alpha",
    822: "useT16 = T16alpha on the author's metric (substitution ssgm4488)",
    828: "Lg[] = sqrt(det g) Psi16^T sigma16 T16alpha (d Psi16 + (Q1/2) omega SAB Psi16) + ...: the Lagrangian with T16alpha",
    830: "La[] = useDSQRT Psi16^T sigma16 useT16 (d Psi16 + (Q1/2) omega SAB Psi16) + H M Psi16^T sigma16 Psi16: the Lagrangian used for the field equations",
    836: "Lj[j] = Lagrangian with useT16, SAB and the basis product base16[[j]]",
    839: "eL[L, sqrt] = Euler-Lagrange equations of L with respect to the sixteen f16[k]",
    841: "eLa = eL[La, useDSQRT]: the field equations of La",
}
CHAIN_EXPECT = {  # cell -> (assigns, uses): measured by the .wls scan; the check compares
    43: (["Psi16"], ["Psi16"]),
    285: (["sigma16"], ["sigma16", "T16A"]),
    286: (["T16A"], ["T16A"]),
    326: (["SAB"], ["T16A", "SAB"]),
    361: (["T16alpha"], ["T16A", "T16alpha"]),
    822: (["useT16"], ["T16alpha", "useT16"]),
    453: (["base16"], ["base16"]),
    828: (["Lg"], ["sigma16", "T16alpha", "SAB", "Psi16", "Lg"]),
    830: (["La"], ["sigma16", "SAB", "useT16", "Psi16", "La"]),
    836: (["Lj"], ["sigma16", "SAB", "useT16", "base16", "Psi16", "Lj"]),
    839: (["eL"], ["eL"]),
    841: (["eLa"], ["La", "eL", "eLa"]),
}
ASSIGN_EXPECT = {"sigma16": [285], "T16A": [286, 287], "T16alpha": [361, 362], "SAB": [326], "useT16": [822],
                 "base16": [453], "Psi16": [43], "Lg": [828], "La": [830], "Lj": [836], "eL": [839],
                 "eLa": [841], "P_L": [323], "P_R": [324]}


# --------------------------------------------------------------------------- main
def main():
    if "--list-consumers" in sys.argv:
        files = list_consumers()
        print(f"files under Revision/, tests/ and scripts/ that mention gammas.json ({len(files)}):")
        for f in files:
            print(f"  {f}")
        return 0
    for f, cmd in ((NB_JSON, "extract_from_author_notebook.wls"), (WL_JSON, "extract_repository_wolfram_gammas.wls")):
        if not f.exists():
            print(f"ERROR: {f.relative_to(ROOT)} not found; run {cmd} first")
            return 1
    nbd = json.loads(NB_JSON.read_text(encoding="utf-8"))
    wl = json.loads(WL_JSON.read_text(encoding="utf-8"))
    labels = nbd["labels"]
    G = [[[int(x) for x in r] for r in m] for m in nbd["T16A"]]
    eta8 = [[int(x) for x in r] for r in nbd["eta4488"]]
    eta = [eta8[A][A] for A in IDX]
    sigma16 = nbd["sigma16"]
    T8 = nbd["T16A_8"]
    tau = nbd["tau"]
    taubar = nbd["taubar"]
    sigma8 = nbd["sigma8"]
    PL = [[Fraction(x, 2) for x in r] for r in nbd["twice_PL"]]
    PR = [[Fraction(x, 2) for x in r] for r in nbd["twice_PR"]]
    I = ident()
    M5 = mul(sigma16, G[4])          # B = -i M5
    negM5 = scal(-1, M5)

    # ---- 0. the author's notebook: environment, order, stored outputs
    check("eta4488_diagonal_4_4",
          eta == [1, 1, 1, 1, -1, -1, -1, -1] and all(eta8[A][B] == 0 for A in IDX for B in IDX if A != B),
          f"eta4488 from author input cell 41 ({labels['41']}) = diag{tuple(eta)}: signature (4,4)")
    plan_labels = [int(c["label"][3:-1]) for c in nbd["cells"]]
    order_cells = [c["input_cell"] for c in nbd["cells"]]
    out370 = nbd["stored_Out370"]["text"]
    check("author_evaluation_order",
          plan_labels == sorted(plan_labels) and len(set(plan_labels)) == len(plan_labels)
          and order_cells.index(285) < order_cells.index(286)
          and nbd["sigma16_symbolic_after_cell_285"] is True
          and out370 == "HoldForm[T16A[0] . T16A[1] . T16A[2] . T16A[3]]",
          f"the {len(order_cells)} author input cells are evaluated in the author's order of In[n] labels "
          f"({plan_labels[0]} .. {plan_labels[-1]}, strictly increasing); input cell 285 ({labels['285']}, sigma16) "
          f"precedes 286 ({labels['286']}, T16A); the author's stored {nbd['stored_Out370']['out_label']} is the "
          f"unevaluated product {out370[9:-1]}, and right after cell 285 sigma16 holds that symbolic product here too")
    nt = nbd["notation"]
    check("notation_emulation",
          [c["input_cell"] for c in nt["cells"]] == [51, 54, 55, 56, 477]
          and "HoldForm[Symbol]" in nt["taubar_head_check"]["stored_outputs"]
          and nt["taubar_atomic"] is True and nt["OverBar_SubValues_empty"] is True
          and nt["emulated_names"]["T16A"] == "T16⎵Superscript⎵A",
          "the author loads Notation` (input cell 51, " + labels["51"] + ") and Symbolizes taubar, T16^A and T16^alpha "
          f"(input cells 54, 55, 56: {labels['54']}, {labels['55']}, {labels['56']}); the notebook records the "
          f"symbol name T16[UnderBracket]Superscript[UnderBracket]A (input cell 477, {labels['477']}) and the "
          f"author's Head check of taubar (input cell 248, {labels['248']}) printed Symbol. The emulation uses that "
          "same atomic name for T16^A and an atomic stand-in for taubar: taubar[0..7] are 8 DownValues of one "
          "symbol and System`OverBar has no SubValues, as in the author's kernel")
    so = {(s["input_cell"]): s for s in nbd["stored_outputs"]}
    expect = {257: [[2 * x for x in r] for r in tau[7]], 287: scal(2, T8), 288: scal(2, sigma16),
              298: scal(2, sigma16), 323: nbd["twice_PL"], 324: nbd["twice_PR"]}
    o393 = nbd["stored_Out393"]
    check("author_stored_outputs",
          sorted(so) == sorted(expect) and all(eq(so[c]["twice_matrix"], expect[c]) for c in expect)
          and nbd["stored_Out406"]["text"] == "HoldForm[{True, True, True}]"
          and o393["true"] == 64 and o393["false"] == 0,
          "the author's stored outputs equal the evaluated values entry by entry: "
          + "; ".join(f"{so[c]['out_label']} (input cell {c}) = {so[c]['what']}" for c in sorted(so))
          + f"; {nbd['stored_Out406']['out_label']} (input cell 325, the author's projector check) = "
            f"{{True, True, True}}; {o393['out_label']} (input cell 314, the author's check of "
            f"{{T16A[A1], T16A[B1]}} = 2 eta4488 ID16) shows {o393['true']} x True and {o393['false']} x False")
    tau_ok = (eq(tau[0], ident(8)) and eq(taubar[0], ident(8))
              and all(eq(taubar[A], mulall(sigma8, tr(tau[A]), sigma8)) for A in range(1, 8))
              and all(eq(G[A], [list(r) + list(s) for r, s in zip(zeros(8), taubar[A])]
                         + [list(r) + list(s) for r, s in zip(tau[A], zeros(8))]) for A in IDX)
              and eq(tau[7], mulall(*tau[1:7])))
    check("construction_tau_taubar", tau_ok,
          "tau[0] = taubar[0] = I8, tau[7] = tau[1]...tau[6], taubar[A] = sigma tau[A]^T sigma (A = 1..7) and "
          "T16A[A] = {{0, taubar[A]}, {tau[A], 0}} (A = 0..7), with the evaluated tau, taubar and sigma of the author's cells")

    # ---- 1. reality
    entries = sorted({x for m in G for r in m for x in r})
    check("eight_16x16", len(G) == 8 and all(len(m) == 16 and all(len(r) == 16 for r in m) for m in G),
          "exactly eight matrices, each 16 x 16")
    check("real_integer_entries", entries == [-1, 0, 1],
          f"the set of all entries of the eight matrices is {entries}: every entry is a real integer")
    check("signed_permutation", all(sum(1 for x in r if x) == 1 for m in G for r in m)
          and all(sum(1 for r in m if r[j]) == 1 for m in G for j in range(N)),
          "each Gamma_A has exactly one nonzero entry (+1 or -1) in every row and every column")
    check("orthogonal", all(eq(mul(tr(m), m), I) for m in G), "Gamma_A^T Gamma_A = I16 for every A")
    sym = [A for A in IDX if eq(tr(G[A]), G[A])]
    asym = [A for A in IDX if eq(tr(G[A]), scal(-1, G[A]))]
    check("transpose_pattern", sym == [0, 1, 2, 3] and asym == [4, 5, 6, 7],
          f"symmetric: A = {sym} (eta = +1); antisymmetric: A = {asym} (eta = -1); so Gamma_A^T = eta_AA Gamma_A")

    # ---- 2. anticommutation (own integers + sympy)
    bad = [(A, B) for A in IDX for B in IDX if not eq(anti(G[A], G[B]), scal(2 * eta8[A][B], I))]
    check("clifford_anticommutation", not bad,
          "{Gamma_A, Gamma_B} = Gamma_A Gamma_B + Gamma_B Gamma_A = 2 eta_AB I16 for all 64 ordered pairs "
          f"(integer arithmetic){'' if not bad else f'; failures {bad}'}")
    sG = [sympy.Matrix(m) for m in G]
    bad_s = [(A, B) for A in IDX for B in IDX if sG[A] * sG[B] + sG[B] * sG[A] != 2 * eta8[A][B] * sympy.eye(N)]
    check("clifford_anticommutation_sympy", not bad_s, "the same 64 relations re-evaluated with sympy.Matrix")
    squares = ["+I16" if eq(mul(G[A], G[A]), I) else "-I16" if eq(mul(G[A], G[A]), scal(-1, I)) else "?"
               for A in IDX]
    check("squares", squares == ["+I16"] * 4 + ["-I16"] * 4,
          f"Gamma_A^2 for A = 0..7: {squares}")

    # ---- 3. products: all 256 ordered basis products
    subsets = [s for k in range(9) for s in itertools.combinations(IDX, k)]
    prods = {s: (mulall(*[G[A] for A in s]) if s else I) for s in subsets}
    gram_ok = all(trace(mul(tr(prods[s]), prods[t])) == (16 if s == t else 0) for s in subsets for t in subsets)
    check("256_products_orthonormal", len(subsets) == 256 and gram_ok,
          "the 256 products P_s = Gamma_{A1}...Gamma_{Ak} (s = {A1 < ... < Ak}, k = 0..8) are signed permutation "
          "matrices with tr(P_s^T P_t) = 16 delta_st: they are linearly independent, so they form a basis of the "
          "256-dimensional space of real 16 x 16 matrices: Cl(4,4) = M16(R)")
    spG = [to_sp(g) for g in G]
    spP = {s: to_sp(prods[s]) for s in subsets}
    eps = {}
    conj_ok = True
    for s in subsets:
        for A in IDX:
            y = sp_mul(sp_mul(spG[A], spP[s]), sp_inv(spG[A]))
            eps[(A, s)] = 1 if y == spP[s] else -1 if y == sp_neg(spP[s]) else 0
            conj_ok &= eps[(A, s)] != 0
    commuting = [s for s in subsets if all(eps[(A, s)] == 1 for A in IDX)]
    anticommuting = [s for s in subsets if all(eps[(A, s)] == -1 for A in IDX)]
    check("irreducible_commutant",
          conj_ok and commuting == [()],
          "X Gamma_A = Gamma_A X solved exactly: Gamma_A P_s Gamma_A^-1 = +-P_s for all 8 x 256 pairs (computed), so for "
          "X = sum_s c_s P_s (basis of `256_products_orthonormal`) X commutes with every Gamma_A iff c_s = 0 whenever P_s "
          f"anticommutes with some Gamma_A; the products commuting with all eight are {['I16' if not s else s for s in commuting]}: "
          "the commutant is R I16 (dimension 1). The representation is irreducible because the Gamma_A generate all of "
          "M16(R) (`256_products_orthonormal`) and M16(R) v = R^16 for every nonzero v (no Schur argument is needed)")
    check("anticommutant_T16A8",
          conj_ok and anticommuting == [tuple(IDX)],
          "X Gamma_A = -Gamma_A X for all A: the only basis product anticommuting with all eight Gamma_A is "
          f"P_{anticommuting[0] if anticommuting else '?'} = T16A[8], which is even (a product of eight Gamma's): the "
          "anticommutant is R T16A[8] and contains no nonzero odd element")
    even = [s for s in subsets if len(s) % 2 == 0]
    T8sp = to_sp(T8)
    blockdiag = all(sp_mul(spP[s], T8sp) == sp_mul(T8sp, spP[s]) for s in even)
    ul = [[x for r in blocks_of(prods[s])[0] for x in r] for s in even]
    lr = [[x for r in blocks_of(prods[s])[3] for x in r] for s in even]
    rk_ul, rk_lr = rank(ul), rank(lr)
    check("even_part_two_halves",
          len(even) == 128 and blockdiag and rk_ul == 64 and rk_lr == 64,
          f"the {len(even)} even basis products all commute with T16A[8] = diag(-I8, I8), so they are block diagonal "
          f"diag(a, b) and leave each chiral half invariant; their upper-left 8 x 8 blocks span a space of exact rank "
          f"{rk_ul} and their lower-right blocks rank {rk_lr} = dim M8(R): the even subalgebra (spanned by the products of "
          "the S^AB, i.e. by Spin_0(4,4)) is M8(R) + M8(R), so each chiral half is irreducible under Spin_0(4,4), and the "
          "halves are inequivalent because the even element T16A[8] acts as -1 on one and +1 on the other (Revision/SPEC.md "
          "section 2: commutant dimension 2, intertwiner dimension 0)")
    check("sigma16_product", eq(sigma16, mulall(G[0], G[1], G[2], G[3])),
          f"sigma16 (author input cell 285, {labels['285']}) = Gamma_0 Gamma_1 Gamma_2 Gamma_3")
    check("T16A8_product", eq(T8, mulall(*G)),
          f"T16A[8] (author input cell 287, {labels['287']}) = Gamma_0 Gamma_1 ... Gamma_7")
    check("T16A8_chirality", eq(mul(T8, T8), I) and all(is_zero(anti(T8, g)) for g in G)
          and eq(T8, [[(-1 if i < 8 else 1) if i == j else 0 for j in range(N)] for i in range(N)]),
          "T16A[8]^2 = I16, T16A[8] anticommutes with every Gamma_A, and T16A[8] = diag(-I8, I8)")
    check("sigma16_properties", eq(tr(sigma16), sigma16) and eq(mul(sigma16, sigma16), I)
          and all(eq(tr(mul(sigma16, g)), scal(-1, mul(sigma16, g))) for g in G),
          "sigma16 is symmetric, sigma16^2 = I16, and sigma16 Gamma_A is antisymmetric for every A")

    # ---- 4. scaled commutators S^AB, Spin_0(4,4), Spin(4,4), Pin(4,4)
    pairs = [(A, B) for A in IDX for B in IDX if A < B]
    S = {}
    for A in IDX:
        for B in IDX:
            S[(A, B)] = [[Fraction(x, 4) for x in r] for r in comm(G[A], G[B])]
    ok = all(eq(S[(A, B)], [[Fraction(x, 2) for x in r] for r in mul(G[A], G[B])]) for A, B in pairs)
    ok = ok and all(eq(S[(A, B)], scal(-1, S[(B, A)])) for A in IDX for B in IDX)
    check("S_definition", ok, "S^AB = (1/4)[Gamma_A, Gamma_B] = (1/2) Gamma_A Gamma_B for A != B, S^BA = -S^AB: "
          "28 independent pairs A < B. Only the S^AB are called the scaled commutators below; they are Lie-algebra "
          "elements, while the matrices Gamma_A Gamma_B = 2 S^AB are group elements")
    sab = nbd["four_SAB"]
    check("author_SAB_cell_326", all(eq([[Fraction(x, 4) for x in r] for r in sab[A][B]], S[(A, B)]) for A in IDX for B in IDX),
          f"the author's SAB (input cell 326, {labels['326']}: SAB = Table[(1/4)(T16A[A1].T16A[B1] - T16A[B1].T16A[A1])]), "
          "evaluated from the notebook, equals S^AB entry by entry for all 64 (A, B)")
    check("S_linearly_independent", rank([[x for r in S[p] for x in r] for p in pairs]) == 28,
          "the 28 matrices S^AB (A < B) have exact rank 28: dim = 28 = dim so(4,4)")

    def eta_(a, b):
        return eta8[a][b]

    bad = 0
    bad_s = 0
    sS = {p: sympy.Matrix(S[p]) for p in S}
    for (a, b), (c, d) in itertools.product(pairs, pairs):
        lhs = comm(S[(a, b)], S[(c, d)])
        rhs = zeros()
        for coef, key in ((eta_(b, c), (a, d)), (-eta_(a, c), (b, d)), (-eta_(b, d), (a, c)), (eta_(a, d), (b, c))):
            if coef:
                rhs = add(rhs, scal(coef, S[key]))
        bad += not eq(lhs, rhs)
        rs = (eta_(b, c) * sS[(a, d)] - eta_(a, c) * sS[(b, d)] - eta_(b, d) * sS[(a, c)] + eta_(a, d) * sS[(b, c)])
        bad_s += (sS[(a, b)] * sS[(c, d)] - sS[(c, d)] * sS[(a, b)]) != rs
    check("so44_closure", bad == 0 and bad_s == 0,
          "[S^AB, S^CD] = eta_BC S^AD - eta_AC S^BD - eta_BD S^AC + eta_AD S^BC for all 28 x 28 pairs "
          f"(integer/Fraction arithmetic: {bad} failures; sympy: {bad_s} failures): the S^AB span the Lie "
          "algebra so(4,4)")

    # vector action: [S^AB, Gamma_C] = eta_BC Gamma_A - eta_AC Gamma_B  ->  8 x 8 matrices M^AB
    M = {}
    bad = []
    for p in pairs:
        A, B = p
        m8 = [[0] * 8 for _ in IDX]  # column C holds the coefficients of [S^AB, Gamma_C] on Gamma_D
        for C in IDX:
            lhs = comm(S[p], G[C])
            coeffs = [Fraction(0)] * 8
            coeffs[A] += eta_(B, C)
            coeffs[B] -= eta_(A, C)
            if not eq(lhs, lin_comb(coeffs, G)):
                bad.append((p, C))
            for D in IDX:
                m8[D][C] = coeffs[D]
        M[p] = m8
    check("S_vector_action", not bad,
          "[S^AB, Gamma_C] = eta_BC Gamma_A - eta_AC Gamma_B for all 28 pairs and all 8 C: the commutator "
          "with S^AB maps the span of the Gamma's to itself by the 8 x 8 matrix M^AB")
    eta_m = [[eta_(i, j) for j in IDX] for i in IDX]
    check("M_in_so44", all(is_zero(add(mul(tr(M[p]), eta_m), mul(eta_m, M[p]))) for p in pairs),
          "(M^AB)^T eta + eta M^AB = 0 for every pair: every M^AB lies in so(4,4) = {X : X^T eta + eta X = 0}")
    rows = []
    for i in IDX:
        for j in IDX:
            row = [0] * 64
            row[j * 8 + i] += eta_(j, j)   # (X^T eta)_ij = X_ji eta_jj
            row[i * 8 + j] += eta_(i, i)   # (eta X)_ij = eta_ii X_ij
            rows.append(row)
    dim_so = 64 - rank(rows)
    check("M_basis_of_so44", dim_so == 28 and rank([[x for r in M[p] for x in r] for p in pairs]) == 28,
          f"so(4,4) has dimension {dim_so} (exact rank of its 64 linear conditions) and the 28 M^AB are "
          "linearly independent: they form a basis of so(4,4)")
    hom_bad = 0
    for (a, b), (c, d) in itertools.product(pairs, pairs):
        lhs = sub(mul(M[(a, b)], M[(c, d)]), mul(M[(c, d)], M[(a, b)]))

        def Mk(x, y):
            return M[(x, y)] if x < y else scal(-1, M[(y, x)]) if x > y else [[0] * 8 for _ in IDX]
        rhs = [[0] * 8 for _ in IDX]
        for coef, (x, y) in ((eta_(b, c), (a, d)), (-eta_(a, c), (b, d)), (-eta_(b, d), (a, c)), (eta_(a, d), (b, c))):
            if coef:
                rhs = add(rhs, scal(coef, Mk(x, y)))
        hom_bad += not eq(lhs, rhs)
    check("spin_to_so_isomorphism", hom_bad == 0,
          "the M^AB satisfy the same commutation relations as the S^AB (28 x 28 pairs, "
          f"{hom_bad} failures): S^AB -> M^AB is a Lie-algebra isomorphism spin(4,4) -> so(4,4)")

    # invariant bilinears and chirality
    s_real = all(isinstance(x, Fraction) for p in pairs for r in S[p] for x in r)
    check("S_preserves_sigma16",
          s_real and all(is_zero(add(mul(tr(S[p]), sigma16), mul(sigma16, S[p]))) for p in pairs),
          "(S^AB)^T sigma16 + sigma16 S^AB = 0 for all 28 pairs, and every S^AB is real (rational entries), so also "
          "(S^AB)^dagger sigma16 + sigma16 S^AB = 0: both the author's bilinear Psi^T sigma16 Psi and the Dirac bilinear "
          "Psibar Psi = Psi^dagger sigma16 Psi of Revision/SPEC.md (C = sigma16) are invariant under Spin_0(4,4), the group "
          "generated by the exp(theta S^AB). Because sigma16 is symmetric (`sigma16_properties`), Psi^T sigma16 Psi vanishes "
          "identically for anticommuting (Grassmann) components; it is nontrivial only for commuting fields (the author's "
          "Psi16, input cell 43, and Phi of dirac16complex00). The boost products Gamma_A Gamma_B map sigma16 to -sigma16 "
          "(`products_components`)")
    check("S_commute_with_T16A8", all(is_zero(comm(T8, S[p])) for p in pairs),
          "[T16A[8], S^AB] = 0: the chiral halves P_L Psi and P_R Psi are invariant under Spin_0(4,4)")

    # exponentials: closed forms, symbolic proof with sympy
    th, ph = sympy.symbols("theta phi", real=True)
    n_rot = n_boost = 0
    exp_ok = vec_ok = lemma_ok = pin_ok = cover_ok = sig_ok = True
    for p in pairs:
        A, B = p
        K = mul(G[A], G[B])          # = 2 S^AB
        s = eta[A] * eta[B]          # K^2 = -s I
        if not eq(mul(K, K), scal(-s, I)):
            exp_ok = False
            continue
        if s == 1:
            n_rot += 1
            c, sn = sympy.cos(th / 2), sympy.sin(th / 2)
        else:
            n_boost += 1
            c, sn = sympy.cosh(th / 2), sympy.sinh(th / 2)
        # g(theta) = c I + sn K.  (i) g(0) = I; (ii) dg/dtheta = S^AB g  <=>  c' = -s sn / 2, sn' = c / 2
        exp_ok &= c.subs(th, 0) == 1 and sn.subs(th, 0) == 0
        exp_ok &= sympy.simplify(sympy.diff(c, th) + s * sn / 2) == 0 and sympy.simplify(sympy.diff(sn, th) - c / 2) == 0
        # (iii) g(theta) g(phi) = g(theta + phi): coefficient identities using K^2 = -s I
        c2, s2 = c.subs(th, ph), sn.subs(th, ph)
        c3, s3 = c.subs(th, th + ph), sn.subs(th, th + ph)
        exp_ok &= sympy.simplify(sympy.expand_trig(c * c2 - s * sn * s2 - c3)) == 0
        exp_ok &= sympy.simplify(sympy.expand_trig(c * s2 + sn * c2 - s3)) == 0
        # vector action at group level: g Gamma_C g^-1 = sum_D Lambda_DC Gamma_D, g^-1 = c I - sn K
        KC_comm = {C: comm(K, G[C]) for C in IDX}
        KCK = {C: mulall(K, G[C], K) for C in IDX}
        Lam = sympy.zeros(8, 8)
        for C in IDX:
            # g G_C g^-1 = c^2 G_C + c sn [K, G_C] - sn^2 K G_C K ; decompose each on the Gamma's
            for D in IDX:
                cD_comm = Fraction(trace(mul(tr(G[D]), KC_comm[C])), 16)
                cD_kck = Fraction(trace(mul(tr(G[D]), KCK[C])), 16)
                Lam[D, C] = (c ** 2 * int(D == C) + c * sn * sympy.Rational(cD_comm.numerator, cD_comm.denominator)
                             - sn ** 2 * sympy.Rational(cD_kck.numerator, cD_kck.denominator))
            recon = sum(([sympy.Matrix(G[D]) * Lam[D, C] for D in IDX]), sympy.zeros(N, N))
            direct = (c * sympy.eye(N) + sn * sympy.Matrix(K)) * sympy.Matrix(G[C]) * (c * sympy.eye(N) - sn * sympy.Matrix(K))
            vec_ok &= sympy.expand(recon - direct) == sympy.zeros(N, N)
        Lam = Lam.applyfunc(sympy.simplify)
        Mm = sympy.Matrix(M[p])
        vec_ok &= sympy.simplify(Lam.diff(th) - Mm * Lam) == sympy.zeros(8, 8)          # Lambda = exp(theta M^AB)
        vec_ok &= Lam.subs(th, 0) == sympy.eye(8)
        vec_ok &= sympy.simplify(Lam.T * sympy.Matrix(eta_m) * Lam - sympy.Matrix(eta_m)) == sympy.zeros(8, 8)
        # Lemma A on Lambda(theta): A^T A = I4 + C^T C and D^T D = I4 + B^T B (space block = directions 0..3)
        La_, Lb_, Lc_, Ld_ = Lam[:4, :4], Lam[:4, 4:], Lam[4:, :4], Lam[4:, 4:]
        lemma_ok &= sympy.simplify(La_.T * La_ - sympy.eye(4) - Lc_.T * Lc_) == sympy.zeros(4, 4)
        lemma_ok &= sympy.simplify(Ld_.T * Ld_ - sympy.eye(4) - Lb_.T * Lb_) == sympy.zeros(4, 4)
        # exp(theta S^AB) is a product of two unit vectors: g = Gamma_A Gamma(u), u = eta_A c e_A + sn e_B
        u = [0] * 8
        u[A], u[B] = eta[A] * c, sn
        norm_u = sympy.simplify(sum(eta[D] * u[D] ** 2 for D in IDX))
        Gu = sum((sympy.Matrix(G[D]) * u[D] for D in IDX), sympy.zeros(N, N))
        g = c * sympy.eye(N) + sn * sympy.Matrix(K)
        pin_ok &= sympy.simplify(norm_u - eta[A]) == 0
        pin_ok &= sympy.simplify(sympy.Matrix(G[A]) * Gu - g) == sympy.zeros(N, N)
        # g^T sigma16 g = c^2 sigma16 + c sn (K^T sigma16 + sigma16 K) + sn^2 K^T sigma16 K
        X1 = add(mul(tr(K), sigma16), mul(sigma16, K))
        X2 = mulall(tr(K), sigma16, K)
        e2 = 1 if eq(X2, sigma16) else -1 if eq(X2, scal(-1, sigma16)) else 0
        sig_ok &= is_zero(X1) and e2 != 0 and sympy.simplify(c ** 2 + e2 * sn ** 2 - 1) == 0
        # double cover for rotations: g(2 pi) = -I16 while Lambda(2 pi) = I8
        if s == 1:
            cover_ok &= g.subs(th, 2 * sympy.pi) == -sympy.eye(N) and Lam.subs(th, 2 * sympy.pi) == sympy.eye(8)
    check("exp_closed_forms", exp_ok and n_rot == 12 and n_boost == 16,
          f"(2 S^AB)^2 = (Gamma_A Gamma_B)^2 = -eta_AA eta_BB I16, so exp(theta S^AB) = cos(theta/2) I16 + "
          f"sin(theta/2) Gamma_A Gamma_B for the {n_rot} rotation generators (eta_AA = eta_BB) and "
          f"cosh(theta/2) I16 + sinh(theta/2) Gamma_A Gamma_B for the {n_boost} boost generators "
          "(eta_AA = -eta_BB); verified symbolically (sympy): g(0) = I16, dg/dtheta = S^AB g, g(theta) g(phi) = g(theta + phi)")
    check("exp_vector_action", vec_ok and lemma_ok,
          "for every generator, exp(theta S^AB) Gamma_C exp(-theta S^AB) = sum_D Lambda(theta)_DC Gamma_D with "
          "Lambda(theta) = exp(theta M^AB) (checked as Lambda(0) = I8 and dLambda/dtheta = M^AB Lambda) and "
          "Lambda^T eta Lambda = eta: each exp(theta S^AB) acts on the Gamma's as an element of SO_0(4,4); for every "
          "Lambda(theta) = [[A, B], [C, D]] (space block first) also A^T A = I4 + C^T C and D^T D = I4 + B^T B "
          "(Lemma A of the argument) (sympy, symbolic theta)")
    check("exp_is_product_of_two_unit_vectors", pin_ok,
          "exp(theta S^AB) = Gamma_A Gamma(u) with Gamma(u) = sum_D u^D Gamma_D, u = eta_AA cos(theta/2) e_A + "
          "sin(theta/2) e_B (rotation) or cosh(theta/2) e_A + sinh(theta/2) e_B (boost), eta(u,u) = eta_AA = +-1: "
          "every exponential of a scaled commutator is a product of two unit vectors, i.e. an element of "
          "Spin(4,4) inside Pin(4,4) (sympy, symbolic theta)")
    check("exp_preserves_sigma16", sig_ok,
          "exp(theta S^AB)^T sigma16 exp(theta S^AB) = sigma16 for all 28 generators and symbolic theta: with "
          "K = Gamma_A Gamma_B, K^T sigma16 + sigma16 K = 0 and K^T sigma16 K = +sigma16 (rotation, cos^2 + sin^2 = 1) or "
          "-sigma16 (boost, cosh^2 - sinh^2 = 1) (sympy)")
    check("double_cover", cover_ok,
          "for the 12 rotation generators exp(2 pi S^AB) = -I16 while Lambda(2 pi) = I8: -I16 lies in Spin_0(4,4) and in "
          "the kernel of the action on the Gamma's. That the kernel is exactly {+-I16} is Lemma B of the argument "
          "(from `irreducible_commutant` and `anticommutant_T16A8`), not this check")

    # the twisted adjoint action and the components of Pin(4,4)
    def twisted_lambda(x, odd):
        """Matrix L with sign * x Gamma_C x^-1 = sum_D L_DC Gamma_D, sign = -1 for odd x (twisted adjoint)."""
        if eq(mul(tr(x), x), I):
            xinv = tr(x)
        else:
            xinv = [[Fraction(v) for v in r] for r in sympy.Matrix(x).inv().tolist()]
        L = [[0] * 8 for _ in IDX]
        for C in IDX:
            y = scal(-1 if odd else 1, mulall(x, G[C], xinv))
            for D in IDX:
                L[D][C] = Fraction(trace(mul(tr(G[D]), y)), 16)
            if not eq(y, lin_comb([L[D][C] for D in IDX], G)):
                return None
        return L

    def pattern(L):
        return (sign(fdet(L)), sign(fdet([r[:4] for r in L[:4]])), sign(fdet([r[4:] for r in L[4:]])))

    comps = []
    for label, x, odd in (("I16", I, False), ("Gamma_0", G[0], True), ("Gamma_4", G[4], True),
                          ("Gamma_0 Gamma_4", mul(G[0], G[4]), False)):
        L = twisted_lambda(x, odd)
        comps.append((label, L is not None and eq(mul(mul(tr(L), eta_m), L), eta_m), pattern(L) if L else None))
    comp_ok = all(c[1] for c in comps) and [c[2] for c in comps] == [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
    check("pin44_four_components", comp_ok,
          "computed: the twisted adjoint action x Gamma_C x^-1 (times -1 for odd x) of the four representatives "
          + "; ".join(f"{c[0]}: (det Lambda, sign det space block, sign det time block) = {c[2]}" for c in comps)
          + ". The four sign patterns are different, so (Lemma A: the block determinants never vanish on O(4,4)) these "
          "four elements lie in four different components of Pin(4,4). Argued, not computed: every product of "
          "exponentials exp(theta S^AB) is connected to I16 and therefore has pattern (1, 1, 1); so the exponentials of "
          "the scaled commutators generate only the identity component Spin_0(4,4)")
    rot_pat, boost_pat, rot_exp, sig_flip = Counter(), Counter(), True, Counter()
    for A, B in pairs:
        K = mul(G[A], G[B])
        pat = pattern(twisted_lambda(K, False))
        X2 = mulall(tr(K), sigma16, K)
        if eta[A] == eta[B]:
            rot_pat[pat] += 1
            # exp(pi S^AB) = cos(pi/2) I16 + sin(pi/2) K = K (closed form of `exp_closed_forms`)
            g = sympy.cos(sympy.pi / 2) * sympy.eye(N) + sympy.sin(sympy.pi / 2) * sympy.Matrix(K)
            rot_exp &= g == sympy.Matrix(K)
            sig_flip["rotation preserves" if eq(X2, sigma16) else "?"] += 1
        else:
            boost_pat[pat] += 1
            rot_exp &= trace(K) == 0
            sig_flip["boost flips" if eq(X2, scal(-1, sigma16)) else "?"] += 1
    check("products_components",
          rot_pat == Counter({(1, 1, 1): 12}) and boost_pat == Counter({(1, -1, -1): 16}) and rot_exp
          and sig_flip == Counter({"rotation preserves": 12, "boost flips": 16}),
          "the 28 group elements Gamma_A Gamma_B = 2 S^AB (A < B), twisted adjoint by traces: the 12 rotation products "
          f"have pattern {dict(rot_pat)} and equal exp(pi S^AB), so they lie in Spin_0(4,4); the 16 boost products have "
          f"pattern {dict(boost_pat)}: they lie in Spin(4,4) but NOT in Spin_0(4,4), whose elements all have pattern "
          "(1, 1, 1) (argument, Lemma A); in particular tr(Gamma_A Gamma_B) = 0 for the boosts, while a boost exponential has "
          "tr exp(theta S^AB) = 16 cosh(theta/2) >= 16. (Gamma_A Gamma_B)^T sigma16 (Gamma_A Gamma_B) = +sigma16 for the 12 "
          "rotations and -sigma16 for the 16 boosts")

    def generated(gens):
        """Closure of a set of signed permutation matrices under products, with the parity of each element."""
        start = (tuple(range(N)), (1,) * N)
        seen = {start: 0}
        frontier = [start]
        while frontier:
            nxt = []
            for x in frontier:
                for gp, par in gens:
                    y = sp_mul(x, gp)
                    if y not in seen:
                        seen[y] = (seen[x] + par) % 2
                        nxt.append(y)
            frontier = nxt
        return seen

    def sp_pattern(x, par):
        L = [[0] * 8 for _ in IDX]
        xi = sp_inv(x)
        for C in IDX:
            y = sp_mul(sp_mul(x, spG[C]), xi)
            hit = [(D, 1) for D in IDX if y == spG[D]] + [(D, -1) for D in IDX if y == sp_neg(spG[D])]
            if len(hit) != 1:
                return None
            D, sgn = hit[0]
            L[D][C] = sgn * (-1 if par else 1)
        if not eq(mul(mul(tr(L), eta_m), L), eta_m):
            return None
        return pattern(L)

    grp_even = generated([(to_sp(mul(G[A], G[B])), 0) for A, B in pairs])
    grp_all = generated([(spG[A], 1) for A in IDX])
    pat_even = Counter(sp_pattern(x, par) for x, par in grp_even.items())
    pat_all = Counter(sp_pattern(x, par) for x, par in grp_all.items())
    refl_ok = all(sp_pattern(spG[A], 1) is not None and
                  twisted_lambda(G[A], True) == [[(-1 if (C == D == A) else int(C == D)) for C in IDX] for D in IDX]
                  for A in IDX)
    check("finite_groups",
          len(grp_even) == 256 and pat_even == Counter({(1, 1, 1): 128, (1, -1, -1): 128})
          and len(grp_all) == 512 and pat_all == Counter({(1, 1, 1): 128, (-1, -1, 1): 128, (-1, 1, -1): 128, (1, -1, -1): 128})
          and refl_ok,
          f"the 28 matrices Gamma_A Gamma_B generate a finite group of order {len(grp_even)} (= +-the 128 even basis "
          f"products) meeting exactly two components: {dict(pat_even)}; the eight Gamma_A generate a group of order "
          f"{len(grp_all)} (= +-all 256 basis products) meeting all four: {dict(pat_all)}. Each Gamma_A acts (twisted) as "
          "the reflection diag(1, .., -1 at A, .., 1) of the frame")

    # ---- 5. projectors and the Krein matrix
    IF = [[Fraction(x) for x in r] for r in I]
    proj_ok = (eq(add(PL, PR), IF) and eq(mul(PL, PL), PL) and eq(mul(PR, PR), PR)
               and is_zero(mul(PL, PR)) and is_zero(mul(PR, PL))
               and eq(tr(PL), PL) and eq(tr(PR), PR) and trace(PL) == 8 and trace(PR) == 8)
    check("projectors_PL_PR", proj_ok,
          f"P_L = (I16 - T16A[8])/2 and P_R = (I16 + T16A[8])/2 (author input cells 323, 324: {labels['323']}, "
          f"{labels['324']}): P_L + P_R = I16, P_L^2 = P_L, P_R^2 = P_R, P_L P_R = P_R P_L = 0, both symmetric, "
          "tr P_L = tr P_R = 8")
    check("projectors_vs_gammas", all(eq(mul(G[A], PL), mul(PR, G[A])) and eq(mul(G[A], PR), mul(PL, G[A])) for A in IDX)
          and all(is_zero(comm(PL, S[p])) and is_zero(comm(PR, S[p])) for p in pairs),
          "Gamma_A P_L = P_R Gamma_A and Gamma_A P_R = P_L Gamma_A (each Dirac matrix exchanges the halves) and "
          "[P_L, S^AB] = [P_R, S^AB] = 0 (each half is invariant under Spin_0(4,4))")
    check("projectors_vs_sigma16", is_zero(comm(PL, sigma16)) and is_zero(comm(PR, sigma16)),
          "[P_L, sigma16] = [P_R, sigma16] = 0: sigma16 = diag(-sigma, sigma) is block diagonal")
    Qp = [[Fraction(x, 2) for x in r] for r in add(I, sigma16)]
    Qm = [[Fraction(x, 2) for x in r] for r in sub(I, sigma16)]
    check("projectors_sigma16",
          eq(mul(Qp, Qp), Qp) and eq(mul(Qm, Qm), Qm) and is_zero(mul(Qp, Qm)) and eq(add(Qp, Qm), IF)
          and eq(tr(Qp), Qp) and eq(tr(Qm), Qm) and trace(Qp) == 8 and trace(Qm) == 8
          and all(is_zero(comm(Q, P)) for Q in (Qp, Qm) for P in (PL, PR)),
          "Q_+- = (I16 +- sigma16)/2 (the projectors (1 +- C)/2 of the Revision calculations, C = sigma16): real, "
          "symmetric, Q^2 = Q, Q_+ Q_- = 0, Q_+ + Q_- = I16, tr Q_+- = 8 (rank 8), and they commute with P_L and P_R")
    Bc = (zeros(), negM5)                         # B = -i M5
    Bdag = (tr(Bc[0]), scal(-1, tr(Bc[1])))
    check("krein_B",
          eq(M5, mulall(G[0], G[1], G[2], G[3], G[4])) and eq(tr(M5), scal(-1, M5)) and eq(mul(M5, M5), scal(-1, I))
          and trace(M5) == 0 and ceq(Bdag, Bc) and ceq(cmul(Bc, Bc), (I, zeros()))
          and not is_zero(Bc[1]) and ceq(cmul(Bc, (T8, zeros())), (zeros(), scal(-1, mul(T8, Bc[1]))))
          and not is_zero(comm(PL, M5)),
          "B = -i C gamma^(x4) of Revision/SPEC.md = -i sigma16 Gamma_4 = -i Gamma_0 Gamma_1 Gamma_2 Gamma_3 Gamma_4: "
          "M = sigma16 Gamma_4 is real with M^T = -M, M^2 = -I16, tr M = 0, so B is Hermitian, B^2 = I16 and tr B = 0: "
          "eigenvalues +1 and -1, eight each (signature (8,8)). B is complex (Re B = 0, Im B = -M), so it is NOT one of "
          "the real Dirac matrices; it is odd (a product of five Gamma's) and anticommutes with T16A[8]")
    Pp = ([[Fraction(int(i == j), 2) for j in range(N)] for i in range(N)], [[Fraction(-x, 2) for x in r] for r in M5])
    Pm = ([[Fraction(int(i == j), 2) for j in range(N)] for i in range(N)], [[Fraction(x, 2) for x in r] for r in M5])
    herm = all(eq(tr(P[0]), P[0]) and eq(tr(P[1]), scal(-1, P[1])) for P in (Pp, Pm))
    check("projectors_B",
          ceq(cmul(Pp, Pp), Pp) and ceq(cmul(Pm, Pm), Pm) and ceq(cmul(Pp, Pm), (zeros(), zeros()))
          and ceq((add(Pp[0], Pm[0]), add(Pp[1], Pm[1])), (IF, zeros())) and herm
          and trace(Pp[0]) == 8 and trace(Pp[1]) == 0 and not is_zero(Pp[1])
          and not ceq(cmul(Pp, (PL, zeros())), cmul((PL, zeros()), Pp)),
          "Pi_+- = (I16 +- B)/2 (used by the Krein-space calculations: Revision/SPEC.md section 6, canonical anticommutator "
          "with B): Pi^2 = Pi, Pi_+ Pi_- = 0, Pi_+ + Pi_- = I16, Hermitian, tr Pi_+- = 8 (rank 8); complex (Re Pi = I16/2, "
          "Im Pi_+- = -+M/2), and they do not commute with P_L, P_R (B is odd)")

    # ---- 6. the author's chain from T16A to the Lagrangians and field equations (scan of all input cells)
    scan = nbd["scan"]
    chain = {c["input_cell"]: c for c in scan["chain"]}
    check("chain_assignments", scan["assigned_in"] == ASSIGN_EXPECT,
          "scan of all input cells of the notebook (commented-out code removed): the only cells that assign "
          + "; ".join(f"{k}: {cells_text(v, labels)}" for k, v in scan["assigned_in"].items()))
    lag_ok = (all(c in chain and chain[c]["assigns"] == a and chain[c]["refs"] == r for c, (a, r) in CHAIN_EXPECT.items())
              and all("T16A" not in chain[c]["refs"] for c in (828, 830, 836)))
    check("chain_lagrangians", lag_ok,
          "T16A (cell 286) -> SAB (326), sigma16 (285), T16alpha = sum_A e_A^alpha T16A[A] (361) -> useT16 (822), and "
          "products -> base16 (451, 453); the Lagrangians Lg[] (828), La[] (830), Lj[] (836) use sigma16, SAB and "
          "T16alpha / useT16 (Lj also base16) and never T16A directly; the field equations eLa = eL[La, useDSQRT] (841) "
          "come from La through eL (839). Assignments and uses measured by the scan")
    ref = scan["referenced_in"]
    check("projectors_only_in_checks",
          ref["P_L"] == [323, 325] and ref["P_R"] == [324, 325]
          and set(ref["T16A[8]"]) & {828, 830, 836, 839, 841} == set(),
          f"P_L is used only in input cells {cells_text(ref['P_L'], labels)} and P_R only in "
          f"{cells_text(ref['P_R'], labels)} (definitions and the author's check 325); the named T16A[8] appears only in "
          f"{cells_text(ref['T16A[8]'], labels)} (definitions and checks), never in a Lagrangian cell")

    # ---- 7. every other copy of the matrices in the repository
    Sx = lambda a, b: S[(COORD_TO_A[a], COORD_TO_A[b])]  # noqa: E731  (coordinate order x1..x8)
    eta_x = [eta[COORD_TO_A[k]] for k in IDX]
    sources = []   # (check name, source, kind, read by, compared, coordinate map, result)

    def grouped(names):
        """'file: obj' names -> 'file: obj1, obj2; file2: ...' (plain names are joined with commas)."""
        groups = {}
        for k in names:
            head, _, obj = k.rpartition(": ")
            groups.setdefault(head, []).append(obj)
        return "; ".join((f"{h}: " if h else "") + ", ".join(v) for h, v in groups.items())

    def compare(name, source, kind, readers, items, cmap):
        fails = [k for k, ok_ in items if not ok_]
        shown = grouped([k for k, _ in items])
        sources.append((name, source, kind, readers, shown, cmap, "equal" if not fails else f"DIFFER: {fails}"))
        return check(name, not fails,
                     f"{source} ({kind}): {shown}: equal to the author's matrices entry by "
                     f"entry ({cmap})" + ("" if not fails else f"; DIFFER: {fails}"))

    fx = json.loads((ROOT / "Revision/algebra/gammas.json").read_text(encoding="utf-8"))
    compare("fixture_Revision_algebra_gammas_json", "Revision/algebra/gammas.json", "Revision fixture, JSON",
            "Revision calculations (e.g. Revision/theory, Revision/pairing, Revision/kohn_sham) and the textbook notebooks",
            [("coordinates", fx["coordinates"] == [f"x{k}" for k in range(1, 9)]),
             ("notebookFrameIndex", fx["notebookFrameIndex"] == COORD_TO_A),
             ("eta", fx["eta"] == eta_x),
             ("gamma", all(eq(int_matrix(fx["gamma"][k]), G[COORD_TO_A[k]]) for k in IDX)),
             ("C", eq(int_matrix(fx["C"]), sigma16)),
             ("Gamma", eq(int_matrix(fx["Gamma"]), T8)),
             ("B", eq(int_matrix(fx["B"]["re"]), zeros()) and eq(int_matrix(fx["B"]["im"]), negM5)),
             ("S", all(eq(frac_matrix(fx["S"][a][b]), Sx(a, b)) for a in IDX for b in IDX))],
            "x_k -> Gamma_A with A = 1..7, 0 for k = 1..8; S[a][b] = S^(A(a) A(b))")
    pg = json.loads((ROOT / "Revision/algebra/reports/python-gammas.json").read_text(encoding="utf-8"))
    compare("report_Revision_algebra_python_gammas_json", "Revision/algebra/reports/python-gammas.json",
            "Revision report of the Python construction, JSON", "e.g. textbook notebook 04a (as a record)",
            [("coordinates", pg["coordinates"] == [f"x{k}" for k in range(1, 9)]),
             ("map_coordinate_to_T16_index", pg["map_coordinate_to_T16_index"] == {f"x{k + 1}": COORD_TO_A[k] for k in IDX}),
             ("eta", pg["eta"] == eta_x),
             ("gamma", all(eq(int_matrix(pg["gamma"][k]), G[COORD_TO_A[k]]) for k in IDX)),
             ("C", eq(int_matrix(pg["C"]), sigma16)),
             ("Gamma", eq(int_matrix(pg["Gamma"]), T8)),
             ("B", eq(int_matrix(pg["B"]["re"]), zeros()) and eq(int_matrix(pg["B"]["im"]), negM5)),
             ("S", len(pg["S"]) == 28 and all(eq(frac_matrix(pg["S"][f"x{a + 1},x{b + 1}"]), Sx(a, b))
                                               for a in IDX for b in IDX if a < b))],
            "x_k -> Gamma_A as above; S['xi,xj'] = S^(A(i) A(j))")
    rev = load_module("Revision/algebra/python/check_algebra.py", "check_algebra").construct()
    compare("Revision_construction", "Revision/algebra/python/check_algebra.py: construct()",
            "Revision Python construction", "Revision/algebra (writes python-gammas.json)",
            [("eta4488", eq(rev["eta4488"], eta8)), ("sigma", eq(rev["sigma"], sigma8)),
             ("tau", all(eq(rev["tau"][A], tau[A]) for A in IDX)),
             ("taubar", all(eq(rev["taubar"][A], taubar[A]) for A in IDX)),
             ("T16[0..7]", all(eq(rev["T16"][A], G[A]) for A in IDX)),
             ("sigma16", eq(rev["sigma16"], sigma16)), ("T16_8", eq(rev["T16_8"], T8))],
            "notebook frame A = 0..7, no map")
    ra = wl["Revision/algebra/wolfram/RevisionAlgebra.wl"]
    compare("Revision_wolfram_RevisionAlgebra", "Revision/algebra/wolfram/RevisionAlgebra.wl",
            "Revision Wolfram construction (producer of gammas.json), loaded by extract_repository_wolfram_gammas.wls",
            "Revision/algebra/wolfram/verify_algebra.wls (writes gammas.json)",
            [("RAEta4488", eq(ra["eta4488"], eta8)), ("RASigma8", eq(ra["sigma8"], sigma8)),
             ("RATau", all(eq(ra["tau"][A], tau[A]) for A in IDX)),
             ("RATauBar", all(eq(ra["taubar"][A], taubar[A]) for A in IDX)),
             ("RAT16[0..8]", all(eq(ra["T16"][A], G[A]) for A in IDX) and eq(ra["T16"][8], T8)),
             ("RANotebookFrame", ra["notebookFrame"] == COORD_TO_A),
             ("RAEta", eq(ra["eta"], [[eta_x[i] if i == j else 0 for j in IDX] for i in IDX])),
             ("RAGamma", all(eq(ra["gamma"][k], G[COORD_TO_A[k]]) for k in IDX)),
             ("RAC", eq(ra["C"], sigma16)), ("RAChirality", eq(ra["Gamma"], T8)),
             ("RAB", eq(ra["B_re"], zeros()) and eq(ra["B_im"], negM5)),
             ("RAS", all(eq([[Fraction(x, 4) for x in r] for r in ra["four_S"][a][b]], Sx(a, b)) for a in IDX for b in IDX)),
             ("RAPL, RAPR", eq(ra["twice_PL"], nbd["twice_PL"]) and eq(ra["twice_PR"], nbd["twice_PR"]))],
            "gamma, eta, S in the order x1..x8 with x_k -> Gamma_A as above; T16, tau, taubar in the notebook frame")
    d16 = load_module("scripts/d16c_exact.py", "d16c_exact")
    old = d16.notebook_gammas()
    old_tau = d16.notebook_tau()
    compare("old_stage_construction", "scripts/d16c_exact.py: notebook_gammas(), notebook_tau(), notebook_taubar(), "
            "charge_matrix(), chirality(), spin_generator()", "earlier-stage Python construction",
            "e.g. scripts/build_dirac16complex_fixture.py, scripts/check_dirac16complex_algebra.py, tests/test_d16c_algebra.py",
            [("gamma", all(eq(int_matrix(old[A]), G[A]) for A in IDX)),
             ("tau", all(eq(int_matrix(old_tau[A]), tau[A]) for A in IDX)),
             ("taubar", all(eq(int_matrix(m), taubar[A]) for A, m in enumerate(d16.notebook_taubar(old_tau)))),
             ("C", eq(int_matrix(d16.charge_matrix(old)), sigma16)),
             ("chirality", eq(int_matrix(d16.chirality(old)), T8)),
             ("S", all(eq(frac_matrix(d16.spin_generator(old, a, b)), S[(a, b)]) for a, b in pairs))],
            "notebook frame A = 0..7, no map")
    prim = load_module("scripts/check_dirac16complex_primordial.py", "check_dirac16complex_primordial").notebook_gammas()
    compare("old_stage_primordial_construction", "scripts/check_dirac16complex_primordial.py: notebook_gammas()",
            "earlier-stage Python construction (its own copy)", "scripts/check_dirac16complex_primordial.py",
            [("gamma", all(eq(int_matrix(prim[0][A]), G[A]) for A in IDX)), ("C", eq(int_matrix(prim[1]), sigma16)),
             ("tau", all(eq(int_matrix(prim[2][A]), tau[A]) for A in IDX)),
             ("taubar", all(eq(int_matrix(prim[3][A]), taubar[A]) for A in IDX)),
             ("sigma", eq(int_matrix(prim[4]), sigma8))],
            "notebook frame A = 0..7, no map")
    af = json.loads((ROOT / "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json").read_text(encoding="utf-8"))
    compare("old_stage_fixture_algebra_fixture_json", "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
            "earlier-stage fixture, JSON",
            "e.g. wolfram/Dirac16Complex00.wl, the earlier-stage Wolfram packages, scripts/generate_dirac16complex_constants.py (Rust constants)",
            [("eta", eq(af["eta"], eta8)), ("sigma8", eq(af["sigma8"], sigma8)),
             ("tau", all(eq(af["tau"][A], tau[A]) for A in IDX)),
             ("taubar", all(eq(af["taubar"][A], taubar[A]) for A in IDX)),
             ("gamma", all(eq(af["gamma"][A], G[A]) for A in IDX)),
             ("C", eq(af["C"], sigma16)), ("chirality", eq(af["chirality"], T8)),
             ("S", len(af["S"]) == 28 and all(eq(frac_matrix(e["matrix"]), S[(e["a"], e["b"])]) and e["a"] < e["b"] for e in af["S"])),
             ("B", eq(af["B"]["real"], zeros()) and eq(af["B"]["imag"], negM5))],
            "notebook frame A = 0..7, no map")
    gc, go = af["gammaClifford"], af["gammaOctonion"]
    Kc, Ko = af["K_clifford"], af["K_octonion"]
    same_c = [A for A in IDX if eq(gc[A], G[A])]
    same_o = [A for A in IDX if eq(go[A], G[A])]
    dKc, dKo = fdet(Kc), fdet(Ko)
    other_ok = (all(eq(mul(gc[A], Kc), mul(Kc, G[A])) for A in IDX) and dKc != 0
                and all(eq(mul(G[A], Ko), mul(Ko, go[A])) for A in IDX) and dKo != 0)
    sources.append(("old_stage_fixture_other_pictures", "algebra-fixture.json: gammaClifford, gammaOctonion",
                    "earlier-stage fixture, two OTHER bases", "e.g. scripts/check_dirac16complex_algebra.py and its tests (equivalence checks)",
                    "gammaClifford, gammaOctonion", "notebook frame A = 0..7, no map",
                    f"NOT equal entry by entry (gammaClifford_A = Gamma_A only for A in {same_c}, gammaOctonion_A = Gamma_A "
                    f"only for A in {same_o}); equivalent: "
                    f"gammaClifford_A K_clifford = K_clifford Gamma_A, Gamma_A K_octonion = K_octonion gammaOctonion_A, "
                    f"det K_clifford = {dKc}, det K_octonion = {dKo}"))
    check("old_stage_fixture_other_pictures", other_ok,
          "algebra-fixture.json also stores two OTHER real bases of Cl(4,4), gammaClifford (dirac-main tensor products) and "
          f"gammaOctonion (split octonions). Measured: they are NOT equal to the author's matrices entry by entry "
          f"(gammaClifford_A = Gamma_A only for A in {same_c}, gammaOctonion_A = Gamma_A only for A in {same_o}); they are "
          f"equivalent to them: gammaClifford_A K = K Gamma_A with K = K_clifford, det K = {dKc}, and Gamma_A K' = K' "
          f"gammaOctonion_A with K' = K_octonion, det K' = {dKo}, for all eight A")
    rust_items = []
    for rf in ("studies/dirac16complex_kohn_sham/src/generated.rs", "studies/dirac16complex_cosmology/src/generated.rs"):
        txt = (ROOT / rf).read_text(encoding="utf-8")
        rust_items += [
            (f"{rf}: ETA", [int_matrix([rust_const(txt, "ETA")])[0]] == [eta]),
            (f"{rf}: GAMMA", all(eq(int_matrix(m), G[A]) for A, m in enumerate(rust_const(txt, "GAMMA")))
             and len(rust_const(txt, "GAMMA")) == 8),
            (f"{rf}: CHARGE", eq(int_matrix(rust_const(txt, "CHARGE")), sigma16)),
            (f"{rf}: CHIRALITY", eq(int_matrix(rust_const(txt, "CHIRALITY")), T8)),
            (f"{rf}: B_IMAG", eq(int_matrix(rust_const(txt, "B_IMAG")), negM5))]
    compare("old_stage_rust_generated_constants", "studies/dirac16complex_kohn_sham/src/generated.rs, "
            "studies/dirac16complex_cosmology/src/generated.rs", "earlier-stage Rust constants (f64)",
            "the earlier-stage Rust studies dirac16complex_kohn_sham and dirac16complex_cosmology",
            rust_items, "notebook frame A = 0..7, no map; every f64 entry is an exact integer; B = i B_IMAG")
    wl_items = []
    for pk in ("wolfram/Dirac16ComplexAlgebra.wl", "wolfram/Dirac16ComplexGeometry.wl", "wolfram/Dirac16ComplexPrimordial.wl",
               "wolfram/Dirac16ComplexKohnSham.wl", "wolfram/Dirac16ComplexPairing.wl",
               "wolfram/Dirac16ComplexMatterAntimatter.wl"):
        d = wl[pk]
        name = pk.split("/")[1]
        wl_items.append((f"{name}: gamma", all(eq(d["gamma"][A], G[A]) for A in IDX)))
        wl_items.append((f"{name}: C", eq(d["C"], sigma16)))
        wl_items.append((f"{name}: chirality", eq(d["chirality"], T8)))
        if "eta" in d:
            wl_items.append((f"{name}: eta", eq(d["eta"], eta8)))
        if "tau" in d:
            wl_items.append((f"{name}: sigma8, tau, taubar", eq(d["sigma8"], sigma8)
                             and all(eq(d["tau"][A], tau[A]) and eq(d["taubar"][A], taubar[A]) for A in IDX)))
        if "four_S" in d:
            wl_items.append((f"{name}: S", all(eq([[Fraction(x, 4) for x in r] for r in d["four_S"][a][b]], S[(a, b)])
                                               for a in IDX for b in IDX)))
        if "B_im" in d:
            wl_items.append((f"{name}: B", eq(d["B_re"], zeros()) and eq(d["B_im"], negM5)))
        if "twice_Pminus" in d:
            wl_items.append((f"{name}: P_-, P_+", eq(d["twice_Pminus"], nbd["twice_PL"]) and eq(d["twice_Pplus"], nbd["twice_PR"])))
    compare("old_stage_wolfram_packages", "wolfram/Dirac16Complex{Algebra, Geometry, Primordial, KohnSham, Pairing, "
            "MatterAntimatter}.wl", "earlier-stage Wolfram constructions (each builds its own copy), loaded by "
            "extract_repository_wolfram_gammas.wls", "e.g. the earlier-stage scripts/verify_dirac16complex*.wls",
            wl_items, "notebook frame A = 0..7, no map")

    failed = [c for c in CHECKS if not c[1]]
    if failed:
        print(f"{len(failed)} of {len(CHECKS)} checks FAILED; {OUT.name} not written")
        return 1

    # ------------------------------------------------------------------- write the Markdown
    n_checks = len(CHECKS)
    L = []
    w = L.append
    w("# Dirac matrices: the eight real 16 x 16 Dirac matrices of the author's notebook")
    w("")
    w(f"Provenance file.  Generated by `provenance/dirac_matrices/build_dirac_matrices_md.py` from the author's "
      f"notebook `{NOTEBOOK}` (read only, never modified).  Do not edit by hand: re-run the three commands below.")
    w("")
    w("## Answer in one paragraph")
    w("")
    w("Yes: the calculations use eight real-valued 16 x 16 Dirac matrices, and they are the author's own, Gamma_A = T16A[A] "
      "(A = 0..7). They come from the author's input cells, evaluated directly from the `.nb` file in the author's order "
      "(nothing re-typed; the author's Notation-package symbols are emulated, see Source), and they reproduce the author's "
      "stored outputs entry by entry. All entries are -1, 0 or +1. The matrices satisfy {Gamma_A, Gamma_B} = 2 eta_AB I16 "
      "with eta = diag(+1,+1,+1,+1,-1,-1,-1,-1), which is the Clifford algebra Cl(4,4) = M16(R). "
      "The 28 scaled commutators S^AB = (1/4)[Gamma_A, Gamma_B] are Lie-algebra elements: they form a basis of spin(4,4), "
      "which is isomorphic to so(4,4). Their exponentials exp(theta S^AB) are products of two unit vectors, so they lie in "
      "Pin(4,4), and together they generate exactly the identity component Spin_0(4,4), not all of Pin(4,4). "
      "Pin(4,4) has four components. What is computed exactly: the component invariants of the four representatives "
      "I16, Gamma_0, Gamma_4, Gamma_0 Gamma_4 (four different sign patterns) and of all 28 products Gamma_A Gamma_B. What is "
      "argued (continuity), not computed: every product of exponentials stays in the identity component; cited standard "
      "facts are listed in the argument. The group elements Gamma_A Gamma_B = 2 S^AB themselves reach a second component "
      "(the 16 boost pairs), so the exp(theta S^AB) together with one boost product such as Gamma_0 Gamma_4 generate "
      "Spin(4,4), which has two components. Every such product is even, so one Dirac matrix is still needed for the two odd "
      "components: Pin(4,4) = <exp(theta S^AB), Gamma_0, Gamma_4> = <exp(theta S^AB), Gamma_A Gamma_B, Gamma_0>. "
      "In the author's notebook the matrices enter the Lagrangians Lg[], La[], Lj[] and the field equations eLa through "
      "sigma16, SAB and the curved matrices T16alpha = e_A^alpha T16A (traced below); P_L and P_R enter only the author's "
      "checks. Every other copy of the matrices in the repository (Revision and earlier-stage JSON fixtures, Python, "
      "Wolfram and Rust constructions) equals these entry by entry, with the coordinate map x8 -> Gamma_0, x1..x3 -> "
      "Gamma_1..3, x4 -> Gamma_4, x5..x7 -> Gamma_5..7; the only exception is two alternative bases stored in the "
      "earlier-stage fixture, which are equivalent to the author's matrices but not equal to them. "
      "The matrices are real; the fields are not required to be: the author's Psi16 has commuting function components, "
      "and Revision/SPEC.md uses the same matrices for a complex Grassmann field Psi and a complex commuting field Phi. "
      f"All {n_checks} exact checks pass.")
    w("")
    w("## How to reproduce (complete, self-contained)")
    w("")
    w("Requirements: Wolfram Engine or Mathematica with `wolframscript` on the PATH (no front end is needed); "
      "Python 3.10+ with `sympy`. From the repository root:")
    w("")
    w("```bash")
    w("wolframscript -file provenance/dirac_matrices/extract_from_author_notebook.wls")
    w("wolframscript -file provenance/dirac_matrices/extract_repository_wolfram_gammas.wls")
    w("python provenance/dirac_matrices/build_dirac_matrices_md.py")
    w("```")
    w("")
    w(f"Expected output: the first command prints `author notebook: 996 input cells`, then one line "
      f"`evaluated author input cell N (In[n]): ...` for each of the {len(nbd['cells'])} cells listed below, then "
      "`wrote .../author_notebook_T16.json`. The second prints `loaded <package>` for seven packages and "
      "`wrote .../repository_wolfram_gammas.json`. The third prints "
      f"`{n_checks} of {n_checks} checks pass` and `wrote provenance/dirac matrices.md`. "
      "Run time: about 20 seconds for each Wolfram command and about 1 minute for Python. "
      "Side effects: the commands write only `provenance/dirac_matrices/author_notebook_T16.json`, "
      "`provenance/dirac_matrices/repository_wolfram_gammas.json` and `provenance/dirac matrices.md`. The notebook and "
      "the compared repository files are only read. "
      "If any check fails, the third command prints `FAIL <name>: <detail>`, does not write this file and exits with code 1. "
      "`python provenance/dirac_matrices/build_dirac_matrices_md.py --check` runs every check and confirms that this file "
      "is up to date without writing anything; the test `tests/test_dirac_matrices_provenance.py` does the same. This file "
      "depends only on the notebook and the compared files named below, never on a directory listing.")
    w("")
    w("## Source: the author's input cells that were evaluated")
    w("")
    w("| input cell (index among the notebook's 996 Input cells) | CellLabel | defines |")
    w("|---|---|---|")
    for c in nbd["cells"]:
        w(f"| {c['input_cell']} | {c['label']} | `{c['defines']}` |")
    w("")
    w(f"**Order.** The cells are evaluated in the author's order of In[n] labels. Input cell 285 ({labels['285']}, sigma16) "
      f"comes before input cell 286 ({labels['286']}, the definition of T16A): the author's stored "
      f"{nbd['stored_Out370']['out_label']} is the unevaluated product `{out370[9:-1]}`. So in the author's kernel sigma16 "
      "holds the symbolic product and takes its matrix value once T16A is defined; the extractor records the same state "
      "right after cell 285 (`author_evaluation_order`). Because T16A[0..3] are assigned only in cell 286 "
      "(`chain_assignments`), this lazily evaluated sigma16 has the same value as the product taken after cell 286.")
    w("")
    w(f"**Notation package.** The author loads the Notation package (input cell 51, {labels['51']}) and Symbolizes the boxes "
      f"taubar (input cell 54, {labels['54']}), T16^A (input cell 55, {labels['55']}) and T16^alpha (input cell 56, "
      f"{labels['56']}), so each of them is one atomic symbol. The notebook records the name of the T16^A symbol, "
      f"`T16[UnderBracket]Superscript[UnderBracket]A` (input cell 477, {labels['477']}), and the author's Head check of "
      f"taubar (input cell 248, {labels['248']}) printed `Symbol`. The Notation package needs a front end, which "
      "`wolframscript` does not have, so the extractor emulates Symbolize: before evaluation the box T16^A is replaced by "
      "that same atomic symbol and the box taubar by an atomic stand-in symbol (the name Notation creates for it is not "
      "recorded in the notebook; only atomicity matters). These two box replacements are the only changes to the author's "
      "cells (`notation_emulation`). Below, T16A and taubar name these two symbols.")
    w("")
    w("The construction, in the author's words: `Qa[h,p,q] = Signature[{h,p,q,4}]`, "
      "`Qb[h,p,q] = ID4[[p,4]] ID4[[q,h]] - ID4[[p,h]] ID4[[q,4]]`; `s4by4[h] = Qa - Qb`, `t4by4[h] = Qa + Qb` "
      "(self-dual and anti-self-dual 4 x 4 blocks); `tau[0] = ID8`, `tau[h] = {{0, s4by4[h]}, {s4by4[h], 0}}`, "
      "`tau[7-h] = {{0, t4by4[h]}, {-t4by4[h], 0}}` (h = 1..3), `tau[7] = tau[1]...tau[6]`; "
      "`taubar[A] = sigma . Transpose[tau[A]] . sigma` with `sigma = {{0, I4}, {I4, 0}}`; "
      "and finally **`T16A[A] = {{0, taubar[A]}, {tau[A], 0}}`, A = 0..7** (`construction_tau_taubar`). "
      "Below, Gamma_A = T16A[A].")
    w("")
    w("Coordinates (Revision/SPEC.md section 2): " + ", ".join(
        f"Gamma_{A} = gamma^({COORD_OF_A[A]}) ({ROLE_OF_A[A]}, eta = {eta[A]:+d})" for A in IDX) + ".")
    w("")
    w("**The author's stored outputs** (the outputs saved in the notebook, compared entry by entry with the evaluated "
      "values, `author_stored_outputs`):")
    w("")
    w("| input cell | In[n] | stored output | object | equal |")
    w("|---|---|---|---|---|")
    for c in sorted(so):
        w(f"| {c} | {so[c]['in_label']} | {so[c]['out_label']} | {so[c]['what']} | yes |")
    w(f"| 285 | {labels['285']} | {nbd['stored_Out370']['out_label']} | `{out370[9:-1]}` (unevaluated) | yes |")
    w(f"| 314 | {labels['314']} | {o393['out_label']} | the author's check {{T16A[A1], T16A[B1]}} = 2 eta4488 ID16: "
      f"{o393['true']} x True | yes |")
    w(f"| 325 | {labels['325']} | {nbd['stored_Out406']['out_label']} | the author's projector check: {{True, True, True}} | yes |")
    w("")
    w("## The proofs (every check, exact)")
    w("")
    w("| # | check | result | what is proved |")
    w("|---|---|---|---|")
    for i, (name, ok_, detail) in enumerate(CHECKS, 1):
        w(f"| {i} | `{name}` | {'PASS' if ok_ else 'FAIL'} | {detail.replace('|', '/')} |")
    w("")
    w("### What the scaled commutators generate, and what generates Pin(4,4) (argument)")
    w("")
    w("Notation: Gamma(v) = sum_A v^A Gamma_A, eta(v,v) = sum_A eta_AA (v^A)^2. Pin(4,4) is the group generated by the "
      "unit vectors Gamma(v), eta(v,v) = +-1; Spin(4,4) is its even part. The twisted adjoint action pi(x): Gamma_C -> "
      "e(x) x Gamma_C x^-1 (e = +1 for even, -1 for odd x) maps Pin(4,4) into O(4,4); pi(Gamma(v)) is the reflection in "
      "the hyperplane orthogonal to v (`finite_groups` computes it for v = e_A). Every claim below is either a check of the "
      "table above, a short proof given here, or a standard fact marked *cited*.")
    w("")
    w("1. **Lie algebra.** The 28 matrices S^AB are linearly independent (`S_linearly_independent`). They close under "
      "commutators with the structure constants of so(4,4) (`so44_closure`). The map S^AB -> M^AB, given by the action on "
      "the Gamma's, is an isomorphism onto the 28-dimensional so(4,4) (`S_vector_action`, `M_in_so44`, `M_basis_of_so44`, "
      "`spin_to_so_isomorphism`). So the S^AB span spin(4,4), which is isomorphic to so(4,4).")
    w("2. **Lemma A (block determinants).** Write Lambda in O(4,4) as [[A, B], [C, D]] with the space block (directions "
      "0..3) first, as in the notebook frame. Lambda^T eta Lambda = eta with eta = diag(I4, -I4) gives A^T A - C^T C = I4 "
      "and D^T D - B^T B = I4, so A^T A = I4 + C^T C and D^T D = I4 + B^T B are >= I4, hence |det A| >= 1 and |det D| >= 1. "
      "The block determinants never vanish on O(4,4), so sign det A and sign det D are continuous and constant on each "
      "connected component; with det Lambda they form the sign pattern used below (`exp_vector_action` also verifies the "
      "two identities for every Lambda(theta)). That O(4,4) has exactly four components is *cited*: the polar "
      "decomposition makes O(4,4) homeomorphic to O(4) x O(4) x R^16. Lemma A shows that the four sign patterns tell the "
      "four components apart.")
    w("3. **Lemma B (kernel).** Let pi(x) = I8 for x in Pin(4,4). If x is even, x commutes with every Gamma_A, so x = "
      "lambda I16 (`irreducible_commutant`). Gamma(v)^2 = eta(v,v) I16 = +-I16 gives det Gamma(v) = +-1, so det x = +-1 "
      "and lambda = +-1. If x is odd, x anticommutes with every Gamma_A, so x = lambda T16A[8] (`anticommutant_T16A8`). "
      "But T16A[8] is even, and the even and odd basis products are linearly independent (`256_products_orthonormal`), "
      "so x = 0, which is impossible. Hence ker pi = {+-I16}, and -I16 = exp(2 pi S^01) (`double_cover`). pi is onto "
      "O(4,4) because every element of O(4,4) is a product of reflections (Cartan-Dieudonne, *cited*). So pi is a double "
      "cover, dim Pin(4,4) = 28, and the Lie algebra of Pin(4,4) is spanned by the S^AB.")
    w("4. **Spin_0(4,4).** Each exp(theta S^AB) is a product of two unit vectors (`exp_is_product_of_two_unit_vectors`), "
      "so it lies in Spin(4,4), and it acts as exp(theta M^AB) in SO_0(4,4) (`exp_vector_action`). A connected Lie group is "
      "generated by the exponentials of its Lie algebra (*cited*), so the exp(theta S^AB) generate the identity component "
      "Spin_0(4,4), and pi(Spin_0(4,4)) = SO_0(4,4) because d pi maps the S^AB onto the basis M^AB of so(4,4). Since "
      "-I16 is in Spin_0(4,4), the preimage of SO_0(4,4) is Spin_0(4,4) itself, and the preimage of each component of "
      "O(4,4) is one coset of Spin_0(4,4). So Pin(4,4) has exactly four components and Spin(4,4) has two. Every product of "
      "exponentials lies in Spin_0(4,4) and has pattern (1, 1, 1). This follows from continuity and Lemma A; it is not a "
      "separate computation.")
    w("5. **The products Gamma_A Gamma_B = 2 S^AB (group elements).** `products_components`: the 12 rotation products have "
      "pattern (1, 1, 1) and equal exp(pi S^AB), so they lie in Spin_0(4,4). The 16 boost products have pattern "
      "(1, -1, -1), so they lie in Spin(4,4) but not in Spin_0(4,4). `finite_groups`: the 28 products generate a finite "
      "group of order 256 that meets exactly two components (128 + 128). The eight Gamma_A generate a group of order 512 "
      "that meets all four (4 x 128). So exp(theta S^AB) together with one boost product (for example Gamma_0 Gamma_4) "
      "generate Spin(4,4), and no product of even elements reaches the two odd components.")
    w("6. **All of Pin(4,4).** `pin44_four_components` shows that I16, Gamma_0, Gamma_4 and Gamma_0 Gamma_4 lie in the four "
      "different components. Transitivity, by explicit construction: let v = (x, y) with x in R^4 (directions 0..3), "
      "y in R^4 (directions 4..7) and eta(v,v) = |x|^2 - |y|^2 = +1, so x != 0. Pick R1 in SO(4) with R1 e_0 = x/|x|, and "
      "R2 in SO(4) with R2 e_4 = y/|y| (R2 = I if y = 0). Let L be the boost in the (0,4) plane with cosh phi = |x|, "
      "sinh phi = |y|. Then diag(R1, R2) L e_0 = v, and diag(R1, R2) and L lie in SO_0(4,4). For eta(v,v) = -1, exchange the roles "
      "of e_0 and e_4. For g in Spin_0(4,4) over this element, g Gamma_0 g^-1 = Gamma(v) (or g Gamma_4 g^-1 = Gamma(v)). "
      "So every unit vector Gamma(v) lies in the group generated by Spin_0(4,4), Gamma_0 and Gamma_4. Hence "
      "**Pin(4,4) = <exp(theta S^AB), Gamma_0, Gamma_4> = <exp(theta S^AB), Gamma_A Gamma_B, Gamma_0>**; the second form "
      "holds because Gamma_4 = Gamma_0 (Gamma_0 Gamma_4). In short: the exponentials of the scaled commutators generate "
      "exactly Spin_0(4,4); adding the products Gamma_A Gamma_B gives Spin(4,4); one Dirac matrix is still needed for "
      "Pin(4,4). We state this restriction plainly rather than claim more than is proved.")
    w("7. **Invariants.** S^AB is real and (S^AB)^T sigma16 + sigma16 S^AB = 0 (`S_preserves_sigma16`); integrated, "
      "g^T sigma16 g = sigma16 for every exp(theta S^AB) (`exp_preserves_sigma16`). So both Psi^T sigma16 Psi (the "
      "author's bilinear; the author's Psi16 = (f16[i][x0, x4]) has commuting components, input cell 43) and "
      "Psi^dagger sigma16 Psi = Psibar Psi (Revision/SPEC.md: Psibar = Psi^dagger C, C = sigma16) are invariant under "
      "Spin_0(4,4). Because sigma16 is symmetric, Psi^T sigma16 Psi vanishes identically for anticommuting components; "
      "for the Grassmann Psi of dirac16complex the invariant is Psibar Psi. The boost products Gamma_A Gamma_B map "
      "sigma16 to -sigma16 (`products_components`), so neither bilinear is invariant under all of Spin(4,4). "
      "[T16A[8], S^AB] = 0, so the two chiral halves P_L Psi and P_R Psi are invariant under Spin_0(4,4); they are "
      "irreducible and inequivalent there (`even_part_two_halves`). The 256 products form a basis of M16(R), so the "
      "16-dimensional representation is irreducible under Pin(4,4) (`irreducible_commutant`).")
    w("")
    w("## The eight real 16 x 16 Dirac matrices")
    w("")
    for A in IDX:
        w(f"### Gamma_{A} = T16A[{A}] = gamma^({COORD_OF_A[A]}) - {ROLE_OF_A[A]}, Gamma_{A}^2 = {'+' if eta[A] > 0 else '-'}I16")
        w("")
        w("```text")
        w(fmt_matrix(G[A]))
        w("```")
        w("")
    w("## Products")
    w("")
    w("### sigma16 = Gamma_0 Gamma_1 Gamma_2 Gamma_3 (the author's bilinear form, = C of Revision/SPEC.md, = diag(-sigma, sigma))")
    w("")
    w("```text")
    w(fmt_matrix(sigma16))
    w("```")
    w("")
    w("### T16A[8] = Gamma_0 Gamma_1 ... Gamma_7 (chirality, = diag(-I8, I8))")
    w("")
    w("```text")
    w(fmt_matrix(T8))
    w("```")
    w("")
    w("### The 28 pairwise products Gamma_A Gamma_B = 2 S^AB (A < B)")
    w("")
    w("These are group elements (elements of Spin(4,4)). The scaled commutators are the Lie-algebra elements "
      "S^AB = (1/2) Gamma_A Gamma_B. Each heading gives the component of Spin(4,4) that the product lies in "
      "(`products_components`).")
    w("")
    for A, B in pairs:
        if eta[A] == eta[B]:
            kind = f"rotation, (Gamma_A Gamma_B)^2 = -I16, = exp(pi S^{A}{B}), in Spin_0(4,4)"
        else:
            kind = "boost, (Gamma_A Gamma_B)^2 = +I16, pattern (1, -1, -1): in Spin(4,4), not in Spin_0(4,4)"
        w(f"#### Gamma_{A} Gamma_{B} = 2 S^{A}{B} ({kind})")
        w("")
        w("```text")
        w(fmt_matrix(mul(G[A], G[B])))
        w("```")
        w("")
    w("### All 256 ordered basis products (compact form)")
    w("")
    w("Each product Gamma_{A1}...Gamma_{Ak} (A1 < ... < Ak) is a signed permutation matrix. It is written on one line as 16 entries: "
      "entry i is +j or -j, meaning row i has its single nonzero entry, +1 or -1, in column j. "
      "Example: `I16` is `+1 +2 ... +16`. These 256 matrices are a basis of M16(R) (`256_products_orthonormal`).")
    w("")
    w("```text")
    for s in subsets:
        label = ("I16" if not s else "G" + ".".join(str(a) for a in s)).ljust(17)
        w(f"{label} {signed_perm(prods[s])}")
    w("```")
    w("")
    w("## Projection matrices")
    w("")
    w("The relevant projectors are the author's chiral projectors P_L, P_R, the projectors (I16 +- sigma16)/2 and the "
      "projectors (I16 +- B)/2 onto the eigenspaces of the Krein matrix B = -i sigma16 Gamma_4. The Revision calculations "
      "use the last two kinds ((1 +- C)/2 and (I16 + B)/2); B is complex, so it is not one of the real Dirac matrices.")
    w("")
    w(f"### P_L = (I16 - T16A[8]) / 2 (author input cell 323, {labels['323']}) = diag(I8, 0)")
    w("")
    w("```text")
    w(fmt_matrix(PL))
    w("```")
    w("")
    w(f"### P_R = (I16 + T16A[8]) / 2 (author input cell 324, {labels['324']}) = diag(0, I8)")
    w("")
    w("```text")
    w(fmt_matrix(PR))
    w("```")
    w("")
    w("### Q_+ = (I16 + sigma16) / 2 (real, rank 8, commutes with P_L and P_R; `projectors_sigma16`)")
    w("")
    w("```text")
    w(fmt_matrix(Qp))
    w("```")
    w("")
    w("### Q_- = (I16 - sigma16) / 2")
    w("")
    w("```text")
    w(fmt_matrix(Qm))
    w("```")
    w("")
    w("### Im B, where B = -i sigma16 Gamma_4 = -i Gamma_0 Gamma_1 Gamma_2 Gamma_3 Gamma_4 (Re B = 0; `krein_B`)")
    w("")
    w("```text")
    w(fmt_matrix(negM5))
    w("```")
    w("")
    w("### Im Pi_+, where Pi_+ = (I16 + B) / 2 = I16/2 + i Im Pi_+ (complex, Hermitian, rank 8; `projectors_B`)")
    w("")
    w("```text")
    w(fmt_matrix(Pp[1]))
    w("```")
    w("")
    w("### Im Pi_-, where Pi_- = (I16 - B) / 2 = I16/2 + i Im Pi_-")
    w("")
    w("```text")
    w(fmt_matrix(Pm[1]))
    w("```")
    w("")
    w("## How the author's Lagrangians use these matrices")
    w("")
    w("A scan of all 996 input cells of the notebook (by the extractor, with commented-out code removed) finds where each "
      "symbol is assigned and used (`chain_assignments`, `chain_lagrangians`, `projectors_only_in_checks`). The chain is: "
      "T16A -> SAB, sigma16 and the curved matrices T16alpha = e_A^alpha T16A (-> useT16) -> the Lagrangians Lg[], La[], "
      "Lj[] -> the field equations eLa. The Lagrangians never use T16A directly.")
    w("")
    w("| input cell | In[n] | assigns (scan) | uses (scan) | role |")
    w("|---|---|---|---|---|")
    for c in sorted(chain):
        ch = chain[c]
        w(f"| {c} | {ch['label']} | {', '.join(ch['assigns']) or '-'} | {', '.join(ch['refs'])} | "
          f"{CHAIN_ROLE[c].replace('|', '/')} |")
    w("")
    w(f"P_L and P_R are used only in input cells {cells_text(sorted(set(ref['P_L'] + ref['P_R'])), labels)}: their "
      f"definitions and the author's check. The named T16A[8] appears only in input cells "
      f"{cells_text(ref['T16A[8]'], labels)}, which are its definition, P_L, P_R and checks. Its value is also element 255 "
      "of base16 (the author's check in input cell 479), and Lj[j] indexes base16.")
    w("")
    w("## Every other copy of these matrices in the repository")
    w("")
    w("Each source below is loaded or constructed and compared entry by entry with the matrices evaluated from the "
      "author's notebook (checks `fixture_Revision_algebra_gammas_json` to `old_stage_wolfram_packages`).")
    w("")
    w("The column *read by* gives examples found by a repository search when this generator was written; it is not "
      "re-checked by `--check` (the files are owned by other workflows).")
    w("")
    w("| check | source | kind | read by (examples) | compared | coordinate map | result |")
    w("|---|---|---|---|---|---|---|")
    for name, source, kind, readers, shown, cmap, result in sources:
        w(f"| `{name}` | `{source}` | {kind} | {readers} | {shown} | {cmap} | {result} |".replace("\n", " "))
    w("")
    w("## Calculations that use these matrices")
    w("")
    w("The Revision calculations and the textbook notebooks read their gamma matrices from `Revision/algebra/gammas.json` "
      "(compared above), or from the report `Revision/algebra/reports/python-gammas.json` (compared above). The "
      "earlier-stage calculations read `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` or build their own "
      "copy in Python, Wolfram or Rust (all compared above). The textbook notebook source "
      "`Revision/textbook/notebooks/src/04a_t16_from_formulas.py` contains its own re-typed construction inside the "
      "notebook (owned by the textbook workflow); this file does not execute or compare it.")
    w("")
    w("The list of files that read `gammas.json` is deliberately not part of this file, because other workflows keep adding "
      "such files. `python provenance/dirac_matrices/build_dirac_matrices_md.py --list-consumers` prints the current list.")
    w("")
    text = "\n".join(L) + "\n"
    print(f"{n_checks} of {n_checks} checks pass")
    if "--check" in sys.argv:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else None
        if current != text:
            print(f"OUT OF DATE: {OUT.relative_to(ROOT).as_posix()} differs from the regenerated text")
            return 1
        print(f"{OUT.relative_to(ROOT).as_posix()} is up to date")
        return 0
    OUT.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {OUT.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
