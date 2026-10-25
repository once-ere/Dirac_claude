#!/usr/bin/env python3
"""um3_series.py - the first-order terms of the power series of the metric (FE-35) around the static block, and the
consequences of the junction conditions for the cosmology of the fold (SOLUTION.md; corrects the text of FE-59).

The general warped metric FE-34, ds^2 = d sigma^2 + e^{2 fa} dx_i^2 - e^{2 fn} dx4^2 - e^{2 fb} dx_r^2, is expanded around
the static block fa = fb = -H|sigma|, fn = 0 (a4 = 0, b4 = 1 normalised):
    fa = -H|sigma| + eps alpha(sigma),  fb = -H|sigma| + eps beta(sigma),  fn = eps nu(sigma)    (static).
Inputs: the exact left-hand side of FE-1 and the junction potential of FE-4 for the general metric (outputs/fold.json of
um3_fold.py).  Computed and checked:
  SR1  the linearised static bulk operator (sigma > 0; the mirror image for sigma < 0): four equations for alpha', beta',
       nu' with constant coefficients;
  SR2  its homogeneous solutions when the bulk medium does not respond (delta T = 0): the only non-trivial solution is the
       difference mode alpha' = -beta' ~ e^{6H|sigma|}, which grows away from the fold; there is no bounded static correction;
  SR3  the linearised junction conditions: the jumps [alpha'], [beta'], [nu'] at the fold give kappa delta S, from the
       junction potential and, independently, from the coefficients of the second derivatives; the combination
       ([alpha'], [beta'], [nu']) = (1, -1, 5) changes only the extra-time component (a radion mode);
  SR4  with the induced gravity of the fold (IN-9), to leading order in eps_r: the (4,4) and (i,i) components are the
       Friedmann and acceleration equations of general relativity; the extra-time (r,r) component is an additional
       equation, q_tot = -R_hat/(2 kappa4), i.e. sum over the matter of (q + (rho - 3p)/2) = 0 (the radion condition);
       radiation satisfies it, non-relativistic matter and vacuum energy do not;
  SR5  if the bulk medium does not respond, the difference mode must absorb the extra-time mismatch and the acceleration
       equation becomes 5 H4' + 9 H4^2 = -kappa4 (p + q): radiation still expands as t^{1/2}, but dust expands as t^{5/6}
       (q = -rho) or t^{5/9} (q = 0) and vacuum energy gives H4' = -(3/5) H4^2: excluded by observation;
  SR6  with a responding bulk medium (the radion mode of SR3) the four-dimensional equations stay those of general
       relativity; the amplitude of the response today, in units of H, is (8/5)(3 A^2 Delta/rho_c)/eps_r with
       Delta = sum(q + (rho - 3p)/2); it is a small correction of the power series if A^2 << eps_r.
Writes outputs/series.json and reports/series_checks.json.
Usage: python universe_model_3/code/um3_series.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

H = sp.Symbol('H', positive=True)
eps = sp.Symbol('eps')
NAMES = ['fa_s', 'fa_ss', 'fa_st', 'fa_t', 'fa_tt', 'fb_s', 'fb_ss', 'fb_st', 'fb_t', 'fb_tt', 'fn_s', 'fn_ss', 'fn_st',
         'fn_t', 'fn_tt', 'fn0']
SY = {n: sp.Symbol(n, real=True) for n in NAMES}
a1, a2, b1, b2, n1, n2, n0 = sp.symbols('a1 a2 b1 b2 n1 n2 n0', real=True)


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def static_sub(side):
    """Static perturbation of the static block on one side (side = +1: sigma > 0, fa_s = -H + eps a1)."""
    s = {SY['fa_s']: -H * side + eps * a1, SY['fa_ss']: eps * a2, SY['fb_s']: -H * side + eps * b1, SY['fb_ss']: eps * b2,
         SY['fn_s']: eps * n1, SY['fn_ss']: eps * n2, SY['fn0']: eps * n0}
    for k in ('fa_st', 'fa_t', 'fa_tt', 'fb_st', 'fb_t', 'fb_tt', 'fn_st', 'fn_t', 'fn_tt'):
        s[SY[k]] = 0
    return s


def main():
    t0 = time.time()
    rep = Report()
    out = {}
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())
    loc = dict(SY, H=H)
    L = {k: sp.sympify(v, locals=loc) for k, v in fold['lhs_general'].items()}
    F = {k: sp.sympify(v, locals=loc) for k, v in fold['junction_potential'].items()}
    comps = [('sigma', 'x0,x0'), ('space', 'x1,x1'), ('time', 'x4,x4'), ('extra', 'x5,x5')]

    # ---------------- SR1: linearised static operator
    lin, zero = {}, {}
    for side in (+1, -1):
        sub = static_sub(side)
        for nm, k in comps:
            e = L[k].subs(sub)
            zero[(side, nm)] = sp.simplify(e.subs(eps, 0))
            lin[(side, nm)] = sp.expand(sp.simplify(sp.diff(e, eps).subs(eps, 0)))
    expected0 = {'sigma': -5 * H**2 / 16, 'space': -5 * H**2 / 16, 'time': H**2 / 16, 'extra': -5 * H**2 / 16}
    ok0 = all(sp.simplify(zero[(s, nm)] - expected0[nm]) == 0 for s in (1, -1) for nm, _ in comps)
    # mirror: the sigma < 0 operator equals the sigma > 0 one under sigma -> -sigma (a1 -> -a1, a2 -> a2, ...)
    mirror = {a1: -a1, b1: -b1, n1: -n1}
    okm = all(sp.simplify(lin[(-1, nm)] - lin[(1, nm)].subs(mirror, simultaneous=True)) == 0 for nm, _ in comps)
    out['SR1'] = {nm: str(lin[(1, nm)]) for nm, _ in comps}
    rep.check('SR1_linear_operator', ok0 and okm,
              'order 0 = the stabiliser (kappa T/H^2 = -5/16, -5/16, 1/16, -5/16); first order on sigma > 0 (a1 = alpha\', a2 = '
              'alpha\'\', b = beta, n = nu): %s; the sigma < 0 side is the mirror image' % out['SR1'])

    # ---------------- SR2: homogeneous static solutions with a rigid bulk medium (delta T = 0)
    lam = sp.Symbol('lam')
    ca, cb, cn = sp.symbols('ca cb cn')
    ans = {a1: ca, a2: lam * ca, b1: cb, b2: lam * cb, n1: cn, n2: lam * cn, n0: 0}
    M = sp.Matrix([[sp.diff(lin[(1, nm)].subs(ans), c) for c in (ca, cb, cn)] for nm, _ in comps])
    # nontrivial solutions: rank < 3; find lam by requiring all 3x3 minors to vanish
    minors = []
    for rows in ([0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]):
        minors.append(sp.factor(M.extract(rows, [0, 1, 2]).det()))
    g = minors[0]
    for mnr in minors[1:]:
        g = sp.gcd(g, mnr)
    roots = sp.solve(g, lam) if g.has(lam) else []
    modes = []
    for r in roots:
        ns = M.subs(lam, r).nullspace()
        modes.append({'lambda': str(r), 'vectors': [str(list(v.T)) for v in ns]})
    ok2 = [str(r) for r in roots] == ['6*H'] and len(modes[0]['vectors']) == 1
    vec = sp.Matrix(M.subs(lam, roots[0]).nullspace()[0]) if roots else None
    ok2 = ok2 and vec is not None and sp.simplify(vec[0] + vec[1]) == 0 and vec[2] == 0
    out['SR2'] = {'common_factor_of_minors': str(g), 'modes': modes}
    rep.check('SR2_homogeneous_solutions', ok2,
              'exponential ansatz e^{lam sigma} on sigma > 0: the 4 x 3 system has a non-trivial solution only for lam = %s, '
              'the difference mode (alpha\', beta\', nu\') ~ %s e^{6H sigma}: it grows away from the fold (mirror: e^{6H|sigma|}); '
              'no bounded static first-order correction exists when the bulk medium does not respond' % (
                  [str(r) for r in roots], [str(x) for x in vec]))

    # ---------------- SR3: linearised junction conditions
    ja, jb, jn = sp.symbols('ja jb jn')   # the jumps [alpha'], [beta'], [nu'] (mirror-odd: value at 0+ = jump/2)
    jump = {}
    for nm, k in comps[1:]:
        Fp = F[k].subs(static_sub(+1))
        Fm = F[k].subs(static_sub(-1))
        Fp = Fp.subs({a1: ja / 2, b1: jb / 2, n1: jn / 2, n0: 0})
        Fm = Fm.subs({a1: -ja / 2, b1: -jb / 2, n1: -jn / 2, n0: 0})
        d = sp.expand(sp.simplify(sp.diff(Fp - Fm, eps).subs(eps, 0)))
        jump[nm] = d
    # independent route: the coefficients of the second derivatives (the junction potential is their integral)
    coef = {nm: (sp.diff(lin[(1, nm)], a2), sp.diff(lin[(1, nm)], b2), sp.diff(lin[(1, nm)], n2)) for nm, _ in comps[1:]}
    ok3a = all(sp.simplify(jump[nm] - (coef[nm][0] * ja + coef[nm][1] * jb + coef[nm][2] * jn)) == 0 for nm in jump)
    radion = {ja: 1, jb: -1, jn: 5}
    dmode = {ja: 1, jb: -1, jn: 0}
    rad_vals = {nm: sp.simplify(jump[nm].subs(radion)) for nm in jump}
    d_vals = {nm: sp.simplify(jump[nm].subs(dmode)) for nm in jump}
    ok3 = ok3a and rad_vals['space'] == 0 and rad_vals['time'] == 0 and rad_vals['extra'] != 0
    out['SR3'] = {'kappa_deltaS': {nm: str(v) for nm, v in jump.items()},
                  'difference_mode_(1,-1,0)': {nm: str(v) for nm, v in d_vals.items()},
                  'radion_mode_(1,-1,5)': {nm: str(v) for nm, v in rad_vals.items()}}
    rep.check('SR3_linear_junction', ok3,
              'kappa delta S (space, time, extra) = %s from the junction potential, equal to the coefficients of the second '
              'derivatives; the difference mode (1,-1,0) gives %s (no energy, opposite stresses), the radion mode (1,-1,5) gives '
              '%s: it changes only the extra-time component' % (
                  {nm: str(v) for nm, v in jump.items()}, {nm: str(v) for nm, v in d_vals.items()},
                  {nm: str(v) for nm, v in rad_vals.items()}))

    # ---------------- SR4: the junction with induced gravity at leading order in eps_r
    # T_IG (four-dimensional FRW of the fold, H4 = a4', H4d = H4'): T^4_4 = 3 H4^2/k4, T^i_i = (2 H4d + 3 H4^2)/k4,
    # T^r_r = L_IG = R_hat/(2 k4) = 3 (H4d + 2 H4^2)/k4.  Leading order: T_matter + T_IG = 0 in every component.
    H4, H4d, k4, rho, p, q = sp.symbols('H4 H4d kappa4 rho p q', real=True)
    eq44 = sp.Eq(-rho + 3 * H4**2 / k4, 0)
    eqii = sp.Eq(p + (2 * H4d + 3 * H4**2) / k4, 0)
    eqrr = sp.Eq(q + 3 * (H4d + 2 * H4**2) / k4, 0)
    solGR = sp.solve([eq44, eqii], [rho, H4d], dict=True)[0]
    cond = sp.simplify(eqrr.lhs.subs(H4d, solGR[H4d]).subs(H4**2, k4 * rho / 3))
    # cond = q + (rho - 3p)/2 ?
    ok4 = sp.simplify(cond - (q + (rho - 3 * p) / 2)) == 0
    species = {'radiation (q = 0)': (sp.Rational(1, 3), 0), 'dust, classical (q = -rho)': (0, -1), 'dust, q = 0': (0, 0),
               'vacuum energy (p = q = -rho)': (-1, -1)}
    viol = {k: str(sp.simplify(cond.subs({p: w * rho, q: wq * rho}))) for k, (w, wq) in species.items()}
    out['SR4'] = {'radion_condition': str(cond), 'per_species': viol}
    rep.check('SR4_radion_condition', ok4 and viol['radiation (q = 0)'] == '0',
              'to leading order in eps_r the (4,4) and (i,i) components are 3H4^2 = kappa4 rho and 2H4\' + 3H4^2 = -kappa4 p '
              '(general relativity), and the extra-time component adds q + (rho - 3p)/2 = 0 (q = <L_fold>, the on-shell '
              'Lagrangian): %s' % viol)

    # ---------------- SR5: no response of the bulk medium: the difference mode absorbs the mismatch
    # (i,i) + (r,r) eliminates the difference mode (it enters with opposite signs): p + q + T_IG^i_i + T_IG^r_r = 0
    acc = sp.solve(sp.Eq(p + q + (2 * H4d + 3 * H4**2) / k4 + 3 * (H4d + 2 * H4**2) / k4, 0), H4d)[0]
    acc = sp.simplify(acc.subs(rho, 3 * H4**2 / k4))
    res = {}
    for k, (w, wq) in species.items():
        e = sp.simplify(acc.subs({p: w * 3 * H4**2 / k4, q: wq * 3 * H4**2 / k4}) / H4**2)
        # H' = -c H^2 -> a ~ t^{1/c}
        c = -e
        res[k] = {'H4prime_over_H4sq': str(e), 'a_exponent': str(sp.nsimplify(1 / c)) if c != 0 else 'de Sitter'}
    ok5 = (res['radiation (q = 0)']['a_exponent'] == '1/2' and res['dust, classical (q = -rho)']['a_exponent'] == '5/6'
           and res['dust, q = 0']['a_exponent'] == '5/9' and res['vacuum energy (p = q = -rho)']['H4prime_over_H4sq'] == '-3/5')
    out['SR5'] = {'acceleration_equation': '5 H4\' + 9 H4^2 = -kappa4 (p + q)', 'per_species': res}
    rep.check('SR5_rigid_medium_modifies_expansion', ok5,
              'with a rigid bulk medium: 5H4\' + 9H4^2 = -kappa4(p + q); %s (general relativity: radiation t^{1/2}, dust t^{2/3}, '
              'vacuum energy H4\' = 0)' % {k: (v['a_exponent'] if v['a_exponent'] != 'de Sitter' else v['H4prime_over_H4sq'])
                                           for k, v in res.items()})

    # ---------------- SR6: the radion response today
    # kappa delta S^r_r per unit radion amplitude c (jumps c(1,-1,5)) = rad_vals['extra'] * c; it must equal
    # (kappa/V*) Delta with Delta = sum(q + (rho - 3p)/2); (kappa/V*) = (kappa4/(eps_r H^2)) H  -> c/H = (kappa4 Delta/H^2)/(eps_r k)
    kval = sp.nsimplify(rad_vals['extra'])
    Om = {'chi (q = 0)': (0.265, 0.0, 0.0), 'baryons (q = -rho)': (0.049, 0.0, -1.0), 'vacuum energy': (0.685, -1.0, -1.0),
          'radiation': (9.1e-5, 1 / 3, 0.0)}
    Delta = sum(om * (wq + (1 - 3 * w) / 2) for om, w, wq in Om.values())
    # kappa4 rho_c / H^2 = 3 A^2  ->  c/H = 3 A^2 Delta / (eps_r k)
    out['SR6'] = {'radion_jump_kappaS_extra_per_unit_c': str(kval), 'Delta_over_rho_c_today': Delta,
                  'c_over_H': '3 A^2 x %.4f / (eps_r x %s) = %.4f A^2/eps_r' % (Delta, kval, 3 * Delta / float(kval))}
    ok6 = abs(float(kval) - 0.625) < 1e-12 and 0.79 < Delta < 0.80
    rep.check('SR6_radion_response_today', ok6,
              'a radion mode with jumps c(1, -1, 5) gives kappa delta S^(r)_(r) = %s c; the mismatch today is Delta = %.3f rho_c '
              '(dark matter q = 0, baryons q = -rho, vacuum energy q = -rho); the response c/H = %.3f A^2/eps_r is a small '
              'term of the power series if A^2 = (H4/H)^2 << eps_r' % (kval, Delta, 3 * Delta / float(kval)))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs' / 'series.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_series.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'series_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
