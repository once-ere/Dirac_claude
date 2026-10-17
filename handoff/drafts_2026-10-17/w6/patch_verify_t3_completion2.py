"""W6 draft, part 2 of verify_t3_completion.wls: the zero mode with the hidden scale f, (E^(f M y), 0) (copy argv[1])."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''zm0 = {E^(MM y), 0}; zmI = s2 . zm0;''', '''zm0 = {E^(fh MM y), 0}; zmI = s2 . zm0;''')
rep('''fillOk = zmI === {0, I E^(MM y)} &&''', '''fillOk = zmI === {0, I E^(fh MM y)} &&''')
rep('''  Simplify[ComplexExpand[Conjugate[zmI] . zmI] - E^(2 MM y), MM > 0 && y \\[Element] Reals] === 0;''',
    '''  Simplify[ComplexExpand[Conjugate[zmI] . zmI] - E^(2 fh MM y), MM > 0 && fh > 0 && y \\[Element] Reals] === 0;''')
rep('''(ii) the k = 0 brane zero mode (E^(M y), 0) of (M, j, even, theta = 0) (h_j = 0, b(0) = 0, b(-L) = 0) goes to (0, I E^(M y)), a zero mode of h_(-j)(-M) with odd parity (a(0) = 0) and the transformed tip theta = Pi (a(-L) = 0), brane-localised like the original (|chi|^2 = E^(2 M y), M > 0), for both j;''',
    '''(ii) the k = 0 fold zero mode (E^(f M y), 0) of (M, j, fold condition theta = 0, tip theta = 0) (h_j = 0, b(0) = 0, b(-L) = 0; f > 0 the hidden scale) goes to (0, I E^(f M y)), a zero mode of h_(-j)(-M) with the other fold condition (a(0) = 0) and the transformed tip theta = Pi (a(-L) = 0), fold-localised like the original (|chi|^2 = E^(2 f M y), M > 0), for both j;''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok")
