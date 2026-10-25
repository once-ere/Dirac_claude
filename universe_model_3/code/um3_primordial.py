#!/usr/bin/env python3
"""um3_primordial.py - the primordial era of UM-3: what the author's vacuum does to the fields of the fold, and why the
primordial spectrum of the CMB (A_s, n_s of Planck 2018) cannot come from it.

In the author's vacuum a4 = H x4 and b4 = b0 (constant): ordinary space expands with the rate H and the extra times
deflate, e^{-a4} b4 = b0 e^{-H x4}.  A field of the fold has the action (four-dimensional normalisation)
    S = int d^4x sqrt(-h) Z [ -(1/2) h^{mu nu} d_mu phi d_nu phi - (1/2) m^2 phi^2 ],
    h_{mu nu} = diag(e^{2 a4}, e^{2 a4}, e^{2 a4}, -1),  sqrt(-h) = e^{3 a4},  Z = V_t (e^{-a4} b4)^3 / V_*,
(V_t the coordinate volume of the extra times, V_* their physical volume in the late universe) and its Fourier mode
phi_k(x4) obeys (sqrt(-h) Z phi_k')' / (sqrt(-h) Z) + (k^2 e^{-2 a4} + m^2) phi_k = 0.
Checks:
  PR1  in the author's vacuum sqrt(-h) Z = V_t b0^3/V_* is constant: the fields of the fold feel no Hubble friction
       (sympy);
  PR2  the massless mode equation phi'' + k^2 e^{-2 H x4} phi = 0 is Bessel's equation of order 0 in k tau, tau =
       e^{-H x4}/H; with the canonical normalisation (Wronskian) phi_k = sqrt(pi/(4H)) H_0^(1)(k tau), independent of k
       at early times, and at late times |phi_k|^2 = (pi/(4H)) [1 + (4/pi^2) (ln(k tau/2) + gamma_E)^2]: the power
       spectrum k^3 |phi_k|^2/(2 pi^2) grows like k^3 (times a logarithm); the mode equation integrated numerically from
       the early-time vacuum agrees, and the spectral index n - 1 = d ln P/d ln k is close to 3 (Planck: n_s - 1 = -0.035);
  PR3  the gauge couplings of the fold: the gauge action carries Z/g^2, so the effective coupling g^2/Z grows like
       e^{3 H x4}: the couplings of the fold grow like e^{3 H x4/2} in the author's vacuum;
  PR4  the observed spectrum therefore cannot have left the horizon in the author's vacuum: it needs an era with frozen
       extra times (Z constant) and nearly exponential expansion; the bound on primordial gravitational waves
       (r < 0.036, BICEP/Keck 2021, A_s = 2.1e-9) limits its Hubble rate to H_inf < pi M_Pl,red sqrt(r A_s/2) = 4.7e13 GeV;
  PR5  UM-3 contains no inflaton; the Higgs field could inflate only with a non-minimal coupling xi_H of order 10^4
       (A_s = lambda N^2/(72 pi^2 xi^2), N = 55), while the induced Einstein-Hilbert term of the fold, if it comes from the
       loops of the fields of the fold (Sakharov), needs 1 - 6 xi_H > 0: the two exclude each other.
Writes outputs/primordial.json and reports/primordial_checks.json.  Runs in a few seconds.
Usage: python universe_model_3/code/um3_primordial.py

BEGIN FOLD DEFINITION
THE FOLD (the definition used in every UM-3 file)

Definition. The fold is the seven-dimensional surface of the author's eight-dimensional spacetime on which the cosine of
the angle z = 6 H x0 of the hidden direction vanishes:
    (FD-1)  F = { X = (x0, x1, ..., x7) : cos(6 H x0) = 0 };  in one period 0 < z < pi of the metric: z = pi/2, x0 = pi/(12 H).
X = {x0, ..., x7} are the author's coordinates: x0 the hidden space-like direction, x1, x2, x3 ordinary space, x4 the
time, x5, x6, x7 the three extra times; H is the author's constant (an inverse length). The author's metric depends on x0
only through cot(z)^2 and (sin(z)^2)^(1/6), so it repeats with the period pi/(6 H) of x0, and every period 0 < z < pi
contains exactly one fold, at z = pi/2. A point of the fold is labelled by the seven coordinates x1, ..., x7, and the
metric restricted to the fold (dx0 = 0, z = pi/2) is
    (FD-2)  ds^2 on F = e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - dx4^2 - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2),
with three space-like and four time-like directions; a4 and b4 are the author's two functions of the time x4.

Why this surface is called a fold. Measured by the proper distance along the hidden direction,
    (FD-3)  sigma = sgn(pi/2 - z) ln(sin z)/(6 H),   d sigma = |cot z| dx0,   sin z = e^(-6 H |sigma|)
(the fold is sigma = 0; the half-period 0 < z < pi/2 is sigma < 0, the half-period pi/2 < z < pi is sigma > 0; the two ends
of the period, the tips z -> 0 and z -> pi, lie at sigma -> -infinity and sigma -> +infinity), the author's metric is
    (FD-4)  ds^2 = d sigma^2 + e^(-2 H |sigma|) [ e^(2 a4) (dx1^2 + dx2^2 + dx3^2) - e^(-2 a4) b4^2 (dx5^2 + dx6^2 + dx7^2) ] - dx4^2.
It depends on sigma only through |sigma|. Four properties make the surface sigma = 0 a fold, and together they single it
out within the period:
  1. It is a mirror. The reflection sigma -> -sigma (that is z -> pi - z, or x0 -> pi/(6 H) - x0) maps the metric to
     itself, and the fold is the only surface of the period that the reflection leaves in place: the two halves of the
     period are mirror images of each other, joined along the fold, as the two halves of a folded sheet of paper are
     joined along the crease.
  2. The warp is largest on it. The warp factor (sin(z)^2)^(1/6) = e^(-2 H |sigma|), which multiplies ordinary space and
     the extra times, equals 1 on the fold and decreases on both sides.
  3. The metric has a kink on it. The metric is continuous across the fold, but its first derivative along sigma jumps.
     The extrinsic curvature of the surfaces sigma = const changes sign across the fold,
        (FD-5)  K^a_b = (1/2) g^ac d_sigma g_cb:  K^1_1 = K^2_2 = K^3_3 = K^5_5 = K^6_6 = K^7_7 = -H sgn(sigma),  K^4_4 = 0;
     (g_ab the metric components along the fold, g^ab their inverse, d_sigma the derivative with respect to sigma, sgn the
     sign function); it jumps by -2 H along ordinary space and along the extra times. The Einstein-Lovelock equations are
     linear in the second sigma-derivatives of the metric, so the jump puts a Dirac delta function delta_D(sigma) into
     them: the metric solves them only if the fold carries a thin source S^a_b, an energy-momentum tensor concentrated on
     sigma = 0 (the junction conditions). At the author's vacuum (a4' = H, b4 constant) its frame components along (ordinary space, the
     time, the extra times) are kappa S = (-10 H, -6 H, -10 H), at the static late-time state (a4 and b4 constant)
     kappa S = (-61 H/8, -31 H/4, -61 H/8), with kappa = 8 pi G_8 the gravitational coupling of eight dimensions. The fold
     is therefore not only a place but a physical object: a thin layer that carries energy and momentum (a brane).
  4. The author's coordinate x0 degenerates on it. The metric component g_x0x0 = cot(6 H x0)^2 vanishes on the fold and
     nowhere else in the period; near the fold the proper distance grows with the square of the coordinate distance,
        (FD-6)  |sigma| = 3 H (x0 - pi/(12 H))^2 [1 + 6 H^2 (x0 - pi/(12 H))^2 + ...],
     so the two coordinate values on either side of x0 = pi/(12 H) at the same coordinate distance lie at the same proper
     distance from the fold: the coordinate line of x0 is folded onto the line of proper distances (a fold map, example 5).

What lives on the fold. In UM-3 the Standard Model (the Higgs doublet with the ad hoc vacuum, the gauge fields of
SU(3)_C x SU(2)_L x U(1)_Y, three generations of quarks and leptons and three right-handed neutrinos), the fold fluid and
the induced Einstein-Hilbert term of the fold live on the fold: they are fields at sigma = 0, functions of x1, ..., x4 (no
field depends on the extra times). Integrated over the extra times, the fold is the four-dimensional universe that we
observe, with the metric diag(e^(2 a4), e^(2 a4), e^(2 a4), -1) in x1, ..., x4. dirac16complex and gravity live in the
bulk sigma != 0 as well as on the fold; the bound states chi of dirac16complex are the part of it that the fold holds,
and the portals couple dirac16complex to the Standard Model at sigma = 0. In UM-3 files the word fold means this surface
and nothing else: a number of equal energy levels is written as a number of degenerate states, and a growth by powers of
Euler's number as a logarithm.

Examples of folds that are meaningful for UM-3.
  1. Our fold. The fold z = pi/2 of the period that contains our world (FD-1): the seven-dimensional world-volume of the
     Standard Model, and after the integration over the extra times the four-dimensional universe that we observe.
  2. The copies of the fold. Because the metric repeats with the period pi/(6 H), every surface
     x0 = pi/(12 H) + (an integer multiple of pi/(6 H)) is a copy of the fold, one per period. Neighbouring copies are
     separated by a tip (z a multiple of pi), where the warp (sin(z)^2)^(1/6) vanishes and g_x0x0 = cot(z)^2 diverges, and
     which lies at an infinite proper distance from both: in proper distance every copy has its own complete line
     -infinity < sigma < infinity. This is why the period pi/(6 H) of x0 produces no Kaluza-Klein tower with the spacing
     12 H; the x0 mass of the bound states is their binding to the fold.
  3. A folded sheet of paper. The crease of a folded sheet is a fold in this sense: the two halves are mirror images
     (property 1) joined along the crease, the sheet is continuous there and its direction changes abruptly (property 3).
     In UM-3 the direction across the crease is the hidden direction sigma, the seven directions along the crease are
     x1, ..., x7, and the crease is the fold.
  4. A folded function. The warp factor e^(-2 H |sigma|) is the simplest folded function: continuous, mirror symmetric,
     largest at sigma = 0, with a jump of its derivative,
        (FD-7)  d/d sigma e^(-2 H |sigma|) = -2 H sgn(sigma) e^(-2 H |sigma|),
                d^2/d sigma^2 e^(-2 H |sigma|) = 4 H^2 e^(-2 H |sigma|) - 4 H delta_D(sigma),
     whose delta function is the origin of the thin source of property 3. Every function of UM-3 that depends on sigma
     through |sigma| is folded at sigma = 0: the metric functions of FD-4 and the profiles of the bound states of
     dirac16complex (example 7).
  5. A fold map. In the mathematics of smooth maps the fold (Whitney's fold singularity) is the map u -> u^2 of a line onto
     a half-line: it folds the line at u = 0, two points +u and -u land on the same point, and the derivative of the map
     vanishes on the fold. Near the fold the map from the author's coordinate x0 to the distance |sigma| from the fold is
     of this kind (FD-6), and g_x0x0 = cot(z)^2, the square of the derivative d sigma/d x0, vanishes there.
  6. The brane of Randall and Sundrum. The five-dimensional metric
        (FD-8)  dy_RS^2 + e^(-2 k_RS |y_RS|) (dx1^2 + dx2^2 + dx3^2 - dx4^2),
                lambda_RS = 6 k_RS/kappa_5,   Lambda_RS = -6 k_RS^2/kappa_5
     (y_RS the proper coordinate across the brane, k_RS the inverse curvature length of the bulk, kappa_5 = 8 pi G_5) has a
     fold at y_RS = 0 with the properties 1 to 3 (its coordinate y_RS is already the proper distance, so property 4 does
     not arise); Einstein's equations require there a brane of the tension lambda_RS (Israel's junction condition) and in
     the bulk the vacuum energy Lambda_RS. The fold of UM-3 is of the same kind; it differs in that the time x4 is not
     warped, three extra times are warped together with ordinary space, and the Lovelock terms add to the junction
     conditions.
  7. A particle bound to a thin layer. A particle held by an attractive thin layer has a folded wave function: it falls
     off exponentially with the distance on both sides, and the layer makes its derivative jump (for the first-order
     Dirac equation, the wave function itself). In UM-3 the particles chi of dark matter are the states of dirac16complex
     bound to the fold; at rest and without their self-interaction (the field is
     Psi = e^(3 H |sigma|) chi(sigma) e^(-i omega_b x4))
        (FD-9)  chi(sigma) = e^(-q_b |sigma|) chi(0+) (sigma > 0),   chi(sigma) = e^(-q_b |sigma|) chi(0-) (sigma < 0),
                chi(0+) = exp( gamma^(0) (mu_L P_L + mu_R P_R) ) chi(0-),   omega_b = sqrt(m_Psi^2 - q_b^2),
     where mu_L, mu_R are the strengths of the fold for the left- and right-handed halves of dirac16complex (set by the
     Standard-Model fields on the fold), gamma^(0) = T^0 the Dirac matrix along sigma, P_L, P_R the chiral projectors,
     m_Psi the bulk mass, and q_b = -m_Psi (mu_L + mu_R) tanh(s)/(2 s), s = sqrt(mu_L mu_R) (q_b = -m_Psi mu_L/2 for
     mu_R = 0).
  8. The fold as a mirror for dirac16complex. The reflection across the fold acts on the profiles chi(sigma) in two ways,
        (FD-10)  (R_1 chi)(sigma) = T_0 T_1 T_2 T_3 chi(-sigma),   (R_2 chi)(sigma) = T_0 T_5 T_6 T_7 chi(-sigma)
     (T_a the author's Dirac matrices; for states at rest R_1 is the reflection across the fold combined with the
     reflection of ordinary space, R_2 the reflection across the fold combined with the reflection of the extra times).
     The Krein charge of a state is its share of the conserved charge of dirac16complex, which is indefinite: a state can
     carry the charge -1 or +1. R_1 is a symmetry of dirac16complex, of gravity and of the mean field of a gas of the
     particles chi: the four bound states of Krein charge -1 (the particles chi) are even under it and the four of Krein
     charge +1 are odd, so the mean field of the gas cannot mix the two signs of the indefinite charge. R_2 maps the bound
     states of one Krein charge onto those of the other and makes the two sets degenerate without the self-interaction.
  9. The planes of Horava and Witten. In M-theory on an interval (a circle whose points are identified with their mirror
     images), the two ten-dimensional planes left in place by the reflection are mirror surfaces (property 1); the gauge
     fields E8 x E8 live on them while gravity fills the bulk. This is the arrangement of UM-3, where the Standard Model
     lives on the fold and gravity and dirac16complex fill the bulk.

What is not a fold.
  * The tips z = 0 and z = pi (mod pi): the mirror exchanges them within a period, but there the warp vanishes, g_x0x0
    diverges, and they lie at an infinite proper distance; they carry no thin source.
  * A smooth maximum of a warp, such as 1/cosh(H sigma)^2: mirror symmetric and largest at sigma = 0, but without a kink
    and without a thin source.
END FOLD DEFINITION
"""
from __future__ import annotations

import json
import math
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import hankel1

HERE = Path(__file__).resolve().parent
UM3 = HERE.parent

M_PL_RED = 2.435e18          # the reduced Planck mass (GeV)
R_MAX = 0.036                # BICEP/Keck 2021 (95 %)
A_S = 2.1e-9                 # Planck 2018
NS = 0.9649                  # Planck 2018 (TT,TE,EE+lowE+lensing)
EULER_GAMMA = 0.5772156649015329


class Report:
    def __init__(self):
        self.checks = []

    def check(self, name, ok, detail=''):
        ok = bool(ok)
        self.checks.append({'name': name, 'passed': ok, 'detail': detail})
        print(('PASS ' if ok else 'FAIL ') + name + (': ' + detail if detail else ''), flush=True)
        return ok


def fold_definition():
    """The definition of the fold, word for word as in the docstring of this module (written into its JSON files)."""
    d = __doc__
    return d[d.index('BEGIN FOLD DEFINITION') + len('BEGIN FOLD DEFINITION'):d.index('END FOLD DEFINITION')].strip('\n')


def main():
    t0 = time.time()
    rep = Report()
    out = {}

    # ---------------- PR1
    x4, H, b0, Vt, Vs = sp.symbols('x4 H b0 V_t V_s', positive=True)
    a4 = H * x4
    b4 = b0
    sqrth = sp.exp(3 * a4)
    Z = Vt * (sp.exp(-a4) * b4) ** 3 / Vs
    prod = sp.simplify(sqrth * Z)
    out['PR1'] = {'sqrt(-h) Z': str(prod)}
    rep.check('PR1_no_friction', sp.diff(prod, x4) == 0,
              'author\'s vacuum a4 = H x4, b4 = b0: sqrt(-h) Z = %s, constant: the mode equation of a field of the fold has '
              'no friction term' % prod)

    # ---------------- PR2: the spectrum
    Hn = 1.0
    x4_end = 12.0                    # late time, H x4 = 12: k tau = k e^{-12}
    ks = np.array([1e3, 2e3, 4e3, 8e3, 1.6e4]) * math.exp(-0.0)
    rows = []
    for k in ks:
        # start at k tau_start = 400 (deep inside the horizon), the WKB vacuum phi = sqrt(pi/(4H)) H_0^(1)(k tau)
        tau0 = 400.0 / k
        x0 = -math.log(Hn * tau0) / Hn
        z0 = k * tau0
        ph0 = math.sqrt(math.pi / (4 * Hn)) * hankel1(0, z0)
        # d phi/dx4 = d phi/d tau * d tau/dx4 = -k H_0^(1)'(k tau) * (H tau) * norm = k H_1^(1)(k tau) H tau norm
        dph0 = math.sqrt(math.pi / (4 * Hn)) * k * hankel1(1, z0) * Hn * tau0

        def rhs(x, y):
            om2 = k * k * math.exp(-2 * Hn * x)
            return [y[2], y[3], -om2 * y[0], -om2 * y[1]]
        sol = solve_ivp(rhs, (x0, x4_end), [ph0.real, ph0.imag, dph0.real, dph0.imag], rtol=1e-10, atol=1e-13,
                        method='DOP853')
        phi = complex(sol.y[0, -1], sol.y[1, -1])
        tau = math.exp(-Hn * x4_end) / Hn
        exact = math.sqrt(math.pi / (4 * Hn)) * hankel1(0, k * tau)
        late = (math.pi / (4 * Hn)) * (1 + 4 / math.pi ** 2 * (math.log(k * tau / 2) + EULER_GAMMA) ** 2)
        rows.append({'k': float(k), 'k_tau_end': k * tau, 'abs2_numerical': abs(phi) ** 2, 'abs2_hankel': abs(exact) ** 2,
                     'abs2_late_formula': late, 'P': k ** 3 * abs(phi) ** 2 / (2 * math.pi ** 2)})
    lnk = np.log([r['k'] for r in rows])
    lnP = np.log([r['P'] for r in rows])
    n_minus_1 = float(np.polyfit(lnk, lnP, 1)[0])
    out['PR2'] = {'rows': rows, 'n_minus_1': n_minus_1, 'Planck_ns_minus_1': NS - 1}
    rep.check('PR2_spectrum', all(abs(r['abs2_numerical'] - r['abs2_hankel']) < 1e-6 * r['abs2_hankel'] for r in rows)
              and all(abs(r['abs2_late_formula'] - r['abs2_hankel']) < 0.02 * r['abs2_hankel'] for r in rows)
              and 2.5 < n_minus_1 < 3.0,
              'the mode equation integrated from the early-time vacuum agrees with sqrt(pi/(4H)) H_0^(1)(k tau) (relative '
              'difference below 1e-6) and at k tau = %.1e ... %.1e with the late-time formula; the spectrum k^3 |phi_k|^2/'
              '(2 pi^2) has the index n - 1 = %.3f (3 less a logarithmic correction), against n_s - 1 = %.4f observed' % (
                  rows[0]['k_tau_end'], rows[-1]['k_tau_end'], n_minus_1, NS - 1))

    # ---------------- PR3: the gauge couplings
    g = sp.symbols('g', positive=True)
    geff2 = sp.simplify(g ** 2 / Z * Vt * b0 ** 3 / Vs)     # normalised to g^2 at x4 = 0
    rate = sp.simplify(sp.diff(sp.log(geff2), x4))
    out['PR3'] = {'g_eff^2 / g^2 (normalised at x4 = 0)': str(sp.simplify(geff2 / g ** 2)), 'd ln g_eff^2/d x4': str(rate)}
    rep.check('PR3_couplings_grow', sp.simplify(rate - 3 * H) == 0,
              'the gauge action carries Z/g^2: g_eff^2 = g^2/Z grows like %s (d ln g_eff^2/dx4 = %s): the couplings of the '
              'fold grow like e^{3 H x4/2} in the author\'s vacuum' % (sp.simplify(geff2 / g ** 2), rate))

    # ---------------- PR4: the tensor bound
    Hinf = math.pi * M_PL_RED * math.sqrt(R_MAX * A_S / 2)
    out['PR4'] = {'H_inf_max_GeV': Hinf, 'r_max': R_MAX, 'A_s': A_S}
    rep.check('PR4_tensor_bound', 4.0e13 < Hinf < 5.5e13,
              'the observed spectrum (n_s - 1 = %.4f) cannot come from the author\'s vacuum (n - 1 close to 3, PR2): it needs '
              'an era with frozen extra times and nearly exponential expansion, whose Hubble rate is limited by r < %.3f '
              '(A_s = %.1e) to H_inf < pi M_Pl,red sqrt(r A_s/2) = %.2e GeV' % (NS - 1, R_MAX, A_S, Hinf))

    # ---------------- PR5: Higgs inflation against Sakharov induced gravity
    N = 55
    rows5 = []
    for lam in (0.13, 0.01):
        xi = N * math.sqrt(lam / (72 * math.pi ** 2 * A_S))
        rows5.append({'lambda': lam, 'xi_H_needed': xi, 'sakharov_N_eff': 4 * (1 - 6 * xi)})
    out['PR5'] = {'rows': rows5, 'sakharov_requires': 'xi_H < 1/6'}
    rep.check('PR5_higgs_inflation', all(r['xi_H_needed'] > 1e3 and r['sakharov_N_eff'] < 0 for r in rows5),
              'Higgs inflation needs xi_H = N sqrt(lambda/(72 pi^2 A_s)) = %s (lambda = 0.13 and 0.01 at the inflationary '
              'scale, N = 55); the induced gravity of the fold from the loops of its fields has 1/(16 pi G) proportional to '
              'N_eff = 4(1 - 6 xi_H), positive only for xi_H < 1/6 (N_eff = %s here): UM-3 has no inflaton, and its Higgs '
              'field cannot be one if the Einstein-Hilbert term of the fold is induced' % (
                  ['%.0f' % r['xi_H_needed'] for r in rows5], ['%.0f' % r['sakharov_N_eff'] for r in rows5]))

    out['runtime_s'] = round(time.time() - t0, 1)
    out['definition_of_the_fold'] = fold_definition()
    (UM3 / 'outputs' / 'primordial.json').write_text(json.dumps(out, indent=1, sort_keys=True, default=str) + '\n')
    report = {'script': 'universe_model_3/code/um3_primordial.py', 'checks': rep.checks,
              'passed': sum(c['passed'] for c in rep.checks), 'total': len(rep.checks),
              'all_passed': all(c['passed'] for c in rep.checks)}
    report['definition_of_the_fold'] = fold_definition()
    (UM3 / 'reports' / 'primordial_checks.json').write_text(json.dumps(report, indent=1) + '\n')
    print('%d/%d checks passed in %.1f s' % (report['passed'], report['total'], time.time() - t0))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
