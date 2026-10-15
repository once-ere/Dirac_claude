"""08a builder: the author's coordinates x0..x7 (positions and record texts) and the metric with b4."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/08a_growth_rates.py"
s = p.read_text(encoding="utf-8")
pairs = [
    # markdown
    (r'''      $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2$;''',
     r'''      $E^2 = m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2$;'''),
    (r'''      $\kappa = \sqrt{K^2 - m^2 - k_1^2 - k_2^2 - k_3^2 - k_0^2}$, and that $\kappa$ has''',
     r'''      $\kappa = \sqrt{K^2 - m^2 - k_0^2 - k_1^2 - k_2^2 - k_3^2}$, and that $\kappa$ has'''),
    (r'''      = 2\eta^{ab} I_{16}$ (the *Clifford relation*), $\eta = \mathrm{diag}(+1, +1, +1,
      -1, -1, -1, -1, +1)$: a gamma squares to $+1$ for a space-like direction and to''',
     r'''      = 2\eta^{ab} I_{16}$ (the *Clifford relation*), $\eta = \mathrm{diag}(+1, +1, +1,
      +1, -1, -1, -1, -1)$ in the order $x_0, \dots, x_7$: a gamma squares to $+1$ for a
      space-like direction and to'''),
    (r'''    - **Plane wave**: a field of the form $\Psi = u\, e^{i(k_0 x_0 + \dots + k_7 x_0)''',
     r'''    - **Plane wave**: a field of the form $\Psi = u\, e^{i(k_0 x_0 + \dots + k_7 x_7)'''),
    (r'''    $$e^{-a_4}\sin^{-1/6}z\,\gamma^{(i)}\partial_i\Psi + \gamma^{(4)}\partial_4\Psi
    + e^{a_4}\sin^{-1/6}z\,\gamma^{(t)}\partial_t\Psi + \tan z\,\gamma^{(0)}\partial_0\Psi
    + 3H\gamma^{(0)}\Psi = m\Psi$$

    (sums over $i = 1, 2, 3$ and $t = 5, 6, 7$). The term $3H\gamma^{(0)}\Psi$ disappears
    exactly in the variables $\chi = \sin^{1/2}z\,\Psi$ (Revision check
    `rescaling_removes_the_connection_term`). With frozen coefficients the factors
    $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$ become constants and are absorbed into the
    frame momenta $k_a$; in flat 4 + 4 space they are exactly 1. (Freezing them is a
    local MODEL: along the history $a_4(x_4)$ the extra-time factor $e^{a_4}$ keeps
    growing, so the frame momentum of a given wave along an extra time keeps growing
    too; Notebook 08b computes that.)''',
     r'''    $$\tan z\,\gamma^{(0)}\partial_0\Psi + e^{-a_4}\sin^{-1/6}z\,\gamma^{(i)}\partial_i\Psi
    + \gamma^{(4)}\partial_4\Psi + e^{a_4}b_4^{-1/2}\sin^{-1/6}z\,\gamma^{(t)}\partial_t\Psi
    + M\Psi = m\Psi$$

    (sums over $i = 1, 2, 3$ and $t = 5, 6, 7$; $b_4(x_4) > 0$ is the second function
    of the author's metric, and the backgrounds of the record have $b_4 = 1$). $M =
    3H\gamma^{(0)} + \frac34(b_4'/b_4)\gamma^{(4)}$ is the gravitational term (Chapter
    6); it has no derivative, so it does not change the growth of short waves. It
    disappears exactly in the variables $\chi = \sin^{1/2}z\,b_4^{3/4}\Psi$ (Revision
    check `rescaling_removes_the_connection_term`, at $b_4 = 1$). With frozen
    coefficients the factors $e^{-a_4}\sin^{-1/6}z$, $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ and
    $\tan z$ become constants and are absorbed into the frame momenta $k_a$; in flat
    4 + 4 space they are exactly 1. (Freezing them is a local MODEL: along the history
    $a_4(x_4)$ the extra-time factor $e^{a_4}$ keeps growing, so the frame momentum of
    a given wave along an extra time keeps growing too; Notebook 08b computes that on
    the background $b_4 = 1$.)'''),
    (r'''    $E^2 = m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2 - k_5^2 - k_6^2 - k_7^2$: the
    extra-time momenta enter with a MINUS sign, because the extra times are time-like.
    When $k_5^2 + k_6^2 + k_7^2 > m^2 + k_1^2 + k_2^2 + k_3^2 + k_0^2$, $E^2 < 0$, the''',
     r'''    $E^2 = m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2 - k_5^2 - k_6^2 - k_7^2$: the
    extra-time momenta enter with a MINUS sign, because the extra times are time-like.
    When $k_5^2 + k_6^2 + k_7^2 > m^2 + k_0^2 + k_1^2 + k_2^2 + k_3^2$, $E^2 < 0$, the'''),
    (r'''    ordered pairs $(a, b)$ with exact integer arithmetic. In Python lists count from 0,
    so $\gamma^{(x_1)}$ is `GAMMA[0]` and $\gamma^{(x_4)}$ is `GAMMA[3]`. Last, it''',
     r'''    ordered pairs $(a, b)$ with exact integer arithmetic. In Python lists count from 0,
    like the author's coordinates: $\gamma^{(x_0)}$ is `GAMMA[0]` and $\gamma^{(x_4)}$
    is `GAMMA[4]`. Last, it'''),
    # code
    ("    check_record(np.array_equal(GAMMA[3] @ GAMMA[3], -I16),\n",
     "    check_record(np.array_equal(GAMMA[4] @ GAMMA[4], -I16),\n"),
    ('''    k = {a: sp.Symbol(f"k{a}", real=True) for a in (1, 2, 3, 5, 6, 7, 8)}  # momenta''',
     '''    k = {a: sp.Symbol(f"k{a}", real=True) for a in (0, 1, 2, 3, 5, 6, 7)}  # momenta'''),
    ("    g4 = G[3]  # gamma^(x4)\n", "    g4 = G[4]  # gamma^(x4)\n"),
    ('''    for a, k_a in k.items():  # a runs over 1, 2, 3, 5, 6, 7, 8
        momentum_part += k_a * g4 * G[a - 1]  # k_a gamma^(x4) gamma^(xa)''',
     '''    for a, k_a in k.items():  # a runs over 0, 1, 2, 3, 5, 6, 7
        momentum_part += k_a * g4 * G[a]  # k_a gamma^(x4) gamma^(xa)'''),
    ("    E2 = m**2 + k[1]**2 + k[2]**2 + k[3]**2 + k[8]**2 - k[5]**2 - k[6]**2 - k[7]**2\n",
     "    E2 = m**2 + k[0]**2 + k[1]**2 + k[2]**2 + k[3]**2 - k[5]**2 - k[6]**2 - k[7]**2\n"),
    ('''    E2_sympy_text = sp.sstr(E2)  # "k1**2 + k2**2 + ... + m**2"
    E2_wolfram_text = E2_sympy_text.replace("**", "^")  # "k1^2 + k2^2 + ... + m^2"''',
     '''    E2_sympy_text = sp.sstr(E2)  # "k0**2 + k1**2 + ... + m**2"
    E2_wolfram_text = E2_sympy_text.replace("**", "^")  # "k0^2 + k1^2 + ... + m^2"'''),
    ('''                 "h_k^2 = E^2 I16, E^2 = m^2 + k1^2 + k2^2 + k3^2 + k8^2 - k5^2 - k6^2 "''',
     '''                 "h_k^2 = E^2 I16, E^2 = m^2 + k0^2 + k1^2 + k2^2 + k3^2 - k5^2 - k6^2 "'''),
    ("    extra_time_part = -(k[5] * g4 * G[4] + k[6] * g4 * G[5] + k[7] * g4 * G[6])\n",
     "    extra_time_part = -(k[5] * g4 * G[5] + k[6] * g4 * G[6] + k[7] * g4 * G[7])\n"),
    ("    sample = {m: 1, k[5]: 2, k[1]: 0, k[2]: 0, k[3]: 0, k[6]: 0, k[7]: 0, k[8]: 0}\n",
     "    sample = {m: 1, k[5]: 2, k[0]: 0, k[1]: 0, k[2]: 0, k[3]: 0, k[6]: 0, k[7]: 0}\n"),
    ('''        g4n = GAMMA[3]
        result = -1j * mass * g4n.astype(complex)
        for a, k_a in momenta.items():
            result = result - k_a * (g4n @ GAMMA[a - 1])''',
     '''        g4n = GAMMA[4]
        result = -1j * mass * g4n.astype(complex)
        for a, k_a in momenta.items():  # a is the direction: GAMMA[a] is gamma^(xa)
            result = result - k_a * (g4n @ GAMMA[a])'''),
    ('''                 "(0, 0, 0, 2, 0, 0, 0): w^2 = -3, eigenspace dimensions "''',
     '''                 "(0, 0, 0, 0, 2, 0, 0): w^2 = -3, eigenspace dimensions "'''),
    ('''    V_real = eigenspace(mode_matrix(1.0, {1: 2.0, 8: 2.0}), 3.0)''',
     '''    V_real = eigenspace(mode_matrix(1.0, {0: 2.0, 1: 2.0}), 3.0)'''),
    ('''    report("Krein inertia of the eigenspace of E = 3 (m = 1, k1 = k8 = 2)", inertia)''',
     '''    report("Krein inertia of the eigenspace of E = 3 (m = 1, k0 = k1 = 2)", inertia)'''),
    ('''                 "m = 1, k1 = k8 = 2: the eigenspace of E = 3 has Krein inertia (4, 4)",''',
     '''                 "m = 1, k0 = k1 = 2: the eigenspace of E = 3 has Krein inertia (4, 4)",'''),
    ('''    good = mode_matrix(1.3, {1: 0.4, 2: -1.1, 3: 0.7, 8: 2.2})  # no k5, k6, k7''',
     '''    good = mode_matrix(1.3, {0: 2.2, 1: 0.4, 2: -1.1, 3: 0.7})  # no k5, k6, k7'''),
]
s = strict_replace(s, pairs, "08a")
p.write_bytes(s.encode("utf-8"))
print("ok")
