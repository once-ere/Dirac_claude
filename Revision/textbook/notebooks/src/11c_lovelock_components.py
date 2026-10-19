#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Builder of Notebook 11c, "The Lovelock tensors along the deflating history: components
and identities" (textbook "Universes in Pairs", chapter 11 "GKD and the Lovelock
tensors").

The notebook Revision/textbook/notebooks/11c_lovelock_components.ipynb is BUILT from this
file by Revision/textbook/tools/nbkit.py (never edit the .ipynb by hand):

    python Revision/textbook/tools/nbkit.py build \
        Revision/textbook/notebooks/src/11c_lovelock_components.py --date YYYY-MM-DD
    python Revision/textbook/tools/nbkit.py check \
        Revision/textbook/notebooks/src/11c_lovelock_components.py

Revision sources (read in full before this builder was written):
Revision/gkd_lovelock/results/lovelock-tensors.json, lovelock-report.json,
python-lovelock-report.json; Revision/docs/LOVELOCK_GKD.md (sections 6 and 9);
Revision/docs/METRIC_SELF_CONSISTENCY.md (sections 3 to 5);
Revision/field_equations_a4/a4-equations.json (its lovelockTensors, generalSource and
exponentialHistory entries) and reports/python-a4-report.json (checks
json_lovelock_components, constraint_first_order, second_order_system, bianchi_x4,
independent_components, author_weights_history_source).

Rewritten on 2026-10-18 for the corrected metric of 2026-10-16 (version 2,
Revision/SPEC.md section 1): the components are polynomials in H, a4', a4'', u = b4'/b4,
v = u' and k = e^(2 a4)/b4; the hidden component equals the extra-time component; the
history of the record is a4 = A H x4, b4 = b4(0) e^((4/3) A H x4) with A = 1, b4(0) = 1.
The test history of section 9 is an ILLUSTRATION chosen here, not a Revision result and
not a solution of any field equation; the notebook says so.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from nbkit import code, md, run_builder  # noqa: E402

FIGURES = [
    "components_linear_history",
    "lovelock_scalars",
    "test_history",
    "components_test_history",
    "conservation_identity",
]

FACTS = {
    "id": "11c",
    "name": "11c_lovelock_components",
    "title": "The Lovelock tensors along the deflating history: components and identities",
    "purpose": (
        "It reads the exact components of the three Lovelock tensors of the corrected "
        "metric of the Revision record from the record lovelock-tensors.json, writes "
        "the normalised tensors E(1) (the Einstein tensor), E(2) and E(3) as polynomials "
        "in H, the first and second time derivatives of a4, u = b4 prime / b4, its time "
        "derivative v and k = exp(2 a4) / b4, reproduces the components recorded for the "
        "field equations of a4 and b4 and by the independent sympy verification, proves "
        "with sympy their structure (diagonal, equal components within ordinary space, "
        "the hidden component equal to the extra-time component, a time component "
        "without second derivatives, components linear in the second derivatives with "
        "the recorded coefficient matrix, at most linear in k for the hidden direction, "
        "unchanged under the reversal of the time, the order of each term) and the two "
        "conservation identities, plots every component and the three Lovelock scalars "
        "along the deflating history of the record and as functions of its slope, "
        "reproduces the source that this history needs, for Einstein gravity and for the "
        "author's weights, and plots the components along an illustrative test history "
        "with a numerical check of the conservation identity; it checks again that "
        "every check and statement it quotes from the Revision records is there, every "
        "check with the verdict PASS; it draws five figures."
    ),
    "records": [
        ["Revision/gkd_lovelock/results/lovelock-tensors.json",
         "the exact components of the Lovelock tensors P(k) and the scalars L(k), "
         "k = 1, 2, 3, for general a4 and b4, read by the notebook"],
        ["Revision/gkd_lovelock/results/python-lovelock-report.json",
         "its list `independentResults` of the nonzero components, reproduced"],
        ["Revision/gkd_lovelock/results/lovelock-report.json",
         "its checks `k1_divergence_free` to `k3_divergence_free`, reproduced by the two "
         "conservation identities, and its checks on the diagonal form, quoted"],
        ["Revision/field_equations_a4/a4-equations.json",
         "the normalised components E(1), E(2), E(3) in its entry `lovelockTensors`, the "
         "coefficient matrix `secondOrderJacobian` and the source of the history in "
         "`exponentialHistory`, reproduced; its statements `hiddenEqualsExtraTimes`, "
         "`constraint_propagation`, `energyExchange` and `offDiagonal`, quoted and "
         "checked"],
        ["Revision/field_equations_a4/reports/python-a4-report.json",
         "its checks `json_lovelock_components`, `constraint_first_order`, "
         "`second_order_system`, `bianchi_x4`, `independent_components` and "
         "`author_weights_history_source`, reproduced"],
    ],
    "packages": ["numpy", "sympy", "matplotlib"],
    "needs_rust": [],
    "expected_seconds": 20,
    "timeout_seconds": 300,
    "files_written": ["Revision/textbook/figures/11c.captions.json"] + [
        f"Revision/textbook/figures/11c_{k}_{name}.png"
        for k, name in enumerate(FIGURES, 1)
    ],
    "final_lines": [
        "PASS all five figure files of the notebook exist",
        "ALL 22 CHECKS PASSED (notebook 11c)",
    ],
    "troubleshooting": [],
}

CELLS = [
    md(r"""
    ## 1. What this notebook computes

    Notebook 11b computed the three Lovelock tensors $P_{(1)}, P_{(2)}, P_{(3)}$ of the
    corrected metric of the Revision record and found that only their eight diagonal
    components are not zero. This notebook studies those components: what they look
    like, which structure they have, and how they behave as the extra times deflate. It

    - reads the exact components from the Revision record `lovelock-tensors.json` and
      forms the normalised tensors $E_{(k)} = -P_{(k)}/2^{k+1}$ ($E_{(1)}$ is Einstein's
      tensor $G$), and checks that they are the components recorded for the field
      equations of $a_4$ and $b_4$ in `Revision/field_equations_a4/a4-equations.json`
      and by the Revision's independent sympy verification;
    - proves with sympy their structure: only the diagonal is filled, the three space
      components are equal, the hidden component equals the three extra-time
      components, the time component contains no second derivative, the other
      components are linear in the second derivatives (with the coefficient matrix of
      the record), the hidden component is at most linear in $k = e^{2a_4}/b_4$, every
      component is unchanged when the time is reversed, and every term of order $k$ is
      $2k$ powers of an inverse length;
    - derives and checks the two conservation identities (the Bianchi identities) that
      every Lovelock tensor obeys in this metric;
    - draws the components and the Lovelock scalars along the deflating history of the
      record and as functions of its slope, and reproduces the source that this history
      needs, for Einstein gravity and for the author's weights;
    - draws the components along an illustrative test history in which the deflation
      speeds up, to show where the second derivatives enter, with a numerical check of
      the conservation identity along it;
    - reads the Revision records once more and checks that every check and statement
      it quotes from them is there, every quoted check with the verdict PASS.

    It draws five figures and takes about 20 seconds.
    """),
    md(r"""
    ## 3. The words used in this notebook

    - **Coordinates** $x_0, \dots, x_7$: $x_0$ the hidden direction (space-like),
      $x_1, x_2, x_3$ ordinary space, $x_4$ the time, $x_5, x_6, x_7$ the three extra
      times. The programs number them $0, \dots, 7$: the number $k$ stands for $x_k$.
    - **The metric functions** $a_4(x_4)$ and $b_4(x_4) > 0$ of the time. The scale
      factor of ordinary space is $e^{a_4}$; that of the extra times
      $e^{-a_4} b_4^{1/2} (\sin^2 z)^{1/12}$ and that of the hidden direction
      $e^{-a_4} b_4^{1/2} |\cot z|$, $z = 6 H x_0$. If $e^{a_4}$ grows, space
      **inflates**; if $e^{-a_4} b_4^{1/2}$ shrinks, the hidden direction and the extra
      times **deflate** together. The four directions $x_0, x_5, x_6, x_7$ are called
      the **block**.
    - **The six variables**: $H$; $a_4' = da_4/dx_4$ and $a_4'' = d^2 a_4/dx_4^2$;
      $u = b_4'/b_4$ and its derivative $v = du/dx_4$; and $k = e^{2a_4}/b_4$, a pure
      number. In code they are the symbols `H`, `A1`, `A2`, `U`, `V`, `K`. The block
      changes at the rate $h_4 = u/2 - a_4'$ (the derivative of
      $\ln(e^{-a_4} b_4^{1/2})$), and $k' = k\,(2a_4' - u)$.
    - **The history of the record**: $a_4 = A H x_4$, $b_4 = b_4(0)\, e^{(4/3) A H x_4}$
      with the **slope** $A = 1$ and $b_4(0) = 1$. On it $a_4' = AH$, $u = 4AH/3$,
      $a_4'' = v = 0$ and $k = e^{(2/3) A H x_4}$; the block deflates like
      $e^{-A H x_4/3}$. It is a PRESCRIBED background: no field of the Revision record
      is shown to be its source.
    - **Component** $E^h{}_j$: the number in row $h$ and column $j$ of a tensor;
      $E^{x_1}{}_{x_1}$ is written $E^{x1}_{x1}$ in printed text.
    - **Lovelock tensor** $P_{(k)}$, **normalised Lovelock tensor**
      $E_{(k)} = -P_{(k)}/2^{k+1}$, **Lovelock scalar** $L_{(k)}$: built from the
      curvature with the generalized Kronecker delta (Notebooks 11a and 11b).
    - **Covariant divergence** $\nabla_h E^h{}_j$: the derivative of a tensor that takes
      the curving of the coordinates into account (through the Christoffel symbols).
      **Bianchi identity**: the statement that it is zero for every Lovelock tensor.
    - **Constraint**: an equation without second derivatives. **Coefficient matrix**
      (Jacobian): the table of the factors with which $a_4''$ and $v$ enter two
      equations.
    - **Even function**: $f(-x) = f(x)$. **Weight**: the number of inverse lengths of a
      term ($H$, $a_4'$ and $u$ count 1; $a_4''$ and $v$ count 2; $k$ counts 0).
    - **Finite difference**: the approximation $f'(t) \approx (f(t + \epsilon) -
      f(t - \epsilon))/(2\epsilon)$ of a derivative.
    - **Illustration**: a choice made only to show how a formula behaves; it is not a
      result and not a solution of any equation.
    """),
    md(r"""
    ## 4. The physical and mathematical situation

    **The tensors.** For the corrected metric (Notebook 11b) the Lovelock tensors
    $P_{(k)}{}^h{}_j$, $k = 1, 2, 3$, are diagonal and do not depend on $x_0$; each
    component is a polynomial in the six variables. The field equations of $a_4$ and
    $b_4$ (chapter 12) use the normalised tensors

    $$E_{(k)}{}^h{}_j = -\frac{1}{2^{k+1}}\, P_{(k)}{}^h{}_j ,\qquad
      \sum_{k=1}^{3} \alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda\,\delta^\mu_\nu
      = \kappa\, T^\mu{}_\nu ,$$

    with $E_{(1)} = G$, Einstein's tensor. The independent components are
    $E^{x1}_{x1}$ (equal to $E^{x2}_{x2}$ and $E^{x3}_{x3}$: ordinary space),
    $E^{x4}_{x4}$ (the time) and $E^{x0}_{x0}$, which equals $E^{x5}_{x5}$, $E^{x6}_{x6}$
    and $E^{x7}_{x7}$ (the block of the hidden direction and the extra times).

    **The two conservation identities, derived line by line.** Every Lovelock tensor has
    zero covariant divergence (Lovelock's theorem; the Revision checked it exactly). For
    a diagonal tensor that does not depend on $x_0$ the divergence is

    $$\nabla_h P^h{}_j = \partial_h P^h{}_j + \sum_{h,m} \Gamma^h{}_{hm} P^m{}_j
      - \sum_{h,m} \Gamma^m{}_{hj} P^h{}_m .$$

    Take $j = x_4$. The first term is $\partial_4 P^4{}_4$ (only $h = x_4$ survives,
    because $P^h{}_4 = 0$ for $h \ne x_4$). In the second term only $m = x_4$ survives:
    $\sum_h \Gamma^h{}_{h4} P^4{}_4$. In the third, $P^h{}_m$ is diagonal, so $m = h$:
    $\sum_h \Gamma^h{}_{h4} P^h{}_h$. Hence

    $$\nabla_h P^h{}_4 = \partial_4 P^4{}_4 + \sum_h \Gamma^h{}_{h4}
      \big(P^4{}_4 - P^h{}_h\big).$$

    The Christoffel symbols of the metric (Notebook 11b) are $\Gamma^h{}_{h4} = a_4'$ for
    the three space directions, $\Gamma^h{}_{h4} = u/2 - a_4' = h_4$ for the hidden
    direction and the three extra times, and 0 for $x_4$. The block components are all
    equal, so the sum is $3a_4'(P^4{}_4 - P^1{}_1) + 4h_4(P^4{}_4 - P^0{}_0)$, and zero
    divergence, multiplied by $-1/2^{k+1}$, reads

    $$\frac{d}{dx_4} E^{x4}{}_{x4} = 3\, a_4'\, \big(E^{x1}{}_{x1} - E^{x4}{}_{x4}\big)
      + 4\, h_4\, \big(E^{x0}{}_{x0} - E^{x4}{}_{x4}\big),\qquad h_4 = \frac{u}{2} - a_4'.
      \qquad (\text{I})$$

    Take $j = x_0$. Nothing depends on $x_0$, and the same steps give
    $\sum_h \Gamma^h{}_{h0}(P^0{}_0 - P^h{}_h)$. Here $\Gamma^h{}_{h0} = H \cot z$ for the
    three extra times (their factor $(\sin^2 z)^{1/12}$ depends on $x_0$) and 0 for the
    space directions and $x_4$; the term $h = x_0$ is zero because
    $P^0{}_0 - P^0{}_0 = 0$. So $3H\cot z\,(P^0{}_0 - P^5{}_5) = 0$, and wherever
    $\cot z \neq 0$

    $$E^{x0}{}_{x0} = E^{x5}{}_{x5} .\qquad (\text{II})$$

    The divergences along $x_1, x_2, x_3, x_5, x_6, x_7$ vanish because nothing depends
    on these coordinates and the tensors are diagonal. In the field equations (I) becomes
    the energy balance of the source and (II) the condition $p_0 = p_t$: the pressure
    along the hidden direction equals that along the extra times (chapter 12).

    **Status.** The components are PROVED by exact computation (Revision records); the
    structure and the identities are PROVED here with sympy; the history of the record
    is a PRESCRIBED background; the test history of section 9 is an ILLUSTRATION, not a
    solution of the field equations.
    """),
    md(r"""
    ## 5. The components, from the Revision record

    The next cell reads `lovelock-tensors.json`, which lists every component of
    $P_{(k)}$, for general $a_4$ and $b_4$, as exact monomials `[numerator, denominator,
    [fourteen exponents]]`. The fourteen exponents belong, in this order, to $H$, the
    four derivatives of $a_4$, $E = e^{a_4}$, $W = (\sin^2 z)^{1/12}$, $C = \cot z$,
    $Q = b_4^{1/2}$, the four derivatives of $b_4$ and $\mathrm{sgn}(\cot z)$. The
    function `from_monomials` rebuilds each component as a sympy expression in the six
    variables, with $E^2 = k\, Q^2$, $b_4' = u\, Q^2$ and $b_4'' = (v + u^2)\, Q^2$:
    the monomial becomes $H^{e_0} a_4'^{e_1} a_4''^{e_2} k^{e_5/2} u^{e_9}
    (v + u^2)^{e_{10}}$ times $Q^{e_5 + e_8 + 2e_9 + 2e_{10}}$, and the cell stops with
    an error if this power of $Q$ is not 0 or if any of $a_4'''$, $a_4''''$, $W$, $C$,
    $b_4'''$, $b_4''''$ or $\mathrm{sgn}(\cot z)$ occurs. It forms
    $E_{(k)} = -P_{(k)}/2^{k+1}$, checks that every off-diagonal component is zero and
    which diagonal components are equal, and prints the three independent components of
    each order.
    """),
    code(r'''
    import re  # regular expressions: rewrites the record's names

    import numpy as np  # arrays of numbers
    import sympy as sp  # exact algebra

    H, A1, A2, U, V = sp.symbols("H A1 A2 U V")  # H, a4', a4'', u = b4'/b4, v = u'
    K = sp.Symbol("K", positive=True)  # k = e^(2 a4)/b4 > 0
    NAMES = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
    tensors = json.loads(repository_file(
        "Revision/gkd_lovelock/results/lovelock-tensors.json").read_text(encoding="utf-8"))


    def from_monomials(monomials):
        """A component of lovelock-tensors.json as a sympy expression in H, A1, A2, U,
        V and K."""
        total = sp.Integer(0)
        for numerator, denominator, e in monomials:
            if any(e[i] for i in (3, 4, 6, 7, 11, 12, 13)):
                raise ValueError("the component contains a third or fourth "
                                 "derivative, W, cot z or sgn(cot z)")
            if e[5] % 2 or e[5] + e[8] + 2 * e[9] + 2 * e[10] != 0:
                raise ValueError("the powers of b4 do not cancel")
            total += (sp.Rational(numerator, denominator) * H ** e[0] * A1 ** e[1]
                      * A2 ** e[2] * K ** (e[5] // 2) * U ** e[9] * (V + U ** 2) ** e[10])
        return sp.expand(total)


    P = {k: {(h, j): from_monomials(tensors[f"P{k}_mixed_up_h_down_j"][f"{a},{b}"]
                                    ["monomials"])
             for h, a in enumerate(NAMES) for j, b in enumerate(NAMES)}
         for k in (1, 2, 3)}
    E = {k: {hj: sp.expand(-value / 2 ** (k + 1)) for hj, value in P[k].items()}
         for k in (1, 2, 3)}
    check(all(E[k][h, j] == 0 for k in (1, 2, 3) for h in range(8) for j in range(8)
              if h != j),
          "every off-diagonal component of E(1), E(2), E(3) is zero, x4-x0 included, "
          "for general a4 and b4",
          record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
                 "k1_offdiagonal_vanishes to k3_offdiagonal_vanishes")
    check(all(E[k][1, 1] == E[k][2, 2] == E[k][3, 3]
              and E[k][0, 0] == E[k][5, 5] == E[k][6, 6] == E[k][7, 7]
              for k in (1, 2, 3)),
          "x1 = x2 = x3 and x0 = x5 = x6 = x7 for every order",
          record="Revision/gkd_lovelock/results/lovelock-report.json, checks "
                 "k1_hidden_equals_extra_times to k3_hidden_equals_extra_times")
    for k in (1, 2, 3):
        for h in (1, 4, 0):  # x1, x4, x0
            say(f"E({k})^{NAMES[h]}_{NAMES[h]} = {E[k][h, h]}")
    '''),
    md(r"""
    The next cell compares these components with two other Revision records. The record
    `a4-equations.json` of the field equations of $a_4$ and $b_4$ (written by the
    Revision's Wolfram derivation and checked by its sympy checker) lists $E_{(1)},
    E_{(2)}, E_{(3)}$ in the entry `lovelockTensors`, in Wolfram's input notation with
    `ad1`, `ad2`, `uu`, `vv`, `kk` for $a_4'$, $a_4''$, $u$, $v$, $k$. The record
    `python-lovelock-report.json` lists the nonzero components of $P_{(k)}$ in its entry
    `independentResults`, written with `B0`, `B1`, `B2` for $b_4$, $b_4'$, $b_4''$ and
    `E` for $e^{a_4}$; there $b_4' = u\, b_4$, $b_4'' = (v + u^2)\, b_4$ and
    $e^{a_4} = \sqrt{k\, b_4}$ are put in, and $b_4$ cancels. Both texts are turned into
    sympy expressions with `sp.sympify` (`^` is first replaced by `**`).
    """),
    code(r'''
    a4_record = json.loads(repository_file(
        "Revision/field_equations_a4/a4-equations.json").read_text(encoding="utf-8"))
    RECORD_NAMES = {"ad1": A1, "ad2": A2, "uu": U, "vv": V, "kk": K, "H": H}


    def from_text(text, names=RECORD_NAMES):
        """A formula of the records as a sympy expression."""
        return sp.sympify(text.replace("^", "**"), locals=names)


    same = all(sp.expand(from_text(a4_record["lovelockTensors"][f"E{k}"][key]["input"])
                         - E[k][h, h]) == 0
               for k in (1, 2, 3)
               for key, h in (("x0x0", 0), ("x1x1", 1), ("x4x4", 4), ("x5x5", 5)))
    check(same, "E(1), E(2), E(3) equal the components recorded for the a4 and b4 "
          "equations",
          record="Revision/field_equations_a4/reports/python-a4-report.json, check "
                 "json_lovelock_components")
    checker = json.loads(repository_file(
        "Revision/gkd_lovelock/results/python-lovelock-report.json").read_text(
            encoding="utf-8"))
    independent = checker["independentResults"]
    B0, B1, B2, EA = sp.symbols("B0 B1 B2 EA", positive=True)
    CHECKER_NAMES = {"A1": A1, "A2": A2, "H": H, "B0": B0, "B1": B1, "B2": B2, "E": EA}
    IN_SIX = {B1: U * B0, B2: (V + U ** 2) * B0, EA: sp.sqrt(K * B0)}
    same = all(
        sp.expand(from_text(text, CHECKER_NAMES).subs(IN_SIX)
                  - P[k][NAMES.index(key.split(",")[0]), NAMES.index(key.split(",")[1])])
        == 0
        for k in (1, 2, 3) for key, text in independent[f"P{k}_mixed_nonzero"].items())
    check(same and all(len(independent[f"P{k}_mixed_nonzero"]) == 8 for k in (1, 2, 3)),
          "P(1), P(2), P(3) equal the independent sympy results (8 nonzero components "
          "each)",
          record="Revision/gkd_lovelock/results/python-lovelock-report.json, "
                 "independentResults")
    '''),
    md(r"""
    ## 6. The structure of the components

    The next cell proves, for $k = 1, 2, 3$, with exact sympy algebra:

    1. $E^{x4}_{x4}$ contains neither $a_4''$ nor $v$ (`expr.has(A2)` is False): the
       time component of the field equations is a condition on $a_4'$, $u$ and $k$
       only, a **constraint**, not an equation for their change.
    2. $E^{x1}_{x1}$ and $E^{x0}_{x0}$ are linear in the second derivatives: as
       polynomials in $a_4''$ and $v$ (`sp.Poly(expr, A2, V)`) they have the total
       degree at most 1. Their coefficients form the $2 \times 2$ matrix
       $J = \big(\partial E^{x1}_{x1}/\partial a_4'',\ \partial E^{x1}_{x1}/\partial v;\
       \partial E^{x0}_{x0}/\partial a_4'',\ \partial E^{x0}_{x0}/\partial v\big)$, and
       $\sum_k \alpha_k J_{(k)}$ must equal the matrix `secondOrderJacobian` of the
       record (`sp.sympify` reads its braces after they are turned into brackets).
    3. The hidden component $E^{x0}_{x0}$ is at most linear in $k$, the space and time
       components at most quadratic (`sp.degree(expr, K)`).
    4. Reversing the time ($x_4 \to -x_4$) changes the signs of $a_4'$ and $u$ and
       keeps $a_4''$, $v$ and $k$; every component is unchanged under
       $(a_4', u) \to (-a_4', -u)$. So inflation of space with deflation of the block
       and the reverse give the same components: these tensors do not select the sign.
    5. Every term of $E_{(k)}$ has the **weight** $2k$: replacing $H, a_4', u$ by
       $sH, sa_4', su$ and $a_4'', v$ by $s^2 a_4'', s^2 v$ ($k$ unchanged) multiplies
       $E_{(k)}$ by $s^{2k}$. Order $k$ has the dimension $1/\text{length}^{2k}$, so the
       three orders can be added in one field equation only with constants $\alpha_k$
       of different dimensions, for example $\alpha_k = w_k/H^{2k}$.
    """),
    code(r'''
    s = sp.Symbol("s")  # the scaling number of item 5
    alphas = sp.symbols("alpha1 alpha2 alpha3")  # the constants of the field equations
    recorded_J = sp.Matrix(from_text(
        a4_record["generalSource"]["secondOrderJacobian"]["input"].replace("{", "[")
        .replace("}", "]"), {**RECORD_NAMES, "alpha1": alphas[0], "alpha2": alphas[1],
                             "alpha3": alphas[2]}))
    J = sp.zeros(2, 2)  # sum_k alpha_k J_(k)
    structure = {name: True for name in ("constraint", "linear", "k", "even", "weight")}
    for k in (1, 2, 3):
        e = E[k]
        structure["constraint"] &= not e[4, 4].has(A2) and not e[4, 4].has(V)
        structure["linear"] &= all(sp.Poly(e[h, h], A2, V).total_degree() <= 1
                                   for h in (1, 0))
        J += alphas[k - 1] * sp.Matrix([[sp.diff(e[1, 1], A2), sp.diff(e[1, 1], V)],
                                        [sp.diff(e[0, 0], A2), sp.diff(e[0, 0], V)]])
        degrees = [sp.degree(e[h, h], K) for h in (1, 4, 0)]  # x1, x4, x0
        structure["k"] &= degrees[2] <= 1 and max(degrees) <= 2
        structure["even"] &= all(sp.expand(e[h, h].subs({A1: -A1, U: -U}, simultaneous=True)
                                           - e[h, h]) == 0 for h in range(8))
        scaled = {H: s * H, A1: s * A1, U: s * U, A2: s ** 2 * A2, V: s ** 2 * V}
        structure["weight"] &= all(
            sp.expand(e[h, h].subs(scaled, simultaneous=True) - s ** (2 * k) * e[h, h])
            == 0 for h in range(8))
        report(f"degrees of E({k}) in k (x1, x4, x0)", degrees)
    report("coefficient matrix of Einstein's tensor (k = 1)",
           J.subs({alphas[0]: 1, alphas[1]: 0, alphas[2]: 0}).tolist())
    check(structure["constraint"], "the x4 component contains no a4'' and no v",
          record="Revision/field_equations_a4/reports/python-a4-report.json, check "
                 "constraint_first_order")
    check(structure["linear"] and sp.expand(J - recorded_J) == sp.zeros(2, 2),
          "the x1 and x0 components are linear in (a4'', v), with the coefficient matrix "
          "of the record",
          record="Revision/field_equations_a4/reports/python-a4-report.json, check "
                 "second_order_system (a4-equations.json, secondOrderJacobian)")
    check(structure["k"], "the hidden component is at most linear in k, the space and "
          "time components at most quadratic")
    check(structure["even"], "every component is unchanged under (a4', u) -> (-a4', -u), "
          "the reversal of the time")
    check(structure["weight"], "every component of E(k) has the weight 2k (dimension "
          "1/length^(2k))")
    '''),
    md(r"""
    ## 7. The two conservation identities

    Identity (I) of section 4 needs the derivative of the time component along $x_4$.
    By item 1 of section 6 the time component depends on $x_4$ only through $a_4'$, $u$
    and $k$, so by the chain rule

    $$\frac{d}{dx_4} E^{x4}_{x4} = \frac{\partial E^{x4}_{x4}}{\partial a_4'}\, a_4''
      + \frac{\partial E^{x4}_{x4}}{\partial u}\, v
      + \frac{\partial E^{x4}_{x4}}{\partial k}\, k\,(2a_4' - u)$$

    ($k = e^{2a_4}/b_4$ gives $k' = k\,(2a_4' - b_4'/b_4)$). The function `d_dx4` does
    exactly this. The next cell checks identity (I) exactly for $k = 1, 2, 3$ and prints
    both sides for Einstein's tensor; this is the "constraint propagation" of the
    record: the derivative of the constraint is fixed by the other components. Then it
    checks identity (II), $E^{x0}_{x0} = E^{x5}_{x5}$, exactly.
    """),
    code(r'''
    rate = U / 2 - A1  # h4 = u/2 - a4', the rate of the block


    def d_dx4(expr):
        """d/dx4 of a function of a4', u and k: a4' -> a4'', u -> v, k -> k (2 a4' - u)."""
        return sp.expand(sp.diff(expr, A1) * A2 + sp.diff(expr, U) * V
                         + sp.diff(expr, K) * K * (2 * A1 - U))


    def balance(k):
        """The right side of identity (I) for order k."""
        e = E[k]
        return sp.expand(3 * A1 * (e[1, 1] - e[4, 4]) + 4 * rate * (e[0, 0] - e[4, 4]))


    say(f"order 1: d/dx4 E^x4_x4 = {d_dx4(E[1][4, 4])}")
    say(f"         right side of (I) = {balance(1)}")
    check(all(sp.expand(d_dx4(E[k][4, 4]) - balance(k)) == 0 for k in (1, 2, 3)),
          "d/dx4 E^x4_x4 = 3 a4' (E^x1_x1 - E^x4_x4) + 4 h4 (E^x0_x0 - E^x4_x4) with "
          "h4 = u/2 - a4', for k = 1, 2, 3 (identity I)",
          record="Revision/field_equations_a4/reports/python-a4-report.json, check "
                 "bianchi_x4; Revision/gkd_lovelock/results/lovelock-report.json, checks "
                 "k1_divergence_free, k2_divergence_free and k3_divergence_free")
    check(all(sp.expand(E[k][0, 0] - E[k][5, 5]) == 0 for k in (1, 2, 3)),
          "E^x0_x0 = E^x5_x5 for k = 1, 2, 3 (identity II)",
          record="Revision/field_equations_a4/a4-equations.json, generalSource "
                 "hiddenEqualsExtraTimes")
    '''),
    md(r"""
    ## 8. Along the deflating history of the record

    On the histories $a_4 = A H x_4$, $b_4 = b_4(0)\, e^{(4/3) A H x_4}$ we have
    $a_4' = AH$, $a_4'' = 0$, $u = 4AH/3$, $v = 0$, and $k = e^{(2/3) A H x_4}/b_4(0)$.
    Every component then becomes $H^{2k}$ times a polynomial in the slope $A$ and in
    $k$ (the dictionary `FAMILY` puts these values in, with $H = 1$). The next cell
    prints these polynomials and draws them in two ways. Top row: against the slope $A$
    from $-2$ to $2$ at the moment where $k = 1$ ($x_4 = 0$ for $b_4(0) = 1$); the
    curves are symmetric about $A = 0$, because $A \to -A$ is the reversal of the time
    of section 6. Bottom row: along the history of the record ($A = 1$, $b_4(0) = 1$)
    against the time $H x_4$ from $-3$ to $3$, where $k = e^{2 H x_4/3}$ grows; the
    components grow with $k$, the curvature of the shrinking block. `sp.lambdify` turns
    a sympy expression into a numpy function that can be evaluated on an array.
    """),
    code(r'''
    A, t = sp.symbols("A t")  # the slope A and the time t = H x4
    FAMILY = {H: 1, A1: A, A2: 0, U: sp.Rational(4, 3) * A, V: 0}
    ON_FAMILY = {k: {h: sp.expand(E[k][h, h].subs(FAMILY)) for h in (4, 1, 0)}
                 for k in (1, 2, 3)}
    for k in (1, 2, 3):
        say(f"E({k}): x4: {ON_FAMILY[k][4]};  x1: {ON_FAMILY[k][1]};  "
            f"x0: {ON_FAMILY[k][0]}")
    slopes = np.linspace(-2.0, 2.0, 401)
    times = np.linspace(-3.0, 3.0, 601)
    STYLES = ((4, "-", "$E^{x_4}{}_{x_4}$ (time)"), (1, "--", "$E^{x_1}{}_{x_1}$ (space)"),
              (0, ":", "$E^{x_0}{}_{x_0} = E^{x_5}{}_{x_5}$ (block)"))
    fig, axes = plt.subplots(2, 3, figsize=(12.6, 7.6))
    symmetric = True
    for column, k in enumerate((1, 2, 3)):
        for h, style, label in STYLES:
            at_moment = sp.lambdify(A, ON_FAMILY[k][h].subs(K, 1), "numpy")
            values = np.broadcast_to(at_moment(slopes), slopes.shape).astype(float)
            symmetric &= np.allclose(values, values[::-1])
            axes[0, column].plot(slopes, values, style, label=label)
            along = sp.lambdify(t, ON_FAMILY[k][h].subs({A: 1, K: sp.exp(2 * t / 3)}),
                                "numpy")
            axes[1, column].plot(times, np.broadcast_to(along(times), times.shape),
                                 style, label=label)
        axes[0, column].set_xlabel("slope $A = a_4^{\\prime}/H$ (at $k = 1$)")
        axes[1, column].set_xlabel("time $H x_4$ on the history of the record")
        axes[0, column].set_title(f"order k = {k}")
        for row in (0, 1):
            axes[row, column].axhline(0.0, color="0.5", lw=0.8)
            axes[row, column].set_ylabel(f"$E_{{({k})}}$ in units of $H^{{{2 * k}}}$")
            axes[row, column].legend(fontsize=7, loc="best")
    fig.tight_layout()
    save_figure(fig, "components_linear_history",
                "The normalised Lovelock tensors $E_{(1)}$ (Einstein), $E_{(2)}$ and "
                "$E_{(3)}$ of the corrected metric on the histories $a_4 = A H x_4$, "
                "$b_4 = b_4(0) e^{(4/3) A H x_4}$, in units of $H^2$, $H^4$ and $H^6$: "
                "the time component (solid), the space component (dashed) and the "
                "common component of the hidden direction and the extra times "
                "(dotted). Top: against the slope $A$ at the moment where "
                "$k = e^{2 a_4}/b_4 = 1$; every curve is symmetric about $A = 0$, the "
                "reversal of the time. Bottom: along the history of the record, $A = 1$, "
                "against the time $H x_4$, where $k = e^{2 H x_4/3}$ grows; for "
                "$k = 1$ the curves are $A^2/3 + 6k$, $6k - 13A^2/9$ and $3k - 11A^2/3$.")
    check(symmetric, "on the histories every curve is symmetric under A -> -A")
    '''),
    md(r"""
    The next cell draws the three Lovelock scalars $L_{(k)}$ (read from the record; the
    function `from_mathematica` turns the record's text into a sympy expression in the
    six variables) along the history of the record, in units of $H^{2k}$, against the
    time $H x_4$ from $-3$ to $4$, and computes where they are zero. On the history
    $L_{(k)}$ is a polynomial in $k$; `sp.Poly(...).nroots()` computes all its roots
    numerically (15 digits), the cell keeps the real positive ones, and each such root
    $k_0$ is the moment $H x_4 = \frac32 \ln k_0$. $L_{(1)} = 2R = 112/9 - 24k$ is zero
    exactly at $k = 14/27$, before $x_4 = 0$.
    """),
    code(r'''
    def from_mathematica(text):
        """A formula of lovelock-tensors.json (Mathematica text) in the six variables."""
        text = re.sub(r"Derivative\[(\d)\]\[a4\]\[x4\]", r"A\1", text)  # a4' -> A1
        text = text.replace("Derivative[1][b4][x4]", "(U*B0)")  # b4' = u b4
        text = text.replace("Derivative[2][b4][x4]", "((V + U**2)*B0)")  # b4''
        text = text.replace("b4[x4]", "B0")  # b4
        text = re.sub(r"E\^\((-?\d+)\*a4\[x4\]\)", r"(K*B0)**(\1/2)", text)  # e^(n a4)
        return sp.expand(from_text(text, {"H": H, "A1": A1, "A2": A2, "U": U, "V": V,
                                          "K": K, "B0": B0}))


    L = {k: from_mathematica(tensors[f"L{k}"]) for k in (1, 2, 3)}
    L_HISTORY = {k: sp.expand(L[k].subs(FAMILY).subs(A, 1)) for k in (1, 2, 3)}
    scalar_times = np.linspace(-3.0, 4.0, 701)  # H x4 from -3 to 4
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.8))
    zeros = {}
    for ax, k in zip(axes, (1, 2, 3)):
        roots = sp.Poly(L_HISTORY[k], K).nroots(n=15)  # every root, numerically
        zeros[k] = [float(r) for r in roots if r.is_real and r > 0]
        moments = [1.5 * np.log(r) for r in zeros[k]]  # H x4 = (3/2) ln k0
        say(f"L({k}) on the history = {sp.factor(L_HISTORY[k])}")
        report(f"positive zeros of L({k}) on the history: k, H x4",
               ", ".join(f"{r:.6f}, {m:.4f}" for r, m in zip(zeros[k], moments))
               or "none")
        along = sp.lambdify(t, L_HISTORY[k].subs(K, sp.exp(2 * t / 3)), "numpy")
        ax.plot(scalar_times, along(scalar_times), color="tab:green")
        for m in moments:
            ax.plot([m], [0.0], "o", color="black", markersize=4)
        ax.axhline(0.0, color="0.5", lw=0.8)
        ax.axvline(0.0, color="0.5", lw=0.8)
        ax.set_xlabel("time $H x_4$ on the history of the record")
        ax.set_ylabel(f"$L_{{({k})}}$ in units of $H^{{{2 * k}}}$")
        ax.set_title(f"Lovelock scalar of order {k}")
    fig.tight_layout()
    save_figure(fig, "lovelock_scalars",
                "The Lovelock scalars $L_{(1)} = 2R$, $L_{(2)}$ and $L_{(3)}$ of the "
                "corrected metric along the history of the record, $a_4 = H x_4$, "
                "$b_4 = e^{(4/3) H x_4}$, in units of $H^2$, $H^4$ and $H^6$, against "
                "the time $H x_4$; on this history each is a polynomial in "
                "$k = e^{2 H x_4/3}$: $L_{(1)} = 112/9 - 24k$ vanishes at $k = 14/27$, "
                "$L_{(2)}$ at one positive $k$, and $L_{(3)}$, a quadratic in $k$ with "
                "positive coefficients, never; the black dots mark the zeros. At "
                "$x_4 = 0$ the three values are $-104/9$, $-21728/27$ and $93184/9$.")
    check(len(zeros[1]) == 1 and abs(zeros[1][0] - 14 / 27) < 1e-12
          and len(zeros[2]) == 1 and zeros[3] == []
          and [L_HISTORY[k].subs(K, 1) for k in (1, 2, 3)]
          == [sp.Rational(-104, 9), sp.Rational(-21728, 27), sp.Rational(93184, 9)],
          "on the history L(1) vanishes at k = 14/27, L(2) at one positive k, L(3) "
          "never; at x4 = 0 the scalars are -104/9, -21728/27, 93184/9")
    '''),
    md(r"""
    **The source that this history needs.** The field equations
    $\sum_k \alpha_k E_{(k)}{}^\mu{}_\nu + \Lambda \delta^\mu_\nu = \kappa T^\mu{}_\nu$
    with $T = \mathrm{diag}(p_0, p_3, p_3, p_3, -\rho, p_t, p_t, p_t)$ (in the order
    $x_0, \dots, x_7$) say, component by component, $-\kappa\rho - \Lambda =
    \sum_k \alpha_k E^{x4}_{x4}$, $\kappa p_3 - \Lambda = \sum_k \alpha_k E^{x1}_{x1}$
    and $\kappa p_0 - \Lambda = \kappa p_t - \Lambda = \sum_k \alpha_k E^{x0}_{x0}$. On
    the history of the record these are polynomials in $k$. The next cell computes them
    for Einstein gravity ($\alpha_1 = 1$, $\alpha_2 = \alpha_3 = 0$) and for the
    author's weights $\alpha_k = w_k/H^{2k}$ with $w = (1, 1/32, 1/1152)$, and compares
    them with the record `a4-equations.json` (entry `exponentialHistory`,
    `authorWeights`). The source grows with $k$, and $p_0 = p_t$ is at most linear in
    $k$ (item 3 of section 6).
    """),
    code(r'''
    weights = {"Einstein": (1, 0, 0),
               "author": (1, sp.Rational(1, 32), sp.Rational(1, 1152))}
    record_sources = a4_record["exponentialHistory"]["authorWeights"]
    keys = {"Einstein": "einsteinHistorySource_kappaT_minus_Lam",
            "author": "historySource_kappaT_minus_Lam"}
    agree = {}
    for name, w in weights.items():
        source = {h: sp.expand(sum(w[k - 1] * ON_FAMILY[k][h] for k in (1, 2, 3))
                               .subs(A, 1)) for h in (4, 1, 0)}
        say(f"{name}: -kappa rho - Lambda = {source[4]};  kappa p3 - Lambda = "
            f"{source[1]};  kappa p0 - Lambda = kappa pt - Lambda = {source[0]}")
        recorded = record_sources[keys[name]]
        agree[name] = all(
            sp.expand(from_text(recorded[entry]["input"]).subs(H, 1) - source[h]) == 0
            for entry, h in (("minus_rho", 4), ("p3", 1), ("p0", 0), ("pt", 0)))
    check(agree["Einstein"], "Einstein gravity: the source of the history equals the "
          "record",
          record="Revision/field_equations_a4/a4-equations.json, exponentialHistory, "
                 "authorWeights, einsteinHistorySource_kappaT_minus_Lam")
    check(agree["author"], "the author's weights: the source of the history equals the "
          "record",
          record="Revision/field_equations_a4/reports/python-a4-report.json, check "
                 "author_weights_history_source")
    '''),
    md(r"""
    ## 9. An illustrative test history in which the deflation speeds up

    On the history of the record $a_4'' = v = 0$, so it cannot show where the second
    derivatives enter. The next cells therefore use a test history in which the block
    deflates at ALL times, slowly in the far past and three times faster in the far
    future, with the same ratio $b_4 = e^{(4/3) a_4}$ as the record:

    $$a_4(x_4) = H x_4 + \tfrac12 \ln\cosh(H x_4),\qquad
      a_4' = H\big(1 + \tfrac12 \tanh(H x_4)\big),\qquad
      a_4'' = \tfrac{H^2}{2}\,\mathrm{sech}^2(H x_4),$$

    and then $u = \frac43 a_4'$, $v = \frac43 a_4''$, $k = e^{2a_4}/b_4 =
    e^{(2/3) a_4}$. (The derivative of $\ln\cosh t$ is $\tanh t$, and that of $\tanh t$
    is $\mathrm{sech}^2 t = 1/\cosh^2 t$.) Since $-1 < \tanh < 1$, $a_4'$ lies between
    $H/2$ and $3H/2$; the scale factor $e^{-a_4} b_4^{1/2} = e^{-a_4/3}$ of the block
    always shrinks. $a_4''$ is largest, $H^2/2$, at $x_4 = 0$, where the deflation
    speeds up. This history is an ILLUSTRATION chosen only to show how the components
    depend on the second derivatives; it is not a solution of the field equations, and
    no source is attached to it. The next cell checks the derivatives with sympy and
    draws the history.
    """),
    code(r'''
    history = t + sp.log(sp.cosh(t)) / 2  # a4 with H = 1 (t = H x4)
    b4_history = sp.exp(sp.Rational(4, 3) * history)  # b4 = e^((4/3) a4)
    first = sp.diff(history, t)  # a4'
    second = sp.diff(history, t, 2)  # a4''
    u_history = sp.diff(b4_history, t) / b4_history  # u = b4'/b4
    k_history = sp.exp(2 * history) / b4_history  # k = e^(2 a4)/b4
    check(sp.simplify(first - (1 + sp.tanh(t) / 2)) == 0
          and sp.simplify(second - sp.sech(t) ** 2 / 2) == 0
          and sp.simplify(u_history - sp.Rational(4, 3) * first) == 0
          and sp.simplify(k_history - sp.exp(sp.Rational(2, 3) * history)) == 0,
          "the test history has a4' = 1 + tanh/2 > 0, a4'' = sech^2/2, u = (4/3) a4' and "
          "k = e^((2/3) a4) (H = 1)")
    test_times = np.linspace(-4.0, 4.0, 801)  # H x4 from -4 to 4
    VALUES = {name: sp.lambdify(t, expr, "numpy")(test_times)
              for name, expr in (("a4", history), ("a1", first), ("a2", second))}
    VALUES["u"] = 4 * VALUES["a1"] / 3  # u = (4/3) a4'
    VALUES["v"] = 4 * VALUES["a2"] / 3  # v = (4/3) a4''
    VALUES["k"] = np.exp(2 * VALUES["a4"] / 3)  # k = e^((2/3) a4)
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.0))
    axes[0].semilogy(test_times, np.exp(VALUES["a4"]),
                     label="space, $e^{a_4}$ (inflates)")
    axes[0].semilogy(test_times, np.exp(-VALUES["a4"] / 3), "--",
                     label="block, $e^{-a_4} b_4^{1/2} = e^{-a_4/3}$ (deflates)")
    axes[0].set_xlabel("time $H x_4$")
    axes[0].set_ylabel("scale factor (logarithmic scale)")
    axes[0].set_title("scale factors of the test history")
    axes[0].legend(fontsize=8)
    for name, style, label in (("a1", "-", "$a_4^{\\prime}/H$"), ("u", "-.", "$u/H$"),
                               ("a2", "--", "$a_4^{\\prime\\prime}/H^2$"),
                               ("v", ":", "$v/H^2$")):
        axes[1].plot(test_times, VALUES[name], style, label=label)
    axes[1].set_xlabel("time $H x_4$")
    axes[1].set_ylabel("value")
    axes[1].set_title("its first and second derivatives")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    save_figure(fig, "test_history",
                "The illustrative test history $a_4 = H x_4 + \\frac{1}{2} \\ln\\cosh H "
                "x_4$, $b_4 = e^{(4/3) a_4}$, not a solution of any field equation, "
                "against the time $H x_4$. Left: the scale factor $e^{a_4}$ of "
                "ordinary space (solid) grows and the scale factor "
                "$e^{-a_4} b_4^{1/2} = e^{-a_4/3}$ of the hidden direction and the "
                "extra times (dashed) shrinks at all times, both on a logarithmic axis, "
                "where exponential change is a straight line whose slope steepens "
                "around $x_4 = 0$. Right: $a_4^{\\prime}/H$ rises from 1/2 to 3/2 with "
                "$u = 4a_4^{\\prime}/3$, and $a_4^{\\prime\\prime}/H^2$ and "
                "$v = 4a_4^{\\prime\\prime}/3$ are bumps at $x_4 = 0$.")
    '''),
    md(r"""
    The next cell evaluates the three independent components of $E_{(1)}, E_{(2)},
    E_{(3)}$ along the test history (with $H = 1$, so in units of $H^{2k}$) and draws
    them in the top row; they grow with $k = e^{(2/3) a_4}$. The bottom row shows what
    the second derivatives contribute: each component minus the same component with
    $a_4''$ and $v$ set to 0 (the argument `second_derivatives=False` of the function
    `along_history`). The space and block contributions are bumps where $a_4''$ and $v$
    are not zero, and the time component does not feel them at all (item 1 of section
    6): the check confirms that its contribution is exactly 0 at every time.
    """),
    code(r'''
    def along_history(expr, second_derivatives=True):
        """expr (H = 1) at every time of the test history."""
        function = sp.lambdify((A1, A2, U, V, K), expr.subs(H, 1), "numpy")
        a2 = VALUES["a2"] if second_derivatives else 0 * VALUES["a2"]
        v = VALUES["v"] if second_derivatives else 0 * VALUES["v"]
        values = function(VALUES["a1"], a2, VALUES["u"], v, VALUES["k"])
        return np.broadcast_to(values, test_times.shape).astype(float)


    fig, axes = plt.subplots(2, 3, figsize=(12.6, 7.6))
    curves, parts = {}, {}
    constraint_ok = True
    for column, k in enumerate((1, 2, 3)):
        curves[k] = {h: along_history(E[k][h, h]) for h in (1, 4, 0)}
        parts[k] = {h: curves[k][h] - along_history(E[k][h, h], False)
                    for h in (1, 4, 0)}  # what a4'' and v contribute
        constraint_ok &= not np.any(parts[k][4])  # the time component: exactly 0
        for h, style, label in STYLES:
            axes[0, column].plot(test_times, curves[k][h], style, label=label)
            axes[1, column].plot(test_times, parts[k][h], style, label=label)
        axes[0, column].set_title(f"order k = {k}")
        axes[0, column].set_ylabel(f"$E_{{({k})}}$ in units of $H^{{{2 * k}}}$")
        axes[1, column].set_ylabel("part with $a_4''$ and $v$")
        for row in (0, 1):
            axes[row, column].set_xlabel("time $H x_4$")
            axes[row, column].legend(fontsize=7)
    fig.tight_layout()
    save_figure(fig, "components_test_history",
                "The three independent components of $E_{(1)}$, $E_{(2)}$ and $E_{(3)}$ "
                "along the illustrative test history, in units of $H^2$, $H^4$, $H^6$, "
                "against the time $H x_4$: the time component $E^{x_4}_{\\ x_4}$ "
                "(solid), the space component $E^{x_1}_{\\ x_1}$ (dashed) and the "
                "common component $E^{x_0}_{\\ x_0} = E^{x_5}_{\\ x_5}$ of the hidden "
                "direction and the extra times (dotted). Top: the components, which "
                "grow with $k$. Bottom: the part that the second derivatives "
                "$a_4^{\\prime\\prime}$ and $v = 4a_4^{\\prime\\prime}/3$, a bump "
                "around $x_4 = 0$, contribute; it enters the space and block components "
                "linearly and is exactly 0 for the time component, which depends on "
                "$a_4^{\\prime}$, $u$ and $k$ only.")
    check(constraint_ok, "along the test history the second derivatives contribute "
          "exactly 0 to the time component, for k = 1, 2, 3")
    '''),
    md(r"""
    The last computation checks identity (I) NUMERICALLY along the test history, as an
    independent confirmation of the exact proof of section 7: the derivative of the time
    component, computed as a finite difference of the 801 values (`np.gradient` uses
    $(f(t + \epsilon) - f(t - \epsilon))/(2\epsilon)$ inside the interval, with
    $\epsilon = 0.01$), must agree with $3a_4'(E^{x1}_{x1} - E^{x4}_{x4}) +
    4h_4(E^{x0}_{x0} - E^{x4}_{x4})$, $h_4 = u/2 - a_4'$, up to the error of the finite
    difference, which is of the order of $\epsilon^2$ times the third derivative. The
    cell prints the largest deviation for each order, relative to the largest value of
    the curve, and draws both sides.
    """),
    code(r'''
    step = test_times[1] - test_times[0]  # epsilon = 0.01
    block_rate = VALUES["u"] / 2 - VALUES["a1"]  # h4 = u/2 - a4'
    fig, axes = plt.subplots(1, 3, figsize=(12.0, 3.8))
    worst = {}
    for ax, k in zip(axes, (1, 2, 3)):
        left = np.gradient(curves[k][4], step)  # d/dx4 of the time component
        right = (3 * VALUES["a1"] * (curves[k][1] - curves[k][4])
                 + 4 * block_rate * (curves[k][0] - curves[k][4]))
        inner = slice(1, -1)  # the two end points use a one-sided difference
        worst[k] = float(np.max(np.abs(left[inner] - right[inner]))
                         / np.max(np.abs(right)))
        report(f"order {k}: largest relative deviation of the finite difference",
               f"{worst[k]:.1e}")
        ax.plot(test_times, right, color="tab:blue", lw=3, alpha=0.5,
                label="right side of (I)")
        ax.plot(test_times, left, "k:",
                label="$d E^{x_4}{}_{x_4} / d x_4$ (finite difference)")
        ax.set_xlabel("time $H x_4$")
        ax.set_ylabel(f"units of $H^{{{2 * k + 1}}}$")
        ax.set_title(f"identity (I), order k = {k}")
        ax.legend(fontsize=7)
    fig.tight_layout()
    largest = max(worst.values())  # the largest relative deviation of the three orders
    power = int(np.floor(np.log10(largest)))  # its power of ten
    deviation_text = f"${largest / 10 ** power:.1f} \\times 10^{{{power}}}$"
    save_figure(fig, "conservation_identity",
                "Identity (I), the conservation identity along the time, checked "
                "numerically along the illustrative test history for $k = 1, 2, 3$: the "
                "finite-difference derivative of the time component $E^{x_4}_{\\ x_4}$ "
                "(dotted black) lies on the right side $3 a_4^{\\prime} (E^{x_1}_{\\ x_1} "
                "- E^{x_4}_{\\ x_4}) + 4 h_4 (E^{x_0}_{\\ x_0} - E^{x_4}_{\\ x_4})$ with "
                "$h_4 = u/2 - a_4^{\\prime}$ (thick blue), in units of $H^{2k+1}$, against "
                "the time $H x_4$; the largest relative deviation is about "
                f"{deviation_text}, the size of the finite-difference error.")
    check(all(value < 1e-4 for value in worst.values()),
          "the finite-difference derivative agrees with identity (I) to 1e-4")
    '''),
    md(r"""
    ## 10. The Revision records quoted in this notebook

    This notebook quotes check names and statements from the Revision records. The
    components themselves were compared with `lovelock-tensors.json`,
    `python-lovelock-report.json` and `a4-equations.json` in section 5. The next cell
    reads the records once more and checks the rest of what the text quotes, so that a
    later change of a record cannot pass unnoticed:

    - every check quoted from the report `python-a4-report.json` of the field equations
      and from the Rust report `lovelock-report.json` is present with the verdict PASS;
    - the record `a4-equations.json` states the consequences quoted in section 4: no
      off-diagonal source component (its entry `offDiagonal`), $p_0 = p_t$ (entry
      `hiddenEqualsExtraTimes`), the constraint propagation of section 7 (entry
      `constraint_propagation`) and the energy balance (entry `energyExchange`).

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
        "Revision/field_equations_a4/reports/python-a4-report.json": [
            "json_lovelock_components", "constraint_first_order", "second_order_system",
            "bianchi_x4", "independent_components", "author_weights_history_source"],
        "Revision/gkd_lovelock/results/lovelock-report.json": [
            "k1_divergence_free", "k2_divergence_free", "k3_divergence_free",
            "k1_offdiagonal_vanishes", "k2_offdiagonal_vanishes",
            "k3_offdiagonal_vanishes", "k1_hidden_equals_extra_times",
            "k2_hidden_equals_extra_times", "k3_hidden_equals_extra_times"],
    }
    for path, names in QUOTED.items():
        found = verdicts(path)
        missing = [name for name in names if found.get(name) != "PASS"]
        say(f"{path.split('/')[-1]}: {len(names)} quoted checks; not there or not "
            f"PASS: {missing if missing else 'none'}")
        check(not missing,
              f"the {len(names)} checks quoted from {path.split('/')[-1]} are there and "
              "PASS", record=f"{path}, checks " + ", ".join(names))
    general = a4_record["generalSource"]  # a4-equations.json, read in section 5
    stated = ("p0 = p_t" in general["hiddenEqualsExtraTimes"]
              and "for every mu != nu" in general["offDiagonal"]
              and "3 ad1 (E^x1_x1 - E^x4_x4) + 4 hh (E^x0_x0 - E^x4_x4)"
              in general["constraint_propagation"]
              and general["energyExchange"]["input"]
              == "-d4rho - 3*ad1*(p3 + rho) - 4*(p0 + rho)*(-ad1 + uu/2) == 0")
    check(stated, "a4-equations.json states no off-diagonal source, p0 = p_t, the "
                  "constraint propagation and the energy balance, as quoted",
          record="Revision/field_equations_a4/a4-equations.json, generalSource: "
                 "offDiagonal, hiddenEqualsExtraTimes, constraint_propagation, "
                 "energyExchange")
    '''),
    md(r"""
    The last cell checks that all five figure files exist and prints the number of
    checks that passed.
    """),
    code(r'''
    figure_files = [f"11c_{k}_{name}.png" for k, name in enumerate(
        ["components_linear_history", "lovelock_scalars", "test_history",
         "components_test_history", "conservation_identity"], 1)]
    check(all(output_file(f"{FIGURE_FOLDER}/{name}").is_file() for name in figure_files),
          "all five figure files of the notebook exist")
    all_checks_passed()
    '''),
    md(r"""
    ## 11. What this notebook showed

    - The normalised Lovelock tensors of the corrected metric are diagonal polynomials in
      $H$, $a_4'$, $a_4''$, $u = b_4'/b_4$, $v = u'$ and $k = e^{2a_4}/b_4$, for example
      Einstein's tensor $E^{x1}_{x1} = 2a_4'' - 5a_4'^2 + 6a_4'u + 6H^2k - \frac52 u^2 -
      2v$, $E^{x4}_{x4} = 3a_4'^2 + 6H^2k - \frac32 u^2$ and $E^{x0}_{x0} = E^{x5}_{x5} =
      -3a_4'^2 + \frac32 a_4'u + 3H^2k - \frac32 u^2 - \frac32 v$; all three orders equal
      the components recorded for the field equations and by the independent sympy
      verification.
    - Their structure (PROVED): space components equal; hidden component equal to the
      extra-time components; the time component free of second derivatives (a
      constraint); the other components linear in $a_4''$ and $v$ with the recorded
      coefficient matrix; the hidden component at most linear in $k$; everything
      unchanged under the reversal of the time, so the deflation of the block is not
      selected by these tensors; order $k$ has the dimension $1/\text{length}^{2k}$.
    - The two conservation identities, $\frac{d}{dx_4}E^{x4}_{x4} = 3a_4'(E^{x1}_{x1} -
      E^{x4}_{x4}) + 4h_4(E^{x0}_{x0} - E^{x4}_{x4})$ with $h_4 = u/2 - a_4'$, and
      $E^{x0}_{x0} = E^{x5}_{x5}$, hold exactly for every order; the first was confirmed
      numerically along a test history.
    - On the deflating history of the record every component is a polynomial in the
      slope and in $k = e^{2Hx_4/3}$, even in the slope, and grows with $k$; the source
      that this history needs, for Einstein gravity and for the author's weights, equals
      the record, with $p_0 = p_t$ at most linear in $k$. The test history (an
      illustration only) shows that $a_4''$ and $v$ enter the space and block components
      and not the time component.
    - Every check and statement that the notebook quotes from the Revision records is
      present in them, every quoted check with the verdict PASS.
    """),
]

if __name__ == "__main__":
    raise SystemExit(run_builder(__file__))
