#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 11b, "The three Lovelock tensors of the author's metric, computed
with GKD" (textbook "Universes in Pairs", chapter 11 "GKD and the Lovelock tensors").

The notebook Revision/textbook/notebooks/11b_lovelock_tensors.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/11b_lovelock_tensors.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/11b_lovelock_tensors.py

Revision sources (read in full before this builder was written):
Revision/gkd_lovelock/code (src/geometry.rs, gkd.rs, lovelock.rs, main.rs, poly.rs,
output.rs), Revision/gkd_lovelock/results/ (PROVENANCE_OF_THE_COMPUTATION.md,
curvature.json, lovelock-tensors.json, lovelock-components.md, lovelock-report.json,
python-lovelock-report.json, wolfram-gkd-report.json), Revision/docs/LOVELOCK_GKD.md,
Revision/docs/METRIC_SELF_CONSISTENCY.md (sections 2 to 5) and
Revision/gkd_lovelock/verification/check_lovelock_gkd.py (the Gauss-Bonnet tensor and the
cubic Lovelock density used in section 9 are the ones of that checker).

Rewritten on 2026-10-18 for the corrected metric of 2026-10-16 (version 2,
Revision/SPEC.md section 1): every component is a polynomial in H, a4', a4'', u = b4'/b4,
v = u' and k = e^(2 a4)/b4; the Riemann tensor has 112 nonzero components, all of them
plane curvatures; every Lovelock tensor is diagonal with x0 = x5 = x6 = x7.  The metric of
2026-10-14 (withdrawn on 2026-10-16) appears only as dated history.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "work_of_the_sums",
    "curvature_of_planes",
    "riemann_matrix",
    "mixing_terms_vanish",
    "lovelock_component_tables",
]

RESULTS = "Revision/gkd_lovelock/results"

FACTS = {
    "id": "11b",
    "name": "11b_lovelock_tensors",
    "title": "The three Lovelock tensors of the author's metric, computed with GKD",
    "purpose": (
        "It builds the Revision Rust program lovelock_gkd with cargo inside the "
        "notebook when the program file is missing (a few seconds, up to a minute on a "
        "slow computer; about a second when it is up to date) and runs it; the program "
        "computes exactly the curvature of the corrected metric of the Revision record "
        "(version 2 of 2026-10-16) and the three Lovelock tensors of Lovelock's "
        "equation (4.38) in eight dimensions with GKD, and the notebook checks that its "
        "four output files are byte for byte the committed Revision records (the "
        "report apart from two floating-point rounding errors, which must stay below "
        "1e-10). Then it recomputes the Christoffel symbols and the Riemann tensor with "
        "sympy (112 nonzero components, every one the curvature of a coordinate plane, "
        "none mixing the time with the hidden direction) and the three Lovelock tensors "
        "and scalars with its own Python GKD sum, compares every component exactly with "
        "the records, reproduces the counters of the Rust sums, repeats the sums of "
        "orders 1 and 2 literally without skipping any term, derives and checks the "
        "expansion of every Lovelock tensor along the column of its free upper label, "
        "and checks that the first Lovelock tensor is -4 times the Einstein tensor, the "
        "second -8 times the Gauss-Bonnet tensor, the third scalar 8 times the cubic "
        "Lovelock density, that the traces obey the trace identity and that the fourth "
        "tensor vanishes; it checks again that every check it quotes from the Revision "
        "records is there with the verdict PASS; it draws five teaching figures, among "
        "them the components of the three tensors on the history of the record. The "
        "Rust program writes its four output files (curvature.json, "
        "lovelock-tensors.json, lovelock-components.md and lovelock-report.json) into "
        "the folder `Revision/gkd_lovelock/code/target/textbook_11b`, inside the Rust "
        "build folder, which git ignores."
    ),
    "records": [
        ["Revision/gkd_lovelock/code",
         "the Rust crate lovelock_gkd, built and run by the notebook (command "
         "`lovelock` with the brute-force check of order 2)"],
        [f"{RESULTS}/curvature.json",
         "the corrected metric, its 21 nonzero Christoffel symbols, the 112 nonzero mixed "
         "Riemann components and the Ricci scalar; reproduced byte for byte and "
         "recomputed with sympy"],
        [f"{RESULTS}/lovelock-tensors.json",
         "every component of the Lovelock tensors P(k) and A(k) and the scalars L(k), "
         "k = 1, 2, 3; reproduced byte for byte and recomputed in Python"],
        [f"{RESULTS}/lovelock-components.md",
         "the same components in LaTeX form; reproduced byte for byte"],
        [f"{RESULTS}/lovelock-report.json",
         "the 27 checks and the counters of the GKD sums; reproduced byte for byte "
         "apart from the two floating-point deviations of its brute-force checks, and "
         "the counters recomputed"],
        [f"{RESULTS}/python-lovelock-report.json",
         "the independent sympy verification (56 checks); its checks on the Riemann "
         "tensor, on the Rust components, on the literal unpruned sums of orders 1 and "
         "2 and on the Einstein, Gauss-Bonnet and cubic identities are reproduced"],
        [f"{RESULTS}/wolfram-gkd-report.json",
         "the independent Wolfram verification (29 checks); its numbers of checks and "
         "of failed checks are quoted and checked"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [
        {"manifest": "Revision/gkd_lovelock/code/Cargo.toml",
         "binaries": ["lovelock_gkd"], "build_minutes": 1},
    ],
    "expected_seconds": 90,
    "timeout_seconds": 900,
    "files_written": ["Revision/textbook/figures/11b.captions.json"] + [
        f"Revision/textbook/figures/11b_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)
    ],
    "final_lines": [
        "PASS all five figure files of the notebook exist",
        "ALL 38 CHECKS PASSED (notebook 11b)",
    ],
    "troubleshooting": [
        ["AssertionError: check failed: the program wrote curvature.json equal to the "
         "Revision record byte for byte (or the same message for one of the other three "
         "files)",
         "The file that the program wrote differs from the committed record. Run "
         "git status in the repository folder to see whether the records or the Rust "
         "source were changed, and restore both with the command below.",
         ["git checkout -- Revision/gkd_lovelock"]],
    ],
    "work_folders": ["Revision/gkd_lovelock/code/target/textbook_11b"],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Einstein's field equations equate the Einstein tensor $G$, built from the curvature
    of space-time, to the energy and momentum of matter. In eight dimensions Lovelock's
    theorem allows two more tensors of the same kind, built from products of two and of
    three curvature tensors. Together with Einstein's they are the three **Lovelock
    tensors** $P_{(1)}, P_{(2)}, P_{(3)}$ of Lovelock's equation (4.38), which the
    author's notebook quotes. This notebook computes them for the corrected metric of
    the Revision record, in two independent ways, and checks them. It

    - builds the Revision Rust program `lovelock_gkd` with cargo and runs it: from the
      metric alone it computes exactly the Christoffel symbols, the Riemann tensor and
      the three Lovelock tensors (with GKD, the generalized Kronecker delta), checks 27
      identities, and writes four files; the notebook checks that the four files are,
      byte for byte, the committed Revision records;
    - draws how much work the sums are, and how the program reduces it;
    - recomputes the Christoffel symbols and the Riemann tensor with sympy and compares
      all 112 nonzero components exactly with the record; draws the curvature of every
      coordinate plane and the whole Riemann tensor, and shows why no component mixes
      the time $x_4$ with the hidden direction $x_0$;
    - recomputes the three Lovelock tensors and the three Lovelock scalars in Python
      with its own GKD sum and its own exact polynomial arithmetic, reproduces the
      counters of the Rust sums, and compares all $3 \times 64$ components exactly;
    - repeats the sums of orders 1 and 2 LITERALLY, calling GKD on every ordered
      product of curvature entries without skipping anything, and finds the same
      tensors: the skipping changes nothing;
    - derives, line by line, the expansion of every Lovelock tensor along the column
      of its free upper label, and checks it exactly for $k = 1, 2, 3$;
    - checks three classical identities: $P_{(1)} = -4\,G$ (Einstein),
      $P_{(2)} = -8\,\mathcal{H}$ with the Gauss-Bonnet tensor $\mathcal{H}$, and
      $L_{(3)} = 8 \times$ the cubic Lovelock density; the trace identities; and
      $P_{(4)} = 0$;
    - draws the components of the three normalised Lovelock tensors at one moment of
      the deflating history of the Revision record;
    - reads the Revision verification reports once more and checks that every check
      it quotes from them is there with the verdict PASS.

    It draws five figures and takes about one and a half minutes.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_0, \dots, x_7$ of the author's metric: $x_0$ the hidden
      direction (space-like, listed first), $x_1, x_2, x_3$ ordinary space, $x_4$ the
      time, $x_5, x_6, x_7$ the three extra times. The programs number them
      $0, \dots, 7$ in the same order: the number $k$ stands for $x_k$.
    - **Metric** $g_{ab}$: the table of numbers that gives lengths and times; here it is
      diagonal (only $g_{00}, g_{11}, \dots, g_{77}$ are not zero). **Inverse metric**
      $g^{aa} = 1/g_{aa}$ for a diagonal metric. **Scale factor** $f_a =
      \sqrt{|g_{aa}|}$: the factor by which a coordinate step along $x_a$ is stretched.
    - **Index up, index down**: a tensor component carries upper and lower coordinate
      labels, such as $R^{ab}{}_{cd}$; a label is raised with the inverse metric.
    - **Christoffel symbol** $\Gamma^a{}_{bc}$: the combination of first derivatives of
      the metric that says how the coordinate directions turn from point to point.
    - **Riemann tensor** $R^a{}_{bcd}$: the combination of Christoffel symbols and their
      derivatives that measures curvature. We use mostly $R^{ab}{}_{cd} =
      g^{bb} R^a{}_{bcd}$, which changes sign when $a, b$ or $c, d$ are exchanged.
    - **Curvature of a plane** $K(a, b) = R^{ab}{}_{ab}$ (no sum): the curvature of the
      surface spanned by the directions $x_a$ and $x_b$. A **mixed component** is a
      nonzero $R^{ab}{}_{cd}$ whose lower pair is not the upper pair, such as
      $R^{x_4 x_5}{}_{x_0 x_5}$.
    - **Ricci tensor** $R^h{}_j = \sum_a R^{ha}{}_{ja}$, **Ricci scalar**
      $R = \sum_h R^h{}_h$, **Einstein tensor** $G^h{}_j = R^h{}_j - \tfrac12
      \delta^h{}_j R$.
    - **The six variables**: $H$, $a_4' = da_4/dx_4$, $a_4''$, $u = b_4'/b_4$,
      $v = du/dx_4$ and $k = e^{2a_4}/b_4$. In code they are the symbols `H`, `A1`,
      `A2`, `U`, `V`, `K`.
    - **Generalized Kronecker delta, GKD**: the number $+1$, $-1$ or $0$ that weights
      every term of the Lovelock sums (built and tested in Notebook 11a).
    - **Lovelock tensor** $P_{(k)}{}^h{}_j$ of order $k$, **Lovelock scalar**
      $L_{(k)}$: defined in section 4. **Gauss-Bonnet tensor**: the classical name of
      the order-2 Lovelock tensor.
    - **Exact**: computed with whole numbers and fractions, without rounding.
      **Polynomial, monomial**: a polynomial is a sum of monomials, each a number times
      powers of symbols such as $H^2 a_4'^2$.
    - **Brute force**, **literal sum**: a computation that tries every case without any
      shortcut. **Skipping** (pruning): leaving out terms that are known to be zero.
    - **Expansion of a determinant along a column** (Laplace's rule): the determinant
      equals the sum, over the entries of one column, of the entry times
      $(-1)^{\text{row} + \text{column}}$ times the determinant of the smaller matrix
      that is left when the entry's row and column are removed (its **minor**).
      Exchanging two neighbouring rows of a matrix changes the sign of its determinant.
    - **Revision record**: a file committed under `Revision/` that holds a result.
      **Byte for byte**: two files equal in every byte.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The metric.** The corrected primordial metric of the Revision record (version 2
    of 2026-10-16) is diagonal,

    $$g = \mathrm{diag}\big(e^{-2a_4} b_4 \cot^2 z,\ e^{2a_4},\ e^{2a_4},\ e^{2a_4},\
      -1,\ -e^{-2a_4} b_4 w,\ -e^{-2a_4} b_4 w,\ -e^{-2a_4} b_4 w\big),\qquad
      w = (\sin^2 z)^{1/6},\quad z = 6 H x_0,$$

    in the order $x_0, \dots, x_7$, with a constant $H > 0$ and two functions
    $a_4(x_4)$ and $b_4(x_4) > 0$ of the time ($b_4$ is never 1); $z$ takes every real
    value, and $w$ is the positive sixth root of $\sin^2 z$. The signature is (4,4)
    wherever $\sin z \cos z \neq 0$. Lengths along ordinary space carry the scale
    factor $e^{a_4}$ (it INFLATES as $a_4$ grows); lengths along the three extra times
    the factor $e^{-a_4} b_4^{1/2} (\sin^2 z)^{1/12}$ (they DEFLATE), and the hidden
    direction the factor $e^{-a_4} b_4^{1/2} |\cot z|$: it shrinks together with the
    extra times. The volume factor is $\sqrt{|\det g|} = e^{-a_4} b_4^2 |\cot z|
    (\sin^2 z)^{1/4}$. The Revision record uses the prescribed history
    $a_4 = H x_4$, $b_4 = e^{(4/3) H x_4}$, on which $a_4' = H$, $u = b_4'/b_4 = 4H/3$
    and $k = e^{2a_4}/b_4 = e^{(2/3) H x_4}$. (The metric of 2026-10-14, with the
    factor $\sin^{1/3} z$ on 3-space and $\cot^2 z$ alone as $g_{00}$, was withdrawn on
    2026-10-16; this notebook does not use it.)

    **Derivatives along $x_0$.** Write $C = \cot z$ and $W = (\sin^2 z)^{1/12} > 0$, so
    that $g_{00} = e^{-2a_4} b_4 C^2$ and $g_{55} = -e^{-2a_4} b_4 W^2$. For every real
    $z$ with $\sin z \neq 0$ the chain rule gives

    $$\frac{dC}{dx_0} = -\frac{6H}{\sin^2 z} = -6H\,(1 + C^2),\qquad
      \frac{dW}{dx_0} = \frac{1}{12}(\sin^2 z)^{-11/12}\, 2 \sin z \cos z \cdot 6H
      = H\, C\, W .$$

    So sympy can treat $C$ and $W$ as unknown functions of $x_0$ and replace their
    derivatives by these two rules: no absolute values and no case distinctions are
    needed.

    **Curvature** (the convention of Misner, Thorne and Wheeler, used by the Revision):

    $$\Gamma^a{}_{bc} = \tfrac12 g^{aa}\big(\partial_b g_{ac} + \partial_c g_{ab}
      - \partial_a g_{bc}\big),$$

    $$R^a{}_{bcd} = \partial_c \Gamma^a{}_{db} - \partial_d \Gamma^a{}_{cb}
      + \sum_e \big(\Gamma^a{}_{ce} \Gamma^e{}_{db} - \Gamma^a{}_{de} \Gamma^e{}_{cb}\big),
      \qquad R^{ab}{}_{cd} = g^{bb} R^a{}_{bcd}.$$

    (For a diagonal metric the sum $g^{ad}(\dots)$ of the general formula keeps only
    $d = a$.) The derivatives of $a_4$ and $b_4$ are written with the six variables:
    $b_4' = u\, b_4$, $b_4'' = (v + u^2)\, b_4$ and $e^{2a_4} = k\, b_4$.

    **Lovelock's equation (4.38)** gives, for $n$ dimensions with $n = 2m$ even, the
    tensors

    $$P_{(k)}{}^h{}_j = \sum \delta^{h\, h_1 \dots h_{2k}}_{j\, j_1 \dots j_{2k}}\,
      R^{j_1 j_2}{}_{h_1 h_2} \cdots R^{j_{2k-1} j_{2k}}{}_{h_{2k-1} h_{2k}},$$

    where the sum runs over all $4k$ labels $h_1, \dots, h_{2k}, j_1, \dots, j_{2k}$ and
    $\delta$ is the generalized Kronecker delta with the upper list
    $(h, h_1, \dots, h_{2k})$ and the lower list $(j, j_1, \dots, j_{2k})$. The orders
    are $k = 1, \dots, m - 1$; for $n = 8$, $m = 4$ and $k = 1, 2, 3$. The **Lovelock
    scalar** $L_{(k)}$ is the same sum without the free pair $h, j$. The equation itself
    (with constants $\alpha_k$ and $\lambda$) is written with the densities
    $A_{(k)}{}^{lh} = \sqrt{|\det g|}\, g^{ll} P_{(k)}{}^h{}_l$; the usual normalisation
    is $E_{(k)} = -P_{(k)}/2^{k+1}$, so that $E_{(1)}$ is Einstein's tensor $G$. The
    field equations for $a_4$ and $b_4$ built from them are the subject of chapter 12.

    **Why the sum must be organised.** Written literally, each component is a sum over
    $8^{4k}$ lists of labels: $8^{12} \approx 6.9 \times 10^{10}$ terms per component for
    $k = 3$. Two facts make it small. First, a term with a vanishing curvature factor
    vanishes, so only the 112 nonzero $R^{ab}{}_{cd}$ need to be combined. Second, a
    term in which a label repeats in the upper or in the lower list has GKD $= 0$
    (Notebook 11a), so such combinations are skipped as soon as they appear. Every term
    that remains is weighted by an explicit call of GKD. The Rust program and the Python
    code of section 8 both follow this plan, written independently; the program also
    checks it against the literal, unpruned sum for $k = 1$ and $k = 2$ at a numerical
    point ("brute force").

    **Status.** The tensors are exact polynomials, computed by two independent programs
    and verified again by the Revision's sympy and Wolfram checks (records
    `python-lovelock-report.json`, 56 checks, and `wolfram-gkd-report.json`, 29 checks):
    PROVED by exact computation. No physical assumption enters this notebook: it is the
    geometry of the given metric.
    """),
    md(r"""
    ## 5. The Rust program `lovelock_gkd`

    The next cell builds the program with cargo, through the helper `rust_program` of the
    set-up cell (it runs `cargo build --release` for the crate
    `Revision/gkd_lovelock/code` and returns the path of the program file). When the
    program file is missing, cargo compiles it: 4 seconds on the computer that built the
    book, up to a minute on a slow computer. When the program is up to date, cargo only
    checks that, in about a second. The crate has no dependencies, so cargo downloads
    nothing.
    """),
    code(r'''
    program = rust_program("Revision/gkd_lovelock/code/Cargo.toml", "lovelock_gkd")
    '''),
    md(r"""
    The next cell runs `lovelock_gkd lovelock --output FOLDER --brute-force-k2`. FOLDER
    is `Revision/gkd_lovelock/code/target/textbook_11b`, inside the crate's build folder
    `target`, which git ignores; so the run adds no file to the repository. The program
    computes everything exactly from the metric, runs its 27 checks (the option
    `--brute-force-k2` adds the literal unpruned sum of order 2 over 1,073,741,824 index
    lists at one numerical point) and writes four files: `curvature.json`,
    `lovelock-tensors.json`, `lovelock-components.md` and `lovelock-report.json`. It
    takes about 15 seconds.

    The program prints one line per check (`PASS - name: detail` or `FAIL - ...`), one
    line per order $k$ with its counters and run time, and an information line with the
    eighth-order scalar $L_{(4)}$. The cell prints the names of the checks with their
    verdicts and the number of terms of $L_{(4)}$ (section 9 prints the scalar itself);
    it leaves out the run times, which differ from run to run. `re.match` and
    `re.split` read parts of a line with a pattern (a regular expression).
    """),
    code(r'''
    import re  # regular expressions: patterns that read parts of a line of text

    RESULTS = "Revision/gkd_lovelock/results"  # the folder of the Revision records
    OUT_FOLDER = REPO / "Revision" / "gkd_lovelock" / "code" / "target" / "textbook_11b"
    completed = subprocess.run(
        [str(program), "lovelock", "--output", str(OUT_FOLDER), "--brute-force-k2"],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    rust_checks = []  # (name, verdict) of every check the program printed
    for line in completed.stdout.splitlines():
        found = re.match(r"(PASS|FAIL) - (\w+): ", line)
        if found:
            rust_checks.append((found.group(2), found.group(1)))
        if line.startswith("info - L_(4)"):
            l4_text = line.split("): ", 1)[1]  # the formula after the explanation
    say("The checks of the Rust program (name, verdict):")
    for number, (name, verdict) in enumerate(rust_checks, 1):
        say(f"  {number:2d} {name:34s} {verdict}")
    l4_terms = len(re.split(r" [+-] ", l4_text))  # the terms, separated by + and -
    report("terms of the eighth-order scalar L(4) printed by the program", l4_terms)
    check(completed.returncode == 0 and "lovelock: SUCCESS" in completed.stdout,
          "the Rust program lovelock_gkd lovelock ended with SUCCESS")
    check(len(rust_checks) == 27 and all(v == "PASS" for _, v in rust_checks),
          "all 27 checks of the Rust program passed",
          record=f"{RESULTS}/lovelock-report.json, checkCount 27, failedCheckCount 0")
    '''),
    md(r"""
    The next cell compares the four files that the program has just written with the
    committed Revision records in `Revision/gkd_lovelock/results`, byte for byte
    (`read_bytes()` reads a file as a sequence of bytes). Equal bytes mean that the
    program, built on this computer, has reproduced every symbol of the Revision's
    results.

    The first three files hold only exact whole numbers and fractions, so they must be
    equal byte for byte on every computer. The fourth, `lovelock-report.json`, holds
    two decimal numbers: the largest relative deviation between the exact $P_{(1)}$,
    $P_{(2)}$ and their literal brute-force sums, evaluated in floating point at one
    numerical point (in the record $7.86 \times 10^{-16}$ and $3.57 \times 10^{-13}$,
    rounding errors of the decimal arithmetic). The last digits of such rounding errors
    depend on the mathematics library of the operating system (the functions $\sin$
    and $\cos$) and on the order in which the computer adds the terms. So the cell
    compares this file byte for byte after replacing these two numbers by the letter X
    in both texts (`re.sub`), and checks separately that both numbers are below the
    program's own limit $10^{-10}$. The cell does not print the two numbers, so that
    its output is the same on every computer.
    """),
    code(r'''
    DEVIATION = re.compile(r"(max relative deviation from the exact P_\(\d\) = )"
                           r"([0-9.]+e[-+]?\d+)")  # the two floating-point numbers
    for file_name in ("curvature.json", "lovelock-tensors.json",
                      "lovelock-components.md"):
        written = (OUT_FOLDER / file_name).read_bytes()
        stored = repository_file(f"{RESULTS}/{file_name}").read_bytes()
        report(f"size of {file_name}", len(written), "bytes")
        check(written == stored,
              f"the program wrote {file_name} equal to the Revision record byte for byte",
              record=f"{RESULTS}/{file_name} (the whole file)")
    written = (OUT_FOLDER / "lovelock-report.json").read_text(encoding="utf-8")
    stored = repository_file(f"{RESULTS}/lovelock-report.json").read_text(
        encoding="utf-8")
    deviations = [float(number) for _, number in DEVIATION.findall(written)]
    masked_written = DEVIATION.sub(r"\1X", written)  # the two numbers replaced by X
    masked_stored = DEVIATION.sub(r"\1X", stored)
    report("size of lovelock-report.json", len(written.encode("utf-8")), "bytes")
    check(masked_written == masked_stored and len(deviations) == 2
          and all(value < 1e-10 for value in deviations),
          "the program wrote lovelock-report.json equal to the Revision record byte for "
          "byte, apart from its two brute-force deviations, both below 1e-10",
          record=f"{RESULTS}/lovelock-report.json (the whole file; checks "
                 "k1_brute_force_numeric and k2_brute_force_numeric)")
    '''),
    md(r"""
    ## 6. How much work the sums are

    The report `lovelock-report.json` (just reproduced) lists, for each order $k$, the
    **leaves** (the combinations of $k$ nonzero curvature entries that survive the
    skipping of repeated labels, for all 64 pairs $(h, j)$), the **GKD calls** (the
    leaves whose upper and lower label sets are equal, so that GKD may be nonzero; GKD
    is then called) and the number of nonzero GKD values. The next cell reads them and
    compares them with two counts without any shortcut: the number of ordered
    combinations of $k$ of the 112 nonzero entries for the 64 pairs, $64 \cdot 112^k$,
    and the literal number of index lists, $64 \cdot 8^{4k}$. For $k = 4$ nothing
    survives: a combination of four entries needs nine different labels in each list,
    and there are only eight.
    """),
    code(r'''
    import numpy as np  # arrays of numbers

    lovelock_report = json.loads((OUT_FOLDER / "lovelock-report.json").read_text(
        encoding="utf-8"))
    COUNTERS = {row["k"]: row for row in lovelock_report["counters"]}
    say("order k   literal lists   ordered products    leaves   GKD calls   nonzero GKD")
    for k in (1, 2, 3, 4):
        leaves, calls = COUNTERS[k]["leaves"], COUNTERS[k]["gkdCalls"]
        nonzero = COUNTERS[k]["gkdNonzero"]
        say(f"      {k}   {64 * 8 ** (4 * k):13.2e}   {64 * 112 ** k:16.2e}   "
            f"{leaves:7d}   {calls:9d}   {nonzero:11d}")

    fig, ax = plt.subplots(figsize=(7.6, 4.5))
    orders = np.array([1, 2, 3, 4])
    series = [("literal index lists, $64 \\cdot 8^{4k}$", [64 * 8 ** (4 * k)
                                                          for k in orders], "0.7"),
              ("ordered products of nonzero entries, $64 \\cdot 112^k$",
               [64 * 112 ** k for k in orders], "tab:purple"),
              ("leaves after skipping repeated labels",
               [COUNTERS[k]["leaves"] for k in orders], "tab:blue"),
              ("GKD calls", [COUNTERS[k]["gkdCalls"] for k in orders], "tab:orange")]
    width = 0.2
    for number, (name, heights, colour) in enumerate(series):
        place = orders + (number - 1.5) * width
        ax.bar(place, [h if h > 0 else np.nan for h in heights], width, color=colour,
               label=name)
        for x, h in zip(place, heights):
            if h == 0:
                ax.text(x, 1.5, "0", ha="center", fontsize=8)
    ax.set_yscale("log")
    ax.set_ylim(1.0, 1e18)
    ax.set_xlim(0.5, 4.5)
    ax.set_xticks(orders, [f"k = {k}" for k in orders])
    ax.set_xlabel("order $k$ of the Lovelock tensor")
    ax.set_ylabel("number of terms (logarithmic scale)")
    ax.set_title("The work of the Lovelock sums, and how it is reduced")
    ax.legend(loc="upper left", fontsize=8)
    save_figure(fig, "work_of_the_sums",
                "The number of terms of the Lovelock sums for the 64 components of "
                "$P_{(k)}$ of the corrected metric, order $k = 1$ to $4$, on a "
                "logarithmic vertical axis: all index lists of the literal formula "
                "(grey), the ordered products of $k$ of the 112 nonzero curvature "
                "entries (purple), the combinations left after skipping those with a "
                "repeated label (blue), and the ones for which GKD is called (orange). "
                "For $k = 3$ the literal sum has about $4.4 \\times 10^{12}$ terms, of "
                "which only 322,560 are evaluated; for $k = 4$ nothing is left, because "
                "nine labels out of eight must repeat.")
    check([COUNTERS[k]["leaves"] for k in (1, 2, 3, 4)] == [4032, 107520, 645120, 0]
          and [COUNTERS[k]["gkdCalls"] for k in (1, 2, 3, 4)] == [672, 26880, 322560, 0],
          "the counters of the Rust sums are 4032, 107520, 645120, 0 leaves and 672, "
          "26880, 322560, 0 GKD calls",
          record=f"{RESULTS}/lovelock-report.json, counters")
    '''),
    md(r"""
    ## 7. The curvature, recomputed with sympy

    The next three cells compute the curvature of the metric of section 4 with sympy,
    from the formulas of section 4, without using anything of the Rust program. The
    first one defines the metric and its Christoffel symbols. `sp.Function("a4")(x4)`,
    `sp.Function("b4")(x4)`, `sp.Function("C")(x0)` and `sp.Function("W")(x0)` are
    unknown functions; `sp.diff` differentiates exactly, and the dictionary `RULES`
    replaces the derivatives of $C = \cot z$ and $W = (\sin^2 z)^{1/12}$ by the two
    rules of section 4. Because the metric is diagonal, the formula
    $\Gamma^a{}_{bc} = \tfrac12 g^{aa}(\partial_b g_{ac} + \partial_c g_{ab} -
    \partial_a g_{bc})$ has at most three terms, each present only when two of the
    labels $a, b, c$ are equal; the cell adds exactly those, simplifies the fraction
    (`sp.cancel`) and keeps the symbols that are not zero in the dictionary
    `christoffel`. For printing it writes $a_4'$, $a_4''$, $b_4'$, $b_4''$, $b_4$ and
    $e^{2a_4}$ with the symbols `A1`, `A2`, `U`, `V`, `B`, `K` ($b_4' = u\,b_4$,
    $b_4'' = (v + u^2)\, b_4$, $e^{2a_4} = k\, b_4$; the dictionary `SYMBOLS` and the
    replacement of $a_4$ by $\frac12 \ln(k\, b_4)$) and $C$, $W$ as plain letters.
    """),
    code(r'''
    import sympy as sp  # exact algebra and calculus

    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]  # label k is xk
    H = sp.Symbol("H", positive=True)  # the author's constant H > 0
    X = sp.symbols("x0:8", real=True)  # the coordinates x0, ..., x7
    a4 = sp.Function("a4")(X[4])  # the unknown function a4(x4)
    b4 = sp.Function("b4")(X[4])  # the unknown function b4(x4) > 0
    C = sp.Function("C")(X[0])  # C = cot z with z = 6 H x0
    W = sp.Function("W")(X[0])  # W = (sin^2 z)^(1/12) > 0
    RULES = {sp.Derivative(C, X[0]): -6 * H * (1 + C ** 2),  # d cot z / d x0
             sp.Derivative(W, X[0]): H * C * W}  # d (sin^2 z)^(1/12) / d x0
    block = sp.exp(-2 * a4) * b4  # the factor of g_00 and of the three extra times
    METRIC = ([block * C ** 2] + [sp.exp(2 * a4)] * 3 + [sp.Integer(-1)]
              + [-block * W ** 2] * 3)  # g_00, g_11, ..., g_77
    A1, A2, U, V = sp.symbols("A1 A2 U V")  # a4', a4'', u = b4'/b4, v = u'
    K, B = sp.symbols("K B", positive=True)  # k = e^(2 a4)/b4 and b4 itself
    SYMBOLS = {sp.Derivative(a4, (X[4], 2)): A2, sp.Derivative(a4, X[4]): A1,
               sp.Derivative(b4, (X[4], 2)): (V + U ** 2) * B,
               sp.Derivative(b4, X[4]): U * B}
    PLAIN = {C: sp.Symbol("C"), W: sp.Symbol("W")}  # C(x0), W(x0) printed as C, W


    def readable(expr):
        """expr with the six variables, b4 written B and C(x0), W(x0) written C, W."""
        expr = expr.subs(SYMBOLS).subs(b4, B).subs(a4, sp.log(K * B) / 2)
        return sp.factor(sp.cancel(expr)).subs(PLAIN)


    christoffel = {}  # (a, b, c) -> Gamma^a_bc, only the nonzero ones
    for a in range(8):
        for b in range(8):
            for c in range(8):
                value = 0
                if a == c:
                    value += sp.diff(METRIC[a], X[b])  # d_b g_ac
                if a == b:
                    value += sp.diff(METRIC[a], X[c])  # d_c g_ab
                if b == c:
                    value -= sp.diff(METRIC[b], X[a])  # - d_a g_bc
                if value != 0:  # times g^aa / 2, the derivatives of C and W replaced
                    christoffel[a, b, c] = sp.cancel((value / (2 * METRIC[a]))
                                                     .subs(RULES))


    def gamma(a, b, c):
        """Gamma^a_bc (0 when it is not in the dictionary)."""
        return christoffel.get((a, b, c), 0)


    christoffel_b_le_c = sorted(key for key in christoffel if key[1] <= key[2])
    report("nonzero Christoffel symbols Gamma^a_bc with b <= c", len(christoffel_b_le_c))
    for a, b, c in christoffel_b_le_c:
        say(f"  Gamma^{NAMES[a]}_({NAMES[b]} {NAMES[c]}) = "
            f"{readable(christoffel[a, b, c])}")
    check(all(christoffel.get((a, c, b)) == value
              for (a, b, c), value in christoffel.items()),
          "Gamma^a_bc = Gamma^a_cb (symmetric in the lower labels)")
    '''),
    md(r"""
    The next cell computes the Riemann tensor from the formula of section 4 and raises
    its second label, $R^{ab}{}_{cd} = R^a{}_{bcd}/g_{bb}$. For every component it
    replaces the derivatives of $C$ and $W$ by `RULES`, writes the derivatives of $a_4$
    and $b_4$ with the six variables (`SYMBOLS`; $b_4$ becomes the symbol `B`), replaces
    $a_4$ by $\frac12 \ln(k B)$, so that $e^{2a_4} = kB$ and $e^{-2a_4} = 1/(kB)$, and
    simplifies the fraction with `sp.cancel`. If a component still contained $C$, $W$
    (that is, $x_0$), $B$ or $e^{a_4}$ alone, the check at the end would fail: they
    cancel in every $R^{ab}{}_{cd}$, which is a polynomial in the six variables. The
    cell takes a few seconds.
    """),
    code(r'''
    RIEMANN = {}  # (a, b, c, d) -> R^ab_cd in the symbols H, A1, A2, U, V, K
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    value = sp.diff(gamma(a, d, b), X[c]) - sp.diff(gamma(a, c, b), X[d])
                    for e in range(8):
                        value += (gamma(a, c, e) * gamma(e, d, b)
                                  - gamma(a, d, e) * gamma(e, c, b))
                    if value == 0:
                        continue
                    value = (value / METRIC[b]).subs(RULES).subs(SYMBOLS).subs(b4, B)
                    value = sp.cancel(value.subs(a4, sp.log(K * B) / 2))  # e^(2a4) = K B
                    if value != 0:
                        RIEMANN[a, b, c, d] = sp.expand(value)
    report("nonzero components R^ab_cd", len(RIEMANN))
    VARIABLES = (H, A1, A2, U, V, K)  # the six variables
    check(all(v.free_symbols <= set(VARIABLES) and v.is_polynomial(*VARIABLES)
              for v in RIEMANN.values()),
          "every R^ab_cd is a polynomial in H, a4', a4'', u, v and k: free of x0 (of C and "
          "W) and of b4 and e^a4 except through u, v and k",
          record=f"{RESULTS}/lovelock-report.json, check mixed_riemann_free_of_x0")
    '''),
    md(r"""
    The next cell reads the 112 components that the Rust program wrote into
    `curvature.json` (as Mathematica text such as
    `(1/2)*Derivative[1][a4][x4]*b4[x4]^(-1)*Derivative[1][b4][x4]`). The function
    `from_mathematica` turns such a text into a sympy expression: `Derivative[n][a4][x4]`
    becomes `An`, $b_4'$ becomes `(U*B)`, $b_4''$ becomes `((V + U**2)*B)`, $b_4$
    becomes `B`, $e^{n a_4}$ becomes `(K*B)**(n/2)`, and `^` becomes `**`. The cell
    checks that the two computations give the same nonzero components with EXACTLY the
    same values, the antisymmetry $R^{ab}{}_{cd} = -R^{ba}{}_{cd} = -R^{ab}{}_{dc}$,
    that every nonzero component has its lower pair equal to its upper pair (a plane
    curvature, $\{c, d\} = \{a, b\}$), the number of Christoffel symbols, and the Ricci
    scalar $R = \sum_{a,b} R^{ab}{}_{ab}$.
    """),
    code(r'''
    curvature = json.loads((OUT_FOLDER / "curvature.json").read_text(encoding="utf-8"))


    def from_mathematica(text):
        """A formula written by the Rust program (Mathematica text) as a sympy
        expression in H, A1, A2, U, V and K."""
        text = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"A\1", text)  # a4' -> A1
        text = text.replace("Derivative[1][b4][x4]", "(U*B)")  # b4' = u b4
        text = text.replace("Derivative[2][b4][x4]", "((V + U**2)*B)")  # b4''
        text = text.replace("b4[x4]", "B")  # b4
        text = re.sub(r"E\^\((-?\d+)\*a4\[x4\]\)", r"(K*B)**(\1/2)", text)  # e^(n a4)
        value = sp.sympify(text.replace("^", "**"),
                           locals={"H": H, "A1": A1, "A2": A2, "U": U, "V": V, "K": K,
                                   "B": B})
        return sp.expand(value)


    rust_riemann = {}
    for item in curvature["riemannMixedNonzero"]:
        a, b = (NAMES.index(name) for name in item["up"])
        c, d = (NAMES.index(name) for name in item["down"])
        rust_riemann[a, b, c, d] = from_mathematica(item["value"])
    same_values = set(rust_riemann) == set(RIEMANN) and all(
        sp.expand(RIEMANN[key] - rust_riemann[key]) == 0 for key in RIEMANN)
    check(same_values, "sympy and Rust give the same 112 nonzero R^ab_cd exactly",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
                 "check rust_riemann_agrees")
    antisymmetric = all(sp.expand(v + RIEMANN.get((b, a, c, d), 0)) == 0 and
                        sp.expand(v + RIEMANN.get((a, b, d, c), 0)) == 0
                        for (a, b, c, d), v in RIEMANN.items())
    check(antisymmetric, "R^ab_cd = -R^ba_cd = -R^ab_dc for all components",
          record=f"{RESULTS}/lovelock-report.json, check riemann_antisymmetry")
    sectional = all({c, d} == {a, b} for (a, b, c, d) in RIEMANN)
    check(sectional and len(RIEMANN) == 4 * 28,
          "every nonzero R^ab_cd has {c, d} = {a, b}: 4 entries for each of the 28 "
          "planes, no mixed component",
          record=f"{RESULTS}/lovelock-report.json, check mixed_riemann_only_sectional")
    check(len(christoffel_b_le_c) == len(curvature["christoffelNonzero_b_le_c"]) == 21,
          "21 nonzero Christoffel symbols with b <= c, as in the record")
    ricci_scalar = sp.expand(sum(RIEMANN.get((a, b, a, b), 0) for a in range(8)
                                 for b in range(8)))
    report("Ricci scalar R", ricci_scalar)
    check(sp.expand(ricci_scalar - from_mathematica(curvature["ricciScalar"])) == 0,
          "the Ricci scalar is R = 8 a4'^2 - 8 a4' u - 2 a4'' - 12 H^2 k + 5 u^2 + 4 v, "
          "as in the record",
          record=f"{RESULTS}/curvature.json, ricciScalar")
    '''),
    md(r"""
    The next cell draws the curvature of every coordinate plane, $K(a, b) =
    R^{ab}{}_{ab}$, as two $8 \times 8$ tables, in units of $H^2$ (that is, with
    $H = 1$), with the exact values written as fractions. The left table is the moment
    $x_4 = 0$ of the history of the Revision record: $a_4' = H$, $a_4'' = 0$,
    $u = 4H/3$, $v = 0$ and $k = 1$. The right table is the same moment with
    $a_4'' = v = H^2$ added, to show which planes feel the second derivatives. The
    dictionaries `MOMENT` and `SPED_UP` hold these values; `expr.subs(point)` puts them
    in place of the symbols, which gives an exact fraction. The table is symmetric,
    $K(a, b) = K(b, a)$. Reading it: inside ordinary space $K = a_4'^2$; between
    ordinary space and the hidden direction or an extra time $K = -a_4'(a_4' - u/2)$;
    inside the block of the hidden direction and the three extra times
    $K = (a_4' - u/2)^2 - H^2 k$; with the time $x_4$, $K = a_4'^2 + a_4''$ for
    ordinary space and $(a_4' - u/2)^2 - a_4'' + v/2$ for the block. The hidden
    direction behaves exactly like an extra time.
    """),
    code(r'''
    MOMENT = {H: 1, A1: 1, A2: 0, U: sp.Rational(4, 3), V: 0, K: 1}  # record, x4 = 0
    SPED_UP = {**MOMENT, A2: 1, V: 1}  # the same moment with a4'' = v = H^2
    fig, axes = plt.subplots(1, 2, figsize=(11.6, 5.0))
    planes = {}
    for ax, (name, point) in zip(axes, (("moment", MOMENT), ("sped up", SPED_UP))):
        table = [[sp.sympify(RIEMANN.get((a, b, a, b), 0)).subs(point) for b in range(8)]
                 for a in range(8)]  # exact fractions
        planes[name] = table
        picture = ax.imshow(np.array([[float(x) for x in row] for row in table]),
                            cmap="RdBu_r", vmin=-2.2, vmax=2.2)
        for a in range(8):
            for b in range(8):
                if a != b:
                    ax.text(b, a, str(table[a][b]), ha="center", va="center",
                            fontsize=7)
        ax.set_xticks(range(8), NAMES)
        ax.set_yticks(range(8), NAMES)
        ax.grid(False)
    axes[0].set_title("history of the record at $x_4 = 0$")
    axes[1].set_title("the same moment with $a_4'' = v = H^2$")
    fig.colorbar(picture, ax=list(axes), shrink=0.8, label="$K(a, b)$ in units of $H^2$")
    save_figure(fig, "curvature_of_planes",
                "The curvature $K(a, b) = R^{ab}_{\\ ab}$ of the plane of the coordinate "
                "directions $x_a$ and $x_b$ of the corrected metric, in units of $H^2$, "
                "as exact fractions: left at the moment $x_4 = 0$ of the history of the "
                "record, where $a_4^{\\prime} = H$, $u = 4H/3$, $k = 1$ and "
                "$a_4^{\\prime\\prime} = v = 0$; right at the same moment with "
                "$a_4^{\\prime\\prime} = v = H^2$; red positive, blue negative, the "
                "diagonal empty. Planes in 3-space have 1, planes of 3-space with "
                "$x_0$ or an extra time $-1/3$, planes inside the block of "
                "$x_0, x_5, x_6, x_7$ have $(a_4^{\\prime} - u/2)^2 - H^2 k = -8/9$; "
                "only the planes with the time $x_4$ change on the right, where "
                "$a_4^{\\prime\\prime}$ and $v$ enter.")
    check(planes["moment"][1][2] == 1 and planes["moment"][1][5] == sp.Rational(-1, 3)
          and planes["moment"][1][0] == sp.Rational(-1, 3)
          and planes["moment"][0][5] == sp.Rational(-8, 9)
          and planes["moment"][4][0] == sp.Rational(1, 9) == planes["moment"][4][5]
          and planes["moment"][1][4] == 1 and planes["sped up"][1][4] == 2
          and planes["sped up"][5][4] == sp.Rational(-7, 18) == planes["sped up"][0][4],
          "plane curvatures: 3-space 1, 3-space with the block -1/3, block -8/9, x4 with "
          "3-space 1 + a4'', x4 with the block 1/9 - a4'' + v/2")
    '''),
    md(r"""
    The next cell draws the WHOLE tensor $R^{ab}{}_{cd}$ at the sped-up moment of the
    right table as a $64 \times 64$ table: row number $8a + b$ belongs to the upper pair
    $(x_a, x_b)$ and column number $8c + d$ to the lower pair $(x_c, x_d)$. Thin lines
    separate the blocks of the first labels $a$ and $c$. Most squares are white: only
    112 of the 4096 components are not zero. Each of them is a plane curvature: it sits
    either on the main diagonal ($c = a$, $d = b$, the square of $R^{ab}{}_{ab}$) or at
    the mirrored place ($c = b$, $d = a$, the square of $R^{ab}{}_{ba} =
    -R^{ab}{}_{ab}$). No square lies anywhere else: no component mixes two different
    planes.
    """),
    code(r'''
    whole = np.zeros((64, 64))
    for (a, b, c, d), value in RIEMANN.items():
        whole[8 * a + b, 8 * c + d] = float(value.subs(SPED_UP))
    fig, ax = plt.subplots(figsize=(6.8, 6.2))
    largest = np.abs(whole).max()
    picture = ax.imshow(whole, cmap="RdBu_r", vmin=-largest, vmax=largest)
    for edge in range(8, 64, 8):  # lines between the blocks
        ax.axhline(edge - 0.5, color="0.8", lw=0.5)
        ax.axvline(edge - 0.5, color="0.8", lw=0.5)
    ticks = list(range(3, 64, 8))  # the middle of each block
    ax.set_xticks(ticks, [f"c = {name}" for name in NAMES], rotation=90, fontsize=8)
    ax.set_yticks(ticks, [f"a = {name}" for name in NAMES], fontsize=8)
    ax.set_xlabel("lower pair $(x_c, x_d)$, column $8c + d$")
    ax.set_ylabel("upper pair $(x_a, x_b)$, row $8a + b$")
    ax.set_title("All components $R^{ab}{}_{cd}$ at one moment")
    ax.grid(False)
    fig.colorbar(picture, ax=ax, shrink=0.8, label="value (units of $H^2$)")
    save_figure(fig, "riemann_matrix",
                "All 4096 components of the Riemann tensor $R^{ab}_{\\ \\ cd}$ of the "
                "corrected metric at the moment $a_4^{\\prime} = H$, $u = 4H/3$, $k = 1$, "
                "$a_4^{\\prime\\prime} = v = H^2$, arranged as a 64 by 64 table: row "
                "$8a + b$ is the upper pair of labels, column $8c + d$ the lower pair, "
                "counted from 0; red positive, blue negative, white zero. Only 112 "
                "components are not zero, and each lies on the main diagonal, the "
                "curvature $R^{ab}_{\\ \\ ab}$ of a coordinate plane, or at its mirrored "
                "place $R^{ab}_{\\ \\ ba} = -R^{ab}_{\\ \\ ab}$: no component mixes two "
                "different planes.")
    places = {(8 * a + b, 8 * c + d) for (a, b, c, d) in RIEMANN}
    check(int(np.count_nonzero(whole)) == 112
          and all(column in (8 * (row // 8) + row % 8, 8 * (row % 8) + row // 8)
                  for row, column in places),
          "112 of the 4096 components are not zero, all at the places of R^ab_ab and "
          "R^ab_ba")
    '''),
    md(r"""
    Why is there no mixed component, such as $R^{x_4 c}{}_{x_0 c}$, which would couple
    the time to the hidden direction? For a diagonal metric with $g_{44} = -1$ whose
    scale factors split as $f_c = (\text{function of } x_4) \times (\text{function of }
    x_0)$, the Riemann formula gives (derived line by line in the book)

    $$R^{x_4 c}{}_{x_0 c} = \partial_0 \ln f_c \,\big(\partial_4 \ln f_c
      - \partial_4 \ln f_0\big):$$

    the rate at which the scale factor of direction $c$ changes along $x_0$, times the
    difference between its rate of change in time and that of the hidden direction.
    The next cell computes both factors from the metric, with $\partial \ln f_c =
    \partial g_{cc} / (2 g_{cc})$ (the function `rate`), for the six directions of
    3-space and of the extra times. For 3-space the first factor is 0: $e^{2a_4}$ does
    not depend on $x_0$. For the extra times the second factor is 0: they share the
    factor $e^{-a_4} b_4^{1/2}$ of the hidden direction, so they change in time at the
    same rate. Every product vanishes, for every history and every real $z$; the cell
    confirms that no such component is among the 112, and that the Ricci component
    $R^{x_4}{}_{x_0}$ and the record's Einstein component $G^{x_4}{}_{x_0}$ are 0. It
    draws the two factors at $z = \pi/4$ ($\cot z = 1$) and the moment $x_4 = 0$ of the
    history of the record.
    """),
    code(r'''
    def rate(c, coordinate):
        """d ln f_c / d x_coordinate = (d g_cc / d x_coordinate) / (2 g_cc)."""
        value = (sp.diff(METRIC[c], X[coordinate]) / (2 * METRIC[c])).subs(RULES)
        return sp.cancel(value.subs(SYMBOLS).subs(b4, B))


    transverse = [1, 2, 3, 5, 6, 7]  # the directions of 3-space and the extra times
    along_x0 = {c: rate(c, 0) for c in transverse}  # first factor
    relative = {c: sp.cancel(rate(c, 4) - rate(0, 4)) for c in transverse}  # second
    for c in transverse:
        say(f"c = {NAMES[c]}: d0 ln f_c = {along_x0[c].subs(PLAIN)}, "
            f"d4 ln f_c - d4 ln f_0 = {relative[c]}, product = "
            f"{sp.cancel(along_x0[c] * relative[c])}")
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    places_c = np.arange(len(transverse))
    first = [float(along_x0[c].subs(H, 1).subs(C, 1)) for c in transverse]
    second = [float(relative[c].subs(MOMENT)) for c in transverse]
    ax.bar(places_c - 0.18, first, 0.36, color="tab:blue",
           label="$\\partial_0 \\ln f_c$ (units of $H \\cot z$)")
    ax.bar(places_c + 0.18, second, 0.36, color="tab:orange",
           label="$\\partial_4 \\ln f_c - \\partial_4 \\ln f_0$ (units of $H$)")
    for place in places_c:
        ax.text(place, 1.45, "product 0", ha="center", fontsize=8)
    ax.axhline(0.0, color="black", lw=0.8)
    ax.set_ylim(-0.2, 2.15)
    ax.set_xticks(places_c, [NAMES[c] for c in transverse])
    ax.set_xlabel("the direction $c$ of the term $R^{x_4 c}{}_{x_0 c}$")
    ax.set_ylabel("value")
    ax.set_title("The two factors of each mixed term: one of them is always 0")
    ax.legend(loc="upper center", ncol=2, fontsize=8)
    save_figure(fig, "mixing_terms_vanish",
                "Why the corrected metric has no curvature component that mixes the "
                "time $x_4$ with the hidden direction $x_0$: for each direction $c$ of "
                "3-space and of the extra times the component "
                "$R^{x_4 c}_{\\ \\ x_0 c}$ is the product of the rate "
                "$\\partial_0 \\ln f_c$ of its scale factor along $x_0$ (blue, in units "
                "of $H \\cot z$) and the difference $\\partial_4 \\ln f_c - "
                "\\partial_4 \\ln f_0$ of its rate in time and that of the hidden "
                "direction (orange, in units of $H$, at the moment $x_4 = 0$ of the "
                "history of the record). For 3-space the first factor is 0, for the "
                "extra times the second, because they share the scale factor "
                "$e^{-a_4} b_4^{1/2}$ of the hidden direction: every product is 0, for "
                "every history and every real $z$.")
    check(all(sp.cancel(along_x0[c] * relative[c]) == 0 for c in transverse)
          and not any((4, c, 0, c) in RIEMANN or (0, c, 4, c) in RIEMANN
                      for c in transverse),
          "every term R^(x4 c)_(x0 c) has a vanishing factor, and none is among the 112 "
          "components")
    ricci_40 = sp.expand(sum(RIEMANN.get((4, c, 0, c), 0) for c in range(8)))
    check(ricci_40 == 0 and curvature["einsteinMixed"]["x4,x0"]["mathematica"] == "0"
          and curvature["einsteinMixed"]["x0,x4"]["mathematica"] == "0",
          "R^x4_x0 = 0, and the record's G^x4_x0 and G^x0_x4 are 0",
          record=f"{RESULTS}/curvature.json, einsteinMixed x4,x0 and x0,x4")
    '''),
    md(r"""
    ## 8. The three Lovelock tensors with a Python GKD sum

    The next cell prepares the exact arithmetic. A polynomial in the six variables
    $H, a_4', a_4'', u, v, k$ is stored as a Python dictionary that maps the exponents
    $(e_H, e_{a_4'}, e_{a_4''}, e_u, e_v, e_k)$ of a monomial to its coefficient, a
    `Fraction` (an exact fraction of whole numbers). `poly_mul` multiplies two
    polynomials (every monomial of the first by every monomial of the second, adding the
    exponents), `poly_add` adds a multiple of one polynomial to another, dropping
    monomials whose coefficient becomes 0. `to_poly` turns a sympy polynomial into this
    form (`sp.Poly` lists its monomials and coefficients). The 112 nonzero entries
    $R^{ab}{}_{cd}$ of the sympy computation of section 7, sorted by their labels,
    become the list `ENTRIES`.

    The cell also defines `gkd`, the rule of Notebook 11a: the sign of the permutation
    that carries the lower list into the upper list, or 0. In a term of the sum the
    UPPER labels $a, b$ of an entry $R^{ab}{}_{cd}$ go into the LOWER list of the delta
    and its lower labels $c, d$ into the upper list (look at the formula of section 4).
    The cell stores both pairs of every entry as **bit masks**: a set of labels
    is written as the whole number $\sum 2^{\text{label}}$, so that two sets share a
    label exactly when the bitwise AND (`&`) of their numbers is not 0, and the union of
    two sets is the bitwise OR (`|`). `np.array` holds the 112 masks, so that one
    comparison tests all 112 entries at once.
    """),
    code(r'''
    from fractions import Fraction  # exact fractions of whole numbers

    ONE = {(0, 0, 0, 0, 0, 0): Fraction(1)}  # the polynomial 1


    def poly_mul(p, q):
        """The product of the polynomials p and q."""
        out = {}
        for m1, c1 in p.items():
            for m2, c2 in q.items():
                m = tuple(e1 + e2 for e1, e2 in zip(m1, m2))  # add the exponents
                out[m] = out.get(m, 0) + c1 * c2
        return {m: c for m, c in out.items() if c != 0}


    def poly_add(p, q, factor=1):
        """p + factor * q."""
        out = dict(p)
        for m, c in q.items():
            out[m] = out.get(m, 0) + factor * c
        return {m: c for m, c in out.items() if c != 0}


    def to_poly(expr):
        """A polynomial sympy expression in H, A1, A2, U, V, K as a dict."""
        poly = sp.Poly(sp.expand(expr), *VARIABLES)
        return {m: Fraction(int(v.p), int(v.q))
                for m, v in zip(poly.monoms(), poly.coeffs())}


    def gkd(lower, upper):
        """GKD (Notebook 11a): the sign of the permutation from lower to upper, or 0."""
        position = {}
        for place, label in enumerate(upper):
            if label in position:
                return 0
            position[label] = place
        sigma = [position.get(label) for label in lower]
        if None in sigma or len(set(sigma)) < len(sigma):
            return 0
        inversions = sum(1 for i in range(len(sigma)) for j in range(i + 1, len(sigma))
                         if sigma[i] > sigma[j])
        return 1 if inversions % 2 == 0 else -1


    ENTRIES = [(key, to_poly(RIEMANN[key])) for key in sorted(RIEMANN)]  # 112 entries
    LOWER_MASK = np.array([(1 << a) | (1 << b) for (a, b, c, d), _ in ENTRIES])
    UPPER_MASK = np.array([(1 << c) | (1 << d) for (a, b, c, d), _ in ENTRIES])
    report("nonzero curvature entries in the sums", len(ENTRIES))
    check(gkd([0, 1, 2], [1, 2, 0]) == 1 and gkd([0, 1], [1, 0]) == -1,
          "gkd: a cycle of three labels is even (+1), an exchange of two odd (-1)",
          record=f"{RESULTS}/lovelock-report.json, gkdSelfCheck")
    '''),
    md(r"""
    The next cell defines `lovelock_sum(k, free_pair)`, the sum of section 4. It works
    with a list `stack` of partial combinations: each holds the chosen entries (their
    numbers in `ENTRIES`) and the masks of the labels used so far in the lower and in
    the upper list. A partial combination with fewer than $k$ entries is extended by
    every entry that shares no label with it, in the lower list or in the upper list
    (`np.nonzero` finds them among all 112 at once); this is the skipping of repeated
    labels. A complete combination (a **leaf**) is kept only if its lower and upper
    label sets are equal (otherwise some lower label is missing above and GKD is 0);
    then GKD is called on the lower list $(j, j_1, \dots, j_{2k})$ and the upper list
    $(h, h_1, \dots, h_{2k})$, and its value is added to the weight of the combination.
    The weights are collected per SET of entries (`tuple(sorted(...))`), because the
    product of the entries does not depend on their order; at the end every set's
    product is multiplied out once. With `free_pair=True` the sum is done for each of
    the 64 pairs $(h, j)$ and gives the tensor $P_{(k)}{}^h{}_j$; with `free_pair=False`
    it gives the scalar $L_{(k)}$. The function also counts leaves and GKD calls.
    """),
    code(r'''
    def lovelock_sum(k, free_pair):
        """P_(k) as {(h, j): polynomial} (free_pair True) or L_(k) as {None: polynomial},
        and the numbers of leaves and of GKD calls."""
        pairs = [(h, j) for h in range(8) for j in range(8)] if free_pair else [None]
        weights, leaves, calls = {}, 0, 0
        for pair in pairs:
            start_lower = 1 << pair[1] if pair else 0  # j is the first lower label
            start_upper = 1 << pair[0] if pair else 0  # h is the first upper label
            stack = [((), start_lower, start_upper)]
            while stack:
                chosen, lower_mask, upper_mask = stack.pop()
                if len(chosen) == k:  # a leaf
                    leaves += 1
                    if lower_mask != upper_mask:
                        continue  # a lower label is missing above: GKD = 0
                    lower = ([pair[1]] if pair else []) + [
                        x for i in chosen for x in ENTRIES[i][0][:2]]  # j, j1, ..., j2k
                    upper = ([pair[0]] if pair else []) + [
                        x for i in chosen for x in ENTRIES[i][0][2:]]  # h, h1, ..., h2k
                    sign = gkd(lower, upper)
                    calls += 1
                    if sign != 0:
                        bucket = weights.setdefault(pair, {})
                        key = tuple(sorted(chosen))  # the set of entries
                        bucket[key] = bucket.get(key, 0) + sign
                    continue
                free = np.nonzero(((LOWER_MASK & lower_mask) == 0)
                                  & ((UPPER_MASK & upper_mask) == 0))[0]
                for i in free:  # every entry that repeats no label
                    stack.append((chosen + (int(i),), lower_mask | int(LOWER_MASK[i]),
                                  upper_mask | int(UPPER_MASK[i])))
        products = {}  # set of entries -> the product of their polynomials
        result = {}
        for pair, bucket in weights.items():
            total = {}
            for key, weight in bucket.items():
                if weight == 0:
                    continue
                if key not in products:
                    product = ONE
                    for i in key:
                        product = poly_mul(product, ENTRIES[i][1])
                    products[key] = product
                total = poly_add(total, products[key], weight)
            if total:
                result[pair] = total
        return result, leaves, calls
    '''),
    md(r"""
    The next cell runs the sums for $k = 1, 2, 3$, the tensors and the scalars, and
    compares the counters with those of the Rust program (`lovelock-report.json`:
    `leaves`, `gkdCalls`, `gkdNonzero` and `scalarGkdCalls`). The numbers of leaves and
    of GKD calls depend only on which entries are not zero. Both programs find 8 nonzero
    components of each tensor: the 8 diagonal ones (field `nonzeroComponents`). It
    takes about 10 seconds, almost all of it for $k = 3$.
    """),
    code(r'''
    P, L, MY_COUNTERS = {}, {}, {}
    for k in (1, 2, 3):
        P[k], leaves, calls = lovelock_sum(k, free_pair=True)
        scalar, scalar_leaves, scalar_calls = lovelock_sum(k, free_pair=False)
        L[k] = scalar.get(None, {})
        MY_COUNTERS[k] = (leaves, calls, scalar_calls)
        say(f"k = {k}: leaves {leaves:7d}, GKD calls {calls:6d}, scalar GKD calls "
            f"{scalar_calls:6d}, nonzero components {len(P[k])}")
    same_counters = all(
        MY_COUNTERS[k] == (COUNTERS[k]["leaves"], COUNTERS[k]["gkdCalls"],
                           COUNTERS[k]["scalarGkdCalls"])
        and COUNTERS[k]["gkdNonzero"] == COUNTERS[k]["gkdCalls"]
        and len(P[k]) == COUNTERS[k]["nonzeroComponents"] == 8
        for k in (1, 2, 3))
    check(same_counters, "the Python sums reproduce the counters of the Rust sums; "
          "8 nonzero components for each order",
          record=f"{RESULTS}/lovelock-report.json, counters k = 1, 2, 3")
    '''),
    md(r"""
    The next cell compares every one of the $3 \times 64$ components with the Rust
    record `lovelock-tensors.json`, which stores each component, for general $a_4$ and
    $b_4$, as an exact list of monomials `[numerator, denominator, [fourteen
    exponents]]`. The fourteen exponents belong, in this order, to $H$, the four
    derivatives of $a_4$, $E = e^{a_4}$, $W = (\sin^2 z)^{1/12}$, $C = \cot z$,
    $Q = b_4^{1/2}$, the four derivatives of $b_4$ and $\mathrm{sgn}(\cot z)$. The
    function `from_monomials` rebuilds each component in the six variables:
    $H^{e_0} a_4'^{e_1} a_4''^{e_2} E^{e_5} Q^{e_8} b_4'^{e_9} b_4''^{e_{10}} =
    H^{e_0} a_4'^{e_1} a_4''^{e_2} k^{e_5/2} u^{e_9} (v + u^2)^{e_{10}}\,
    Q^{e_5 + e_8 + 2e_9 + 2e_{10}}$ (with $E^2 = k\,Q^2$, $b_4' = u\,Q^2$, $b_4'' =
    (v + u^2)\,Q^2$), and it stops with an error if any other symbol occurs or if the
    power of $Q$ is not 0. The comparison is exact (dictionaries of fractions must be
    equal). Then it compares the three scalars with the record's `L1`, `L2`, `L3`, and
    prints the components that are not zero: only the eight diagonal ones $h = j$, for
    every $k$, with equal components for $x_1, x_2, x_3$ and equal components for the
    hidden direction and the three extra times, $x_0, x_5, x_6, x_7$.
    """),
    code(r'''
    tensors = json.loads((OUT_FOLDER / "lovelock-tensors.json").read_text(
        encoding="utf-8"))
    U2_PLUS_V = {(0, 0, 0, 2, 0, 0): Fraction(1), (0, 0, 0, 0, 1, 0): Fraction(1)}


    def from_monomials(monomials):
        """A component of lovelock-tensors.json as a polynomial dict in H, A1, A2, U,
        V, K."""
        out = {}
        for numerator, denominator, e in monomials:
            if any(e[i] for i in (3, 4, 6, 7, 11, 12, 13)):
                raise ValueError("unexpected symbol in a Lovelock component")
            if e[5] % 2 or e[5] + e[8] + 2 * e[9] + 2 * e[10] != 0:
                raise ValueError("the powers of b4 do not cancel")
            term = {(e[0], e[1], e[2], e[9], 0, e[5] // 2): Fraction(numerator,
                                                                     denominator)}
            for _ in range(e[10]):  # b4''/b4 = v + u^2, once for each power of b4''
                term = poly_mul(term, U2_PLUS_V)
            out = poly_add(out, term)
        return out


    agree = all(from_monomials(tensors[f"P{k}_mixed_up_h_down_j"]
                               [f"{NAMES[h]},{NAMES[j]}"]["monomials"])
                == P[k].get((h, j), {})
                for k in (1, 2, 3) for h in range(8) for j in range(8))
    for k in (1, 2, 3):
        nonzero = " ".join(sorted(f"{NAMES[h]},{NAMES[j]}" for h, j in P[k]))
        say(f"k = {k}: nonzero components (h, j): {nonzero}")
    check(agree,
          "all 3 x 64 components of P(1), P(2), P(3) equal the Rust components exactly",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
                 "rust_k1_mixed_components_agree, rust_k2_mixed_components_agree and "
                 "rust_k3_mixed_components_agree")
    scalars_agree = all(to_poly(from_mathematica(tensors[f"L{k}"])) == L[k]
                        for k in (1, 2, 3))
    check(scalars_agree, "the scalars L(1), L(2), L(3) equal the Rust scalars exactly",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
                 "rust_L1_agrees, rust_L2_agrees and rust_L3_agrees")
    check(all(set(P[k]) == {(h, h) for h in range(8)}
              and P[k][1, 1] == P[k][2, 2] == P[k][3, 3]
              and P[k][0, 0] == P[k][5, 5] == P[k][6, 6] == P[k][7, 7]
              for k in (1, 2, 3)),
          "only the 8 diagonal components are nonzero, with x1 = x2 = x3 and "
          "x0 = x5 = x6 = x7, for k = 1, 2, 3",
          record=f"{RESULTS}/lovelock-report.json, checks k1_offdiagonal_vanishes to "
                 "k3_offdiagonal_vanishes, k1_hidden_equals_extra_times to "
                 "k3_hidden_equals_extra_times")
    '''),
    md(r"""
    **The skipping changes nothing: the literal sums of orders 1 and 2.** The sums
    above leave out every combination in which a label repeats, because GKD is 0 there
    (Notebook 11a). The next cell does NOT rely on this. For $k = 1$ and $k = 2$ it
    runs through EVERY ordered list of $k$ of the 112 nonzero entries
    (`itertools.product(range(112), repeat=k)` gives all $112^k$ of them), builds the
    lower list $(j_1, \dots, j_{2k})$ and the upper list $(h_1, \dots, h_{2k})$ of the
    delta, and calls GKD for the scalar and for each of the 64 pairs $(h, j)$, with no
    test before the call: $65 \cdot 112 = 7280$ calls for $k = 1$ and
    $65 \cdot 112^2 = 815360$ calls for $k = 2$, the numbers recorded by the Revision's
    sympy checker for the same literal sums. The weights are collected per set of
    entries as before, the products are multiplied out, and the results must equal the
    tensors and scalars of the skipping sums EXACTLY. The cell takes about 10 seconds.
    """),
    code(r'''
    import itertools  # all ordered lists of k entries


    def literal_sum(k):
        """P_(k) and L_(k) from EVERY ordered list of k nonzero entries, GKD called on
        every index list without any test; also the number of GKD calls."""
        pairs = [None] + [(h, j) for h in range(8) for j in range(8)]
        weights, calls = {}, 0
        for chosen in itertools.product(range(len(ENTRIES)), repeat=k):
            lower = [x for i in chosen for x in ENTRIES[i][0][:2]]  # j1, ..., j2k
            upper = [x for i in chosen for x in ENTRIES[i][0][2:]]  # h1, ..., h2k
            key = tuple(sorted(chosen))  # the set of entries of this product
            for pair in pairs:
                if pair is None:  # the scalar: no free pair
                    sign = gkd(lower, upper)
                else:  # the tensor: j first in the lower list, h first in the upper
                    sign = gkd([pair[1]] + lower, [pair[0]] + upper)
                calls += 1
                if sign != 0:
                    bucket = weights.setdefault(pair, {})
                    bucket[key] = bucket.get(key, 0) + sign
        result = {}
        for pair, bucket in weights.items():
            total = {}
            for key, weight in bucket.items():
                product = ONE
                for i in key:
                    product = poly_mul(product, ENTRIES[i][1])
                total = poly_add(total, product, weight)
            if total:
                result[pair] = total
        return result, calls


    record_checks = {c["name"]: c for c in json.loads(repository_file(
        "Revision/gkd_lovelock/results/python-lovelock-report.json").read_text(
            encoding="utf-8"))["checks"]}
    for k in (1, 2):
        literal, calls = literal_sum(k)
        recorded = record_checks[f"k{k}_unpruned_literal_sum_agrees"]
        recorded_calls = int(re.search(r"(\d+) kdelta calls", recorded["detail"]).group(1))
        say(f"k = {k}: {calls} GKD calls (the record: {recorded_calls})")
        same = (literal.pop(None, {}) == L[k]
                and all(literal.get(hj, {}) == P[k].get(hj, {})
                        for hj in set(literal) | set(P[k])))
        check(same and calls == recorded_calls == 65 * 112 ** k
              and recorded["verdict"] == "PASS",
              f"the literal sum of order {k}, without skipping, gives the same P({k}) "
              f"and L({k})",
              record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
                     f"k{k}_unpruned_literal_sum_agrees")
    '''),
    md(r"""
    **Order 4 is zero.** A term of $P_{(4)}$ needs four curvature entries, that is nine
    labels in each list. The next cell looks at the leaves of order 3: every one of them
    already uses seven DIFFERENT labels in its lower list ($j$ and six more), so a
    fourth entry, which brings two new labels, would need nine different labels out of
    eight. No leaf of order 4 exists, which is the Rust counter `leaves = 0` for
    $k = 4$. (`bin(mask).count("1")` counts the labels in a mask.) The scalar $L_{(4)}$,
    with eight labels per list, is NOT zero (the program printed it in section 5); it is
    the Euler density of eight dimensions, and its tensor $P_{(4)}$ vanishes
    identically.
    """),
    code(r'''
    seven_labels = True
    for h in range(8):
        for j in range(8):
            stack = [((), 1 << j, 1 << h)]
            while stack:
                chosen, lower_mask, upper_mask = stack.pop()
                if len(chosen) == 3:  # a leaf of order 3
                    seven_labels = seven_labels and bin(lower_mask).count("1") == 7
                    continue
                free = np.nonzero(((LOWER_MASK & lower_mask) == 0)
                                  & ((UPPER_MASK & upper_mask) == 0))[0]
                for i in free:
                    stack.append((chosen + (int(i),), lower_mask | int(LOWER_MASK[i]),
                                  upper_mask | int(UPPER_MASK[i])))
    check(seven_labels and COUNTERS[4]["leaves"] == 0,
          "every leaf of order 3 uses 7 labels, so P(4) has no term: P(4) = 0",
          record=f"{RESULTS}/lovelock-report.json, check k4_tensor_vanishes")
    '''),
    md(r"""
    ## 9. Three classical identities, and the traces

    **Order 1 is Einstein's tensor, derived line by line.** Expand the $3 \times 3$
    determinant $\delta^{h h_1 h_2}_{j j_1 j_2}$ along its column of $h$ (rows belong to
    the lower labels $j, j_1, j_2$, columns to the upper labels $h, h_1, h_2$):

    $$\delta^{h h_1 h_2}_{j j_1 j_2} = \delta^h_j\, \delta^{h_1 h_2}_{j_1 j_2}
      - \delta^h_{j_1}\, \delta^{h_1 h_2}_{j j_2} + \delta^h_{j_2}\,
      \delta^{h_1 h_2}_{j j_1}.$$

    (Each term is an entry of the column times the $2 \times 2$ determinant left when
    its row and the column are removed, with the signs $+, -, +$.) Multiply by
    $R^{j_1 j_2}{}_{h_1 h_2}$ and sum. Since $\delta^{h_1 h_2}_{j_1 j_2} =
    \delta^{h_1}_{j_1}\delta^{h_2}_{j_2} - \delta^{h_2}_{j_1}\delta^{h_1}_{j_2}$, the
    first term gives $\delta^h_j (R^{h_1 h_2}{}_{h_1 h_2} - R^{h_2 h_1}{}_{h_1 h_2})
    = 2R\,\delta^h_j$ (antisymmetry, and $\sum R^{ab}{}_{ab} = R$). The second gives
    $-(R^{h j_2}{}_{j j_2} - R^{h j_2}{}_{j_2 j}) = -2 R^h{}_j$. The third gives
    $R^{j_1 h}{}_{j j_1} - R^{j_1 h}{}_{j_1 j} = 2 R^{j_1 h}{}_{j j_1} = -2 R^h{}_j$.
    Together

    $$P_{(1)}{}^h{}_j = 2R\,\delta^h_j - 4 R^h{}_j = -4\big(R^h{}_j - \tfrac12 R\,
      \delta^h_j\big) = -4\, G^h{}_j,$$

    and in the same way $L_{(1)} = \delta^{h_1 h_2}_{j_1 j_2} R^{j_1 j_2}{}_{h_1 h_2} =
    2R$.

    **Order 2 is the Gauss-Bonnet tensor.** The same expansion, done twice, gives
    $P_{(2)} = -8\,\mathcal{H}$ and $L_{(2)} = 4\,\mathrm{GB}$, with the Gauss-Bonnet
    scalar $\mathrm{GB} = R^2 - 4 R^a{}_b R^b{}_a + R^{ab}{}_{cd} R^{cd}{}_{ab}$ and
    Lanczos's tensor
    $2\mathcal{H}^h{}_j = 4\big(R R^h{}_j - 2 R^h{}_a R^a{}_j - 2 R^{ha}{}_{jb} R^b{}_a
    + R^{ha}{}_{bc} R^{bc}{}_{ja}\big) - \delta^h_j\, \mathrm{GB}$ (the derivation is
    written out in the Revision checker `check_lovelock_gkd.py`, which also confirmed the
    factors $-4$ and $-8$ on random curvature tensors).

    **Order 3 is the cubic Lovelock density.** $L_{(3)} = 8\,(2T_1 + 8T_2 + 24T_3 + 3T_4
    + 24T_5 + 16T_6 - 12T_7 + T_8)$ with the eight cubic invariants
    $T_1 = R^{ab}{}_{cd}R^{cd}{}_{ef}R^{ef}{}_{ab}$,
    $T_2 = R^{ab}{}_{cd}R^{ce}{}_{bf}R^{df}{}_{ae}$,
    $T_3 = R^{ab}{}_{cd}R^{cd}{}_{be}R^e{}_a$,
    $T_4 = R\,R^{ab}{}_{cd}R^{cd}{}_{ab}$,
    $T_5 = R^{ab}{}_{cd}R^c{}_aR^d{}_b$,
    $T_6 = R^a{}_bR^b{}_cR^c{}_a$, $T_7 = R\,R^a{}_bR^b{}_a$, $T_8 = R^3$ (the
    coefficients were derived by the Revision checker from 9 random curvature tensors).

    The next three cells compute, from `ENTRIES` and with the exact polynomial
    arithmetic, the Ricci tensor, the Ricci scalar and Einstein's tensor; then the
    Gauss-Bonnet scalar and tensor; then the eight cubic invariants; and each checks its
    identity for all 64 components. The first cell checks order 1. `RM` is the
    dictionary of the entries, `get(key, {})` gives the empty polynomial (zero) for a
    missing key, `poly_sum` adds a list of polynomials, `constant(n)` is the polynomial
    with the single number $n$, and `delta[h, j]` is the polynomial 1 for $h = j$ and 0
    otherwise.
    """),
    code(r'''
    RM = dict(ENTRIES)  # (a, b, c, d) -> R^ab_cd as a polynomial dict


    def poly_sum(polynomials):
        """The sum of a list of polynomials."""
        total = {}
        for p in polynomials:
            total = poly_add(total, p)
        return total


    def constant(n):
        """The polynomial with the single number n."""
        return {(0, 0, 0, 0, 0, 0): Fraction(n)}


    RIC = {(h, j): poly_sum(RM.get((h, a, j, a), {}) for a in range(8))
           for h in range(8) for j in range(8)}  # R^h_j
    R_SCALAR = poly_sum(RIC[h, h] for h in range(8))  # R
    delta = {(h, j): (ONE if h == j else {}) for h in range(8) for j in range(8)}
    EINSTEIN = {hj: poly_add(RIC[hj], poly_mul(delta[hj], R_SCALAR), Fraction(-1, 2))
                for hj in RIC}  # G = Ric - R/2
    check(all(P[1].get(hj, {}) == poly_mul(constant(-4), EINSTEIN[hj])
              for hj in EINSTEIN) and L[1] == poly_add({}, R_SCALAR, 2),
          "P(1) = -4 G for all 64 components and L(1) = 2 R",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
                 "k1_equals_minus_4_einstein and L1_equals_2R")
    '''),
    md(r"""
    The next cell checks order 2. It forms the two squares $R^a{}_b R^b{}_a$ and
    $R^{ab}{}_{cd} R^{cd}{}_{ab}$, the Gauss-Bonnet scalar
    $\mathrm{GB} = R^2 - 4 R^a{}_b R^b{}_a + R^{ab}{}_{cd} R^{cd}{}_{ab}$, and, for each
    of the 64 pairs $(h, j)$, the four sums of Lanczos's tensor $2\mathcal{H}^h{}_j$
    written above (`t` collects them before the factor 4 and the term
    $-\delta^h_j\,\mathrm{GB}$ are applied).
    """),
    code(r'''
    ric_square = poly_sum(poly_mul(RIC[a, b], RIC[b, a]) for a in range(8)
                          for b in range(8))  # R^a_b R^b_a
    riem_square = poly_sum(poly_mul(v, RM[(c, d, a, b)]) for (a, b, c, d), v in
                           RM.items() if (c, d, a, b) in RM)  # R^ab_cd R^cd_ab
    GB = poly_add(poly_add(poly_mul(R_SCALAR, R_SCALAR), ric_square, -4), riem_square)
    two_h = {}  # 2 H^h_j
    for h in range(8):
        for j in range(8):
            t = poly_mul(R_SCALAR, RIC[h, j])
            t = poly_add(t, poly_sum(poly_mul(RIC[h, a], RIC[a, j]) for a in range(8)),
                         -2)
            t = poly_add(t, poly_sum(poly_mul(RM.get((h, a, j, b), {}), RIC[b, a])
                                     for a in range(8) for b in range(8)), -2)
            t = poly_add(t, poly_sum(poly_mul(v, RM.get((b, c, j, a), {}))
                                     for (hh, a, b, c), v in RM.items() if hh == h))
            two_h[h, j] = poly_add(poly_mul(constant(4), t), poly_mul(delta[h, j], GB),
                                   -1)
    check(all(P[2].get(hj, {}) == poly_mul(constant(-4), two_h[hj]) for hj in two_h)
          and L[2] == poly_add({}, GB, 4),
          "P(2) = -8 times the Gauss-Bonnet tensor for all 64 components and L(2) = 4 GB",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, checks "
                 "k2_equals_minus_8_gauss_bonnet and L2_equals_4_gauss_bonnet")
    '''),
    md(r"""
    The next cell computes the eight cubic invariants, in the same mixed form as the
    Revision checker (sums over the nonzero entries), and checks the cubic identity.
    """),
    code(r'''
    T = [{} for _ in range(8)]  # T1 ... T8
    for (a, b, c, d), v in RM.items():
        for (c2, d2, e, f), w in RM.items():
            if (c2, d2) == (c, d) and (e, f, a, b) in RM:  # R^ab_cd R^cd_ef R^ef_ab
                T[0] = poly_add(T[0], poly_mul(poly_mul(v, w), RM[(e, f, a, b)]))
        for e in range(8):
            for f in range(8):
                if (c, e, b, f) in RM and (d, f, a, e) in RM:  # R^ab_cd R^ce_bf R^df_ae
                    T[1] = poly_add(T[1], poly_mul(poly_mul(v, RM[(c, e, b, f)]),
                                                   RM[(d, f, a, e)]))
            if (c, d, b, e) in RM:  # R^ab_cd R^cd_be R^e_a
                T[2] = poly_add(T[2], poly_mul(poly_mul(v, RM[(c, d, b, e)]), RIC[e, a]))
        T[4] = poly_add(T[4], poly_mul(poly_mul(v, RIC[c, a]), RIC[d, b]))  # R R^c_a R^d_b
    T[3] = poly_mul(R_SCALAR, riem_square)  # R R^ab_cd R^cd_ab
    T[5] = poly_sum(poly_mul(poly_mul(RIC[a, b], RIC[b, c]), RIC[c, a])
                    for a in range(8) for b in range(8) for c in range(8))
    T[6] = poly_mul(R_SCALAR, ric_square)  # R R^a_b R^b_a
    T[7] = poly_mul(poly_mul(R_SCALAR, R_SCALAR), R_SCALAR)  # R^3
    density = {}
    for coefficient, t in zip([2, 8, 24, 3, 24, 16, -12, 1], T):
        density = poly_add(density, t, coefficient)
    check(L[3] == poly_add({}, density, 8),
          "L(3) = 8 (2 T1 + 8 T2 + 24 T3 + 3 T4 + 24 T5 + 16 T6 - 12 T7 + T8)",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, check "
                 "L3_equals_8_cubic_lovelock_density")
    '''),
    md(r"""
    **The expansion along the column of $h$, for every order (derived line by line).**
    The delta of $P_{(k)}$ is the determinant of a $(2k + 1) \times (2k + 1)$ matrix
    whose rows belong to the lower labels $j, j_1, \dots, j_{2k}$ (in this order) and
    whose columns belong to the upper labels $h, h_1, \dots, h_{2k}$. Expand it along
    its first column, the column of $h$ (Laplace's rule, section 3).

    1. The first entry of the column is $\delta^h_j$, in row 1 and column 1: its sign
       is $(-1)^{1+1} = +1$, and its minor is $\delta^{h_1 \dots h_{2k}}_{j_1 \dots
       j_{2k}}$. Multiplied by the curvature factors and summed, it gives
       $\delta^h_j\, L_{(k)}$, by the definition of the scalar.
    2. The entry in row $r + 1$ ($r = 1, \dots, 2k$) is $\delta^h_{j_r}$, with the sign
       $(-1)^{(r+1)+1} = (-1)^r$. Its minor has the rows $j, j_1, \dots, j_{r-1},
       j_{r+1}, \dots, j_{2k}$. Moving the row of $j$ down past the $r - 1$ rows
       $j_1, \dots, j_{r-1}$ is $r - 1$ exchanges of neighbouring rows, so the minor is
       $(-1)^{r-1}$ times the delta whose lower list is $j_1, \dots, j_{2k}$ with $j$
       in place $r$. The two signs give $(-1)^r (-1)^{r-1} = -1$.
    3. The factor $\delta^h_{j_r}$ is 1 only for $j_r = h$, so the sum over $j_r$
       puts $h$ into the curvature factor that held $j_r$. Term $r$ is therefore
       $-\delta^{h_1 \dots h_{2k}}_{j_1 \dots j \dots j_{2k}} R \cdots R$, with $j$ in
       place $r$ of the delta and $h$ in place $r$ of the upper labels of the factors.
    4. The $2k$ terms are equal. If $r$ is the second place of its factor
       $R^{j_{r-1} j_r}{}_{h_{r-1} h_r}$, exchange the rows $r - 1$ and $r$ of the
       delta (sign $-1$) and write $R^{j_{r-1} h}{}_{\dots} = -R^{h j_{r-1}}{}_{\dots}$
       (sign $-1$): the term is unchanged and $h$ stands first. If the factor is not
       the first one, exchange it with the first factor: the product of the factors is
       unchanged, and in the delta two pairs of rows and the two matching pairs of
       columns change places; each such exchange of two pairs is two exchanges of two
       rows (or columns), sign $(-1)^2 = +1$ for the rows and $+1$ for the columns.
       After renaming the summed labels every term is the term $r = 1$.
    5. Hence, with $Y_{(k)}{}^h{}_j = \sum \delta^{h_1 \dots h_{2k}}_{j\, j_2 \dots
       j_{2k}}\, R^{h j_2}{}_{h_1 h_2} R^{j_3 j_4}{}_{h_3 h_4} \cdots
       R^{j_{2k-1} j_{2k}}{}_{h_{2k-1} h_{2k}}$,

    $$P_{(k)}{}^h{}_j = \delta^h_j\, L_{(k)} - 2k\, Y_{(k)}{}^h{}_j .$$

    For $k = 1$: $Y_{(1)}{}^h{}_j = \delta^{h_1 h_2}_{j j_2} R^{h j_2}{}_{h_1 h_2} =
    R^{h j_2}{}_{j j_2} - R^{h j_2}{}_{j_2 j} = 2 R^h{}_j$, and $P_{(1)} = 2R\,\delta
    - 4 R^h{}_j = -4G$, the result above. The next cell computes $Y_{(k)}$ for
    $k = 1, 2, 3$ with GKD (the sum of section 8, with the first entry required to
    carry the upper label $h$) and checks the expansion for all 64 components exactly.
    """),
    code(r'''
    def expansion_sum(k):
        """Y_(k)^h_j as {(h, j): polynomial}: like lovelock_sum, but the first entry
        R^{h j2}_{h1 h2} must have the upper label h, and the delta has the lower list
        (j, j2, ..., j2k) and the upper list (h1, ..., h2k)."""
        result = {}
        for h in range(8):
            first = [i for i, (key, _) in enumerate(ENTRIES) if key[0] == h]
            for j in range(8):
                bucket = {}
                stack = []
                for i in first:  # the first factor R^{h j2}_{h1 h2}
                    a, b, c, d = ENTRIES[i][0]
                    if b != j:  # j2 = j would repeat j in the lower list: GKD = 0
                        stack.append(((i,), (1 << j) | (1 << b), (1 << c) | (1 << d)))
                while stack:
                    chosen, lower_mask, upper_mask = stack.pop()
                    if len(chosen) == k:  # a leaf
                        if lower_mask != upper_mask:
                            continue  # a lower label is missing above: GKD = 0
                        lower = [j, ENTRIES[chosen[0]][0][1]] + [
                            x for i in chosen[1:] for x in ENTRIES[i][0][:2]]
                        upper = [x for i in chosen for x in ENTRIES[i][0][2:]]
                        sign = gkd(lower, upper)
                        if sign != 0:
                            key = tuple(sorted(chosen))
                            bucket[key] = bucket.get(key, 0) + sign
                        continue
                    free = np.nonzero(((LOWER_MASK & lower_mask) == 0)
                                      & ((UPPER_MASK & upper_mask) == 0))[0]
                    for i in free:
                        stack.append((chosen + (int(i),), lower_mask | int(LOWER_MASK[i]),
                                      upper_mask | int(UPPER_MASK[i])))
                total = {}
                for key, weight in bucket.items():
                    product = ONE
                    for i in key:
                        product = poly_mul(product, ENTRIES[i][1])
                    total = poly_add(total, product, weight)
                result[h, j] = total
        return result


    Y = {k: expansion_sum(k) for k in (1, 2, 3)}
    expansion_holds = all(
        P[k].get((h, j), {})
        == poly_add(poly_mul(delta[h, j], L[k]), Y[k][h, j], -2 * k)
        for k in (1, 2, 3) for h in range(8) for j in range(8))
    check(expansion_holds and all(Y[1][hj] == poly_add({}, RIC[hj], 2) for hj in RIC),
          "P(k) = delta L(k) - 2k Y(k) for all 64 components, k = 1, 2, 3; Y(1) = 2 Ric")
    '''),
    md(r"""
    **The trace identity.** Set $j = h$ in the expansion and sum over $h$. The first
    term gives $\sum_h \delta^h_h\, L_{(k)} = 8\, L_{(k)}$ (eight values of $h$). In
    $\sum_h Y_{(k)}{}^h{}_h$ the label $h$ is summed like $j_1$ in the definition of
    the scalar; renaming it $j_1$ gives exactly $L_{(k)}$. So
    $\sum_h P_{(k)}{}^h{}_h = 8 L_{(k)} - 2k\, L_{(k)} = (8 - 2k)\, L_{(k)}$. The next
    cell checks it for $k = 1, 2, 3$, and prints the three scalars and, with the
    function `from_mathematica` of section 7, the eighth-order scalar $L_{(4)}$ that
    the program printed in section 5, in general and on the history of the record,
    where $a_4' = H$, $a_4'' = 0$, $u = 4H/3$, $v = 0$ and $k = e^{(2/3) H x_4}$ stays a
    symbol (`show` writes a polynomial dictionary as text).
    """),
    code(r'''
    def show(p):
        """A polynomial dict as text in H, A1, A2, U, V, K."""
        return str(sp.expand(sum(c * sp.prod([s ** e for s, e in zip(VARIABLES, m)])
                                 for m, c in p.items())))


    for k in (1, 2, 3):
        trace = poly_sum(P[k].get((h, h), {}) for h in range(8))
        report(f"Lovelock scalar L({k})", show(L[k]))
        check(trace == poly_add({}, L[k], 8 - 2 * k),
              f"the trace of P({k}) is (8 - {2 * k}) L({k})",
              record=f"{RESULTS}/lovelock-report.json, check k{k}_trace_identity")
    L4 = from_mathematica(l4_text)  # the scalar printed by the program in section 5
    report("eighth-order scalar L(4) (the Euler density)", L4)
    report("L(4) on the history of the record (H = 1)",
           sp.factor(L4.subs({H: 1, A1: 1, A2: 0, U: sp.Rational(4, 3), V: 0})))
    '''),
    md(r"""
    ## 10. The components of the three tensors at one moment

    The field equations for $a_4$ and $b_4$ (chapter 12) use the normalised tensors
    $E_{(k)} = -P_{(k)}/2^{k+1}$ of section 4. The next cell draws all 64 components
    of $E_{(1)}$ (Einstein's tensor $G$), $E_{(2)}$ and $E_{(3)}$ as three
    $8 \times 8$ tables, at the moment $x_4 = 0$ of the history of the Revision record
    ($a_4' = H$, $a_4'' = 0$, $u = 4H/3$, $v = 0$, $k = 1$, the left table of the plane
    curvatures), in units of $H^2$, $H^4$ and $H^6$ (that is, with $H = 1$). The
    function `poly_value` evaluates a polynomial dictionary exactly at a point given as
    the tuple $(H, a_4', a_4'', u, v, k)$. Each square shows the exact number of row
    $h$ and column $j$; red is positive, blue negative, white zero, and each table has
    its own colour scale (its largest value is the darkest colour). The tables show what
    sections 7 and 8 proved: only the diagonal is filled, the $x_4$-$x_0$ squares are
    zero, the three space entries are equal, and the hidden entry $x_0$ equals the three
    extra-time entries.
    """),
    code(r'''
    def poly_value(p, point):
        """The exact value (a Fraction) of the polynomial dict p at the point
        (H, a4', a4'', u, v, k)."""
        total = Fraction(0)
        for m, coefficient in p.items():
            term = coefficient
            for value, exponent in zip(point, m):
                term *= Fraction(value) ** exponent
            total += term
        return total


    POINT = (1, 1, 0, Fraction(4, 3), 0, 1)  # H, a4', a4'', u, v, k at x4 = 0
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.6))
    tables = {}
    for ax, k in zip(axes, (1, 2, 3)):
        scale = Fraction(-1, 2 ** (k + 1))  # E_(k) = -P_(k) / 2^(k+1)
        table = [[scale * poly_value(P[k].get((h, j), {}), POINT) for j in range(8)]
                 for h in range(8)]  # exact fractions
        tables[k] = table
        numbers = np.array([[float(x) for x in row] for row in table])
        largest = np.abs(numbers).max()
        ax.imshow(numbers, cmap="RdBu_r", vmin=-largest, vmax=largest)
        for h in range(8):
            for j in range(8):
                if h != j:
                    colour = "0.6"  # grey zeros off the diagonal
                elif abs(numbers[h, j]) > 0.6 * largest:
                    colour = "white"  # white on the darkest squares, to stay readable
                else:
                    colour = "black"
                ax.text(j, h, str(table[h][j]), ha="center", va="center",
                        fontsize=6 if h == j else 5.5, color=colour)
        ax.set_xticks(range(8), NAMES)
        ax.set_yticks(range(8), NAMES)
        ax.set_xlabel("lower label $j$")
        ax.set_ylabel("upper label $h$")
        ax.set_title(f"$E_{{({k})}}{{}}^h{{}}_j$ in units of $H^{{{2 * k}}}$")
        ax.grid(False)
    fig.tight_layout()
    save_figure(fig, "lovelock_component_tables",
                "All 64 components $E_{(k)}{}^h{}_j$ of the normalised Lovelock tensors "
                "$E_{(1)} = G$ (left), $E_{(2)}$ (middle) and $E_{(3)}$ (right) of the "
                "corrected metric at the moment $x_4 = 0$ of the history of the record, "
                "where $a_4^{\\prime} = H$, $u = 4H/3$, $k = 1$ and "
                "$a_4^{\\prime\\prime} = v = 0$, in units of $H^2$, $H^4$ and $H^6$, as "
                "exact fractions; row $h$, column $j$; red positive, blue negative, "
                "white zero, each table on its own colour scale. Only the diagonal is "
                "filled, so the $x_4$-$x_0$ components vanish; the three space entries "
                "are equal, and the hidden entry $x_0$ equals the three extra-time "
                "entries, for example $-2/3$ for Einstein's tensor.")
    diagonal_ok = all(
        all(tables[k][h][j] == 0 for h in range(8) for j in range(8) if h != j)
        and tables[k][1][1] == tables[k][2][2] == tables[k][3][3]
        and tables[k][0][0] == tables[k][5][5] == tables[k][6][6] == tables[k][7][7]
        for k in (1, 2, 3))
    say("diagonals (x0 ... x7):")
    for k in (1, 2, 3):
        say(f"  E({k}): " + " ".join(str(tables[k][h][h]) for h in range(8)))
    check(diagonal_ok and [tables[1][h][h] for h in range(8)]
          == [Fraction(-2, 3)] + [Fraction(41, 9)] * 3 + [Fraction(19, 3)]
          + [Fraction(-2, 3)] * 3,
          "at x4 = 0 on the history of the record: only diagonal entries, space entries "
          "equal, hidden entry = extra-time entries; G = diag(-2/3, 41/9, 41/9, 41/9, "
          "19/3, -2/3, -2/3, -2/3) H^2")
    '''),
    md(r"""
    ## 11. The Revision records quoted in this notebook

    This notebook quotes check names and numbers from the Revision records. The four
    result files of the Rust program were compared in full in section 5 (byte for byte),
    and its counters in sections 6 and 8. The next cell reads the verification reports
    once more and checks the rest of what the text quotes, so that a later change of a
    record cannot pass unnoticed:

    - every check quoted from the sympy verification `python-lovelock-report.json` and
      from the Rust report `lovelock-report.json` is present with the verdict PASS;
    - the sympy verification has 56 checks and the Wolfram verification
      `wolfram-gkd-report.json` has 29 checks, none of them failed, as section 4 says.

    The function `verdicts(path)` returns, for one report, a dictionary from the name of
    each check to its verdict. The reports store their checks in one of two forms: a
    list of entries, each with a `name` and a `verdict`, or a dictionary from the name to
    an entry whose field `passed` is true or false; the function reads both.
    """),
    code(r'''
    def verdicts(path):
        """{check name: "PASS" or "FAIL"} of the Revision report at `path`."""
        data = json.loads(repository_file(path).read_text(encoding="utf-8"))
        checks = data["checks"]
        if isinstance(checks, dict):  # name -> {"passed": true or false, ...}
            return {name: "PASS" if entry["passed"] else "FAIL"
                    for name, entry in checks.items()}
        return {entry["name"]: entry["verdict"] for entry in checks}  # a list of entries


    QUOTED = {  # report -> the checks that this notebook quotes from it
        "python-lovelock-report.json": [
            "rust_riemann_agrees", "rust_k1_mixed_components_agree",
            "rust_k2_mixed_components_agree", "rust_k3_mixed_components_agree",
            "rust_L1_agrees", "rust_L2_agrees", "rust_L3_agrees",
            "k1_unpruned_literal_sum_agrees", "k2_unpruned_literal_sum_agrees",
            "k1_equals_minus_4_einstein", "L1_equals_2R",
            "k2_equals_minus_8_gauss_bonnet", "L2_equals_4_gauss_bonnet",
            "L3_equals_8_cubic_lovelock_density", "normalisation_P1_derived_minus_4",
            "normalisation_P2_derived_minus_8", "normalisation_L3_cubic_derived",
            "mixed_riemann_only_sectional", "rust_christoffels_agree"],
        "lovelock-report.json": [
            "riemann_antisymmetry", "mixed_riemann_free_of_x0",
            "mixed_riemann_only_sectional", "k1_trace_identity", "k2_trace_identity",
            "k3_trace_identity", "k1_offdiagonal_vanishes", "k2_offdiagonal_vanishes",
            "k3_offdiagonal_vanishes", "k1_hidden_equals_extra_times",
            "k2_hidden_equals_extra_times", "k3_hidden_equals_extra_times",
            "k4_tensor_vanishes", "k1_brute_force_numeric", "k2_brute_force_numeric"],
    }
    for report_name, names in QUOTED.items():
        found = verdicts(f"{RESULTS}/{report_name}")
        missing = [name for name in names if found.get(name) != "PASS"]
        say(f"{report_name}: {len(names)} quoted checks; not there or not PASS: "
            f"{missing if missing else 'none'}")
        check(not missing,
              f"the {len(names)} checks quoted from {report_name} are there and PASS",
              record=f"{RESULTS}/{report_name}, checks " + ", ".join(names))
    totals = {}
    for report_name in ("python-lovelock-report.json", "wolfram-gkd-report.json"):
        data = json.loads(repository_file(f"{RESULTS}/{report_name}").read_text(
            encoding="utf-8"))
        totals[report_name] = (data["checkCount"], data["failedCheckCount"],
                               data["verdict"])
        say(f"{report_name}: {data['checkCount']} checks, {data['failedCheckCount']} "
            f"failed, verdict {data['verdict']}")
    check(totals == {"python-lovelock-report.json": (56, 0, "SUCCESS"),
                     "wolfram-gkd-report.json": (29, 0, "SUCCESS")},
          "the sympy verification has 56 checks and the Wolfram verification 29, none "
          "failed",
          record=f"{RESULTS}/python-lovelock-report.json and wolfram-gkd-report.json, "
                 "checkCount and failedCheckCount")
    '''),
    md(r"""
    The last cell checks that all five figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_files = [f"11b_{k}_{name}.png" for k, name in enumerate(
        ["work_of_the_sums", "curvature_of_planes", "riemann_matrix",
         "mixing_terms_vanish", "lovelock_component_tables"], 1)]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
          "all five figure files of the notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 12. What this notebook showed

    - The Revision Rust program `lovelock_gkd`, built here, computed the curvature and
      the three Lovelock tensors of the corrected metric, passed its 27 checks
      (including the literal unpruned sums of orders 1 and 2), and wrote its four result
      files again, byte for byte equal to the Revision records (the report apart from
      its two rounding errors).
    - The curvature, recomputed independently with sympy, has 21 nonzero Christoffel
      symbols and 112 nonzero components $R^{ab}{}_{cd}$, the curvatures of the 28
      coordinate planes; they are polynomials in $H$, $a_4'$, $a_4''$, $u = b_4'/b_4$,
      $v = u'$ and $k = e^{2a_4}/b_4$, free of $x_0$. Planes in ordinary space have the
      curvature $a_4'^2$, planes of ordinary space with the hidden direction or an extra
      time $-a_4'(a_4' - u/2)$, planes inside the block of the hidden direction and the
      extra times $(a_4' - u/2)^2 - H^2 k$; the hidden direction behaves like an extra
      time.
    - No curvature component mixes the time with the hidden direction: in each possible
      term one of two factors vanishes (3-space has no warp along $x_0$; the extra times
      change in time at the rate of the hidden direction).
    - Pruning (only nonzero curvature entries, no repeated labels) reduces the sum of
      order 3 from about $4.4 \times 10^{12}$ terms to 322,560 GKD calls; a Python
      implementation of the same plan, written independently, reproduces every counter
      of the Rust program and all $3 \times 64$ components and the three scalars exactly.
      The literal sums of orders 1 and 2, with GKD called on every one of 7,280 and
      815,360 index lists and nothing skipped, give the same tensors: the skipping
      changes nothing.
    - Every Lovelock tensor expands along the column of its free upper label as
      $P_{(k)} = \delta\, L_{(k)} - 2k\, Y_{(k)}$ (derived line by line and checked
      exactly for $k = 1, 2, 3$); for $k = 1$ this gives Einstein's tensor, and for
      every $k$ the trace identity $\sum_h P_{(k)}{}^h{}_h = (8 - 2k) L_{(k)}$.
    - Only the eight diagonal components of each Lovelock tensor are nonzero; the three
      space entries are equal, and the hidden entry equals the three extra-time entries.
      Order 1 is $-4$ times Einstein's tensor, order 2 is $-8$ times the Gauss-Bonnet
      tensor, the third scalar is 8 times the cubic Lovelock density, and $P_{(4)} = 0$
      (PROVED by exact computation).
    - Every check that the notebook quotes from the Revision verifications is present in
      them with the verdict PASS, and the sympy and Wolfram verifications have 56 and 29
      checks, none of which failed.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
