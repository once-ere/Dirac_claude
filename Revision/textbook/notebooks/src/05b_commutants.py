#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 05b, "Commutants: Pin(4,4) is irreducible, Spin(4,4) splits"
(textbook "Universes in Pairs").

The notebook Revision/textbook/notebooks/05b_commutants.ipynb is BUILT from this file by
Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/05b_commutants.py --date YYYY-MM-DD --scratch DIR
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/05b_commutants.py --scratch DIR

It reads Revision/algebra/gammas.json and repeats, with its own exact linear algebra
(sympy DomainMatrix over the rational numbers) and a numerical second engine (numpy), the
representation checks of Revision/algebra/reports/python-algebra.json and
wolfram-algebra.json: the 256 Clifford products span all 16 x 16 matrices, the commutant of
the gammas is one-dimensional (Pin(4,4) irreducible), the commutant of the S^ab is
two-dimensional, the two chiral halves are irreducible and inequivalent.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FACTS = {
    "id": "05b",
    "name": "05b_commutants",
    "title": "Commutants: Pin(4,4) acts irreducibly, Spin(4,4) splits into two "
             "inequivalent halves",
    "purpose": (
        "It turns the matrix equations X M = M X into systems of linear equations for "
        "the 256 entries of an unknown 16 by 16 matrix X, solves them exactly, and so "
        "computes: the rank of the 256 Clifford products, the commutant of the eight "
        "gammas (dimension 1: the 16 components carry an irreducible representation of "
        "Pin(4,4)), the commutant of the 28 generators S^ab (dimension 2, spanned by the "
        "chiral projectors), the commutants of the two halves (1 and 1) and the "
        "intertwiners between them (0 and 0: inequivalent halves), with a negative "
        "control that shows what equivalent halves would give. Five teaching plots show "
        "the counts, the eigenvalues of the equation systems and the dimensions."
    ),
    "records": [
        ["Revision/algebra/gammas.json",
         "the author's gamma matrices in the coordinate order x1 to x8 (read)"],
        ["Revision/algebra/reports/python-algebra.json",
         "the exact Python checks (reproduced: clifford_products_span_M16, "
         "even_products_span_M8_plus_M8, pin_commutant_dimension_1, "
         "spin_commutant_dimension_2, spin_halves_irreducible, spin_halves_inequivalent "
         "and others)"],
        ["Revision/algebra/reports/wolfram-algebra.json",
         "the exact WolframScript checks of the same statements (reproduced)"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 30,
    "timeout_seconds": 600,
    "files_written": [
        "Revision/textbook/figures/05b.captions.json",
        "Revision/textbook/figures/05b_1_clifford_products.png",
        "Revision/textbook/figures/05b_2_system_eigenvalues.png",
        "Revision/textbook/figures/05b_3_commutant_halving.png",
        "Revision/textbook/figures/05b_4_spin_commutant.png",
        "Revision/textbook/figures/05b_5_dimensions.png",
    ],
    "final_lines": [
        "PASS the five figure files of notebook 05b exist",
        "ALL 16 CHECKS PASSED (notebook 05b)",
    ],
    "troubleshooting": [
        ["\"FileNotFoundError\" naming Revision/algebra/gammas.json",
         "the notebook was opened outside the repository, or the repository is "
         "incomplete; clone the repository again and open the notebook from its folder "
         "Revision/textbook/notebooks."],
        ["the cells of sections 9 and 11 take much longer than a few seconds",
         "they solve 7168 linear equations exactly; on a slow computer they may take "
         "a minute. Wait until the star in the brackets left of the cell turns into a "
         "number."],
    ],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    The 16 components of the author's spinor field are acted on by two groups of
    $16 \times 16$ matrices: **Pin(4,4)**, made of products of gamma matrices, and its
    subgroup **Spin(4,4)**, made of products of an *even* number of them. The Revision
    record states, and this notebook verifies with its own exact computation:

    1. the $2^8 = 256$ products of different gammas are linearly independent, so they
       span all $16 \times 16$ matrices;
    2. only the multiples of the identity commute with all eight gammas (the
       *commutant* has dimension 1): the 16 components form an **irreducible**
       representation of Pin(4,4);
    3. the matrices that commute with all 28 generators $S^{ab}$ of Spin(4,4) form a
       space of dimension 2, spanned by the two chiral projectors $P_-$ and $P_+$:
       under Spin(4,4) the 16 components split into two halves of 8;
    4. each half is irreducible (commutant dimension 1), and the two halves are
       **inequivalent**: the only matrix that carries one half into the other while
       respecting Spin(4,4) is zero.

    The method is the same for every statement: a matrix equation such as
    $X\gamma^a = \gamma^a X$ for an unknown matrix $X$ is a system of *linear
    equations* for the 256 entries of $X$, and the number of independent solutions is
    256 minus the *rank* of the system. Every check that repeats a recorded check
    prints the record file and the check name. Five teaching plots show the counts and
    the dimensions; a negative control shows what the computation would give if the
    two halves were equivalent.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Linear equation, system**: an equation of the form $c_1 y_1 + c_2 y_2 + \dots
      + c_n y_n = 0$ for unknown numbers $y_1, \dots, y_n$ with given coefficients
      $c_j$. A *system* is a list of such equations; its coefficients form the
      **coefficient matrix** $A$ (one row per equation), and the system reads
      $Ay = 0$.
    - **Solution space, dimension**: the set of all solutions $y$ of $Ay = 0$. Sums
      and multiples of solutions are solutions. Its **dimension** is the number of
      solutions needed so that every solution is a combination of them (a
      **basis**).
    - **Rank**: the number of independent rows of $A$ (rows that are not combinations
      of other rows). For $n$ unknowns: dimension of the solution space $= n -
      \text{rank}$.
    - **Exact arithmetic**: computing with fractions, never rounding. The package
      sympy does this (`DomainMatrix` over `QQ`, the rational numbers).
    - **Linearly independent matrices**: no one of them is a combination of the
      others. Writing each $16 \times 16$ matrix as one row of 256 numbers, $N$ matrices
      are independent when these $N$ rows have rank $N$.
    - **Span**: all combinations of a list of matrices.
    - **Clifford product**: a product $\gamma^{a_1}\gamma^{a_2}\cdots\gamma^{a_k}$ of
      $k$ *different* gammas, taken in the order $x1, \dots, x8$; $k$ is its
      **degree**; it is **even** or **odd** with $k$. The degree-0 product is $1$.
    - **Group**: a set of invertible matrices that contains the products and the
      inverses of its members.
    - **Representation, invariant subspace, irreducible**: a group of $16 \times 16$
      matrices *represents* the group on columns of 16 numbers. A set of columns that
      every group matrix maps into itself is *invariant*. The representation is
      **irreducible** when the only invariant subspaces are $\{0\}$ and everything.
    - **Commutant**: all matrices $X$ that commute with every matrix of a list.
    - **Intertwiner**: a matrix $X$ with $X M_k = N_k X$ for two lists of matrices
      $M_k$, $N_k$ (it carries the first representation into the second).
      **Equivalent** representations have an invertible intertwiner.
    - **Schur's lemma** (used here, proved in the text): when the matrices of a
      representation span all matrices, the representation is irreducible and its
      commutant is the multiples of 1; an intertwiner between two irreducible
      representations is zero or invertible.
    - **Generators** $S^{ab} = \tfrac14[\gamma^a, \gamma^b] = \tfrac14(\gamma^a\gamma^b
      - \gamma^b\gamma^a)$: the 28 matrices ($a < b$) from which every element of the
      part of Spin(4,4) connected to 1 is built by exponentials.
    - **Chiral halves**: the components 1 to 8 (chirality $\Gamma = -1$) and 9 to 16
      ($\Gamma = +1$); $P_- = \mathrm{diag}(1_8, 0)$ and $P_+ = \mathrm{diag}(0, 1_8)$.
    - **Kronecker product** `np.kron(L, R)`: the big matrix whose block in block row
      $r$ and block column $k$ is $L_{rk}$ times the whole matrix $R$.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **From a matrix equation to linear equations.** Let $X$ be an unknown $n \times m$
    matrix, $L$ a known $n \times n$ and $R$ a known $m \times m$ matrix, and consider
    $LX - XR = 0$. List the $nm$ entries of $X$ row by row: $X_{11}, X_{12}, \dots,
    X_{1m}, X_{21}, \dots$. The entry $(r, c)$ of the equation is

    $$(LX)_{rc} - (XR)_{rc} = \sum_k L_{rk} X_{kc} - \sum_k X_{rk} R_{kc} = 0 .$$

    In the first sum the unknown $X_{kc}$ has the coefficient $L_{rk}$; in the second
    the unknown $X_{rk}$ has the coefficient $R_{kc}$. Collected over all $(r, c)$,
    these coefficients form the matrix $\mathrm{kron}(L, 1_m) - \mathrm{kron}(1_n,
    R^T)$, with one row per equation and one column per unknown. For a list of pairs
    $(L_j, R_j)$ the coefficient matrices are stacked on top of each other. For the
    commutant of the eight gammas: $n = m = 16$, $L_j = R_j = \gamma^{a}$, so
    $8 \times 256 = 2048$ equations for 256 unknowns.

    **How the two computations prove irreducibility.** Every element of Pin(4,4) is a
    product of matrices $\gamma(u) = \sum_a u_a \gamma^a$, so it is a combination of
    Clifford products; conversely every Clifford product is, up to a sign, an element
    of Pin(4,4) (each $\gamma^a$ is one). So the span of Pin(4,4) is the span of the 256
    Clifford products. *First computation*: if they span all $16 \times 16$ matrices,
    then every invariant subspace is $\{0\}$ or everything (a subspace kept by every
    matrix is $\{0\}$ or everything), and only the multiples of 1 commute with them
    (Schur's lemma in its span form). *Second computation*: the commutant of the eight
    gammas, solved directly; it confirms the second statement independently. For
    Spin(4,4) the even products play the same role: if they span exactly the
    block-diagonal matrices $\mathrm{diag}(X, Y)$, each half is irreducible and the two
    halves are inequivalent (an intertwiner $T$ with $TX = YT$ for all $X$, $Y$ must
    vanish: take $X = 1_8$, $Y = 0$). The commutant of the 28 generators $S^{ab}$, which
    build the part of Spin(4,4) connected to 1, and the intertwiners between the two
    halves are then computed directly, in the form in which the Revision record states
    them.

    **Two halves, equivalent or not.** If the 16 components split into two invariant
    halves of 8 and each half is irreducible, the commutant has dimension 2 when the
    halves are inequivalent ($X = p P_- + q P_+$) and dimension 4 when they are
    equivalent (then a matrix that carries one half onto the other also commutes).
    The notebook computes both the real case and an artificial *control* with two
    equal halves.

    **A second engine.** For a coefficient matrix $A$ the matrix $N = A^T A$ is
    symmetric, and $Ny = 0$ exactly when $Ay = 0$: if $Ny = 0$, then
    $0 = y^T N y = (Ay)^T(Ay) = |Ay|^2$, the sum of the squares of the entries of
    $Ay$, so $Ay = 0$; the converse is clear. Hence the dimension of the solution space
    equals the number of zero eigenvalues of $N$, which numpy computes in
    floating-point numbers, independently of sympy.
    """),
    md(r"""
    ## 5. The gammas and the recorded checks

    The next cell reads the gammas from the record `Revision/algebra/gammas.json` (exact
    whole numbers), reads the two Revision reports, and defines the helpers
    `recorded(key, name)` (true when the report `key`, "python" or "wolfram", holds the
    check `name` with the verdict pass), `detail(key, name)` (the detail text of that
    check), `record_of(key, name)` (the text printed after "reproduces") and
    `check_reproduces(condition, name, record)`, the helper `check` for a check that
    reproduces a Revision record: it lets `check` print the PASS line and the line
    "reproduces ..." into a text buffer (`contextlib.redirect_stdout`) and sends both
    lines with one `sys.stdout.write`, because Jupyter delivers printed text in pieces
    and one piece keeps the two lines together for the tools that read the notebook.
    Then it checks the Clifford relation, on which everything below rests.
    """),
    code(r'''
    import contextlib  # lets a block of code print into a text buffer
    import io  # the text buffer io.StringIO
    import sys  # sys.stdout: the channel through which the notebook prints

    import numpy as np  # arrays of numbers, matrices and linear algebra

    fixture = json.loads(repository_file("Revision/algebra/gammas.json")
                         .read_text(encoding="utf-8"))
    COORDS = fixture["coordinates"]  # "x1", ..., "x8"
    ETA = dict(zip(COORDS, fixture["eta"]))  # +1 space-like, -1 time-like
    gamma = {x: np.array(m, dtype=np.int64) for x, m in zip(COORDS, fixture["gamma"])}
    I16 = np.eye(16, dtype=np.int64)  # the identity matrix 1

    REPORT_FILES = {"python": "Revision/algebra/reports/python-algebra.json",
                    "wolfram": "Revision/algebra/reports/wolfram-algebra.json"}
    VERDICTS = {}  # (report key, check name) -> (verdict in lower case, detail text)
    for key, path in REPORT_FILES.items():
        report_data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        for entry in report_data["checks"]:
            VERDICTS[(key, entry["name"])] = (entry["verdict"].lower(), entry["detail"])


    def recorded(key, name):
        """True when the report key records the check name with the verdict pass."""
        return VERDICTS[(key, name)][0] == "pass"


    def detail(key, name):
        """The detail text of the recorded check."""
        return VERDICTS[(key, name)][1]


    def record_of(key, name):
        """The text printed after "reproduces": the record file and the check name."""
        return f"{REPORT_FILES[key]}, check {name}"


    def check_reproduces(condition, name, record):
        """check(condition, name, record=record), printed in one piece."""
        collected = io.StringIO()
        with contextlib.redirect_stdout(collected):  # print into the buffer
            check(condition, name, record=record)  # stops here if the check fails
        sys.stdout.write(collected.getvalue())  # the PASS and reproduces lines together


    clifford_ok = all(
        np.array_equal(gamma[x] @ gamma[y] + gamma[y] @ gamma[x],
                       2 * ETA[x] * I16 if x == y else 0 * I16)
        for x in COORDS for y in COORDS)
    check_reproduces(clifford_ok and recorded("python", "clifford_relation"),
                     "{gamma^a, gamma^b} = 2 eta^ab 1 for all 64 pairs",
                     record=record_of("python", "clifford_relation"))
    '''),
    md(r"""
    ## 6. The tools: equation systems and their exact rank

    The next cell defines three tools.

    - `commutation_system(lefts, rights)` builds the coefficient matrix of the
      equations $L X - X R = 0$ for all pairs $(L, R)$ of the two lists, following
      section 4.
    - `exact_rank(A)` computes the rank of a matrix of whole numbers exactly, with
      sympy's `DomainMatrix` over the rational numbers `QQ` (Gaussian elimination with
      fractions).
    - `solution_basis(A, n, m)` returns a basis of the solutions as $n \times m$
      matrices (sympy's `nullspace`, also exact).

    Then the cell tests the construction: for a random matrix $X$ of whole numbers
    (from a random-number generator with the fixed seed 12345, so every run uses the
    same numbers), the coefficient matrix applied to the entries of $X$ must give the
    entries of $LX - XR$.
    """),
    code(r'''
    import sympy as sp  # exact algebra
    from sympy.polys.matrices import DomainMatrix  # exact matrices over QQ


    def commutation_system(lefts, rights):
        """Coefficient matrix of L X - X R = 0 for every pair (L, R); X is n x m with
        n = size of L and m = size of R; the unknowns are the entries of X row by row."""
        blocks = []
        for L, R in zip(lefts, rights):
            n, m = L.shape[0], R.shape[0]
            blocks.append(np.kron(L, np.eye(m, dtype=np.int64))
                          - np.kron(np.eye(n, dtype=np.int64), R.T))
        return np.vstack(blocks)  # the blocks stacked on top of each other


    def exact_rank(A):
        """The rank of the whole-number matrix A, computed exactly."""
        return DomainMatrix.from_list(A.tolist(), sp.QQ).rank()


    def solution_basis(A, n, m):
        """A basis of all solutions of A y = 0, each reshaped to an n x m matrix."""
        null = DomainMatrix.from_list(A.tolist(), sp.QQ).nullspace().to_Matrix()
        return [np.array(null.row(k).tolist()[0], dtype=float).reshape(n, m)
                for k in range(null.rows)]


    rng = np.random.default_rng(12345)  # random numbers with a fixed seed
    X = rng.integers(-5, 6, size=(16, 16))  # a random 16 x 16 matrix, entries -5..5
    L, R = gamma["x1"], gamma["x4"]
    A = commutation_system([L], [R])
    say(f"one pair (L, R) gives {A.shape[0]} equations for {A.shape[1]} unknowns")
    check(np.array_equal(A @ X.reshape(256), (L @ X - X @ R).reshape(256)),
          "the coefficient matrix applied to X row by row gives L X - X R")
    '''),
    md(r"""
    **A warm-up with $2 \times 2$ matrices.** Which $2 \times 2$ matrices
    $X = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$ commute with
    $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$? By hand: $MX =
    \begin{pmatrix} r & s \\ p & q \end{pmatrix}$ and $XM = \begin{pmatrix} q & p \\ s & r
    \end{pmatrix}$, so $MX = XM$ means $r = q$ and $s = p$: the solutions are
    $\begin{pmatrix} p & q \\ q & p \end{pmatrix}$, a space of dimension 2 (basis: the
    identity and $M$ itself). The next cell gets the same answer from the tools: 4
    equations, rank 2, dimension $4 - 2 = 2$.
    """),
    code(r'''
    M = np.array([[0, 1], [1, 0]], dtype=np.int64)
    A_small = commutation_system([M], [M])  # 4 equations for the 4 entries p, q, r, s
    rank_small = exact_rank(A_small)
    basis_small = solution_basis(A_small, 2, 2)
    say(f"coefficient matrix (rows = equations, columns = p, q, r, s):")
    for row in A_small.tolist():
        say(f"    {row}")
    say(f"rank {rank_small}; dimension of the solution space {4 - rank_small}")
    for k, b in enumerate(basis_small, 1):
        say(f"basis solution {k}: rows {b.astype(int).tolist()}")
    check(rank_small == 2 and len(basis_small) == 2,
          "warm-up: the 2 x 2 matrices commuting with M form a space of dimension 2")
    '''),
    md(r"""
    ## 7. The 256 Clifford products span all 16 x 16 matrices

    The next cell builds the Clifford products of every degree $k = 0, \dots, 8$ (for
    each $k$, `itertools.combinations` lists the $\binom{8}{k}$ subsets of $k$
    directions in the order $x1, \dots, x8$). It writes each product as one row of 256
    numbers and computes exactly the rank of all 256 rows (must be 256: independent),
    of the 128 even ones (must be 128), and the rank after adding the products degree
    by degree. It also checks that every even product is block diagonal (it maps each
    half into itself) and every odd product block off-diagonal (it exchanges the
    halves).
    """),
    code(r'''
    import itertools  # subsets of a given size
    from math import comb  # comb(8, k): the number of subsets of size k

    products = {}  # degree k -> list of the Clifford products of degree k
    for k in range(9):
        products[k] = []
        for subset in itertools.combinations(COORDS, k):
            p = I16
            for x in subset:
                p = p @ gamma[x]
            products[k].append(p)
    rows_all = np.array([p.reshape(256) for k in range(9) for p in products[k]])
    rows_even = np.array([p.reshape(256) for k in (0, 2, 4, 6, 8) for p in products[k]])
    rank_all, rank_even = exact_rank(rows_all), exact_rank(rows_even)
    cumulative = []  # the rank after adding the degrees 0, 1, ..., k
    for k in range(9):
        cumulative.append(exact_rank(np.array(
            [p.reshape(256) for j in range(k + 1) for p in products[j]])))
    for k in range(9):
        say(f"degree {k}: {len(products[k]):2d} products (comb(8, {k}) = {comb(8, k):2d});"
            f" rank of all products up to degree {k}: {cumulative[k]}")
    say(f"rank of all 256 products: {rank_all}; rank of the 128 even products: "
        f"{rank_even}")
    check_reproduces(rank_all == 256 and f"rank {rank_all} (Fraction elimination)"
                     in detail("python", "clifford_products_span_M16")
                     and recorded("python", "clifford_products_span_M16")
                     and recorded("wolfram", "Clifford_basis_spans_full_matrix_algebra"),
                     "the 256 Clifford products are independent: they span all 16 x 16 "
                     "matrices",
                     record=record_of("python", "clifford_products_span_M16"))
    even_diagonal = all(not p[:8, 8:].any() and not p[8:, :8].any()
                        for k in (0, 2, 4, 6, 8) for p in products[k])
    odd_off = all(not p[:8, :8].any() and not p[8:, 8:].any()
                  for k in (1, 3, 5, 7) for p in products[k])
    check_reproduces(rank_even == 128 and even_diagonal and odd_off
                     and f"rank {rank_even} (Fraction)"
                     in detail("python", "even_products_span_M8_plus_M8")
                     and recorded("python", "even_products_span_M8_plus_M8")
                     and recorded("wolfram", "even_subalgebra_dimension"),
                     "the 128 even products are block diagonal and independent (64 + 64); "
                     "the odd "
                     "ones are block off-diagonal",
                     record=record_of("python", "even_products_span_M8_plus_M8"))
    '''),
    md(r"""
    The next cell draws two pictures: the number of Clifford products of each degree
    (even degrees in blue, odd in orange), and the rank after adding the degrees one
    after the other, which climbs exactly along the number of products added: no
    product is a combination of the others.
    """),
    code(r'''
    from matplotlib.patches import Patch  # a coloured square for a legend

    degrees = np.arange(9)
    counts = [len(products[k]) for k in range(9)]
    colors = ["#2a78d6" if k % 2 == 0 else "#eb6834" for k in range(9)]
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    axes[0].bar(degrees, counts, color=colors, edgecolor="white", linewidth=2)
    for k in range(9):
        axes[0].text(k, counts[k] + 1.5, str(counts[k]), ha="center")
    axes[0].set_xlabel("degree $k$ (number of different gammas multiplied)")
    axes[0].set_ylabel("number of products")
    axes[0].set_title(r"$\binom{8}{k}$ products of degree $k$")
    axes[0].set_ylim(0, 80)
    axes[0].legend(handles=[Patch(color="#2a78d6", label="even degree"),
                            Patch(color="#eb6834", label="odd degree")],
                   loc="upper right")
    added = np.cumsum(counts)  # how many products have been added up to degree k
    axes[1].plot(added, cumulative, "o-", color="#2a78d6", linewidth=2, markersize=8,
                 label="exact rank")
    axes[1].plot([0, 256], [0, 256], ":", color="black", linewidth=1,
                 label="rank = number of products")
    axes[1].set_xlabel("number of products added (degrees 0 to $k$)")
    axes[1].set_ylabel("rank")
    axes[1].set_title("The rank grows by one for every product")
    axes[1].legend(loc="upper left")
    save_figure(fig, "clifford_products",
                "Left: the number of Clifford products of each degree $k$ (the number of "
                "different gammas multiplied), which is the binomial number "
                "$\\binom{8}{k}$: 1, 8, 28, 56, 70, 56, 28, 8, 1, in total 256; blue "
                "even degrees, orange odd degrees. Right: the exact rank of all "
                "products of degrees 0 to $k$ (dots) against the number of products "
                "added (horizontal axis); the dots lie on the dotted line rank = "
                "number of products, ending at 256: the 256 products are independent "
                "and span all 16 by 16 matrices.")
    '''),
    md(r"""
    ## 8. The commutant of the eight gammas: Pin(4,4) is irreducible

    The next cell builds the $2048 \times 256$ system $X\gamma^a - \gamma^a X = 0$
    ($a = x1, \dots, x8$; with `commutation_system`, $L = R = \gamma^a$ gives
    $\gamma^a X - X\gamma^a$, the same equations with the opposite sign), computes its
    exact rank and a basis of its solutions, and checks that the only solutions are
    the multiples of the identity.
    """),
    code(r'''
    gammas = [gamma[x] for x in COORDS]
    A_pin = commutation_system(gammas, gammas)  # 8 x 256 = 2048 equations
    rank_pin = exact_rank(A_pin)
    basis_pin = solution_basis(A_pin, 16, 16)
    dimension_pin = 256 - rank_pin
    say(f"equations {A_pin.shape[0]}, unknowns {A_pin.shape[1]}, rank {rank_pin}, "
        f"dimension of the commutant {dimension_pin}")
    only = basis_pin[0]
    proportional = np.array_equal(only / only[0, 0], np.eye(16))  # a multiple of 1?
    say(f"the basis solution divided by its entry (1,1) equals the identity: "
        f"{proportional}")
    check_reproduces(dimension_pin == 1 and len(basis_pin) == 1 and proportional
                     and f"= {dimension_pin} (Fraction)"
                     in detail("python", "pin_commutant_dimension_1")
                     and recorded("python", "pin_commutant_dimension_1")
                     and recorded("wolfram", "Pin44_irreducible_commutant_dim_1"),
                     "only the multiples of 1 commute with all eight gammas: Pin(4,4) acts "
                     "irreducibly on the 16 components",
                     record=record_of("python", "pin_commutant_dimension_1"))
    '''),
    md(r"""
    **The second engine and what its eigenvalues mean.** The next cell computes the
    eigenvalues of $N = A^T A$ ($256 \times 256$) with numpy and counts those below
    $10^{-9}$: by section 4 their number is the dimension of the commutant. The
    eigenvalues can even be predicted exactly. The equations for $\gamma^a$ act on $X$
    as $X \to \gamma^a X - X\gamma^a$; the transposed equations act as $X \to
    \eta_{aa}(\gamma^a X - X\gamma^a)$ (because $(\gamma^a)^T = \eta_{aa}\gamma^a$).
    Take for $X$ a Clifford product $P$. If $\gamma^a$ commutes with $P$, the first
    step gives 0. If it anticommutes, the first step gives $2\gamma^a P$, the second
    $\eta_{aa}(2\gamma^a\gamma^a P - 2\gamma^a P\gamma^a) = \eta_{aa}(2\eta_{aa}P +
    2\eta_{aa}P) = 4P$. So $NP = 4\, n(P)\, P$, where $n(P)$ is the number of gammas
    that anticommute with $P$. By the sign rule for moving a gamma through $k$
    different factors, $n(P) = k$ for even $k$ and $n(P) = 8 - k$ for odd $k$. The cell
    checks $NP = 4n(P)P$ exactly for all 256 products and compares the predicted list
    of eigenvalues with numpy's.
    """),
    code(r'''
    N_pin = A_pin.T @ A_pin  # 256 x 256, whole numbers, symmetric
    eigen_pin = np.linalg.eigvalsh(N_pin.astype(float))  # sorted from small to large
    zeros_pin = int(np.sum(np.abs(eigen_pin) < 1e-9))
    say(f"numpy: eigenvalues of A^T A below 1e-9: {zeros_pin}")
    predicted = []  # the eigenvalue 4 n(P) of every Clifford product P
    exact_eigenvectors = True
    for k in range(9):
        n_anti = k if k % 2 == 0 else 8 - k  # gammas anticommuting with a product
        for p in products[k]:
            predicted.append(4 * n_anti)
            exact_eigenvectors &= np.array_equal(N_pin @ p.reshape(256),
                                                 4 * n_anti * p.reshape(256))
    predicted = np.sort(np.array(predicted))
    values, multiplicities = np.unique(predicted, return_counts=True)
    say("predicted eigenvalues of A^T A, written value x multiplicity:")
    say("    " + ", ".join(f"{v} x {c}" for v, c in zip(values, multiplicities)))
    check(exact_eigenvectors and zeros_pin == 1
          and np.max(np.abs(eigen_pin - predicted)) < 1e-9,
          "A^T A has exactly one zero eigenvalue; every Clifford product P is an "
          "eigenvector with eigenvalue 4 n(P)")
    '''),
    md(r"""
    ## 9. Imposing the gammas one at a time

    How does the commutant shrink as more gammas are required to commute with $X$?
    With no condition, all 256 entries are free. The matrices that commute with one
    gamma, say $\gamma^{(x1)}$, are those that map each of its two eigenspaces
    (eigenvalue $+1$ and $-1$, eight dimensions each) into itself: $8^2 + 8^2 = 128$
    of them. The next cell computes the dimension after imposing $\gamma^{(x1)}$, then
    also $\gamma^{(x2)}$, and so on up to all eight, exactly.
    """),
    code(r'''
    halving = [256]  # dimension of the commutant of the first j gammas, j = 0, 1, ..., 8
    for j in range(1, 9):
        A_j = commutation_system(gammas[:j], gammas[:j])
        halving.append(256 - exact_rank(A_j))
    for j in range(9):
        names = ", ".join(COORDS[:j]) if j else "none"
        say(f"gammas imposed: {j} ({names}); commutant dimension {halving[j]}")
    check(halving == [256 // 2 ** j for j in range(9)],
          "every further gamma halves the commutant: 256, 128, 64, ..., 2, 1")
    '''),
    md(r"""
    ## 10. The generators S^ab and the commutant of Spin(4,4)

    The next cell builds the 28 generators $S^{ab} = \tfrac14[\gamma^a, \gamma^b]$
    ($a$ before $b$ in the order $x1, \dots, x8$). For $a \neq b$ the two gammas
    anticommute, so $[\gamma^a, \gamma^b] = 2\gamma^a\gamma^b$ and $S^{ab} =
    \tfrac12\gamma^a\gamma^b$: its entries are $0$ and $\pm\tfrac12$. It checks these
    recorded facts and that every $S^{ab}$ is block diagonal. For the exact equation
    system it uses the whole-number matrices $2S^{ab} = \gamma^a\gamma^b$, which have
    the same commutant (a matrix commutes with $S$ exactly when it commutes with $2S$).
    """),
    code(r'''
    pairs = [(a, b) for i, a in enumerate(COORDS) for b in COORDS[i + 1:]]  # 28 pairs
    S = {(a, b): (gamma[a] @ gamma[b] - gamma[b] @ gamma[a]) / 4 for a, b in pairs}
    entries = sorted({float(v) for s in S.values() for v in s.flat})
    say(f"{len(S)} generators S^ab; their entries are {entries}")
    check_reproduces(len(S) == 28 and entries == [-0.5, 0.0, 0.5]
                     and all(np.array_equal(S[(a, b)], gamma[a] @ gamma[b] / 2)
                             for a, b in pairs)
                     and recorded("python", "S_definition"),
                     "S^ab = (1/4)[gamma^a, gamma^b] = (1/2) gamma^a gamma^b: 28 matrices "
                     "with "
                     "entries 0, +1/2, -1/2",
                     record=record_of("python", "S_definition"))
    check_reproduces(all(not s[:8, 8:].any() and not s[8:, :8].any() for s in S.values())
                     and recorded("python", "S_block_diagonal"),
                     "every S^ab is block diagonal: it maps each chiral half into itself",
                     record=record_of("python", "S_block_diagonal"))
    '''),
    md(r"""
    The next cell solves $[X, 2S^{ab}] = 0$ for all 28 generators: $28 \times 256 =
    7168$ equations for 256 unknowns. The solution space must have dimension 2 and be
    spanned by $P_-$ and $P_+$: the cell checks that the two basis matrices that sympy
    returns, together with $P_-$ and $P_+$, have rank 2 (they span the same space). The
    second engine counts the zero eigenvalues of $A^T A$.
    """),
    code(r'''
    generators = [(gamma[a] @ gamma[b]).astype(np.int64) for a, b in pairs]  # 2 S^ab
    A_spin = commutation_system(generators, generators)  # 7168 equations
    rank_spin = exact_rank(A_spin)
    basis_spin = solution_basis(A_spin, 16, 16)
    dimension_spin = 256 - rank_spin
    P_minus = np.diag([1] * 8 + [0] * 8)  # diag(1_8, 0): components 1 to 8
    P_plus = np.diag([0] * 8 + [1] * 8)  # diag(0, 1_8): components 9 to 16
    together = np.array([b.reshape(256) for b in basis_spin]
                        + [P_minus.reshape(256), P_plus.reshape(256)])
    same_span = np.linalg.matrix_rank(together) == 2  # four matrices, two directions
    eigen_spin = np.linalg.eigvalsh((A_spin.T @ A_spin).astype(float))
    zeros_spin = int(np.sum(np.abs(eigen_spin) < 1e-9))
    say(f"equations {A_spin.shape[0]}, rank {rank_spin}, dimension {dimension_spin}; "
        f"numpy: zero eigenvalues of A^T A: {zeros_spin}")
    say(f"the basis and P_-, P_+ span the same space: {same_span}")
    check_reproduces(dimension_spin == 2 and zeros_spin == 2 and same_span
                     and f"= {dimension_spin} (Fraction)"
                     in detail("python", "spin_commutant_dimension_2")
                     and recorded("python", "spin_commutant_dimension_2")
                     and recorded("wolfram", "Spin44_commutant_dim_2_chiral_projectors"),
                     "the commutant of the 28 S^ab has dimension 2, spanned by P_- and P_+",
                     record=record_of("python", "spin_commutant_dimension_2"))
    '''),
    md(r"""
    The next cell draws the eigenvalues of $A^T A$ for both systems, sorted from the
    smallest to the largest: for the eight gammas exactly one is zero (the levels 0,
    4, 8, ..., 32 predicted above), for the 28 generators exactly two.
    """),
    code(r'''
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.2))
    for ax, eig, zeros, title in [
            (axes[0], eigen_pin, zeros_pin, "eight gammas (Pin(4,4))"),
            (axes[1], eigen_spin, zeros_spin, "28 generators $S^{ab}$ (Spin(4,4))")]:
        index = np.arange(1, 257)  # the eigenvalues numbered 1 to 256
        ax.plot(index, eig, color="#2a78d6", linewidth=2, label="eigenvalue")
        ax.plot(index[:zeros], eig[:zeros], "o", color="#eb6834", markersize=9,
                label=f"zero eigenvalues: {zeros}")
        ax.set_xlabel("number of the eigenvalue (sorted)")
        ax.set_title(f"$A^T A$ for the {title}")
        ax.legend(loc="lower right")
    axes[0].set_ylabel("eigenvalue of $A^T A$")
    save_figure(fig, "system_eigenvalues",
                "The 256 eigenvalues of $A^T A$, sorted (horizontal axis: their number "
                "from 1 to 256; vertical axis: their value, a pure number), for the "
                "equation system of the commutant of the eight gammas (left) and of "
                "the 28 generators $S^{ab}$ (right). The number of zero eigenvalues "
                "(orange dots) is the dimension of the commutant: one on the left "
                "(only multiples of 1: Pin(4,4) is irreducible), two on the right "
                "(the projectors onto the two halves). On the left the eigenvalues "
                "come in the exact steps 0, 4, 8, ..., 32, four times the number of "
                "gammas that anticommute with a Clifford product.")
    '''),
    md(r"""
    The next cell draws how the commutant shrinks when the gammas are imposed one at
    a time (section 9). The vertical axis is logarithmic with base 2, so halving is a
    step of equal size.
    """),
    code(r'''
    fig, ax = plt.subplots(figsize=(7.0, 4.2))
    ax.plot(range(9), halving, "o-", color="#2a78d6", linewidth=2, markersize=8)
    for j in range(9):
        ax.annotate(str(halving[j]), (j, halving[j]), textcoords="offset points",
                    xytext=(8, 4))
    ax.set_yscale("log", base=2)
    ax.set_yticks([1, 4, 16, 64, 256], ["1", "4", "16", "64", "256"])
    ax.set_xticks(range(9), ["none"] + COORDS)
    ax.set_xlabel("gammas imposed, in the order x1, x2, ..., x8 (the last one named)")
    ax.set_ylabel("dimension of the commutant")
    ax.set_title("Each further gamma halves the commutant")
    save_figure(fig, "commutant_halving",
                "The dimension of the space of 16 by 16 matrices that commute with the "
                "gammas imposed so far (vertical axis, logarithmic with base 2), when "
                "the gammas are imposed one at a time in the order $x1$ to $x8$ "
                "(horizontal axis: the last gamma added). Without a condition all 256 "
                "entries are free; every further gamma halves the dimension, and with "
                "all eight only the multiples of the identity remain (dimension 1), "
                "computed exactly.")
    '''),
    md(r"""
    The next cell draws the two basis matrices of the Spin(4,4) commutant as sympy
    returned them, and $P_-$ and $P_+$. The basis matrices may look different from the
    projectors (sympy picks its own basis); the check above showed that both pairs span
    the same space: every matrix that commutes with all $S^{ab}$ is $pP_- + qP_+$, a
    number $p$ on the first half and a number $q$ on the second.
    """),
    code(r'''
    from matplotlib.colors import LinearSegmentedColormap

    SIGNS = LinearSegmentedColormap.from_list("signs", ["#2a78d6", "#f0efec", "#e34948"])
    pictures = [(basis_spin[0], "sympy basis matrix 1"),
                (basis_spin[1], "sympy basis matrix 2"),
                (P_minus, "$P_- = \\mathrm{diag}(1_8, 0)$"),
                (P_plus, "$P_+ = \\mathrm{diag}(0, 1_8)$")]
    fig, axes = plt.subplots(1, 4, figsize=(13.0, 3.9))
    for k, (ax, (matrix, title)) in enumerate(zip(axes, pictures)):
        image = ax.imshow(matrix, cmap=SIGNS, vmin=-1, vmax=1)
        ax.set_title(title)
        ax.set_xticks([0, 7, 15], ["1", "8", "16"])
        ax.set_yticks([0, 7, 15], ["1", "8", "16"])
        ax.axhline(7.5, color="black", linewidth=0.8)
        ax.axvline(7.5, color="black", linewidth=0.8)
        ax.set_xlabel("column")
        if k == 0:
            ax.set_ylabel("row")
        ax.grid(False)
    fig.colorbar(image, ax=axes, ticks=[-1, 0, 1], shrink=0.8, label="matrix entry")
    save_figure(fig, "spin_commutant",
                "Heat maps of the two basis matrices of the commutant of the 28 "
                "generators $S^{ab}$ found by the exact solver (left two) and of the "
                "chiral projectors $P_-$ and $P_+$ (right two); horizontal axis the "
                "column, vertical axis the row (1 to 16); grey $0$, red $+1$ (no "
                "entry is negative). All four are diagonal and constant on each half "
                "(rows 1 to 8 and 9 to 16, separated by the black lines): every matrix "
                "that "
                "commutes with Spin(4,4) is a number times $P_-$ plus a number times "
                "$P_+$.")
    '''),
    md(r"""
    ## 11. The two halves: irreducible and inequivalent

    Every $S^{ab}$ is $\mathrm{diag}(S_-^{ab}, S_+^{ab})$ with $8 \times 8$ blocks. The
    next cell computes, exactly:

    - the commutant of the 28 blocks $S_-^{ab}$ (64 unknowns): dimension 1 means the
      first half is irreducible; the same for the 28 blocks $S_+^{ab}$;
    - the intertwiners $X$ with $X S_+^{ab} = S_-^{ab} X$ and with $X S_-^{ab} =
      S_+^{ab} X$ (with `commutation_system` the pairs are $(S_-, S_+)$ and $(S_+,
      S_-)$): dimension 0 means the only intertwiner is zero, so the halves are
      inequivalent;
    - the **negative control**: the artificial $16 \times 16$ matrices
      $\mathrm{diag}(S_-^{ab}, S_-^{ab})$, two copies of the *same* half. Their
      commutant must have dimension 4 ($X = \begin{pmatrix} p 1_8 & q 1_8 \\ r 1_8 & s 1_8
      \end{pmatrix}$): this shows that the computation would detect equivalent halves.
    """),
    code(r'''
    minus_blocks = [g[:8, :8] for g in generators]  # the blocks of 2 S^ab on half -
    plus_blocks = [g[8:, 8:] for g in generators]  # the blocks of 2 S^ab on half +
    dim_minus = 64 - exact_rank(commutation_system(minus_blocks, minus_blocks))
    dim_plus = 64 - exact_rank(commutation_system(plus_blocks, plus_blocks))
    dim_minus_plus = 64 - exact_rank(commutation_system(minus_blocks, plus_blocks))
    dim_plus_minus = 64 - exact_rank(commutation_system(plus_blocks, minus_blocks))
    Z8 = np.zeros((8, 8), dtype=np.int64)
    doubled = [np.block([[m, Z8], [Z8, m]]) for m in minus_blocks]  # the control
    dim_control = 256 - exact_rank(commutation_system(doubled, doubled))
    say(f"commutant on half -: {dim_minus}; on half +: {dim_plus}")
    say(f"intertwiners: {dim_minus_plus} and {dim_plus_minus}")
    say(f"control (two copies of half -): commutant dimension {dim_control}")
    check_reproduces(dim_minus == 1 and dim_plus == 1
                     and "dimension 1 (sympy 1)"
                     in detail("python", "spin_halves_irreducible")
                     and recorded("python", "spin_halves_irreducible")
                     and recorded("wolfram", "chiral_halves_irreducible"),
                     "each chiral half is an irreducible representation of Spin(4,4)",
                     record=record_of("python", "spin_halves_irreducible"))
    check_reproduces(dim_minus_plus == 0 and dim_plus_minus == 0
                     and "dimension 0 (sympy 0)"
                     in detail("python", "spin_halves_inequivalent")
                     and recorded("python", "spin_halves_inequivalent")
                     and recorded("wolfram", "chiral_halves_inequivalent_intertwiners_0"),
                     "the two halves are inequivalent: the only intertwiner is zero",
                     record=record_of("python", "spin_halves_inequivalent"))
    check(dim_control == 4,
          "negative control: two copies of the same half give commutant dimension 4")
    '''),
    md(r"""
    **Why Pin(4,4) sees one block of 16 and Spin(4,4) two blocks of 8.** The next
    cell checks the recorded fact $\gamma^a P_- = P_+ \gamma^a$: every gamma (an odd
    element of Pin(4,4), a *reflection*) carries the first half into the second and
    back. So no half is invariant under Pin(4,4), while each half is invariant under
    the even elements. Then it draws all the dimensions computed in this notebook.
    """),
    code(r'''
    check_reproduces(all(np.array_equal(gamma[x] @ P_minus, P_plus @ gamma[x])
                         for x in COORDS)
                     and recorded("python", "reflections_exchange_halves"),
                     "gamma^a P_- = P_+ gamma^a: every reflection exchanges the two halves",
                     record=record_of("python", "reflections_exchange_halves"))
    labels = ["Pin(4,4) on all 16", "Spin(4,4) on all 16", "Spin(4,4) on half -",
              "Spin(4,4) on half +", "intertwiners - to +", "intertwiners + to -",
              "control: two equal halves"]
    values = [dimension_pin, dimension_spin, dim_minus, dim_plus, dim_minus_plus,
              dim_plus_minus, dim_control]
    colors = ["#2a78d6"] * 6 + ["#eb6834"]  # blue: the theory, orange: the control
    fig, ax = plt.subplots(figsize=(8.0, 4.4))
    positions = np.arange(len(labels))[::-1]  # the first label at the top
    ax.barh(positions, values, color=colors, edgecolor="white", linewidth=2)
    for y, v in zip(positions, values):
        ax.text(v + 0.06, y, str(v), va="center")
    ax.set_yticks(positions, labels)
    ax.set_xlim(0, 4.6)
    ax.set_xlabel("dimension of the space of solutions")
    ax.set_title("Commutants and intertwiners")
    legend_squares = [Patch(color="#2a78d6", label="the author's spinor (computed)"),
                      Patch(color="#eb6834", label="negative control (artificial)")]
    ax.legend(handles=legend_squares, loc="upper right")
    save_figure(fig, "dimensions",
                "The dimensions computed exactly in this notebook (horizontal axis): "
                "the commutant of Pin(4,4) on the 16 components is 1 (irreducible); "
                "the commutant of Spin(4,4) is 2 (two invariant halves); the "
                "commutant on each half is 1 (each half irreducible); the intertwiners "
                "between the halves are 0 in both directions (inequivalent halves). "
                "The orange bar is the negative control with two copies of the same "
                "half: equivalent halves give 4, so the value 2 above proves "
                "inequivalence.")
    '''),
    md(r"""
    ## 12. The last check

    The last cell checks that the five figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    FIGURES = ["05b_1_clifford_products.png", "05b_2_system_eigenvalues.png",
               "05b_3_commutant_halving.png", "05b_4_spin_commutant.png",
               "05b_5_dimensions.png"]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in FIGURES),
          "the five figure files of notebook 05b exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 13. What this notebook showed

    - A matrix equation $LX = XR$ for an unknown matrix is a system of linear
      equations; its solutions form a space of dimension (number of unknowns) minus
      (rank), and the rank can be computed exactly.
    - The 256 Clifford products of the author's gammas are independent: they span all
      $16 \times 16$ matrices; the 128 even ones are block diagonal and span all
      block-diagonal matrices ($64 + 64$).
    - Only the multiples of 1 commute with all eight gammas: the 16 components carry
      an **irreducible** representation of Pin(4,4). The equation system has exactly
      one zero eigenvalue of $A^T A$, and all its eigenvalues are predicted exactly by
      the sign rule. Each further gamma halves the commutant: 256, 128, ..., 1.
    - The matrices that commute with the 28 generators $S^{ab}$ are exactly
      $pP_- + qP_+$ (dimension 2): under Spin(4,4) the components split into the two
      chiral halves of 8.
    - Each half is irreducible, and the two halves are **inequivalent** (no nonzero
      intertwiner); the negative control with two equal halves gives 4 instead of 2.
      The gammas exchange the halves, which is how the two inequivalent halves of
      Spin(4,4) form one irreducible representation of Pin(4,4).
    - Every one of these numbers equals the number recorded in
      `Revision/algebra/reports/python-algebra.json` and `wolfram-algebra.json`.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
