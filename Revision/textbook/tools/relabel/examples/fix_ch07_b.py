"""Chapter 07, sections 7.19 to 7.23 with b4."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/07-two-fields-and-lagrangians.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''- $\sqrt{|g|} = \cos z$ turns the coordinate volume into proper volume, so that the action does not depend on the coordinates.''',
     r'''- $\sqrt{|g|} = b_4^{3/2}\cos z$ turns the coordinate volume into proper volume, so that the action does not depend on the coordinates.'''),
    (r'''\mathcal{L} = \cos z\,\Big[\tfrac12\sum_{a=1}^{8}\frac{1}{f_a}\big(''',
     r'''\mathcal{L} = b_4^{3/2}\cos z\,\Big[\tfrac12\sum_{a=0}^{7}\frac{1}{f_a}\big('''),
    (r'''Gravity is still present in $\mathcal{L}$, through $\cos z$ and the frame factors $1/f_a$.''',
     r'''Gravity is still present in $\mathcal{L}$, through $b_4^{3/2}\cos z$ and the frame factors $1/f_a$.'''),
    (r'''- Step 6. $\sqrt{|g|} = \cos z \neq 0$ and''',
     r'''- Step 6. $\sqrt{|g|} = b_4^{3/2}\cos z \neq 0$ and'''),
    (r'''**The explicit form.** Since $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)}$, the Dirac operator is $\gamma^\mu D_\mu\Psi = \sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + 3H\gamma^{(x_0)}\Psi$, and the field equation in the author's metric reads''',
     r'''**The explicit form.** Since $\gamma^\mu = \gamma^{(\mu)}/f_\mu$ and $\gamma^\mu\Omega_\mu = M = 3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$ (Section 7.18), the Dirac operator is $\gamma^\mu D_\mu\Psi = \sum_a\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + M\Psi$, and the field equation in the author's metric reads'''),
    (r'''\frac{1}{e^{a_4}\sin^{1/6}z}\sum_{i=1}^{3}\gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}\partial_4\Psi + \frac{e^{a_4}}{\sin^{1/6}z}\sum_{t=5}^{7}\gamma^{(x_t)}\partial_t\Psi + \tan z\,\gamma^{(x_0)}\partial_0\Psi + 3H\gamma^{(x_0)}\Psi = (m + \lambda S)\Psi''',
     r'''\tan z\,\gamma^{(x_0)}\partial_0\Psi + \frac{1}{e^{a_4}\sin^{1/6}z}\sum_{i=1}^{3}\gamma^{(x_i)}\partial_i\Psi + \gamma^{(x_4)}\partial_4\Psi + \frac{e^{a_4}}{b_4^{1/2}\sin^{1/6}z}\sum_{t=5}^{7}\gamma^{(x_t)}\partial_t\Psi + 3H\gamma^{(x_0)}\Psi + \frac34\,\frac{b_4'}{b_4}\,\gamma^{(x_4)}\Psi = (m + \lambda S)\Psi'''),
    (r'''(PROVED; Notebook 07b, In [17]; Wolfram checks `Dirac_operator_explicit_G` and `Dirac_operator_explicit_C`; formula record key `field_equation`). The coefficient $e^{a_4}\sin^{-1/6}z$ of the extra-time derivatives GROWS as the extra times deflate, while that of the 3-space derivatives shrinks.''',
     r'''(PROVED; Notebook 07b, In [17]; `wolfram-field-theory-b4.json`, checks `Dirac_operator_explicit_G` and `Dirac_operator_explicit_C`; formula records, key `field_equation`; at $b_4 = 1$ the same checks of `wolfram-field-theory.json`). The coefficient $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ of the extra-time derivatives GROWS as the extra times deflate, while that of the 3-space derivatives shrinks.'''),
    (r'''\frac{-\partial_1\Psi_{16} + \partial_2\Psi_{15} - \partial_3\Psi_{14}}{e^{a_4}\sin^{1/6}z} - \partial_4\Psi_{14} + \frac{e^{a_4}(\partial_5\Psi_{15} + \partial_6\Psi_{16} + \partial_7\Psi_9)}{\sin^{1/6}z} + \tan z\,\partial_0\Psi_9 + 3H\Psi_9 = (m + \lambda S)\Psi_1 .''',
     r'''\tan z\,\partial_0\Psi_9 + \frac{-\partial_1\Psi_{16} + \partial_2\Psi_{15} - \partial_3\Psi_{14}}{e^{a_4}\sin^{1/6}z} - \partial_4\Psi_{14} + \frac{e^{a_4}(\partial_5\Psi_{15} + \partial_6\Psi_{16} + \partial_7\Psi_9)}{b_4^{1/2}\sin^{1/6}z} + 3H\Psi_9 - \frac34\,\frac{b_4'}{b_4}\,\Psi_{14} = (m + \lambda S)\Psi_1 .'''),
    (r'''Notebook 07b prints this equation in its own symbols and the same equation read from the formula record (`Revision/theory/field-theory.json`, key `field_equation_components`), and checks that all 16 equations agree term by term (In [17]).''',
     r'''Notebook 07b prints this equation in its own symbols and the same equation read from the formula record (`Revision/theory/field-theory-b4.json`, key `field_equation_components`), and checks that all 16 equations agree term by term with it and, at $b_4 = 1$, with the record `Revision/theory/field-theory.json` (In [17]).'''),
    (r'''and the gravitational term $3H\Psi_B$ stands next to the hidden-direction derivative $\tan z\,\partial_0\Psi_B$ of the same component (Figure 07b.4).''',
     r'''and the gravitational term $3H\Psi_B$ stands next to the hidden-direction derivative $\tan z\,\partial_0\Psi_B$ of the same component, the term $-\frac34(b_4'/b_4)\Psi_B$ next to the time derivative $-\partial_4\Psi_B$ (Figure 07b.4).'''),
    (r'''\sum_a\frac{1}{f_a}\bar\tau_a\,\partial_a\psi_+ + 3H\psi_+ = V\psi_-,\qquad \sum_a\frac{1}{f_a}\tau_a\,\partial_a\psi_- + 3H\psi_- = V\psi_+ :''',
     r'''\sum_a\frac{1}{f_a}\bar\tau_a\,\partial_a\psi_+ + 3H\psi_+ + \tfrac34\tfrac{b_4'}{b_4}\bar\tau_{x_4}\psi_+ = V\psi_-,\qquad \sum_a\frac{1}{f_a}\tau_a\,\partial_a\psi_- + 3H\psi_- + \tfrac34\tfrac{b_4'}{b_4}\tau_{x_4}\psi_- = V\psi_+ :'''),
    (r'''**The evolution form.** Write the explicit equation with the $x_4$ term separately ($f_4 = 1$) and solve it for $\partial_4\Psi$, line by line:''',
     r'''**The evolution form.** Write the explicit equation with the $x_4$ term separately ($f_4 = 1$), with the gravitational term $M = 3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$, and solve it for $\partial_4\Psi$, line by line:'''),
    (r'''\gamma^{(x_4)}\partial_4\Psi + \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + 3H\gamma^{(x_0)}\Psi = V\Psi''',
     r'''\gamma^{(x_4)}\partial_4\Psi + \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi + M\Psi = V\Psi'''),
    (r'''\gamma^{(x_4)}\partial_4\Psi = V\Psi - \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(x_0)}\Psi''',
     r'''\gamma^{(x_4)}\partial_4\Psi = V\Psi - \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - M\Psi'''),
    (r'''\partial_4\Psi = -\gamma^{(x_4)}\Big[V\Psi - \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - 3H\gamma^{(x_0)}\Psi\Big]''',
     r'''\partial_4\Psi = -\gamma^{(x_4)}\Big[V\Psi - \sum_{a\neq x_4}\frac{1}{f_a}\gamma^{(a)}\partial_a\Psi - M\Psi\Big]'''),
    (r'''the slices $x_4 = $ const are **non-characteristic** (PROVED; Notebook 07b, In [19]; Wolfram checks `evolution_form_G` and `evolution_form_C`).''',
     r'''the slices $x_4 = $ const are **non-characteristic** (PROVED; Notebook 07b, In [19]; `wolfram-field-theory-b4.json`, checks `evolution_form_G` and `evolution_form_C`; the part $\frac34(b_4'/b_4)\gamma^{(x_4)}$ of $M$ gives $-\frac34(b_4'/b_4)\Psi$ on the right, formula record key `evolution_form`).'''),
    # self-consistency
    (r'''This book treats them as follows.

**(i) One system.**''',
     r'''This book treats them as follows. The record proves (iii), (v) and (vi) for the metric at $b_4 = 1$; for a general $b_4$ the record contains (i), (ii) and the local law of (iv), while the Noether identities of (v), the Lichnerowicz identity of (iii) and the exact solutions of (vi) were NOT recomputed for a general $b_4$ (`Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`; `claude_failures.md`, C1).

**(i) One system.**'''),
    (r'''(\gamma^\mu D_\mu)^2\Psi = g^{\mu\nu}\big(D_\mu D_\nu\Psi - \Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\big) - \frac{R}{4}\Psi,\qquad R = 6\big((a_4')^2 - 7H^2\big).''',
     r'''(\gamma^\mu D_\mu)^2\Psi = g^{\mu\nu}\big(D_\mu D_\nu\Psi - \Gamma^\lambda{}_{\mu\nu}D_\lambda\Psi\big) - \frac{R}{4}\Psi,\qquad R = 6\big((a_4')^2 - 7H^2\big)\ \text{at}\ b_4 = 1.'''),
    (r'''and $R$ is the Ricci scalar of the author's metric (Section 3.17; its value is derived in Sections 3.25 and 8.7).''',
     r'''and $R$ is the Ricci scalar of the author's metric (Section 3.17; its value is derived in Sections 3.25 and 8.7; with $b_4$ it is $R = 6a_4'^2 - 3a_4'b_4'/b_4 + 3b_4''/b_4 - 42H^2$, formula record key `ricci_scalar`).'''),
    (r'''Status: the identity is PROVED in the Revision record (checks `Lichnerowicz_identity_G` of `wolfram-field-theory.json`, `lichnerowicz_identity_on_fields` and `lichnerowicz_contraction` of `python-field-theory.json`); it is quoted here and NOT derived in this book.''',
     r'''Status: the identity is PROVED in the Revision record for the metric at $b_4 = 1$ (checks `Lichnerowicz_identity_G` of `wolfram-field-theory.json`, `lichnerowicz_identity_on_fields` and `lichnerowicz_contraction` of `python-field-theory.json`); it is quoted here and NOT derived in this book. It is a general identity of the square of the Dirac operator, but the record has not checked it for the metric with a changing $b_4$.'''),
    (r'''It is real and obeys the local law $\nabla_\mu J^\mu = 0$, that is $\sum_\mu\partial_\mu(\sqrt{|g|}\,J^\mu) = 0$, on every solution (PROVED; derived line by line in Section 21.17; checks `current_conservation_identity_G` and `grassmann_current_conservation`).''',
     r'''It is real and obeys the local law $\nabla_\mu J^\mu = 0$, that is $\sum_\mu\partial_\mu(\sqrt{|g|}\,J^\mu) = 0$ with $\sqrt{|g|} = b_4^{3/2}\cos z$, on every solution (PROVED; derived line by line in Section 21.17; checks `current_conservation_identity_G` and `grassmann_current_conservation` at $b_4 = 1$, and `u1_noether_matrix_identity_b4` of `python-field-theory-b4.json` for every $b_4$).'''),
    (r'''on every solution they make the energy-momentum tensor symmetric and conserved, $\nabla_\mu T^\mu{}_\nu = 0$ (PROVED in the Revision record, checks''',
     r'''on every solution they make the energy-momentum tensor symmetric and conserved, $\nabla_\mu T^\mu{}_\nu = 0$ (PROVED in the Revision record for the metric at $b_4 = 1$, checks'''),
    (r'''**(vi) Exact solutions as test points.** The exact family derived at the end of this section solves the field equation for every $a_4$ (PROVED here; Notebook 07b, In [21]);''',
     r'''**(vi) Exact solutions as test points.** The exact family derived at the end of this section solves the field equation for every $a_4$ and every constant $b_4$ (PROVED here; Notebook 07b, In [21]);'''),
    # 7.23 theorem
    (r'''**Theorem (non-triviality [1] and [2] in the diagonal frame).** Hypotheses: the author's metric with $H > 0$ and $0 < z < \pi/2$; any function $a_4(x_4)$, a constant one included; real $m$ and $\lambda$;''',
     r'''**Theorem (non-triviality [1] and [2] in the diagonal frame).** Hypotheses: the author's metric with $H > 0$ and $0 < z < \pi/2$; any function $a_4(x_4)$, a constant one included; a constant $b_4 > 0$ (as on the backgrounds $b_4 = 1$; a changing $b_4$ is treated after the proof); real $m$ and $\lambda$;'''),
    (r'''\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(x_0)}\Psi \neq 0 .''',
     r'''\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(x_0)}\Psi \neq 0 .'''),
    (r'''*Proof.* The difference is $\gamma^\mu(D_\mu - \partial_\mu)\Psi = \gamma^\mu\Omega_\mu\Psi$ by the definition of $D_\mu$, and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)}$ by Section 7.18.''',
     r'''*Proof.* The difference is $\gamma^\mu(D_\mu - \partial_\mu)\Psi = \gamma^\mu\Omega_\mu\Psi$ by the definition of $D_\mu$, and $\gamma^\mu\Omega_\mu = 3H\gamma^{(x_0)}$ for a constant $b_4$ by Section 7.18.'''),
    (r'''Moreover, $\Omega_\mu$ vanishes for all $\mu$ only if $a_4' = 0$ AND $H = 0$, because each of its 12 nonzero components is $a_4'$ or $H$ times a factor that never vanishes;''',
     r'''Moreover, $\Omega_\mu$ vanishes for all $\mu$ only if $H = 0$, because six of its 12 nonzero components are $H$ times a factor that never vanishes (and the other six are $a_4'$ or $a_4' - b_4'/(2b_4)$ times such a factor);'''),
    (r'''**The exact scope of the theorem.** The value $3H\gamma^{(x_0)}$ belongs to the diagonal frame and to the field variables $\Psi$;''',
     r'''**A changing $b_4$.** Then the difference is $M\Psi$ with $M = 3H\gamma^{(x_0)} + \frac34(b_4'/b_4)\gamma^{(x_4)}$. Because $\gamma^{(x_0)}$ and $\gamma^{(x_4)}$ anticommute and $(\gamma^{(x_0)})^2 = 1$, $(\gamma^{(x_4)})^2 = -1$, the cross terms cancel and $MM = \big(9H^2 - \frac{9}{16}(b_4'/b_4)^2\big)1$. So $M\Psi = 0$ forces $\Psi = 0$ at every time where $|b_4'/b_4| \neq 4H$; at a time where $|b_4'/b_4| = 4H$ the matrix $M$ has rank 8 and $M\Psi$ vanishes for the fields in its null space (PROVED; `python-field-theory-b4.json`, check `gravity_term_square_b4`; Notebook 07b, In [20], checks the difference $M\Psi$ in all 16 components). The theorem, as the record states it, is the case of a constant $b_4$.

**The exact scope of the theorem.** The value $3H\gamma^{(x_0)}$ belongs to the diagonal frame and to the field variables $\Psi$;'''),
    (r'''- In another frame of the same metric, boosted in the $(x_4, x_0)$ plane with the rapidity $6Hx_4 + b_0$, the term $\gamma^\mu\Omega_\mu$ vanishes identically.
- Within the diagonal frame the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it (derived below).
- The deflation contributes nothing to $\gamma^\mu\Omega_\mu$: $a_4$ enters the field equation only through the frame factors $e^{\mp a_4}\sin^{-1/6}z$ of the derivative terms. And since the connection drops out of $\mathcal{L}$ (Section 7.20), the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; $3H\gamma^{(x_0)} = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ is its volume-and-frame term.''',
     r'''- In another frame of the same metric, boosted in the $(x_4, x_0)$ plane with the rapidity $6Hx_4 + b_0$, the term $\gamma^\mu\Omega_\mu$ vanishes identically (for a constant $b_4$; Section 6.16).
- Within the diagonal frame the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it (derived below for a constant $b_4$; for a changing $b_4$ the rescaling $\Psi = \sin^{-1/2}z\,b_4^{-3/4}\chi$ removes all of $M$, Section 6.18).
- The deflation contributes nothing to $\gamma^\mu\Omega_\mu$: $a_4$ enters the field equation only through the frame factors $e^{-a_4}\sin^{-1/6}z$ and $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ of the derivative terms. And since the connection drops out of $\mathcal{L}$ (Section 7.20), the Euler-Lagrange equations are those of the connection-free symmetric Lagrangian; $M = \frac{1}{2\sqrt{|g|}}\partial_\mu(\sqrt{|g|}\gamma^\mu)$ is its volume-and-frame term.'''),
    (r'''Only the $x_0$ term of the Dirac operator acts on the factor $\sin^{-1/2}z$, so by the product rule''',
     r'''Take $b_4$ constant. Only the $x_0$ term of the Dirac operator acts on the factor $\sin^{-1/2}z$, so by the product rule'''),
    (r'''(the explicit equation; the derivatives along the other six directions vanish, which is why the result holds for EVERY $a_4$);''',
     r'''(the explicit equation for a constant $b_4$; the derivatives along the other six directions vanish, which is why the result holds for EVERY $a_4$);'''),
    # table
    (r'''| the gravitational term $3H\gamma^{(x_0)}\Psi$ of the field equation is nonzero, both statistics | PROVED; Notebook 07b, In [20] | `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00` |
| $\Omega_\mu = 0$ only for $a_4' = 0$ and $H = 0$; $H = 0$ degenerate; curved for every $H > 0$ | PROVED |''',
     r'''| the gravitational term $3H\gamma^{(x_0)}\Psi$ of the field equation is nonzero for a constant $b_4$, both statistics | PROVED; Notebook 07b, In [20] | `wolfram-field-theory.json`, checks `nontriviality_1_dirac16complex` and `nontriviality_2_dirac16complex00` (at $b_4 = 1$) |
| with a changing $b_4$: $MM = (9H^2 - \frac{9}{16}(b_4'/b_4)^2)1$, so $M\Psi \neq 0$ unless $\lvert b_4'/b_4\rvert = 4H$ | PROVED | `python-field-theory-b4.json`, check `gravity_term_square_b4` |
| $\Omega_\mu = 0$ only for $a_4' = 0$ and $H = 0$ (at $b_4 = 1$); $H = 0$ degenerate; curved for every $H > 0$ | PROVED |'''),
    (r'''| the boosted frame removes $\gamma^\mu\Omega_\mu$ | PROVED (quoted) |''',
     r'''| the boosted frame removes $\gamma^\mu\Omega_\mu$ (constant $b_4$) | PROVED (quoted) |'''),
    (r'''| the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it; the coupling $\lambda S[\chi]/\sin z$ | PROVED here |''',
     r'''| the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it; the coupling $\lambda S[\chi]/\sin z$ (constant $b_4$; with $b_4$ see Section 6.18) | PROVED here |'''),
    (r'''| self-consistency (iii): the Lichnerowicz identity, $R = 6((a_4')^2 - 7H^2)$ | PROVED in the record, quoted,''',
     r'''| self-consistency (iii): the Lichnerowicz identity, $R = 6((a_4')^2 - 7H^2)$ (at $b_4 = 1$) | PROVED in the record at $b_4 = 1$, quoted,'''),
]
s = strict_replace(s, pairs, "ch07_b")
p.write_bytes(s.encode("utf-8"))
print("ok")
