"""W6 draft: Revision/pairing/kohn_sham/numerics/t3_reference_demo.py, the general-tip sector arrays for the corrected
metric (kappa = e^{-a4} constant in y, the hidden scale f: 1/f on d_y and phi'), as ks_fd.sector_arrays.  argv[1]: the copy."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''    a4 = phys.a4 if a4 is None else a4
    kap = np.exp(-phys.H * grid.y - a4)
    Kk = kap[:, None] * sec.kmag(phys.dk)[None, :]''', '''    a4 = phys.a4 if a4 is None else a4
    finv = 1.0 / phys.fh_at(a4)                 # the hidden scale f (ks_fd.Phys.fh_at): 1/f on d_y and on phi'
    kap = math.exp(-a4)                         # kappa = e^{-a4}, constant in y (the corrected metric)
    Kk = np.full((grid.n, 1), kap) * sec.kmag(phys.dk)[None, :]''')
rep('''    phig, dphi = frame(grid.y, phys.L, sec.odd, sec.j, tip_pi)
    phi = j * phig''', '''    phig, dphi = frame(grid.y, phys.L, sec.odd, sec.j, tip_pi)
    dphi = dphi * finv
    phi = j * phig''')
rep('''    beta = j * (grid.bs[:, None] + 0.5 * m2[grid.bu, :])
    return alpha, beta''', '''    beta = j * (grid.bs[:, None] * finv + 0.5 * m2[grid.bu, :])
    return alpha, beta''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok (numerics; the texts are done in W6)")
