"""W6 draft: Revision/pairing/kohn_sham/python/check_t3.py for the corrected metric, applied to a COPY given as argv[1]:
the block Hamiltonian with 1/f, the ODE chi' = f N chi, the fold conditions instead of the Z2 brane, the mirror check
removed (the corrected metric has no mirror copy: ks-theory.json boundaryConditions.fold), texts."""
import sys
from pathlib import Path

p = Path(sys.argv[1])
t = p.read_text(encoding="utf-8")


def rep(a, b, n=1):
    global t
    assert t.count(a) == n, (t.count(a), a[:90])
    t = t.replace(a, b)


rep('''T3: the block map (chi, j) -> (sigma2 chi, -j) at the same momentum (the chirality Gamma of the 16-component
orbital in the block basis of Revision/kohn_sham/ks-theory.json), together with the transformed boundary
conditions (brane parities exchanged, tip angle theta -> pi - theta), maps every self-consistent instantaneous''',
    '''T3: the block map (chi, j) -> (sigma2 chi, -j) at the same momentum (the chirality Gamma of the 16-component
orbital in the block basis of Revision/kohn_sham/ks-theory.json), together with the transformed boundary
conditions (the two fold conditions exchanged, tip angle theta -> pi - theta), maps every self-consistent instantaneous''')
rep('''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln(sin z)/(6 H) in [-L, 0], z = 6 H x0''' + " " + '''
(brane y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra times.
The metric is the author's metric with b4(x4) (SPEC section 1; b4 is never 1); b4 does not enter the block
Hamiltonians h_j (ks-theory.json sectorAndAnsatz.instantaneousProblem), so T3 holds slice by slice for every b4.''',
    '''The author's coordinates {x0, x1, ..., x7}: x0 = hidden direction, y = ln|sin z|/(6 H) in [-L, 0], z = 6 H x0 real
(the fold cos z = 0 at y = 0, tip y = -L); x1, x2, x3 = 3-space; x4 = time; x5, x6, x7 = the exponentially DEFLATING extra
times.  The metric is the corrected primordial metric of 2026-10-16 (version 2; SPEC section 1): a4 and b4 enter the
block Hamiltonians h_j only through the hidden scale f = e^{-a4} b4^{1/2} and kappa = e^{-a4}, positive constants on a
slice (ks-theory.json blockEquation), so T3 holds slice by slice for every a4, b4.''')
rep('''def h_block(j, M, kap, v, chi):
    """h_j = j[-i sigma1 d_y + M sigma2 + kappa k sigma3] + v  (ks-theory.json blockEquation.hamiltonian)."""
    return j * (-sp.I * s1 * chi.diff(y) + M * s2 * chi + kap * k * s3 * chi) + v * chi''',
    '''def h_block(j, M, kap, v, chi, f=1):
    """h_j = j[-(i/f) sigma1 d_y + M sigma2 + kappa k sigma3] + v  (ks-theory.json blockEquation.hamiltonian)."""
    return j * (-sp.I / f * s1 * chi.diff(y) + M * s2 * chi + kap * k * s3 * chi) + v * chi''')
rep('''    ok_stated = "h_j=j[-isigma1d/dy+M_eff(y)sigma2+kappa(y)ksigma3]+v_v(y)" in stated''',
    '''    ok_stated = "h_j=j[-(i/f)sigma1d/dy+M_eff(y)sigma2+kappaksigma3]+v_v(y)" in stated''')
rep('''    for j in (1, -1):
        lhs = h_block(-j, -M, kap, v, s2 * chi)
        rhs = s2 * h_block(j, M, kap, v, chi)
        ok = ok and vzero(lhs - rhs)
    ctl = not vzero(h_block(-1, M, kap, v, s2 * chi) - s2 * h_block(1, M, kap, v, chi))''',
    '''    fs = sp.Symbol("f", positive=True)          # the hidden scale, a positive constant on a slice
    for j in (1, -1):
        lhs = h_block(-j, -M, kap, v, s2 * chi, fs)
        rhs = s2 * h_block(j, M, kap, v, chi, fs)
        ok = ok and vzero(lhs - rhs)
    ctl = not vzero(h_block(-1, M, kap, v, s2 * chi, fs) - s2 * h_block(1, M, kap, v, chi, fs))''')
rep('''          "with the block Hamiltonian of ks-theory.json blockEquation (h_j = j[-i sigma1 d_y + M_eff sigma2 + kappa k "
          "sigma3] + v_v, stated there and re-typed here), general M(y), kappa(y), v(y), k: h_(-j)(-M) (sigma2 chi) = "''',
    '''          "with the block Hamiltonian of ks-theory.json blockEquation (h_j = j[-(i/f) sigma1 d_y + M_eff sigma2 + kappa k "
          "sigma3] + v_v, stated there and re-typed here), general M(y), kappa(y), v(y), k and hidden scale f > 0: h_(-j)(-M) (sigma2 chi) = "''')
p.write_text(t, encoding="utf-8", newline="\n")
print("ok (part 1)")
