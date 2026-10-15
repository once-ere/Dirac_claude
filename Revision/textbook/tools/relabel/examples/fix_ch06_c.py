"""Chapter 06, sections 6.23 to 6.25: the mixed contraction with b4, order x0..x7."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # the folder of relabel_common.py
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/06-spinors-in-curved-space.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''**The author's metric.** Of the 12 components of Section 6.6 the six with an $x0$ for $\mu = x_i$ are space-space pairs (kept), the three $(x4, x_t)$ are time-time pairs (sign reversed), and the three $(x_i, x4)$ and the three $(x_t, x0)$ are boost pairs (deleted). So

$$
\Omega^{nb}_{x_i} = e^{a_4}s\,H\,S^{x_i\,x0}, \qquad \Omega^{nb}_{x_t} = +e^{-a_4}s\,a_4'\,S^{x4\,x_t},
$$

compared with $\Omega_{x_i} = e^{a_4}s(a_4'S^{x_ix4} + HS^{x_ix0})$ and $\Omega_{x_t} = -e^{-a_4}s(a_4'S^{x4x_t} + HS^{x_tx0})$. The contraction, by the steps of Section 6.8:

$$
\gamma^{x_i}\Omega^{nb}_{x_i} = \frac{\gamma^{(x_i)}}{f_i}\,f_iH\,\tfrac12\gamma^{(x_i)}\gamma^{(x0)} = \tfrac H2\gamma^{(x0)}, \qquad \gamma^{x_t}\Omega^{nb}_{x_t} = \frac{\gamma^{(x_t)}}{f_t}\,f_ta_4'\,\tfrac12\gamma^{(x4)}\gamma^{(x_t)} = \tfrac{a_4'}2\gamma^{(x4)}
$$

($(\gamma^{(x_i)})^2 = 1$; and $\gamma^{(x_t)}\gamma^{(x4)}\gamma^{(x_t)} = \gamma^{(x4)}$ as in Section 6.8). Summed over the six warped directions:

$$
\sum_\mu\gamma^\mu\Omega^{nb}_\mu = \tfrac{3H}{2}\gamma^{(x0)} + \tfrac{3a_4'}{2}\gamma^{(x4)} \qquad\text{instead of}\qquad \sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)} .
$$

Half of the hidden term is lost, and the time-direction terms no longer cancel: with the mixed contraction the deflation would appear in this term.''',
     r'''**The author's metric.** Of the 12 components of Section 6.6 the three $(x0, x_i)$ are space-space pairs (kept), the three $(x4, x_t)$ are time-time pairs (sign reversed), and the three $(x_i, x4)$ and the three $(x0, x_t)$ are boost pairs (deleted). So, with $r = a_4' - b_4'/(2b_4)$ and $f_t = e^{-a_4}b_4^{1/2}s$,

$$
\Omega^{nb}_{x_i} = e^{a_4}s\,H\,S^{x_i\,x0}, \qquad \Omega^{nb}_{x_t} = +f_t\,r\,S^{x4\,x_t},
$$

compared with $\Omega_{x_i} = e^{a_4}s(a_4'S^{x_ix4} + HS^{x_ix0})$ and $\Omega_{x_t} = -f_t(r\,S^{x4x_t} + HS^{x_tx0})$ (Section 6.7). The contraction, by the steps of Section 6.8:

$$
\gamma^{x_i}\Omega^{nb}_{x_i} = \frac{\gamma^{(x_i)}}{f_i}\,f_iH\,\tfrac12\gamma^{(x_i)}\gamma^{(x0)} = \tfrac H2\gamma^{(x0)}, \qquad \gamma^{x_t}\Omega^{nb}_{x_t} = \frac{\gamma^{(x_t)}}{f_t}\,f_t\,r\,\tfrac12\gamma^{(x4)}\gamma^{(x_t)} = \tfrac{r}2\gamma^{(x4)}
$$

($(\gamma^{(x_i)})^2 = 1$; and $\gamma^{(x_t)}\gamma^{(x4)}\gamma^{(x_t)} = \gamma^{(x4)}$ as in Section 6.8). Summed over the six warped directions:

$$
\sum_\mu\gamma^\mu\Omega^{nb}_\mu = \tfrac{3H}{2}\gamma^{(x0)} + \tfrac32\Big(a_4' - \frac{b_4'}{2b_4}\Big)\gamma^{(x4)} \quad\text{instead of}\quad \sum_\mu\gamma^\mu\Omega_\mu = 3H\gamma^{(x0)} + \frac34\,\frac{b_4'}{b_4}\,\gamma^{(x4)} ;
$$

at $b_4 = 1$, $\frac{3H}{2}\gamma^{(x0)} + \frac{3a_4'}{2}\gamma^{(x4)}$ instead of $3H\gamma^{(x0)}$. Half of the hidden term is lost, and the $a_4'$ terms along the time no longer cancel: with the mixed contraction the deflation would appear in this term.'''),
    (r'''For $\mu = x1$ the difference is $\Omega^{nb}_{x1} - \Omega_{x1} = -f_1a_4'S^{x1x4}$, the deleted boost part, and''',
     r'''(The counting below is written at $b_4 = 1$; for a general $b_4$ replace $a_4'$ in the extra-time parts by $r = a_4' - b_4'/(2b_4)$, which changes no count.) For $\mu = x1$ the difference is $\Omega^{nb}_{x1} - \Omega_{x1} = -f_1a_4'S^{x1x4}$, the deleted boost part, and'''),
    (r'''| $\gamma^\mu\Omega^{nb}_\mu = \frac{3H}{2}\gamma^{(x0)} + \frac{3a_4'}{2}\gamma^{(x4)}$; 15 violated pairs, 288 entries |''',
     r'''| $\gamma^\mu\Omega^{nb}_\mu = \frac{3H}{2}\gamma^{(x0)} + \frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$; 15 violated pairs, 288 entries |'''),
    (r'''Two facts single out the correct value $3H\gamma^{(x0)}$ among all candidates.''',
     r'''Two facts single out the correct value $3H\gamma^{(x0)} + \frac34(b_4'/b_4)\gamma^{(x4)}$ ($3H\gamma^{(x0)}$ at $b_4 = 1$) among all candidates.'''),
    (r'''The mixed contraction, $\frac{3H}{2}\gamma^{(x0)} + \frac{3a_4'}{2}\gamma^{(x4)}$, does not equal it.''',
     r'''The mixed contraction, $\frac{3H}{2}\gamma^{(x0)} + \frac32(a_4' - \frac{b_4'}{2b_4})\gamma^{(x4)}$, does not equal it.'''),
    (r'''This is the property that makes $iA$ a Hermitian operator in quantum theory (Chapter 10), and the natural weight is the volume factor $\cos z$.''',
     r'''This is the property that makes $iA$ a Hermitian operator in quantum theory (Chapter 10), and the natural weight is the volume factor $\sqrt{\lvert g\rvert} = b_4^{3/2}\cos z$; along the hidden direction $b_4^{3/2}$ is a constant factor, which multiplies every line below and is left out, so the weight is $\cos z$.'''),
    (r'''PROVED; `field-theory.json`, formula `hidden_direction_hermiticity`; `wolfram-field-theory.json`, check `good_sector_hermiticity_curved`; both scope reports, check `good_sector_hermiticity_up_to_the_brane_flux`; Notebook 06c, In [15].''',
     r'''PROVED; `field-theory.json`, formula `hidden_direction_hermiticity` (written at $b_4 = 1$); `wolfram-field-theory.json`, check `good_sector_hermiticity_curved`; both scope reports, check `good_sector_hermiticity_up_to_the_brane_flux`; Notebook 06c, In [15].'''),
    (r'''Notebook 06c checks Sections 6.23 and 6.24 with exact algebra. It reads the author's gammas and the formulas of the record,''',
     r'''Notebook 06c checks Sections 6.23 and 6.24 with exact algebra, for arbitrary functions $a_4(x_4)$ and $b_4(x_4)$. It reads the author's gammas and the formulas of the records (with $b_4$, and at $b_4 = 1$),'''),
    (r'''Every correct result is compared with the Revision record; the results about the mixed contraction''',
     r'''Every correct result is compared with the Revision records; the results about the mixed contraction'''),
]
s = strict_replace(s, pairs, "ch06_c")
p.write_bytes(s.encode("utf-8"))
print("ok")
