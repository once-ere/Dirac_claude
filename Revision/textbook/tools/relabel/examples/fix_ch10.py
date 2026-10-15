"""Chapter 10 (and builder 10d): code descriptions after the relabel; M_8 -> M_0 (the record's
M0); momenta in the order k0..k3; R_8 -> R_0."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

b = REPO / "Revision/textbook/notebooks/src/10d_curved_good_sector.py"
t = b.read_text(encoding="utf-8")
t = t.replace("# the coefficient of the derivative d/dx8", "# the coefficient of the derivative d/dx0")
b.write_bytes(t.encode("utf-8"))

p = REPO / "Revision/textbook/chapters/10-canonical-quantisation-krein-space.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''Python counts list positions from 0, so the matrix of $x_a$ is at position `a - 1`. The **dictionary comprehension** `{a: ... for a in range(1, 9)}` builds a dictionary in one line: for $a = 1, \dots, 8$ (`range(1, 9)` runs from 1 up to, but not including, 9) it stores the matrix''',
     r'''Python counts list positions from 0, like the author's coordinates, so the matrix of $x_a$ is at position `a`. The **dictionary comprehension** `{a: ... for a in range(8)}` builds a dictionary in one line: for $a = 0, \dots, 7$ (`range(8)` runs from 0 up to, but not including, 8) it stores the matrix'''),
    (r'''the cell prints: `k1**2 + k2**2 + k3**2 - k5**2 - k6**2 - k7**2 + k8**2 + m**2` (sympy writes the power as `**`).''',
     r'''the cell prints: `k0**2 + k1**2 + k2**2 + k3**2 - k5**2 - k6**2 - k7**2 + m**2` (sympy writes the power as `**`).'''),
    (r'''for the masses $\pm2$ with $(k_1, k_2, k_0) = (1, 2, 4)$ the frequency is $5 = \sqrt{4 + 1 + 4 + 16}$;''',
     r'''for the masses $\pm2$ with $(k_0, k_1, k_2) = (4, 1, 2)$ the frequency is $5 = \sqrt{4 + 16 + 1 + 4}$;'''),
    (r'''`itertools.combinations(range(1, 9), 2)` lists every pair $(a, b)$ with $a < b$ from 1 to 8, $\binom82 = 28$ pairs.''',
     r'''`itertools.combinations(range(8), 2)` lists every pair $(a, b)$ with $a < b$ from 0 to 7, $\binom82 = 28$ pairs.'''),
    (r'''The printed line shows `[1, 2, 3, 4, 8]` and `[5, 6, 7]`, as Section 10.2 derived,''',
     r'''The printed line shows `[0, 1, 2, 3, 4]` and `[5, 6, 7]`, as Section 10.2 derived,'''),
]
s = strict_replace(s, pairs, "ch10")
s = s.replace("M_8", "M_0").replace("R_8k", "R_0k").replace("R_8", "R_0")
s = s.replace("$m = 2$, $k = (1, 2, 0, 4)$", "$m = 2$, $k = (k_0, k_1, k_2, k_3) = (4, 1, 2, 0)$")
p.write_bytes(s.encode("utf-8"))
print("ok", s.count("k = (1, 2, 0, 4)"), s.count("(k_1, k_2, k_3, k_0)"))
