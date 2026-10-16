# Hypothesis00: dirac16complex00 and a time-varying dark-sector equation of state (Revision record)

This folder investigates Hypothesis00 of `Revision/SPEC.md` section 8 for the semi-classical field
dirac16complex00: 16 commuting complex components that transform as a Pin(4,4) spinor, with the Lagrangian and
energy-momentum tensor of `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`.

**The metric** is the author's of `Dirac_Einstein-Lovelock_4+4_Nash.nb` (In[48]: `X = {x0[], ..., x7[]}`;
In[97]-In[102]): g = diag(cot^2 z, e^{2 a4} sin^{1/3} z (x1, x2, x3), -1, -e^{-2 a4} b4 sin^{1/3} z (x5, x6, x7)),
z = 6 H x0. The three extra times x5, x6, x7 deflate exponentially, with the scale factor e^{-a4} b4^{1/2}.
**b4 is a function of x4 (never 1).** The record before 2026-10-14 used b4 = 1; it is withdrawn and quoted below
only as "withdrawn" for comparison.

**The history of the numbers** is a4 = H x4 and **b4(x4) = b4(0) e^{(4/3) H x4}** (beta = d ln b4/d a4 = 4/3, so
b4 ~ a^{4/3} and the extra-time scale factor goes like a^{-1/3}): with the author's weights (w1 = 1, w2 = 1/32,
w3 = 1/1152) this is the branch that the mixed (x4, x0) field equation allows for a source without T^x4_x0
(`Revision/dark_sector/dirac16complex/derive/derive_effective.py`, check `author_weights_b4_branch`). Every formula
is derived for general a4(x4), b4(x4).

The questions are what equation of state a 3-space observer infers, whether it varies in time, and how it
compares with the author's Supernovae Unite values: the constant-w fit w = -0.764, and the CPL fit
w(a) = w0 + wa (1 - a) with (w0, wa) = (-0.861, -0.60). Phantom crossing and the ghost-like sector are part
of the question.

Every number below comes from the two outputs of this folder: `eos-theory.json` (implementation A) and
`results/independent-numerics.json` (implementation B). The checks are in `reports/`. Nothing here is taken
from the earlier stages of the repository.

Labels: **EXACT** means verified by exact symbolic computation in a named check. **APPROXIMATION**,
**ASSUMPTION** and **INTERPRETATION** are marked where they apply.

## 1. Method

**Conservation (EXACT; re-derived from the metric with b4).** For a diagonal T(x4, x0):

- nabla_mu T^mu_x4 = -d4 rho - a4' (p1 + p2 + p3 - p5 - p6 - p7) - (b4'/(2 b4)) (3 rho + p5 + p6 + p7)
- nabla_mu T^mu_x0 = d0 p0 + H cot z sum_dir (p0 - p_dir) (no b4)

Every other component vanishes identically. For an isotropic, x0-independent source this gives
d rho/dx4 = -3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t) and p3 + p_t = 2 p0. The local model (warp frozen) has the
same x4 identity and sqrt|g| = b4^{3/2}. Checks: `conservation_*`, `local_model_volume_b4`, with a negative control
(the b4-free form of the withdrawn record fails).

**The observer (ASSUMPTION, stated with its alternatives).** a = e^{a4} is the 3-space scale factor. The
3-space observer averages over the hidden direction with the weight cos z (the proper weight is b4^{3/2} cos z;
its b4 factor is written out below). The extra times are time-like:

- a compact coordinate range for them means closed time-like directions;
- a non-compact range needs a normalisation.

Two normalisations are used:

- **N1, per unit extra-time coordinate volume:** rho_4 = e^{-3 a4} b4^{3/2} <rho>. This is SPEC section 11's
  rho_4 ~ rho_8 c^3 with c = e^{-a4} b4^{1/2}.
- **N2, per unit proper 7-volume:** rho_4 = <rho>.

Then, with beta = d ln b4/d a4:

- w_eff = -1 - (1/3) d ln rho_4 / d ln a;
- with the exact conservation identity, **w_eff(N1) = w3 - w_t + (beta/2) w_t** and
  **w_eff(N2) = w_eff(N1) - 1 + beta/2** (EXACT, checks `observer_*_b4`); on the history: w_eff(N2) = w_eff(N1) - 1/3;
- the ratio **w = p3/rho** does not depend on the normalisation.

INTERPRETATION: supernova distances measure the dilution-inferred w_eff of a 4-dimensional Friedmann
observer. It agrees with p3/rho only when no energy is exchanged with the extra times.

**Classical solutions used:**

1. The homogeneous condensate, an exact solution for every a4 and b4.
2. Plane-wave modes in the frozen local frame, exact for the local model. For both, the Krein-signed energies
   and the growing modes are computed exactly with the author's T16.
3. Adiabatic (WKB) gases of such modes in the deflating local model. This is an APPROXIMATION: the warp
   sin^{1/6} z and tan z are frozen at a fixed hidden position (wavelengths short compared with 1/H), the
   adiabatic invariance of each mode's Krein charge per coordinate volume is assumed, and the superposition is
   incoherent. The B-run of the full 16-component equation measures how well this holds (section 3).
4. Superpositions and wave packets. Their averaged energy-momentum is the sum of the mode contributions
   (`B_superposition_average`).

## 2. Exact results

**Condensate.** Checks `condensate_*`.

- In the metric with b4 the homogeneous equation is d4 Phi = A Phi with A = -gamma^(x4) (M - 3 H gamma^(x0))
  - (3/4)(b4'/b4): C A + A^T C = -(3/2)(b4'/b4) C, so **b4^{3/2} S is constant** (S = S0 b4^{-3/2}); K_x4 = M S.
- rho = m S + lambda S^2/2 and p3 = p_t = p0 = lambda S^2/2. The ratio w = lambda S/(2 m + lambda S) **drifts**:
  d w/d a4 = -3 beta m lambda S/(2 m + lambda S)^2 (lambda S/m ~ e^{-2 a4} on the history).
- Normalisation dependence: w_eff(N1) = (beta/2) w = (2/3) w and w_eff(N2) = -1 + (beta/2)(1 + w) = -1/3 + (2/3) w.
- The ratio equals the Unite constant w = -0.764 at lambda S/m = **-382/441** at one instant. With rho > 0 this needs
  m S > 0 and lambda < 0. Then its wa is -2.695 (thawing sign).
- The ratio is phantom exactly for lambda S/m in (-2, -1), at an instant.
- **The source the author's equations require on the history** (check `branch_required_source`; the field equations
  of `Revision/field_equations_a4/a4-equations.json`, key b4, with the author's weights, which first reproduce the
  author's vacuum, check `author_weights_vacuum_recovered`): kappa T^x4_x0 = 0 and the constant diagonal source
  **kappa (rho, p3, p_t, p0) = (-2/27, -2/9, -22/27, -14/27)**, which satisfies both conservation identities with b4.
  A condensate decays like b4^{-3/2} and is therefore not this source (check `condensate_cannot_source_branch`); in
  Einstein gravity a b4(x4) needs T^x4_x0 != 0, which a condensate does not have.
- The observer's expansion-inferred w_exp = -1 - (2/3) a4''/a4'^2 is -1 exactly on a4 = H x4, for every b4.

**Modes and the Krein-signed classical energy.** Checks `mode_*` and `growing_*` (frozen frame, physical momenta).

- For a plane wave with 3-momentum k and extra-time momentum q, omega^2 = m^2 + k^2 - q^2. The extra times
  are time-like, so q enters with the opposite sign.
- Every real-frequency eigenspace is 8-dimensional, with Krein form of signature (4, 4). This is exact for the
  three test cases; the general statement is the Krein-inertia theorem of `Revision/pairing`.
- On it, T^mu_nu = k^mu k_nu Q/omega exactly, so rho = omega Q. **At every real frequency there are modes of
  both energy signs.** B confirms this: rho = +1.25 and -1.25 at omega = 1.25.
- For q^2 > m^2 + k^2 the modes grow. They are Krein-neutral, with rho = 0 but a growing extra-time pressure
  p5 = -m S.
- In the deflating field q_phys = q a b4^{-1/2} grows (like a^{1/3} on the history). Every mode with q != 0 therefore
  reaches a turning point a_* and then grows; the deflation drives the growth.

**Gases (EXACT within the WKB model).** Checks `wkb_*_b4` and `mixture_*_b4`.

- Each component has rho_i = omega_i Q_i b4^{-3/2} and eps_i = w_eff(N1)_i = (k_p^2 + (1 - beta/2) q_p^2)/(3 omega^2)
  >= 0 for beta < 2, independent of the sign of Q.
- For mixtures, w_eff(N1) = sum eps_i rho_i / sum rho_i and w_eff(N2) = w_eff(N1) - 1 + beta/2.
- **Theorem:** if every component has rho_i >= 0, with real frequencies, then w_eff(N1) >= 0 and
  **w_eff(N2) >= -1 + beta/2 = -1/3** on the history, at every a at which these conditions hold. There is then no
  phantom, no crossing of -1 and no w_eff(N2) below -1/3. A mode with extra-time momentum loses its real frequency
  past its turning point a_*, where the theorem does not apply.
- Going below -1/3 needs a component with **negative classical energy**.

## 3. Models, CPL tangents and fits

The models keep the physical parameters of the withdrawn b4 = 1 record, so that the effect of b4(x4) is seen
directly. Each model is normalised to rho_tot = 1 at a = 1. The tangent is w0 = w(1), wa = -w'(1). The fits are
least squares over 101 uniform points in a ∈ [1/2, 1] (z ≤ 1) and [1/3, 1] (z ≤ 2). The "constant w" column is the
mean of w(a), a PROXY. Applied to the Unite CPL line itself, the proxy gives -1.011 on [1/2, 1]
(`unite_line_fit_proxy`). The Unite line crosses -1 at a = 461/600 = 0.768.

| model (positive energy unless stated) | definition | tangent (w0, wa) | fit [1/2, 1] (w0, wa; const) | crosses -1? |
| --- | --- | --- | --- | --- |
| M1 condensate | ratio / N1 / N2 | (w, 4u/(2+u)^2) / (2/3)(w, 4u/(2+u)^2) / (-1/3 + (2/3) w, (2/3) 4u/(2+u)^2) | drifts | no |
| M2 good-sector gas (q = 0), k^2/(k^2+m^2) = 0.417 at a = 1 | N2 | (-583/3000, **+0.162074**): freezing | (-0.1988, 0.2173; -0.1445) | no |
| M2 | N1 = ratio | (0.139, 0.162074): 1/3 → 0, **dark-matter-like** | (0.1345, 0.2173; 0.1888) | no |
| M3 extra-time mode (k = 0), q_p^2/m^2 = 417/1417 | N2 | (-0.287, **-0.0437696**): thawing sign, w ≥ -1/3 for a < a_* | (-0.2871, -0.0420; -0.2976) | no |
| M4 condensate + extra-time mode, s = 264037/403037, Omega_q = 57963/264037 | N2 | (-0.287, -0.0667) | (-0.2882, -0.0502; -0.3007) | no |
| M5 = M4-type + **ghost** (negative-energy massless modes, G = 0.3 of the total at a = 1) | N2 | (-0.3465, -0.1964) | (-0.3327, -0.3231; -0.4135) | no |

Notes on the table:

- **M3:** omega^2 = m^2 (1 - s a^{2/3}); the turning point is at a_* = s^{-3/2} = (1417/417)^{3/2} = 6.264 (withdrawn
  b4 = 1: 1.843 and the tangent (-0.861, -0.393926)).
- **M4:** the parameters of the withdrawn tuning that gave the Unite tangent exactly; on the history its N2 tangent is
  (-0.287, -0.0667), min of w_eff(N2) over a = 1/300 ... 1 = -0.3328 ≥ -1/3; a_* = 1.886.
- **M5:** the composition and parameters of the withdrawn record (G = 3/10, s = 0.5678, Omega_q = 0.5947); on the
  history it does not cross -1 in [1/3, 1] (withdrawn: crossing at a = 0.779); a_* = 2.337.
- **The Unite w0 needs a dominant ghost** (check `unite_w0_requires_dominant_ghost`): w_eff(N2)(1) ≥ -1/3 - G/3,
  so -0.861 needs a ghost fraction G ≥ **1583/1000**; for condensate + ghost the total energy then vanishes at
  a = G/(1 + G) = 1583/2583 = 0.613, inside [1/2, 1], where w_eff diverges.

**Independent second implementation (B).** B integrates the 16-component field equation of the local model with
the author's T16, including the b4 term (3/4)(b4'/b4) gamma^(x4), which it integrates exactly, and the
blueshift q e^{a4} b4^{-1/2}. It uses the exact Krein-preserving exponential midpoint step, with H/m = 10^-3
(adiabatic). Along every run it checks numerically that:

- the Krein charge per coordinate volume b4^{3/2} Q is conserved (drift ≤ 1.3e-13);
- the solution is on shell (|L0| ≤ 1.4e-15);
- the conservation identity with the b4 term holds;
- the condensate dilutes with b4^{3/2} (b4^{3/2} rho constant to 1.3e-13).

It then rebuilds M2 to M5 from the solutions. All tangents, fits and constant proxies agree with A to within
2.3e-5 (`B_vs_A_*`). It also measures w_eff(N2) **directly from the dilution of the proper density** of the
solutions; that agrees with the formula w_eff(N1) - 1 + beta/2 to within 4.0e-5 (`B_dilution_equals_formula_*`).
From the field-equation solutions, the positive models have w_eff(N2) ≥ -0.318 on a ∈ [0.35, 1]
(`B_positive_models_bounded`); M5 has no crossing of -1.

B solves M3 by bisection on the field-equation solutions: w_eff(N2)(1) = -0.287 at s = 0.294292 (A: 0.294284).

Past the turning point a_* = 6.264, the M3 mode grows at d ln|phi|/dx4 = 0.3089 against the WKB rate
sqrt(s a^{2/3} - 1) - (3/4) b4'/b4 = 0.3117. Its amplitude grows by 10^16.2 between a = 5.5 and 7.4, and its energy
density becomes large and negative (rho/Q = -4.3e29 at a = 7.4, for H/m = 10^-3).

## 4. Verdict for Hypothesis00 on the metric with b4(x4)

1. **Dark matter.** A positive-energy gas of good-sector modes gives, under N1 and in the ratio p3/rho, a
   time-varying equation of state from 1/3 (relativistic) to 0 (dust) (M2), independent of b4. A lambda = 0
   condensate is dust-like under N1.
2. **No dark energy without ghosts.** On the history b4 ~ a^{4/3} every positive-energy model has
   w_eff(N2) ≥ -1/3 (theorem of section 2; M2: -0.194, M3 and M4: -0.287 today). The thawing slope of the extra-time
   mode is small (M3: -0.0437696) because q_p grows only like a^{1/3}.
3. **The Unite values.** Reaching w0 = -0.861 under N2 needs a ghost-like component with G ≥ 1583/1000 of the total
   energy at a = 1 (the total energy of condensate + ghost then vanishes inside the fit range). The only negative
   values without a ghost come from a condensate with lambda < 0, whose ratio drifts strongly (wa = -2.695 at the
   ratio -0.764).
4. **The source of the history.** The author's equations need the constant source kappa (rho, p3, p_t, p0) =
   (-2/27, -2/9, -22/27, -14/27) on this history (a negative energy density for kappa > 0); a condensate is not it.
5. **Expansion-inferred w.** On a4 = H x4 the 3-space Hubble rate is constant, so w_exp = -1 exactly, for every b4.

## 5. What is not claimed

- No supernova likelihood: there are no covariances and no distance fits; the "fits" are least squares of
  w(a).
- The models M2 to M5 are illustrative members with stated parameters (those of the withdrawn record). They are not
  predictions, and nothing selects their populations.
- The WKB/local model freezes the hidden-direction warp. The test-field results are not backreacted.
- The history b4 = b4(0) e^{(4/3) H x4} is allowed by the mixed equation of the author's weights; the source it needs
  is computed but not constructed from the fields of this record.
- The growing modes make the Cauchy problem ill-posed (`Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`
  section 7). Nothing here cures that.
- Nothing here establishes that dirac16complex00 *is* dark energy or dark matter.

## 6. Reproduction

From the repository root:

```text
python Revision/dark_sector/dirac16complex00/python/derive_eos.py            # A: 49 checks, about 4 s
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py  # B: 32 checks, about 7 s (reads A's eos-theory.json for the comparison)
python -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
```

Both scripts accept `--out DIR`. Two runs give byte-identical outputs, and the test re-runs both and compares
them byte for byte.

Inputs (Revision outputs only):

- `Revision/algebra/gammas.json` (the author's T16);
- `Revision/field_equations_a4/a4-equations.json` (key b4: the field equations of the metric with b4).
