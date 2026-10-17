"""W6 draft: Revision/pairing/kohn_sham/python/check_t3_completion.py for the corrected metric (applied to the copy argv[1]):
the block Hamiltonian with 1/f, the fold, the texts."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0], z = 6 H x0''' + " " + '''
(brane y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times.  The metric is the
author's metric with b4(x4) (SPEC section 1; b4 is never 1).  The Kohn-Sham history a4 = A H x4, b4 = b4(0) e^{(4/3) A H x4}
used by the demonstrations is a PRESCRIBED BACKGROUND (ks-theory.json adiabaticity.historyStatus).''',
    '''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real
(the fold cos z = 0 at y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times.  The metric is the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1).  The Kohn-Sham history
a4 = A H x4, b4 = b4(0) e^{(4/3) A H x4} used by the demonstrations is a PRESCRIBED BACKGROUND (ks-theory.json
adiabaticity.historyStatus).''')
rep('''    hB = lambda jj, MM, c: jj * (-sp.I * s1 * c.diff(y) + MM * s2 * c + kap * k * s3 * c) + v * c''',
    '''    fs = sp.Symbol("f", positive=True)          # the hidden scale (ks-theory.json blockEquation), constant on a slice
    hB = lambda jj, MM, c: jj * (-sp.I / fs * s1 * c.diff(y) + MM * s2 * c + kap * k * s3 * c) + v * c''')
rep('''          "the filling CONVENTION (H5: positive lambda = 0 branch plus the k = 0 brane zero modes, followed continuously in "''',
    '''          "the filling CONVENTION (H5: positive lambda = 0 branch plus the k = 0 fold zero modes, followed continuously in "''')
rep('''          "h_(-j)(-M) with odd parity (a(0) = 0) and the transformed tip theta = pi (a(-L) = 0), brane-localised "
          "(|chi|^2 = e^(2 M y)); control: it violates the untransformed tip")''',
    '''          "h_(-j)(-M) with the other fold condition (a(0) = 0) and the transformed tip theta = pi (a(-L) = 0), fold-localised "
          "(|chi|^2 = e^(2 M y); with the hidden scale f the profile is e^(2 f M y), the map is the same); control: it violates "
          "the untransformed tip")''')
rep('''        "background": "T3 holds slice by slice (b4 does not enter the block Hamiltonians); the history a4 = A H x4, b4 = "''',
    '''        "background": "T3 holds slice by slice (a4 and b4 enter the block Hamiltonians only through the positive constants f "
                      "and kappa of the slice); the history a4 = A H x4, b4 = "''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
