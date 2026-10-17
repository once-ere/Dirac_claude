"""W6 draft, part 2 of Revision/pairing/kohn_sham/python/check_t3_completion.py (after patch_check_t3_completion.py;
applied to the copy argv[1]): the zero mode with the hidden scale f, (e^(f M y), 0), and h0 with 1/f (as the Wolfram
twin, patch_verify_t3_completion2.py)."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''    z0 = sp.Matrix([sp.exp(M * y), 0])
    zI = s2 * z0
    h0 = lambda jj, MM, c: jj * (-sp.I * s1 * c.diff(y) + MM * s2 * c)
    zero = sp.zeros(2, 1)
    ok = zI == sp.Matrix([0, sp.I * sp.exp(M * y)])''',
    '''    fs = sp.Symbol("f", positive=True)          # the hidden scale (ks-theory.json blockEquation), constant on a slice
    z0 = sp.Matrix([sp.exp(fs * M * y), 0])
    zI = s2 * z0
    h0 = lambda jj, MM, c: jj * (-sp.I / fs * s1 * c.diff(y) + MM * s2 * c)
    zero = sp.zeros(2, 1)
    ok = zI == sp.Matrix([0, sp.I * sp.exp(fs * M * y)])''')
rep('''    ok = ok and sp.simplify((zI.H * zI)[0, 0] - sp.exp(2 * M * y)) == 0''',
    '''    ok = ok and sp.simplify((zI.H * zI)[0, 0] - sp.exp(2 * fs * M * y)) == 0''')
rep('''    fs = sp.Symbol("f", positive=True)          # the hidden scale (ks-theory.json blockEquation), constant on a slice
    hB = lambda jj, MM, c:''', '''    hB = lambda jj, MM, c:''')
rep('''          "continuation; the zero mode (e^(M y), 0) of (M, j, even, theta = 0) maps to (0, i e^(M y)), a zero mode of "
          "h_(-j)(-M) with the other fold condition (a(0) = 0) and the transformed tip theta = pi (a(-L) = 0), fold-localised "
          "(|chi|^2 = e^(2 M y); with the hidden scale f the profile is e^(2 f M y), the map is the same); control: it violates "
          "the untransformed tip")''',
    '''          "continuation; the zero mode (e^(f M y), 0) of (M, j, fold condition theta = 0, tip theta = 0) (f > 0 the hidden "
          "scale) maps to (0, i e^(f M y)), a zero mode of h_(-j)(-M) with the other fold condition (a(0) = 0) and the "
          "transformed tip theta = pi (a(-L) = 0), fold-localised (|chi|^2 = e^(2 f M y)); control: it violates the "
          "untransformed tip")''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
