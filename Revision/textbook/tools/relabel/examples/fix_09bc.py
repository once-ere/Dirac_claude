"""09b and 09c builders: positions of the author's coordinates x0..x7 (gammas.json and the
records are in that order); names with the old label 8 renamed (g8 -> g0, B84 -> B04)."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402


def tokens(s, mapping):
    for old, new in mapping:
        s = re.sub(r"(?<![A-Za-z0-9_])" + re.escape(old) + r"(?![A-Za-z0-9_])", new, s)
    return s


# 09b
p = REPO / "Revision/textbook/notebooks/src/09b_condensates.py"
s = p.read_text(encoding="utf-8")
s = strict_replace(s, [
    ("    g4, g8 = gamma[3], gamma[7]  # gamma^(x4) and gamma^(x0)\n",
     "    g4, g0 = gamma[4], gamma[0]  # gamma^(x4) and gamma^(x0)\n"),
    ("    momentum = {0: 1.0, 1: 2.0, 2: 0.0, 7: 4.0}  # k1, k2, k3, k8 (x5, x6, x7: zero)\n",
     "    momentum = {0: 4.0, 1: 1.0, 2: 2.0, 3: 0.0}  # k0, k1, k2, k3 (x5, x6, x7: zero)\n"),
], "09b")
s = tokens(s, [("g8", "g0"), ("B84", "B04")])
p.write_bytes(s.encode("utf-8"))

# 09c
p = REPO / "Revision/textbook/notebooks/src/09c_condensate_tensor.py"
s = p.read_text(encoding="utf-8")
s = strict_replace(s, [
    ("    g4, g8 = gamma[3], gamma[7]  # gamma^(x4) and gamma^(x0)\n",
     "    g4, g0 = gamma[4], gamma[0]  # gamma^(x4) and gamma^(x0)\n"),
    (r'''    first example of this chapter: `frame_factors(a4, z)` returns the eight vielbein
    factors $f_a$ ($e^{a_4}\sin^{1/6}z$ three times, $1$, $e^{-a_4}\sin^{1/6}z$ three
    times, $\cot z$),''',
     r'''    first example of this chapter: `frame_factors(a4, z)` returns the eight vielbein
    factors $f_a$ in the order $x_0, \dots, x_7$ ($\cot z$, $e^{a_4}\sin^{1/6}z$ three
    times, $1$, $e^{-a_4}\sin^{1/6}z$ three times; the background $b_4 = 1$),'''),
    ('''        return np.array([space] * 3 + [1.0] + [extra] * 3 + [1 / np.tan(z)])''',
     '''        return np.array([1 / np.tan(z)] + [space] * 3 + [1.0] + [extra] * 3)'''),
    ('''        for i in range(3):  # the three 3-space directions x1, x2, x3''',
     '''        for i in range(1, 4):  # the three 3-space directions x1, x2, x3'''),
    ('''        for t in range(4, 7):  # the three extra times x5, x6, x7''',
     '''        for t in range(5, 8):  # the three extra times x5, x6, x7'''),
    ("        dphi[3] = A_value @ column  # the only nonzero derivative\n",
     "        dphi[4] = A_value @ column  # the only nonzero derivative\n"),
    ("    expected_diagonal[3] = -V * S_chi\n",
     "    expected_diagonal[4] = -V * S_chi\n"),
    ('''        if 3 in directions and 7 not in directions:
            directions.add(7)  # add x0
        elif 7 in directions and 3 not in directions:
            directions.add(3)  # add x4
        elif 3 not in directions and 7 not in directions:
            directions.add(3)  # add x4''',
     '''        if 4 in directions and 0 not in directions:
            directions.add(0)  # add x0
        elif 0 in directions and 4 not in directions:
            directions.add(4)  # add x4
        elif 4 not in directions and 0 not in directions:
            directions.add(4)  # add x4'''),
    ('''        nu, mu = [int(digit) - 1 for digit in re.findall(r"x(\\d)", item["component"])]''',
     '''        nu, mu = [int(digit) for digit in re.findall(r"x(\\d)", item["component"])]'''),
    ('''        directions = [int(digit) - 1 for digit in re.findall(r"x(\\d)", term["bilinear"])]''',
     '''        directions = [int(digit) for digit in re.findall(r"x(\\d)", term["bilinear"])]'''),
    ('''    P = [gamma[i] @ gamma[i + 4] for i in range(3)]  # gamma^(x1) gamma^(x5), ...''',
     '''    P = [gamma[i] @ gamma[i + 4] for i in range(1, 4)]  # gamma^(x1) gamma^(x5), ...'''),
    ('''    a4_function = sp.Function("a4")(x[3])
    zs = 6 * Hs * x[7]''',
     '''    a4_function = sp.Function("a4")(x[4])
    zs = 6 * Hs * x[0]'''),
    ('''    g = sp.diag(*([space_entry] * 3 + [-1] + [extra_entry] * 3 + [sp.cot(zs) ** 2]))''',
     '''    g = sp.diag(*([sp.cot(zs) ** 2] + [space_entry] * 3 + [-1] + [extra_entry] * 3))'''),
    ('''    history = sp.Rational(3, 10) * x[3] + sp.Rational(1, 20) * x[3] ** 2  # a4(x4)''',
     '''    history = sp.Rational(3, 10) * x[4] + sp.Rational(1, 20) * x[4] ** 2  # a4(x4)'''),
    ('''                        (x[3], x[7], Hs), value.subs(a4_function, history).doit(), "numpy")''',
     '''                        (x[4], x[0], Hs), value.subs(a4_function, history).doit(), "numpy")'''),
    ("        dphi[3] = d4\n", "        dphi[4] = d4\n"),
    ('''        d8T = (tensor_at(M, k2, x4, x0 + h) - tensor_at(M, k2, x4, x0 - h)) / (2 * h)''',
     '''        d0T = (tensor_at(M, k2, x4, x0 + h) - tensor_at(M, k2, x4, x0 - h)) / (2 * h)'''),
    ('''            result[nu] = (d4T[3, nu] + d8T[7, nu]  # d_mu T^mu_nu (only x4 and x0)''',
     '''            result[nu] = (d4T[4, nu] + d0T[0, nu]  # d_mu T^mu_nu (only x4 and x0)'''),
    ('''    momentum = [0, 1, 2, 4, 5, 6]  # the components nu = x1, x2, x3, x5, x6, x7''',
     '''    momentum = [1, 2, 3, 5, 6, 7]  # the components nu = x1, x2, x3, x5, x6, x7'''),
    ('''          and max(abs(div_control[3]), abs(div_control[7])) < 1e-9,''',
     '''          and max(abs(div_control[4]), abs(div_control[0])) < 1e-9,'''),
], "09c")
s = tokens(s, [("g8", "g0")])
p.write_bytes(s.encode("utf-8"))
for name in ("09b_condensates", "09c_condensate_tensor"):
    text = (REPO / f"Revision/textbook/notebooks/src/{name}.py").read_text(encoding="utf-8")
    print(name, [l.strip() for l in text.splitlines()
                 if re.search(r"gamma\[(3|7)\]|x\[(3|7)\]|\bg8\b|d8T|\[3\]|\[7\]", l)])
