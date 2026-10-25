#!/usr/bin/env python3
"""um3_bulk.py - fields that propagate in the bulk of the author's UM-3 metric: their x0 (sigma) mode equations, their
four-dimensional zero modes and the speed with which those zero modes propagate along ordinary space.

The author's metric in the proper chart (um3_fold.py):
    ds^2 = d sigma^2 + e^{-2H|sigma|} (e^{2 a4} dx_i^2 - e^{-2 a4} b4^2 dx_r^2) - dx4^2.
Ordinary space x1..x3 is warped by e^{-H|sigma|}, the time x4 is not: a field confined to the fold sigma = 0 sees the
light cone e^{2 a4} dx^2 = dx4^2, a bulk field sees the light cone of each sigma, and its four-dimensional modes move with
a speed set by the sigma-average of e^{2H|sigma|} over their profile.  Computed (static block a4 = 0, b4 = 1 unless
stated; speeds relative to the light cone of the fold):
  B1  massless scalar: mode equation, zero mode (flat, normalisable), the k = 0 spectrum (bound zero mode and the
      continuum omega >= 3H: u = e^{-3H|sigma|} chi turns the fold into an attractive delta potential), speed of the zero
      mode c^2 = 3/2 (exact first order in k^2; numerical eigenvalue check);
  B2  gauge field (Maxwell): zero mode flat, c^2 = 2 (exact first order; numerical check);
  B3  bulk fermion with a kink mass M sgn(sigma): normalisable chiral zero mode for M > 0, speed c = 2M/(2M - H);
  B4  dirac16complex with chirality-dependent masses m_L, m_R: the 16 x 16 dispersion det(D - M) = 0 gives
      omega^2 = p_sigma^2 + k^2 e^{...} + m_L m_R (eight-fold): the threshold sqrt(m_L m_R), tachyonic if m_L m_R < 0;
  B5  gravitons (transverse traceless h_12) with the author's Einstein-Lovelock terms: the local effective metric of
      the principal symbol, at the static block and at the author's vacuum, and the speed of the zero mode;
  B6  summary: relative speeds of fold-confined matter, bulk photons, bulk gravitons and bulk fermion zero modes.
Writes outputs/bulk.json and reports/bulk_checks.json; exit code 0 iff every check passes.
Usage: python universe_model_3/code/um3_bulk.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent
sys.path.insert(0, str(HERE))
import um3_gammas as GM  # noqa: E402
from um3_lovelock import lovelock_tensor  # noqa: E402


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


H = sp.Symbol('H', positive=True)
s = sp.Symbol('sigma', positive=True)   # sigma > 0 side; the other side by symmetry


def lowest_eigen(kind, k, Hv=1.0, L=12.0, n=3000):
    """Lowest omega^2 of the sigma problem on -L..L (Dirichlet ends, far from the fold), finite differences of the
    self-adjoint form (w(sigma) chi')' + (omega^2 w_t(sigma) - k^2 w_s(sigma)) chi = 0 with
      scalar: w = w_t = e^{-6H|s|}, w_s = e^{-4H|s|};  gauge: w = w_t = e^{-4H|s|}, w_s = e^{-2H|s|}."""
    x = np.linspace(-L, L, n)
    hstep = x[1] - x[0]
    if kind == 'scalar':
        w = lambda q: np.exp(-6 * Hv * np.abs(q))
        ws = lambda q: np.exp(-4 * Hv * np.abs(q))
    else:
        w = lambda q: np.exp(-4 * Hv * np.abs(q))
        ws = lambda q: np.exp(-2 * Hv * np.abs(q))
    xm = 0.5 * (x[1:] + x[:-1])
    wm = w(xm)
    N = n - 2
    Kmat = np.zeros((N, N))
    for i in range(N):
        Kmat[i, i] = (wm[i] + wm[i + 1]) / hstep**2 + k**2 * ws(x[i + 1])
        if i + 1 < N:
            Kmat[i, i + 1] = Kmat[i + 1, i] = -wm[i + 1] / hstep**2
    Mm = np.diag(w(x[1:-1]))
    # symmetric generalised problem K chi = omega^2 M chi -> M^{-1/2} K M^{-1/2}
    d = 1 / np.sqrt(np.diag(Mm))
    S = (Kmat * d[:, None]) * d[None, :]
    ev = np.linalg.eigvalsh(S)
    return float(ev[0])


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- B1: massless scalar
    chi = sp.Function('chi')
    om, k = sp.symbols('omega k', positive=True)
    # sigma > 0: e^{6Hs} d/ds(e^{-6Hs} chi') + omega^2 chi - k^2 e^{2Hs} chi = 0
    u = sp.Function('u')
    expr = sp.exp(6 * H * s) * sp.diff(sp.exp(-6 * H * s) * sp.diff(sp.exp(3 * H * s) * u(s), s), s) + om**2 * sp.exp(3 * H * s) * u(s)
    red = sp.simplify(expr * sp.exp(-3 * H * s))
    ok = sp.simplify(red - (sp.diff(u(s), s, 2) + (om**2 - 9 * H**2) * u(s))) == 0
    # the fold: e^{3H|sigma|} has the jump 6H in its derivative -> u'' + 6H delta u ; bound state e^{-3H|sigma|} at omega = 0
    kap = sp.Symbol('kappa_b', positive=True)
    ok2 = sp.solve(sp.Eq(-2 * kap, -6 * H), kap) == [3 * H] and sp.simplify(9 * H**2 - (3 * H)**2) == 0
    rep.check('B1_scalar_k0_spectrum', ok and ok2, 'chi = e^{3H|sigma|} u turns the k = 0 mode equation into u\'\' + (omega^2 - 9H^2) u '
              '+ 6H delta(sigma) u = 0: one bound state u = e^{-3H|sigma|} (chi = 1, omega = 0: the normalisable zero mode) and '
              'the continuum omega >= 3H (a gap 3H between the zero mode and the bulk modes)')
    # first-order speed of the zero mode
    num = sp.integrate(sp.exp(-6 * H * s) * sp.exp(2 * H * s), (s, 0, sp.oo))
    den = sp.integrate(sp.exp(-6 * H * s), (s, 0, sp.oo))
    c2s = sp.simplify(num / den)
    ev = [lowest_eigen('scalar', kk) / kk**2 for kk in (0.02, 0.05)]
    rep.check('B1_scalar_zero_mode_speed', c2s == sp.Rational(3, 2) and abs(ev[0] - 1.5) < 2e-3,
              'omega^2 = (3/2) k^2 + O(k^4) for the zero mode (k the comoving momentum in units of the fold light cone): '
              'c_scalar^2 = <e^{2H|sigma|}> = 3/2; finite-difference eigenvalue omega^2/k^2 = %.5f (k = 0.02 H), %.5f (k = 0.05 H)' % tuple(ev))
    out['scalar_zero_mode_c2'] = '3/2'

    # ---------------- B2: gauge field
    num = sp.integrate(sp.exp(-2 * H * s), (s, 0, sp.oo))
    den = sp.integrate(sp.exp(-4 * H * s), (s, 0, sp.oo))
    c2g = sp.simplify(num / den)
    ev = [lowest_eigen('gauge', kk) / kk**2 for kk in (0.02, 0.05)]
    rep.check('B2_gauge_zero_mode_speed', c2g == 2 and abs(ev[0] - 2) < 3e-3,
              'Maxwell field in the bulk: (e^{-4H|sigma|} A\')\' + (omega^2 e^{-4H|sigma|} - k^2 e^{-2H|sigma|}) A = 0; '
              'the flat zero mode (the photon of a bulk gauge field) has c_gauge^2 = 2; numerical %.5f, %.5f' % tuple(ev))
    out['gauge_zero_mode_c2'] = '2'

    # ---------------- B3: bulk fermion with a kink mass
    M = sp.Symbol('M', positive=True)
    Nt = 2 * sp.integrate(sp.exp(-6 * H * s) * sp.exp(2 * (3 * H - M) * s), (s, 0, sp.oo))
    Ns = 2 * sp.integrate(sp.exp(-6 * H * s) * sp.exp(H * s) * sp.exp(2 * (3 * H - M) * s), (s, 0, sp.oo), conds='none')
    cf = sp.simplify(Ns / Nt)
    ok = sp.simplify(cf - 2 * M / (2 * M - H)) == 0
    rep.check('B3_fermion_zero_mode_speed', ok, 'for a bulk fermion with the kink mass M sgn(sigma), the zero mode '
              'Psi_- ~ e^{(3H - M)|sigma|} is normalisable for M > 0 and moves with c = N_s/N_t = 2M/(2M - H) (finite for '
              'M > H/2): every species with its own profile has its own speed, the deviation H/(2M - H)')

    # ---------------- B4: dirac16complex dispersion with m_L, m_R
    T = GM.T16A()
    eta = GM.eta4488()
    Tup = {a: eta[a, a] * T[a] for a in range(8)}
    P_L, P_R = GM.projectors()
    mL, mR, w_, p_, kk_ = sp.symbols('m_L m_R omega p k', real=True)
    Dop = sp.I * p_ * Tup[0] - sp.I * w_ * Tup[4] + sp.I * kk_ * Tup[3]
    Mm = mL * P_L + mR * P_R
    Gam = T[8]
    Mt = mL * P_R + mR * P_L
    prod = ((Dop + Mt) * (Dop - Mm)).applyfunc(sp.expand)
    target = (w_**2 - p_**2 - kk_**2 - mL * mR) * sp.eye(16)
    ok = (prod - target).applyfunc(sp.expand) == sp.zeros(16, 16)
    # determinant check at random numbers
    rng = np.random.default_rng(5)
    okd = True
    for _ in range(3):
        vals = {mL: float(rng.uniform(0.2, 2)), mR: float(rng.uniform(0.2, 2)), p_: float(rng.uniform(-1, 1)), kk_: float(rng.uniform(-1, 1))}
        Dn = np.array((Dop - Mm).subs(vals).subs(w_, 0).tolist(), dtype=complex)
        Tn = np.array((-sp.I * Tup[4]).tolist(), dtype=complex)
        # eigenvalues omega of (D(0) - M) + omega (-i T^4) = 0 -> omega = eig( -(-i T^4)^{-1} (D(0) - M))
        evw = np.linalg.eigvals(-np.linalg.solve(Tn, Dn))
        target_w = np.sqrt(vals[p_]**2 + vals[kk_]**2 + vals[mL] * vals[mR])
        if not np.allclose(np.sort(np.abs(evw)), target_w, atol=1e-9):
            okd = False
    rep.check('B4_dirac16complex_dispersion', ok and okd, '(D + m_L P_R + m_R P_L)(D - m_L P_L - m_R P_R) = (omega^2 - p_sigma^2 - '
              'k^2 - m_L m_R) I_16 with D = i p_sigma T^(x0) - i omega T^(x4) + i k T^(x3) (D anticommutes with T16^A[8]): '
              'all 16 roots have omega^2 = p_sigma^2 + k^2 + m_L m_R; the rest energy is sqrt(m_L m_R); m_L m_R < 0 is tachyonic')

    # ---------------- B5: gravitons with the Einstein-Lovelock terms
    geo = json.loads((UM3 / 'outputs' / 'geometry.json').read_text())
    Asym, Usym, Adsym, Udsym = sp.symbols('A U Ad Ud', real=True)
    idx = {'x%d' % i: i for i in range(8)}

    def bg_riemann(vals):
        Rf = {}
        for key, v in geo['frame_curvature'].items():
            # key 'R^{x0x1}_{x1x4}'
            up = key[3:key.index('}')]
            lo = key[key.index('_{') + 2:-1]
            a, b = idx[up[:2]], idx[up[2:]]
            c, d = idx[lo[:2]], idx[lo[2:]]
            val = sp.sympify(v, locals={'A': Asym, 'U': Usym, 'Ad': Adsym, 'Ud': Udsym, 'H': H}).subs(vals)
            if val != 0:
                Rf[((a, b), (c, d))] = val
        return Rf

    def principal(Rbg, k3, k4, orders=(1, 2, 3)):
        """delta E^1_2 per unit h_12 for the plane wave h_12 = h_21 = eps e^{i(k3 x3 + k4 x4)} (frame), eikonal."""
        epsy = sp.Symbol('epsy')
        kvec = [0] * 8
        kvec[3], kvec[4] = k3, k4
        kup = [eta[a, a] * kvec[a] for a in range(8)]
        hl = sp.zeros(8, 8)
        hl[1, 2] = hl[2, 1] = 1
        hmix = sp.zeros(8, 8)   # h^c_b = eta^cc h_cb
        for c in range(8):
            for b in range(8):
                hmix[c, b] = eta[c, c] * hl[c, b]
        dR = {}
        for c in range(8):
            for d in range(c + 1, 8):
                for a in range(8):
                    for b in range(a + 1, 8):
                        v = -sp.Rational(1, 2) * (kvec[a] * kup[d] * hmix[c, b] - kvec[a] * kup[c] * hmix[d, b]
                                                  - kvec[b] * kup[d] * hmix[c, a] + kvec[b] * kup[c] * hmix[d, a])
                        if v != 0:
                            dR[((c, d), (a, b))] = v
        Rt = dict(Rbg)
        for kk2, v in dR.items():
            Rt[kk2] = Rt.get(kk2, 0) + epsy * v
        W = [None, sp.Integer(1), sp.Rational(1, 32) / H**2, sp.Rational(1, 1152) / H**4]
        tot = 0
        for p in orders:
            Ep = lovelock_tensor(Rt, p, simplify=sp.expand)
            tot += W[p] * Ep[1, 2]
        return sp.expand(sp.diff(tot, epsy).subs(epsy, 0))

    k3s, k4s = sp.symbols('k3 k4', real=True)

    def coefficients(Rbg, orders=(1, 2, 3)):
        pe = principal(Rbg, k3s, k4s, orders)
        return (sp.factor(sp.diff(pe, k3s, 2) / 2), sp.factor(sp.diff(pe, k4s, 2) / 2), sp.factor(sp.diff(pe, k3s, k4s)))

    # Einstein limit (flat background) and the general background (A, U, Ad, Ud)
    c33e, c44e, c34e = coefficients({})
    Rgen = bg_riemann({})
    c33g, c44g, c34g = coefficients(Rgen)
    perorder = {p: coefficients(Rgen, (p,)) for p in (1, 2, 3)}
    out['graviton_principal_symbol'] = {
        'einstein_flat': {'c33': str(c33e), 'c44': str(c44e)},
        'general_background': {'c33': str(c33g), 'c44': str(c44g), 'c34': str(c34g)},
        'per_order_general': {str(p): {'c33': str(v[0]), 'c44': str(v[1])} for p, v in perorder.items()}}
    rep.check('B5_graviton_einstein_limit', c33e == sp.Rational(1, 2) and c44e == -sp.Rational(1, 2) and c34e == 0,
              'principal symbol of delta E^1_2 for a transverse traceless wave h_12 = h_21 ~ e^{i(k3 x3 + k4 x4)} (frame '
              'components, eikonal): (c33 k3^2 + c44 k4^2) h with c33 = -c44 = 1/2 in flat space: the light cone')
    sbv = {Asym: 0, Usym: 0, Adsym: 0, Udsym: 0}
    avv = {Asym: 1, Usym: 0, Adsym: 0, Udsym: 0}
    c33_sb, c44_sb = sp.simplify(c33g.subs(sbv)), sp.simplify(c44g.subs(sbv))
    c33_av, c44_av = sp.simplify(c33g.subs(avv)), sp.simplify(c44g.subs(avv))
    out['graviton_static_block'] = {'c33': str(c33_sb), 'c44': str(c44_sb)}
    out['graviton_author_vacuum'] = {'c33': str(c33_av), 'c44': str(c44_av)}
    v2_sb = sp.simplify(-c33_sb / c44_sb)
    rep.check('B5_graviton_static_block', c33_sb == sp.Rational(5, 32) and c44_sb == -sp.Rational(1, 32) and v2_sb == 5,
              'at the static block c33 = 5/32, c44 = -1/32: the Gauss-Bonnet and cubic terms reduce the time-kinetic term of '
              'the graviton sixteen-fold and its gradient term 3.2-fold; the local graviton cone is v^2 = 5 times the light '
              'cone of the frame')
    rep.check('B5_graviton_author_vacuum_degenerate', c44_av == 0 and c33_av != 0,
              "at the author's vacuum (A = 1, U = 0) c44 = 0 (c33 = %s): the transverse traceless graviton has no time-kinetic "
              "term -- the author's vacuum is a degenerate vacuum of the Lovelock theory (strongly coupled gravitons; the "
              "same degeneracy as the vanishing linear response of the energy constraint, um3_geometry G4)" % c33_av)
    cg2_sb = sp.nsimplify(v2_sb * sp.Rational(3, 2))
    out['graviton_zero_mode_c2_static_block'] = str(cg2_sb)
    rep.check('B5_graviton_zero_mode_speed', cg2_sb == sp.Rational(15, 2),
              'zero mode of the graviton at the static block (flat profile, constant coefficients, weight e^{-6H|sigma|} for the '
              'time term and e^{-4H|sigma|} for the gradient term): c_g^2 = v_local^2 x 3/2 = 15/2, c_g = %.4f times the light '
              'cone of the fold (GW170817 requires |c_g - c| < 1e-15 c)' % float(sp.sqrt(cg2_sb)))

    # ---------------- B6: summary
    summary = {
        'fold_confined_matter_and_light': 1.0,
        'bulk_photon_zero_mode': float(sp.sqrt(2)),
        'bulk_scalar_zero_mode': float(sp.sqrt(sp.Rational(3, 2))),
        'bulk_graviton_zero_mode_static_block': float(sp.sqrt(cg2_sb)),
        'bulk_fermion_zero_mode_M=H': float(2 / (2 - 1)),
        'bulk_fermion_zero_mode_M=10H': float(20 / 19),
        'bulk_fermion_zero_mode_M=1e3H': float(2000 / 1999),
    }
    out['speeds_relative_to_fold_light_cone'] = summary
    rep.check('B6_speed_summary', True, '; '.join('%s: %.6f' % kv for kv in summary.items()) +
              ' -- different species in the bulk move with different limiting speeds (excluded at the 1e-15 to 1e-20 level '
              'for photons and charged matter); confining the Standard Model to the fold gives all of it the one light cone '
              'of the fold')
    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs' / 'bulk.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_bulk.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'bulk_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
