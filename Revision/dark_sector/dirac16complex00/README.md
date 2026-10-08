# Hypothesis00: dirac16complex00 and a time-varying dark-sector equation of state (Revision record)

This folder investigates Hypothesis00 of `Revision/SPEC.md` section 8 for the semi-classical field
dirac16complex00: 16 commuting complex components that transform as a Pin(4,4) spinor, with the Lagrangian and
energy-momentum tensor of `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`. The background is the author's metric
of SPEC section 1, with the three extra times x5, x6, x7 deflating exponentially (scale factor e^{-a4}, a4
increasing). The reference background is the member a4 = A H x4 + a0, the only member that a homogeneous
dirac16complex00 condensate allows (`Revision/field_equations_a4`). The statements about test fields hold for
every a4(x4).

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

**Conservation (EXACT; re-derived from the metric).** For a diagonal T(x4, x8):

- nabla_mu T^mu_x4 = -d4 rho - a4' (p1 + p2 + p3 - p5 - p6 - p7)
- nabla_mu T^mu_x8 = d8 p8 + H cot z sum_dir (p8 - p_dir)

Every other component vanishes identically. For an isotropic, x8-independent source this gives
d rho/dx4 = -3 a4' (p3 - p_t) and p3 + p_t = 2 p8. Checks: `conservation_*`, with a negative control.

**The observer (ASSUMPTION, stated with its alternatives).** a = e^{a4} is the 3-space scale factor. The
3-space observer averages over the hidden direction with the weight sqrt|g| = cos z, which does not depend
on x4. The extra times are time-like:

- a compact coordinate range for them means closed time-like directions;
- a non-compact range needs a normalisation.

Two normalisations are used:

- **N1, per unit extra-time coordinate volume:** rho_4 = e^{-3 a4} <rho>. This is SPEC section 11's
  rho_4 ~ rho_8 c^3.
- **N2, per unit proper 7-volume:** rho_4 = <rho>. Equivalently, the observer integrates over a fixed proper
  extra-time volume.

Then:

- w_eff = -1 - (1/3) d ln rho_4 / d ln a;
- with the exact conservation identity, **w_eff(N1) = w3 - w_t** and **w_eff(N2) = w_eff(N1) - 1** (EXACT,
  checks `observer_*`);
- the ratio **w = p3/rho** does not depend on the normalisation.

INTERPRETATION: supernova distances measure the dilution-inferred w_eff of a 4-dimensional Friedmann
observer. It agrees with p3/rho only when no energy is exchanged with the extra times.

**Classical solutions used:**

1. The homogeneous condensate, an exact solution for every a4.
2. Plane-wave modes in the frozen local frame, exact for the local model. For both, the Krein-signed energies
   and the growing modes are computed exactly with the author's T16.
3. Adiabatic (WKB) gases of such modes in the deflating local model. This is an APPROXIMATION: the warp
   sin^{1/6} z and tan z are frozen at a fixed hidden position (wavelengths short compared with 1/H), the
   adiabatic invariance of each mode's Krein charge is assumed, and the superposition is incoherent. The
   B-run of the full 16-component equation measures how well this holds (section 3).
4. Superpositions and wave packets. Their averaged energy-momentum is the sum of the mode contributions
   (`B_superposition_average`).

## 2. Exact results

**Condensate.** Checks `condensate_*` and `linear_member_*`.

- rho = m S + lambda S^2/2 and p3 = p_t = p8 = lambda S^2/2, both constant. The ratio is
  w = lambda S/(2 m + lambda S).
- Normalisation dependence: w_eff(N1) = 0 (dust-like dilution) and w_eff(N2) = -1 (Lambda-like). wa = 0 in
  all three definitions: **no time dependence**.
- The ratio equals the Unite constant w = -0.764 at lambda S/m = **-382/441**. With rho > 0 this needs
  m S > 0 and lambda < 0, that is a negative potential U.
- The ratio is phantom exactly for lambda S/m in (-2, -1).
- For a condensate that is a self-consistent source of the linear member (A = a4'/H):
  kappa (rho + p) = -(a4'^2 + H^2) [6 alpha1 - 48 alpha2 (a4'^2 + 5 H^2) + 432 alpha3 (a4'^4 + 2 a4'^2 H^2 + 5 H^4)].
  - In Einstein gravity, rho + p = -6 (1 + A^2) H^2/kappa. With rho > 0 the ratio is therefore
    w = -1 - 6 (1 + A^2) H^2/(kappa rho) < -1, which is phantom and constant.
  - In Einstein gravity the observer's Hubble rate from the expansion gives
    w_tot = -1 - kappa (p3 - p_t)/(3 a4'^2). This is exactly -1 for the linear member, whose Hubble rate is
    constant.

**Modes and the Krein-signed classical energy.** Checks `mode_*` and `growing_*`.

- For a plane wave with 3-momentum k and extra-time momentum q, omega^2 = m^2 + k^2 - q^2. The extra times
  are time-like, so q enters with the opposite sign.
- Every real-frequency eigenspace is 8-dimensional, with Krein form of signature (4, 4). This is exact for the
  three test cases; the general statement is the Krein-inertia theorem of `Revision/pairing`.
- On it, T^mu_nu = k^mu k_nu Q/omega exactly, so rho = omega Q. **At every real frequency there are modes of
  both energy signs.** B confirms this: rho = +1.25 and -1.25 at omega = 1.25.
- For q^2 > m^2 + k^2 the modes grow. They are Krein-neutral, with rho = 0 but a growing extra-time pressure
  p5 = -m S.
- In the deflating field q_phys = q a grows. Every mode with q != 0 therefore reaches a turning point a_* and
  then grows; the deflation drives the growth.

**Gases (EXACT within the WKB model).** Checks `wkb_*` and `mixture_*`.

- Each component has rho_i = omega_i Q_i and eps_i = w_eff(N1)_i = (k^2/a^2 + q^2 a^2)/(3 omega^2) >= 0,
  independent of the sign of Q.
- For mixtures, w_eff(N1) = sum eps_i rho_i / sum rho_i.
- **Theorem:** if every component has rho_i >= 0, with real frequencies, then w_eff(N1) >= 0 and
  w_eff(N2) >= -1 at every a. There is no phantom and no crossing of -1.
- A crossing needs a component with **negative classical energy**.

## 3. Models, CPL tangents and fits

Each model is normalised to rho_tot = 1 at a = 1. The tangent is w0 = w(1), wa = -w'(1). The fits are least
squares over 101 uniform points in a ∈ [1/2, 1] (z ≤ 1) and [1/3, 1] (z ≤ 2). The "constant w" column is the
mean of w(a), a PROXY. Applied to the Unite CPL line itself, the proxy gives -1.011 on [1/2, 1]. It is
therefore not comparable with the supernova constant-w fit -0.764, which weights the data
(`unite_line_fit_proxy`). The Unite line crosses -1 at a = 461/600 = 0.768.

| model (positive energy unless stated) | definition | tangent (w0, wa) | fit [1/2, 1] (w0, wa; const) | crosses -1? |
| --- | --- | --- | --- | --- |
| M1 condensate | ratio / N1 / N2 | (lambda S/(2m+lambda S), 0) / (0, 0) / (-1, 0) | constant | no |
| M2 good-sector gas (q = 0), k^2/(k^2+m^2) = 0.417 at a = 1 | N2 | (-0.861, **+0.162074**): freezing | (-0.8655, 0.2173; -0.8112) | no |
| M2 | N1 = ratio | (0.139, 0.162074): 1/3 → 0, **dark-matter-like** | (0.1345, 0.2173; 0.1888) | no |
| M3 extra-time mode (k = 0), q^2/m^2 = 417/1417 | N2 | (-0.861, **-0.393926**): thawing, w ≥ -1 | (-0.8734, -0.2196; -0.9283) | no |
| M4 condensate + extra-time mode, s = **264037/403037**, Omega_q = **57963/264037** | N2 | (**-0.861, -0.600**) = Unite, exactly | (-0.8832, -0.2203; -0.9383) | **no** (min w → -1 from above) |
| M4 | N1 / ratio | (0.139, -0.600) / (0, 0) | (0.1168, -0.2203; 0.0617) / 0 | no |
| M5 = M4-type + **ghost** (negative-energy massless modes, 30 % of the total at a = 1) | N2 | (-0.8396, -1.0399) | (**-0.861, -0.600**; -1.011) | **yes, at a = 0.779** |

Notes on the table:

- **M3:** the turning point is at a_* = sqrt(1417/417) = 1.843, in the future.
- **M4:** the turning point is at a_* = 1.235.
- **M5:** s = 0.5678 and Omega_c = 0.7053. Without its ghost component M5 does not cross -1
  (`M5_without_ghost_no_crossing`).

**Independent second implementation (B).** B integrates the 16-component field equation of the local model
with the author's T16. It uses the exact Krein-preserving exponential midpoint step, with
A H/m = 10^-3 (adiabatic). Along every run it checks numerically that:

- the Krein charge is conserved (drift ≤ 2e-12);
- the solution is on shell (|L0| ≤ 2e-15);
- the conservation identity holds.

It then rebuilds M2 to M5 from the solutions. All tangents, fits and constant proxies agree with A to within
8.3e-4 (`B_vs_A_*`). The M5 crossing comes out at a = 0.77905 (A: 0.77910).

B also solves two problems by bisection on the field-equation solutions:

- M3: s = 0.294264 (A: 0.294284);
- M4: s = 0.655054 and Omega_q = 0.219460 (A: 0.655119 and 0.219526).

Past the turning point, the M3 mode grows at d ln|phi|/dx4 = 0.5434 against the WKB rate 0.5511. Its
amplitude grows by 10^32.2 between a = 1.5 and 2.2, and its energy density becomes large and negative
(rho/Q = -2.9e61 at a = 2.2, for A H/m = 10^-3).

## 4. Verdict for Hypothesis00

1. **Dark matter.** A positive-energy gas of good-sector modes gives, under N1 and in the ratio p3/rho, a
   time-varying equation of state from 1/3 (relativistic) to 0 (dust) (M2). A homogeneous condensate is
   dust-like under N1. Under N2 the same states look like dark energy instead. The reading depends on the
   observer ASSUMPTION.
2. **Dark energy without ghosts.** This exists only under N2, and only as freezing (M2: wa > 0) or thawing
   (M3, M4: wa < 0) evolution with w ≥ -1 at every a.
   - The thawing case is driven by the deflation, which blueshifts the extra-time momentum.
   - M4 reproduces the Unite CPL **tangent** (-0.861, -0.60) exactly, but its actual w(a) never crosses -1.
     The phantom past w0 + wa = -1.461 belongs to the linear CPL extrapolation, not to the model.
   - Its least-squares fit over [1/2, 1] is (-0.883, -0.220), not the Unite pair.
   - The same mode reaches a turning point (a_* = 1.235) and then grows without bound.
   - Under N1, or in the ratio, the same model is not dark energy (w ≥ 0).
3. **Phantom and crossing of -1.** With positive-energy components only, both are impossible (theorem of
   section 2).
   - They occur when components of negative classical energy are present (M5: the Unite fit over [1/2, 1]
     reproduced, crossing at a = 0.779 against 0.768).
   - The only phantom without a negative energy density is the constant ratio of a condensate with lambda < 0.
   - **A classical field with negative-energy components is a ghost-like sector**, and dirac16complex00 has
     one at every real frequency: its classical energy is unbounded below (the classical form of the
     spin-statistics problem of a commuting field with a first-order Lagrangian).
   - A dark-energy reading of Hypothesis00 that reproduces the Unite crossing therefore requires that ghost
     sector to be populated with a sizeable fraction (30 % in M5, a stated choice; smaller fractions push the
     extra-time mode's turning point towards a = 1). It also requires the observer normalisation N2.
4. **The constant-w fit -0.764** is matched exactly only by the time-independent condensate ratio
   (lambda S/m = -382/441, lambda < 0). Under N1 and N2 the condensate gives 0 and -1.
5. **Expansion-inferred w (Einstein gravity, backreacted homogeneous source).** For the exponentially
   deflating linear member the 3-space Hubble rate is constant, so w_tot = -1 exactly. A time-varying total w
   needs a4'' != 0, which requires p3 != p_t, and no condensate source gives that.

## 5. What is not claimed

- No supernova likelihood: there are no covariances and no distance fits; the "fits" are least squares of
  w(a).
- The models M2 to M5 are illustrative members with stated parameters. They are not predictions, and nothing
  selects their populations.
- The WKB/local model freezes the hidden-direction warp. An x8-dependent configuration is not a consistent
  source of the metric (`Revision/field_equations_a4`): the test-field results are not backreacted, except in
  item 5 of section 4.
- The growing modes make the Cauchy problem ill-posed (`Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY`
  section 7). Nothing here cures that.
- Nothing here establishes that dirac16complex00 *is* dark energy or dark matter.

## 6. Reproduction

From the repository root:

```text
python Revision/dark_sector/dirac16complex00/python/derive_eos.py            # A: 49 checks, about 25 s
python Revision/dark_sector/dirac16complex00/python/independent_numerics.py  # B: 28 checks, about 20 s (reads A's eos-theory.json for the comparison)
python -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
```

Both scripts accept `--out DIR`. Two runs give byte-identical outputs, and the test re-runs both and compares
them byte for byte.

Inputs (Revision outputs only):

- `Revision/algebra/gammas.json` (the author's T16);
- `Revision/field_equations_a4/a4-equations.json` (the linear member).
