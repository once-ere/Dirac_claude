"""Chapter 14: code descriptions after the relabel; the background b4 = 1 stated."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/chapters/14-kohn-sham-model.md"
s = p.read_text(encoding="utf-8")
pairs = [
    (r'''`g[0]` is $\gamma^{(x_1)}$ and `g[7]` is $\gamma^{(x_0)}$ (Python counts from 0). `eta` is the list of the eight signs. The third line gives the eight matrices the names `g1` to `g8` (unpacking a list into names).''',
     r'''`g[0]` is $\gamma^{(x_0)}$ and `g[7]` is $\gamma^{(x_7)}$ (Python counts from 0, like the author's coordinates). `eta` is the list of the eight signs. The third line gives the eight matrices the names `g0` to `g7` (unpacking a list into names), so `gN` is $\gamma^{(x_N)}$.'''),
    (r'''If $X = c_4\gamma^{(x_4)} + c_8\gamma^{(x_0)}$, then $X\gamma^{(x_4)} = -c_4 + c_8\gamma^{(x_0)}\gamma^{(x_4)}$,''',
     r'''If $X = c_4\gamma^{(x_4)} + c_0\gamma^{(x_0)}$, then $X\gamma^{(x_4)} = -c_4 + c_0\gamma^{(x_0)}\gamma^{(x_4)}$,'''),
    (r'''in the same way $\mathrm{tr}(X\gamma^{(x_0)}) = 16c_8$. These are the second and third lines. The fourth line checks that $X$ is exactly $c_4\gamma^{(x_4)} + c_8\gamma^{(x_0)}$''',
     r'''in the same way $\mathrm{tr}(X\gamma^{(x_0)}) = 16c_0$. These are the second and third lines. The fourth line checks that $X$ is exactly $c_4\gamma^{(x_4)} + c_0\gamma^{(x_0)}$'''),
    (r'''`c4_list[0:3]` is the part of the list from position 0 up to, but not including, position 3 (the directions $x_1, x_2, x_3$), and `c4_list[4:7]` the positions 4 to 6 ($x_5, x_6, x_7$).''',
     r'''`c4_list[1:4]` is the part of the list from position 1 up to, but not including, position 4 (the directions $x_1, x_2, x_3$), and `c4_list[5:8]` the positions 5 to 7 ($x_5, x_6, x_7$).'''),
    (r'''`sp.symbols("x1:8")` makes the seven symbols $x_1, \dots, x_7$; adding a one-element **tuple** (a list in round brackets) with the symbol $y$ gives the eight coordinates, with $y$ in the place of $x_0$.''',
     r'''`sp.symbols("x1:8")` makes the seven symbols $x_1, \dots, x_7$; a one-element **tuple** (a list in round brackets) with the symbol $y$ put in front of them gives the eight coordinates, with $y$ in the place of $x_0$ (position 0), so `X[k]` is $x_k$ for $k \ge 1$. The frame factors `vb` are in the same order: $1$ for $y$, $e^{a_4}W$ for $x_1, x_2, x_3$, $1$ for $x_4$ and $e^{-a_4}W$ for the extra times (the metric on the background $b_4 = 1$; the author's metric of 2026-10-14 has the factor $b_4^{1/2}$ in the extra times, Chapter 3).'''),
    (r'''**The history is a PRESCRIBED BACKGROUND.** The slices are taken along the history $a_4 = AHx_4$ with $A = 1$,''',
     r'''**The history is a PRESCRIBED BACKGROUND.** The Kohn-Sham record works on the backgrounds $b_4 = 1$ of the author's metric (the second function $b_4(x_4)$ of the metric of 2026-10-14 is put equal to 1; Chapter 3). The slices are taken along the history $a_4 = AHx_4$ with $A = 1$,'''),
]
s = strict_replace(s, pairs, "ch14")
s = s.replace("c_8", "c_0")
p.write_bytes(s.encode("utf-8"))
print("ok")
