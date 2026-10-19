#!/usr/bin/env python3
"""UM-2 residuals (version 3, 2026-10-18): how well the approximate solution satisfies each coupled field equation that it
uses, and whether the solution is consistent across the field equations that contain the same fields ("in concert").

For every field equation (or system) of FIELD_EQUATIONS (version 3) that SOLUTION (version 3, steps 1 to 10) uses, the script
records: the solution (exact formula, numerical method, order of the approximation); a precisely defined residual with its
value, either taken from the stored outputs (file and key quoted) or computed afresh by substituting the stored solution into
the equation; the size of the terms the approximation drops; and the in-concert links, in which the same quantity is compared in
the two (or more) places where different field equations use it (the inputs of each script are read where that script reads
them).  Every equation (R_<key>) and every link (L_<key>) has a named check with a tolerance fixed here and a one-line
justification; where a residual is not small it is reported as it is and the tolerance is set by what the physics justifies.

Equations (FIELD_EQUATIONS section; SOLUTION step):
  R1  einstein_lovelock_background          5.3, 5.4; step 1      static block in the printed x4, x1, x0 equations; printed = code
  R2  block_linear_response                 5.5; steps 1, 3, 8   adiabatic response substituted into the nonlinear equations
  R3  primordial_deflation_system           5.3, 5.5; step 1     stored trajectories: constraint and one-step defect
  R4  four_dimensional_effective_gravity    5.6; step 1          Lambda4(k*) = 0, d/dk of the x4 balance, G(k*)
  R5  boson_x0_eigenvalue                   6.1, 4.3; step 2     stored Lambda in the characteristic equations
  R6  fermion_x0_tip_determinant            6.2, 4.2; step 2     D(e) and the 3 x 3 tip determinant at the stored roots
  R7  dirac16complex_x0_spectrum            6.2 (M = m); step 2  tan(p f L) = -p/m, the levels
  R8  kohn_sham_scf                         7; step 3            the N = 8, +lambda_B state re-solved; one more Kohn-Sham map
  R9  kohn_sham_in_gravity_block_response   7, 5.5; step 3       the Kohn-Sham block averages in the block response
  R10 portal_overlaps_hellmann_feynman      7.1, 10; steps 3, 8  overlaps from the closed-form orbitals; O = d eps_DM/dm
  R11 coupled_environment_mean_fields       7.1, 11; step 8      mean fields, condensates, block response, loop
  R12 wz_x0_with_dark_matter_kinetic_function 7.1; step 8        first-order perturbation theory and shooting
  R13 yang_mills_masses_and_widths          4.3, 6.1; steps 2, 4 m_Z and the tree-level Z widths
  R14 linear_perturbations_cmb_bao          8; step 6            Poisson against the Weyl potential; matter-era limit
  R15 graviton_tower                        8.1; step 10         the exact profiles in the graviton operator; Yukawa strengths
  R16 metric_series_order2                  8, 8.1; step 10      the first omitted order against the kept order
  R17 neutrino_flavour_evolution            9.1, 9.2; step 5     unitarity, vacuum formula, accelerator and solar probabilities
  R18 neutrino_thermal_potential            9.3; step 5          the onset condition at the stored temperatures
  R19 neutrino_decoupling                   9.4; step 5          the instantaneous limit recomputed; the published values
  R20 fast_flavour_dispersion               9.5; step 5          moments, analytic growth, discretised homogeneous equations
  R21 cosmic_neutrino_background            9.6; step 5          densities, energy densities, velocities, Omega_nu h^2
  R22 thermal_degrees_of_freedom            10; step 9           g_rho, g_s by independent quadrature; exact limits
  R23 boltzmann_relic                       10; steps 7, 9       the relic re-solved at the stored G_A; late-time identity
  R24 freeze_in                             10; step 9           Delta N_eff per G_V^2 re-integrated
  R25 right_handed_neutrino_boltzmann       10; step 9           the nu_R equation (B - L alternative) re-solved
  R26 self_interaction_channel              10; step 9           Itilde_lambda, G_lambda, Delta N_eff per G_lambda^2
In-concert links (L_<key>): the Kohn-Sham source in the block response; the hidden pressure of the dark matter (Kohn-Sham stress,
x0 eigenvalue, block response); m_Z and the weak angle in the x0 problem and in the Z widths; the x0 fermion masses in the thermal
history; the neutrino masses and the PMNS matrix of the tip matrices in the flavour evolution, the CNB and CAMB; Omega_nu h^2 and
N_eff in the CMB; the relic density as omega_c of the CMB; the Hubble rate of the thermal history against the four-dimensional
Friedmann equation with all species; the late-time radiation; the plasma density in the coupled sources; the portal responses of the
Kohn-Sham jobs and of the coupled solution; O; the I12 benchmark in the mean field; the dark-matter mass; the relic and freeze-in
couplings in the mean fields; the block-response coefficients; the radion frequency; f*; the heating factor F_h; the metric series;
the freeze-out temperature; the block sensitivities of the masses.
Reads outputs/*.json and outputs/ks/*.json (never writes them); writes outputs/residuals.json and reports/residuals-checks.json.
"""
import os

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[_v] = '1'          # single-threaded linear algebra, as in um2_ks_jobs.py: the same numbers on every machine

import cmath  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402

import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402
from scipy.integrate import quad, solve_ivp  # noqa: E402
from scipy.interpolate import CubicSpline  # noqa: E402
from scipy.optimize import brentq  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from um2_common import OUT, Report, read_json, write_json  # noqa: E402
from um2_constants import CKM_PDG2024, ETA, NEFF_SM, NUFIT60_NO, val  # noqa: E402

KS_DIR = os.path.join(OUT, 'ks')
H1 = 1.0                 # H = 1 in the units of the background and Kohn-Sham computations
L_CELL = ETA / H1        # hidden length of a half cell, L = eta/H
DK = 0.25                # momentum-shell spacing of the Kohn-Sham states
LAM_B = 7.0e-5           # the benchmark self-coupling of the Kohn-Sham tests (units H^-6)
O_HARDCODED = 0.7072     # the I12 response d eps_DM/dm as hard-coded in um2_thermal.py and um2_coupled.py
FH_HARDCODED = 1.0095    # the heating factor F_h as hard-coded in um2_coupled.py


def rel(a, b):
    a, b = float(a), float(b)
    if b == 0.0:
        return abs(a)
    return abs(a / b - 1.0)


def maxrel(pairs):
    return max(rel(a, b) for a, b in pairs)


def load():
    names = ('background', 'geometry', 'masses', 'flavour', 'neutrino', 'electroweak', 'primordial', 'cosmology', 'analysis',
             'thermal', 'coupled', 'series')
    D = {n: read_json(os.path.join(OUT, n + '.json')) for n in names}
    for n in ('validate', 'spectrum', 'ground8', 'ground592', 'darkmatter', 'portals', 'feedback'):
        D['ks_' + n] = read_json(os.path.join(KS_DIR, n + '.json'))
    return D


# ======================================================================================================================
# the background equations as printed in FIELD_EQUATIONS section 5.3 (units H = 1); each returns the list of terms
def e4_terms(A, h, k):
    """x4 (constraint): sum = -kappa rho."""
    return [-15 * A ** 2 * h ** 4 / 16, -5 * A ** 3 * h ** 3 / 4, -3 * h ** 4 / 8, -9 * A * h ** 3 / 2, -27 * A ** 2 * h ** 2 / 4,
            9 * k * A ** 2 * h ** 2 / 8, -3 * h * A ** 3 / 2, 3 * h * k * A ** 3 / 4, -6 * h ** 2, 3 * k * h ** 2 / 4, -12 * A * h,
            9 * A * h * k / 2, -3 * A ** 2, 9 * k * A ** 2 / 4, -3 * A ** 2 * k ** 2 / 16, -10, 6 * k, -3 * k ** 2 / 8]


def x1_parts(A, h, k):
    """x1: (sum cA) dA/dx4 + (sum ch) dh/dx4 + sum r = kappa p3."""
    cA = [-h ** 4 / 8, -A * h ** 3 / 2, -3 * h ** 2 / 2, k * h ** 2 / 4, -A * h, A * h * k / 2, -2, 3 * k / 2, -k ** 2 / 8]
    ch = [-A * h ** 3 / 2, -3 * A ** 2 * h ** 2 / 4, -3 * h ** 2 / 2, -3 * A * h, A * h * k / 2, -A ** 2 / 2, k * A ** 2 / 4, -4,
          3 * k / 2]
    r = [-A * h ** 5 / 2, -19 * A ** 2 * h ** 4 / 16, -A ** 3 * h ** 3 / 2, -15 * h ** 4 / 8, -6 * A * h ** 3, A * k * h ** 3 / 2,
         -17 * A ** 2 * h ** 2 / 4, 7 * k * A ** 2 * h ** 2 / 8, -h * A ** 3, h * k * A ** 3 / 2, -10 * h ** 2, 9 * k * h ** 2 / 4,
         -8 * A * h, 3 * A * h * k, -3 * A ** 2, 9 * k * A ** 2 / 4, -3 * A ** 2 * k ** 2 / 16, -10, 6 * k, -3 * k ** 2 / 8]
    return cA, ch, r


def x0_parts(A, h, k):
    """x0: (sum cA) dA/dx4 + (sum ch) dh/dx4 + sum r = kappa pbar."""
    cA = [-3 * A * h ** 3 / 8, -9 * A ** 2 * h ** 2 / 16, -9 * h ** 2 / 8, -9 * A * h / 4, 3 * A * h * k / 8, -3 * A ** 2 / 8,
          3 * k * A ** 2 / 16, -3, 9 * k / 8]
    ch = [-9 * A ** 2 * h ** 2 / 16, -3 * h * A ** 3 / 8, -3 * h ** 2 / 8, -9 * A * h / 4, -9 * A ** 2 / 8, 3 * k * A ** 2 / 16, -3,
          3 * k / 8]
    r = [-9 * A ** 2 * h ** 4 / 16, -17 * A ** 3 * h ** 3 / 16, -9 * A ** 4 * h ** 2 / 16, -3 * h ** 4 / 8, -27 * A * h ** 3 / 8,
         -45 * A ** 2 * h ** 2 / 8, 3 * k * A ** 2 * h ** 2 / 16, -27 * h * A ** 3 / 8, 9 * h * k * A ** 3 / 16, -3 * A ** 4 / 8,
         3 * k * A ** 4 / 16, -6 * h ** 2, 3 * k * h ** 2 / 8, -9 * A * h, 9 * A * h * k / 8, -6 * A ** 2, 9 * k * A ** 2 / 4, -10,
         3 * k]
    return cA, ch, r


def rates_bg(A, h, k, kp3, kpbar):
    """dA/dx4, dh/dx4 from the printed x1 and x0 equations with the sources kappa p3, kappa pbar."""
    cA1, ch1, r1 = x1_parts(A, h, k)
    cA0, ch0, r0 = x0_parts(A, h, k)
    a11, a12, b1 = sum(cA1), sum(ch1), kp3 - sum(r1)
    a21, a22, b2 = sum(cA0), sum(ch0), kpbar - sum(r0)
    det = a11 * a22 - a12 * a21
    return (b1 * a22 - a12 * b2) / det, (a11 * b2 - a21 * b1) / det


KSTAR_EXACT = 12 + 4 * math.sqrt(51) / 3
KRHO_EXACT = 26 + 4 * math.sqrt(51)
G_EXACT = 20.0 / 3.0 + math.sqrt(51)


# ======================================================================================================================
class Builder:
    """Collects the equation entries and the in-concert links and registers their checks."""

    def __init__(self, rep):
        self.rep = rep
        self.equations = []
        self.links = []
        self.notes = []

    def equation(self, key, name, section, solution, residual, neglected, value, tol, justification, extra_ok=True, extra='',
                 in_concert_note=None):
        passed = bool(value <= tol and extra_ok)
        entry = {'equation': key, 'name': name, 'section': section, 'solution': solution, 'residual': residual,
                 'neglected': neglected, 'in_concert': [],
                 'check': {'name': 'R_' + key, 'value': value, 'tolerance': tol, 'justification': justification, 'passed': passed,
                           'detail': extra}}
        if in_concert_note:
            entry['in_concert_note'] = in_concert_note
        self.equations.append(entry)
        self.rep.check('R_' + key, passed, 'residual %.3e (tolerance %.1e)%s' % (value, tol, ('; ' + extra) if extra else ''))
        return entry

    def link(self, key, name, equations, quantity, places, difference, tol, justification, definition, extra_ok=True, extra=''):
        passed = bool(difference <= tol and extra_ok)
        lk = {'link': key, 'name': name, 'equations': equations, 'quantity': quantity, 'places': places,
              'difference': difference, 'difference_definition': definition, 'tolerance': tol, 'justification': justification,
              'check': 'L_' + key, 'passed': passed, 'detail': extra}
        self.links.append(lk)
        self.rep.check('L_' + key, passed, 'difference %.3e (tolerance %.1e)%s' % (difference, tol, ('; ' + extra) if extra else ''))
        return lk

    def finish(self):
        keys = [e['equation'] for e in self.equations]
        for lk in self.links:
            for k in lk['equations']:
                if k not in keys:
                    raise KeyError('link %s names unknown equation %s' % (lk['link'], k))
                self.equations[keys.index(k)]['in_concert'].append(
                    {'link': lk['link'], 'quantity': lk['quantity'], 'difference': lk['difference'], 'tolerance': lk['tolerance'],
                     'passed': lk['passed']})


# ======================================================================================================================
# R1-R4 gravity: background, block response, primordial era, four-dimensional reduction
def gravity(D, B, S):
    import sympy as sp
    bg = D['background']
    cs = bg['casimir_type']
    ks, krho, Gk = cs['k_star_value'], cs['kappa_rho_b_over_H2'], cs['G_k_star_value']
    # ---- printed equations = the code's equations (sympy, exact) ----
    Asym, hsym, ksym, Adsym, hdsym = sp.symbols('A h k Adot hdot', real=True)
    Hs, w2s, w3s, Lams = sp.symbols('H w2 w3 Lambda', real=True)
    loc = {'A': Asym, 'h': hsym, 'k': ksym, 'Adot': Adsym, 'hdot': hdsym, 'H': Hs, 'w2': w2s, 'w3': w3s, 'Lambda': Lams}
    sub = {w2s: sp.Rational(1, 32), w3s: sp.Rational(1, 1152), Lams: -10 * Hs ** 2}
    fe = bg['field_equations_class_form']

    def code_lhs(key):
        return sp.expand(sp.sympify(fe[key].split(' = ')[0], locals=loc).subs(sub).subs(Hs, 1))
    # exact rational transcription of the printed equations (the functions above evaluated on symbols with rational coefficients)
    one = sp.Integer(1)
    d4 = sp.expand(code_lhs('x4 (constraint)') - sum(sp.nsimplify(t) for t in e4_terms(Asym * one, hsym * one, ksym * one)))
    cA, ch, r = x1_parts(Asym * one, hsym * one, ksym * one)
    d1 = sp.expand(code_lhs('x1 = x2 = x3') - (sum(cA) * Adsym + sum(ch) * hdsym + sum(r)))
    cA, ch, r = x0_parts(Asym * one, hsym * one, ksym * one)
    d0 = sp.expand(code_lhs('x0 = x5 = x6 = x7') - (sum(cA) * Adsym + sum(ch) * hdsym + sum(r)))
    sym_ok = (d4 == 0 and d1 == 0 and d0 == 0)
    # ---- static block in the printed equations ----

    def static_res(k_, kr_):
        t4 = e4_terms(0.0, 0.0, k_)
        _, _, r1 = x1_parts(0.0, 0.0, k_)
        _, _, r0 = x0_parts(0.0, 0.0, k_)
        sc = max(abs(x) for x in t4 + r1 + r0)
        return [abs(sum(t4) + kr_) / sc, abs(sum(r1) + kr_) / sc, abs(sum(r0) - kr_) / sc]
    res_stored = static_res(ks, krho)
    res_exact = static_res(KSTAR_EXACT, KRHO_EXACT)
    env = D['coupled']['environments']
    kV = D['coupled']['block_response_coefficients']['kappa_over_Vperp_GeV-2']
    HG = D['masses']['scales']['H_GeV']
    src_ratio = {k_: kV * v['sources_GeV4']['rho'] / HG ** 2 / krho for k_, v in env.items()}
    worst_env = max(src_ratio, key=src_ratio.get)
    S['src_ratio_max'] = src_ratio[worst_env]
    S['kappa_drho_over_H2_max'] = src_ratio[worst_env] * krho
    v1 = max(res_stored)
    B.equation(
        'einstein_lovelock_background',
        'Einstein-Lovelock background equations (x4 constraint, x1, x0) of the order-0 metric with the block stabiliser',
        'FIELD_EQUATIONS (version 3) section 5.3 (the background field equations) and 5.4 (the static block and the stabiliser); '
        'SOLUTION step 1 (the static block)',
        {'description': 'the static block A = h = 0, k = k* = 12 + (4/3) sqrt(51), f* = k*^(-1/2), with the stabiliser kappa rho_b* = '
                        '(26 + 4 sqrt(51)) H^2, p3 = -rho_b, p0 = p_t = rho_b',
         'method': 'exact (closed form; sympy in um2_background.py); stored as background.json casimir_type (12 significant digits)',
         'order': 'order 0 of the metric power series (exact solution of the order-0 equations)',
         'k_star': ks, 'kappa_rho_b_over_H2': krho},
        {'definition': 'max over the three printed components (FIELD_EQUATIONS 5.3) of |LHS - kappa T| / max|term| at the stored k*, '
                       'kappa rho_b* (afresh); and the printed polynomials minus the code\'s symbolic field equations '
                       '(background.json field_equations_class_form with w = (1, 1/32, 1/1152), Lambda = -10 H^2), sympy',
         'value': v1, 'source': 'computed afresh by direct substitution',
         'details': {'x4_x1_x0_with_stored_k_star': res_stored, 'x4_x1_x0_with_closed_form_k_star': res_exact,
                     'printed_minus_code_symbolic_x4_x1_x0': [str(d4), str(d1), str(d0)]}},
        {'definition': 'block-averaged matter sources against the stabiliser, kappa delta rho/(kappa rho_b*), kappa delta rho = '
                       '(kappa/V_perp) rho_4 (coupled.json environments sources_GeV4.rho, block_response_coefficients)',
         'value': src_ratio[worst_env], 'where': worst_env, 'today_cosmic_mean': src_ratio['cosmic mean today'],
         'source': 'computed from coupled.json'},
        v1, 1e-11, 'the stored k* and kappa rho_b* carry 12 significant digits and the equations contain terms up to 3 H^2 k*^2/8 = 174 H^2: '
                   'rounding alone gives about 1e-12 of the largest term; the printed and the coded equations must agree exactly',
        extra_ok=sym_ok, extra='printed = code (sympy): %s; closed form %.1e' % (sym_ok, max(res_exact)))

    # ---- R2 the linear (adiabatic) block response ----
    lr = bg['linear_response_static_dk']
    lv = bg['linear_response_values']
    c_rho, c_3, c_p = lr['per_kappa_drho_H2'], lr['per_kappa_dp3_H2'], lr['per_kappa_dpbar_H2']
    lin = {}
    for eps in (1e-4, 1e-5):
        drho, dp3, dpb = eps, 0.2 * eps, 0.7 * eps
        dk = c_rho * drho + c_3 * dp3 + c_p * dpb
        k_ = KSTAR_EXACT + dk
        Rk = KRHO_EXACT * (k_ / KSTAR_EXACT) ** 4
        A_ = math.sqrt(drho / (3 * G_EXACT))
        Ad, hd = rates_bg(A_, 0.0, k_, -Rk + dp3, Rk + dpb)
        first = abs(lv['s_h3'] * dp3) + abs(lv['s_hp'] * dpb) + abs(lv['q_h'] * drho) + abs(lv['J_hk'] * dk)
        fried = -(drho + dp3) / (2 * G_EXACT)
        con = sum(e4_terms(A_, 0.0, k_)) + Rk + drho
        lin[eps] = [abs(hd) / first, abs(Ad / fried - 1), abs(con) / drho]
    ratios = [lin[1e-5][i] / lin[1e-4][i] for i in range(3)]
    coef = max(lin[1e-4][i] / 1e-4 for i in range(3))
    S['response_second_order_coefficient'] = coef
    # adiabaticity at the freeze-out: (Hubble rate / radion mass)^2
    th = D['thermal']
    T_fo = env['dark-matter freeze-out (T = 1.42 TeV)']['T_GeV']
    curve = th['g_star_curve']
    lnTc = np.log(curve['T_GeV'])
    grc, gsc = np.array(curve['g_rho']), np.array(curve['g_s'])
    S['g_of'] = lambda T: (float(np.interp(math.log(T), lnTc, grc)), float(np.interp(math.log(T), lnTc, gsc)))
    MPl = val('M_Pl_GeV')
    H_fo = math.sqrt(8 * math.pi ** 3 * S['g_of'](T_fo)[0] / 90) * T_fo ** 2 / MPl
    mr = D['masses']['scales']['radion_mass_GeV']
    S['adiabaticity_fo'] = (H_fo / mr) ** 2
    rad_cancel = abs(c_3 + 3 * c_rho)
    v2 = max(lin[1e-5])
    B.equation(
        'block_linear_response',
        'linearised block equations about the static block and their adiabatic (static) response to block-averaged sources',
        'FIELD_EQUATIONS section 5.5 (the dynamical system, the radion and the response to matter) and 7.1 (gravity closes the loop); '
        'SOLUTION step 1 (the response of the block to matter), step 3 (back-reaction) and step 8 (gravity)',
        {'description': 'delta k\'\' + omega_r^2 delta k = -2 k* (s_h3 kappa dp3 + s_hp kappa dpbar + q_h kappa drho); adiabatic response '
                        'dk = (c_rho kappa drho + c_3 kappa dp3 + c_p kappa dpbar)/H^2, c_rho = %.6f, c_3 = %.6f, c_p = %.6f; '
                        'dA/dx4 = -kappa (drho + dp3)/(2 G(k*))' % (c_rho, c_3, c_p),
         'method': 'exact algebraic numbers (sympy, um2_background.py; background.json linear_response, linear_response_static_dk)',
         'order': 'first order in the sources (A^2 counted as first order)'},
        {'definition': 'the adiabatic solution (dk from the stored coefficients, A^2 = kappa drho/(3 G(k*)), h = 0) substituted into the '
                       'full nonlinear printed x1, x0 (solved for dA/dx4, dh/dx4) and x4: |dh/dx4| / sum of the first-order terms, '
                       '|dA/dx4 / (-kappa (drho + dp3)/(2 G)) - 1|, |x4 residual| / kappa drho, for sources kappa (drho, dp3, dpbar) = '
                       'eps (1, 0.2, 0.7) H^2; value: the largest of the three at eps = 1e-5',
         'value': v2, 'source': 'computed afresh by direct substitution',
         'details': {'eps_1e-4': lin[1e-4], 'eps_1e-5': lin[1e-5], 'ratio_eps_1e-5_over_1e-4': ratios,
                     'second_order_coefficient_residual_over_eps': coef, 'radiation_cancels_c3_plus_3c_rho': rad_cancel}},
        {'definition': 'second-order terms relative to the first-order response at the largest source of the coupled solution '
                       '(residual coefficient times kappa drho/H^2 at the dark-matter freeze-out), and the neglected inertia '
                       'delta k\'\'/(omega_r^2 delta k) ~ (H_Hubble/m_r)^2 at the freeze-out',
         'value': coef * S['kappa_drho_over_H2_max'], 'adiabaticity_at_freeze_out': S['adiabaticity_fo'],
         'source': 'computed (coupled.json sources, thermal.json g_rho, masses.json radion mass)'},
        v2, 1e-6, 'a first-order solution leaves a residual of second order: it must fall by the factor 10 with the sources (checked: '
                  'ratios 0.10) and stay at about eps (0.1 eps allowed); eps = 1e-5 gives at most 1e-6',
        extra_ok=all(0.08 < x < 0.12 for x in ratios) and rad_cancel < 1e-12,
        extra='residual/eps ratios %s (second order), c_3 + 3 c_rho = %.1e' % (', '.join('%.3f' % x for x in ratios), rad_cancel))

    # ---- R3 the primordial era ----
    pr = D['primordial']
    con_max = 0.0
    defect_max = 0.0
    nint = 0
    for key in sorted(pr['runs']):
        run = pr['runs'][key]
        rr0 = float(key.split('rr0=')[1])
        smp = run['samples']
        for (t, a4, A_, h_, k_) in smp:
            rr = rr0 * math.exp(-4 * a4) * (k_ / KSTAR_EXACT) ** 2
            terms = e4_terms(A_, h_, k_) + [KRHO_EXACT * (k_ / KSTAR_EXACT) ** 4, rr]
            con_max = max(con_max, abs(sum(terms)) / sum(abs(x) for x in terms))
        for i in range(0, len(smp) - 1, 5):
            t, a4, A_, h_, k_ = smp[i]

            def rhs(tt, Y, rr0=rr0):
                aa, AA, hh, lk = Y
                kk = math.exp(lk)
                Rk = KRHO_EXACT * (kk / KSTAR_EXACT) ** 4
                rr_ = rr0 * math.exp(-4 * aa) * (kk / KSTAR_EXACT) ** 2
                Ad_, hd_ = rates_bg(AA, hh, kk, -Rk + rr_ / 3.0, Rk)
                return [AA, Ad_, hd_, -2 * hh]
            sol = solve_ivp(rhs, (t, smp[i + 1][0]), [a4, A_, h_, math.log(k_)], method='DOP853', rtol=1e-12, atol=1e-14)
            y = sol.y[:, -1]
            nxt = smp[i + 1]
            defect_max = max(defect_max, abs(y[0] - nxt[1]), abs(y[1] - nxt[2]), abs(y[2] - nxt[3]), abs(y[3] - math.log(nxt[4])))
            nint += 1
    r5, r5r = pr['runs']['k0=5,h0=-0.3333,rr0=0'], pr['runs']['k0=5,h0=-0.3333,rr0=10']
    rad_effect = abs(r5r['k_end'] / r5['k_end'] - 1)
    Amax = max(abs(s_[2]) for run in pr['runs'].values() for s_ in run['samples'])
    stored_con = max(run['constraint_max_residual'] for run in pr['runs'].values())
    v3 = max(con_max, defect_max)
    B.equation(
        'primordial_deflation_system',
        'full nonlinear homogeneous Einstein-Lovelock equations of the primordial era (deflating block with the stabiliser and radiation)',
        'FIELD_EQUATIONS section 5.3 (x4 constraint, x1 and x0 linear in dA/dx4 and dh/dx4) and 5.5 (the closed system for (A, h, k)); '
        'SOLUTION step 1 (the primordial era: the deflating extra times)',
        {'description': 'trajectories (a4, A, h, ln k) from deflating starts k0 = 3, 5, 10 at h0 = -H/3 (one with radiation of zero modes) '
                        'into the stable block (primordial.json runs, samples every 0.1/H up to x4 = 40/H)',
         'method': 'DOP853, rtol 1e-11, atol 1e-13, max step 0.05/H (um2_primordial.py)', 'order': 'exact equations, numerical solution'},
        {'definition': 'largest of (a) the printed x4 constraint with kappa rho_b(k) and the radiation at the %d stored samples, '
                       '|sum| / sum |terms|, and (b) the one-step defect: from every fifth stored sample the printed x1, x0 equations '
                       'are integrated (DOP853, rtol 1e-12) over 0.1/H to the next stored sample, max |delta (a4, A, h, ln k)| in units '
                       'of H (A reaches %.2f H)' % (sum(len(r_['samples']) for r_ in pr['runs'].values()), Amax),
         'value': v3, 'source': 'computed afresh by direct substitution and short re-integration (%d intervals)' % nint,
         'details': {'constraint_relative': con_max, 'one_step_defect': defect_max,
                     'stored_constraint_max_residual_absolute_over_0_120': stored_con}},
        {'definition': 'radiation of zero modes (kappa rho_r = 10 at the start, k0 = 5): relative change of the final block k(120/H); the '
                       'metric perturbations (order eps) and the block-shape mode are not part of the order-0 ansatz (OPEN)',
         'value': rad_effect, 'source': 'primordial.json runs k_end'},
        v3, 1e-9, 'the samples carry 12 digits and come from an integration with rtol 1e-11 at rates up to 8.3 H, so an exact '
                  'trajectory shows a defect near 1e-11; 1e-9 is where the stored trajectory would no longer solve the equations',
        extra='constraint %.1e, defect %.1e' % (con_max, defect_max))
    S['primordial_omega'] = r5['omega_from_zero_crossings']

    # ---- R4 the four-dimensional reduction ----
    w2 = 1.0 / 32.0

    def lam4(k_, kr_):
        G_ = 1 - 24 * w2 * k_ + 72 * (1.0 / 1152.0) * k_ ** 2
        terms = [6 * k_, -12 * w2 * k_ ** 2, -10.0, kr_]
        return sum(terms) / G_, max(abs(x) for x in terms) / abs(G_)

    def dF4(k_, kr_):
        terms = [6.0, -24 * w2 * k_, 4 * kr_ / k_]
        return abs(sum(terms)) / max(abs(x) for x in terms)
    l4s, sc4 = lam4(ks, krho)
    l4x, sc4x = lam4(KSTAR_EXACT, KRHO_EXACT)
    dF_s, dF_x = dF4(ks, krho), dF4(KSTAR_EXACT, KRHO_EXACT)
    Gres = rel(Gk, G_EXACT)
    coefR = bg['reduction']['coefficient_R4']
    kk_ = sp.Symbol('k', real=True)
    coef_ok = sp.simplify(sp.sympify(coefR, locals={'k': kk_, 'w2': w2s, 'w3': w3s}).subs(sub) - (kk_ ** 2 - 12 * kk_ + 16) / 16) == 0
    v4 = max(abs(l4s) / sc4, dF_s, Gres)
    B.equation(
        'four_dimensional_effective_gravity',
        'dimensional reduction on M4 x (static block): four-dimensional general relativity with Lambda4 and G_N',
        'FIELD_EQUATIONS section 5.6 (the four-dimensional effective gravity); SOLUTION step 1',
        {'description': 'sum alpha_p L_(p) - 2 Lambda - 2 kappa rho_b = G(k) R4 + topological - 2 G(k) Lambda4, G(k*) = 20/3 + sqrt(51), '
                        'Lambda4(k*) = 0, 8 pi G_N = kappa/(G(k*) V_perp); the x4 balance stationary at k* (so the 4D cosmological term '
                        'is unchanged at linear order by a block shift)',
         'method': 'exact (sympy, um2_background.py B5)', 'order': 'exact on the static block'},
        {'definition': 'largest of |Lambda4(k*)| / max|term| and |d/dk [6 H^2 k (1 - 2 w2 k) + kappa rho_b(k)]| / max|term| at the stored k*, '
                       'kappa rho_b*, and |G(k*) stored / (20/3 + sqrt 51) - 1|; background.json reduction coefficient_R4 = G(k) symbolic',
         'value': v4, 'source': 'computed afresh',
         'details': {'Lambda4_relative_stored': abs(l4s) / sc4, 'Lambda4_relative_closed_form': abs(l4x) / sc4x,
                     'dF4_dk_relative_stored': dF_s, 'dF4_dk_relative_closed_form': dF_x,
                     'ks_feedback_d_F4_dk_stored': D['ks_feedback']['d_F4_dk'], 'coefficient_R4_equals_G': bool(coef_ok)}},
        {'definition': 'the observed dark energy needs Lambda4/H^2 ~ (H0/H)^2 (tuned, OPEN), analysis.json vacuum_energy.H0_over_H_squared; '
                       'Kaluza-Klein modes start at m_KK = %.0f GeV' % D['masses']['scales']['m_KK_GeV'],
         'value': D['analysis']['vacuum_energy']['H0_over_H_squared'], 'source': 'analysis.json'},
        v4, 1e-11, 'the inputs carry 12 significant digits and the terms are of order 100 H^2; the exact values are 0 and 20/3 + sqrt 51',
        extra_ok=bool(coef_ok), extra='d/dk of the x4 balance at the stored k*: %.1e (ks/feedback.json d_F4_dk %.1e is this rounding; '
                                      'exact 0, closed form %.1e)' % (dF_s, D['ks_feedback']['d_F4_dk'], dF_x))


# ======================================================================================================================
# R5-R7 the x0 eigenvalue problems
def x0_spectra(D, B, S):
    from um2_flavour import mixing_matrix_mp, tip_matrix     # (importing um2_flavour sets the mpmath precision; it is fixed here)
    mp.mp.dps = 40
    masses = D['masses']
    WZ = masses['WZ']
    un = masses['unbroken']
    g = mp.mpf(3) * mp.mpf(ETA) / 2

    def even_below(L_, beta):
        kap = mp.sqrt(g * g - L_)
        return (g * (beta + g) - kap ** 2) * mp.sinh(kap) - beta * kap * mp.cosh(kap)

    def even_above(L_, beta):
        q = mp.sqrt(L_ - g * g)
        return (q * q + g * (beta + g)) * mp.sin(q) - beta * q * mp.cos(q)

    def odd_above(L_, beta):
        q = mp.sqrt(L_ - g * g)
        return q * mp.cos(q) + (beta + g) * mp.sin(q)

    def dirichlet(L_):
        kap = mp.sqrt(g * g - L_)
        return g * mp.sinh(kap) - kap * mp.cosh(kap)

    def implied(fun, L_):
        L_ = mp.mpf(L_)
        return float(abs(fun(L_) / mp.diff(fun, L_)) / abs(L_))
    res = {'W': implied(lambda L_: even_below(L_, mp.mpf(WZ['beta_W'])), WZ['Lambda_W']),
           'Z': implied(lambda L_: even_below(L_, mp.mpf(WZ['beta_Z'])), WZ['Lambda_Z'])}
    for i, Lv in enumerate(un['even'][1:]):
        res['even_KK_%d' % (i + 1)] = implied(lambda L_: even_above(L_, 0), Lv)
    for i, Lv in enumerate(un['odd']):
        res['odd_KK_%d' % (i + 1)] = implied(lambda L_: odd_above(L_, 0), Lv)
    res['dirichlet_bound'] = implied(dirichlet, masses['Lambda_D'])
    v5 = max(res.values())
    S['mZ_x0'] = val('m_W_GeV') * math.sqrt(WZ['Lambda_Z'] / WZ['Lambda_W'])
    S['mKK_x0'] = val('m_W_GeV') * math.sqrt(un['Lambda1'] / WZ['Lambda_W'])
    B.equation(
        'boson_x0_eigenvalue',
        'x0 eigenvalue problem of the gauge fields and the graviton (Robin tip condition from the tip mass terms)',
        'FIELD_EQUATIONS section 6.1 (gauge fields and the graviton) with 4.3 (the tip terms as Robin conditions); SOLUTION step 2 '
        '(gauge bosons and the graviton)',
        {'description': '-e^{-3 eta xi}(e^{3 eta xi} u\')\' = Lambda u, u\'(0) = 0 or u(0) = 0, u\'(-1) = beta u(-1); exact characteristic '
                        'equations; photon, gluons, graviton Lambda = 0 (flat profile, exact); W, Z with beta_W = %.7f, beta_Z = '
                        'beta_W/cos^2(theta_W)' % WZ['beta_W'],
         'method': 'roots of the transcendental conditions with mpmath (60 digits), finite elements as a cross-check (um2_spectra.py; '
                   'masses.json WZ, unbroken, Lambda_D)', 'order': 'exact on the static block (tree level)'},
        {'definition': 'implied relative eigenvalue error |F(Lambda) / (Lambda dF/dLambda)| of each stored eigenvalue in its exact '
                       'characteristic equation F = 0 (mpmath, 40 digits): W, Z (below the gap), the even and odd Kaluza-Klein levels, '
                       'the Dirichlet bound; the flat profile solves the beta = 0 problem with Lambda = 0 exactly',
         'value': v5, 'source': 'computed afresh by direct substitution', 'details': res},
        {'definition': 'shift of Lambda_W by the dark-matter kinetic function at the freeze-out amplitude, e |d ln Lambda_W/de| (coupled.json '
                       'WZ_kinetic_shift amplitude, coefficient recomputed in wz_x0_with_dark_matter_kinetic_function); the Lovelock '
                       'corrections to the graviton operator are OPEN (not estimated); tree level (rho0 - 1 = 3.8e-4 is fitted)',
         'value': None, 'source': 'filled below'},
        v5, 1e-10, 'the stored Lambda and beta carry 12 digits and |d ln Lambda_W/d ln beta_W| = 1: rounding gives about 1e-12',
        extra='W %.1e, Z %.1e' % (res['W'], res['Z']))
    S['boson_entry'] = B.equations[-1]

    # ---- R6 fermions ----
    def Dfun(e, cL, cR):
        wL = mp.sqrt(cL ** 2 - e ** 2)
        wR = mp.sqrt(cR ** 2 - e ** 2)
        sL = mp.sinh(wL) / wL
        sR = mp.sinh(wR) / wR
        return e ** 2 * sL * sR - (mp.cosh(wL) - cL * sL) * (mp.cosh(wR) + cR * sR)
    fres = {}
    for n in sorted(masses['fermions']):
        F = masses['fermions'][n]
        cL, cR, e = mp.mpf(F['c_L']), mp.mpf(F['c_R']), mp.mpf(F['e_exact'])
        fun = lambda ee, cL=cL, cR=cR: Dfun(ee, cL, cR)
        fres[n] = float(abs(fun(e) / mp.diff(fun, e)) / e)
    nu = {k: v[0] for k, v in NUFIT60_NO.items()}
    Ump = mixing_matrix_mp(math.sqrt(nu['sin2_theta12']), math.sqrt(nu['sin2_theta13']), math.sqrt(nu['sin2_theta23']),
                           math.radians(nu['delta_CP_deg']))
    ck = {k: v[0] for k, v in CKM_PDG2024.items()}
    Vmp = mixing_matrix_mp(ck['s12'], ck['s13'], ck['s23'], ck['delta_rad'])
    Fm, dc = masses['fermions'], masses['doublet_c']
    sectors = {'neutrinos (kappa = U_PMNS)': ([dc['leptons']] * 3, [Fm['nu1']['c_R'], Fm['nu2']['c_R'], Fm['nu3']['c_R']], Ump),
               'charged leptons (kappa = 1)': ([dc['leptons']] * 3, [Fm['e']['c_R'], Fm['mu']['c_R'], Fm['tau']['c_R']], mp.eye(3)),
               'up quarks (kappa = 1)': ([dc['quarks']] * 3, [Fm['u']['c_R'], Fm['c']['c_R'], Fm['t']['c_R']], mp.eye(3)),
               'down quarks (kappa = V_CKM)': ([dc['quarks']] * 3, [Fm['d']['c_R'], Fm['s']['c_R'], Fm['b']['c_R']], Vmp)}
    three = {}
    vs1 = 0.0
    for name in sorted(sectors):
        cD, cR, K = sectors[name]
        tg = D['flavour']['three_generation_tip_condition'][name]
        w_ = 0.0
        for r in tg['roots']:
            r = mp.mpf(r)
            hstep = r * mp.mpf('1e-8')
            d0 = mp.det(tip_matrix(r, cD, cR, K))
            dd = (mp.det(tip_matrix(r + hstep, cD, cR, K)) - mp.det(tip_matrix(r - hstep, cD, cR, K))) / (2 * hstep)
            w_ = max(w_, float(abs(d0 / dd) / r))
        three[name] = w_
        vs1 = max(vs1, maxrel(zip(tg['roots'], tg['one_generation_roots'])))
    v6 = max(max(fres.values()), max(three.values()))
    kkmix = D['analysis']['kk_mixing_estimate']
    fo_dev = max(rel(F['e_first_order'], F['e_exact']) for F in Fm.values())
    B.equation(
        'fermion_x0_tip_determinant',
        'x0 eigenvalue problem of the twelve fermions: the tip mixing condition D(e) = 0 and the three-generation tip determinant',
        'FIELD_EQUATIONS section 6.2 (fermions) with 4.2 (the tip conditions b_L = kappa b_R, a_R = -kappa^dagger a_L); SOLUTION step 2 '
        '(fermions: masses and mixing of three generations)',
        {'description': 'exact lowest roots of D(e) = e^2 s_L s_R - kappa_f^2 (C_L - c_L s_L)(C_R + c_R s_R) with kappa_f = 1 (one doublet '
                        'localisation per sector, fitted singlet localisations); for a common doublet bulk mass and a unitary tip matrix '
                        'the 3 x 3 determinant factorises into these roots (kappa_nu = U_PMNS, kappa_d = V_CKM)',
         'method': 'mpmath root finding (60 digits; masses.json fermions) and the 3 x 3 determinant at 50 digits (flavour.json)',
         'order': 'exact on the static block (tree-level targets)'},
        {'definition': 'implied relative root error |D(e) / (e dD/de)| at the stored (c_L, c_R, e_exact) of the twelve fermions, and '
                       '|det / (e d det/de)| of the 3 x 3 tip determinant at the stored three-generation roots of the four sectors '
                       '(mpmath, 40 digits)',
         'value': v6, 'source': 'computed afresh by direct substitution',
         'details': {'one_generation': fres, 'three_generation_determinant': three,
                     'three_generation_roots_vs_one_generation_roots_stored': vs1}},
        {'definition': 'mixing with the Kaluza-Klein modes, (m_f/m_KK)^2 (analysis.json kk_mixing_estimate), largest for the top quark; '
                       'the first-order formula is not used (it would differ by up to %.1e); radiative running not included' % fo_dev,
         'value': max(kkmix.values()), 'where': max(kkmix, key=kkmix.get), 'source': 'analysis.json kk_mixing_estimate'},
        v6, 1e-9, 'the stored c_R carry 12 digits and |d ln e/d c_R| is about 1 for |c_R| up to 35: rounding alone gives up to 4e-11',
        extra='largest %s %.1e; three generations %.1e' % (max(fres, key=fres.get), max(fres.values()), max(three.values())))

    # ---- R7 dirac16complex ----
    sp_ = D['ks_spectrum']
    f = D['background']['casimir_type']['f_star']
    fL = f * L_CELL
    c = fL * 1.0
    P = sp_['p_dm'] * fL
    fP = lambda PP: c * mp.sin(PP) + PP * mp.cos(PP)
    impl_p = float(abs(fP(mp.mpf(P)) / mp.diff(fP, mp.mpf(P))) / P)
    Pex = brentq(lambda PP: c * math.sin(PP) + PP * math.cos(PP), 0.5 * math.pi + 1e-12, math.pi - 1e-12, xtol=1e-15, rtol=1e-15)
    pex = Pex / fL
    eps_dm = math.sqrt(1.0 + pex * pex)
    eps_even = math.sqrt(1.0 + (math.pi / fL) ** 2)
    dPdc = Pex / (c * c / math.cos(Pex) ** 2 + c)
    dlneps = (pex * pex / eps_dm ** 2) * (c * dPdc / Pex - 1.0)
    S['dm_orbital'] = (c, Pex, pex, eps_dm, fL)
    S['dlneps_dlnf_analytic'] = dlneps
    S['O_analytic'] = (1.0 + pex * dPdc) / eps_dm
    r7 = {'p_dm_implied': impl_p, 'eps_dm': rel(sp_['eps_dm'], eps_dm), 'eps_even_bulk': rel(sp_['eps_even_bulk'], eps_even),
          'fL_equals_3_f_star': rel(sp_['fL'], fL), 'x0_momentum_fraction': rel(sp_['x0_momentum_fraction_dm'], pex ** 2 / eps_dm ** 2)}
    v7 = max(r7.values())
    worst_shift = max(abs(v['d_eps_DM_over_M']) for v in D['coupled']['environments'].values())
    B.equation(
        'dirac16complex_x0_spectrum',
        'x0 spectrum of dirac16complex on the static block (fold zero mode, odd dark-matter level, even bulk levels)',
        'FIELD_EQUATIONS section 6.2 (the h_j operator with M = m) and 4.5 (fold and tip conditions of dirac16complex); SOLUTION step 2 '
        '(dirac16complex)',
        {'description': 'fold zero mode eps = 0; odd levels sqrt(m^2 + p^2) with tan(p f L) = -p/m (lowest %.9f m: the dark matter); even '
                        'bulk levels sqrt(m^2 + (n pi/(f L))^2)' % sp_['eps_dm'],
         'method': 'exact formulas, Brent root (ks/spectrum.json); the Kohn-Sham solver reproduces them to 1e-12', 'order': 'exact'},
        {'definition': 'implied relative error of the stored p_dm in c sin(P) + P cos(P) = 0 (P = p f L, c = m f L), and the stored eps_dm, '
                       'eps_even_bulk, f L and x0-momentum fraction against the closed forms (afresh)',
         'value': v7, 'source': 'computed afresh', 'details': r7},
        {'definition': 'largest shift of the dark-matter level by the Standard-Model mean fields over the ten environments, delta eps/M '
                       '(coupled.json; added as a correction in step 8)',
         'value': worst_shift, 'source': 'coupled.json environments d_eps_DM_over_M'},
        v7, 1e-10, 'all stored numbers carry 12 digits; the closed forms are exact', extra='p %.1e, eps %.1e' % (impl_p, r7['eps_dm']))


# ======================================================================================================================
# R8-R12 dirac16complex: Kohn-Sham states, gravity, portals, environments, the W with the dark-matter kinetic function
def kohn_sham(D, B, S):
    from um2_kohnsham import Cell, KSState
    f = D['background']['casimir_type']['f_star']
    vol7 = (2 * math.pi / DK) ** 3 * 1.0 * f ** 4
    g8 = D['ks_ground8']['N8_lamp']
    c = Cell(f=f, L=L_CELL, H=H1, m=1.0, nb=120, nq=1200)
    st = KSState(c, dk=DK, N=8, lam=LAM_B, n2max=1, vol7=vol7).label_set().scf(tol=1e-13, mix=0.5)
    E, _, _ = st.energy()
    hh, ll = st.homo_lumo()
    emt = st.emt()
    ints = {k: st.integrate(v) for k, v in emt.items()}
    # one more Kohn-Sham map on the converged densities (the solver's own measure: max |x_out - x_in| / max |x_out|)
    dM, v = st.potentials()
    secs = st.diagonalise(dM, v)
    occ = st.occupy(secs)
    n_new, S_new = st.densities(secs, occ)
    xin = np.concatenate([st.n, st.S])
    xout = np.concatenate([n_new, S_new])
    scf_res = float(np.max(np.abs(xout - xin)) / np.max(np.abs(xout)))
    # absolute differences in units of H: the eigenvalues of the 241 x 241 Kohn-Sham matrices (basis energies up to 583 H) carry an
    # absolute rounding error of order 1e-13 that depends on the BLAS kernel and threads (fixed to one thread here and in um2_ks_jobs.py)
    repro = {'E_KS': abs(E - g8['E_KS']), 'HOMO': abs(hh - g8['HOMO']), 'LUMO': abs(ll - g8['LUMO']), 'int_p0': abs(ints['p0'] - g8['int_p0']),
             'int_rho': abs(ints['rho'] - g8['int_rho'])}
    repro_rel = {'E_KS': rel(E, g8['E_KS']), 'HOMO': rel(hh, g8['HOMO']), 'int_p0': rel(ints['p0'], g8['int_p0'])}
    emax = max(float(np.max(np.abs(bs['E']))) for bs in c.basis.values())
    states = {}
    for src in ('ks_ground8', 'ks_ground592'):
        for k, s_ in D[src].items():
            if k.startswith('N'):
                states[k] = s_
    eid = max(abs(s_['E_KS'] - s_['int_rho']) / max(1.0, abs(s_['E_KS'])) for s_ in states.values())
    cons = max(abs(s_['cons_residual_richardson']) / s_['cons_scale'] for s_ in states.values() if s_['lambda'] != 0)
    runc = max(s_['E_KS_uncertainty'] / max(1.0, abs(s_['E_KS'])) for s_ in states.values())
    val_ = D['ks_validate']
    valid = max(max(rel(x['E'], x['E_ref']), abs(x['HOMO'] - x['HOMO_ref']), abs(x['LUMO'] - x['LUMO_ref']),
                    rel(x['p0_richardson'], x['p0_ref'])) for k, x in val_.items() if k.startswith('N'))
    lam_max = D['coupled']['self_interaction_channel']['lambda_max_for_vt1_H-6']
    dM_bound = D['ks_ground592']['N592_lamp']['max_abs_dM'] * lam_max / LAM_B
    v8 = max(scf_res, max(repro.values()), eid)
    S['ks_emax'] = emax
    B.equation(
        'kohn_sham_scf',
        'Kohn-Sham equations of dirac16complex on the static block (self-consistent densities, energy and energy-momentum tensor)',
        'FIELD_EQUATIONS section 7 (the Kohn-Sham equations, densities, E_KS, the energy-momentum tensor and the y-conservation law); '
        'SOLUTION step 3 (the Kohn-Sham equations, validation, ground states, dark-matter quanta)',
        {'description': 'Kohn-Sham orbitals of h_j with M_eff = m + (15/16) lambda S + <F>/Lambda*^3 and v = -(lambda/16) n + portal fields; '
                        'states N = 8 (k = 0 fold zero modes) and N = 592 (fold-band gas) with lambda = 0, +-lambda_B and the stress coupling; '
                        'eight dark-matter quanta in the lowest odd level',
         'method': 'Galerkin in the exact free eigenbasis (60/120/240 functions per sector), SCF to 1e-13 with safeguarded Anderson mixing, '
                   'Richardson in the basis size (ks/ground8.json, ground592.json, darkmatter.json)',
         'order': 'Kohn-Sham mean field (Hartree plus the exact local exchange of the contact interaction)'},
        {'definition': 'largest of: the N = 8, +lambda_B state re-solved with the same solver (120 functions per sector; the shells n2 >= 2 '
                       'are empty and omitted) against the stored E_KS, HOMO, LUMO, int p0, int rho (absolute, units of H); one further '
                       'Kohn-Sham map of the converged densities, max |x_out - x_in| / max |x_out| over x = (n, S); and the energy identity '
                       '|E_KS - 2 Vol7 int e^{3Hy} rho dy| / max(1, |E_KS|) over the eight stored states',
         'value': v8, 'source': 'computed afresh (re-solved state) and from ks/ground8.json, ks/ground592.json',
         'details': {'reproduction_N8_plus_lambda_B_absolute': repro, 'reproduction_relative': repro_rel,
                     'largest_basis_energy_over_H': emax, 'scf_map_residual': scf_res, 'energy_identity_max': eid,
                     'y_conservation_law_max_relative_richardson': cons, 'basis_richardson_uncertainty_max_relative': runc,
                     'record_reference_states_ks_validate': valid, 'iterations': st.iterations}},
        {'definition': 'self-interaction mean field at the assumed bound lambda <= %.2e H^-6 (coupled.json self_interaction_channel): the '
                       'largest |delta M| of the N = 592, +lambda_B state scaled by lambda_max/lambda_B (units of m); correlation beyond '
                       'the local exchange is not estimated (OPEN); y-conservation law %.1e; basis error %.1e' % (lam_max, cons, runc),
         'value': dM_bound, 'source': 'computed from ks/ground592.json and coupled.json'},
        v8, 1e-12, 'the solver converges to 1e-13 in the max norm, so one further map moves the densities by about the last step; with '
                   'one BLAS thread (here and in um2_ks_jobs.py) the re-solved state reproduces the stored one to its 12 digits (the LUMO '
                   '0.25 H is stored to 5e-13 H); another BLAS kernel rounds the eigenvalues of matrices with basis energies up to 583 H '
                   'differently by up to about 5e-13 H (as two threads did)',
        extra_ok=cons < 1e-6 and valid < 1e-8,
        extra='SCF map %.1e, reproduction %.1e H (%.1e relative), energy identity %.1e, conservation %.1e' % (
            scf_res, max(repro.values()), max(repro_rel.values()), eid, cons))

    # ---- R9 the Kohn-Sham source in the block response ----
    bg = D['background']
    lr = bg['linear_response_static_dk']
    c_rho, c_3, c_p = lr['per_kappa_drho_H2'], lr['per_kappa_dp3_H2'], lr['per_kappa_dpbar_H2']
    fb = D['ks_feedback']
    gs = dict(D['ks_ground8'])
    gs.update(D['ks_ground592'])
    w = 2 * vol7 * (1 - math.exp(-3 * H1 * L_CELL)) / (3 * H1)
    avg_dev = 0.0
    dk_dev = 0.0
    dkv = {}
    for key in ('N8_lamp', 'N592_lamp', 'N592_lam0'):
        rho = gs[key]['int_rho'] / w
        p3 = gs[key]['int_p3'] / w
        pbar = (gs[key]['int_p0_richardson'] / w + 3 * gs[key]['int_pt'] / w) / 4
        avg_dev = max(avg_dev, maxrel([(rho, fb[key]['rho_avg']), (p3, fb[key]['p3_avg']), (pbar, fb[key]['pbar_avg'])]))
        dk = c_rho * rho + c_3 * p3 + c_p * pbar
        dkv[key] = (dk, abs(c_rho * rho))
        if key != 'N592_lam0':
            dk_dev = max(dk_dev, rel(dk, fb[key]['dk_full_per_unit_kappa']))
    free_gas = abs(dkv['N592_lam0'][0]) / dkv['N592_lam0'][1]
    S['ks_avg_dev'] = avg_dev
    dmq = D['ks_darkmatter']['0']
    shape = {'N592_lamp': abs(fb['N592_lamp']['shape_source_p0_minus_pt'] / fb['N592_lamp']['pbar_avg']),
             'N8_lamp': abs(fb['N8_lamp']['shape_source_p0_minus_pt'] / fb['N8_lamp']['pbar_avg']),
             'dark_matter_lambda_0': abs((dmq['p0_over_rho'] - dmq['pt_over_rho']) / ((dmq['p0_over_rho'] + 3 * dmq['pt_over_rho']) / 4))}
    v9 = max(dk_dev, free_gas)
    B.equation(
        'kohn_sham_in_gravity_block_response',
        'the Kohn-Sham energy-momentum tensor as the source of the background equations (adiabatic block response)',
        'FIELD_EQUATIONS section 7 (the Kohn-Sham source enters the background equations through its block averages rho, p3, pbar) with '
        '5.5; SOLUTION step 3 (back-reaction on the block)',
        {'description': 'dk = (c_rho kappa rho + c_3 kappa p3 + c_p kappa pbar)/H^2 with the cell averages of the Kohn-Sham EMT, pbar = '
                        '(p0 + 3 p_t)/4; radiation (w = 1/3) drops out (c_3 = -3 c_rho)',
         'method': 'cell averages of the integrated EMT (ks/feedback.json from ks/ground8.json, ks/ground592.json)', 'order': 'first order'},
        {'definition': 'largest of |dk recomputed from the stored Kohn-Sham integrals with the background coefficients / dk stored - 1| '
                       '(N = 8 and N = 592 with +lambda_B) and, for the free fold-band gas (w = 1/3), |dk| / |c_rho kappa rho| (the '
                       'cancellation of radiation)',
         'value': v9, 'source': 'computed afresh from ks/ground*.json and background.json',
         'details': {'dk_recomputed_vs_stored': dk_dev, 'free_gas_cancellation': free_gas,
                     'dk_per_unit_kappa': {k: x[0] for k, x in dkv.items()}}},
        {'definition': 'the block-shape source p0 - p_t, which the order-0 metric cannot absorb (OPEN), against the kept hidden pressure pbar: '
                       'NOT small (about 0.9 for the self-interacting test states and 4 for non-relativistic dark matter, whose p_t = 0); '
                       'its absolute size is suppressed like that of pbar (kappa p/kappa rho_b <= %.0e at the freeze-out), if the shape '
                       'mode is stable (OPEN)' % S['src_ratio_max'],
         'value': max(shape.values()), 'ratios': shape, 'source': 'ks/feedback.json shape_source_p0_minus_pt, ks/darkmatter.json'},
        v9, 1e-9, 'both are products of stored 12-digit numbers; radiation cancels exactly (c_3 = -3 c_rho), so the free gas leaves '
                  'only rounding of terms of order 0.5',
        extra='dk %.1e, free gas %.1e; shape source / pbar up to %.2f (OPEN)' % (dk_dev, free_gas, max(shape.values())))


def portals_and_environments(D, B, S):
    masses = D['masses']
    cp = D['coupled']
    c, P, p, eps, fL = S['dm_orbital']
    e_ = eps * fL
    f = D['background']['casimir_type']['f_star']
    # Gauss-Legendre panels on [-L, 0], refined towards the fold (the sharpest profile has width L/(2 c) = 0.043)
    xg, wg = np.polynomial.legendre.leggauss(400)
    edges = [-L_CELL, -1.5, -0.6, -0.25, -0.1, -0.03, 0.0]
    y = np.concatenate([0.5 * (b - a) * xg + 0.5 * (b + a) for a, b in zip(edges[:-1], edges[1:])])
    w = np.concatenate([0.5 * (b - a) * wg for a, b in zip(edges[:-1], edges[1:])])
    xi = y / L_CELL
    aD = np.sin(P * xi)
    bD = (c * np.sin(P * xi) - P * np.cos(P * xi)) / e_
    nD = float(np.sum(w * (aD ** 2 + bD ** 2)))
    aD, bD = aD / math.sqrt(nD), bD / math.sqrt(nD)
    aF = np.exp(c * xi)
    aF = aF / math.sqrt(float(np.sum(w * aF ** 2)))
    bF = np.zeros_like(y)
    q1 = math.pi / fL
    eps1 = math.sqrt(1.0 + q1 * q1)
    aE = np.cos(f * q1 * y) + (1.0 / q1) * np.sin(f * q1 * y)
    bE = (eps1 / q1) * np.sin(f * q1 * y)
    nE = math.sqrt(float(np.sum(w * (aE ** 2 + bE ** 2))))
    aE, bE = aE / nE, bE / nE

    def prof(cz):
        return (2 * cz / L_CELL) * np.exp(2 * cz * y / L_CELL) / (1 - math.exp(-2 * cz))
    F = masses['fermions']
    zm = {'Q (quark doublets)': masses['doublet_c']['quarks'], 'L (lepton doublets)': masses['doublet_c']['leptons']}
    for n_ in ('u', 'c', 't', 'd', 's', 'b', 'e', 'mu', 'tau', 'nu1', 'nu2', 'nu3'):
        zm['%s_R' % n_] = -F[n_]['c_R']
    orbs = {'dark matter (lowest odd level)': (aD, bD), 'fold band (zero mode)': (aF, bF), 'first even bulk level': (aE, bE)}
    devI = devIb = 0.0
    for on in sorted(orbs):
        a, b = orbs[on]
        for zn in sorted(zm):
            wt = w * prof(zm[zn]) * np.exp(-3 * H1 * y)
            devI = max(devI, rel(float(np.sum(wt * (a * a + b * b))), cp['overlaps_Itilde'][on][zn]))
            sb = cp['overlaps_Itilde_b'][on][zn]
            Ib = float(np.sum(wt * b * b))
            devIb = max(devIb, rel(Ib, sb) if sb != 0 else abs(Ib))
    Ilam = float(np.sum(w * (aD * bF + bD * aF) ** 2 * np.exp(-3 * H1 * y)))
    devlam = rel(Ilam, cp['self_interaction_channel']['Itilde_lambda'])
    O_ks = D['ks_portals']['I12 gluon condensate <G G> (M, uniform)']['hellmann_feynman']
    devO = rel(S['O_analytic'], O_ks)
    fd_I11 = max(rel(x['finite_difference'], x['overlap']) for x in cp['overlap_checks_finite_amplitude'])
    fd_I13 = max(rel(x['finite_difference'], x['overlap_b']) for x in cp['I13_checks'])
    S['dm_orbital_arrays'] = (y, w, aD, bD)
    scr = abs(cp['screened_response_Q']['interacting'] / cp['screened_response_Q']['bare'] - 1)
    lam_max = cp['self_interaction_channel']['lambda_max_for_vt1_H-6']
    v10 = max(devI, devIb, devlam, devO)
    B.equation(
        'portal_overlaps_hellmann_feynman',
        'the portals I11, I13 on the zero modes and I12 on the dark-matter level: overlaps as Hellmann-Feynman responses',
        'FIELD_EQUATIONS section 7.1 (Itilde_of, Itilde^(b)_of, G_V, G_A; I12: O = d eps_DM/dm) and section 10 (Itilde_lambda); SOLUTION '
        'step 3 (the Standard-Model fields acting on dirac16complex) and step 8 (the portals on the zero modes)',
        {'description': 'Itilde_of = int (a_o^2 + b_o^2) rho_f e^{-3Hy} dy, Itilde^(b)_of = int b_o^2 rho_f e^{-3Hy} dy for the dark-matter level, '
                        'the fold band and the first even bulk level against the zero modes of all multiplets; Itilde_lambda = int s_DF^2 '
                        'e^{-3Hy} dy; O = d eps_DM/dm = %.9f' % O_ks,
         'method': 'quadrature of the exact free orbitals (80 basis functions per sector, 800 Gauss nodes; coupled.json overlaps_Itilde, '
                   'overlaps_Itilde_b, self_interaction_channel), self-consistent Kohn-Sham finite differences as checks (coupled.json, '
                   'ks/portals.json)', 'order': 'linear response (exact for the physical amplitudes)'},
        {'definition': 'the overlaps recomputed from the closed-form orbitals (odd level a = sin P xi, b = (c sin P xi - P cos P xi)/e; fold '
                       'zero mode (e^{c xi}, 0); first even level) and profiles with 2400 Gauss nodes refined at the fold: max relative '
                       'deviation of Itilde, Itilde^(b), Itilde_lambda from the stored values, and O from tan(p f L) = -p/m in closed '
                       'form against the Hellmann-Feynman value of ks/portals.json',
         'value': v10, 'source': 'computed afresh',
         'details': {'Itilde': devI, 'Itilde_b': devIb, 'Itilde_lambda': devlam, 'O_analytic_vs_ks': devO, 'O_analytic': S['O_analytic'],
                     'stored_Kohn_Sham_finite_differences_I11': fd_I11, 'stored_Kohn_Sham_finite_differences_I13': fd_I13}},
        {'definition': 'screening of the response by the interacting dirac16complex gas, measured at lambda_B (coupled.json '
                       'screened_response_Q) and scaled to the assumed bound lambda <= %.2e H^-6; the response is linear at the physical '
                       'amplitudes' % lam_max,
         'value': scr * lam_max / LAM_B, 'at_lambda_B': scr, 'source': 'coupled.json screened_response_Q'},
        v10, 1e-9, 'the same integrals of exact functions: the stored ones (800 Gauss nodes, 12 digits) and the afresh ones must agree '
                   'to the quadrature and storage precision',
        extra='Itilde %.1e, Itilde^(b) %.1e, O %.1e' % (devI, devIb, devO))

    # ---- R11 environments ----
    HBARC_CM = val('hbar_c_GeV_m') * 100.0
    cm3 = HBARC_CM ** 3
    Idm = cp['overlaps_Itilde']['dark matter (lowest odd level)']
    Ibd = cp['overlaps_Itilde_b']['dark matter (lowest odd level)']
    GV = cp['freeze_in']['G_V_benchmark_GeV-2']
    GA = cp['I13']['G_A_GeV-2']
    cL3 = D['thermal']['I12_universal_benchmark']['c_over_Lambda_star3_GeV-3']
    brc = cp['block_response_coefficients']
    kV = brc['kappa_over_Vperp_GeV-2']
    HG = masses['scales']['H_GeV']
    kst = D['background']['casimir_type']['k_star_value']
    MDM = D['ks_spectrum']['eps_dm'] * HG
    devs = {'I11': 0.0, 'I13': 0.0, 'I12': 0.0, 'dM_I12': 0.0, 'delta_k': 0.0, 'delta_ln_f': 0.0, 'over_M': 0.0, 'self_consistent': 0.0,
            'GG_vacuum': 0.0}
    brackets = {}
    for k_ in sorted(cp['environments']):
        e = cp['environments'][k_]
        nn = {kk: e['densities_cm3'][kk] * cm3 for kk in ('n_p', 'n_n', 'n_e')}
        nu_, nd_ = 2 * nn['n_p'] + nn['n_n'], nn['n_p'] + 2 * nn['n_n']
        b11 = ((1 / 3.) * nu_ * 0.5 * (Idm['Q (quark doublets)'] + Idm['u_R']) + (1 / 3.) * nd_ * 0.5 * (Idm['Q (quark doublets)'] + Idm['d_R'])
               - nn['n_e'] * 0.5 * (Idm['L (lepton doublets)'] + Idm['e_R']))
        b13 = (1 / 3.) * nu_ * 0.5 * (Ibd['Q (quark doublets)'] + Ibd['u_R']) + (1 / 3.) * nd_ * 0.5 * (Ibd['Q (quark doublets)'] + Ibd['d_R'])
        brackets[k_] = (b11, b13)
        cd = e['condensates_GeV4']
        dM = cL3 * (cd['GG'] + cd['WW'] + cd['BB'])
        src = e['sources_GeV4']
        dk = (brc['c_rho'] * kV * src['rho'] + brc['c_3'] * kV * src['p3'] + brc['c_p'] * kV * src['pbar']) / HG ** 2
        dlnf = -dk / (2 * kst)
        devs['I11'] = max(devs['I11'], rel(GV * b11, e['d_eps_DM_I11_GeV']))
        devs['I13'] = max(devs['I13'], rel(GA * b13, e['d_eps_DM_I13_GeV']))
        devs['dM_I12'] = max(devs['dM_I12'], rel(dM, e['dM_I12_GeV']))
        devs['I12'] = max(devs['I12'], rel(O_HARDCODED * dM, e['d_eps_DM_I12_GeV']))
        devs['delta_k'] = max(devs['delta_k'], rel(dk, e['delta_k']))
        devs['delta_ln_f'] = max(devs['delta_ln_f'], rel(dlnf, e['delta_ln_f']))
        devs['over_M'] = max(devs['over_M'], rel((GV * b11 + GA * b13 + O_HARDCODED * dM) / MDM, e['d_eps_DM_over_M']))
        devs['self_consistent'] = max(devs['self_consistent'], rel(e['delta_ln_f_self_consistent'], e['delta_ln_f']))
        if e['T_GeV'] == 0.0:
            devs['GG_vacuum'] = max(devs['GG_vacuum'], rel(0.012 * 4 * math.pi ** 2, cd['GG']))
    S['env_brackets'] = brackets
    gain = max(v['loop_gain'] for v in cp['environments'].values())
    worst = max(abs(v['d_eps_DM_over_M']) for v in cp['environments'].values())
    v11 = max(devs.values())
    B.equation(
        'coupled_environment_mean_fields',
        'the Kohn-Sham levels in the mean fields of the Standard-Model fields of an environment, with the block response to every species',
        'FIELD_EQUATIONS section 7.1 (the mean fields of an environment, the condensates, gravity closes the loop, the hidden pressure, the '
        'nucleon) and section 11 item 6; SOLUTION step 8 (the mean fields of the Standard-Model fields; dirac16complex acting on the Standard '
        'Model, and gravity)',
        {'description': 'delta eps = sum_f (G_V q_f Itilde + G_A q^B_f Itilde^(b)) n_f + O (c/Lambda*^3)(<g_s^2 GG> + <g^2 WW> + <g\'^2 BB>) in '
                        'ten environments; dk = (c_rho kappa drho + c_3 kappa dp3 + c_p kappa dpbar)/H^2 from all species, delta ln f = '
                        '-dk/(2 k*), iterated with the masses',
         'method': 'closed formulas with the overlaps, the benchmark strengths G_V = %.3e, G_A = %.3e GeV^-2, c/Lambda*^3 = %.3e GeV^-3 '
                   '(coupled.json environments; 2 iterations each)' % (GV, GA, cL3), 'order': 'first order in the mean fields, iterated'},
        {'definition': 'every stored mean-field shift and block response recomputed from the stored overlaps, strengths, densities, '
                       'condensates and sources: max relative deviation over the ten environments of delta eps_I11, delta eps_I13, '
                       'delta eps_I12 (with O = 0.7072 as coded), dM_I12, delta k, delta ln f, delta eps/M, the vacuum condensate '
                       '<g_s^2 GG> = 0.012 x 4 pi^2 GeV^4, and |delta ln f (iterated) / delta ln f (one step) - 1|',
         'value': v11, 'source': 'computed afresh from coupled.json and thermal.json', 'details': devs},
        {'definition': 'the gain of the loop mass -> source -> block -> mass (the relative size of each further iteration), coupled.json '
                       'loop_gain; second order in the mean fields (delta eps/M)^2 = %.1e; the neglected inertia of the block '
                       '(H_Hubble/m_r)^2 = %.0e at the freeze-out' % (worst ** 2, S['adiabaticity_fo']),
         'value': gain, 'source': 'coupled.json'},
        v11, 1e-9, 'products and sums of stored 12-digit numbers; the iteration has converged when the iterated and the one-step block '
                   'shifts agree to the loop gain (1e-33)',
        extra='largest %s %.1e' % (max(devs, key=devs.get), v11))

    # ---- R12 the W with the dark-matter kinetic function ----
    WZ = masses['WZ']
    eta = ETA
    a_ = 1.5 * eta
    LW = WZ['Lambda_W']
    beta = WZ['beta_W']
    kap = math.sqrt(a_ * a_ - LW)
    xg2, wg2 = np.polynomial.legendre.leggauss(800)
    xx = 0.5 * (xg2 - 1.0)
    wx = 0.5 * wg2

    def uW(x_):
        return np.exp(-a_ * x_) * (np.cosh(kap * x_) + (a_ / kap) * np.sinh(kap * x_))

    def upW(x_):
        # kappa - a^2/kappa = -Lambda/kappa, written without the cancellation of two numbers close to 4.5
        return -(LW / kap) * np.exp(-a_ * x_) * np.sinh(kap * x_)
    nrm_y = L_CELL * float(np.sum(wx * (np.sin(P * xx) ** 2 + ((c * np.sin(P * xx) - P * np.cos(P * xx)) / e_) ** 2)))

    def s_dm(x_):
        return 2 * np.sin(P * x_) * (c * np.sin(P * x_) - P * np.cos(P * x_)) / e_ / nrm_y

    def ds_dm(x_):
        a0, b0 = math.sin(P * x_), (c * math.sin(P * x_) - P * math.cos(P * x_)) / e_
        da, db = P * math.cos(P * x_), (c * P * math.cos(P * x_) + P * P * math.sin(P * x_)) / e_
        return 2 * (da * b0 + a0 * db) / nrm_y
    wt = np.exp(3 * eta * xx)
    u, up = uW(xx), upW(xx)
    dlnL_pt = float((np.sum(wx * s_dm(xx) * wt * up ** 2) - LW * np.sum(wx * s_dm(xx) * wt * u ** 2)) / np.sum(wx * wt * u ** 2)) / LW
    tip_check = rel(float(upW(-1.0) / uW(-1.0)), beta)

    def mismatch(Lam, amp):
        def rhs(x_, Y):
            K = 1.0 + amp * float(s_dm(x_))
            return [Y[1], -(3 * eta + amp * ds_dm(x_) / K) * Y[1] - Lam * Y[0]]
        sol = solve_ivp(rhs, (0.0, -1.0), [1.0, 0.0], method='DOP853', rtol=1e-13, atol=1e-16)
        u1, up1 = sol.y[:, -1]
        return (1.0 + amp * float(s_dm(-1.0))) * up1 - beta * u1

    def eig(amp):
        return brentq(lambda Lm: mismatch(Lm, amp), LW * 0.99, LW * 1.01, xtol=1e-22, rtol=1e-14)
    L0 = eig(0.0)
    S['L0_shoot'] = L0
    dd = {a: (eig(a) - eig(-a)) / (2 * a) / L0 for a in (1e-3, 2e-3)}
    dlnL_shoot = (4 * dd[1e-3] - dd[2e-3]) / 3
    stored = cp['WZ_kinetic_shift']['dlnLambdaW_damp']
    photon = cp['WZ_kinetic_shift']['photon_Lambda_with_K']
    dev_stored = rel(stored, dlnL_pt)
    e_fo = max(cp['WZ_kinetic_shift']['amplitude_e_by_environment'].values())
    S['dlnLW_de'] = dlnL_pt
    S['boson_entry']['neglected']['value'] = e_fo * abs(dlnL_pt)
    S['boson_entry']['neglected']['source'] = 'computed (coupled.json amplitude at the freeze-out times the coefficient of R12)'
    v12 = dev_stored
    B.equation(
        'wz_x0_with_dark_matter_kinetic_function',
        'x0 eigenvalue problem of the W (and Z, photon) with the kinetic function K = 1 + e s_DM(y) of the dark-matter scalar density',
        'FIELD_EQUATIONS section 7.1 (Psi acting on the x0 problem of the W and Z: -(1/(K e^{3 eta xi}))(K e^{3 eta xi} u\')\' = Lambda u, '
        'K(-1) u\'(-1) = beta u(-1)); SOLUTION step 8 (dirac16complex acting on the Standard Model)',
        {'description': 'd ln Lambda_W/de = %.9f (stored), photon Lambda = %.1f at e = 0.01 (exact value 0)' % (stored, photon),
         'method': 'first-order perturbation theory of the Sturm-Liouville problem with the exact W eigenfunction and the dark-matter '
                   'orbital on the 800 Gauss nodes of the Kohn-Sham cell; the photon zero mode u = 1 solves the problem for every K '
                   '(coupled.json WZ_kinetic_shift)', 'order': 'first order in e (the physical e <= %.1e)' % e_fo},
        {'definition': '|stored d ln Lambda_W/de / afresh - 1|, afresh = the same first-order formula [int s w u\'^2 - Lambda int s w '
                       'u^2]/(Lambda int w u^2), w = e^{3 eta xi}, evaluated independently with the closed-form orbital (800 Gauss nodes '
                       'on the cell) and the exact W eigenfunction (tip condition reproduced to %.0e); confirmed by shooting the '
                       'perturbed problem (DOP853, rtol 1e-13, Richardson in e): %.9f. The photon zero mode has u\' = 0, so its shift '
                       'vanishes exactly (stored: %.1f)' % (tip_check, dlnL_shoot, photon),
         'value': v12, 'source': 'computed afresh',
         'details': {'first_order_perturbation': dlnL_pt, 'shooting_richardson': dlnL_shoot, 'stored': stored,
                     'shooting_vs_perturbation': rel(dlnL_shoot, dlnL_pt), 'photon_Lambda_stored': photon,
                     'shooting_unperturbed_Lambda_W_vs_x0': rel(L0, LW)}},
        {'definition': 'the physical amplitude at the dark-matter freeze-out times the coefficient: delta ln Lambda_W = e |d ln Lambda_W/de|',
         'value': e_fo * abs(dlnL_pt), 'source': 'coupled.json WZ_kinetic_shift.amplitude_e_by_environment'},
        v12, 1e-9, 'the same first-order integral of exact functions on two independent 800-node quadratures, stored to 12 digits; '
                   'shooting, whose finite differences in e carry about 1e-11, must agree to 1e-8',
        extra_ok=rel(dlnL_shoot, dlnL_pt) < 1e-8 and photon == 0.0,
        extra='stored %.9f, first order %.9f, shooting %.9f, photon %.1f' % (stored, dlnL_pt, dlnL_shoot, photon))


# ======================================================================================================================
# R13-R16 electroweak widths, linear cosmology, graviton tower, metric series
def electroweak_cosmology_series(D, B, S):
    ew = D['electroweak']['Z_widths_tree_MeV']
    GF, mZ, s2 = val('G_F_GeV-2'), val('m_Z_GeV'), val('sin2_theta_W_MSbar')

    def widths(s2_, mZ_):
        G0 = GF * mZ_ ** 3 / (6 * math.sqrt(2) * math.pi)
        wdt = lambda T3, Q, Nc: Nc * G0 * ((T3 - 2 * Q * s2_) ** 2 + T3 ** 2) * 1e3
        nu_, l_, u_, d_ = wdt(0.5, 0, 1), wdt(-0.5, -1, 1), wdt(0.5, 2 / 3., 3), wdt(-0.5, -1 / 3., 3)
        had = 2 * u_ + 3 * d_
        qcd = 1 + val('alpha_s_mZ') / math.pi
        return {'nu (each of 3)': nu_, 'charged lepton (each of e, mu, tau)': l_, 'up-type quark (each of u, c)': u_,
                'down-type quark (each of d, s, b)': d_, 'invisible (3 nu)': 3 * nu_, 'hadronic': had, 'total': 3 * nu_ + 3 * l_ + had,
                'hadronic_with_QCD_factor': qcd * had, 'total_with_QCD_factor': 3 * nu_ + 3 * l_ + qcd * had,
                'R_l_with_QCD_factor': qcd * had / l_}
    wd = widths(s2, mZ)
    dev_w = maxrel((wd[k], ew[k]) for k in wd)
    dev_mZ = rel(S['mZ_x0'], val('m_Z_GeV'))
    loops = (ew['measured_total'] - ew['total_with_QCD_factor']) / ew['measured_total']
    mb = val('m_b_GeV_mb')
    bq = 1 - 4 * mb ** 2 / mZ ** 2
    beta_b = math.sqrt(bq)
    gVb, gAb = -0.5 + 2 / 3. * s2, -0.5
    mass_b = beta_b * ((3 - bq) / 2 * gVb ** 2 + bq * gAb ** 2) / (gVb ** 2 + gAb ** 2) - 1
    mass_b_total = mass_b * wd['down-type quark (each of d, s, b)'] / wd['total_with_QCD_factor']
    as2 = 1.409 * (val('alpha_s_mZ') / math.pi) ** 2 * wd['hadronic'] / wd['total_with_QCD_factor']
    S['widths'] = widths
    v13 = max(dev_w, dev_mZ)
    B.equation(
        'yang_mills_masses_and_widths',
        'Yang-Mills equations with the tip mass terms: W and Z masses and the tree-level Z widths of three generations',
        'FIELD_EQUATIONS section 4.3 (the gauge fields; unitary gauge Sigma = 1, section 2) and 6.1; SOLUTION step 2 (W, Z) and step 4 '
        '(the Z widths of three generations)',
        {'description': 'm_Z = m_W sqrt(Lambda_Z/Lambda_W) = %.6f GeV; Gamma(Z -> f fbar) = N_c G_F m_Z^3 (g_V^2 + g_A^2)/(6 sqrt2 pi), '
                        'g_V = T3 - 2 Q sin^2(theta_W) (MS-bar 0.23122), g_A = T3, massless fermions; hadronic with 1 + alpha_s/pi' % S['mZ_x0'],
         'method': 'closed formulas (electroweak.json Z_widths_tree_MeV)', 'order': 'tree level (QCD factor 1 + alpha_s/pi for comparison)'},
        {'definition': 'max relative deviation of the stored widths (each channel, invisible, hadronic, totals, R_l) from the formula '
                       'recomputed with the stored inputs, and |m_W sqrt(Lambda_Z/Lambda_W) / m_Z(measured) - 1| with the stored x0 '
                       'eigenvalues',
         'value': v13, 'source': 'computed afresh', 'details': {'widths': dev_w, 'm_Z': dev_mZ}},
        {'definition': 'electroweak loop corrections, (measured - computed with the QCD factor)/measured total width; the b-quark mass in '
                       'Gamma(Z -> b bbar) (m_b(m_b) = 4.183 GeV) relative to the total; the O(alpha_s^2) QCD term 1.409 (alpha_s/pi)^2 of '
                       'the hadronic width relative to the total',
         'value': loops, 'b_quark_mass_relative_to_total': mass_b_total, 'alpha_s_squared_relative_to_total': as2,
         'source': 'computed from electroweak.json and the inputs'},
        v13, 1e-9, 'the same formulas with the same 12-digit inputs; m_Z is reproduced by construction of the fit (to 1e-8 in um2_spectra.py)',
        extra='widths %.1e, m_Z %.1e; loop corrections %.2f %%' % (dev_w, dev_mZ, 100 * loops))

    # ---- R14 linear perturbations ----
    cos = D['cosmology']
    m1 = cos['models'][1]
    dphi = m1['Delta_Phi_z0']
    pois = max(rel(r['Delta_Phi_Poisson'], r['Delta_Phi_Weyl']) for r in dphi if r['k_Mpc-1'] >= 0.01)
    As = math.exp(3.044) * 1e-10
    ns = 0.9649
    r0 = dphi[0]
    Om = m1['Omega_m_total']
    Ea = lambda a: math.sqrt(Om * a ** -3 + 1 - Om)
    g0 = 2.5 * Om * Ea(1.0) * quad(lambda b: 1 / (b * Ea(b)) ** 3, 0, 1, epsabs=0, epsrel=1e-12)[0]
    large = rel(0.6 * math.sqrt(As) * (r0['k_Mpc-1'] / 0.05) ** ((ns - 1) / 2) * g0, r0['Delta_Phi_Weyl'])
    it = m1['camb_mass_iteration'][-1]
    S['Delta_Phi_max'] = r0['Delta_Phi_Weyl']
    v14 = pois
    B.equation(
        'linear_perturbations_cmb_bao',
        'linear (order epsilon) Einstein-Boltzmann equations of the four-dimensional effective theory: CMB, CNB, BAO, sigma_8',
        'FIELD_EQUATIONS section 8 (the linear perturbations: Einstein equations in the Newtonian gauge, photons, baryons, cold dark '
        'matter, three massive neutrino hierarchies, the freeze-in fold bands); SOLUTION step 6',
        {'description': 'CAMB 2.0.5 with the three neutrino mass states (each N_eff/3), N_eff = 3.0432 + 0.0010, the Planck 2018 omega_b, '
                        'omega_c, theta, tau, A_s, n_s; Delta_Phi(k) from the Weyl potential (cosmology.json models[1])',
         'method': 'Einstein-Boltzmann solver CAMB (default accuracy, lensing)', 'order': 'first order in epsilon'},
        {'definition': 'the stored first-order solution in the Poisson equation Phi = (3/2) Omega_m H0^2 delta_m/(a k^2): max over k >= 0.01 '
                       'Mpc^-1 of |Delta_Phi(Poisson) / Delta_Phi(Weyl) - 1| (cosmology.json models[1].Delta_Phi_z0); on the largest scale '
                       'the matter-era solution (3/5) A_s^{1/2} (k/k0)^{(n_s-1)/2} g(0), g(0) recomputed from Omega_m',
         'value': v14, 'source': 'computed afresh from cosmology.json',
         'details': {'poisson_k_ge_0.01': pois, 'matter_era_limit_k_1e-4': large, 'g0_recomputed': g0,
                     'g0_stored': cos['growth_suppression_g0'], 'camb_neutrino_mass_iteration_last': it}},
        {'definition': 'order epsilon^2 relative to order epsilon: Delta_Phi on the largest scale (series.json order2 = Delta_Phi^2 relative to '
                       'order 0); the Kaluza-Klein modes and the radion (>= 48 TeV) are absent at cosmological scales',
         'value': r0['Delta_Phi_Weyl'], 'source': 'cosmology.json'},
        v14, 1e-4, 'a first-order potential inconsistent with the first-order density beyond 1e-4 would show at a tenth of the CAMB default '
                   'accuracy (about 1e-3); the matter-era limit neglects 1 - T(k) ~ (k/k_eq)^2 and radiation, about 1e-4 at k = 1e-4 Mpc^-1',
        extra_ok=large < 1e-3 and it < 1e-10 and rel(g0, cos['growth_suppression_g0']) < 1e-9,
        extra='Poisson %.1e, matter-era limit %.1e, CAMB mass iteration %.1e' % (pois, large, it))

    # ---- R15 graviton tower ----
    ser = D['series']
    eta = ETA
    a_ = 1.5 * eta
    xg, wg = np.polynomial.legendre.leggauss(600)
    xx = 0.5 * (xg - 1)
    wx = 0.5 * wg
    grid = np.linspace(-1.0, 0.0, 2001)
    ode = bc = 0.0
    ndev = adev = orth = 0.0
    N0 = (1 - math.exp(-3 * eta)) / (3 * eta)
    cQ, cL = D['masses']['doublet_c']['quarks'], D['masses']['doublet_c']['leptons']
    prof = lambda c_, x_: 2 * c_ * np.exp(2 * c_ * x_) / (1 - math.exp(-2 * c_))
    for lv in ser['kaluza_klein_gravitons'][1:]:
        n = lv['n']
        q = n * math.pi
        Lam = lv['Lambda_n']
        u = lambda x_: np.exp(-a_ * x_) * (np.cos(q * x_) + (a_ / q) * np.sin(q * x_))
        up = lambda x_: -np.exp(-a_ * x_) * (q + a_ * a_ / q) * np.sin(q * x_)
        upp = lambda x_: np.exp(-a_ * x_) * (a_ * (q + a_ * a_ / q) * np.sin(q * x_) - q * (q + a_ * a_ / q) * np.cos(q * x_))
        r_ = upp(grid) + 3 * eta * up(grid) + Lam * u(grid)
        ode = max(ode, float(np.max(np.abs(r_) / (np.abs(upp(grid)) + np.abs(3 * eta * up(grid)) + np.abs(Lam * u(grid))))))
        bc = max(bc, abs(float(up(0.0))) / float(np.max(np.abs(up(grid)))), abs(float(up(-1.0))) / float(np.max(np.abs(up(grid)))))
        wt = np.exp(3 * eta * xx)
        Nn = float(np.sum(wx * wt * u(xx) ** 2))
        ndev = max(ndev, rel(Nn, 0.5 * (1 + a_ * a_ / (q * q))), rel(lv['N_n'], 0.5 * (1 + a_ * a_ / (q * q))))
        orth = max(orth, abs(float(np.sum(wx * wt * u(xx)))) / float(np.sum(wx * wt)))
        aq = (N0 / Nn) * float(np.sum(wx * prof(cQ, xx) * u(xx))) ** 2
        al = (N0 / Nn) * float(np.sum(wx * prof(cL, xx) * u(xx))) ** 2
        adev = max(adev, rel(aq, lv['alpha_quark_doublet']), rel(al, lv['alpha_lepton_doublet']), rel(N0 / Nn, lv['alpha_fold_point']),
                   rel(Lam, 9 * eta ** 2 / 4 + q * q))
    v15 = max(ode, bc, orth, ndev)
    B.equation(
        'graviton_tower',
        'Kaluza-Klein graviton tower (n >= 1 terms of the first-order metric) and the Yukawa strengths of a static source',
        'FIELD_EQUATIONS section 8.1 (beyond n = 0: the Kaluza-Klein gravitons and the radion) with 6.1 (beta = 0); SOLUTION step 10',
        {'description': 'u_n = e^{-a xi}(cos q_n xi + (a/q_n) sin q_n xi), q_n = n pi, a = 3 eta/2, Lambda_n = 9 eta^2/4 + n^2 pi^2, N_n = '
                        '(1 + a^2/q_n^2)/2, alpha_n = (N_0/N_n)(int rho_M u_n)(int rho_m u_n) (series.json kaluza_klein_gravitons)',
         'method': 'exact eigenfunctions (finite elements as a check)', 'order': 'exact (Einstein-gravity operator)'},
        {'definition': 'the stored profiles in -e^{-3 eta xi}(e^{3 eta xi} u\')\' = Lambda_n u: max |u\'\' + 3 eta u\' + Lambda_n u| / max |Lambda_n u| '
                       'on 2001 points (analytic derivatives), the fold and tip conditions u\'(0) = u\'(-1) = 0 relative to max |u\'|, the '
                       'orthogonality to the flat profile and N_n by Gauss-Legendre quadrature, n = 1..5; the stored Yukawa strengths '
                       'recomputed (details)',
         'value': v15, 'source': 'computed afresh',
         'details': {'ode': ode, 'boundary': bc, 'flat_profile_orthogonality': orth, 'norms': ndev, 'yukawa_strengths_and_Lambda_n': adev,
                     'stored_flat_source_overlap_max': max(abs(lv['flat_source_overlap']) for lv in ser['kaluza_klein_gravitons'][1:])}},
        {'definition': 'the Kaluza-Klein correction to Newton\'s law at the smallest measured distance (50 micrometres), alpha_1 e^{-m_1 r} '
                       'with m_1 r = %.2e (series.json newton_law): zero in double precision; the Lovelock corrections to the graviton '
                       'operator are OPEN (not estimated)' % ser['newton_law']['m1_r'],
         'value': 0.0,
         'exponent_m1_r': ser['newton_law']['m1_r'], 'source': 'series.json'},
        v15, 1e-11, 'analytic functions in double precision (terms up to (q_5^2 + a^2) e^{a} = 2.4e4 cancel to 1e-16 of themselves) and the '
                    '12-digit storage of N_n; the stored Yukawa strengths (200001-point trapezoid, error about 5e-9) are checked separately '
                    '(tolerance 1e-8)',
        extra_ok=adev < 1e-8, extra='Yukawa strengths %.1e' % adev)

    # ---- R16 the metric series ----
    o2 = ser['order2']
    dcos = r0['Delta_Phi_Weyl']
    o2_re = rel(o2['cosmological (Delta_Phi^2 at k = 1e-4 Mpc^-1)'], dcos ** 2)
    GN_SI, c_SI, Msun = 6.67430e-11, 299792458.0, 1.98892e30
    bodies = {'Earth (surface)': (5.9722e24, 6.371e6), 'Sun (surface)': (Msun, 6.957e8),
              'white dwarf (0.6 Msun, 8700 km)': (0.6 * Msun, 8.7e6), 'neutron star (1.4 Msun, 12 km)': (1.4 * Msun, 1.2e4)}
    pot_dev = maxrel((GN_SI * M_ / (R_ * c_SI ** 2), ser['order1_n0']['potentials_of_bound_objects'][k]) for k, (M_, R_) in bodies.items())
    rad = max(abs(v['delta_ln_f']) for v in ser['radion']['static_response'].values())
    seq = [1.0, dcos, dcos ** 2, rad, 0.0]
    mono = all(seq[i] > seq[i + 1] for i in range(len(seq) - 1))
    v16 = dcos ** 2 / dcos
    B.equation(
        'metric_series_order2',
        'the metric power series g = gbar + eps h1 + eps^2 h2 + ... (truncation after the first order)',
        'FIELD_EQUATIONS section 8 and 8.1; SOLUTION "The approximation scheme" and step 10 (the terms of the metric power series)',
        {'description': 'order 0: 1; order 1 (n = 0): Delta_Phi(k) <= %.2e (cosmological), G M/(R c^2) (bound objects); order 1 (n >= 1): '
                        'Kaluza-Klein gravitons; radion delta ln f <= %.1e; order 2: (order 1)^2 (ESTIMATE) (series.json)' % (dcos, rad),
         'method': 'magnitudes from the computed solution', 'order': 'first order kept'},
        {'definition': 'the first omitted order relative to the kept one on cosmological scales, Delta_Phi^2/Delta_Phi = Delta_Phi at k = 1e-4 '
                       'Mpc^-1 (recomputed from cosmology.json); the stored order-2 magnitude and the bound-object potentials recomputed '
                       '(details); the terms decrease strictly: 1, %.1e, %.1e, %.1e, 0' % (dcos, dcos ** 2, rad),
         'value': v16, 'source': 'computed afresh from cosmology.json and series.json',
         'details': {'order2_stored_vs_recomputed': o2_re, 'bound_object_potentials': pot_dev, 'strictly_decreasing': mono}},
        {'definition': 'order 2 at a neutron star, Phi^2 (series.json order2): the series converges slowly there, where full nonlinear '
                       'general relativity applies (outside the cosmological solution)',
         'value': o2['neutron star'], 'source': 'series.json'},
        v16, 1e-3, 'the first-order cosmology (CMB, BAO) is used at the level of the CAMB default accuracy (about 1e-3); the omitted '
                   'second order is 2.4e-5 of the first',
        extra_ok=mono and o2_re < 1e-9 and pot_dev < 1e-9, extra='order 2/order 1 %.1e' % v16)


# ======================================================================================================================
# R17-R21 neutrinos
def neutrinos(D, B, S):
    nu = D['neutrino']
    masses = D['masses']
    fL = masses['scales']['fL_GeV_inv']
    m_x0 = np.array([masses['fermions'][n]['e_exact'] / fL * 1e9 for n in ('nu1', 'nu2', 'nu3')])   # eV
    m2 = m_x0 ** 2
    fl = D['flavour']['PMNS']
    U = np.array(fl['re']) + 1j * np.array(fl['im'])
    S['m_x0'] = m_x0
    S['U'] = U
    HBARC_EV_M = val('hbar_c_GeV_m') * 1e9
    HBARC_EV_CM = HBARC_EV_M * 100.0
    GF_EV = val('G_F_GeV-2') * 1e-18
    NA = val('N_A')
    SQ2GF_CM3 = math.sqrt(2) * GF_EV * HBARC_EV_CM ** 3
    KM = 1e3 / HBARC_EV_M

    def ham(UU, E, V):
        return UU @ np.diag(m2) @ UU.conj().T / (2 * E) + np.diag([V, 0.0, 0.0])

    def evolve(Hm, Li):
        wv, Q = np.linalg.eigh(Hm)
        return Q @ np.diag(np.exp(-1j * wv * Li)) @ Q.conj().T
    unit = vac = cpt = 0.0
    for (Lkm, EMeV, rho) in [(1.65, 4.0, 0.0), (52.5, 4.0, 0.0), (295.0, 600.0, 2.6), (810.0, 2000.0, 2.84), (1300.0, 2500.0, 2.848),
                             (12742.0, 10000.0, 0.0)]:
        E, Li, V = EMeV * 1e6, Lkm * KM, SQ2GF_CM3 * rho * 0.5 * NA
        Sm = evolve(ham(U, E, V), Li)
        unit = max(unit, float(np.max(np.abs(Sm @ Sm.conj().T - np.eye(3)))))
        Sv = evolve(ham(U, E, 0.0), Li)
        Sb = evolve(ham(U.conj(), E, 0.0), Li)
        for a in range(3):
            for b in range(3):
                amp = sum(U[b, i] * np.conj(U[a, i]) * cmath.exp(-1j * m2[i] * Li / (2 * E)) for i in range(3))
                vac = max(vac, abs(abs(Sv[b, a]) ** 2 - abs(amp) ** 2))
                cpt = max(cpt, abs(abs(Sv[b, a]) ** 2 - abs(Sb[a, b]) ** 2))
    lbl = 0.0
    for name, v in nu['long_baseline'].items():
        E, Li, V = v['E_MeV'] * 1e6, v['L_km'] * KM, SQ2GF_CM3 * v['rho'] * 0.5 * NA
        Pn = np.abs(evolve(ham(U, E, V), Li)) ** 2
        Pa = np.abs(evolve(ham(U.conj(), E, -V), Li)) ** 2
        Pv = np.abs(evolve(ham(U, E, 0.0), Li)) ** 2
        lbl = max(lbl, abs(Pn[0, 1] - v['P_mue_nu']), abs(Pa[0, 1] - v['P_mue_antinu']), abs(Pv[0, 1] - v['P_mue_nu_vacuum']),
                  abs(Pn[1, 1] - v['P_mumu_nu']))
    n_ = {k: v_[0] for k, v_ in NUFIT60_NO.items()}
    c13sq = 1 - n_['sin2_theta13']
    sol_dev = 0.0
    for s_ in nu['solar']:
        ne = NA * min(245.0 * math.exp(-10.54 * s_['x_production']), 100.0)
        A_ = 2 * s_['E_MeV'] * 1e6 * SQ2GF_CM3 * ne * c13sq / n_['dm2_21_eV2']
        c2 = 1 - 2 * n_['sin2_theta12']
        s2t = math.sqrt(1 - c2 * c2)
        c2m = (c2 - A_) / math.sqrt((c2 - A_) ** 2 + s2t * s2t)
        sol_dev = max(sol_dev, abs(c13sq ** 2 * (0.5 + 0.5 * c2 * c2m) + n_['sin2_theta13'] ** 2 - s_['P_ee_adiabatic']))
    nonad = max(abs(s_['P_ee_numeric_40000'] - s_['P_ee_adiabatic']) for s_ in nu['solar'])
    layer = max(abs(s_['P_ee_numeric_40000'] - s_['P_ee_numeric_20000']) for s_ in nu['solar'])
    plz = max(r_['P_LZ'] for e_ in nu['supernova_MSW']['resonances'].values() for r_ in e_.values())
    v17 = max(unit, vac, cpt, lbl, sol_dev)
    B.equation(
        'neutrino_flavour_evolution',
        'flavour evolution of the three neutrinos in vacuum and matter (i dpsi/dx4 = H psi), MSW resonances, the Sun, supernova envelopes',
        'FIELD_EQUATIONS section 9.1 (the matter potentials) and 9.2 (vacuum and matter: evolution operator, MSW conditions, adiabatic P_ee, '
        'Landau-Zener); SOLUTION step 5 (masses, mixing and the equations; vacuum, matter and accelerators; the Sun; supernovae)',
        {'description': 'S = exp(-i H L) for constant density, ordered products of 20000/40000 layer operators in the Sun; H = U diag(m_i^2) '
                        'U^dagger/(2E) + diag(V_CC, 0, 0); masses from the x0 eigenvalues, U the neutrino tip matrix (neutrino.json)',
         'method': 'exact matrix exponentials (eigendecomposition)', 'order': 'coherent (collisionless) evolution, exact for the given '
                                                                              'potential'},
        {'definition': 'with the x0 masses (masses.json e_exact/fL) and the stored PMNS matrix (flavour.json): unitarity max |S S^dagger - 1| '
                       '(6 baselines, vacuum and matter), the exact vacuum evolution against the analytic sum formula and CPT (max abs), '
                       'the stored T2K, NOvA, DUNE probabilities recomputed (max abs), the stored adiabatic solar P_ee recomputed (max abs)',
         'value': v17, 'source': 'computed afresh',
         'details': {'unitarity': unit, 'vacuum_formula': vac, 'CPT': cpt, 'long_baseline_recomputed': lbl, 'solar_adiabatic_recomputed': sol_dev}},
        {'definition': 'what the adiabatic formula drops (non-adiabatic and production-region effects): max |numerical - adiabatic| solar P_ee '
                       '(neutrino.json solar); the layer discretisation %.1e; supernova Landau-Zener jumps <= %.1e; the flavour-universal '
                       'neutral-current potential drops out exactly; collective effects beyond the linear analysis OPEN' % (layer, plz),
         'value': nonad, 'source': 'neutrino.json'},
        v17, 1e-9, 'exact unitary operators in double precision (1e-15); the recomputation uses masses that differ from the stored ones by '
                   'the fit residual (1e-12) and the 12-digit PMNS matrix',
        extra='unitarity %.1e, accelerators %.1e' % (unit, lbl))

    # ---- R18 the thermal potential ----
    mW = val('m_W_GeV') * 1e9
    coef = 8 * math.sqrt(2) * GF_EV / (3 * mW ** 2) * 7 * math.pi ** 2 / 60
    ons = nu['oscillation_onset_T_MeV']
    cond = {}
    eta_b, Qnp = 6.1e-10, 1.29333e6
    zeta3 = 1.2020569031595942
    for key, dm2, c2 in (('atmospheric_13', n_['dm2_31_eV2'], 1 - 2 * n_['sin2_theta13']),
                         ('solar_12', n_['dm2_21_eV2'], 1 - 2 * n_['sin2_theta12'])):
        T = ons[key] * 1e6
        vth = coef * 3.15 * T ** 5
        vac_ = dm2 * c2 / (2 * 3.15 * T)
        cond[key] = abs(vth / vac_ - 1)
    # the thermal potential at momentum p = 3.15 T is coef p T^4; the CP-asymmetric one, sqrt2 G_F n_e,net, is momentum independent
    asym = {k: math.sqrt(2) * GF_EV * eta_b * (2 * zeta3 / math.pi ** 2 * (ons[k] * 1e6) ** 3) / (1 + math.exp(-Qnp / (ons[k] * 1e6)))
               / (coef * 3.15 * (ons[k] * 1e6) ** 5) for k in ons}
    v18 = max(cond.values())
    B.equation(
        'neutrino_thermal_potential',
        'thermal potential of the e+- plasma that suppresses mixing in the early Universe',
        'FIELD_EQUATIONS section 9.3 (the thermal potential); SOLUTION step 5 (the early Universe and N_eff)',
        {'description': 'V_e - V_mu = -(8 sqrt2 G_F p/(3 m_W^2)) (7 pi^2/60) T^4 equals dm2 cos 2theta/(2p) at p = 3.15 T: T = %.2f MeV '
                        '(atmospheric), %.2f MeV (solar) (neutrino.json oscillation_onset_T_MeV)' % (ons['atmospheric_13'], ons['solar_12']),
         'method': 'Brent root', 'order': 'leading order in T/m_W, CP-symmetric plasma'},
        {'definition': 'the onset condition at the stored temperatures, |V_thermal / (dm2 cos 2theta/(2p)) - 1|',
         'value': v18, 'source': 'computed afresh', 'details': cond},
        {'definition': 'the CP-asymmetric potential sqrt2 G_F (n_e- - n_e+), with n_e- - n_e+ = n_p = eta_b n_gamma/(1 + e^{-Q/T}) (charge '
                       'neutrality, eta_b = 6.1e-10 as in coupled.json; neutrino asymmetries assumed zero), relative to the thermal term at '
                       'the onset temperatures (ESTIMATE; it would shift the onset temperatures by about a sixth of this); higher orders in '
                       '(T/m_W)^2 ~ 4e-9',
         'value': max(asym.values()), 'ratios': asym, 'source': 'computed (ESTIMATE)'},
        v18, 1e-9, 'the stored temperatures carry 12 digits and the condition scales as T^6',
        extra='CP-asymmetric term %.1e of the thermal one (ESTIMATE)' % max(asym.values()))

    # ---- R19 neutrino decoupling: the instantaneous limit recomputed ----
    me = val('m_e_MeV')

    def nF(E):
        ex = math.exp(-E)
        return ex / (1.0 + ex)

    def s_eg(T):
        x = me / T
        um = 60.0 + 10.0 * x
        rho = 4 / (2 * math.pi ** 2) * T ** 4 * quad(lambda u: u * u * math.sqrt(u * u + x * x) * nF(math.sqrt(u * u + x * x)),
                                                      0, um, epsabs=0, epsrel=1e-13, limit=200)[0]
        pr_ = 4 / (6 * math.pi ** 2) * T ** 4 * quad(lambda u: u ** 4 / math.sqrt(u * u + x * x) * nF(math.sqrt(u * u + x * x)),
                                                      0, um, epsabs=0, epsrel=1e-13, limit=200)[0]
        rg = math.pi ** 2 / 15 * T ** 4
        return (rg + rg / 3 + rho + pr_) / T
    Td, Te = 20.0, 0.005
    Tnu = Td / (s_eg(Td) / s_eg(Te)) ** (1.0 / 3.0)
    neff_inst = 3 * (11.0 / 4.0) ** (4.0 / 3.0) * (Tnu / Te) ** 4
    runs = nu['N_eff_runs']
    pub = [(runs['instantaneous_noQED'], 3.000), (runs['instantaneous_LO'], 3.011), (runs['instantaneous_NLO'], 3.010),
           (runs['FD_common_noQED']['N_eff'], 3.039), (runs['FD_common_NLO']['N_eff'], 3.049), (runs['FD_separate_NLO']['N_eff'], 3.048)]
    pubdev = max(abs(a - b) for a, b in pub)
    dev_inst = abs(neff_inst - runs['instantaneous_noQED'])
    comp = nu['N_eff_UM2_computed']['separate_temperatures']
    v19 = dev_inst
    B.equation(
        'neutrino_decoupling',
        'neutrino decoupling: temperature equations with Fermi-Dirac energy transfer, the QED pressure of the plasma, N_eff',
        'FIELD_EQUATIONS section 9.4 (the quantum kinetic equations and neutrino decoupling); SOLUTION step 5 (the early Universe and N_eff)',
        {'description': 'dT_gamma/dx4, dT_nu_alpha/dx4 with the Escudero kernels and P_int = P2 + P3, from 20 MeV to 5 keV: N_eff = %.4f '
                        '(separate nu_e, nu_mu,tau temperatures), %.4f (common); the precision value %.4f (Cielo et al. 2023) is adopted '
                        '(neutrino.json)' % (comp, nu['N_eff_UM2_computed']['common_temperature'], nu['N_eff_adopted']['value']),
         'method': 'LSODA, rtol 1e-11; e+- thermodynamics tabulated on 400 points (spline in ln T)',
         'order': 'momentum-averaged (one temperature per flavour); QED to O(e^3)'},
        {'definition': '|N_eff(instantaneous decoupling at 20 MeV, no QED) recomputed independently from the separate entropy conservation '
                       'of the e+- gamma plasma with exact Fermi-Dirac integrals (scipy quad) - stored value| (neutrino.json N_eff_runs.'
                       'instantaneous_noQED); the method against the six published values of Escudero 2020 (Table 1, 3 decimals): %.1e' % pubdev,
         'value': v19, 'source': 'computed afresh; published comparison from neutrino.json',
         'details': {'recomputed': neff_inst, 'stored': runs['instantaneous_noQED'], 'published_values_max_abs_difference': pubdev}},
        {'definition': 'the electron mass in the rates and the momentum dependence (absent in the method of temperatures): computed - adopted '
                       'N_eff; the treatment of oscillations (separate - common) %.4f; neutrino masses (m_3/T_dec)^2 = %.0e' % (
                           abs(comp - nu['N_eff_UM2_computed']['common_temperature']), (m_x0[2] / 2e6) ** 2),
         'value': comp - nu['N_eff_adopted']['value'], 'source': 'neutrino.json'},
        v19, 1e-6, 'both evaluate the same exact entropy balance; the stored one through a 400-point spline table of the e+- thermodynamics, '
                   'whose interpolation error must stay far below the 1e-4 to which N_eff is used',
        extra_ok=pubdev < 1.5e-3, extra='recomputed %.10f, stored %.10f; published values within %.1e' % (
            neff_inst, runs['instantaneous_noQED'], pubdev))

    # ---- R20 the fast flavour instability ----
    ffi = nu['fast_flavour_instability']

    def gshape(sig):
        nrm = quad(lambda u: math.exp(-(1 - u) ** 2 / (2 * sig * sig)), -1, 1, epsabs=0, epsrel=1e-13)[0] / 2
        return lambda u: math.exp(-(1 - u) ** 2 / (2 * sig * sig)) / nrm
    ge6, gb4 = gshape(0.6), gshape(0.4)
    cases = {'crossing: nu_e broad (sigma 0.6), nubar_e forward (sigma 0.4), alpha 0.8': lambda u: ge6(u) - 0.8 * gb4(u),
             'crossing: linear g_e = 1 + 0.2u, g_ebar = 1 + 0.6u, alpha 0.9': lambda u: (1 + 0.2 * u) - 0.9 * (1 + 0.6 * u),
             'no crossing: nu_e sigma 0.6, nubar_e sigma 0.4, alpha 0.3': lambda u: ge6(u) - 0.3 * gb4(u)}
    fdev = {'moments': 0.0, 'analytic_growth': 0.0, 'homogeneous_matrix': 0.0}
    ug, wgq = np.polynomial.legendre.leggauss(300)
    for name in sorted(cases):
        G = cases[name]
        st = ffi[name]
        mom = [quad(lambda u: G(u) * u ** n / 2, -1, 1, epsabs=1e-15, epsrel=1e-13)[0] for n in range(3)]
        fdev['moments'] = max(fdev['moments'], max(abs(a - b) for a, b in zip(mom, st['moments_I0_I1_I2'])))
        Dd = (mom[0] + mom[2]) ** 2 - 4 * mom[1] ** 2
        gr = math.sqrt(-Dd) / 2 if Dd < 0 else 0.0
        fdev['analytic_growth'] = max(fdev['analytic_growth'], abs(gr - st['growth_K_eq_Lambda_analytic']))
        gv = np.array([G(u) for u in ug])
        lam0, lam3 = float(np.sum(wgq * gv) / 2), float(np.sum(wgq * gv * ug) / 2)
        Am = np.diag(lam0 - ug * lam3) - (1 - np.outer(ug, ug)) * (wgq * gv / 2)[None, :]
        fdev['homogeneous_matrix'] = max(fdev['homogeneous_matrix'], abs(float(np.max(np.linalg.eigvals(Am).imag)) - st['growth_homogeneous_matrix']))
    agree = max(max(abs(c_['growth_K_eq_Lambda_analytic'] - c_['growth_K_eq_Lambda_dispersion']),
                    abs(c_['growth_homogeneous_matrix'] - c_['growth_homogeneous_dispersion'])) for c_ in ffi.values())
    mu32 = nu['fast_flavour_scales']['1e+32']['mu_eV']
    vac_over_mu = n_['dm2_31_eV2'] / (2 * 11e6) / mu32
    v20 = max(fdev.values())
    B.equation(
        'fast_flavour_dispersion',
        'linearised flavour evolution of a dense neutrino gas: the dispersion relation of the fast flavour instability',
        'FIELD_EQUATIONS section 9.5 (the dense neutrino gas: dispersion relation, homogeneous mode, ELN crossing); SOLUTION step 5 '
        '(supernovae: the fast flavour instability)',
        {'description': 'roots with Im omega > 0 of det Pi = 0 (axisymmetric and azimuthal branches) for real k; the homogeneous mode from the '
                        'discretised equations; the analytic growth (1/2) sqrt(4 I1^2 - (I0 + I2)^2) of the mode K = Lambda^3 '
                        '(neutrino.json fast_flavour_instability)',
         'method': 'vectorised Newton iterations; eigenvalues of the 300-node discretisation', 'order': 'linear in the flavour coherence'},
        {'definition': 'the ELN moments recomputed with adaptive quadrature, the analytic growth from them and the eigenvalues of the '
                       'discretised homogeneous equations (300 nodes) recomputed: max abs deviation from the stored values (units mu); the '
                       'stored agreement of the three evaluations: %.1e' % agree,
         'value': v20, 'source': 'computed afresh', 'details': dict(fdev, stored_three_evaluations=agree)},
        {'definition': 'the vacuum term relative to the self-interaction near the neutrinosphere, dm2_31/(2 <E> mu) with <E> = 11 MeV and '
                       'n_nu_e = 1e32 cm^-3; the nonlinear evolution beyond the linear analysis is OPEN',
         'value': vac_over_mu, 'source': 'computed from neutrino.json fast_flavour_scales'},
        v20, 1e-10, 'the same moments and matrices evaluated twice; the stored growth rates agree among three methods to 1e-14',
        extra='moments %.1e, growth %.1e, matrix %.1e' % (fdev['moments'], fdev['analytic_growth'], fdev['homogeneous_matrix']),
        in_concert_note='none: its fields (a nu_e and nubar_e gas near a neutrinosphere with assumed angular distributions) enter no other '
                        'field equation of UM-2; the only shared quantities are G_F (an input) and, through the neglected vacuum term '
                        '(%.0e of mu), the x0 masses' % vac_over_mu)

    # ---- R21 the cosmic neutrino background ----
    kB = val('k_B_eV_per_K')
    T0 = val('T_CMB_K')
    Tnu_ = kB * (4.0 / 11.0) ** (1.0 / 3.0) * T0
    n_state = 3 * zeta3 / (2 * math.pi ** 2) * Tnu_ ** 3 / HBARC_EV_CM ** 3
    cnb = nu['CNB']
    cdev = {'n': rel(n_state, cnb['n_per_mass_state_cm3']), 'rho': 0.0, 'v': 0.0, 'flavour_content': 0.0}
    rho_tot = 0.0
    for i in range(3):
        m = m_x0[i]
        # in the dimensionless variable u = p/T_nu (integrals of order 1), unlike um2_neutrino.py, which integrates in eV
        mu_ = m / Tnu_
        rho_i = Tnu_ ** 4 * quad(lambda u: u * u * math.sqrt(u * u + mu_ * mu_) / (math.exp(u) + 1), 0, 60, epsabs=0,
                                 epsrel=1e-13, limit=200)[0] / math.pi ** 2
        vm = quad(lambda u: u ** 3 / math.sqrt(u * u + mu_ * mu_) / (math.exp(u) + 1), 0, 60, epsabs=0, epsrel=1e-13, limit=200)[0] / \
            quad(lambda u: u * u / (math.exp(u) + 1), 0, 60, epsabs=0, epsrel=1e-13, limit=200)[0]
        rho_tot += rho_i
        st = cnb['states'][i]
        cdev['rho'] = max(cdev['rho'], rel(rho_i, st['rho_eV4']))
        cdev['v'] = max(cdev['v'], rel(vm, st['mean_velocity_over_c']))
        for j, fla in enumerate(('e', 'mu', 'tau')):
            cdev['flavour_content'] = max(cdev['flavour_content'], abs(abs(U[j, i]) ** 2 - st['flavour_content'][fla]))
    rho_c = 1.87834e-29 * 5.60959e32 * HBARC_EV_CM ** 3
    cdev['Omega_nu_h2'] = rel(rho_tot / rho_c, cnb['Omega_nu_h2'])
    S['Omega_nu_h2_cnb'] = rho_tot / rho_c
    v21 = max(cdev.values())
    B.equation(
        'cosmic_neutrino_background',
        'cosmic neutrino background: an incoherent mixture of the three mass states with the Fermi-Dirac distribution',
        'FIELD_EQUATIONS section 9.6 (the cosmic neutrino background); SOLUTION step 5 (the cosmic neutrino background)',
        {'description': 'T_nu = (4/11)^{1/3} T_CMB, n_i = 3 zeta(3) T_nu^3/(2 pi^2), rho_i = 2 int d^3p/(2pi)^3 sqrt(p^2 + m_i^2) f, mean '
                        'velocities, flavour content |U_alpha i|^2, Omega_nu h^2 (neutrino.json CNB)',
         'method': 'adaptive quadrature', 'order': 'exact for free streaming after instantaneous decoupling'},
        {'definition': 'n_i, rho_i, <v>_i, |U_alpha i|^2 and Omega_nu h^2 recomputed with the x0 masses and the stored PMNS matrix: max '
                       'relative (absolute for the flavour content) deviation from the stored values',
         'value': v21, 'source': 'computed afresh', 'details': cdev},
        {'definition': 'the non-instantaneous heating, (N_eff/3)^{3/4} - 1 in Omega_nu h^2 (included in the CMB computation through the '
                       'degeneracy N_eff/3, not in the CNB table); gravitational clustering not computed',
         'value': (NEFF_SM[0] / 3) ** 0.75 - 1, 'source': 'computed'},
        v21, 1e-10, 'two adaptive quadratures of the same integrals with relative tolerances 1e-13 (in eV in um2_neutrino.py, in '
                    'u = p/T_nu here), stored to 12 digits',
        extra='largest %s %.1e' % (max(cdev, key=cdev.get), v21))


# ======================================================================================================================
# R22-R26 thermal history
def thermal(D, B, S):
    from um2_thermal import (Cosmo, gas, omega_h2, relic, sigma_I12, sigmav_thermal, species, thermo, w_qgp, T_NU_DEC)  # noqa: F401
    masses = D['masses']
    th = D['thermal']
    cp = D['coupled']
    HG = masses['scales']['H_GeV']
    MDM = D['ks_spectrum']['eps_dm'] * HG
    sp_ = species(masses, MDM)
    MPl = val('M_Pl_GeV')

    # ---- R22 degrees of freedom by independent quadrature ----
    def gas_quad(m, T, g, fermion):
        x = m / T
        if x > 200.0:
            return 0.0, 0.0
        sgn = 1.0 if fermion else -1.0
        um = math.sqrt((x + 60.0) ** 2 - x * x)
        r = quad(lambda u: u * u * math.sqrt(u * u + x * x) / (math.exp(math.sqrt(u * u + x * x)) + sgn), 0, um, epsabs=0, epsrel=1e-12,
                 limit=200)[0]
        p = quad(lambda u: u ** 4 / max(math.sqrt(u * u + x * x), 1e-300) / (math.exp(math.sqrt(u * u + x * x)) + sgn), 0, um, epsabs=0,
                 epsrel=1e-12, limit=200)[0]
        return g / (2 * math.pi ** 2) * r * T ** 4, g / (6 * math.pi ** 2) * p * T ** 4

    def thermo_quad(T):
        rho = s = 0.0
        for (n, m, g, fe, grp) in sp_:
            if grp in ('nu', 'dm'):
                continue
            r, p = gas_quad(m, T, g, fe)
            wgt = w_qgp(T) if grp == 'qgp' else ((1.0 - w_qgp(T)) if grp == 'hrg' else 1.0)
            rho += wgt * r
            s += wgt * (r + p) / T
        if T >= T_NU_DEC:
            Tnu = T
        else:
            tot = sum(sum(gas_quad(m, T, g, fe)) / T for (n, m, g, fe, grp) in sp_ if grp == 'eg')
            Tnu = T * (tot / (2 * math.pi ** 2 / 45 * T ** 3) / 5.5) ** (1.0 / 3.0)
        for (n, m, g, fe, grp) in sp_:
            if grp == 'nu':
                r, p = gas_quad(m, Tnu, g, fe)
                rho += r
                s += (r + p) / Tnu
        return rho / (math.pi ** 2 / 30 * T ** 4), s / (2 * math.pi ** 2 / 45 * T ** 3)
    gdev = 0.0
    for key, rowv in sorted(th['g_star_table'].items()):
        T = float(key.split()[0])
        gr, gs_ = thermo_quad(T)
        gdev = max(gdev, rel(gr, rowv['g_rho']), rel(gs_, rowv['g_s']))
    lim = {'g_s_today_vs_43_over_11': rel(th['today']['g_s'], 43.0 / 11.0),
           'g_rho_today_vs_exact': rel(th['today']['g_rho'], 2 + 7.0 / 8 * 6 * (4.0 / 11) ** (4.0 / 3))}
    # the O(alpha) interaction pressure at the freeze-out (FIELD_EQUATIONS 7.1, the formulas of um2_coupled.py)
    T_fo = MDM / cp['I13']['x_f_capped']
    a_s, mZ0, a_em, s2ms = val('alpha_s_mZ'), val('m_Z_GeV'), 1 / 127.95, val('sin2_theta_W_MSbar')
    Lm = math.log(2 * math.pi * T_fo / mZ0) / (2 * math.pi)
    als = 1 / (1 / a_s + 7.0 * Lm)
    a2 = 1 / (s2ms / a_em + 10.0 / 3.0 * Lm)
    aY = 1 / ((1 - s2ms) / a_em - 20.0 / 3.0 * Lm)
    supp = gas(val('m_W_GeV'), T_fo, 3, False)[0] / gas(0.0, T_fo, 3, False)[0]
    p2 = {'QCD': -(4 * math.pi * als / 144.0) * 8 * (3 + 2.5 * 0.5 * 6) * T_fo ** 4,
          'SU2': -(4 * math.pi * a2 / 144.0) * 3 * (2 + 2.5 * 3) * supp * T_fo ** 4,
          'U1Y': -(4 * math.pi * aY / 144.0) * 2.5 * 5 * supp * T_fo ** 4}
    p_ideal = 0.0
    for (n, m, g, fe, grp) in sp_:
        if grp in ('dm', 'hrg'):
            continue
        wgt = w_qgp(T_fo) if grp == 'qgp' else 1.0
        p_ideal += wgt * gas(m, T_fo, g, fe)[1]
    p2rel = {k: v / p_ideal for k, v in p2.items()}
    p2tot = sum(p2rel.values())
    S['p2_relative_fo'] = p2tot
    S['omega_shift_interaction'] = -0.5 * p2tot
    v22 = max(gdev, max(lim.values()))
    B.equation(
        'thermal_degrees_of_freedom',
        'thermal history: the ideal-gas energy and entropy densities of the thermalised species with their x0 masses',
        'FIELD_EQUATIONS section 10 (degrees of freedom: rho_i, p_i, s_i, g_rho, g_s, H, the QCD crossover, instantaneous neutrino '
        'decoupling); SOLUTION step 9 (the thermal history)',
        {'description': 'g_rho(T), g_s(T) from photon, gluons, W+, W-, Z, six quarks, three charged leptons, three neutrinos (no Higgs), a '
                        'hadron gas below the crossover, neutrinos decoupled at 2 MeV (thermal.json g_star_table, g_star_curve, today)',
         'method': 'Gauss-Legendre (160 nodes) on the ideal-gas integrals (um2_thermal.py)', 'order': 'ideal gases (no interactions)'},
        {'definition': 'g_rho, g_s at the 13 tabulated temperatures recomputed with the same species, switch and neutrino rule but adaptive '
                       'quadrature (scipy quad, 1e-12): max relative deviation; the exact limits today, g_s = 43/11 and g_rho = 2 + (7/8) 6 '
                       '(4/11)^{4/3}',
         'value': v22, 'source': 'computed afresh', 'details': dict(lim, g_table_independent_quadrature=gdev)},
        {'definition': 'the O(alpha) interaction pressure of the plasma, p_2 = -(g^2 T^4/144) d_A [C_A + (5/2) T_F N_f] (FIELD_EQUATIONS 7.1; '
                       'couplings at 2 pi T), relative to the ideal-gas pressure at the freeze-out (T = %.1f GeV): NOT small, %.1f %% (QCD '
                       '%.1f %%, SU(2) %.1f %%, U(1) %.2f %%); the ideal-gas thermal history (and so H and s of the Boltzmann equation) '
                       'leaves it out, while step 8 uses p_2 for the condensates; since Omega h^2 ~ g_rho^{1/2}/g_s at freeze-out, it would '
                       'raise Omega h^2 by about %.1f %% and G_A by about half of that (ESTIMATE)' % (
                           T_fo, 100 * p2tot, 100 * p2rel['QCD'], 100 * p2rel['SU2'], 100 * p2rel['U1Y'], 100 * S['omega_shift_interaction']),
         'value': p2tot, 'parts': p2rel, 'source': 'computed (ESTIMATE, leading order)'},
        v22, 1e-6, 'the stored integrals use 160 Gauss nodes on a finite range, the afresh ones adaptive quadrature to 1e-12; the exact '
                   'limits hold to the decoupling rule (e+- fully annihilated today)',
        extra='O(alpha) pressure at the freeze-out %.1f %% (neglected)' % (100 * p2tot))

    # ---- R23 the relic ----
    cosmo = Cosmo(sp_)
    s0 = th['s0_cm3']
    G12 = th['I12_universal_benchmark']['G_combination_GeV-3']
    S13 = sum(c_['mult'] * (c_['q'] * c_['Itilde_b']) ** 2 for c_ in cp['I13']['components'])
    GA = cp['I13']['G_A_GeV-2']

    def sig13(s_):
        bi = math.sqrt(max(1 - 4 * MDM * MDM / s_, 1e-300))
        return S13 * GA ** 2 * s_ * (1 + 2 * MDM * MDM / s_) / (24 * math.pi * bi)
    bound13 = lambda s_: 3 * math.pi / (4 * (s_ / 4 - MDM * MDM))
    XT = np.logspace(math.log10(5.0), math.log10(2000.0), 200)
    sv12 = CubicSpline(np.log(XT), np.log([sigmav_thermal(xx, MDM, lambda s_: sigma_I12(s_, MDM, G12 ** 2)) for xx in XT]))
    scx = brentq(lambda s_: sig13(s_) - bound13(s_), 4 * MDM * MDM * (1 + 1e-9), 1e4 * MDM * MDM)
    tab = CubicSpline(np.log(XT), np.log([sigmav_thermal(xx, MDM, lambda s_: min(sig13(s_), bound13(s_)), (scx / (4 * MDM * MDM) - 1.0,))
                                          for xx in XT]))
    clip = lambda x: math.log(min(max(x, 5.0), 2000.0))
    sv = lambda x: math.exp(float(sv12(clip(x)))) + math.exp(float(tab(clip(x))))
    Y, hist, xf = relic(MDM, sv, cosmo, MPl=MPl)
    om = omega_h2(MDM, Y, s0)
    dev_relic = abs(om / 0.060 - 1)
    dev_xf = rel(xf, cp['I13']['x_f_capped'])
    S['omega_recomputed'] = om

    def late_identity(hst, svf):
        xs = np.array(hst['x'])
        Ys = np.array(hst['Y'])
        xff = next(xx for xx, yy, ye in zip(xs, Ys, hst['Yeq']) if yy > 2.5 * ye)
        ist = int(np.searchsorted(xs, 3 * xff))

        def lam(x):
            T = MDM / x
            gr, gs_, dl = cosmo.g(T)
            s = 2 * math.pi ** 2 / 45 * gs_ * T ** 3
            Hh = math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / MPl
            return (1 + dl / 3) * s * svf(x) / (2 * x * Hh)
        # composite Gauss-Legendre between the kinks of the linearly interpolated g(T) (the temperature nodes of the thermal history)
        xa, xb = float(xs[ist]), 2000.0
        brk = [xa] + sorted(float(v) for v in MDM / np.exp(cosmo.lnT) if xa < v < xb) + [xb]
        xq, wq = np.polynomial.legendre.leggauss(12)
        integ = 0.0
        for lo, hi in zip(brk[:-1], brk[1:]):
            integ += sum(0.5 * (hi - lo) * wi * lam(0.5 * (hi - lo) * xi_ + 0.5 * (hi + lo)) for xi_, wi in zip(xq, wq))
        return abs((1.0 / Ys[-1] - 1.0 / Ys[ist]) / integ - 1)
    late13 = late_identity(hist, sv)
    # the stored I12 history of thermal.json (effective operator at the relic strength)
    XT2 = np.logspace(math.log10(5.0), math.log10(2000.0), 260)
    svu = CubicSpline(np.log(XT2), np.log([sigmav_thermal(xx, MDM, lambda s_: sigma_I12(s_, MDM, 1.0)) for xx in XT2]))
    G2eff = th['relic_effective_operator']['G_eff_GeV-3'] ** 2
    late12 = late_identity(th['history_effective'], lambda x: G2eff * math.exp(float(svu(clip(x)))))
    # neglected: the dark matter in g_rho at x = 5 and at x_f
    T5 = MDM / 5.0
    dm5 = gas(MDM, T5, 8, True)[0] / (math.pi ** 2 / 30 * cosmo.g(T5)[0] * T5 ** 4)
    ist_f = int(np.searchsorted(np.array(hist['x']), xf))
    Tf = MDM / xf
    dmf = MDM * hist['Y'][ist_f] * 2 * (2 * math.pi ** 2 / 45 * cosmo.g(Tf)[1] * Tf ** 3) / (math.pi ** 2 / 30 * cosmo.g(Tf)[0] * Tf ** 4)
    S['dm_share_x5'] = dm5
    S['dm_share_xf'] = dmf
    S['cosmo'] = cosmo
    S['T_fo'] = T_fo
    S['MDM'] = MDM
    sat = cp['I13']['fraction_of_rate_saturated_capped']
    v23 = max(dev_relic, late13, late12)
    B.equation(
        'boltzmann_relic',
        'Boltzmann equation of the two dark-matter species (thermal average of the I12 + I13 cross-sections, partial-wave unitarity)',
        'FIELD_EQUATIONS section 10 (the dark matter: Boltzmann equation, Gondolo-Gelmini average, sigma_I12, sigma_I13, the unitarity '
        'bounds); SOLUTION step 7 and step 9 (the Boltzmann equation; I12 alone and partial-wave unitarity; the relic with I13)',
        {'description': 'dY/dx = -(1 + delta) s <sigma v>/(2 x H) (Y^2 - Y_eq^2) per Dirac species with sigma_I12 (benchmark G = pi/(2 M^3)) + '
                        'sigma_I13 capped at 3 pi/(4 p^2); Omega h^2 = 0.060 per species for G_A = %.4e GeV^-2 (x_f = %.2f) (coupled.json I13); '
                        'I12 alone at the relic strength (thermal.json)' % (GA, cp['I13']['x_f_capped']),
         'method': 'Radau on ln Y (rtol 1e-10) from x = 5 to 2000, thermal average by adaptive quadrature tabulated on 200 points, Brent '
                   'root for G_A (xtol 1e-6 in ln G_A)', 'order': 'numerical solution of the kinetic equation (kinetic equilibrium, '
                                                               'Maxwell-Boltzmann for the dark matter)'},
        {'definition': 'largest of: the relic condition at the stored G_A, |Omega h^2 / 0.060 - 1| with the Boltzmann equation re-solved '
                       '(the same machinery, S13 from the stored overlaps); the late-time integral identity 1/Y(2000) - 1/Y(x*) = int '
                       '(1 + delta) s <sigma v>/(2 x H) dx (x* = 3 x_f) on the recomputed I13 history and on the STORED I12 history of '
                       'thermal.json history_effective (relative)',
         'value': v23, 'source': 'computed afresh',
         'details': {'late_time_quadrature': 'composite Gauss-Legendre (12 nodes) between the temperature nodes of g(T)',
                     'relic_condition_at_stored_G_A': dev_relic, 'Omega_h2_recomputed': om, 'Omega_h2_stored': cp['I13']['Omega_h2_per_species_capped'],
                     'x_f_recomputed_vs_stored': dev_xf, 'late_time_identity_I13_recomputed': late13,
                     'late_time_identity_I12_stored_history': late12,
                     'stored_s_wave_validation': th['validation_s_wave']['late_time_integral_check']}},
        {'definition': 'the leading neglected effects on the relic: the O(alpha) interaction pressure missing from g_rho, g_s (Omega h^2 shift '
                       'about %+.1f %%, ESTIMATE, see thermal_degrees_of_freedom); the fold bands missing from H at the freeze-out (see the '
                       'link hubble_rate_thermal_vs_four_dimensional_friedmann); the unitarity completion: %.1f %% of the freeze-out rate '
                       'comes from collisions at the J = 1 bound; the thermal shift of the mass, delta eps/M = %.1e; the dark matter in '
                       'g_rho: %.1e at x = 5 (where Y = Y_eq), %.0e at x_f' % (
                           100 * S['omega_shift_interaction'], 100 * sat,
                           abs(cp['environments']['dark-matter freeze-out (T = 1.42 TeV)']['d_eps_DM_over_M']), dm5, dmf),
         'value': S['omega_shift_interaction'], 'source': 'computed (ESTIMATE) and coupled.json'},
        v23, 1e-6, 'the root finding fixes ln G_A to 1e-6 (Omega h^2 to 2e-6); the Radau tolerance 1e-10 accumulated over the history and the '
                   'tabulated thermal average allow about 1e-8 in the late-time identity',
        extra_ok=dev_xf < 1e-6,
        extra='Omega h^2 = %.12f, late-time identity %.1e (I13), %.1e (stored I12 history)' % (om, late13, late12))

    # ---- R24 freeze-in ----
    fi = cp['freeze_in']
    Sfi = sum(c_['mult'] * (c_['q'] * c_['Itilde']) ** 2 for c_ in fi['components'])
    g_of = S['g_of']
    Nchi = 2
    gs0 = th['today']['g_s']

    def fi_integrand(lnT, GV):
        T = math.exp(lnT)
        gr, gs_ = g_of(T)
        Hh = math.sqrt(8 * math.pi ** 3 * gr / 90) * T * T / MPl
        Prate = 8 * T * (4 / math.pi ** 5) * Nchi * Sfi * GV ** 2 * T ** 8
        return Prate * (gs_ ** (-1 / 3.) / T) ** 4 / (Hh * T) * T

    def gl_int(fun, a, b, npan=60, nn=16):
        xq, wq = np.polynomial.legendre.leggauss(nn)
        tot = 0.0
        edges = np.linspace(a, b, npan + 1)
        for lo, hi in zip(edges[:-1], edges[1:]):
            tot += sum(0.5 * (hi - lo) * wi * fun(0.5 * (hi - lo) * xi_ + 0.5 * (hi + lo)) for xi_, wi in zip(xq, wq))
        return tot
    rho_nu1 = 7 / 8 * math.pi ** 2 / 15 * (4 / 11) ** (4.0 / 3.0)
    acc = gl_int(lambda lt: fi_integrand(lt, 1.0), math.log(1.0), math.log(fi['T_max_GeV']))
    dN1 = acc / (gs0 ** (-1 / 3.)) ** 4 / rho_nu1
    GVb = fi['G_V_benchmark_GeV-2']
    # Bessel moments int x^mu K_nu = 2^{mu-1} Gamma((1+mu+nu)/2) Gamma((1+mu-nu)/2)
    b6 = 2 ** 5 * math.gamma(4) * math.gamma(3)
    b7 = 2 ** 6 * math.gamma(5) * math.gamma(3)
    fdev = {'Delta_Neff_per_GV2': rel(dN1, fi['Delta_Neff_per_GV2']), 'sum_Nc_q2_I2': rel(Sfi, fi['sum_Nc_q2_I2']),
            'Bessel_x6K1': rel(fi['Bessel_x6K1'], b6), 'Bessel_x7K2': rel(fi['Bessel_x7K2'], b7),
            'Delta_Neff_benchmark_vs_0.001': rel(fi['Delta_Neff_per_GV2'] * GVb ** 2, 1e-3)}
    # the fold-band energy density at the freeze-out (for the Friedmann link)
    acc_fo = gl_int(lambda lt: fi_integrand(lt, GVb), math.log(T_fo), math.log(fi['T_max_GeV']))
    gr_fo, gs_fo = g_of(T_fo)
    rho_fold_fo = acc_fo / (gs_fo ** (-1 / 3.) / T_fo) ** 4
    S['fold_share_fo'] = rho_fold_fo / (math.pi ** 2 / 30 * gr_fo * T_fo ** 4)
    S['dN_freeze_in'] = fi['Delta_Neff_per_GV2'] * GVb ** 2
    v24 = fdev['Delta_Neff_per_GV2']
    B.equation(
        'freeze_in',
        'freeze-in of the fold bands through I11 (pair production f fbar -> Psi_fold Psibar_fold from the Standard-Model plasma)',
        'FIELD_EQUATIONS section 10 (the fold bands: freeze-in through I11); SOLUTION step 9 (the fold bands: freeze-in through I11)',
        {'description': 'gamma = (4/pi^5) N_chi G_V^2 T^8 sum N_c (q Itilde)^2, d(rho_fold a^4)/dx4 = 8 T gamma a^4 from T_max = 10 TeV; '
                        'Delta N_eff = %.4e G_V^2 GeV^4; G_V = %.4e GeV^-2 for Delta N_eff = 0.001 (coupled.json freeze_in)' % (
                            fi['Delta_Neff_per_GV2'], GVb),
         'method': 'trapezoid rule on 600 logarithmic temperatures with the stored g_rho(T), g_s(T)', 'order': 'Maxwell-Boltzmann, no back-reaction'},
        {'definition': '|Delta N_eff per G_V^2 re-integrated (Gauss-Legendre, 60 panels x 16 nodes in ln T, the same g_rho(T), g_s(T)) / '
                       'stored - 1|; further: sum N_c (q Itilde)^2 from the stored overlaps, the Bessel moments against 2^{mu-1} '
                       'Gamma((1+mu+nu)/2) Gamma((1+mu-nu)/2) = 384, 3072, Delta N_eff(G_V benchmark) against 0.001',
         'value': v24, 'source': 'computed afresh', 'details': fdev},
        {'definition': 'inverse processes: the production rate per fold quantum over the Hubble rate at T_max (coupled.json); Delta N_eff '
                       'grows like T_max^3 (T_max ASSUMED); quantum statistics not included',
         'value': fi['Gamma_over_H_at_Tmax'], 'source': 'coupled.json freeze_in.Gamma_over_H_at_Tmax'},
        v24, 1e-4, 'the stored value uses the trapezoid rule on 600 logarithmic points, whose error for an integrand growing like T^2 is '
                   '(d ln T)^2/6 = 4e-5 (as measured); 1e-4 is far below the sensitivity of the CMB to Delta N_eff (about 0.1)',
        extra_ok=max(fdev['sum_Nc_q2_I2'], fdev['Bessel_x6K1'], fdev['Bessel_x7K2'], fdev['Delta_Neff_benchmark_vs_0.001']) < 1e-8,
        extra='trapezoid vs Gauss %.1e' % v24)

    # ---- R25 the right-handed neutrinos (the B - L alternative) ----
    bl = cp['I13_B_minus_L_alternative']
    Ibd = cp['overlaps_Itilde_b']['dark matter (lowest odd level)']
    Idm = cp['overlaps_Itilde']['dark matter (lowest odd level)']
    Inu = [Ibd['nu1_R'], Ibd['nu2_R'], Ibd['nu3_R']]
    Ibar = math.sqrt(sum(I_ * I_ for I_ in Inu) / 3.0)
    GA_BL = bl['G_A_BL_GeV-2']
    zeta3 = 1.2020569

    def rates_nuR(x, gel_fac=1.0, ga=GA_BL):
        T = MDM / x
        gr_, gs_ = g_of(T)
        Hh = math.sqrt(8 * math.pi ** 3 * gr_ / 90) * T * T / MPl
        nchi = 2 * (MDM * T / (2 * math.pi)) ** 1.5 * math.exp(-x)
        n_nu = 0.75 * zeta3 / math.pi ** 2 * T ** 3
        G2 = (ga * Ibar) ** 2
        return 2 * nchi * nchi * G2 * MDM ** 2 / (2 * math.pi), n_nu, Hh, gel_fac * 2 * 2 * nchi * G2 * (3 * T) ** 2 / (2 * math.pi), gs_

    def solve_nuR(ga_fac=1.0):
        def rhs(s_, Yv):
            x = 2.0 + s_
            gam, n_nu, Hh, _, gs_ = rates_nuR(x, ga=GA_BL * ga_fac)
            T = MDM / x
            sden = 2 * math.pi ** 2 / 45 * gs_ * T ** 3
            return [gam / (sden * Hh * x) * (1 - (Yv[0] / (n_nu / sden)) ** 2)]
        # in s = x - 2, as in um2_coupled.py: the equilibration from zero abundance takes Y_eq/(dY/dx) = 7e-11 in x, and the steps that
        # resolve its start lie below the spacing of the floating-point numbers at x = 2
        sol = solve_ivp(rhs, (0.0, 38.0), [0.0], method='Radau', rtol=1e-13, atol=1e-30)
        _, n_nu40, _, _, gs40 = rates_nuR(40.0)
        return int(sol.status), float(sol.y[0][-1]) / (n_nu40 / (2 * math.pi ** 2 / 45 * gs40 * (MDM / 40.0) ** 3))
    status0, ratio40 = solve_nuR()
    # robustness: the integration of version 3 (in x, rtol 1e-8) stopped at its first step when G_A(B - L) changed by 2e-12
    robust = {'%+.0e' % d_: solve_nuR(1.0 + d_) for d_ in (-2e-12, -1e-12, 1e-12, 2e-12)}
    S['nuR_robust'] = (all(st_ == 0 for st_, _ in robust.values()) and status0 == 0,
                       max(abs(r_ - ratio40) for _, r_ in robust.values()))

    def x_kin(fac):
        for x in np.linspace(1.0, 60.0, 5901):
            _, _, Hh_, Gel, _ = rates_nuR(x, fac)
            if Gel / Hh_ < 1.0:
                return float(x)
        return None
    xk = {fac: x_kin(fac) for fac in (0.5, 1.0, 2.0)}
    dN = {fac: 3 * (10.75 / g_of(MDM / xk[fac])[1]) ** (4.0 / 3.0) * FH_HARDCODED for fac in xk}
    S13_BL = bl['S13_BL']
    rdev = {'Y_over_Yeq_x40': rel(ratio40, bl['Y_nuR_over_Yeq_at_x40']), 'x_kinetic_decoupling': rel(xk[1.0], bl['x_kinetic_decoupling']),
            'Delta_Neff': rel(dN[1.0], bl['Delta_Neff']),
            'G_A_BL': rel(cp['I13']['G_A_effective_operator_GeV-2'] * math.sqrt(S13 / S13_BL), GA_BL),
            'I11_over_I13': rel(GVb ** 2 * sum(Idm[n + '_R'] ** 2 for n in ('nu1', 'nu2', 'nu3')) /
                                (cp['I13']['G_A_effective_operator_GeV-2'] ** 2 * S13), bl['nuR_production_I11_over_I13_annihilation_JB'])}
    v25 = max(rdev.values())
    B.equation(
        'right_handed_neutrino_boltzmann',
        'Boltzmann equation of the right-handed neutrinos if I13 coupled to the B - L current (the alternative that version 3 rejects)',
        'FIELD_EQUATIONS section 10 (the right-handed neutrinos); SOLUTION step 9 (why the baryon current)',
        {'description': 'dn/dx4 + 3 H n = gamma_nu (1 - n^2/n_eq^2) from zero abundance at M/T = 2; elastic decoupling Gamma_el = H; Delta N_eff = '
                        '3 (10.75/g_s)^{4/3} F_h = %.3f (coupled.json I13_B_minus_L_alternative)' % bl['Delta_Neff'],
         'method': 'Radau in s = M/T - 2 (rtol 1e-13); decoupling on a grid of step 0.01 in M/T',
         'order': 'number-density equation, s-wave rates (ESTIMATE for the elastic rate)'},
        {'definition': 'the nu_R equation re-solved with the stored couplings and g(T): |Y/Y_eq(x = 40) recomputed / stored - 1|; the kinetic '
                       'decoupling, Delta N_eff, G_A(B - L) = G_A sqrt(S13/S13_BL) and the I11/I13 production ratio recomputed (relative)',
         'value': v25, 'source': 'computed afresh (Radau in s = x - 2, rtol 1e-13)',
         'details': dict(rdev, robustness_G_A_BL_changed_by={k_: {'status': st_, 'Y_over_Yeq_x40': r_} for k_, (st_, r_) in robust.items()})},
        {'definition': 'the elastic rate is an ESTIMATE: a factor 1/2 or 2 moves the kinetic decoupling to M/T = %s and Delta N_eff by at most '
                       'the value given (relative)' % ', '.join('%.2f' % xk[f_] for f_ in (0.5, 2.0)),
         'value': max(rel(dN[0.5], dN[1.0]), rel(dN[2.0], dN[1.0])), 'source': 'computed'},
        v25, 1e-10, 'the same equation with the same inputs and the same integration (converged to about 2e-13); the other quantities are '
                    'products of stored 12-digit numbers or the same 0.01 grid in M/T',
        extra_ok=S['nuR_robust'][0] and S['nuR_robust'][1] < 1e-10,
        extra='Y/Y_eq %.12f; with G_A(B - L) changed by +-1e-12, +-2e-12 every integration succeeds (Y/Y_eq within %.0e)' % (
            ratio40, S['nuR_robust'][1]))

    # ---- R26 the self-interaction channel ----
    si = cp['self_interaction_channel']
    f = D['background']['casimir_type']['f_star']
    Glam_B = LAM_B * si['Itilde_lambda'] / (2 * f ** 4 * 1.0) / HG ** 2
    xf_c = cp['I13']['x_f_capped']
    NF = 2

    def si_integrand(lnT):
        T = math.exp(lnT)
        gr_, gs_ = g_of(T)
        Hh = math.sqrt(8 * math.pi ** 3 * gr_ / 90) * T * T / MPl
        nchi = 2 * (MDM * T / (2 * math.pi)) ** 1.5 * math.exp(-MDM / T)
        gam = 2 * nchi * nchi * (MDM ** 2 / (2 * math.pi)) * NF
        return 2 * MDM * gam * (gs_ ** (-1 / 3.) / T) ** 4 / (Hh * T) * T
    accl = gl_int(si_integrand, math.log(MDM / xf_c), math.log(fi['T_max_GeV']))
    dNl = accl / (gs0 ** (-1 / 3.)) ** 4 / rho_nu1
    sdev = {'Delta_Neff_per_Glam2': rel(dNl, si['Delta_Neff_per_Glam2']),
            'G_lambda_benchmark': rel(Glam_B, si['G_lambda_benchmark_vt1_GeV-2']),
            'Delta_Neff_at_bound_vs_0.001': rel(si['Delta_Neff_per_Glam2'] * si['G_lambda_max_GeV-2'] ** 2, 1e-3)}
    v26 = max(sdev.values())
    B.equation(
        'self_interaction_channel',
        'the self-interaction channel chi chibar -> fold pairs of -(lambda/2)(Psibar Psi)^2 and its Delta N_eff',
        'FIELD_EQUATIONS section 10 (the self-interaction channel); SOLUTION step 9 (the self-interaction channel)',
        {'description': 'G_lambda = lambda H Itilde_lambda/(2 f^4 v_t), sigma v = G_lambda^2 M^2/(2 pi) per fold species (ESTIMATE), '
                        'd(rho_fold a^4)/dx4 = 2 M gamma_lambda a^4 from T_max to x_f; Delta N_eff = %.4e G_lambda^2; bound G_lambda <= %.3e '
                        'GeV^-2 (coupled.json self_interaction_channel)' % (si['Delta_Neff_per_Glam2'], si['G_lambda_max_GeV-2']),
         'method': 'trapezoid rule on 800 logarithmic temperatures', 'order': 'non-thermal production (fold bands out of equilibrium)'},
        {'definition': '|Delta N_eff per G_lambda^2 re-integrated (Gauss-Legendre in ln T) / stored - 1|, G_lambda(lambda_B, v_t = H^-3) '
                       'recomputed, Delta N_eff at the bound against 0.001 (relative); Itilde_lambda is checked in '
                       'portal_overlaps_hellmann_feynman',
         'value': v26, 'source': 'computed afresh', 'details': sdev},
        {'definition': 'inverse annihilation of the fold quanta at the bound: the production rate per fold quantum over H (coupled.json '
                       'equilibrium_ratio_at_max); the Fierz coefficients of the cross-section are not computed (ESTIMATE)',
         'value': si['equilibrium_ratio_at_max'], 'source': 'coupled.json'},
        v26, 1e-4, 'the stored integral uses the trapezoid rule on 800 logarithmic points (error about 1e-5 for this steep integrand, as '
                   'measured); 1e-4 is far below the significance of the bound (Delta N_eff = 0.001)',
        extra='largest %s %.1e' % (max(sdev, key=sdev.get), v26))


# ======================================================================================================================
# the in-concert links
def links(D, B, S):
    masses, cp, cos, nu, th, bg = D['masses'], D['coupled'], D['cosmology'], D['neutrino'], D['thermal'], D['background']
    m1 = cos['models'][1]

    # L1 the Kohn-Sham source in the block response
    B.link('ks_energy_density_in_block_response', 'the Kohn-Sham energy density and pressures inserted in the gravitational equation',
           ['kohn_sham_scf', 'kohn_sham_in_gravity_block_response', 'block_linear_response'],
           'block averages rho, p3, pbar of the Kohn-Sham states N8_lamp, N592_lamp, N592_lam0',
           {'here': 'the Kohn-Sham equations: ks/ground8.json, ks/ground592.json int_rho, int_p3, int_pt, int_p0_richardson divided by the cell '
                    'weight 2 Vol7 (1 - e^{-3HL})/(3H)',
            'there': 'the gravitational (block) equation: ks/feedback.json rho_avg, p3_avg, pbar_avg'},
           S['ks_avg_dev'], 1e-10, 'the same integrals divided by the same weight; only the 12-digit storage differs',
           'max relative difference')

    # L2 the hidden pressure of the dark matter
    dm = D['ks_darkmatter']['0']['p0_over_rho']
    vals = {'Kohn-Sham stress tensor p0/rho (ks/darkmatter.json)': dm,
            'x0 eigenvalue -d ln eps_DM/d ln f, closed form (afresh)': -S['dlneps_dlnf_analytic'],
            'x0 eigenvalue, finite difference (ks/spectrum.json)': -D['ks_spectrum']['dln_eps_dm_dln_f'],
            'block-response input, -d ln M_DM/d ln f (analysis.json sensitivities, read by um2_coupled.py)': -D['analysis']['sensitivities_dlnX_dlnf']['M_DM']}
    ref = -S['dlneps_dlnf_analytic']
    B.link('dark_matter_hidden_pressure', 'the hidden pressure of the dark-matter quanta in the Kohn-Sham, x0 and block-response equations',
           ['kohn_sham_scf', 'dirac16complex_x0_spectrum', 'coupled_environment_mean_fields'],
           'p0/rho = -d ln eps_DM/d ln f of the lowest odd level', {'values': vals},
           max(rel(v, ref) for v in vals.values()), 1e-9,
           'the Kohn-Sham stress is Richardson-extrapolated (basis error about 1e-11 here) and the stored derivative uses a step 1e-5 '
           '(error about 1e-11)', 'max relative difference from the closed form')

    # L3 m_Z and the weak angle in the x0 problem and in the Z widths
    B.link('z_mass_x0_vs_z_widths', 'the Z mass from the x0 eigenvalues and in the Z widths',
           ['boson_x0_eigenvalue', 'yang_mills_masses_and_widths'], 'm_Z',
           {'here': 'x0 eigenvalues: m_W sqrt(Lambda_Z/Lambda_W) from masses.json WZ = %.9f GeV' % S['mZ_x0'],
            'there': 'Z widths: m_Z = %.4f GeV (um2_electroweak.py reads the measured value)' % val('m_Z_GeV')},
           rel(S['mZ_x0'], val('m_Z_GeV')), 1e-9, 'the fit reproduces the measured m_Z by construction (to 1e-8 in um2_spectra.py)',
           'relative difference')
    s2c = masses['WZ']['sin2_theta_couplings']
    wc = S['widths'](s2c, S['mZ_x0'])
    w0 = S['widths'](val('sin2_theta_W_MSbar'), val('m_Z_GeV'))
    eff = wc['total_with_QCD_factor'] / w0['total_with_QCD_factor'] - 1
    B.link('weak_angle_x0_vs_z_widths', 'the weak mixing angle of the x0 W/Z problem and of the Z widths',
           ['boson_x0_eigenvalue', 'yang_mills_masses_and_widths'], 'sin^2(theta_W) and its effect on the total Z width',
           {'here': 'x0 W/Z problem (beta_Z = beta_W/cos^2): the angle of the couplings sin^2 = %.6f (masses.json WZ; also the Z condensate '
                    'split in um2_coupled.py)' % s2c,
            'there': 'Z widths, I12 benchmark couplings and running couplings: the MS-bar value %.5f (um2_constants.py)' % val('sin2_theta_W_MSbar'),
            'total_width_with_x0_angle_and_x0_mZ_MeV': wc['total_with_QCD_factor'], 'total_width_reported_MeV': w0['total_with_QCD_factor'],
            'stored_relative_change_tree': D['electroweak']['Z_widths_tree_MeV_coupling_angle']['relative_change_total']},
           abs(eff), 0.02,
           'NOT zero: two values of the same angle (difference %.4f); the scheme ambiguity of a tree-level angle is of the size of the '
           'electroweak loop corrections that UM-2 does not compute (per-cent level), so its effect on the width is allowed up to 2 %%' % (
               val('sin2_theta_W_MSbar') - s2c), 'relative change of the total width (with the QCD factor)')

    # L4 the x0 fermion masses in the thermal history
    fL = masses['scales']['fL_GeV_inv']
    pairs = [(F['e_exact'] / fL, F['m_GeV']) for F in masses['fermions'].values()]
    B.link('fermion_masses_x0_vs_thermal_history', 'the fermion masses of the x0 tip conditions in the thermal history and the sectors that use them',
           ['fermion_x0_tip_determinant', 'thermal_degrees_of_freedom', 'yang_mills_masses_and_widths'], 'the twelve fermion masses',
           {'here': 'x0 roots e_exact/(f L) (masses.json fermions)',
            'there': 'masses.json fermions m_GeV, read by um2_thermal.py species(), um2_coupled.py (I13 components) and um2_electroweak.py '
                     '(top threshold)'},
           maxrel(pairs), 1e-9, 'the fit makes the exact roots equal the targets to 1e-12', 'max relative difference')

    # L5 the neutrino masses and the PMNS matrix
    mx = S['m_x0']
    vals_m = []
    vals_m += list(zip(mx, nu['masses_eV']))
    vals_m += list(zip(mx, [s_['mass_eV'] for s_ in nu['CNB']['states']]))
    vals_m += list(zip(mx, cos['neutrinos']['camb_masses_times_deg_quarter_eV']))
    deg = NEFF_SM[0] / 3.0
    vals_m += list(zip(mx, [x * deg ** 0.25 for x in m1['camb_masses_eV']]))
    vals_m += [(mx.sum(), m1['mnu_sum_eV']), (mx.sum(), nu['sum_masses_eV'])]
    n0 = {k: v[0] for k, v in NUFIT60_NO.items()}
    vals_dm2 = [(mx[2] ** 2 - mx[0] ** 2, n0['dm2_31_eV2']), (mx[1] ** 2 - mx[0] ** 2, n0['dm2_21_eV2'])]
    vals_m += vals_dm2
    B.link('neutrino_masses_tip_matrices_vs_flavour_cnb_cmb', 'the neutrino masses of the tip matrices in the flavour evolution, the CNB '
           'and the CMB (sum of masses)',
           ['fermion_x0_tip_determinant', 'neutrino_flavour_evolution', 'cosmic_neutrino_background', 'linear_perturbations_cmb_bao',
            'neutrino_thermal_potential'],
           'm_1, m_2, m_3, their sum and the splittings dm2_31, dm2_21',
           {'here': 'x0 roots (masses.json fermions nu1..nu3 e_exact/(f L))',
            'there': 'neutrino.json masses_eV and CNB states; CAMB masses m_i deg^{1/4} (cosmology.json neutrinos and models[1]); sum in '
                     'CAMB (models[1].mnu_sum_eV) and neutrino.json sum_masses_eV; the NuFIT splittings that um2_neutrino.py uses directly '
                     '(thermal potential, MSW resonances, supernova envelope); N_eff uses the massless limit (m_3/T_dec)^2 = 6e-16',
            'splittings_relative': maxrel(vals_dm2)},
           maxrel(vals_m), 1e-10, 'the CAMB mass iteration converges to 7.8e-12; everything else is a copy', 'max relative difference')
    from um2_flavour import mixing_matrix
    n_ = {k: v[0] for k, v in NUFIT60_NO.items()}
    Unu = mixing_matrix(math.sqrt(n_['sin2_theta12']), math.sqrt(n_['sin2_theta13']), math.sqrt(n_['sin2_theta23']),
                        math.radians(n_['delta_CP_deg']))
    U = S['U']
    dU = float(np.max(np.abs(Unu - U)))
    dfc = max(abs(abs(U[j, i]) ** 2 - nu['CNB']['states'][i]['flavour_content'][fl]) for i in range(3) for j, fl in enumerate(('e', 'mu', 'tau')))
    B.link('pmns_tip_matrix_vs_flavour_evolution_and_cnb', 'the PMNS matrix (neutrino tip matrix) in the flavour evolution and the CNB',
           ['fermion_x0_tip_determinant', 'neutrino_flavour_evolution', 'cosmic_neutrino_background'], 'U_PMNS',
           {'here': 'flavour.json PMNS (the tip matrix kappa_nu of the three-generation condition)',
            'there': 'the matrix rebuilt by um2_neutrino.py from NuFIT 6.0 (mixing_matrix) and the CNB flavour content |U_alpha i|^2 '
                     '(neutrino.json)', 'max_abs_U': dU, 'max_abs_flavour_content': dfc},
           max(dU, dfc), 1e-11, 'the same parametrisation in double precision, stored with 12 digits', 'max absolute difference')
    om_c = S['Omega_nu_h2_cnb'] * deg ** 0.75
    B.link('omega_nu_cnb_vs_camb', 'the neutrino density today in the CNB and in the CMB computation',
           ['cosmic_neutrino_background', 'linear_perturbations_cmb_bao'], 'Omega_nu h^2 of the three mass states',
           {'here': 'CNB (afresh, x0 masses) times (N_eff/3)^{3/4} = %.6e' % om_c,
            'there': 'CAMB omnuh2 today (cosmology.json models[1].omnuh2_camb_today) = %.6e' % m1['omnuh2_camb_today']},
           rel(om_c, m1['omnuh2_camb_today']), 1e-4,
           'the degeneracy scaling deg^{3/4} is exact for non-relativistic states only; the semi-relativistic nu_1 (16 % above m n, 2 % of the '
           'density) leaves about 1e-5', 'relative difference')
    dneff = {'N_eff total': abs(m1['Neff'] - (nu['N_eff_adopted']['value'] + S['dN_freeze_in'])),
             'massive part': abs(m1['Neff_massive'] - nu['N_eff_adopted']['value']),
             'massless part (fold bands)': abs(m1['Neff_massless'] - S['dN_freeze_in']),
             'cosmology.json Delta_Neff_freeze_in_benchmark': abs(cos['Delta_Neff_freeze_in_benchmark'] - S['dN_freeze_in'])}
    B.link('neff_decoupling_plus_freeze_in_vs_camb', 'N_eff of the neutrino decoupling and of the freeze-in in the CMB computation',
           ['neutrino_decoupling', 'freeze_in', 'linear_perturbations_cmb_bao'], 'N_eff = 3.0432 (neutrinos) + Delta N_eff (fold bands)',
           {'here': 'neutrino.json N_eff_adopted and the freeze-in Delta N_eff(G_V) = (coupled.json Delta_Neff_per_GV2) G_V^2 = %.12f' % S['dN_freeze_in'],
            'there': 'cosmology.json models[1] Neff, Neff_massive, Neff_massless', 'differences': dneff},
           max(dneff.values()), 1e-9, 'the CMB computation copies the adopted value and the freeze-in benchmark (hard-coded 0.001 in '
                                      'um2_cosmology.py)', 'max absolute difference')

    # L6 the relic density as omega_c of the CMB
    h_ = m1['H0'] / 100
    from um2_cosmology import PLANCK
    omc = m1['omegam'] * h_ * h_ - PLANCK['ombh2'] - m1['omnuh2']
    rel_st = 2 * cp['I13']['Omega_h2_per_species_capped']
    rel_re = 2 * S['omega_recomputed']
    B.link('relic_density_vs_cmb_omega_c', 'the relic density of the Boltzmann equation as the cold dark matter of the CMB computation',
           ['boltzmann_relic', 'linear_perturbations_cmb_bao'], 'Omega_c h^2 (two species)',
           {'here': 'Boltzmann: 2 x %.12f (coupled.json I13, stored), 2 x %.12f (re-solved)' % (rel_st / 2, rel_re / 2),
            'there': 'CAMB omega_c = Omega_m h^2 - omega_b - omega_nu of cosmology.json models[1] = %.12f (input 0.1200)' % omc},
           max(rel(rel_st, omc), rel(rel_re, omc)), 1e-6, 'the relic coupling is root-found to 1e-6 in ln G_A (2e-6 in Omega h^2)',
           'max relative difference')

    # L7 the Hubble rate of the thermal history against the four-dimensional Friedmann equation with all species
    from um2_thermal import gas, species, thermo
    cosmo = S['cosmo']
    MDM = S['MDM']
    T_fo = S['T_fo']
    kV = cp['block_response_coefficients']['kappa_over_Vperp_GeV-2']
    Gk = bg['casimir_type']['G_k_star_value']
    gr_t = cosmo.g(T_fo)[0]
    H_th = math.sqrt(8 * math.pi ** 3 * gr_t / 90) * T_fo ** 2 / val('M_Pl_GeV')
    sp_ = species(masses, MDM)
    g_ex = thermo(T_fo, sp_, include_dm=False)[0]
    rho_sm = math.pi ** 2 / 30 * g_ex * T_fo ** 4
    rho_dm = S['dm_share_xf'] * math.pi ** 2 / 30 * gr_t * T_fo ** 4
    rho_fold = S['fold_share_fo'] * math.pi ** 2 / 30 * gr_t * T_fo ** 4
    H_4 = math.sqrt(kV / Gk * (rho_sm + rho_dm + rho_fold) / 3)
    dH = abs(H_4 / H_th - 1)
    B.notes.append({'item': 'the fold bands of the freeze-in are not in the Hubble rate of the Boltzmann equation',
                    'value': dH, 'explanation': 'at the freeze-out (T = %.1f GeV) the fold quanta produced since T_max = 10 TeV carry %.2e of the '
                                                'energy density (Delta N_eff = 0.001 today, diluted by (g_s0/g_s)^{4/3}); the four-dimensional '
                                                'Friedmann equation with all species has H larger by %.1e; the relic changes by about the same '
                                                'relative amount' % (T_fo, S['fold_share_fo'], dH)})
    B.link('hubble_rate_thermal_vs_four_dimensional_friedmann', 'the expansion rate of the thermal history against the four-dimensional '
           'Friedmann equation with all species, at the dark-matter freeze-out',
           ['thermal_degrees_of_freedom', 'boltzmann_relic', 'four_dimensional_effective_gravity', 'freeze_in'], 'H(T_fo)',
           {'here': 'Boltzmann equation: H = (8 pi^3 g_rho/90)^{1/2} T^2/M_Pl with the ideal Standard-Model g_rho (thermal history, '
                    'M_Pl = %.5e GeV) = %.6e GeV' % (val('M_Pl_GeV'), H_th),
            'there': 'four-dimensional Friedmann equation H^2 = (8 pi G_N/3) rho_all with 8 pi G_N = (kappa/V_perp)/G(k*) of the reduction '
                     '(coupled.json, background.json) and rho_all = Standard Model + dark matter (Y(x_f)) + fold bands produced by freeze-in '
                     'since T_max = 10 TeV: H = %.6e GeV' % H_4,
            'shares_of_rho_at_T_fo': {'dark matter': S['dm_share_xf'], 'fold bands': S['fold_share_fo'],
                                      'g_rho interpolation': abs(gr_t / g_ex - 1)},
            'dark_matter_share_at_x_5': S['dm_share_x5'],
            'not_included_in_either': 'the radion oscillation left by the deflation (redshifts like dust; OPEN, the moduli problem) and the '
                                      'O(alpha) interaction energy (about %.1f %%, thermal_degrees_of_freedom)' % (100 * S['p2_relative_fo'])},
           dH, 1e-3, 'NOT zero: the thermal history leaves out the fold bands (%.1e of rho at T_fo); since Y_inf ~ H(x_f), the relic moves by '
                     'about the same relative amount, which must stay well below the 1 %% precision of the measured Omega_c h^2 (0.1200 +- '
                     '0.0012): 1e-3 keeps it a factor 10 below' % S['fold_share_fo'], 'relative difference |H_4D/H_thermal - 1|')
    neff_cmb = m1['Neff']
    g_cmb = 2 + 7.0 / 8 * 2 * (4.0 / 11) ** (4.0 / 3) * neff_cmb
    d_late = rel(th['today']['g_rho'], g_cmb)
    B.link('late_time_radiation_thermal_vs_cmb', 'the radiation density after neutrino decoupling in the thermal history and in the CMB computation',
           ['thermal_degrees_of_freedom', 'neutrino_decoupling', 'linear_perturbations_cmb_bao'], 'g_rho today (massless neutrinos)',
           {'here': 'thermal history (instantaneous decoupling at 2 MeV, N_eff = 3): g_rho = %.6f (thermal.json today)' % th['today']['g_rho'],
            'there': 'CMB computation: 2 + (7/4)(4/11)^{4/3} N_eff with N_eff = %.4f: %.6f' % (neff_cmb, g_cmb)},
           d_late, 0.01, 'NOT zero: the thermal history decouples the neutrinos instantaneously (documented approximation); below 2 MeV it only '
                         'enters the entropy today (g_s = 43/11, the standard value for s_0) and the nucleosynthesis environment (effects '
                         'below 1e-58), so 1 % (the size of N_eff/3 - 1 times the neutrino share) is what the results tolerate',
           'relative difference')
    rho_cp = cp['environments']['dark-matter freeze-out (T = 1.42 TeV)']['sources_GeV4']['rho']
    rho_thr = rho_sm + gas(MDM * math.exp(0), T_fo, 8, True)[0]
    B.link('plasma_energy_density_thermal_vs_coupled_sources', 'the plasma energy density at the freeze-out in the thermal history and in '
           'the block sources of the coupled solution',
           ['thermal_degrees_of_freedom', 'coupled_environment_mean_fields'], 'rho(T_fo)',
           {'here': 'thermal history: ideal gases with the x0 masses plus the equilibrium dark matter = %.6e GeV^4' % rho_thr,
            'there': 'coupled.json freeze-out sources_GeV4.rho = %.6e GeV^4 (adds the QCD interaction measure and the electroweak trace '
                     'anomaly)' % rho_cp},
           rel(rho_cp, rho_thr), 0.01, 'NOT zero by design: the block sources add the trace anomaly of the interacting plasma (O(alpha_s^2) '
                                       'T^4), which only enters rho - 3 p3; the O(alpha) energy (5 %) is absent from both; 1 % bounds the '
                                       'trace-anomaly share', 'relative difference')

    # L8 the portal mean fields, O, the I12 benchmark, the dark-matter mass, the couplings
    po = D['ks_portals']
    Idm = cp['overlaps_Itilde']['dark matter (lowest odd level)']
    pv = [(po['I11 vector contact, electron density (v)']['hellmann_feynman'], 0.5 * (Idm['L (lepton doublets)'] + Idm['e_R'])),
          (po['I11 vector contact, up-quark density (v)']['hellmann_feynman'], 0.5 * (Idm['Q (quark doublets)'] + Idm['u_R'])),
          (po['I11 vector contact, neutrino density (v, left-chiral)']['hellmann_feynman'], Idm['L (lepton doublets)'])]
    fdv = [(po['I11 vector contact, electron density (v)']['d_eps_dm_de'], 0.5 * (Idm['L (lepton doublets)'] + Idm['e_R'])),
           (po['I11 vector contact, up-quark density (v)']['d_eps_dm_de'], 0.5 * (Idm['Q (quark doublets)'] + Idm['u_R'])),
           (po['I11 vector contact, neutrino density (v, left-chiral)']['d_eps_dm_de'], Idm['L (lepton doublets)'])]
    B.link('portal_responses_ks_jobs_vs_coupled_overlaps', 'the mean fields of the Standard-Model fermions in the Kohn-Sham equations of the '
           'Kohn-Sham jobs and of the coupled solution',
           ['portal_overlaps_hellmann_feynman', 'kohn_sham_scf', 'coupled_environment_mean_fields'],
           'd eps_DM/de for the electron, up-quark and neutrino densities',
           {'here': 'ks/portals.json Hellmann-Feynman expectation (and the self-consistent finite difference at e = +-1e-3: %.1e, its O(e^2) '
                    'error)' % maxrel(fdv),
            'there': 'coupled.json overlaps: (Itilde_L + Itilde_eR)/2, (Itilde_Q + Itilde_uR)/2, Itilde_L'},
           maxrel(pv), 1e-9, 'two scripts, the same orbitals (80 functions per sector) and profiles', 'max relative difference')
    Ovals = {'hard-coded in um2_thermal.py and um2_coupled.py': O_HARDCODED,
             'Kohn-Sham response (ks/portals.json, Hellmann-Feynman)': po['I12 gluon condensate <G G> (M, uniform)']['hellmann_feynman'],
             'coupled.json WZ_kinetic_shift.O_integral': cp['WZ_kinetic_shift']['O_integral'], 'closed form (afresh)': S['O_analytic']}
    B.link('i12_response_O_across_scripts', 'the I12 response O = d eps_DM/dm in the Kohn-Sham equations and in the relic and mean-field '
           'computations and as the integral of the scalar density s_DM = 2ab that enters the W kinetic function',
           ['portal_overlaps_hellmann_feynman', 'boltzmann_relic', 'coupled_environment_mean_fields', 'wz_x0_with_dark_matter_kinetic_function'],
           'O = int s_DM dy',
           {'values': Ovals}, max(rel(v, S['O_analytic']) for v in Ovals.values()), 1e-4,
           'the hard-coded value carries 4 digits (rounding up to 7e-5); it enters c/Lambda*^3 and the I12 mean field linearly',
           'max relative difference from the closed form')
    cL3 = th['I12_universal_benchmark']['c_over_Lambda_star3_GeV-3']
    dmI = maxrel((cL3 * (e['condensates_GeV4']['GG'] + e['condensates_GeV4']['WW'] + e['condensates_GeV4']['BB']), e['dM_I12_GeV'])
                 for e in cp['environments'].values())
    B.link('i12_benchmark_thermal_vs_coupled_mean_field', 'the I12 benchmark strength of the relic computation in the I12 mean field of '
           'the environments', ['boltzmann_relic', 'coupled_environment_mean_fields'], 'c/Lambda*^3',
           {'here': 'thermal.json I12_universal_benchmark.c_over_Lambda_star3 = %.6e GeV^-3' % cL3,
            'there': 'coupled.json environments dM_I12 = c/Lambda*^3 (<g_s^2 GG> + <g^2 WW> + <g\'^2 BB>)'},
           dmI, 1e-10, 'the same 12-digit number', 'max relative difference over the environments')
    HG = masses['scales']['H_GeV']
    Mks = D['ks_spectrum']['eps_dm'] * HG
    dmm = maxrel([(Mks, th['M_DM_GeV']), (Mks, D['analysis']['M_DM_GeV']),
                  (8 * D['ks_spectrum']['eps_dm'], D['ks_darkmatter']['0']['dE'])])
    B.link('dark_matter_mass_ks_vs_boltzmann', 'the dark-matter mass of the x0/Kohn-Sham spectrum in the Boltzmann equation and the analysis',
           ['dirac16complex_x0_spectrum', 'kohn_sham_scf', 'boltzmann_relic', 'coupled_environment_mean_fields'], 'M_DM',
           {'here': 'eps_DM H (ks/spectrum.json, masses.json) = %.6f GeV; the Kohn-Sham energy of eight quanta 8 eps_DM' % Mks,
            'there': 'thermal.json M_DM_GeV, analysis.json M_DM_GeV, ks/darkmatter.json dE (lambda = 0)'},
           dmm, 1e-11, '12-digit copies; the Kohn-Sham bookkeeping is exact at lambda = 0', 'max relative difference')
    fo = cp['environments']['dark-matter freeze-out (T = 1.42 TeV)']
    b11, b13 = S['env_brackets']['dark-matter freeze-out (T = 1.42 TeV)']
    gpairs = [(fo['d_eps_DM_I13_GeV'] / b13, cp['I13']['G_A_GeV-2']), (fo['d_eps_DM_I11_GeV'] / b11, cp['freeze_in']['G_V_benchmark_GeV-2'])]
    B.link('relic_and_freeze_in_couplings_in_mean_fields', 'the I13 coupling of the relic and the I11 coupling of the freeze-in in the '
           'Kohn-Sham mean fields of the environments', ['boltzmann_relic', 'freeze_in', 'coupled_environment_mean_fields'], 'G_A, G_V',
           {'here': 'G_A of the capped relic (coupled.json I13), G_V of the freeze-in benchmark (coupled.json freeze_in)',
            'there': 'the strengths implied by the stored mean-field shifts at the freeze-out, delta eps / (sum_f q_f Itilde_f n_f)'},
           maxrel(gpairs), 1e-10, 'the mean fields are computed with these strengths', 'max relative difference')

    LWm = masses['WZ']['Lambda_W']
    LWf = cp['WZ_kinetic_shift']['Lambda_W_fem']
    B.link('w_eigenvalue_x0_vs_kinetic_function_problem', 'the W eigenvalue of the x0 problem in the W problem with the dark-matter '
           'kinetic function', ['boson_x0_eigenvalue', 'wz_x0_with_dark_matter_kinetic_function'], 'Lambda_W at e = 0',
           {'here': 'masses.json WZ.Lambda_W (exact characteristic equation) = %.11e' % LWm,
            'there': 'coupled.json WZ_kinetic_shift.Lambda_W_fem (300 quadratic elements, matrix Rayleigh quotient) = %.11e; the shooting of '
                     'wz_x0_with_dark_matter_kinetic_function at e = 0: %.11e' % (LWf, S['L0_shoot']),
            'shooting_relative': rel(S['L0_shoot'], LWm)},
           max(rel(LWf, LWm), rel(S['L0_shoot'], LWm)), 1e-5,
           'the finite-element value carries the rounding of the matrix Rayleigh quotient of a nearly constant vector (about 1e-11 absolute, '
           '1e-6 of Lambda_W) besides the discretisation; it enters only as the normalisation of d ln Lambda_W/de',
           'max relative difference')

    # L9 the block response coefficients, the radion, f*
    brc = cp['block_response_coefficients']
    lr = bg['linear_response_static_dk']
    printed = {'c_rho': 0.035852, 'c_3': -0.107556, 'c_p': -0.140028}
    stiff = 3.0 - 4.0 * KRHO_EXACT / KSTAR_EXACT
    d_ss = max(abs(brc['c_rho'] - lr['per_kappa_drho_H2']), abs(brc['c_3'] - lr['per_kappa_dp3_H2']), abs(brc['c_p'] - lr['per_kappa_dpbar_H2']))
    d_pr = max(abs(printed['c_rho'] - lr['per_kappa_drho_H2']), abs(printed['c_3'] - lr['per_kappa_dp3_H2']), abs(printed['c_p'] - lr['per_kappa_dpbar_H2']))
    d_cp = abs(lr['per_kappa_dpbar_H2'] - 1.0 / stiff)
    B.link('block_response_coefficients_across_scripts', 'the block-response coefficients in the background, Kohn-Sham feedback and coupled '
           'computations and in the documents', ['block_linear_response', 'kohn_sham_in_gravity_block_response', 'coupled_environment_mean_fields'],
           'c_rho, c_3, c_p',
           {'here': 'background.json linear_response_static_dk (exact algebraic numbers)',
            'there': 'coupled.json block_response_coefficients; ks/feedback.json (reads background.json); FIELD_EQUATIONS 7.1 and SOLUTION '
                     'step 3 print 0.035852, -0.107556, -0.140028; c_p = 1/(3 H^2 - 4 kappa rho_b*/k*) in closed form',
            'stored_vs_stored': d_ss, 'printed_vs_stored': d_pr, 'c_p_closed_form': d_cp},
           max(d_ss, d_cp), 1e-9, 'stored copies of exact algebraic numbers (12 digits); the printed values carry 6 decimals and must lie '
                                  'within half a unit of the last one (5e-7)', 'max absolute difference of the stored values (printed: separate '
                                  'condition <= 5e-7)', extra_ok=d_pr <= 5e-7, extra='printed values within %.1e' % d_pr)
    om_lin = math.sqrt(31552.0 / 2249.0 - 2416.0 * math.sqrt(51) / 6747.0)
    rvals = [(bg['radion_frequency_over_H'], om_lin), (masses['scales']['radion_mass_GeV'] / HG, om_lin),
             (D['series']['radion']['mass_GeV'] / HG, om_lin), (D['analysis']['radion_decay_estimate']['m_r_GeV'] / HG, om_lin)]
    d_nl = rel(S['primordial_omega'], om_lin)
    B.link('radion_frequency_linear_vs_nonlinear', 'the radion frequency of the linearised block equations, of the nonlinear primordial '
           'evolution and in the masses, the series and the analysis', ['block_linear_response', 'primordial_deflation_system', 'graviton_tower',
                                                                        'metric_series_order2'], 'omega_r = m_r/H',
           {'here': 'closed form sqrt(31552/2249 - 2416 sqrt(51)/6747) = %.9f' % om_lin,
            'there': 'background.json, masses.json scales, series.json radion, analysis.json; nonlinear: primordial.json '
                     'omega_from_zero_crossings = %.9f' % S['primordial_omega'], 'copies_max_relative': maxrel(rvals), 'nonlinear_relative': d_nl},
           max(maxrel(rvals), d_nl), 1e-3, 'the nonlinear frequency is measured from zero crossings of a finite oscillation (relative amplitude '
                                           '3e-3 at x4 > 30/H): anharmonic shifts and the crossing estimate allow 1e-3; the copies agree to 1e-12',
           'max relative difference')
    f0 = bg['casimir_type']['f_star']
    fv = [masses['scales']['f_star'], D['ks_ground8']['_meta']['f'], D['ks_ground592']['_meta']['f'], D['ks_spectrum']['f'],
          D['ks_spectrum']['fL'] / L_CELL, D['series']['order0']['f_star']]
    B.link('static_block_f_star_across_scripts', 'the block scale f* of the static block in the x0 spectra, the Kohn-Sham states and the series',
           ['einstein_lovelock_background', 'boson_x0_eigenvalue', 'fermion_x0_tip_determinant', 'dirac16complex_x0_spectrum', 'kohn_sham_scf'],
           'f* = k*^{-1/2}', {'here': 'background.json casimir_type.f_star = %.12f (closed form %.12f)' % (f0, KSTAR_EXACT ** -0.5),
                              'there': 'masses.json scales, ks/ground8.json, ks/ground592.json, ks/spectrum.json (f, fL/3), series.json order0'},
           max(max(rel(x, f0) for x in fv), rel(f0, KSTAR_EXACT ** -0.5)), 1e-11, '12-digit copies of one closed-form number',
           'max relative difference')

    # L10 the heating factor F_h
    run_ = nu['N_eff_runs']['FD_common_NLO']
    Fh = (run_['Tnu_e_over_Tgamma'] * (11.0 / 4.0) ** (1.0 / 3.0) / (1 + run_['heating_Te_a'])) ** 4
    bl = cp['I13_B_minus_L_alternative']
    Fh_cp = bl['Delta_Neff'] / (3 * (10.75 / bl['g_s_at_decoupling']) ** (4.0 / 3.0))
    Fv = {'electroweak.json Psi_A_thermalisation.non_instantaneous_factor_F': D['electroweak']['Psi_A_thermalisation']['non_instantaneous_factor_F'],
          'um2_coupled.py (hard-coded; from I13_B_minus_L_alternative)': Fh_cp}
    B.link('decoupling_heating_factor_F_h', 'the non-instantaneous heating factor F_h of the neutrino decoupling where Delta N_eff of other '
           'species is computed', ['neutrino_decoupling', 'right_handed_neutrino_boltzmann', 'self_interaction_channel', 'yang_mills_masses_and_widths'],
           'F_h = [(T_nu/T_gamma)(11/4)^{1/3}/(1 + h_nu)]^4',
           {'here': 'neutrino decoupling (neutrino.json N_eff_runs.FD_common_NLO): %.9f' % Fh, 'there': Fv},
           max(rel(v, Fh) for v in Fv.values()), 1e-4, 'the hard-coded 1.0095 carries 4 decimals (rounding up to 5e-5)', 'max relative difference')

    # L11 the metric series against cosmology, coupled, masses
    ser = D['series']
    sv = [(a['Delta_Phi_Weyl'], b['Delta_Phi_Weyl']) for a, b in zip(ser['order1_n0']['Delta_Phi_today'], m1['Delta_Phi_z0'])]
    sv += [(ser['radion']['static_response'][k]['delta_ln_f'], cp['environments'][k]['delta_ln_f']) for k in cp['environments']]
    sv += [(ser['kaluza_klein_gravitons'][1]['m_GeV'], masses['scales']['m_KK_GeV']), (ser['order1_n0']['sigma8_UM2'], m1['sigma8'])]
    sv += [(S['mKK_x0'], masses['scales']['m_KK_GeV'])]
    B.link('metric_series_vs_cosmology_coupled_masses', 'the terms of the metric series against the cosmology, the coupled solution and the '
           'masses', ['metric_series_order2', 'graviton_tower', 'linear_perturbations_cmb_bao', 'coupled_environment_mean_fields'],
           'Delta_Phi(k), delta ln f, m_1 = m_KK, sigma_8',
           {'here': 'series.json', 'there': 'cosmology.json models[1], coupled.json environments, masses.json scales (m_KK = m_W sqrt(Lambda_1/'
                                            'Lambda_W) recomputed)'},
           maxrel(sv), 1e-10, 'copies, and m_KK recomputed from 12-digit eigenvalues', 'max relative difference')

    # L12 the freeze-out temperature
    Tenv = fo['T_GeV']
    B.link('freeze_out_temperature_relic_vs_environment', 'the freeze-out of the relic in the freeze-out environment of the coupled solution '
           'and in the self-interaction channel', ['boltzmann_relic', 'coupled_environment_mean_fields', 'self_interaction_channel'],
           'T_fo = M_DM/x_f', {'here': 'M_DM/x_f with x_f = %.10f (coupled.json I13.x_f_capped)' % cp['I13']['x_f_capped'],
                                'there': 'coupled.json environments freeze-out T_GeV = %.10f; the self-interaction integration ends at the same '
                                         'x_f' % Tenv},
           rel(Tenv, S['MDM'] / cp['I13']['x_f_capped']), 1e-10, 'the same numbers', 'relative difference')

    # L13 the block sensitivities of the masses
    sens = D['analysis']['sensitivities_dlnX_dlnf']
    dlz = lambda c_: 1 - c_ - c_ / math.tanh(c_)          # d ln zeta^2/d ln c, zeta^2 = c e^{-c}/sinh c
    sens_pairs = []
    for n, F in masses['fermions'].items():
        sens_pairs.append((-1 + 0.5 * (dlz(F['c_L']) + dlz(-F['c_R'])), sens['m_' + n]))
    psen = cp['proton_sensitivity']
    a_s, mZ0, mKK = val('alpha_s_mZ'), val('m_Z_GeV'), masses['scales']['m_KK_GeV']
    as_KK = 1 / (1 / a_s + 7.0 / (2 * math.pi) * math.log(mKK / mZ0))
    L6 = -1 - 8 * math.pi / (7 * as_KK)
    L3 = 21 / 27. * L6 + 2 / 27. * (sens['m_t'] + sens['m_b'] + sens['m_c'])
    mp_ = 0.93827
    dmp = (1 - (0.045 + 0.040) / mp_) * L3 + 0.045 / mp_ * 0.5 * (sens['m_u'] + sens['m_d']) + 0.040 / mp_ * sens['m_s']
    sens_pairs += [(L6, psen['dlnLambda6_dlnf']), (L3, psen['dlnLambda3_dlnf']), (dmp, psen['dln_mp_dlnf'])]
    B.link('block_sensitivities_x0_formula_vs_block_response', 'the block sensitivities d ln m/d ln f of the x0 mass formula as used in '
           'the hidden pressure of the block response', ['fermion_x0_tip_determinant', 'coupled_environment_mean_fields'],
           'd ln m_f/d ln f (12 fermions), d ln Lambda^(6,3)/d ln f, d ln m_p/d ln f',
           {'here': 'the first-order x0 formula -1 + (1/2)[d ln zeta^2(c_L)/d ln c_L + d ln zeta^2(-c_R)/d ln(-c_R)], d ln zeta^2/d ln c = 1 - c - '
                    'c coth c (closed form, masses.json c_L, c_R); the one-loop QCD-scale and nucleon formulas of FIELD_EQUATIONS 7.1',
            'there': 'analysis.json sensitivities_dlnX_dlnf (numerical derivative), read by um2_coupled.py; coupled.json proton_sensitivity'},
           maxrel(sens_pairs), 1e-9, 'the stored derivatives use a central difference with step 1e-6 at 60 digits (error about 1e-12)',
           'max relative difference')


# ======================================================================================================================
def main():
    rep = Report('residuals-checks', 'UM-2 residuals: how well the approximate solution satisfies every coupled field equation it uses, '
                 'and the consistency of the solution across the equations (in concert)')
    D = load()
    B = Builder(rep)
    S = {}
    gravity(D, B, S)
    x0_spectra(D, B, S)
    kohn_sham(D, B, S)
    portals_and_environments(D, B, S)
    electroweak_cosmology_series(D, B, S)
    neutrinos(D, B, S)
    thermal(D, B, S)
    links(D, B, S)
    B.finish()
    # notes: version-3 quantities that differ between two places (beyond the links), found while computing the residuals
    B.notes.append({'item': 'd/dk [6 H^2 k (1 - 2 w2 k) + kappa rho_b] at k*',
                    'stored': D['ks_feedback']['d_F4_dk'], 'where_stored': 'ks/feedback.json d_F4_dk; quoted as "-6 x 10^-12" in SOLUTION step 3',
                    'recomputed': 0.0, 'explanation': 'the exact value is 0 (k*^2 - 24 k* + 160/3 = 0); the stored number is the rounding of the '
                                                      '12-digit k* and kappa rho_b* (closed form in double precision: about 1e-15 of the terms)'})
    B.notes.append({'item': 'the dark matter in g_rho at the start of the Boltzmann integration',
                    'value': S['dm_share_x5'],
                    'explanation': 'FIELD_EQUATIONS section 10 leaves the dark matter out of g_rho because it adds less than 0.1 at 5 TeV (true: '
                                   'x = 8.9); the Boltzmann integration starts at x = 5 (T = 8.9 TeV), where it carries %.1e of rho; harmless, '
                                   'since Y = Y_eq there' % S['dm_share_x5']})
    out = {'description': 'UM-2 version 3: residuals of the approximate solution in every coupled field equation it uses, and the '
                          'consistency of the solution across the equations (in concert); written by um2_residuals.py',
           'equations': B.equations, 'in_concert_links': B.links, 'notes': B.notes,
           'summary': {'equation_count': len(B.equations), 'link_count': len(B.links),
                       'equations_not_small': [e['equation'] for e in B.equations if e['check']['tolerance'] > 1e-3],
                       'links_not_zero': [lk['link'] for lk in B.links if lk['tolerance'] >= 1e-3]}}
    write_json(os.path.join(OUT, 'residuals.json'), out)
    ok = rep.write()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
