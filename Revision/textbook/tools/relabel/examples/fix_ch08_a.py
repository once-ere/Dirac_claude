"""Chapter 08, sections 8.1 and 8.2: b4 and the order x0..x7."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/08-non-triviality-and-well-posedness.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''The gravitational term of the field equation is $3H\gamma^{(0)}\Psi$ in the natural frame, but a different, equally valid frame makes it vanish,''',
     r'''The gravitational term of the field equation is $3H\gamma^{(0)}\Psi$ in the natural frame on the backgrounds $b_4 = 1$ of the Revision record ($(3H\gamma^{(0)} + \frac34(b_4'/b_4)\gamma^{(4)})\Psi$ for the general metric with $b_4$), but a different, equally valid frame makes it vanish,'''),
    (r'''- In the diagonal frame of the author's metric the gravitational term of the field equation is $\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(0)}\Psi$, for every history $a_4(x_4)$. The time-direction pieces of the three inflating and the three deflating directions cancel; the six hidden-direction pieces add up to $3H$. The term is not zero for any field $\Psi \neq 0$ (PROVED; Sections 8.4 to 8.6).''',
     r'''- In the diagonal frame of the author's metric the gravitational term of the field equation is $\gamma^\mu\Omega_\mu\Psi = 3H\gamma^{(0)}\Psi$, for every history $a_4(x_4)$ and a constant $b_4$, as on the backgrounds $b_4 = 1$ (for a changing $b_4$ the term $\frac34(b_4'/b_4)\gamma^{(4)}\Psi$ is added; Chapters 6 and 7). The time-direction pieces of the three inflating and the three deflating directions cancel; the six hidden-direction pieces add up to $3H$. The term is not zero for any field $\Psi \neq 0$ (PROVED; Sections 8.4 to 8.6; for a changing $b_4$ except at times where $|b_4'/b_4| = 4H$, Section 7.23).'''),
    (r'''- The spin connection vanishes only in the formal flat limit $a_4' = 0$ and $H = 0$, which is not a member of the author's family of metrics (PROVED; Section 8.6).''',
     r'''- The spin connection vanishes only in the formal flat limit $a_4' = 0$ and $H = 0$ (at $b_4 = 1$; for every $b_4$ it vanishes only for $H = 0$), which is not a member of the author's family of metrics (PROVED; Section 8.6).'''),
    (r'''In a frame boosted in the $(x_4, x_0)$ plane with the rapidity $6Hx_4$ the term is identically zero, and the rescaling $\Psi = \sin^{-1/2}z\,\chi$ removes it in the diagonal frame (PROVED; Sections 8.9 and 8.30).''',
     r'''In a frame boosted in the $(x_4, x_0)$ plane with the rapidity $6Hx_4$ the term is identically zero (for a constant $b_4$), and the rescaling $\Psi = \sin^{-1/2}z\,\chi$ ($\sin^{-1/2}z\,b_4^{-3/4}\chi$ for a changing $b_4$) removes it in the diagonal frame (PROVED; Sections 8.9 and 8.30; Sections 6.16 and 6.18).'''),
    (r'''and the frame factors $e^{\mp a_4}\sin^{-1/6}z$ and $\tan z$ multiply every derivative''',
     r'''and the frame factors $e^{-a_4}\sin^{-1/6}z$, $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ and $\tan z$ multiply every derivative'''),
    (r'''**Labels.** As everywhere in the book,''',
     r'''**The metric with $b_4$.** The author's metric of 2026-10-14 has a second function $b_4(x_4) > 0$ in the extra-time entries (Chapter 3; `Revision/metric_b4/METRIC_CHANGE_PROVENANCE.md`). The Revision record's scope reports and the backgrounds of its numerical work have $b_4 = 1$, and the four notebooks of this chapter compare with those reports, so their exact checks are made at $b_4 = 1$; Notebooks 06a and 06b and Chapter 7 treat a general $b_4$. Where a statement of this chapter changes for a changing $b_4$, the change is stated with it.

**Labels.** As everywhere in the book,'''),
    (r'''In Python, lists are counted from 0, so position 0 holds $x_1$, position 3 the time $x_4$ and position 7 the hidden coordinate $x_0$.''',
     r'''In Python, lists are counted from 0, like the author's coordinates: position $k$ holds $x_k$, so position 0 is the hidden coordinate $x_0$ and position 4 the time $x_4$.'''),
    (r'''$$
g = \mathrm{diag}\big(f_1^2,\ f_2^2,\ f_3^2,\ -f_4^2,\ -f_5^2,\ -f_6^2,\ -f_7^2,\ f_0^2\big),
$$

$$
f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = e^{-a_4}\sin^{1/6}z, \quad f_0 = \cot z .
$$''',
     r'''$$
g = \mathrm{diag}\big(f_0^2,\ f_1^2,\ f_2^2,\ f_3^2,\ -f_4^2,\ -f_5^2,\ -f_6^2,\ -f_7^2\big),
$$

$$
f_0 = \cot z, \quad f_1 = f_2 = f_3 = e^{a_4}\sin^{1/6}z, \quad f_4 = 1, \quad f_5 = f_6 = f_7 = e^{-a_4}b_4^{1/2}\sin^{1/6}z ,
$$

with $b_4 = 1$ on the backgrounds of the record (and in the checks of this chapter's notebooks).'''),
    (r'''The product of the eight factors is the volume factor, $\sqrt{|g|} = f_0f_2\cdots f_7 = \cos z$; it does not depend on the time, because the inflation $e^{3a_4}$ of 3-space and the deflation $e^{-3a_4}$ of the extra times cancel (PROVED; `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g_equals_cos_z`).''',
     r'''The product of the eight factors is the volume factor, $\sqrt{|g|} = f_0f_1\cdots f_7 = b_4^{3/2}\cos z$, which is $\cos z$ at $b_4 = 1$; it does not depend on the time there, because the inflation $e^{3a_4}$ of 3-space and the deflation $e^{-3a_4}$ of the extra times cancel (PROVED; `Revision/theory/reports/python-field-theory.json`, check `sqrt_det_g_equals_cos_z`; for $b_4$, `wolfram-field-theory-b4.json`, check `sqrt_det_g`).'''),
    (r'''one for each direction $a = 1, \dots, 8$, that have length 1''',
     r'''one for each direction $a = 0, \dots, 7$, that have length 1'''),
    (r'''the sum over $\mu = 1, \dots, 8$ is understood''',
     r'''the sum over $\mu = 0, \dots, 7$ is understood'''),
    (r'''Written out in the diagonal frame the equation reads (`Revision/theory/field-theory.json`, formula key `field_equation`; Section 8.5 derives the last term on the left):''',
     r'''Written out in the diagonal frame at $b_4 = 1$ the equation reads (`Revision/theory/field-theory.json`, formula key `field_equation`; Section 8.5 derives the last term on the left; for a general $b_4$ the extra-time factor is $e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ and the term $\frac34(b_4'/b_4)\gamma^{(4)}\Psi$ is added on the left, `Revision/theory/field-theory-b4.json`, key `field_equation`):'''),
    (r'''with $1/f_i = e^{-a_4}\sin^{-1/6}z$, $1/f_4 = 1$, $1/f_t = e^{a_4}\sin^{-1/6}z$ and $1/f_0 = \tan z$.''',
     r'''with $1/f_0 = \tan z$, $1/f_i = e^{-a_4}\sin^{-1/6}z$, $1/f_4 = 1$ and $1/f_t = e^{a_4}b_4^{-1/2}\sin^{-1/6}z$ ($e^{a_4}\sin^{-1/6}z$ at $b_4 = 1$).'''),
]
s = strict_replace(s, pairs, "ch08_a")
p.write_bytes(s.encode("utf-8"))
print("ok")
