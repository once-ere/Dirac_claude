"""W6: Revision/pairing/kohn_sham/python/check_t3.py for the corrected metric (the block Hamiltonian with 1/f, the ODE
chi' = f N chi, the fold conditions instead of the Z2 brane).  Apply in W6 only."""
from pathlib import Path

p = Path(r"D:\Developer\github\Dirac_claude\Revision\pairing\kohn_sham\python\check_t3.py")
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:80])
    t = t.replace(a, b)


rep('''def h_block(j, M, kap, v, chi):
    """h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v  (ks-theory.json blockEquation.hamiltonian)."""
    return j * (-sp.I * s1 * chi.diff(y) + M * s2 * chi + kap * k * s3 * chi) + v * chi''',
    '''def h_block(j, M, kap, v, chi, f=1):
    """h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v  (ks-theory.json blockEquation.hamiltonian)."""
    return j * (-sp.I / f * s1 * chi.diff(y) + M * s2 * chi + kap * k * s3 * chi) + v * chi''')
rep('''    ok_stated = "h_j=j[-isigma1d/dy+M_eff(y)sigma2+kappa(y)ksigma3]+v_v(y)" in stated''',
    '''    ok_stated = "h_j=j[-(i/f)sigma1d/dy+M_eff(y)sigma2+kappaksigma3]+v_v(y)" in stated''')
# the map with a general hidden scale f > 0 (a constant on a slice) and kappa
p_old = '''    for j in (1, -1):
        lhs = h_block(-j, -M, kap, v, s2 * chi)
        rhs = s2 * h_block(j, M, kap, v, chi)
        ok = ok and vzero(lhs - rhs)
    ctl = not vzero(h_block(-1, M, kap, v, s2 * chi) - s2 * h_block(1, M, kap, v, chi))'''
p_new = '''    fs = sp.Symbol("f", positive=True)
    for j in (1, -1):
        lhs = h_block(-j, -M, kap, v, s2 * chi, fs)
        rhs = s2 * h_block(j, M, kap, v, chi, fs)
        ok = ok and vzero(lhs - rhs)
    ctl = not vzero(h_block(-1, M, kap, v, s2 * chi, fs) - s2 * h_block(1, M, kap, v, chi, fs))'''
rep(p_old, p_new)
print("patched (partially; review the remaining texts by hand):", p)
p.write_text(t, encoding="utf-8", newline="\n")
