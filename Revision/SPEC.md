# REVISION SPEC (binding for every file under `Revision/`; written 2026-10-01)

## 0. Rules

* **New record, not mixed with the old.** Everything under `Revision/` is computed anew by code under
  `Revision/` for the author's primordial metric of section 1. No number, report, fixture or result
  file of the old stages (`artifacts/`, `provenance/`, `studies/`, `scripts/`, `wolfram/`, `notebooks/`)
  is copied into `Revision/` or used as a Revision result. Old documents may be READ to recall a method;
  every Revision statement is re-derived and re-verified here. Allowed shared tooling (generic, no
  physics results): `scripts/build_provenance_pdf.py` and `scripts/build_dissertation_tex.py` (PDF
  building), the vendored solver engine `vendor/rustSolveIt` (fetched by `scripts/setup_solver.*`),
  Python, WolframScript, Rust, pdflatex.
* **Honesty rule (overrides everything).** Numbers only from committed Revision outputs; every theorem
  with its exact hypotheses; interpretation labelled; never write "proved" for anything not proved.
  In particular the request "PROVE that Universes of masses {+mass, -mass} are created in pairs" is
  answered by the exact pairing theorems of section 9 and an exact statement of what they do and do not
  establish: no creation process, rate or amplitude is derived by these equations.
* **Private inputs** (never committed): `Gmail - w = ... .pdf`, `prompt_Dirac_claude*.txt`,
  `dirac-main/`, `vendor/`, `Generalized_Kronecker_Delta.*`.
* Read files in chunks of at most 300 lines; LF line endings; deterministic outputs (two runs
  byte-identical); every check recorded in a JSON report with its name, verdict and detail.

## 1. The primordial gravitational field (the author's metric, exactly)

**Changed on 2026-10-14 by the user's order** ("We are changing the metric of the primordial gravitation
field to ... Make this change throughout the entire project; create a provenance that proves that these
critical changes were correctly made"), from the author's notebook `Dirac_Einstein-Lovelock_4+4_Nash.nb`
(repository root; its input cell In[97] builds the metric, its stored output Out[101] shows it).  The user's
text, in the notebook's coordinate order (x0 = the hidden direction listed FIRST, x1..x3 space, x4 time,
x5..x7 the extra times):

```text
{{Cot[6 H x0[]]^2, 0, 0, 0, 0, 0, 0, 0}, {0, E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3), 0, 0, 0, 0, 0, 0},
 {0, 0, E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3), 0, 0, 0, 0, 0}, {0, 0, 0, E^(2 a4[x4[]]) Sin[6 H x0[]]^(1/3), 0, 0, 0, 0},
 {0, 0, 0, 0, -1, 0, 0, 0}, {0, 0, 0, 0, 0, -E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3), 0, 0},
 {0, 0, 0, 0, 0, 0, -E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3), 0},
 {0, 0, 0, 0, 0, 0, 0, -E^(-2 a4[x4[]]) b4[x4[]] Sin[6 H x0[]]^(1/3)}}
```

**The coordinates are the author's: X = {x0, x1, x2, x3, x4, x5, x6, x7}** (the notebook's In[48]; also the older
notebook Pair_Creation_of_Universes_...Nash.nb).  Every array, every component list and every frame index of the
Revision record is ordered x0, x1, ..., x7 (index 0 = x0).  On 2026-10-14 the user ordered that his coordinates be used
throughout ("YOU MUST USE MY COORDINATES {x0,x1,x2,x3,x4,x5,x6,x7}"); until then the Revision record had named them
x1 ... x8 with the hidden direction x8 listed LAST (following the metric text of the task message of 2026-10-01, quoted
in `Revision/README.md`).  That labelling is withdrawn; the map from it is x8 -> x0 (moved to the front), xk -> xk
(k = 1..7).  The metric is the one above:

```text
g = {{Cot[6 H x0]^2,0,0,0,0,0,0,0},{0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0,0,0},
     {0,0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0,0},{0,0,0,E^(2 a4[x4]) Sin[6 H x0]^(1/3),0,0,0,0},
     {0,0,0,0,-1,0,0,0},{0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3),0,0},
     {0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3),0},{0,0,0,0,0,0,0,-E^(-2 a4[x4]) b4[x4] Sin[6 H x0]^(1/3)}}
```

The only difference from the metric of this section before 2026-10-14 is the second metric function
b4(x4) > 0 in the three extra-time components; b4 = 1 is the earlier metric.  The proof that the change is
made correctly, and its consequences, are in `Revision/metric_b4/` (`METRIC_CHANGE_PROVENANCE.md`).

The coordinates, as the author names them: x0 = the hidden space direction (a small circle), z = 6 H x0 in
(0, pi/2), g00 = cot^2 z; x1, x2, x3 = ordinary 3-space (inflating, scale factor e^{a4} sin^{1/6} z); x4 = the time;
x5, x6, x7 = the three EXTRA TIMES, time-like, which DEFLATE EXPONENTIALLY (scale factor e^{-a4} b4^{1/2} sin^{1/6} z,
a4 increasing; see the memory of the author's correction: they are never treated as static or frozen in a canonical
computation).  Signature (4,4): space-like x0, x1, x2, x3; time-like x4, x5, x6, x7 (for b4 > 0).
sqrt|det g| = b4^{3/2} sin z cot z = b4^{3/2} cos z.  H > 0 is the author's constant; a4(x4) and b4(x4) are
the metric functions whose field equations section 5 derives.  Derivatives: a4' = d a4 / d x4, b4' = d b4 / d x4.

**The background history.** With the author's Lovelock weights (w1 = 1, w2 = 1/32, w3 = 1/1152,
Lambda = 10; the notebook's Out[134]/Out[135]) every vacuum solution has b4 = constant and a4 = +-H x4 +
const (proved in `Revision/metric_b4/results/vacuum-b4.json`); a constant b4 is the rescaling
x5,6,7 -> b4^{1/2} x5,6,7, i.e. the earlier metric.  Every Revision calculation that needs a background
history (the Kohn-Sham states on the slices, the dark-sector equations of state) therefore keeps b4 = 1
and states so; every formula is derived for general b4(x4).

## 2. Clifford algebra, Pin(4,4), Spin(4,4)

* Frame indices a = 0 ... 7 aligned with the coordinates x0 ... x7 (diagonal vielbein e^a_mu = sqrt|g_mumu|
  delta^a_mu); frame metric eta_ab = diag(+1, +1, +1, +1, -1, -1, -1, -1) in the order x0 ... x7.
* Gamma matrices: the author's real 16 x 16 matrices T16A[0..7] of the notebook (built from the tau
  matrices), RE-CONSTRUCTED in Revision code from the author's formulas, in the author's own frame order,
  which is the coordinate order: gamma^(xk) = T16A[k] for k = 0 ... 7 (0 = hidden, 1-3 = 3-space, 4 = time,
  5-7 = extra times).  Verify exactly: {gamma^a, gamma^b} = 2 eta^ab; reality; symmetry pattern.
* C = gamma^(x0) gamma^(x1) gamma^(x2) gamma^(x3) = T16A[0] T16A[1] T16A[2] T16A[3] (the four space-like gammas;
  the notebook's sigma16): verify C real symmetric, C^2 = 1, C gamma^a real antisymmetric.  Dirac adjoint
  Psibar = Psi^dagger C.
* Chirality Gamma = gamma^(x0) gamma^(x1) ... gamma^(x7) = T16A[8] (the notebook's product order, giving
  diag(-I8, I8)); B = -i C gamma^(x4) (Hermitian, B^2 = 1, signature (8,8)).
* S^ab = (1/4)[gamma^a, gamma^b]; verify exactly: the 16-dimensional representation is IRREDUCIBLE
  under Pin(4,4) (commutant dimension 1) and splits under Spin(4,4) into TWO INEQUIVALENT irreducible
  8-dimensional representations (the chiral halves; commutant dimension 2, intertwiner dimension 0).
  Pin(4,4) is the double cover of O(4,4), Spin(4,4) of SO(4,4).

## 3. The two fields and their Lagrangians

* dirac16complex: Psi, 16 complex ANTICOMMUTING (Grassmann) components, a Pin(4,4) spinor; quantised
  canonically (section 6).
* dirac16complex00: Phi, 16 complex COMMUTING components (16 scalar fields that transform as a
  Pin(4,4) spinor); a classical ("semi-classical") field, the analogue of Dirac's 1928 wave function.
* Coupling to gravity: the vielbein and the CANONICAL spin connection omega_mu^a_b (vielbein postulate;
  omega_mu ab = eta_ac omega_mu^c_b antisymmetric), Omega_mu = (1/2) omega_mu ab S^ab,
  D_mu Psi = d_mu Psi + Omega_mu Psi, D_mu Psibar = d_mu Psibar - Psibar Omega_mu,
  gamma^mu = e^mu_a gamma^a.  (Not the notebook's contraction of the mixed omega_mu^a_b, which lacks a
  metric factor.)
* Lagrangian density (the same form for both fields; only the statistics differ):

```text
L = sqrt|g| [ (1/2) ( Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi ) - m Psibar Psi - U(S) ],
S = Psibar Psi,   U(S) = (lambda/2) S^2   (general U where stated),
```

  with an explicit mass term linear in m and quadratic in the spinor.  Prove exactly: L is real
  (Hermitian) for both statistics; it differs from sqrt|g| [Psibar gamma^mu D_mu Psi - m S - U] by a
  total divergence; the Euler-Lagrange equations are gamma^mu D_mu Psi = (m + U'(S)) Psi and its
  adjoint, for both statistics.
* NON-TRIVIALITY TESTS [1] (dirac16complex) and [2] (dirac16complex00), both required exactly: the
  Euler-Lagrange equations contain nonzero gravitational contributions through the canonical spin
  connection for the metric of section 1 (compute gamma^mu Omega_mu and show it vanishes only in flat
  4+4 space, H = 0 and a4 constant); state precisely which pieces cancel (the time-direction terms of
  3 inflating and 3 deflating directions) and which survive; self-consistency (integrability of the
  field equations, the conserved current, the Bianchi-type identity of the energy-momentum tensor);
  and the negative control: the notebook's real Majorana-type Lagrangian Lg[] is a total derivative
  for anticommuting real fields (no field equations) - the reason the Dirac-type L is used.

## 4. Energy-momentum tensor, kinetic and potential energy, pressure, energy density, equation of state

* T_mu nu by vielbein variation (symmetric, Belinfante); the sign convention stated so that the
  energy density is rho = -T^{x4}_{x4} and the pressures are p_mu = T^mu_mu (no sum) for the space-like
  and extra-time directions; the OPERATOR (normal-ordered, section 6) for dirac16complex and the
  classical bilinear for dirac16complex00.
* Kinetic part (derivative terms) and potential part (m S + U); energy density, the pressures of
  3-space p3, of the extra times p_t and of the hidden direction p8, the trace; on shell
  (homogeneous states) rho = m S + U, p = S U' - U; the equations of state w3 = p3/rho, w_t, w8 and the
  3-space observer's effective w.  Conservation nabla_mu T^mu_nu = 0 on shell, verified exactly.
* All of this in the metric of section 1 (explicit component formulas), for both fields.

## 5. The field equations for a4[x4] and b4[x4] (each field as the source)

Einstein-Lovelock gravity with the Lovelock tensors computed with GKD (`Revision/gkd_lovelock`):
sum_{k=1}^{3} alpha_k E_(k)^mu_nu + Lambda delta^mu_nu = kappa T^mu_nu, E_(k) = -P_(k)/2^(k+1)
(alpha_1 = 1 gives Einstein).  For the metric of section 1 derive exactly: the independent components
(x0, x1 = x2 = x3, x4, x5 = x6 = x7, and the off-diagonal x0-x4 component), the EVOLUTION EQUATION for
a4 (the 3-space minus extra-time component: it contains a4'' and is sourced by p3 - p_t), the CONSTRAINT
(the x4 component), and the remaining consistency conditions (the x0 component and the x0-dependence
the source must have); specialise to each field's T^mu_nu (dirac16complex: expectation values in the
states of section 7; dirac16complex00: classical bilinears) and to Einstein gravity (alpha_2 = alpha_3 = 0)
as a special case; state what a4 the equations then allow (including the exponentially deflating
member a4 linear in x4 and what source it requires).
ADDED 2026-10-14 (metric with b4, section 1): the same for the pair (a4, b4): the evolution equations now
contain a4'' and b4''; the x4 component stays a constraint (first derivatives only); the off-diagonal x0-x4
component of every E_(k) is proportional to Cot[6 H x0] b4' (it vanishes identically for b4' = 0), so a
source with T^4_8 = 0 forces b4' = 0 or the factor Q(a4', b4'/b4) of `Revision/metric_b4/results/vacuum-b4.json`
to vanish; derive which (a4, b4) each source allows, with b4 = 1 as the earlier special case.

## 6. Canonical quantisation in 4 + 4 dimensions (dirac16complex)

x4 is the evolution time; pi = dL/d(d_4 Psi); canonical anticommutator {Psi_A(x), Psi_B^dagger(y)} =
B_AB delta^7(x - y)/sqrt|g| on a slice x4 = const; prove that this forces an indefinite (Krein) inner
product in signature (4,4); the good sector (no extra-time momentum) with a positive Fock space;
normal ordering; the expectation-value rule <Psi^dagger M Psi> = u^dagger B M u; the energy-momentum
tensor OPERATOR; the extra-time modes that grow.  dirac16complex00 is not quantised (classical field).

## 7. Kohn-Sham (DFT) approximation for dirac16complex in the primordial field

A Kohn-Sham fermion-gas model in the good sector with the contact interaction U = (lambda/2) S^2:
mean field M_eff = m + lambda S (Hartree) plus the exact local exchange of the uniform gas (derive
anew), Mermin's finite-temperature functional (the thermodynamic effective potential), reduction of
the 16-component equation to 2 x 2 blocks in the hidden coordinate, boundary conditions (the patch
end at z = pi/2 with the Z2 mirror construction, labelled ASSUMED, and a regular tip), ground state,
first excited state (Kohn-Sham gap, Delta-SCF, particle-hole), thermodynamics.  Because a4 depends
on x4, there is no stationary ground state: compute the INSTANTANEOUS (adiabatic) Kohn-Sham states
along the history with the extra times deflating (a4 increasing), with an adiabaticity measure; the
non-adiabatic (time-dependent) problem is OPEN.  The Kohn-Sham energy-momentum tensor is the source
for section 5.

## 8. The two hypotheses (to be INVESTIGATED, not assumed)

Hypothesis: dirac16complex provides a possible physical mechanism for a time-varying dark-energy and/or
dark-matter equation of state.  Hypothesis00: the same for dirac16complex00.  For each field: compute
the equation of state seen by a 3-space observer as the extra times deflate and 3-space inflates
(the condensate, the Kohn-Sham gas, mixtures), its time dependence, the CPL parameters
w(a) = w0 + wa (1 - a) (tangent at a = 1 and fits over stated ranges), and compare with the Supernovae
Unite values in the author's private PDF: the constant-w fit w = -0.764 and (w0, wa) = (-0.861, -0.60)
(deep past w0 + wa = -1.46, phantom).  Thawing means wa < 0 in this convention (w rises from near -1),
freezing wa > 0 (the PDF's table states the opposite signs; the formula decides).  Report honestly what
each field can and cannot produce (e.g. crossing w = -1 needs a non-canonical or ghost-like sector).

## 9. Pairing of universes of masses {+m, -m} (both fields)

Prove exactly, with every hypothesis: T1 (chirality map Gamma: L_{m,lambda}[Gamma Psi] =
-L_{-m,-lambda}[Psi], T -> -T, J -> -J in every gravitational field; the pair's total energy-momentum
and charge vanish for classical bilinears); T2 (Gamma combined with a Pin(4,4) reflection of character
-1: (m, lambda) -> (-m, lambda), L -> +L, the mirror across the Z2 brane); T3 (the Kohn-Sham level: the
block map with the transformed boundary conditions, (m, lambda) -> (-m, +lambda) with equal energies);
the quantum-level reading (the image field carries the Krein metric -B; no cancellation between two
independently quantised universes); and an exact statement of what these theorems do NOT establish.

## 10. Deliverables (all under `Revision/`)

* `algebra/`, `theory/` (Wolfram packages + verifiers and independent sympy checkers, reports),
  `gkd_lovelock/` (GKD, Lovelock tensors, done; its verification completed), `field_equations_a4/`,
  `kohn_sham/` (Rust solver, independent reference, checker), `dark_sector/`, `pairing/`, `notebooks/`.
* Documents (md + tex + pdf), built with `python scripts/build_provenance_pdf.py <md> --developer-layout
  --specifications Revision/pdf-specifications.json [--register]` (Revision's OWN registry; the old
  `provenance/pdf-specifications.json` is never touched by Revision work):
  1. `Revision/docs/DIRAC16COMPLEX_FIELD_THEORY` - Lagrangian, field equations, EMT operator, KE, PE,
     pressure, energy density, EoS, quantisation, a4 equations, non-triviality [1];
  2. `Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY` - the same for dirac16complex00, non-triviality [2];
  3. `Revision/docs/PAIR_CREATION_PROOFS` - the proof results for both fields;
  4. `Revision/docs/KOHN_SHAM_DEFLATING_FIELD`, 5. `Revision/docs/DARK_SECTOR_HYPOTHESES`,
  6. `Revision/docs/LOVELOCK_GKD`.
* A gate `Revision/verify_revision.{ps1,sh}` that re-runs every verifier and compares outputs.

## 11. Lead's analysis for section 8 (to be CHECKED by the dark-sector work, not results)

* The 7-volume of the metric is constant when b4 is (the inflation e^{3 a4} of 3-space is compensated by
  the deflation e^{-3 a4} of the extra times; with the metric of 2026-10-14 the volume element is
  b4^{3/2} cos z, constant in x4 exactly when b4 is, which holds on every vacuum history, section 1). A 3-space observer integrates over the hidden direction and
  the extra times, so the effective 4-dimensional density is rho_4 ~ rho_8 c^3 with c = e^{-a4} ~ 1/a,
  where a = e^{a4} is the 3-space scale factor.
* Non-relativistic quanta (conserved number in a constant 7-volume): rho_8 constant, rho_4 ~ a^-3 (dust).
  Relativistic quanta (energy ~ e^{-a4} k): rho_8 ~ a^-1, rho_4 ~ a^-4 (radiation). A Kohn-Sham gas whose
  3-momenta redshift as 3-space inflates therefore has a time-varying equation of state from 1/3 towards
  0: a candidate time-varying DARK-MATTER equation of state - to be computed, with the hidden-direction
  pressure and the extra-time pressure, which a 3-space observer does not see as pressure.
* A homogeneous condensate: S per proper 7-volume constant, rho_8 = m S + U and p = S U' - U constant, so
  w = p/rho is constant in time while rho_4 ~ a^-3: the ratio w and the dilution-inferred
  w_eff = -1 - (1/3) d ln rho_4 / d ln a = 0 disagree; 4-dimensional energy is exchanged with the extra
  dimensions. Whether any state of either field gives a time-varying DARK-ENERGY equation of state near the
  Unite values must be computed, not assumed; crossing w = -1 needs negative kinetic energy, which the
  indefinite (Krein) energy of the extra-time sector and the commuting field dirac16complex00 may supply -
  to be examined explicitly and labelled.
