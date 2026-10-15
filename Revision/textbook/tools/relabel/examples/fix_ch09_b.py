"""Chapter 09: the order x0..x7 in the metric of 9.2, and the metric with b4 (9.2, 9.10)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/09-energy-momentum-tensor.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''$$
g = \mathrm{diag}\big(f_1^2,\, f_2^2,\, f_3^2,\, -f_4^2,\, -f_5^2,\, -f_6^2,\, -f_7^2,\, f_0^2\big),
$$

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z, \quad f_0 = \cot z .
$$

So $g_{x_1x_1} = e^{2a_4}\sin^{1/3}z$,''',
     r'''$$
g = \mathrm{diag}\big(f_0^2,\, f_1^2,\, f_2^2,\, f_3^2,\, -f_4^2,\, -f_5^2,\, -f_6^2,\, -f_7^2\big),
$$

$$
f_0 = \cot z, \quad f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z .
$$

These are the factors on the backgrounds $b_4 = 1$ of the Revision record. The author's metric of 2026-10-14 has a second function $b_4(x_4) > 0$, and then $f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}\sin^{1/6}z$ and $\sqrt{|g|} = b_4^{3/2}\cos z$ (Chapters 3, 6 and 7). This chapter works at $b_4 = 1$, as the record's energy-momentum checks do (`Revision/theory/reports/wolfram-field-theory.json`); where the record has the tensor or its identities for a general $b_4$, the section says so (Sections 9.10 and 9.11). So $g_{x_1x_1} = e^{2a_4}\sin^{1/3}z$,'''),
    (r'''Here the volume factor $\sqrt{|g|} = \cos z$ does not change with $x_4$, so no term with $\rho$ itself appears; only the difference of the two pressures drives the energy.''',
     r'''Here the volume factor $\sqrt{|g|} = \cos z$ does not change with $x_4$, so no term with $\rho$ itself appears; only the difference of the two pressures drives the energy.

**With a changing $b_4$.** For the metric with $b_4(x_4)$ the volume factor is $b_4^{3/2}\cos z$, and the extra times shrink at the rate $a_4' - b_4'/(2b_4)$. The Revision record computes the divergence of a diagonal tensor for this metric (`Revision/theory/field-theory-b4.json`, formula `energy_exchange`; `wolfram-field-theory-b4.json`, check `energy_exchange_equation_b4`): the $x_4$ component becomes

$$
\nabla_\mu T^\mu{}_{x_4} = -\frac{\partial\rho}{\partial x_4} - 3a_4'\,\big(p_3 - p_t\big) - \frac32\,\frac{b_4'}{b_4}\,\big(p_t + \rho\big),
$$

so a changing $b_4$ adds a term of the ordinary cosmological kind, with $\rho + p_t$, for the three extra times; the $x_0$ component is unchanged. The derivation of this section and Notebook 09a are for $b_4 = 1$.'''),
]
s = strict_replace(s, pairs, "ch09_b")
p.write_bytes(s.encode("utf-8"))
print("ok")
