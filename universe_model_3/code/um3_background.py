#!/usr/bin/env python3
"""um3_background.py - the background of UM-3 (SOLUTION.md, order 0 of the power series FE-35): which expansion
histories the author's metric admits, what they require, and the author's ad hoc Higgs vacuum on that background.

Inputs: the exact bulk equations FE-29 and fold equations FE-30 of the author's metric (outputs of um3_geometry.py and
um3_fold.py, restated here as polynomials in A = a4'/H, U = b4'/(H b4), A1 = A'/H, U1 = U'/H).  Computed and checked:
  BG1  the vacuum solutions with constant rates: the polynomial system FE-29 = 0 (A1 = U1 = 0) has exactly the solutions
       (A, U) = (+1, 0) and (-1, 0) (Groebner basis {(A^2-1)^2, A^2 U - A U^2 - U, U^3}): the author's vacuum and its time
       reverse, both degenerate (double root in A^2, triple in U); every other constant-rate history needs bulk sources;
  BG2  the energy conditions of the bulk media that the late universe requires: the stabiliser of the static block and the
       medium of the frozen branch (U = A) violate the null energy condition (rho + p < 0) along every space-like
       direction for |A| < 1;
  BG3  the primordial era with a varying b4 (the author's order: b4 a function of x4, never identically 1): at A = 1 the
       bulk source required by b4' = U H b4 is of second order in U (energy) and its flux of order U^2; the flux-free
       branch U = 2/3; the fold source at A = 1 as a function of U;
  BG4  the fold factor Z(x4) on the three branches (author's vacuum with constant b4, U = 2/3, frozen extra times) and
       the growth of the four-dimensional couplings;
  BG5  the ad hoc Higgs vacuum Phi = (A_c, v)/sqrt 2 (A_c = v_A e^{-2 a40 x4}) is an SU(2) rotation of (0, V)/sqrt 2 with
       V = sqrt(v^2 + A_c^2): with the pure-gauge background W^2_{x4} = theta'/g2 (tan(theta/2) = A_c/v) the isospin
       charge density of the Higgs field vanishes (the Gauss law of FE-17 for homogeneous fields, which the literal ad hoc
       vacuum violates), and the Higgs equation reduces to one radial residual
       R_V = V'' + 3 (b4'/b4) V' + lambda A_c^2 V + c_Phi <Psibar P_L Psi> V;
  BG6  numbers: R_V / (lambda v^3) and the energy density of the ad hoc vacuum for a40/v = 0.1, 1, 10 at x4 = 0, and the
       time after which A_c < 1e-3 v.
Writes outputs/background.json and reports/background_checks.json.
Usage: python universe_model_3/code/um3_background.py
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

A, U, A1, U1 = sp.symbols('A U A1 U1', real=True)

# FE-29: kappa T_bulk^a_b / H^2 for the author's metric (sigma > 0 side for the flux)
T00 = -(A**6 - 3*A**5*U + 12*A**4*U**2 + 3*A**4*U1 + 3*A**4 + 12*A**3*A1*U - 19*A**3*U**3 - 12*A**3*U*U1 - 6*A**3*U
        - 18*A**2*A1*U**2 + 9*A**2*U**4 + 9*A**2*U**2*U1 - 18*A**2*U**2 - 6*A**2*U1 - 9*A**2 + 6*A*A1*U**3 - 12*A*A1*U
        + 21*A*U**3 + 12*A*U*U1 + 9*A*U + 6*A1*U**2 + 3*U**4 + 3*U**2*U1 + 18*U**2 + 3*U1 + 5) / 16
Tii = -(A**6 - 6*A**5*U - 5*A**4*A1 + 12*A**4*U**2 + 3*A**4*U1 + 3*A**4 + 12*A**3*A1*U - 10*A**3*U**3 - 6*A**3*U*U1
        + 12*A**3*U - 9*A**2*A1*U**2 + 6*A**2*A1 + 3*A**2*U**4 + 3*A**2*U**2*U1 - 36*A**2*U**2 - 6*A**2*U1 - 9*A**2
        + 2*A*A1*U**3 - 12*A*A1*U + 18*A*U**3 + 6*A*U*U1 - 6*A*U + 3*A1*U**2 - A1 + 3*U**4 + 3*U**2*U1 + 24*U**2
        + 3*U1 + 5) / 16
T44 = (5*A**6 - 15*A**5*U + 15*A**4*U**2 - 9*A**4 - 5*A**3*U**3 + 18*A**3*U + 3*A**2 - 9*A*U**3 - 3*A*U - 3*U**2 + 1) / 16
Trr = -(A**6 + 5*A**4*A1 - 3*A**4*U**2 - 2*A**4*U1 + 3*A**4 - 8*A**3*A1*U + 2*A**3*U**3 + 2*A**3*U*U1 - 24*A**3*U
        + 3*A**2*A1*U**2 - 6*A**2*A1 + 18*A**2*U**2 - 9*A**2 + 6*A*U**3 + 6*A*U*U1 + 24*A*U + 3*A1*U**2 + A1 + 9*U**2
        + 2*U1 + 5) / 16
GFAC = 5*A**2*(A - U)**2 - 6*A**2 + 6*A*U + U**2 + 1
T04 = sp.Rational(3, 16) * U * GFAC                     # times sgn(sigma)
# FE-30: kappa S^a_b / H
Sii = (9*A**4 - 24*A**3*U - 12*A**2*A1 + 27*A**2*U**2 + 12*A**2*U1 - 66*A**2 + 24*A*A1*U - 6*A*U**3 - 12*A*U*U1
       + 120*A*U - 6*A1*U**2 + 20*A1 - 6*U**4 - 6*U**2*U1 - 111*U**2 - 60*U1 - 183) / 24
S44 = -(3*A**4 - 6*A**3*U - 10*A**2 + 3*A*U**3 + 10*A*U + 10*U**2 + 31) / 4
Srr = (9*A**4 - 12*A**3*U + 12*A**2*A1 + 9*A**2*U**2 - 66*A**2 - 12*A*U**3 - 12*A*U*U1 + 12*A*U - 6*A1*U**2 - 20*A1
       - 57*U**2 - 40*U1 - 183) / 24


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''))
        return ok


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # consistency of the restated polynomials with the stored outputs of um3_fold.py (frozen branch, static block)
    fold = json.loads((UM3 / 'outputs' / 'fold.json').read_text())
    frozen_stored = fold.get('bulk_source_frozen_kappaT_over_H2')
    out['stored_frozen_branch'] = frozen_stored

    # ---------------- BG1: vacuum solutions with constant rates
    const = {A1: 0, U1: 0}
    eqs = [sp.expand(16 * e.subs(const)) for e in (T00, Tii, T44, Trr)] + [sp.expand(16 * T04.subs(const))]
    gb = sp.groebner(eqs, A, U, order='lex')
    sols = sp.solve(eqs, [A, U], dict=True)
    gb_exprs = [sp.factor(g) for g in gb.exprs]
    expected = {sp.factor((A**2 - 1)**2), sp.factor(A**2*U - A*U**2 - U), U**3}
    ok1 = set(gb_exprs) == expected and sorted((s[A], s[U]) for s in sols) == [(-1, 0), (1, 0)]
    out['BG1'] = {'groebner_basis': [str(g) for g in gb_exprs], 'solutions': [str(s) for s in sols],
                  'T44_at_U0': str(sp.factor(16 * T44.subs({U: 0})))}
    rep.check('BG1_vacuum_solutions', ok1,
              'FE-29 = 0 with constant rates: Groebner basis %s; the only solutions are (A, U) = (1, 0) (the author\'s vacuum) '
              'and (-1, 0); 16 kappa T^(4)_(4)/H^2 at U = 0 = %s (a double root at A^2 = 1): every other constant-rate history '
              'needs bulk sources' % ([str(g) for g in gb_exprs], out['BG1']['T44_at_U0']))

    # ---------------- BG2: energy conditions of the late-universe bulk media
    # stabiliser (static block): kappa rho = -1/16, kappa p = -5/16 (units H^2)
    rho_s, p_s = sp.Rational(-1, 16), sp.Rational(-5, 16)
    nec_stab = rho_s + p_s
    # frozen branch U = A (U1 = A1): rho = -T44, pressures T00 (sigma), Tii, Trr
    fz = {U: A, U1: A1}
    rho_f = sp.expand(-T44.subs(fz))
    nec_sigma = sp.factor(sp.expand(rho_f + T00.subs(fz)))
    nec_i = sp.factor(sp.expand(rho_f + Tii.subs(fz)))
    nec_r = sp.factor(sp.expand(rho_f + Trr.subs(fz)))
    flux_f = sp.factor(T04.subs(fz))
    # sample the sign for |A| < 1, |A1| < 1 (slowly varying expansion)
    import random
    random.seed(3)
    worst = -1e9
    for _ in range(4000):
        a_, a1_ = random.uniform(-0.99, 0.99), random.uniform(-0.5, 0.5) * 1e-3
        vals = [float(e.subs({A: a_, A1: a1_})) for e in (nec_sigma, nec_i, nec_r)]
        worst = max(worst, max(vals))
    ok2 = nec_stab < 0 and worst < 0 and sp.simplify(rho_f - (3*A**2 - 1)/16) == 0
    out['BG2'] = {'stabiliser_rho_plus_p': str(nec_stab), 'frozen_rho': str(rho_f), 'frozen_rho_plus_p_sigma': str(nec_sigma),
                  'frozen_rho_plus_p_i': str(nec_i), 'frozen_rho_plus_p_r': str(nec_r), 'frozen_flux_kappaT04_over_H2': str(flux_f),
                  'max_rho_plus_p_sampled': worst}
    rep.check('BG2_null_energy_condition', ok2,
              'stabiliser: kappa(rho_s + p_s) = %s H^2 < 0; frozen branch (U = A): kappa rho = (3A^2 - 1)H^2/16, kappa(rho + p) along '
              'sigma = %s, along ordinary space = %s, along the extra times = %s (units H^2), all negative for |A| < 1 (largest '
              'sampled value %.3f): the bulk medium of the late universe violates the null energy condition; it also carries the '
              'energy flux kappa T^(0)_(4) = sgn(sigma) %s H^2' % (nec_stab, nec_sigma, nec_i, nec_r, worst, flux_f))

    # ---------------- BG3: the primordial era with varying b4 (A = 1)
    a1 = {A: 1, A1: 0, U1: 0}
    rho_p = sp.factor(sp.expand(-T44.subs(a1)))
    flux_p = sp.factor(sp.expand(T04.subs(a1)))
    src_p = {k: sp.factor(sp.expand(v.subs(a1))) for k, v in (('sigma', T00), ('space', Tii), ('time', T44), ('extra', Trr))}
    ser = {k: sp.series(v, U, 0, 3).removeO() for k, v in src_p.items()}
    u23 = {k: sp.nsimplify(v.subs(U, sp.Rational(2, 3))) for k, v in src_p.items()}
    fold_p = {k: sp.factor(sp.expand(v.subs(a1))) for k, v in (('space', Sii), ('time', S44), ('extra', Srr))}
    ok3 = (sp.simplify(flux_p - sp.Rational(3, 8) * U**2 * (3*U - 2)) == 0
           and all(sp.Poly(sp.expand(ser[k]), U).coeff_monomial(1) == 0 for k in ser)
           and u23 == {'sigma': sp.Rational(-14, 27), 'space': sp.Rational(-2, 9), 'time': sp.Rational(2, 27),
                       'extra': sp.Rational(-22, 27)})
    out['BG3'] = {'kappa_rho_bulk_over_H2_at_A1': str(rho_p), 'flux_over_H2': str(flux_p),
                  'sources_over_H2': {k: str(v) for k, v in src_p.items()},
                  'sources_to_second_order_in_U': {k: str(sp.expand(v)) for k, v in ser.items()},
                  'sources_at_U_2_3': {k: str(v) for k, v in u23.items()},
                  'fold_source_kappaS_over_H': {k: str(v) for k, v in fold_p.items()}}
    rep.check('BG3_primordial_varying_b4', ok3,
              'at A = 1 the source that b4\' = U H b4 requires starts at second order in U (no linear term in any component: '
              '%s); flux sgn(sigma)(3/8)U^2(3U - 2)H^2, zero at U = 2/3 (b4 ~ e^{2Hx4/3}) where the constant source is %s '
              '(sigma, space, time, extra times); the fold source at A = 1: %s' % (
                  {k: str(sp.expand(v)) for k, v in ser.items()}, {k: str(v) for k, v in u23.items()},
                  {k: str(v) for k, v in fold_p.items()}))

    # ---------------- BG4: the fold factor on three branches
    # Z ~ (e^{-a4} b4)^3: d ln Z / dx4 = 3 H (U - A)
    branches = {'author_vacuum_constant_b4': (1, 0), 'author_vacuum_U_2_3': (1, sp.Rational(2, 3)), 'frozen_extra_times': ('A', 'A')}
    zrates = {}
    for k, (a_, u_) in branches.items():
        if a_ == 'A':
            zrates[k] = '0'
        else:
            zrates[k] = str(3 * (u_ - a_)) + ' H'
    ok4 = zrates['author_vacuum_constant_b4'] == '-3 H' and zrates['author_vacuum_U_2_3'] == '-1 H' and zrates['frozen_extra_times'] == '0'
    out['BG4'] = {'dlnZ_dx4': zrates, 'coupling_growth_rate': {k: v for k, v in
                  (('author_vacuum_constant_b4', '+3H/2'), ('author_vacuum_U_2_3', '+H/2'), ('frozen_extra_times', '0'))}}
    rep.check('BG4_fold_factor', ok4, 'd ln Z/dx4 = 3H(U - A): %s; the four-dimensional couplings g/sqrt(Z) grow at the '
              'rates 3H/2 (constant b4), H/2 (U = 2/3) and stay constant with frozen extra times' % zrates)

    # ---------------- BG5: the ad hoc vacuum as a rotated, displaced Higgs modulus
    x4 = sp.Symbol('x4', real=True)
    v, vA, a40, g2, lam, cn, Hs, u_ = sp.symbols('v v_A a40 g2 lambda c_n H u', positive=True)
    Ac = vA * sp.exp(-2 * a40 * x4)
    b4 = sp.exp(u_ * Hs * x4)                 # b4 = e^{U H x4} with constant U = u (b4'/b4 = u H)
    mu2 = -lam * v**2
    Phi = sp.Matrix([Ac, v]) / sp.sqrt(2)
    tau2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    theta = 2 * sp.atan(Ac / v)
    W = sp.diff(theta, x4) / g2

    def D4(F):
        return sp.diff(F, x4) - sp.I * g2 * W * (tau2 / 2) * F
    DPhi = D4(Phi)
    # isospin charge density J^{2,x4} = i[(D^4 Phi)^dag tau2/2 Phi - Phi^dag tau2/2 D^4 Phi], D^4 = -D_4
    Dup = -DPhi
    J2 = sp.simplify(sp.I * ((Dup.H * (tau2 / 2) * Phi)[0] - (Phi.H * (tau2 / 2) * Dup)[0]))
    Dup0 = -sp.diff(Phi, x4)
    J2_literal = sp.simplify(sp.I * ((Dup0.H * (tau2 / 2) * Phi)[0] - (Phi.H * (tau2 / 2) * Dup0)[0]))
    # covariant Higgs equation residual: E = -(D4 D4 Phi + 3 (b4'/b4) D4 Phi) - mu^2 Phi - 2 lam (Phi^dag Phi) Phi - c_n Phi
    PhiPhi = sp.simplify((Phi.H * Phi)[0])
    E = -(D4(DPhi) + 3 * (sp.diff(b4, x4) / b4) * DPhi) - mu2 * Phi - 2 * lam * PhiPhi * Phi - cn * Phi
    E = sp.simplify(E)
    V = sp.sqrt(v**2 + Ac**2)
    RV = sp.diff(V, x4, 2) + 3 * u_ * Hs * sp.diff(V, x4) + lam * Ac**2 * V + cn * V
    Urot = sp.Matrix([[sp.cos(theta / 2), sp.sin(theta / 2)], [-sp.sin(theta / 2), sp.cos(theta / 2)]])
    target = Urot * sp.Matrix([0, -RV]) / sp.sqrt(2)
    diff = sp.simplify(E - target)
    # numerical confirmation at random points (the symbolic simplification may leave nested radicals)
    import random as rnd
    rnd.seed(5)
    maxdev = 0.0
    for _ in range(20):
        vals = {v: rnd.uniform(0.5, 2), vA: rnd.uniform(0.1, 2), a40: rnd.uniform(0.05, 3), g2: rnd.uniform(0.3, 1),
                lam: rnd.uniform(0.05, 0.5), cn: rnd.uniform(-0.2, 0.2), Hs: rnd.uniform(0.1, 2), u_: rnd.uniform(-1, 1),
                x4: rnd.uniform(0, 2)}
        dev = max(abs(complex(sp.N(d.subs(vals)))) for d in diff)
        maxdev = max(maxdev, dev)
        maxdev = max(maxdev, abs(complex(sp.N(J2.subs(vals)))))
    lit = sp.simplify(J2_literal - a40 * v * Ac)
    ok5 = maxdev < 1e-10 and lit == 0
    out['BG5'] = {'W2_x4': str(sp.simplify(W)), 'J2_with_W': str(J2), 'J2_literal_ad_hoc': str(sp.simplify(J2_literal)),
                  'radial_residual': 'R_V = V\'\' + 3(b4\'/b4)V\' + lambda A^2 V + c_Phi<Psibar P_L Psi> V, V = sqrt(v^2 + A^2)',
                  'max_deviation': maxdev}
    rep.check('BG5_ad_hoc_vacuum_gauge_equivalence', ok5,
              'with W^2_x4 = theta\'/g2 = %s the isospin charge density of the Higgs field vanishes (the literal ad hoc vacuum has '
              'J^{2,x4} = a40 v A, which no homogeneous field can balance in the Gauss law); the covariant Higgs equation equals '
              'U(theta)(0, -R_V)/sqrt 2 with the radial residual R_V (max deviation %.1e at 20 random points)' % (
                  sp.simplify(W), maxdev))

    # ---------------- BG6: numbers for the residual and the energy of the ad hoc vacuum (units of v; lambda = 0.129)
    lam_v = 0.12941
    rows = []
    for a40_v in (0.1, 1.0, 10.0):
        for vA_v in (1.0,):
            sub = {v: 1, vA: vA_v, a40: a40_v, lam: lam_v, cn: 0, Hs: 1, u_: 0, g2: 0.6517, x4: 0}
            RV0 = float(sp.N(RV.subs(sub)))
            Vp = float(sp.N(sp.diff(V, x4).subs(sub)))
            rhoH = 0.5 * Vp**2 + lam_v / 4 * (vA_v**2) ** 2
            t3 = math.log(vA_v / 1e-3) / (2 * a40_v)
            rows.append({'a40_over_v': a40_v, 'v_A_over_v': vA_v, 'R_V_over_lambda_v3_at_x4_0': RV0 / lam_v,
                         'rho_H_over_v4_at_x4_0': rhoH, 'time_until_A_below_1e-3_v_in_units_1_over_v': t3})
    out['BG6'] = rows
    ok6 = all(r['R_V_over_lambda_v3_at_x4_0'] > 0 for r in rows)
    rep.check('BG6_numbers', ok6, '; '.join('a40 = %g v: R_V(0) = %.3g lambda v^3, rho_H(0) = %.3g v^4, A_c < 1e-3 v after %.3g/v' % (
        r['a40_over_v'], r['R_V_over_lambda_v3_at_x4_0'], r['rho_H_over_v4_at_x4_0'], r['time_until_A_below_1e-3_v_in_units_1_over_v'])
        for r in rows))

    out['runtime_s'] = round(time.time() - t0, 1)
    (UM3 / 'outputs' / 'background.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_background.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    (UM3 / 'reports' / 'background_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
