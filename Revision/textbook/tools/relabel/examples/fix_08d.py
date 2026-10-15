"""08d builder: positions of the author's coordinates x0..x7 and the record's names (M0, dx0);
the notebook stays on the background b4 = 1 of the record's scope reports and says so."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from relabel_common import REPO, strict_replace  # noqa: E402

p = REPO / "Revision/textbook/notebooks/src/08d_rescaling_modes.py"
s = p.read_text(encoding="utf-8")
pairs = [
    ('''    x = sp.symbols("x0:8", real=True)  # the coordinates; x[3] is x4, x[7] is x0''',
     '''    x = sp.symbols("x0:8", real=True)  # the coordinates; x[k] is xk'''),
    ('''    f = [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] + [sp.exp(-a4) * sixth] * 3 \\
        + [sp.cot(z)]''',
     '''    f = [sp.cot(z)] + [sp.exp(a4) * sixth] * 3 + [sp.Integer(1)] \\
        + [sp.exp(-a4) * sixth] * 3  # the frame factors at b4 = 1'''),
    ('''    for i in (0, 1, 2):  # x1, x2, x3 (inflating)''',
     '''    for i in (1, 2, 3):  # x1, x2, x3 (inflating)'''),
    ('''    for t in (4, 5, 6):  # x5, x6, x7 (deflating extra times)''',
     '''    for t in (5, 6, 7):  # x5, x6, x7 (deflating extra times)'''),
    ('''                 "A = -i m g4 + 3 i H g4 g8: not Hermitian, A^2 = (m^2 - 9H^2) I16, "''',
     '''                 "A = -i m g4 + 3 i H g4 g0: not Hermitian, A^2 = (m^2 - 9H^2) I16, "'''),
    ('''    u0 = (G[3] * G[7] - sp.eye(16)).nullspace()[0]  # gamma^(4) gamma^(8) u0 = u0''',
     '''    u0 = (G[3] * G[7] - sp.eye(16)).nullspace()[0]  # gamma^(4) gamma^(0) u0 = u0'''),
]
s = strict_replace(s, pairs, "08d")
for old, new in (("x[3]", "x[4]"), ("x[7]", "x[0]"), ("G[3]", "G[4]"), ("G[7]", "G[0]"),
                 ("M8", "M0"), ("M_8", "M_0"), ("d8_coefficient", "d0_coefficient"),
                 ("X8", "X0"), ("g4g8", "g4g0"), ("dx8", "dx0"), ("dy/dx8", "dy/dx0"),
                 ("tan z d8 ", "tan z d0 "), ("in front of d8 in h", "in front of d0 in h"),
                 ("= d8(sin z", "= d0(sin z")):
    s = s.replace(old, new)
p.write_bytes(s.encode("utf-8"))
left = [l for l in s.splitlines() if any(t in l for t in ("x[3]", "x[7]", "G[3]", "G[7]", "M8", "d8"))]
print("ok", left)
