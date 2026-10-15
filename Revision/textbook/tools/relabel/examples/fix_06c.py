"""06c: the author's order x0..x7 and the metric with b4(x4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the folder of relabel_common.py
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/06c_mixed_contraction.py"
s = p.read_text(encoding="utf-8")
pairs = [
    # module docstring
    (r'''used), Revision/theory/field-theory.json (omega_nonzero, gammaOmega_total,
hidden_direction_hermiticity) and the field-theory reports.  The consequences of the
mixed contraction are computed by this notebook itself (exact sympy); they are not
Revision results and are used nowhere else.  The author's coordinates x0..x7: x1, x2, x3
3-space (inflating), x4 the time, x5, x6, x7 the three extra times (deflating
exponentially), x0 the hidden direction, z = 6 H x0.
"""''',
     r'''used), Revision/theory/field-theory.json (omega_nonzero, gammaOmega_total,
hidden_direction_hermiticity; the metric at b4 = 1), Revision/theory/field-theory-b4.json
(the metric with b4(x4)) and the field-theory reports.  The consequences of the mixed
contraction are computed by this notebook itself (exact sympy); they are not Revision
results and are used nowhere else.  The author's coordinates x0..x7: x0 the hidden
direction (z = 6 H x0), x1, x2, x3 3-space (inflating), x4 the time, x5, x6, x7 the
three extra times (deflating exponentially).
"""'''),
    # purpose
    (r'''        "author's metric it would give gamma^mu Omega_mu = (3 H/2) gamma^(x0) + "
        "(3 a4'/2) gamma^(x4) instead of 3 H gamma^(x0), break the covariant constancy "''',
     r'''        "author's metric it would give gamma^mu Omega_mu = (3 H/2) gamma^(x0) + "
        "(3/2)(a4' - b4'/(2 b4)) gamma^(x4) instead of 3 H gamma^(x0) + (3/4)(b4'/b4) "
        "gamma^(x4), break the covariant constancy "'''),
    (r'''        ["Revision/theory/field-theory.json",
         "the exact formulas omega_nonzero, gammaOmega_total and "
         "hidden_direction_hermiticity (reproduced)"],''',
     r'''        ["Revision/theory/field-theory.json",
         "the exact formulas omega_nonzero, gammaOmega_total and "
         "hidden_direction_hermiticity at b4 = 1 (reproduced)"],
        ["Revision/theory/field-theory-b4.json",
         "the exact formulas omega_nonzero and gammaOmega_total with b4 (reproduced)"],'''),
    (r'''        ["Revision/theory/reports/wolfram-field-theory.json",
         "the WolframScript checks of the defining property of the spinor connection "
         "and of the divergence form (reproduced)"],
    ],''',
     r'''        ["Revision/theory/reports/wolfram-field-theory.json",
         "the WolframScript checks of the defining property of the spinor connection "
         "and of the divergence form (reproduced)"],
        ["Revision/theory/reports/wolfram-field-theory-b4.json",
         "the WolframScript checks of the spin connection, the covariant constancy and "
         "the divergence form with b4 (reproduced)"],
    ],'''),
    # section 1
    (r'''    - computes, for the author's metric, what the notebook's contraction would give:
      $\gamma^\mu\Omega^{nb}_\mu = \frac{3H}{2}\gamma^{(x0)} +
      \frac{3a_4'}{2}\gamma^{(x4)}$ instead of the correct $3H\gamma^{(x0)}$;''',
     r'''    - computes, for the author's metric with $a_4(x_4)$ and $b_4(x_4)$, what the
      notebook's contraction would give: $\gamma^\mu\Omega^{nb}_\mu =
      \frac{3H}{2}\gamma^{(x0)} + \frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$
      instead of the correct $3H\gamma^{(x0)} + \frac34\frac{b_4'}{b_4}\gamma^{(x4)}$
      (at $b_4 = 1$: $\frac{3H}{2}\gamma^{(x0)} + \frac{3a_4'}{2}\gamma^{(x4)}$
      instead of $3H\gamma^{(x0)}$);'''),
    (r'''    - shows the physical reason why only the value $3H$ is right: it makes the
      hidden-direction operator antisymmetric for the volume weight $\cos z$, as the
      Revision record proves;''',
     r'''    - shows the physical reason why only the value $3H$ is right: it makes the
      hidden-direction operator antisymmetric for the volume weight
      $\sqrt{|g|} = b_4^{3/2}\cos z$, as the Revision record proves (at $b_4 = 1$);'''),
    # section 3
    (r'''    - **Coordinates** $x0, \dots, x7$ with the author's names: $x1, x2, x3$ 3-space;
      $x4$ the time; $x5, x6, x7$ the three **extra times**; $x0$ the **hidden
      direction**; $z = 6Hx_0$. In Python lists they have the positions 0 to 7.''',
     r'''    - **Coordinates** $x0, \dots, x7$ with the author's names: $x0$ the **hidden
      direction**; $x1, x2, x3$ 3-space; $x4$ the time; $x5, x6, x7$ the three
      **extra times**; $z = 6Hx_0$. In Python lists they have the positions 0 to 7 in
      the same order.'''),
    # section 4 status
    (r'''    and describe the contraction that the Revision record does NOT use. The correct
    values ($\Omega_\mu$, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)}$, $D_\mu\gamma^\nu = 0$,
    the antisymmetry of the hidden-direction operator) reproduce the Revision record.''',
     r'''    and describe the contraction that the Revision record does NOT use. The correct
    values ($\Omega_\mu$, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)} +
    \frac34(b_4'/b_4)\gamma^{(x4)}$, $D_\mu\gamma^\nu = 0$, the antisymmetry of the
    hidden-direction operator) reproduce the Revision records.'''),
    # cell 5 code
    (r'''    gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(x(a+1))''',
     r'''    gamma = [sp.Matrix(rows) for rows in fixture["gamma"]]  # gamma[a] = gamma^(xa)'''),
    (r'''    THEORY_FILE = "Revision/theory/field-theory.json"
    FORMULAS = {item["key"]: item["wl"] for item in json.loads(
        repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
    REPORT_PY = "Revision/theory/reports/python-field-theory.json"
    REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"''',
     r'''    THEORY_FILE = "Revision/theory/field-theory.json"  # the record at b4 = 1
    THEORY_B4_FILE = "Revision/theory/field-theory-b4.json"  # the record with b4(x4)
    FORMULAS = {item["key"]: item["wl"] for item in json.loads(
        repository_file(THEORY_FILE).read_text(encoding="utf-8"))["formulas"]}
    FORMULAS_B4 = {item["key"]: item["wl"] for item in json.loads(
        repository_file(THEORY_B4_FILE).read_text(encoding="utf-8"))["formulas"]}
    REPORT_PY = "Revision/theory/reports/python-field-theory.json"
    REPORT_WL = "Revision/theory/reports/wolfram-field-theory.json"
    REPORT_WL_B4 = "Revision/theory/reports/wolfram-field-theory-b4.json"'''),
    # section 6 md
    (r'''    $a < b$ by kind (the expected counts are 6 space-space pairs among $x1, x2, x3,
    x0$, 6 time-time pairs among $x4, x5, x6, x7$, and $4 \cdot 4 = 16$ boost pairs),''',
     r'''    $a < b$ by kind (the expected counts are 6 space-space pairs among $x0, x1, x2,
    x3$, 6 time-time pairs among $x4, x5, x6, x7$, and $4 \cdot 4 = 16$ boost pairs),'''),
    # section 8 md
    (r'''    The next cell builds the author's metric with its diagonal vielbein $f =
    (e^{a_4}s\ (\times 3),\ 1,\ e^{-a_4}s\ (\times 3),\ \cot z)$, $s = \sin^{1/6}z$,
    for an arbitrary function $a_4(x_4)$, computes the Christoffel symbols, the MIXED
    spin connection and its lowered form, and compares the 12 nonzero lowered
    components with the record (`omega_nonzero`). Then it builds the correct''',
     r'''    The next cell builds the author's metric with its diagonal vielbein $f =
    (\cot z,\ e^{a_4}s\ (\times 3),\ 1,\ e^{-a_4}b_4^{1/2}s\ (\times 3))$,
    $s = \sin^{1/6}z$, for arbitrary functions $a_4(x_4)$ and $b_4(x_4) > 0$, computes
    the Christoffel symbols, the MIXED spin connection and its lowered form, and
    compares the 12 nonzero lowered components with the records (`omega_nonzero` of
    the record with $b_4$, and at $b_4 = 1$ of the record of $b_4 = 1$; the records
    number the directions from 1 in the order $x0, \dots, x7$). Then it builds the
    correct'''),
    # section 8 code
    (r'''    x = sp.symbols("x0:8", real=True)  # x[0] = x1, ..., x[3] = x4, ..., x[7] = x0
    x4, x0 = x[3], x[7]
    H = sp.Symbol("H", positive=True)  # the author's constant H > 0
    a4 = sp.Function("a4")(x4)  # any function of the time
    a4p = sp.Derivative(a4, x4)  # a4'
    z = 6 * H * x0  # the hidden angle
    s = sp.sin(z) ** sp.Rational(1, 6)
    f = [sp.exp(a4) * s] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * s] * 3 + [sp.cot(z)]
    g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the author's metric
    e = sp.diag(*f)  # the diagonal vielbein
    Gam = christoffel(g, x)
    mixed = mixed_spin_connection(e, Gam, x)  # omega_mu^a_b
    omega = lower_first_index(mixed, ETA)  # omega_mu ab
    # The record lists {mu, a, b, value} with a < b, numbered 1..8, in Wolfram notation.
    text = FORMULAS["omega_nonzero"].replace("Derivative[1][a4][x4]", "a4p")
    text = text.replace("a4[x4]", "a4")
    names = {sp.Symbol("H"): H, sp.Symbol("x0"): x0, sp.Symbol("a4"): a4,
             sp.Symbol("a4p"): a4p}
    omega_record = {(int(m) - 1, int(a) - 1, int(b) - 1): v.subs(names, simultaneous=True)
                    for m, a, b, v in parse_mathematica(text)}
    nonzero = {(mu, a, b): omega[mu][a][b] for mu in range(8) for a, b in pairs
               if omega[mu][a][b] != 0}
    check(set(nonzero) == set(omega_record)
          and all(is_zero(nonzero[k] - omega_record[k]) for k in nonzero),
          "the 12 nonzero lowered components omega_mu ab equal the record",
          record=f"{THEORY_FILE}, formula omega_nonzero")''',
     r'''    x = sp.symbols("x0:8", real=True)  # x[0] = x0, ..., x[4] = x4, ..., x[7] = x7
    x0, x4 = x[0], x[4]  # the hidden direction and the time
    H = sp.Symbol("H", positive=True)  # the author's constant H > 0
    a4 = sp.Function("a4")(x4)  # any function of the time
    b4 = sp.Function("b4", positive=True)(x4)  # any positive function of the time
    a4p, b4p = sp.Derivative(a4, x4), sp.Derivative(b4, x4)  # a4' and b4'
    rate_t = a4p - b4p / (2 * b4)  # the rate of the extra times, a4' - b4'/(2 b4)
    z = 6 * H * x0  # the hidden angle
    s = sp.sin(z) ** sp.Rational(1, 6)
    f = ([sp.cot(z)] + [sp.exp(a4) * s] * 3 + [sp.Integer(1)]
         + [sp.exp(-a4) * sp.sqrt(b4) * s] * 3)  # f_0, ..., f_7
    g = sp.diag(*[ETA[a] * f[a] ** 2 for a in range(8)])  # the author's metric
    e = sp.diag(*f)  # the diagonal vielbein


    def at_b4_1(expr):
        """expr at b4 = 1; doit() evaluates the derivatives of the constant 1 to 0."""
        return sp.sympify(expr).subs({b4: 1}).doit()


    Gam = christoffel(g, x)
    mixed = mixed_spin_connection(e, Gam, x)  # omega_mu^a_b
    omega = lower_first_index(mixed, ETA)  # omega_mu ab
    names = {sp.Symbol("H"): H, sp.Symbol("x0"): x0, sp.Symbol("x4"): x4,
             sp.Symbol("a4"): a4, sp.Symbol("b4"): b4, sp.Symbol("a4p"): a4p,
             sp.Symbol("b4p"): b4p}


    def record_omega(formulas):
        """The record's list {mu, a, b, value} (a < b, numbered from 1, Wolfram
        notation) as a dictionary with Python's numbers 0 to 7."""
        text = formulas["omega_nonzero"]
        for long_form, short_form in (("Derivative[1][a4][x4]", "a4p"),
                                      ("Derivative[1][b4][x4]", "b4p"),
                                      ("a4[x4]", "a4"), ("b4[x4]", "b4")):
            text = text.replace(long_form, short_form)
        return {(int(m) - 1, int(a) - 1, int(b) - 1): v.subs(names, simultaneous=True)
                for m, a, b, v in parse_mathematica(text)}


    omega_record = record_omega(FORMULAS_B4)
    omega_record_1 = record_omega(FORMULAS)
    nonzero = {(mu, a, b): omega[mu][a][b] for mu in range(8) for a, b in pairs
               if omega[mu][a][b] != 0}
    check(set(nonzero) == set(omega_record) == set(omega_record_1)
          and all(is_zero(nonzero[k] - omega_record[k])
                  and is_zero(at_b4_1(nonzero[k]) - omega_record_1[k]) for k in nonzero),
          "the 12 nonzero lowered components omega_mu ab equal the records (with b4, and "
          "at b4 = 1)",
          record=f"{THEORY_B4_FILE} and {THEORY_FILE}, formula omega_nonzero")'''),
    # section 8b md
    (r'''    The previous cell showed that for $\mu = x1$ the boost part (the pair $x1, x4$, with
    the rate $a_4'$) is deleted and the rotation part (the pair $x1, x0$, with $H$) is
    kept, and that for $\mu = x5$ the boost part (the pair $x5, x0$, with $H$) is
    deleted and the time-time part (the pair $x4, x5$, with $a_4'$) has its sign
    reversed. The next cell checks the resulting closed forms

    $$\Omega^{nb}_{x1} = e^{a_4}s\,H\,S^{x1\,x0}, \qquad
    \Omega^{nb}_{x5} = +e^{-a_4}s\,a_4'\,S^{x4\,x5},$$

    compared with the correct $\Omega_{x1} = e^{a_4}s\,(a_4'S^{x1\,x4} +
    HS^{x1\,x0})$ and $\Omega_{x5} = -e^{-a_4}s\,(a_4'S^{x4\,x5} + HS^{x5\,x0})$
    (Notebook 06a), and the same forms for $x2, x3$ and $x6, x7$.
    """),
    code(r''' + "'''" + r'''
    closed_ok = True
    for i in (0, 1, 2):  # the 3-space directions x1, x2, x3
        closed_ok = closed_ok and matrix_is_zero(
            Omega_nb[i] - sp.exp(a4) * s * H * S[i][7])  # pair (xi, x0) kept
        closed_ok = closed_ok and matrix_is_zero(
            Omega[i] - sp.exp(a4) * s * (a4p * S[i][3] + H * S[i][7]))
    for t in (4, 5, 6):  # the extra times x5, x6, x7
        closed_ok = closed_ok and matrix_is_zero(
            Omega_nb[t] - sp.exp(-a4) * s * a4p * S[3][t])  # pair (x4, xt) reversed
        closed_ok = closed_ok and matrix_is_zero(
            Omega[t] + sp.exp(-a4) * s * (a4p * S[3][t] + H * S[t][7]))''',
     r'''    The previous cell showed that for $\mu = x1$ the boost part (the pair $x1, x4$, with
    the rate $a_4'$) is deleted and the rotation part (the pair $x0, x1$, with $H$) is
    kept, and that for $\mu = x5$ the boost part (the pair $x0, x5$, with $H$) is
    deleted and the time-time part (the pair $x4, x5$, with the rate $a_4' -
    b_4'/(2b_4)$) has its sign reversed. The next cell checks the resulting closed
    forms

    $$\Omega^{nb}_{x1} = e^{a_4}s\,H\,S^{x1\,x0}, \qquad
    \Omega^{nb}_{x5} = +e^{-a_4}b_4^{1/2}s\,\big(a_4' - \tfrac{b_4'}{2b_4}\big)\,
    S^{x4\,x5},$$

    compared with the correct $\Omega_{x1} = e^{a_4}s\,(a_4'S^{x1\,x4} +
    HS^{x1\,x0})$ and $\Omega_{x5} = -e^{-a_4}b_4^{1/2}s\,\big((a_4' -
    \frac{b_4'}{2b_4})S^{x4\,x5} + HS^{x5\,x0}\big)$ (Notebook 06a), and the same
    forms for $x2, x3$ and $x6, x7$.
    """),
    code(r''' + "'''" + r'''
    closed_ok = True
    for i in (1, 2, 3):  # the 3-space directions x1, x2, x3
        closed_ok = closed_ok and matrix_is_zero(
            Omega_nb[i] - sp.exp(a4) * s * H * S[i][0])  # pair (x0, xi) kept
        closed_ok = closed_ok and matrix_is_zero(
            Omega[i] - sp.exp(a4) * s * (a4p * S[i][4] + H * S[i][0]))
    f_t = sp.exp(-a4) * sp.sqrt(b4) * s  # the factor of the extra times
    for t in (5, 6, 7):  # the extra times x5, x6, x7
        closed_ok = closed_ok and matrix_is_zero(
            Omega_nb[t] - f_t * rate_t * S[4][t])  # pair (x4, xt) reversed
        closed_ok = closed_ok and matrix_is_zero(
            Omega[t] + f_t * (rate_t * S[4][t] + H * S[t][0]))'''),
    # section 9 md
    (r'''    \frac{1}{f_5}\gamma^{(x5)}\cdot f_5 a_4'\cdot\frac12\gamma^{(x4)}\gamma^{(x5)} =
    -\frac{a_4'}{2}\gamma^{(x4)}(\gamma^{(x5)})^2 = \frac{a_4'}{2}\gamma^{(x4)}$
    (because $\gamma^{(x5)}$ anticommutes with $\gamma^{(x4)}$ and
    $(\gamma^{(x5)})^2 = -1$). Summed:

    $$\gamma^\mu\Omega^{nb}_\mu = \tfrac{3H}{2}\gamma^{(x0)} + \tfrac{3a_4'}{2}
    \gamma^{(x4)} \qquad\text{instead of}\qquad \gamma^\mu\Omega_\mu =
    3H\gamma^{(x0)} .$$

    Half of the hidden term is lost, and the time-direction terms no longer cancel:
    with the wrong contraction the deflation would appear in this term. The cell
    compares the correct total with the record (`gammaOmega_total`).''',
     r'''    \frac{1}{f_5}\gamma^{(x5)}\cdot f_5 r_t\cdot\frac12\gamma^{(x4)}\gamma^{(x5)} =
    -\frac{r_t}{2}\gamma^{(x4)}(\gamma^{(x5)})^2 = \frac{r_t}{2}\gamma^{(x4)}$ with
    $r_t = a_4' - b_4'/(2b_4)$ (because $\gamma^{(x5)}$ anticommutes with
    $\gamma^{(x4)}$ and $(\gamma^{(x5)})^2 = -1$). Summed:

    $$\gamma^\mu\Omega^{nb}_\mu = \tfrac{3H}{2}\gamma^{(x0)} + \tfrac32\big(a_4' -
    \tfrac{b_4'}{2b_4}\big)\gamma^{(x4)} \quad\text{instead of}\quad
    \gamma^\mu\Omega_\mu = 3H\gamma^{(x0)} + \tfrac34\tfrac{b_4'}{b_4}\gamma^{(x4)} .$$

    Half of the hidden term is lost, and the $a_4'$ terms along the time no longer
    cancel: with the wrong contraction the deflation would appear in this term. The
    cell compares the correct total with the records (`gammaOmega_total` with $b_4$,
    and at $b_4 = 1$).'''),
    # section 9 code
    (r'''        alpha = sp.simplify(-(M * gamma[3]).trace() / 16)  # coefficient of gamma^(x4)
        beta = sp.simplify((M * gamma[7]).trace() / 16)  # coefficient of gamma^(x0)
        return alpha, beta, matrix_is_zero(M - alpha * gamma[3] - beta * gamma[7])''',
     r'''        alpha = sp.simplify(-(M * gamma[4]).trace() / 16)  # coefficient of gamma^(x4)
        beta = sp.simplify((M * gamma[0]).trace() / 16)  # coefficient of gamma^(x0)
        return alpha, beta, matrix_is_zero(M - alpha * gamma[4] - beta * gamma[0])'''),
    (r'''    want_nb = [(0, H / 2)] * 3 + [(0, 0)] + [(a4p / 2, 0)] * 3 + [(0, 0)]
    check(all(term[2] for term in correct_terms + notebook_terms)
          and all(is_zero(notebook_terms[mu][0] - want_nb[mu][0])
                  and is_zero(notebook_terms[mu][1] - want_nb[mu][1]) for mu in range(8)),
          "notebook's terms: (H/2) gamma^(x0) for x1, x2, x3; (a4'/2) gamma^(x4) for "
          "x5, x6, x7")
    slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
    slash_nb = sum((gup[mu] * Omega_nb[mu] for mu in range(8)), Z16)
    total_text = FORMULAS["gammaOmega_total"].replace(chr(34), "")  # 3*H*gamma[x0]
    total_record = parse_mathematica(total_text.replace("gamma[x0]", "G8")).subs(
        {sp.Symbol("H"): H, sp.Symbol("G8"): 1})
    check(matrix_is_zero(slash - total_record * gamma[7])
          and record_passed(REPORT_PY, "gamma_mu_Omega_mu_equals_3H_gamma_x0"),
          "correct: gamma^mu Omega_mu = 3 H gamma^(x0)",
          record=f"{THEORY_FILE}, formula gammaOmega_total")
    report("notebook: coefficient of gamma^(x0)", sum(t[1] for t in notebook_terms))
    report("notebook: coefficient of gamma^(x4)", sum(t[0] for t in notebook_terms))
    check(matrix_is_zero(slash_nb - 3 * H / 2 * gamma[7] - 3 * a4p / 2 * gamma[3]),
          "notebook: gamma^mu Omega^nb_mu = (3H/2) gamma^(x0) + (3 a4'/2) gamma^(x4)")''',
     r'''    want_nb = [(0, 0)] + [(0, H / 2)] * 3 + [(0, 0)] + [(rate_t / 2, 0)] * 3
    check(all(term[2] for term in correct_terms + notebook_terms)
          and all(is_zero(notebook_terms[mu][0] - want_nb[mu][0])
                  and is_zero(notebook_terms[mu][1] - want_nb[mu][1]) for mu in range(8)),
          "notebook's terms: (H/2) gamma^(x0) for x1, x2, x3; ((a4' - b4'/(2 b4))/2) "
          "gamma^(x4) for x5, x6, x7")
    slash = sum((gup[mu] * Omega[mu] for mu in range(8)), Z16)
    slash_nb = sum((gup[mu] * Omega_nb[mu] for mu in range(8)), Z16)


    def record_total(formulas):
        """The record's gammaOmega_total as a 16 x 16 matrix."""
        text = formulas["gammaOmega_total"].replace(chr(34), "")  # gamma[x0], gamma[x4]
        for long_form, short_form in (("Derivative[1][b4][x4]", "b4p"),
                                      ("b4[x4]", "b4"), ("gamma[x0]", "G0"),
                                      ("gamma[x4]", "G4")):
            text = text.replace(long_form, short_form)
        total = parse_mathematica(text).subs(names, simultaneous=True)
        G0, G4 = sp.Symbol("G0"), sp.Symbol("G4")
        return total.coeff(G0) * gamma[0] + total.coeff(G4) * gamma[4]


    check(matrix_is_zero(slash - record_total(FORMULAS_B4))
          and matrix_is_zero(at_b4_1(slash) - record_total(FORMULAS))
          and record_passed(REPORT_PY, "gamma_mu_Omega_mu_equals_3H_gamma_x0"),
          "correct: gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4); "
          "3 H gamma^(x0) at b4 = 1",
          record=f"{THEORY_B4_FILE} and {THEORY_FILE}, formula gammaOmega_total")
    report("notebook: coefficient of gamma^(x0)", sum(t[1] for t in notebook_terms))
    report("notebook: coefficient of gamma^(x4)",
           sp.simplify(sum(t[0] for t in notebook_terms)))
    check(matrix_is_zero(slash_nb - 3 * H / 2 * gamma[0] - 3 * rate_t / 2 * gamma[4]),
          "notebook: gamma^mu Omega^nb_mu = (3H/2) gamma^(x0) + (3/2)(a4' - b4'/(2 b4)) "
          "gamma^(x4)")'''),
    # bar chart md
    (r'''    The next cell draws the per-direction table of the previous cell as bar charts:
    for each direction $\mu$ the coefficient of $\gamma^{(x4)}$ in units of $a_4'$
    (left) and of $\gamma^{(x0)}$ in units of $H$ (right), for the correct contraction''',
     r'''    The next cell draws the per-direction table of the previous cell as bar charts, on
    the background $b_4 = 1$: for each direction $\mu$ the coefficient of
    $\gamma^{(x4)}$ in units of $a_4'$ (left) and of $\gamma^{(x0)}$ in units of $H$
    (right), for the correct contraction'''),
    (r'''    alpha_c = [float(sp.simplify(t[0] / a4p)) for t in correct_terms]  # units of a4'
    alpha_n = [float(sp.simplify(t[0] / a4p)) for t in notebook_terms]''',
     r'''    alpha_c = [float(sp.simplify(at_b4_1(t[0]) / a4p)) for t in correct_terms]  # b4 = 1
    alpha_n = [float(sp.simplify(at_b4_1(t[0]) / a4p)) for t in notebook_terms]'''),
    (r'''                "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the author's "
                "metric, each of the form $\\alpha_\\mu\\gamma^{(x4)} + "''',
     r'''                "The eight terms $\\gamma^\\mu\\Omega_\\mu$ (no sum) of the author's "
                "metric at $b_4 = 1$, each of the form $\\alpha_\\mu\\gamma^{(x4)} + "'''),
    # heat maps md and code
    (r'''    The next cell shows the two totals as pictures of 16 x 16 matrices at the sample
    point $H = 1$, $z = \pi/4$, $a_4 = 1/2$, $a_4' = 1/2$ (red positive, blue
    negative, white zero, one colour scale for both). Left: the correct''',
     r'''    The next cell shows the two totals as pictures of 16 x 16 matrices at the sample
    point $H = 1$, $z = \pi/4$, $a_4 = 1/2$, $a_4' = 1/2$, $b_4 = 1$ (red positive, blue
    negative, white zero, one colour scale for both). Left: the correct'''),
    (r'''    def at_sample(expr):
        """The decimal value of expr at H = 1, z = pi/4, a4 = 1/2, a4' = 1/2."""
        expr = sp.sympify(expr).subs(a4p, sp.Rational(1, 2))  # a4' first, then a4''',
     r'''    def at_sample(expr):
        """The decimal value of expr at H = 1, z = pi/4, a4 = 1/2, a4' = 1/2, b4 = 1."""
        expr = at_b4_1(expr).subs(a4p, sp.Rational(1, 2))  # a4' first, then a4'''),
    (r'''                "point $H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1/2$ (rows and columns "
                "are the spinor components; red positive, blue negative, white zero; "''',
     r'''                "point $H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1/2$, $b_4 = 1$ (rows "
                "and columns are the spinor components; red positive, blue negative, "
                "white zero; "'''),
    (r'''                "point $H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1/2$ (pure "
                "numbers; white is zero). Exactly 15 of the 64 pairs are nonzero, all "''',
     r'''                "point $H = 1$, $z = \\pi/4$, $a_4 = 1/2$, $a_4' = 1/2$, $b_4 = 1$ "
                "(pure numbers; white is zero). Exactly 15 of the 64 pairs are nonzero, "
                "all "'''),
    # constancy check record
    (r'''    check(correct_ok and record_passed(REPORT_PY, "covariant_constancy_D_mu_gamma_nu"),
          "correct: D_mu gamma^nu = 0 for all 64 pairs",
          record=f"{REPORT_PY}, check covariant_constancy_D_mu_gamma_nu")''',
     r'''    check(correct_ok and record_passed(REPORT_WL_B4, "gamma_covariantly_constant"),
          "correct: D_mu gamma^nu = 0 for all 64 pairs",
          record=f"{REPORT_WL_B4}, check gamma_covariantly_constant")'''),
    # section 11 md
    (r'''    **The hidden-direction operator.** For fields that depend on $x_0$ only, the
    derivative part of the field equation along $x0$ is the operator $A_c q =
    \tan z\,\partial_{x0}q + c\,q$, where $c$ is the coefficient of $\gamma^{(x0)}$ in
    $\gamma^\mu\Omega_\mu$. The volume weight of the hidden direction is $\sqrt{|g|} =
    \cos z$. Compute, with the product rule and $\partial_{x0}\sin z = 6H\cos z$:''',
     r'''    **The hidden-direction operator.** For fields that depend on $x_0$ only, the
    derivative part of the field equation along $x0$ is the operator $A_c q =
    \tan z\,\partial_{x0}q + c\,q$, where $c$ is the coefficient of $\gamma^{(x0)}$ in
    $\gamma^\mu\Omega_\mu$. The volume weight is $\sqrt{|g|} = b_4^{3/2}\cos z$; along
    the hidden direction the factor $b_4^{3/2}$ is a constant, which multiplies both
    sides below and is left out, so the weight is $\cos z$ (the record's formula is
    written at $b_4 = 1$). Compute, with the product rule and
    $\partial_{x0}\sin z = 6H\cos z$:'''),
    # section 11 code
    (r'''    sqrt_g = sp.cos(z)  # sqrt|det g| of the author's metric''',
     r'''    sqrt_g = b4 ** sp.Rational(3, 2) * sp.cos(z)  # sqrt|det g| of the author's metric'''),
    (r'''          "the divergence form equals the correct contraction, not the notebook's",
          record=f"{REPORT_WL}, check gammaOmega_divergence_form")''',
     r'''          "the divergence form equals the correct contraction, not the notebook's",
          record=f"{REPORT_WL_B4}, check gammaOmega_divergence_form")'''),
    (r'''        """The hidden-direction operator A_c u = tan z du/dx8 + c u."""''',
     r'''        """The hidden-direction operator A_c u = tan z du/dx0 + c u."""'''),
    (r'''          "cos z (p A_c q + (A_c p) q) - d8(sin z p q) = (2c - 6H) cos z p q")
    record_text = FORMULAS["hidden_direction_hermiticity"]
    check(is_zero(leftover.subs(c, 3 * H)) and "Tan[z] d8 + 3 H" in record_text
          and "= d8 (Sin[z] p q)" in record_text,
          "c = 3H: A_c is antisymmetric for the weight cos z up to d8(sin z p q)",''',
     r'''          "cos z (p A_c q + (A_c p) q) - d0(sin z p q) = (2c - 6H) cos z p q")
    record_text = FORMULAS["hidden_direction_hermiticity"]
    check(is_zero(leftover.subs(c, 3 * H)) and "Tan[z] d0 + 3 H" in record_text
          and "= d0 (Sin[z] p q)" in record_text,
          "c = 3H: A_c is antisymmetric for the weight cos z up to d0(sin z p q)",'''),
    # cited
    (r'''        REPORT_WL: ["omega_components", "S_rotates_gamma_with_omega",
                    "gamma_covariantly_constant", "gammaOmega_equals_3H_gamma_x0",
                    "gammaOmega_divergence_form", "good_sector_hermiticity_curved"],
    }''',
     r'''        REPORT_WL: ["omega_components", "S_rotates_gamma_with_omega",
                    "gamma_covariantly_constant", "gammaOmega_equals_3H_gamma_x0",
                    "gammaOmega_divergence_form", "good_sector_hermiticity_curved"],
        REPORT_WL_B4: ["omega_components", "gamma_covariantly_constant",
                       "gammaOmega_total", "gammaOmega_divergence_form"],
    }'''),
    # section 13
    (r'''    - For the author's metric the correct spin connection reproduces the record
      (`omega_nonzero`, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)}$, $D_\mu\gamma^\nu = 0$),
      while the notebook's contraction would give $\gamma^\mu\Omega^{nb}_\mu =
      \frac{3H}{2}\gamma^{(x0)} + \frac{3a_4'}{2}\gamma^{(x4)}$ and would break the''',
     r'''    - For the author's metric the correct spin connection reproduces the records
      (`omega_nonzero`, $\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)} +
      \frac34(b_4'/b_4)\gamma^{(x4)}$, $D_\mu\gamma^\nu = 0$), while the notebook's
      contraction would give $\gamma^\mu\Omega^{nb}_\mu = \frac{3H}{2}\gamma^{(x0)} +
      \frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$ (at $b_4 = 1$:
      $\frac{3H}{2}\gamma^{(x0)} + \frac{3a_4'}{2}\gamma^{(x4)}$) and would break the'''),
    (r'''      hidden-direction operator $\tan z\,\partial_{x0} + 3H$ antisymmetric for the
      volume weight $\cos z$ up to the boundary term $\partial_{x0}(\sin z\,p\,q)$''',
     r'''      hidden-direction operator $\tan z\,\partial_{x0} + 3H$ antisymmetric for the
      volume weight $\cos z$ (times the constant $b_4^{3/2}$ along $x0$) up to the
      boundary term $\partial_{x0}(\sin z\,p\,q)$'''),
]
s = strict_replace(s, pairs, "06c")
p.write_bytes(s.encode("utf-8"))
print("ok")
