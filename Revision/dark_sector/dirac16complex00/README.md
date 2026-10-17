# Hypothesis00: dirac16complex00 and a time-varying dark-sector equation of state (Revision record)

This folder investigates Hypothesis00 of `Revision/SPEC.md` section 8 for the semi-classical field
dirac16complex00: 16 commuting complex components that transform as a Pin(4,4) spinor, with the Lagrangian and
energy-momentum tensor of `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`.

**The metric** is the corrected primordial metric of 2026-10-16 (version 2; `Revision/SPEC.md` section 1), in the
author's coordinates X = {x0, x1, ..., x7}:
g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x1, x2, x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x5, x6, x7)), z = 6 H x0
real (every real z; (sin^2 z)^{1/6} on the positive branch). x0 is the hidden space-like direction, x4 the time, and the
three extra times x5, x6, x7 deflate exponentially with the scale factor e^{-a4} b4^{1/2} (sin^2 z)^{1/12}; the hidden
direction carries the same factor e^{-a4} b4^{1/2}. **b4 is a function of x4.** Every formula is derived for general
a4(x4), b4(x4).

**The history of the numbers** is the record's a4 = H x4 and b4 = e^{(4/3) H x4} (beta = d ln b4/d a4 = 4/3, so the
extra-time scale factor goes like a^{-1/3}). It is a PRESCRIBED background: with the author's weights (w1 = 1,
w2 = 1/32, w3 = 1/1152) the field equations need on it the source of `a4-equations.json`
exponentialHistory.authorWeights (section 2), which no field of this record supplies.

The questions are what equation of state a 3-space observer infers, whether it varies in time, and how it compares
with the author's Supernovae Unite values: the constant-w fit w = -0.764, and the CPL fit w(a) = w0 + wa (1 - a)
with (w0, wa) = (-0.861, -0.60). Phantom crossing and the ghost-like sector are part of the question.

Every number below comes from the two outputs of this folder: `eos-theory.json` (implementation A) and
`results/independent-numerics.json` (implementation B). The checks are in `reports/`. The results of the metric of
2026-10-14 (the b4 record with sin^{1/3} z factors on 3-space) are withdrawn; their numbers are not quoted here.

Labels: **EXACT** means verified by exact symbolic computation in a named check. **APPROXIMATION**,
**ASSUMPTION** and **INTERPRETATION** are marked where they apply.

## 1. Method

**Conservation (EXACT; re-derived from the corrected metric, own Christoffel symbols).** For a diagonal T(x4, x0):

- nabla_mu T^mu_x4 = -d4 rho - a4' (3 rho + p1 + p2 + p3) - h4 (4 rho + p0 + p5 + p6 + p7), with h4 = b4'/(2 b4) - a4'
  the rate of the block (x0, x5, x6, x7);
- nabla_mu T^mu_x0 = d0 p0 + H cot z sum_t (p0 - p_t), i.e. p0_y + 3 H (p0 - p_t) = 0 in y = ln|sin z|/(6H).

Every other component vanishes identically. For an isotropic, x0-independent source: d rho/dx4 = -3 a4' (rho + p3)
- 4 h4 (rho + p0) and p0 = p_t. The local model (warp frozen) has sqrt|g| = e^{-a4} b4^2. Checks: `conservation_*`.

**The observer (ASSUMPTION, stated with its alternatives).** a = e^{a4} is the 3-space scale factor; the extra times
are time-like, so a compact coordinate range for them means closed time-like directions and a non-compact range needs a
normalisation. Two normalisations are used:

- **N1, per unit coordinate volume of the extra times and the hidden direction:** rho_4 = e^{-4 a4} b4^2 <rho>;
- **N2, per unit proper 7-volume:** rho_4 = <rho>/<1>.

Then, with beta = d ln b4/d a4 (EXACT, checks `observer_*`):

- w_eff = -1 - (1/3) d ln rho_4 / d ln a;
- **w_eff(N1) = w3 + (beta/2 - 1)(w0 + 3 w_t)/3** (isotropic) and **w_eff(N2) = w_eff(N1) - (4 - 2 beta)/3**, which is
  w_eff(N1) - 4/9 on the history (the metric of 2026-10-14 had -1/3);
- the ratio **w = p3/rho** does not depend on the normalisation.

INTERPRETATION: supernova distances measure the dilution-inferred w_eff of a 4-dimensional Friedmann observer. It
agrees with p3/rho only when no energy is exchanged with the block.

**Classical solutions used:**

1. The homogeneous condensate, an exact solution for every a4 and b4 (the author's T16).
2. Plane-wave modes in the frozen local frame, exact for the local model, with the Krein-signed energies and the
   growing modes (the author's T16).
3. Adiabatic (WKB) gases of such modes in the deflating local model. This is an APPROXIMATION: the warp is frozen at
   a fixed hidden position (wavelengths short compared with 1/H), the Krein charge of each mode per coordinate volume is
   an adiabatic invariant, and the superposition is incoherent. Implementation B measures how well this holds.
4. Superpositions: their averaged energy-momentum is the sum of the mode contributions (`B_superposition_average`).

## 2. Exact results

**Condensate.** Checks `condensate_*`.

- In the corrected metric the condensate obeys **S = S0 e^{a4} b4^{-2}** (S Vol_7 constant, Vol_7 ~ e^{-a4} b4^2), with
  K_x4 = M S; on the history S ~ e^{-(5/3) a4}.
- rho = m S + lambda S^2/2 and p3 = p_t = p0 = lambda S^2/2. The ratio w = u/(2 + u), u = lambda S/m ~ e^{-(5/3) a4},
  **drifts**: its CPL slope is wa = (10/3) u/(2 + u)^2.
- Normalisation dependence: w_eff(N1) = ((2 beta - 1)/3) w = (5/9) w and w_eff(N2) = (5/9) w - 4/9.
- The ratio equals the Unite constant w = -0.764 at lambda S/m = **-382/441** at one instant. With rho > 0 this needs
  m S > 0 and lambda < 0; its wa is then -2.24616 (thawing sign).
- The ratio is phantom exactly while lambda S/m lies in (-2, -1) (`condensate_phantom_interval`), and the observer then
  reads w_eff(N2) = (5/9)(1 + w) - 1 < -1 as well. For -382/441 today, lambda S/m drifts into that window toward the
  past: from a = (382/441)^{3/5} = 0.917 back to a = (191/441)^{3/5} = 0.605, where the energy vanishes. The value is
  CHOSEN.
- **The source the author's equations require on the history** (`a4-equations.json` exponentialHistory.authorWeights,
  Lambda = -10 H^2; kk = e^{2a4}/b4 = e^{(2/3) H x4}): kappa T - Lambda delta has
  -rho = -9 kk^2/16 + 161 kk/24 + 121/432, p3 = -9 kk^2/16 + 1601 kk/216 - 5359/3888,
  p_t = p0 = 79 kk/16 - 497/144. It is anisotropic and grows; a condensate is isotropic and decays, so **no
  condensate is the source of the history** (`condensate_cannot_source_history`).
- The observer's expansion-inferred w_exp = -1 - (2/3) a4''/a4'^2 is -1 exactly on a4 = H x4, for every b4.

**Modes and the Krein-signed classical energy.** Checks `mode_*` and `growing_*` (frozen frame, physical momenta).

- For a plane wave with 3-momentum k and extra-time momentum q, omega^2 = m^2 + k^2 - q^2 (the extra times are
  time-like).
- Every real-frequency eigenspace is 8-dimensional, with Krein form of signature (4, 4). On it rho = omega Q exactly:
  **at every real frequency there are modes of both energy signs**. B confirms this: rho = +1.25 and -1.25 at
  omega = 1.25.
- For q^2 > m^2 + k^2 the modes grow. They are Krein-neutral, with rho = 0 and a growing extra-time pressure.
- In the deflating field the physical extra-time momentum grows like a^{1/3}. Every mode with q != 0 therefore reaches
  a turning point a_* and then grows: the deflation drives the growth.

**Gases (EXACT within the WKB model).** Checks `wkb_*` and `mixture_*`.

- Each component has rho_i = omega_i Q_i n, n = e^{a4} b4^{-2}, and eps_i = w_eff(N1)_i =
  (k_p^2 + (1 - beta/2) q_p^2)/(3 omega^2) >= 0 for beta < 2, independent of the sign of Q.
- For mixtures, w_eff(N1) = sum eps_i rho_i / sum rho_i and w_eff(N2) = w_eff(N1) - 4/9.
- **Theorem:** if every component has rho_i >= 0, with real frequencies, then w_eff(N1) >= 0 and
  **w_eff(N2) >= -4/9** on the history. There is then no phantom and no crossing of -1. A mode with extra-time momentum
  loses its real frequency past its turning point a_*, where the theorem does not apply.
- Going below -4/9 needs a component with **negative classical energy**.

## 3. Models, CPL tangents and fits

The models keep the physical parameters of the withdrawn records, so that the effect of the corrected metric is seen
directly. Each model is normalised to rho_tot = 1 at a = 1. The tangent is w0 = w(1), wa = -w'(1). The fits are least
squares over 101 uniform points in a in [1/2, 1] (z <= 1) and [1/3, 1] (z <= 2). The "constant w" is the mean of w(a),
a PROXY; applied to the Unite CPL line it gives -1.011 on [1/2, 1]. The Unite line crosses -1 at a = 461/600 = 0.768.

| model (positive energy unless stated) | normalisation | tangent (w0, wa) | fit [1/2, 1] (w0, wa; const) | crosses -1? |
| --- | --- | --- | --- | --- |
| M1 condensate | ratio / N1 / N2 | (u/(2+u), (10/3) u/(2+u)^2) / (5/9) of it / -4/9 + (5/9) of it | drifts | no |
| M2 good-sector gas (q = 0), k^2/(k^2+m^2) = 0.417 at a = 1 | N2 | (-2749/9000, **0.162074**): freezing | (-0.3099, 0.2173; -0.2556) | no |
| M2 | N1 = ratio | (0.139, 0.162074): 1/3 to 0, **dark-matter-like** | (0.1345, 0.2173; 0.1888) | no |
| M3 extra-time mode (k = 0), q_p^2/m^2 = 417/1417 | N2 | (-3583/9000, **-0.0437696**): thawing sign | (-0.3982, -0.0420; -0.4087) | no |
| M4 condensate + extra-time mode, s = 264037/403037, Omega_q = 57963/264037 | N2 | (-0.3981, -0.0667) | (-0.3993, -0.0502; -0.4118) | no |
| M5 = M4-type + **ghost** (negative-energy massless modes, G = 0.3 of the total at a = 1) | N2 | (-0.4577, -0.1964) | (-0.4438, -0.3231; -0.5246) | no |

Notes on the table:

- **M3:** omega^2 = m^2 (1 - s a^{2/3}), w_eff(N2) = -4/9 + (1/9) s a^{2/3}/(1 - s a^{2/3}); the turning point is at
  a_* = s^{-3/2} = 6.264.
- **M4:** min of w_eff(N2) over (0, 1] = -0.4439 >= -4/9; a_* = 1.886.
- **M5:** the composition of the withdrawn record (G = 3/10); it does not cross -1 in [1/3, 1]; a_* = 2.337.
- **The Unite w0 needs a dominant ghost** (check `unite_w0_requires_dominant_ghost`): w_eff(N2)(1) >= -4/9 - G/3, so
  -0.861 needs a ghost fraction G >= **3749/3000** of the total energy at a = 1.

**Independent second implementation (B).** B integrates the 16-component field equation of the local model with the
author's T16 in the corrected metric (the term (b4'/b4 - a4'/2) of the spin connection integrated exactly, the
blueshift of the extra-time momentum), with the exact Krein-preserving exponential midpoint step and H/m = 10^-3
(adiabatic). Along every run it checks numerically that:

- the Krein charge per coordinate volume e^{-a4} b4^2 Q is conserved (drift <= 1e-13);
- the solution is on shell (|L0| <= 1.3e-15);
- the conservation identity with h4 holds;
- the condensate dilutes with e^{-a4} b4^2 rho constant (to 1e-13).

It then rebuilds M2 to M5 from the solutions: every tangent, fit and constant proxy agrees with A (`B_vs_A_*`), and
w_eff(N2) measured directly from the dilution of the proper density agrees with the formula w_eff(N1) - 4/9 to within
3e-5 (`B_dilution_equals_formula_*`). The positive models have w_eff(N2) >= -0.4293 on a in [0.35, 1]
(`B_positive_models_bounded`); M5 has no crossing of -1. B solves M3 by bisection: s = 0.294289 (A: 417/1417 =
0.294284). Past a_* the M3 mode grows at d ln|phi|/dx4 = 0.3091 against the WKB rate 0.3118; its amplitude grows by
10^16.2 between a = 5.5 and 7.4, and its energy density becomes large and negative.

## 4. Verdict for Hypothesis00 in the corrected metric

1. **Dark matter.** A positive-energy gas of good-sector modes gives, under N1 and in the ratio p3/rho, a time-varying
   equation of state from 1/3 (relativistic) to 0 (dust) (M2), independent of b4.
2. **No dark energy from positive-energy mode gases.** On the history every positive-energy model has w_eff(N2) >= -4/9
   (theorem of section 2; M2: -0.305, M3 and M4: -0.398 today).
3. **The Unite values.** Reaching w0 = -0.861 under N2 needs a ghost-like component with G >= 3749/3000 of the total
   energy at a = 1. The only negative values without a ghost come from a condensate with lambda < 0 (positive energy for
   m S > 0), whose ratio drifts strongly (wa = -2.24616 at the ratio -0.764) and which reads w_eff(N2) < -1 while
   lambda S/m lies in (-2, -1); its value is CHOSEN.
4. **The source of the history.** The author's equations need the anisotropic, growing source of section 2 on this
   history; a condensate is not it.
5. **Expansion-inferred w.** On a4 = H x4 the 3-space Hubble rate is constant, so w_exp = -1 exactly, for every b4.

## 5. What is not claimed

- No supernova likelihood: there are no covariances and no distance fits; the "fits" are least squares of w(a).
- The models M2 to M5 are illustrative members with stated parameters. They are not predictions, and nothing selects
  their populations.
- The WKB/local model freezes the hidden-direction warp and drops the hidden momentum (the bulk-band effect of the
  Kohn-Sham record, which lowers w_eff, is not in these gases). The test-field results are not backreacted.
- The growing modes make the Cauchy problem ill-posed (`Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY` section 7).
- Nothing here establishes that dirac16complex00 *is* dark energy or dark matter.

## 6. Reproduction

From the repository root:

```text
python Revision/dark_sector/dirac16complex00/python/derive_eos.py            # A: 48 checks, about 2 s
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py  # B: 32 checks, about 7 s (reads A's eos-theory.json)
python -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
```

Both scripts accept `--out DIR`. Two runs give byte-identical outputs, and the test re-runs both and compares them byte
for byte.

Inputs (Revision outputs only):

- `Revision/algebra/gammas.json` (the author's T16);
- `Revision/field_equations_a4/a4-equations.json` (generalSource, exponentialHistory.authorWeights,
  fields.dirac16complex00.homogeneousCondensate: the field equations of the corrected metric).
