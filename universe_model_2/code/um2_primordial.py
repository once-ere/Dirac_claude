#!/usr/bin/env python3
"""UM-2 primordial era: the full nonlinear homogeneous Einstein-Lovelock equations (author's weights, Lambda = -10 H^2)
with the block stabiliser (kappa rho_b = R* (k/k*)^4, p3 = -rho_b, p0 = p_t = rho_b) and radiation of zero modes
(kappa rho_r ~ e^{-4 a4} f^{-4}, p3 = rho_r/3, p0 = 0), integrated from deflating initial blocks.

State (a4, A = a4', h = f'/f, ln k), k = 1/f^2: the x1 and x0 components give A' and h' (linear), k' = -2 k h; the x4
component is the constraint (preserved by the Bianchi identity; monitored).  Units H = 1.
Results (checked):
  R1  the constraint residual stays below 1e-7 along every solution;
  R2  basin: blocks that start smaller than the unstable static root k_- = 12 - (4/3) sqrt(51) = 2.478 (k0 > k_-) deflate into
      the stable static block k* = 12 + (4/3) sqrt(51) and stay there; larger blocks (k0 < k_-) run into a curvature
      singularity in a time of order 1/H;
  R3  near k* the block oscillates with the radion frequency omega = 3.387 H; the oscillation energy redshifts like dust,
      the mean 3-space rate falls like 2/(3 x4) (radion-dominated expansion);
  R4  the deflation factor of the extra times (and of x0): f(k0)/f* = (k*/k0)^{1/2}, at most (k*/k_-)^{1/2} = 2.947.
Writes outputs/primordial.json, figures/fig_primordial_*.png, reports/primordial-checks.json.
"""
import math
import os
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_background import A, AUTHOR, Ad, H, Lam, classes, h, hd, k, lovelock, w2, w3  # noqa: E402
from um2_common import FIG, OUT, Report, read_json, write_json  # noqa: E402

KSTAR = 12 + sp.Rational(4, 3) * sp.sqrt(51)
KMINUS = 12 - sp.Rational(4, 3) * sp.sqrt(51)
RSTAR = 26 + 4 * sp.sqrt(51)


def build():
    K = classes()
    E = {kk: {hh: lovelock(K, kk, hh) for hh in (0, 1, 4)} for kk in (1, 2, 3)}
    al = {1: 1, 2: w2 / H ** 2, 3: w3 / H ** 4}
    LHS = {hh: sp.expand(sum(al[kk] * E[kk][hh] for kk in (1, 2, 3)) + Lam) for hh in (0, 1, 4)}
    R, rr = sp.symbols('R rr')
    sub = dict(AUTHOR)
    sub[Lam] = -10
    sub[H] = 1
    c4 = sp.expand((LHS[4] + R + rr).subs(sub))
    c1 = sp.expand((LHS[1] - (-R + rr / 3)).subs(sub))
    c0 = sp.expand((LHS[0] - R).subs(sub))
    sol = sp.solve([c1, c0], [Ad, hd], dict=True)[0]
    Rk = RSTAR * (k / KSTAR) ** 4
    fA = sp.lambdify((A, h, k, rr), sol[Ad].subs(R, Rk), 'math')
    fh = sp.lambdify((A, h, k, rr), sol[hd].subs(R, Rk), 'math')
    con = sp.lambdify((A, h, k, rr), c4.subs(R, Rk), 'math')
    cpoly = c4.subs(R, Rk)
    return fA, fh, con, cpoly, rr


def initial_A(cpoly, rr, k0, h0, rr0):
    poly = sp.Poly(sp.expand(cpoly.subs({k: k0, h: h0, rr: rr0})), A)
    rts = [complex(x) for x in sp.nroots(poly, n=30, maxsteps=200)]
    pos = [r.real for r in rts if abs(r.imag) < 1e-10 and r.real > 0]
    return max(pos) if pos else None


def main():
    rep = Report('primordial-checks', 'UM-2: nonlinear primordial evolution of the block with the author\'s weights and Lambda: '
                 'deflation into the stabilised block, basin, radion oscillation, constraint preservation')
    fA, fh, con, cpoly, rr = build()
    ks = float(KSTAR)
    km = float(KMINUS)

    def rhs(t, Y, rr0):
        a, Av, hv, lk = Y
        kv = math.exp(lk)
        rrv = rr0 * math.exp(-4 * a) * (kv / ks) ** 2
        return [Av, fA(Av, hv, kv, rrv), fh(Av, hv, kv, rrv), -2 * hv]

    def blow(t, Y, rr0):
        return abs(Y[1]) + abs(Y[2]) - 1e3
    blow.terminal = True
    out = {'k_star': ks, 'k_minus': km, 'R_star': float(RSTAR)}
    runs = {}
    dense = {}
    key_of = lambda k0, h0, rr0: 'k0=%g,h0=%.4f,rr0=%g' % (k0, h0, rr0)
    maxres = 0.0
    for (k0, h0, rr0) in [(3.0, -1 / 3, 0.0), (5.0, -1 / 3, 0.0), (10.0, -1 / 3, 0.0), (5.0, -1 / 3, 10.0)]:
        A0 = initial_A(cpoly, rr, k0, h0, rr0 * (k0 / ks) ** 2)
        sol = solve_ivp(rhs, [0, 120], [0, A0, h0, math.log(k0)], args=(rr0,), rtol=1e-11, atol=1e-13, method='DOP853',
                        events=blow, dense_output=True, max_step=0.05)
        tt = sol.t
        kk = np.exp(sol.y[3])
        res = max(abs(con(sol.y[1][i], sol.y[2][i], kk[i], rr0 * math.exp(-4 * sol.y[0][i]) * (kk[i] / ks) ** 2)) for i in range(len(tt)))
        maxres = max(maxres, res)
        # oscillation frequency from the zero crossings of k - k* after x4 = 30
        dk = kk - ks
        mask = tt > 30
        zc = [tt[i] for i in range(1, len(tt)) if mask[i] and dk[i - 1] * dk[i] < 0]
        omega = math.pi / np.mean(np.diff(zc)) if len(zc) > 3 else float('nan')
        # mean expansion rate on the last 40 units versus 2/(3 x4) (radion dust domination): fit A_mean * x4
        late = tt > 80
        Amean = float(np.trapezoid(sol.y[1][late], tt[late]) / (tt[late][-1] - tt[late][0]))
        xmid = 0.5 * (tt[late][0] + tt[late][-1])
        runs[key_of(k0, h0, rr0)] = {
            'A0': A0, 'status': int(sol.status), 't_end': float(tt[-1]), 'k_end': float(kk[-1]), 'constraint_max_residual': res,
            'omega_from_zero_crossings': omega, 'A_mean_late': Amean, 'A_mean_late_times_x4': Amean * xmid,
            'deflation_factor_f0_over_fstar': math.sqrt(ks / k0),
            'samples': [[float(t), float(a), float(Av), float(hv), float(math.exp(lk))] for t, (a, Av, hv, lk) in
                        zip(np.linspace(0, 40, 401), sol.sol(np.linspace(0, 40, 401)).T)]}
        dense[key_of(k0, h0, rr0)] = sol
    out['runs'] = runs
    rep.check('constraint_preserved', maxres < 1e-7, 'the x4 constraint stays satisfied along every integrated solution (max residual %.1e)' % maxres)
    r5 = runs['k0=5,h0=-0.3333,rr0=0']
    bg = read_json(os.path.join(OUT, 'background.json'))
    om = bg['radion_frequency_over_H']
    rep.check('radion_oscillation', abs(r5['omega_from_zero_crossings'] - om) / om < 0.01,
              'after deflating from k0 = 5 at h = -H/3 the block oscillates about k* with omega = %.4f H (linear radion frequency %.4f H)' % (
                  r5['omega_from_zero_crossings'], om))
    rep.check('radion_dust_expansion', 0.55 < r5['A_mean_late_times_x4'] < 0.8,
              'the mean 3-space rate on x4 in [80, 120] times x4 is %.3f (2/3 for a dust-dominated expansion: the radion oscillation '
              'energy redshifts like matter)' % r5['A_mean_late_times_x4'])
    # basin scan
    basin = []
    for k0 in [1.5, 2.0, 2.3, km * 0.99, km * 1.01, 2.7, 3.0, 4.0, 6.0, 10.0, 15.0, 20.0]:
        row = {'k0': k0}
        for h0 in (-0.5, -1 / 3, -0.1, 0.0):
            A0 = initial_A(cpoly, rr, k0, h0, 0.0)
            if A0 is None:
                row['h0=%.3f' % h0] = 'no expanding root'
                continue
            sol = solve_ivp(rhs, [0, 60], [0, A0, h0, math.log(k0)], args=(0.0,), rtol=1e-10, atol=1e-12, method='DOP853', events=blow)
            if sol.status != 0:
                row['h0=%.3f' % h0] = 'singular at x4 = %.2f' % sol.t[-1]
            else:
                row['h0=%.3f' % h0] = 'k(60) = %.3f' % math.exp(sol.y[3][-1])
        basin.append(row)
    out['basin'] = basin
    # the separatrix: bisection in k0 for each deflating h0 (attracted = no singularity before x4 = 60 and k(60) near k*)
    def attracted_from(k0, h0):
        A0 = initial_A(cpoly, rr, k0, h0, 0.0)
        if A0 is None:
            return None
        sol = solve_ivp(rhs, [0, 60], [0, A0, h0, math.log(k0)], args=(0.0,), rtol=1e-10, atol=1e-12, method='DOP853', events=blow)
        return sol.status == 0 and abs(math.exp(sol.y[3][-1]) - ks) < 1.0
    thresholds = {}
    for h0 in (-0.5, -1 / 3, -0.1):
        lo, hi = 2.3, 3.0          # lo singular, hi attracted (from the scan)
        if attracted_from(lo, h0) or not attracted_from(hi, h0):
            thresholds['%.4f' % h0] = None
            continue
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            r = attracted_from(mid, h0)
            if r:
                hi = mid
            else:
                lo = mid
        thresholds['%.4f' % h0] = 0.5 * (lo + hi)
    out['separatrix_k0'] = thresholds
    th = [v for v in thresholds.values() if v is not None]
    monotone = all(('k(60)' in v) for r in basin if r['k0'] >= max(th) for kk_, v in r.items() if kk_ != 'k0' and v != 'no expanding root') and \
        all(('singular' in v) for r in basin if r['k0'] <= min(th) for kk_, v in r.items() if kk_ != 'k0' and v != 'no expanding root')
    rep.check('basin_separatrix', len(th) == 3 and monotone and all(km < v < 2.8 for v in th),
              'expanding, deflating starts (h0 = -1/2, -1/3, -1/10) end at the stable block k* = %.4f when k0 exceeds a threshold k_c(h0) = %s '
              'and become singular within x4 ~ 1/H below it; k_c lies just above the unstable static block k_- = %.4f (its stable manifold '
              'is the separatrix)' % (ks, ', '.join('%.4f' % v for v in th), km))
    fmax = math.sqrt(ks / min(th))
    rep.check('deflation_factor', 2.7 < fmax < math.sqrt(ks / km),
              'the largest deflation of the extra times (and of x0) into the stable block is f(k_c)/f* = (k*/k_c)^{1/2} = %.4f '
              '(bounded by (k*/k_-)^{1/2} = %.4f)' % (fmax, math.sqrt(ks / km)))
    out['max_deflation_factor'] = fmax
    # figures
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(1, 3, figsize=(13, 3.8))
    tf = np.linspace(0, 40, 4001)
    for key, sol in dense.items():
        yv = sol.sol(tf)
        lab = key.replace('h0=-0.3333', 'h0=-H/3').replace(',rr0=0', '').replace(',rr0=10', ', with radiation')
        ls = '--' if 'rr0=10' in key else '-'
        axs[0].plot(tf, np.exp(-0.5 * yv[3]), ls, lw=1.0, label=lab)
        axs[1].plot(tf, yv[1], ls, lw=1.0, label=lab)
        axs[2].plot(tf, yv[2], ls, lw=1.0, label=lab)
    axs[0].axhline(1 / math.sqrt(ks), color='k', lw=0.6, ls='--')
    axs[0].set_xlabel('$x_4$ [1/H]'); axs[0].set_ylabel('block scale $f = k^{-1/2}$'); axs[0].set_title('deflation of $x_0, x_5, x_6, x_7$')
    axs[1].set_xlabel('$x_4$ [1/H]'); axs[1].set_ylabel('$A = a_4\'$ [H]'); axs[1].set_title('3-space expansion rate')
    axs[2].set_xlabel('$x_4$ [1/H]'); axs[2].set_ylabel('$h = f\'/f$ [H]'); axs[2].set_title('block rate')
    axs[0].legend(fontsize=7)
    for ax in axs:
        ax.set_xlim(0, 40)
    axs[1].set_ylim(-0.05, 0.6)
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, 'fig_primordial_history.png'), dpi=130)
    plt.close(fig)
    write_json(os.path.join(OUT, 'primordial.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
