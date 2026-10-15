"""07b builder: the author's coordinates x0..x7 (gammas.json and the records are in that order)
and the metric with b4(x4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/07b_euler_lagrange_metric.py"
s = p.read_text(encoding="utf-8")
pairs = [
    # set-up
    ('''    FORMULAS = "Revision/theory/field-theory.json"
''',
     '''    FORMULAS = "Revision/theory/field-theory.json"  # the formulas at b4 = 1
    FORMULAS_B4 = "Revision/theory/field-theory-b4.json"  # the formulas with b4(x4)
    PYREP_B4 = "Revision/theory/reports/python-field-theory-b4.json"
'''),
    ("    X4, X8 = 3, 7  # list positions of the time x4 and of the hidden direction x0\n",
     "    X0, X4 = 0, 4  # list positions of the hidden direction x0 and of the time x4\n"),
    ("    c_ok = (C == G[7] * G[0] * G[1] * G[2] and C.T == C and C * C == I16\n",
     "    c_ok = (C == G[0] * G[1] * G[2] * G[3] and C.T == C and C * C == I16\n"),
    # section 6: the ring
    (r'''    Every coefficient will be written with the symbols $E = e^{a_4(x_4)}$, $s =
    \sin^{1/6}z$, $c = \cos z$, $A_1 = a_4'$, $A_2 = a_4^{\prime\prime}$, $A_3 =
    a_4^{\prime\prime\prime}$, $H$, $m$ and $\lambda$. Their derivatives follow from
    the chain rule, line by line:

    - $\partial_4 E = e^{a_4}a_4' = E A_1$, $\partial_4 A_1 = A_2$, $\partial_4 A_2 =
      A_3$ (the derivative of $e^{a_4(x_4)}$ is $e^{a_4}$ times the derivative of the
      exponent);''',
     r'''    Every coefficient will be written with the symbols $E = e^{a_4(x_4)}$, $s =
    \sin^{1/6}z$, $c = \cos z$, $A_1 = a_4'$, $A_2 = a_4^{\prime\prime}$, $A_3 =
    a_4^{\prime\prime\prime}$, the second function of the metric $b_4(x_4) > 0$ and its
    derivatives (the symbols `b4`, `b4p`, `b4pp`, `b4ppp`), $H$, $m$ and $\lambda$.
    Their derivatives follow from the chain rule, line by line:

    - $\partial_4 E = e^{a_4}a_4' = E A_1$, $\partial_4 A_1 = A_2$, $\partial_4 A_2 =
      A_3$ (the derivative of $e^{a_4(x_4)}$ is $e^{a_4}$ times the derivative of the
      exponent); $\partial_4 b_4 = b_4'$, $\partial_4 b_4' = b_4''$, $\partial_4 b_4''
      = b_4^{\prime\prime\prime}$;'''),
    ('''    A1, A2, A3 = sp.symbols("A1 A2 A3", real=True)  # 1st, 2nd, 3rd derivative of a4
''',
     '''    A1, A2, A3 = sp.symbols("A1 A2 A3", real=True)  # 1st, 2nd, 3rd derivative of a4
    b4 = sp.Symbol("b4", positive=True)  # the function b4(x4) > 0 of the metric
    b4p, b4pp, b4ppp = sp.symbols("b4p b4pp b4ppp", real=True)  # its 1st to 3rd derivative
    AT_B4_1 = {b4: 1, b4p: 0, b4pp: 0, b4ppp: 0}  # the background b4 = 1
'''),
    ('''        if mu == X4:
            return (sp.diff(expression, E) * E * A1 + sp.diff(expression, A1) * A2
                    + sp.diff(expression, A2) * A3)
        if mu == X8:''',
     '''        if mu == X4:
            return (sp.diff(expression, E) * E * A1 + sp.diff(expression, A1) * A2
                    + sp.diff(expression, A2) * A3 + sp.diff(expression, b4) * b4p
                    + sp.diff(expression, b4p) * b4pp + sp.diff(expression, b4pp) * b4ppp)
        if mu == X0:'''),
    ('''    a4 = sp.Function("a4")(x4)  # the free function of the metric
''',
     '''    a4 = sp.Function("a4")(x4)  # the free function of the metric
    b4f = sp.Function("b4")(x4)  # the second function of the metric
'''),
    ('''             A1: a4.diff(x4), A2: a4.diff(x4, 2), A3: a4.diff(x4, 3)})''',
     '''             A1: a4.diff(x4), A2: a4.diff(x4, 2), A3: a4.diff(x4, 3),
             b4: b4f, b4p: b4f.diff(x4), b4pp: b4f.diff(x4, 2), b4ppp: b4f.diff(x4, 3)})'''),
    ('''        for v in (E, s, c, A1, A2) for mu, variable in ((X4, x4), (X8, x0)))''',
     '''        for v in (E, s, c, A1, A2, b4, b4p, b4pp)
        for mu, variable in ((X4, x4), (X0, x0)))'''),
    # section 7: the metric
    (r'''    The diagonal frame has $f_1 = f_2 = f_3 = Es$, $f_4 = 1$, $f_5 = f_6 = f_7 = s/E$,
    $f_0 = c/s^6 = \cot z$, and the metric is $g_{aa} = \eta_{aa}f_a^2$. The volume
    factor is the product of the $f_a$, worked out line by line:

    $$\sqrt{|g|} = f_1 f_2 f_3 \cdot f_4 \cdot f_5 f_6 f_7 \cdot f_0
    = E^3s^3 \cdot 1 \cdot \frac{s^3}{E^3} \cdot \frac{c}{s^6} = c = \cos z .$$

    The first equality: for a diagonal metric $|\det g|$ is the product of the
    $f_a^2$; the second inserts the $f_a$; the third cancels $E^3$ against $E^{-3}$
    and $s^6$ against $s^{-6}$. The inflation $E^3$ of 3-space and the deflation
    $E^{-3}$ of the extra times compensate: the 7-volume does not depend on time. The
    next cell checks that the frame gives the author's metric entry by entry and that
    $\sqrt{|g|} = \cos z$.''',
     r'''    The diagonal frame has $f_0 = c/s^6 = \cot z$, $f_1 = f_2 = f_3 = Es$, $f_4 = 1$,
    $f_5 = f_6 = f_7 = s\sqrt{b_4}/E$, and the metric is $g_{aa} = \eta_{aa}f_a^2$. The
    volume factor is the product of the $f_a$, worked out line by line:

    $$\sqrt{|g|} = f_0 \cdot f_1 f_2 f_3 \cdot f_4 \cdot f_5 f_6 f_7
    = \frac{c}{s^6} \cdot E^3s^3 \cdot 1 \cdot \frac{s^3b_4^{3/2}}{E^3} = b_4^{3/2}c
    = b_4^{3/2}\cos z .$$

    The first equality: for a diagonal metric $|\det g|$ is the product of the
    $f_a^2$; the second inserts the $f_a$; the third cancels $E^3$ against $E^{-3}$
    and $s^6$ against $s^{-6}$. The inflation $E^3$ of 3-space and the deflation
    $E^{-3}$ of the extra times compensate: the 7-volume depends on the time only
    through $b_4^{3/2}$, and not at all on the backgrounds $b_4 = 1$. The next cell
    checks that the frame gives the author's metric entry by entry and that
    $\sqrt{|g|} = b_4^{3/2}\cos z$, which is $\cos z$ at $b_4 = 1$.'''),
    ("    f = [E * s] * 3 + [sp.Integer(1)] + [s / E] * 3 + [c / s**6]  # the frame factors\n",
     "    f = [c / s**6] + [E * s] * 3 + [sp.Integer(1)] + [s * sp.sqrt(b4) / E] * 3  # frame\n"),
    ('''    author = ([sp.exp(2 * a4) * third] * 3 + [-1] + [-sp.exp(-2 * a4) * third] * 3
              + [sp.cot(z) ** 2])  # the author's metric, typed from Revision/SPEC.md
    check(all(sp.simplify(to_physical(g[a]) - author[a]) == 0 for a in range(8)),
          "the diagonal frame reproduces the author's metric entry by entry",
          record=reproduces(PYREP, "metric_from_vielbein_equals_SPEC"))
    say(f"sqrt|g| = {sqrt_g} (ring) = {to_physical(sqrt_g)}")
    check(sqrt_g == c, "sqrt|g| = cos z, independent of x4",
          record=reproduces(WLREP, "sqrt_det_g_is_cos_z"))''',
     '''    author = ([sp.cot(z) ** 2] + [sp.exp(2 * a4) * third] * 3 + [-1]
              + [-sp.exp(-2 * a4) * b4f * third] * 3)  # the author's metric with b4
    check(all(sp.simplify(to_physical(g[a]) - author[a]) == 0 for a in range(8)),
          "the diagonal frame reproduces the author's metric with b4 entry by entry",
          record=reproduces(PYREP, "metric_from_vielbein_equals_SPEC") + " (at b4 = 1)")
    say(f"sqrt|g| = {sqrt_g} (ring) = {to_physical(sqrt_g)}")
    check(sqrt_g == b4 ** sp.Rational(3, 2) * c and sqrt_g.subs(AT_B4_1) == c,
          "sqrt|g| = b4^(3/2) cos z; cos z, independent of x4, at b4 = 1",
          record=reproduces(WLREP, "sqrt_det_g_is_cos_z") + " (at b4 = 1)")'''),
    # the translator
    (r'''    rewrites such a text into sympy syntax (square brackets to round ones, `^` to
    `**`, `Sin` to `sin`, `a4[x4]` to a symbol), lets sympy read it, and then puts it
    into the ring: $a_4 \to \ln E$ (so $e^{a_4} \to E$),''',
     r'''    rewrites such a text into sympy syntax (square brackets to round ones, `^` to
    `**`, `Sin` to `sin`, `a4[x4]`, `b4[x4]` and their derivatives to symbols), lets
    sympy read it, and then puts it into the ring: $a_4 \to \ln E$ (so $e^{a_4} \to
    E$), $b_4$ and its derivatives to `b4`, `b4p`, `b4pp`,'''),
    (r'''    1/s^6$ and $\csc 2z \to 1/(2s^6c)$ (from $\sin 2z = 2\sin z\cos z$). Then a record
    formula and our own result can be compared with `is_zero`. The cell compares the
    frame and the volume factor with the record.''',
     r'''    1/s^6$ and $\csc 2z \to 1/(2s^6c)$ (from $\sin 2z = 2\sin z\cos z$). Then a record
    formula and our own result can be compared with `is_zero`. Two formula records are
    read: `record` (the metric at $b_4 = 1$, Revision/theory/field-theory.json) and
    `record_b4` (the metric with $b_4$, Revision/theory/field-theory-b4.json). A result
    of this notebook is compared with the first after `.subs(AT_B4_1)`, which puts
    $b_4 = 1$ and $b_4' = b_4'' = b_4^{\prime\prime\prime} = 0$. The cell compares the frame and the
    volume factor with the record of $b_4 = 1$.'''),
    ('''    a4x, A1w = sp.symbols("a4x A1w", real=True)  # a4(x4) and a4'(x4) in the record
''',
     '''    record_b4 = {item["key"]: item["wl"] for item in json.loads(
        repository_file(FORMULAS_B4).read_text(encoding="utf-8"))["formulas"]}
    a4x, A1w = sp.symbols("a4x A1w", real=True)  # a4(x4) and a4'(x4) in the record
    b4x = sp.Symbol("b4x", positive=True)  # b4(x4) in the record
    B1w, B2w = sp.symbols("B1w B2w", real=True)  # b4'(x4) and b4''(x4) in the record
'''),
    ('''        t = text.replace("Derivative[1][a4][x4]", "A1w").replace("a4[x4]", "a4x")''',
     '''        t = text.replace("Derivative[1][a4][x4]", "A1w").replace("a4[x4]", "a4x")
        t = t.replace("Derivative[1][b4][x4]", "B1w").replace("Derivative[2][b4][x4]", "B2w")
        t = t.replace("b4[x4]", "b4x")'''),
    ('''        for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc"):''',
     '''        for name in ("Sin", "Cos", "Tan", "Cot", "Sec", "Csc", "Sqrt"):'''),
    ('''        names = {"E": sp.E, "H": H, "x0": x0, "a4x": a4x, "A1w": A1w}''',
     '''        names = {"E": sp.E, "H": H, "x0": x0, "a4x": a4x, "A1w": A1w, "b4x": b4x,
                 "B1w": B1w, "B2w": B2w}'''),
    ('''        """A record formula in the ring symbols E, s, c, A1."""
        return sp.sympify(expression).subs(a4x, sp.log(E)).subs(A1w, A1).subs(RING)''',
     '''        """A record formula in the ring symbols E, s, c, A1, b4, b4p, b4pp."""
        return (sp.sympify(expression).subs(a4x, sp.log(E)).subs(A1w, A1)
                .subs({b4x: b4, B1w: b4p, B2w: b4pp}).subs(RING))'''),
    ('''    check(all(is_zero(to_ring(v) - f[a]) for a, v in enumerate(frame_record))
          and is_zero(to_ring(from_wolfram(record["sqrt_det_g"])) - sqrt_g),
          "the frame factors and sqrt|g| equal the formula record",''',
     '''    check(all(is_zero(to_ring(v) - f[a].subs(AT_B4_1)) for a, v in enumerate(frame_record))
          and is_zero(to_ring(from_wolfram(record["sqrt_det_g"])) - sqrt_g.subs(AT_B4_1)),
          "at b4 = 1 the frame factors and sqrt|g| equal the formula record",'''),
    # figure 1
    (r'''    Figure 1 shows what the metric does, for the illustration $H = 1$ and the
    deflating history $a_4 = Ax_4H$ with $A = 1$.''',
     r'''    Figure 1 shows what the metric does, for the illustration $H = 1$, the
    deflating history $a_4 = Ax_4H$ with $A = 1$ and the background $b_4 = 1$.'''),
    ('''                "The author's metric along the deflating history $a_4 = AHx_4$ "
                "with the illustration values $A = 1$, $H = 1$ (a prescribed "
                "history, not a result).''',
     '''                "The author's metric along the deflating history $a_4 = AHx_4$ "
                "with the illustration values $A = 1$, $H = 1$ on the background "
                "$b_4 = 1$ (a prescribed history, not a result).'''),
    # section 8: Christoffel symbols
    (r'''    independent nonzero symbols ($\mu \le \nu$), compares all of them with the formula
    record, and prints four of them in the ring: $\Gamma^{x_1}{}_{x_1x_4} = a_4'$ (3-space
    stretches with time), $\Gamma^{x_5}{}_{x_4x_5} = -a_4'$ (the extra times shrink),
    $\Gamma^{x_1}{}_{x_1x_0} = H\cot z$ and $\Gamma^{x_0}{}_{x_0x_0}$.''',
     r'''    independent nonzero symbols ($\mu \le \nu$), compares all of them with both formula
    records, and prints four of them in the ring: $\Gamma^{x_1}{}_{x_1x_4} = a_4'$
    (3-space stretches with time), $\Gamma^{x_5}{}_{x_4x_5} = -a_4' + b_4'/(2b_4)$ (the
    extra times shrink; $-a_4'$ at $b_4 = 1$), $\Gamma^{x_1}{}_{x_0x_1} = H\cot z$ and
    $\Gamma^{x_0}{}_{x_0x_0}$.'''),
    ("    for l, mu, nu in [(0, 0, 3), (4, 3, 4), (0, 0, 7), (7, 7, 7)]:\n",
     "    for l, mu, nu in [(1, 1, 4), (5, 4, 5), (1, 0, 1), (0, 0, 0)]:\n"),
    ('''    listed = from_wolfram(record["christoffel_nonzero"])
    check(len(listed) == 25 and all(is_zero(to_ring(v) - Gam[l - 1][mu - 1][nu - 1])
                                    for l, mu, nu, v in listed),
          "every Christoffel symbol equals the formula record",
          record=f"{FORMULAS}, formula christoffel_nonzero")''',
     '''    # the records number the directions from 1 in the order x0 .. x7: subtract 1
    listed = from_wolfram(record_b4["christoffel_nonzero"])
    listed_1 = from_wolfram(record["christoffel_nonzero"])
    check(len(listed) == len(listed_1) == 25
          and all(is_zero(to_ring(v) - Gam[l - 1][mu - 1][nu - 1])
                  for l, mu, nu, v in listed)
          and all(is_zero(to_ring(v) - Gam[l - 1][mu - 1][nu - 1].subs(AT_B4_1))
                  for l, mu, nu, v in listed_1),
          "every Christoffel symbol equals the formula record with b4, and at b4 = 1 "
          "the record of b4 = 1",
          record=f"{FORMULAS_B4} and {FORMULAS}, formula christoffel_nonzero")'''),
    # section 9: omega
    ('''    listed = from_wolfram(record["omega_nonzero"])
    check(len(pairs) == 12 and len(listed) == 12 and all(
        is_zero(to_ring(v) - om[mu - 1][a - 1][b - 1]) for mu, a, b, v in listed),
          "exactly 12 nonzero components, equal to the formula record",
          record=reproduces(WLREP, "omega_components"))''',
     '''    listed = from_wolfram(record_b4["omega_nonzero"])
    listed_1 = from_wolfram(record["omega_nonzero"])
    check(len(pairs) == 12 and len(listed) == len(listed_1) == 12
          and all(is_zero(to_ring(v) - om[mu - 1][a - 1][b - 1])
                  for mu, a, b, v in listed)
          and all(is_zero(to_ring(v) - om[mu - 1][a - 1][b - 1].subs(AT_B4_1))
                  for mu, a, b, v in listed_1),
          "exactly 12 nonzero components, equal to the formula record with b4, and at "
          "b4 = 1 to the record of b4 = 1", record=f"{FORMULAS_B4}, formula "
          "omega_nonzero; " + reproduces(WLREP, "omega_components") + " (at b4 = 1)")'''),
    (r'''    Each of the 12 components printed above is either $a_4'$ or $H$ times a factor
    $\pm E^{\pm1}s$ that never vanishes: the connection vanishes only if $a_4' = 0$ AND
    $H = 0$, and $H = 0$ is not a member of the author's family.''',
     r'''    Each of the 12 components printed above is a rate, $a_4'$, $a_4' - b_4'/(2b_4)$
    (the extra times) or $H$, times a factor $\pm Es$ or $\pm s\sqrt{b_4}/E$ that never
    vanishes. Six of them are $H$ times such a factor: the connection never vanishes,
    because $H = 0$ is not a member of the author's family.'''),
    # section 10
    (r'''    where the factors $Es$ cancel and $(\gamma^{(i)})^2 = +1$. For a deflating extra
    time $t$ the frame factor is $s/E$, $\Omega_{x_t} = -\frac{s}{2E}(A_1\gamma^{(x_4)}
    \gamma^{(t)} + H\gamma^{(t)}\gamma^{(x_0)})$, and with $(\gamma^{(t)})^2 = -1$ and
    $\gamma^{(t)}\gamma^{(x_4)}\gamma^{(t)} = +\gamma^{(x_4)}$ one gets
    $\gamma^{x_t}\Omega_{x_t} = \frac12(-A_1\gamma^{(x_4)} + H\gamma^{(x_0)})$.''',
     r'''    where the factors $Es$ cancel and $(\gamma^{(i)})^2 = +1$. For a deflating extra
    time $t$ the frame factor is $f_t = s\sqrt{b_4}/E$ and its rate is $\alpha_t =
    \partial_4 f_t/f_t = -A_1 + b_4'/(2b_4)$; $\Omega_{x_t} = \frac{f_t}{2}(\alpha_t
    \gamma^{(x_4)}\gamma^{(t)} - H\gamma^{(t)}\gamma^{(x_0)})$, and with
    $(\gamma^{(t)})^2 = -1$ and $\gamma^{(t)}\gamma^{(x_4)}\gamma^{(t)} =
    +\gamma^{(x_4)}$ one gets $\gamma^{x_t}\Omega_{x_t} = \frac12(\alpha_t\gamma^{(x_4)}
    + H\gamma^{(x_0)})$, which is $\frac12(-A_1\gamma^{(x_4)} + H\gamma^{(x_0)})$ at
    $b_4 = 1$. The record with $b_4$ stores only the sum; the cell compares the eight
    terms at $b_4 = 1$ with the record of $b_4 = 1$.'''),
    ('''        beta.append(sp.expand((M * G[X8]).trace() / 16))  # coefficient of gamma^(x0)
        rest_zero = rest_zero and all(
            is_zero(v) for v in (M - alpha[-1] * G[X4] - beta[-1] * G[X8]))''',
     '''        beta.append(sp.expand((M * G[X0]).trace() / 16))  # coefficient of gamma^(x0)
        rest_zero = rest_zero and all(
            is_zero(v) for v in (M - alpha[-1] * G[X4] - beta[-1] * G[X0]))'''),
    ('''    check(rest_zero and all(is_zero(to_ring(al) - alpha[mu - 1])
                            and is_zero(to_ring(be) - beta[mu - 1])
                            for mu, al, be in listed),
          "per direction gamma^mu Omega_mu = alpha gamma^(x4) + beta gamma^(x0), equal "
          "to the formula record", record=f"{FORMULAS}, formula gammaOmega_per_direction")
    total = sum((gam[mu] * Om[mu] for mu in range(8)), Z16)
    check(all(is_zero(v) for v in (total - 3 * H * G[X8])),
          "gamma^mu Omega_mu = 3 H gamma^(x0) (summed over mu)",
          record=reproduces(PYREP, "gamma_mu_Omega_mu_equals_3H_gamma_x0"))
    check(sp.expand(sum(alpha[0:3])) == sp.Rational(3, 2) * A1
          and sp.expand(sum(alpha[4:7])) == -sp.Rational(3, 2) * A1
          and sp.expand(sum(beta)) == 3 * H,
          "the x4 terms cancel (+3 A1/2 inflating, -3 A1/2 deflating), the six x0 "
          "terms add to 3 H",
          record=reproduces(PYREP, "time_terms_cancel_hidden_term_survives"))''',
     '''    check(rest_zero and all(is_zero(to_ring(al) - alpha[mu - 1].subs(AT_B4_1))
                            and is_zero(to_ring(be) - beta[mu - 1].subs(AT_B4_1))
                            for mu, al, be in listed),
          "per direction gamma^mu Omega_mu = alpha gamma^(x4) + beta gamma^(x0); at "
          "b4 = 1 equal to the formula record",
          record=f"{FORMULAS}, formula gammaOmega_per_direction")
    total = sum((gam[mu] * Om[mu] for mu in range(8)), Z16)
    GRAV = 3 * H * G[X0] + 3 * b4p / (4 * b4) * G[X4]  # the gravitational term
    check(all(is_zero(v) for v in (total - GRAV))
          and all(is_zero(v) for v in (total.subs(AT_B4_1) - 3 * H * G[X0])),
          "gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4) (summed over "
          "mu); 3 H gamma^(x0) at b4 = 1",
          record=reproduces(PYREP_B4, "gammaOmega_total") + "; "
          + reproduces(PYREP, "gamma_mu_Omega_mu_equals_3H_gamma_x0") + " (at b4 = 1)")
    check(sp.expand(sum(alpha[1:4])) == sp.Rational(3, 2) * A1
          and sp.expand(sum(alpha[5:8]) + sp.Rational(3, 2) * A1
                        - sp.Rational(3, 4) * b4p / b4) == 0
          and sp.expand(sum(alpha[5:8]).subs(AT_B4_1)) == -sp.Rational(3, 2) * A1
          and sp.expand(sum(beta)) == 3 * H,
          "the a4' terms cancel (+3 A1/2 inflating, -3 A1/2 deflating; the extra times "
          "leave (3/4) b4'/b4, zero at b4 = 1), the six x0 terms add to 3 H",
          record=reproduces(PYREP, "time_terms_cancel_hidden_term_survives")
          + " (at b4 = 1)")'''),
    # figure 2
    (r'''    Figure 2 shows the cancellation: the coefficient of $\gamma^{(x_4)}$ (in units of
    $a_4'$) is $+\frac12$ for each inflating direction and $-\frac12$ for each deflating
    extra time,''',
     r'''    Figure 2 shows the cancellation on the background $b_4 = 1$: the coefficient of
    $\gamma^{(x_4)}$ (in units of $a_4'$) is $+\frac12$ for each inflating direction and
    $-\frac12$ for each deflating extra time,'''),
    ('''    a_units = [float(sp.expand(v / A1)) if v != 0 else 0.0 for v in alpha]  # a4' units''',
     '''    a_units = [float(sp.expand(v.subs(AT_B4_1) / A1)) if v != 0 else 0.0
               for v in alpha]  # in units of a4', at b4 = 1'''),
    ('''        ax.bar(positions, values, color=["tab:blue"] * 3 + ["grey"] + ["tab:red"] * 3
               + ["grey"], label="one direction")''',
     '''        ax.bar(positions, values, color=["grey"] + ["tab:blue"] * 3 + ["grey"]
               + ["tab:red"] * 3, label="one direction")'''),
    ('''                "$x_7$; blue: inflating 3-space, red: deflating extra times, grey: "
                "$x_4$ and $x_0$, which give 0). Left: the coefficient of "''',
     '''                "$x_7$; blue: inflating 3-space, red: deflating extra times, grey: "
                "$x_0$ and $x_4$, which give 0), on the background $b_4 = 1$. Left: "
                "the coefficient of "'''),
    ('''                "in units of $H$; all six are $+1/2$ and the sum is 3. Hence "
                "$\\\\gamma^\\\\mu\\\\Omega_\\\\mu = 3H\\\\gamma^{(x_0)}$ for every $a_4$.")''',
     '''                "in units of $H$; all six are $+1/2$ and the sum is 3. Hence "
                "$\\\\gamma^\\\\mu\\\\Omega_\\\\mu = 3H\\\\gamma^{(x_0)}$ for every $a_4$ at "
                "$b_4 = 1$; a changing $b_4$ adds $\\\\frac{3}{4}(b_4'/b_4)"
                "\\\\gamma^{(x_4)}$.")'''),
    # section 11
    (r'''    $$\frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big)
    = \frac{1}{2c}\,\partial_0\Big(c\,\frac{s^6}{c}\Big)\gamma^{(x_0)}
    = \frac{6Hs^6\cdot c/s^6}{2c}\,\gamma^{(x_0)} = 3H\gamma^{(x_0)} .$$

    The first equality: only $\mu = x_0$ contributes, because $\sqrt{|g|}\gamma^{x_4}
    = c\,\gamma^{(x_4)}$ does not depend on $x_4$ and nothing depends on the other six
    coordinates; $\gamma^{x_0} = \gamma^{(x_0)}/f_0 = (s^6/c)\gamma^{(x_0)}$. The
    second: $c\cdot s^6/c = s^6 = \sin z$ and $\partial_0\sin z = 6H\cos z$. The third
    cancels. This equals $\gamma^\mu\Omega_\mu$: the surviving term is the half-density
    (volume and frame divergence) term. The next cell checks both statements.''',
     r'''    $$\frac{1}{2\sqrt{|g|}}\,\partial_\mu\big(\sqrt{|g|}\,\gamma^\mu\big)
    = \frac{1}{2b_4^{3/2}c}\Big[\partial_0\Big(b_4^{3/2}c\,\frac{s^6}{c}\Big)\gamma^{(x_0)}
    + \partial_4\big(b_4^{3/2}c\big)\gamma^{(x_4)}\Big]
    = 3H\gamma^{(x_0)} + \frac34\,\frac{b_4'}{b_4}\,\gamma^{(x_4)} .$$

    The first equality: only $\mu = x_0$ and $\mu = x_4$ contribute, because nothing
    depends on the other six coordinates; $\gamma^{x_0} = \gamma^{(x_0)}/f_0 =
    (s^6/c)\gamma^{(x_0)}$ and $\gamma^{x_4} = \gamma^{(x_4)}$. The second:
    $c\cdot s^6/c = s^6 = \sin z$ and $\partial_0\sin z = 6H\cos z$, so the first term
    is $6Hb_4^{3/2}c/(2b_4^{3/2}c) = 3H$; and $\partial_4 b_4^{3/2} = \frac32
    b_4^{1/2}b_4'$, so the second is $\frac34 b_4'/b_4$ (zero at $b_4 = 1$). This
    equals $\gamma^\mu\Omega_\mu$: the surviving term is the half-density (volume and
    frame divergence) term. The next cell checks both statements.'''),
    ('''    check(all(is_zero(v) for v in (divergence - 3 * H * G[X8])),
          "(1/(2 sqrt|g|)) d_mu (sqrt|g| gamma^mu) = 3 H gamma^(x0)",
          record=reproduces(PYREP, "divergence_of_sqrtg_gamma"))''',
     '''    check(all(is_zero(v) for v in (divergence - GRAV)),
          "(1/(2 sqrt|g|)) d_mu (sqrt|g| gamma^mu) = 3 H gamma^(x0) + (3/4)(b4'/b4) "
          "gamma^(x4)", record=reproduces(PYREP, "divergence_of_sqrtg_gamma")
          + " (at b4 = 1)")'''),
    # section 12
    ("    coordinate positions (empty for the value itself, `(3,)` for $\\partial_4$). An\n",
     "    coordinate positions (empty for the value itself, `(4,)` for $\\partial_4$). An\n"),
    # section 15 step 6
    (r'''    - Step 6. $\sqrt{|g|} = \cos z \ne 0$''',
     r'''    - Step 6. $\sqrt{|g|} = b_4^{3/2}\cos z \ne 0$'''),
    # section 16
    (r'''    Since $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and $\gamma^\mu\Omega_\mu = 3H
    \gamma^{(x_0)}$, the Dirac operator is

    $$\gamma^\mu D_\mu\Psi = \sum_{a=1}^{8}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi +
    3H\gamma^{(x_0)}\Psi,\qquad \frac{1}{f_a} = \frac{1}{Es}\ (x_1, x_2, x_3),\ 1\
    (x_4),\ \frac{E}{s}\ (x_5, x_6, x_7),\ \frac{s^6}{c} = \tan z\ (x_0).$$

    The coefficient of the extra-time derivatives, $e^{a_4}\sin^{-1/6}z$, grows as the
    extra times deflate. The next cell checks this form for both statistics, then
    turns each of our 16 component equations into an ordinary sympy expression in the
    symbols `d<a>_<B>` (for $\partial_a\Psi_B$) and `P<B>` (for $\Psi_B$), and compares
    it with the corresponding equation of the formula record (key
    `field_equation_components`, left-hand sides), term by term. It prints the first
    equation in both forms.''',
     r'''    Since $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and $\gamma^\mu\Omega_\mu = 3H
    \gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$, the Dirac operator is

    $$\gamma^\mu D_\mu\Psi = \sum_{a=0}^{7}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi +
    3H\gamma^{(x_0)}\Psi + \frac34\frac{b_4'}{b_4}\gamma^{(x_4)}\Psi,$$
    $$\frac{1}{f_a} = \frac{s^6}{c} = \tan z\ (x_0),\ \frac{1}{Es}\ (x_1, x_2, x_3),\
    1\ (x_4),\ \frac{E}{s\sqrt{b_4}}\ (x_5, x_6, x_7).$$

    The coefficient of the extra-time derivatives, $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$,
    grows as the extra times deflate. The next cell checks this form for both
    statistics, then turns each of our 16 component equations into an ordinary sympy
    expression in the symbols `d<a>_<B>` (for $\partial_a\Psi_B$, with $a = 0, \dots,
    7$ for $x_0, \dots, x_7$) and `P<B>` (for $\Psi_B$), and compares it with the
    corresponding equation of both formula records (key `field_equation_components`,
    left-hand sides), term by term: as it is with the record with $b_4$, and at
    $b_4 = 1$ with the record of $b_4 = 1$. It prints the first equation in both
    forms.'''),
    ('''        explicit = matvec(G[X8] * 3 * H, data["psi"], odd)  # 3 H gamma^(x0) psi''',
     '''        explicit = matvec(GRAV, data["psi"], odd)  # (3 H gamma^(x0) + ...) psi'''),
    ('''              f"{name}: gamma^mu D_mu Psi = sum_a (1/f_a) gamma^(a) d_a Psi + 3 H "
              "gamma^(x0) Psi", record=reproduces(WLREP, f"Dirac_operator_explicit_{tag}"))''',
     '''              f"{name}: gamma^mu D_mu Psi = sum_a (1/f_a) gamma^(a) d_a Psi + 3 H "
              "gamma^(x0) Psi + (3/4)(b4'/b4) gamma^(x4) Psi",
              record=reproduces(WLREP, f"Dirac_operator_explicit_{tag}") + " (at b4 = 1)")'''),
    ('''            symbol = f"d{d[0] + 1}_{B + 1}" if d else f"P{B + 1}"''',
     '''            symbol = f"d{d[0]}_{B + 1}" if d else f"P{B + 1}"  # d0 .. d7: x0 .. x7'''),
    ('''    theirs = [to_ring(from_wolfram(text.split("==")[0]))
              for text in record["field_equation_components"]]
    say(f"equation 1, this notebook: {ours[0]} = V P1")
    say(f"equation 1, formula record: {theirs[0]} = V P1")
    check(len(theirs) == 16 and all(is_zero(x - y) for x, y in zip(ours, theirs)),
          "all 16 component equations equal the formula record term by term",
          record=f"{FORMULAS}, formula field_equation_components")''',
     '''    theirs = [to_ring(from_wolfram(text.split("==")[0]))
              for text in record_b4["field_equation_components"]]
    theirs_1 = [to_ring(from_wolfram(text.split("==")[0]))
                for text in record["field_equation_components"]]
    say(f"equation 1, this notebook: {ours[0]} = V P1")
    say(f"equation 1, formula record: {theirs[0]} = V P1")
    check(len(theirs) == len(theirs_1) == 16
          and all(is_zero(x - y) for x, y in zip(ours, theirs))
          and all(is_zero(x.subs(AT_B4_1) - y) for x, y in zip(ours, theirs_1)),
          "all 16 component equations equal the formula record with b4 term by term, "
          "and at b4 = 1 the record of b4 = 1",
          record=f"{FORMULAS_B4} and {FORMULAS}, formula field_equation_components")'''),
    # figure 4
    (r'''    the chiral split. The term $3H\gamma^{(x_0)}\Psi$ sits in the squares labelled
    with 8, next to $\tan z\,\partial_0$ of the same component.''',
     r'''    the chiral split. The term $3H\gamma^{(x_0)}\Psi$ sits in the squares labelled
    with 0, next to $\tan z\,\partial_0$ of the same component, and the term
    $\frac34(b_4'/b_4)\gamma^{(x_4)}\Psi$ in the squares labelled with 4.'''),
    ("                    tags[A][B] += str(a + 1)\n",
     "                    tags[A][B] += str(a)  # the digit k names the direction xk\n"),
    ('''                "equation $A$, and the digits name those directions ($1$ to $8$ for "
                "$x_0$ to $x_7$).''',
     '''                "equation $A$, and the digits name those directions ($k$ for "
                "$x_k$).'''),
    ('''                "8. The term $3H\\\\gamma^{(x_0)}\\\\Psi$ appears in the squares that "
                "contain the digit 8.")''',
     '''                "8. The term $3H\\\\gamma^{(x_0)}\\\\Psi$ appears in the squares that "
                "contain the digit 0, the term $\\\\frac{3}{4}(b_4'/b_4)"
                "\\\\gamma^{(x_4)}\\\\Psi$ in those that contain the digit 4.")'''),
    # section 17
    (r'''    $$\sum_a\frac{1}{f_a}\bar\tau_a\partial_a\psi_+ + 3H\bar\tau_{x_0}\psi_+ =
    V\psi_-,\qquad \sum_a\frac{1}{f_a}\tau_a\partial_a\psi_- + 3H\tau_{x_0}\psi_- =
    V\psi_+ .$$''',
     r'''    $$\sum_a\frac{1}{f_a}\bar\tau_a\partial_a\psi_+ + 3H\bar\tau_{x_0}\psi_+ +
    \tfrac34\tfrac{b_4'}{b_4}\bar\tau_{x_4}\psi_+ = V\psi_-,\qquad
    \sum_a\frac{1}{f_a}\tau_a\partial_a\psi_- + 3H\tau_{x_0}\psi_- +
    \tfrac34\tfrac{b_4'}{b_4}\tau_{x_4}\psi_- = V\psi_+ .$$'''),
    (r'''    **The evolution form.** Write the explicit equation of section 16 with the $x_4$
    term separately ($f_4 = 1$) and solve it for $\partial_4\Psi$, line by line:

    $$\gamma^{(x_4)}\partial_4\Psi + \sum_{a\neq4}\frac{1}{f_a}\gamma^{(a)}
    \partial_a\Psi + 3H\gamma^{(x_0)}\Psi = V\Psi$$
    $$\gamma^{(x_4)}\partial_4\Psi = V\Psi - \sum_{a\neq4}\frac{1}{f_a}\gamma^{(a)}
    \partial_a\Psi - 3H\gamma^{(x_0)}\Psi$$
    $$\partial_4\Psi = -\gamma^{(x_4)}\Big[V\Psi - \sum_{a\neq4}\frac{1}{f_a}
    \gamma^{(a)}\partial_a\Psi - 3H\gamma^{(x_0)}\Psi\Big] .$$''',
     r'''    **The evolution form.** Write the explicit equation of section 16 with the $x_4$
    term separately ($f_4 = 1$), write $M = 3H\gamma^{(x_0)} +
    \frac34(b_4'/b_4)\gamma^{(x_4)}$ for the gravitational term, and solve for
    $\partial_4\Psi$, line by line:

    $$\gamma^{(x_4)}\partial_4\Psi + \sum_{a\neq4}\frac{1}{f_a}\gamma^{(a)}
    \partial_a\Psi + M\Psi = V\Psi$$
    $$\gamma^{(x_4)}\partial_4\Psi = V\Psi - \sum_{a\neq4}\frac{1}{f_a}\gamma^{(a)}
    \partial_a\Psi - M\Psi$$
    $$\partial_4\Psi = -\gamma^{(x_4)}\Big[V\Psi - \sum_{a\neq4}\frac{1}{f_a}
    \gamma^{(a)}\partial_a\Psi - M\Psi\Big] .$$

    (The part $\frac34(b_4'/b_4)\gamma^{(x_4)}$ of $M$ gives $-\frac34(b_4'/b_4)\Psi$
    on the right, as in the record's `evolution_form`.)'''),
    ('''        others = matvec(3 * H * G[X8], psi, odd)  # 3 H gamma^(x0) Psi, then the sum''',
     '''        others = matvec(GRAV, psi, odd)  # the gravitational term M Psi, then the sum'''),
    ('''              record=reproduces(WLREP, f"evolution_form_{tag}"))''',
     '''              record=reproduces(WLREP, f"evolution_form_{tag}") + " (at b4 = 1)")'''),
    # section 18
    (r'''    The difference between the field-equation residual computed with the canonical
    spin connection and the one computed with $\Omega_\mu = 0$ is $\gamma^\mu\Omega_\mu
    \Psi = 3H\gamma^{(x_0)}\Psi$. Because $\gamma^{(x_0)}$ is a signed permutation
    matrix with $(\gamma^{(x_0)})^2 = 1$, this vanishes only for $\Psi = 0$ when $H > 0$.''',
     r'''    The difference between the field-equation residual computed with the canonical
    spin connection and the one computed with $\Omega_\mu = 0$ is $\gamma^\mu\Omega_\mu
    \Psi = M\Psi$, $M = 3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$. Because
    $\gamma^{(x_0)}$ and $\gamma^{(x_4)}$ anticommute, $MM = (9H^2 - \frac{9}{16}
    (b_4'/b_4)^2)\,1$: $M\Psi$ vanishes only for $\Psi = 0$, except at times where
    $|b_4'/b_4| = 4H$ (the check `gravity_term_square_b4` of
    Revision/theory/reports/python-field-theory-b4.json). For a constant $b_4$, as on
    the backgrounds $b_4 = 1$, $M = 3H\gamma^{(x_0)}$, a signed permutation matrix with
    $(\gamma^{(x_0)})^2 = 1$, and $M\Psi$ vanishes only for $\Psi = 0$ when $H > 0$.'''),
    ('''        gravity = matvec(3 * H * G[X8], data["psi"], odd)
        ok = all((data["E"][A] - without[A] - gravity[A]).is_zero() for A in range(16))
        nonzero = all(len(gravity[A].terms) == 1 for A in range(16))
        number = "1_dirac16complex" if odd else "2_dirac16complex00"
        check(ok and nonzero, f"{name}: residual(Omega) - residual(Omega = 0) = 3 H "
              "gamma^(x0) Psi, nonzero in all 16 components",
              record=reproduces(WLREP, f"nontriviality_{number}"))''',
     '''        gravity = matvec(GRAV, data["psi"], odd)  # M Psi
        ok = all((data["E"][A] - without[A] - gravity[A]).is_zero() for A in range(16))
        hidden = matvec(3 * H * G[X0], data["psi"], odd)  # M Psi at b4 = 1
        nonzero = all(len(hidden[A].terms) == 1 for A in range(16))
        number = "1_dirac16complex" if odd else "2_dirac16complex00"
        check(ok and nonzero, f"{name}: residual(Omega) - residual(Omega = 0) = M Psi "
              "with M = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4); at b4 = 1 it is "
              "3 H gamma^(x0) Psi, nonzero in all 16 components",
              record=reproduces(WLREP, f"nontriviality_{number}") + " (at b4 = 1); "
              + reproduces(PYREP_B4, "gravity_term_square_b4"))'''),
    # section 19
    (r'''    Look for solutions that depend only on the time $x_4$ and the hidden direction
    $x_0$: $\Psi = \sin^\alpha z\,P(x_4)\,\chi_0$ with a constant column $\chi_0$ and a
    number $\alpha$. With $U = 0$ ($\lambda = 0$) the field equation becomes, line by
    line,''',
     r'''    Look for solutions that depend only on the time $x_4$ and the hidden direction
    $x_0$: $\Psi = \sin^\alpha z\,P(x_4)\,\chi_0$ with a constant column $\chi_0$ and a
    number $\alpha$, for a constant $b_4$ (as on the backgrounds $b_4 = 1$; a changing
    $b_4$ adds the term $\frac34(b_4'/b_4)\gamma^{(x_4)}\Psi$ and changes the family).
    With $U = 0$ ($\lambda = 0$) the field equation becomes, line by line,'''),
    (r'''    derivatives vanish, which is why the result holds for EVERY $a_4$).''',
     r'''    derivatives vanish, which is why the result holds for EVERY $a_4$ and every
    constant $b_4$).'''),
    ("    M = -m * G[X4] + 3 * H * (2 * al + 1) * G[X4] * G[X8]\n",
     "    M = -m * G[X4] + 3 * H * (2 * al + 1) * G[X4] * G[X0]\n"),
    ('''    def d8(v):  # derivative along x0 in the ring (s^(6 alpha) included)''',
     '''    def d0(v):  # derivative along x0 in the ring (s^(6 alpha) included)'''),
    ('''    residual = (G[X4] * Psi.applyfunc(d4) + (s**6 / c) * G[X8] * Psi.applyfunc(d8)
                + 3 * H * G[X8] * Psi - m * Psi)''',
     '''    residual = (G[X4] * Psi.applyfunc(d4) + (s**6 / c) * G[X0] * Psi.applyfunc(d0)
                + 3 * H * G[X0] * Psi - m * Psi)'''),
    ('''    without_term = residual - 3 * H * G[X8] * Psi  # the same without 3 H gamma^(x0)''',
     '''    without_term = residual - 3 * H * G[X0] * Psi  # the same without 3 H gamma^(x0)'''),
    ('''          "equation for every alpha and every a4 (and fails without 3 H gamma^(x0))",''',
     '''          "equation for every alpha, every a4 and constant b4 (and fails without "
          "3 H gamma^(x0))",'''),
    ("    A_matrix = -sp.I * m * G[X4] + 3 * sp.I * H * G[X4] * G[X8]\n",
     "    A_matrix = -sp.I * m * G[X4] + 3 * sp.I * H * G[X4] * G[X0]\n"),
    ("        Mn = -mass * Gn[X4] + 3 * h * (2 * alpha_value + 1) * Gn[X4] @ Gn[X8]\n",
     "        Mn = -mass * Gn[X4] + 3 * h * (2 * alpha_value + 1) * Gn[X4] @ Gn[X0]\n"),
    ("    Mn = -2.0 * Gn[X4] + 3.0 * Gn[X4] @ Gn[X8]  # alpha = 0, m = 2, H = 1\n",
     "    Mn = -2.0 * Gn[X4] + 3.0 * Gn[X4] @ Gn[X0]  # alpha = 0, m = 2, H = 1\n"),
    ("    full = np.array([Gn[X4] @ dp + 3.0 * Gn[X8] @ p - 2.0 * p\n",
     "    full = np.array([Gn[X4] @ dp + 3.0 * Gn[X0] @ p - 2.0 * p\n"),
    ("    wrong_mass = np.array([Gn[X4] @ dp + 3.0 * Gn[X8] @ p + 2.0 * p\n",
     "    wrong_mass = np.array([Gn[X4] @ dp + 3.0 * Gn[X0] @ p + 2.0 * p\n"),
    # section 21
    (r'''    - The diagonal frame $f = (e^{a_4}\sin^{1/6}z\ (\times3),\ 1,\ e^{-a_4}\sin^{1/6}z\
      (\times3),\ \cot z)$ gives exactly the author's metric, with $\sqrt{|g|} = \cos z$
      independent of time: the inflation of 3-space and the deflation of the extra times
      compensate.
    - The metric has 25 independent nonzero Christoffel symbols; the canonical spin
      connection has 12 nonzero components, each $a_4'$ or $H$ times a nonvanishing
      factor.
    - Direction by direction, $\gamma^\mu\Omega_\mu$ has a time part $\pm\frac12a_4'
      \gamma^{(x_4)}$ that cancels between the three inflating and the three deflating
      directions, and a hidden part $\frac12H\gamma^{(x_0)}$ that adds up: $\gamma^\mu
      \Omega_\mu = 3H\gamma^{(x_0)}$ for every $a_4$.''',
     r'''    - The diagonal frame $f = (\cot z,\ e^{a_4}\sin^{1/6}z\ (\times3),\ 1,\
      e^{-a_4}b_4^{1/2}\sin^{1/6}z\ (\times3))$ gives exactly the author's metric with
      $b_4$, with $\sqrt{|g|} = b_4^{3/2}\cos z$: the inflation of 3-space and the
      deflation of the extra times compensate, and at $b_4 = 1$ the volume factor
      $\cos z$ does not depend on time.
    - The metric has 25 independent nonzero Christoffel symbols; the canonical spin
      connection has 12 nonzero components, each a rate ($a_4'$, $a_4' -
      b_4'/(2b_4)$ or $H$) times a nonvanishing factor. Both agree with the formula
      record with $b_4$ and, at $b_4 = 1$, with the record of $b_4 = 1$.
    - Direction by direction, $\gamma^\mu\Omega_\mu$ has a time part $\pm\frac12a_4'
      \gamma^{(x_4)}$ that cancels between the three inflating and the three deflating
      directions (the extra times leave $\frac34(b_4'/b_4)\gamma^{(x_4)}$), and a hidden
      part $\frac12H\gamma^{(x_0)}$ that adds up: $\gamma^\mu\Omega_\mu =
      3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$, which is $3H\gamma^{(x_0)}$
      for every $a_4$ at $b_4 = 1$.'''),
    (r'''      author's metric the 16 component equations contain the frame factors
      $e^{-a_4}\sin^{-1/6}z$, $1$, $e^{a_4}\sin^{-1/6}z$, $\tan z$ and the
      gravitational term $3H\gamma^{(x_0)}\Psi$; they agree term by term with the
      Revision formula record. Each equation couples four components across the chiral
      halves: every gamma is block off-diagonal, and the mass term and the term
      $3H\gamma^{(x_0)}$ both couple the halves $\psi_-$ and $\psi_+$.
    - Solved for the time derivative, $\partial_4\Psi = -\gamma^{(x_4)}[V\Psi -
      \sum_{a\neq4}f_a^{-1}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(x_0)}\Psi]$: the
      slices $x_4 = $ const are non-characteristic, which does not by itself make the
      initial-value problem well posed (the extra-time growth rates are unbounded).
    - The family $\Psi = \sin^\alpha z(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ solves the
      equations exactly for every $a_4$, with constant $S$;''',
     r'''      author's metric the 16 component equations contain the frame factors $\tan z$,
      $e^{-a_4}\sin^{-1/6}z$, $1$, $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ and the
      gravitational term $M\Psi$, $M = 3H\gamma^{(x_0)} +
      \frac34(b_4'/b_4)\gamma^{(x_4)}$; they agree term by term with the Revision
      formula record with $b_4$, and at $b_4 = 1$ with the record of $b_4 = 1$. Each
      equation couples four components across the chiral halves: every gamma is block
      off-diagonal, and the mass term and the gravitational term both couple the halves
      $\psi_-$ and $\psi_+$. $M\Psi$ vanishes only for $\Psi = 0$, except at times
      where $|b_4'/b_4| = 4H$; for a constant $b_4$ never.
    - Solved for the time derivative, $\partial_4\Psi = -\gamma^{(x_4)}[V\Psi -
      \sum_{a\neq4}f_a^{-1}\gamma^{(a)}\partial_a\Psi - M\Psi]$: the slices $x_4 = $
      const are non-characteristic, which does not by itself make the initial-value
      problem well posed (the extra-time growth rates are unbounded).
    - The family $\Psi = \sin^\alpha z(\cosh kx_4 + \sinh(kx_4)/k\,M)\chi_0$ solves the
      equations exactly for every $a_4$ and every constant $b_4$, with constant $S$;'''),
]
s = strict_replace(s, pairs, "07b")
leftover = [l for l in s.splitlines() if "X8" in l or "d8" in l]
assert not leftover, leftover
p.write_bytes(s.encode("utf-8"))
print("ok")
