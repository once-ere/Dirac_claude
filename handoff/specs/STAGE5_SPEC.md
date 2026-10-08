# STAGE 5 SPEC — dirac16complex00 (commuting), both Lagrangians with explicit mass
# terms, their EMT/EoS in arbitrary and primordial fields, Kohn–Sham DFT of both in
# the primordial field, and the exact {+M, -M} pairing theorems

Binding for every Stage-5 agent.  Conventions are those of Stages 1-4
(`handoff/specs/CONTRACT.md` with errata §11, `STAGE2_SPEC.md`, `STAGE4_SPEC.md`
with errata §7-§9, `HANDOFF.md` §4): counting from 0, x = {x0..x7}, x4 = time,
eta = diag(+1,+1,+1,+1,-1,-1,-1,-1), gamma^a = notebook T16^A[a] (exact fixture
`artifacts/dirac16complex/arbitrary-field/algebra-fixture.json`), C = sigma16,
Psibar = Psi^dagger C, B = -i C gamma^4, gamma^8 = diag(-I8, +I8) (fixture key
"chirality"), canonical spin connection Omega_mu = (1/8) omega_{mu ab}[gamma^a, gamma^b]
with omega_{mu ab} = eta_{ac} omega_mu^c_b.

## 0. What the user asked (verbatim substance) and how "prove" is honoured

1. Recall: dirac16complex is the SECOND-QUANTIZED (anticommuting, Grassmann) spinor field.
2. Define dirac16complex00: a 16-component Pin(4,4) CLASSICAL spinor field whose 16
   components are COMMUTING complex scalar fields that transform together as a
   Pin(4,4) spinor (the analogue of Dirac's original 4-component wave function).
3. A non-zero, non-trivial Lagrangian for dirac16complex00 with a non-zero,
   non-trivial coupling to the spin connection and to gravity.
4. For BOTH Lagrangians an explicit non-zero, non-trivial mass term, linear in the
   mass and quadratic in the spinor components.
5. Write out and record (md, tex, pdf): both Lagrangians, the EMT (operator for
   dirac16complex, classical for dirac16complex00), kinetic energy, potential energy,
   pressure, energy density and equations of state for the covariant field equations
   (the Euler–Lagrange equations of both), in an ARBITRARY gravitational field and in
   the PRIMORDIAL gravitational field.
6. CRITICAL: in the primordial field, a DFT-motivated approximation like Stage 4
   (Kohn–Sham fermion-gas thermodynamic effective potential, DFT ground and first
   excited states) for EACH field, and "PROVE that Universes of masses {+mass, -mass}
   are created in pairs" for each field; new md/tex/pdf with the exact proof results.
7. Push; check and verify the repository.

The author's notebook states the goal as a HYPOTHESIS (cell 6: "at time x4 = 0 ... a
pair of universes with MASSES ± M is created"; cell 17: "TODO: prove Universe(s) of
masses ±M are created in pairs!"; cell 7: "Are Universe(s) of masses ± M created in
pairs at time x4 = 0?").  HONESTY RULE: prove exactly what the equations imply, as
theorems with hypotheses stated; verify each exactly (Wolfram and independently
sympy) and numerically (Kohn–Sham, two solvers).  State separately, as
interpretation, what is not derived (a dynamical creation rate or amplitude, a wave
function of the universe).  Never write "proved" for anything that is not.

## 1. The two fields and their Lagrangians (arbitrary gravitational field)

Both fields: Psi : M^8 -> C^16, Psibar = Psi^dagger C, D_mu = d_mu + Omega_mu,
gamma^mu = e_a^mu gamma^a.  dirac16complex: Grassmann-odd components (Stage 1).
dirac16complex00: commuting (c-number) components.

    L = sqrt|g| [ (1/2)(Psibar gamma^mu D_mu Psi - (D_mu Psibar) gamma^mu Psi)
                  - m Psibar Psi  -  U(Psibar Psi) ]                        (L1)

* The mass term L_m = -m sqrt|g| Psibar Psi is LINEAR in m and QUADRATIC in the
  components.  Non-zero and non-trivial: exhibit exact configurations with
  Psibar Psi != 0 (for the Grassmann field: a nonzero element of the Grassmann
  algebra; for the commuting field: a numerical spinor), and show that it changes the
  field equation (the free equation gamma^mu D_mu Psi = m Psi has the mass-shell
  consequence (gamma^mu D_mu)^2 Psi = m^2 Psi + ..., i.e. m enters the dispersion
  k^2 = m^2 in flat space).
* U: dirac16complex: polynomial in S = Psibar Psi, default U = (lambda/2) S^2
  (Grassmann: only polynomials, S^17 = 0).  dirac16complex00: any smooth U(S); default
  the same U = (lambda/2) S^2 so that the two theories differ ONLY in the statistics.
* Reality: C gamma^a is real antisymmetric (anti-Hermitian) and C is real symmetric;
  prove L real (Hermitian) for commuting components by the same argument as for the
  Grassmann ones (complex conjugation reverses products in both conventions); verify.
* Non-trivial gravitational/spin-connection coupling: gamma^mu Omega_mu != 0 in a
  curved field (explicit metric jets), the divergence identity
  d_mu(sqrt|g| gamma^mu) = sqrt|g| [gamma^mu, Omega_mu], and the Lichnerowicz
  formula; the coupling enters the field equation (show a nonzero Omega-dependent term).
* REAL restriction (the notebook's Lg[]): for REAL COMMUTING Psi16 the notebook-type
  Lagrangian Psi^T sigma16 T16^a D_a Psi (+ mass term (H M) Psi^T sigma16 Psi) is
  NON-trivial (sigma16 T16^a antisymmetric gives a symplectic first-order kinetic
  term; sigma16 symmetric gives a nonzero mass term), in contrast with the Grassmann
  case of Stage 1 where it is a total divergence with an identically vanishing mass
  term.  Prove both statements exactly; state which Lagrangian dirac16complex00 uses
  (the complex (L1)) and how the real restriction relates to it.

## 2. Field equations, EMT, conserved current, energies (arbitrary field)

    gamma^mu D_mu Psi = (m + U'(S)) Psi,      (D_mu Psibar) gamma^mu = -(m + U'(S)) Psibar    (EL)

Same form for both statistics (derive for commuting components: the variation of a
product has no Grassmann signs; verify that the result is identical).

EMT (vielbein variation, symmetric, Belinfante-equivalent; Stage-1 form):

    T_mu nu = -(1/4)[Psibar gamma_mu D_nu Psi + Psibar gamma_nu D_mu Psi
                     - (D_mu Psibar) gamma_nu Psi - (D_nu Psibar) gamma_mu Psi] + g_mu nu L_s

(L_s = L/sqrt|g|).  For dirac16complex T_mu nu is an operator (normal ordered with
respect to the free Krein vacuum as in Stage 1); for dirac16complex00 a c-number
field.  Prove conservation nabla^mu T_mu nu = 0 on shell (both), the trace on shell
(-m S + 7 S U' - 8 U), the current j^mu = Psibar gamma^mu Psi and its conservation.
Energy density rho = T_44 (x4 time; state the index position and sign convention used
in Stage 1 and keep it), pressures p_(i) = T^i_i (no sum) etc., kinetic/potential
splits KE_L, PE_L and KE_H, PE_H exactly as Stage 1 (CONTRACT §7-§8), equations of
state w_(i) = p_(i)/rho.  For dirac16complex00 add: the conserved charge density
j^4 is INDEFINITE (Krein metric B of signature (8,8)), so the Dirac probability
interpretation fails in (4,4); the classical energy is not bounded below; state and
prove both exactly (explicit solutions).

## 3. Primordial gravitational field

Use the Stage-2 primordial field (Dirac16ComplexPrimordial.wl, STAGE2_SPEC.md, with
its errata) and the Stage-4 static warped form (STAGE4_SPEC §1, §8 E4.3: R = -42H^2,
rho_req = -21H^2/kappa, p_req = +15H^2/kappa).  Specialise §1-§2 for both fields:
reduced EL equations (the 3H gamma^0 term removed by W^{-3}), the homogeneous
(cosmological) mean-field EMT, KE/PE, rho, p, w, and the reduced 2x2 block equations
of Stage 4.

## 4. Kohn–Sham DFT of both fields in the primordial field

Common frame (Stage 4, unchanged): static warped chart, sector and ansatz, eight 2x2
blocks, parity conditions at the brane, bag condition at the tip, Mermin finite-T
functional, Fermi–Dirac occupations with mu from N ("fermion-gas thermodynamics";
for dirac16complex00 this is the Pauli filling of Dirac one-particle states, imposed
as the user specifies), no correlation term, no-sea convention of Stage 4.

The ONLY place where the statistics enters the energy functional of a quasi-free
(Gaussian) state with one-body density matrix rho is the Wick contraction of the
interaction:

    dirac16complex   (anticommuting): <U> = (lambda/2)[Tr(M rho)^2 - Tr(M rho M rho)]
    dirac16complex00 (commuting):     <U> = (lambda/2)[Tr(M rho)^2 + Tr(M rho M rho)]

with M the expectation-rule matrix of S (Stage 4: BC).  Consequences to derive
exactly: filled shell E_x = -E_H/8 (anticommuting) versus +E_H/8 (commuting); uniform
gas e_x = -(lambda/32)(n^2 + S^2) versus e_x^{00} = +(lambda/32)(n^2 + S^2); KS
potentials M_eff = m + lambda S_p + v_s, v_s = -+(lambda/16) S, v_v = -+(lambda/16) n
(upper sign anticommuting).  So dirac16complex00 has M_eff = m + (17/16) lambda S_p and
v_x = +(lambda/16) n_p.  State the status of this model plainly: a DFT-motivated
mean field of a random-phase (Gaussian) ensemble of classical modes with Fermi–Dirac
occupations, not a quantum theory of commuting spinors (which would violate the
spin-statistics connection).

Ground state: the self-consistent branch reached by continuation in lambda from
lambda = 0 (STAGE4_SPEC E4.8).  First excited state: KS gap, particle-hole list
(occupation floor 1e-12, E4.9), Delta-SCF.  Finite T as in Stage 4.

## 5. The {+M, -M} pairing theorems (to PROVE exactly, both fields)

T1 (chirality map, field level, arbitrary gravitational field, both statistics).
    Gamma8 : Psi -> gamma^8 Psi.  gamma^8 is Hermitian, (gamma^8)^2 = 1, anticommutes
    with every gamma^a, commutes with C and with every Omega_mu.  Hence
    S[gamma^8 Psi] = S[Psi], kinetic term -> -(kinetic term), j^mu -> -j^mu, B -> -B,
    L_{m,lambda}[gamma^8 Psi] = -L_{-m,-lambda}[Psi], Psi solves EL_{m,lambda} iff
    gamma^8 Psi solves EL_{-m,-lambda}, and
    T_mu nu[gamma^8 Psi; -m, -lambda] = -T_mu nu[Psi; m, lambda].
    COROLLARY (pair): for Psi_+ with (m, lambda) and Psi_- = gamma^8 Psi_+ with
    (-m, -lambda): T_mu nu^{pair} = 0 identically, total charge 0, total energy,
    momentum and stresses 0 — in ANY gravitational field, at every x4, in particular
    at x4 = 0.  The Einstein (or Einstein–Lovelock) equations with the pair as source
    are the source-free equations: a {+M, -M} pair of this type carries no net
    energy-momentum and no net charge, so its creation from the field-free state is
    consistent with every conservation law and constraint.  (Theorem about
    consistency/kinematics, NOT a computed creation rate.)  For lambda = 0 the pair
    consists of the same free field with masses +m and -m.
T2 (mirror map with the same lambda).  Combine gamma^8 with a Pin(4,4) reflection of
    character -1 (CONTRACT E3) to get a map (m, lambda) -> (-m, lambda) with
    L -> +L (up to the coordinate reflection); derive the EMT relation (T -> +T on the
    reflected coordinates).  In the Z2-extended primordial field (Stage 4: the
    reflection Psi(-y) = +-gamma^0 Psi(y) is a symmetry iff the mass function is odd)
    this is the "mirror universe" of mass -M on the other side of the brane.
T3 (Kohn–Sham level, primordial field, both statistics).  The block-level image of
    T1/T2 (sigma1 conjugation of the 2x2 blocks etc.): derive exactly how
    (m, lambda, parity p, bag angle theta, j) map, show the KS equations, occupations,
    energies, densities (n -> n, S -> -S or as derived), potentials, EMT profiles and
    the KS ground and first excited states of the +M universe map EXACTLY onto those
    of the -M universe (with the transformed boundary conditions), and state what
    changes if the -M universe keeps the untransformed boundary conditions.  Derive
    the pair totals at the KS level (energy, charge, EMT averages) including the
    normal ordering/expectation rule (B -> -B under gamma^8).
T4 Numerical demonstration (both solvers, both fields): compute KS ground and first
    excited states of the +M and -M universes (m = 1 and 3, L = 3, N = 8 and 112,
    lambda in {0, +-lambda_hat_1, +-lambda_hat_2}, T = 0 and one T > 0), verify the
    pairing to solver precision, report the pair totals, and the untransformed-BC
    control.

## 6. Deliverables (Stage 5)

* wolfram/Dirac16Complex00.wl + scripts/verify_dirac16complex00.wls (exact: §1-§3 for
  the commuting field, the real restriction vs the notebook's Lg[], side-by-side with
  the Grassmann field) -> artifacts/dirac16complex/pair-creation/wolfram-dirac16complex00-report.json
* wolfram/Dirac16ComplexPairing.wl + scripts/verify_dirac16complex_pairing.wls (exact:
  T1-T3, the Wick sign, the uniform-gas e_x^{00}) -> .../wolfram-pairing-report.json
* scripts/check_dirac16complex00.py, scripts/check_dirac16complex_pairing.py
  (independent sympy/mpmath, own derivations; agreement checks with the Wolfram reports)
* Numerics: the Stage-4 Rust crate studies/dirac16complex_kohn_sham gains a
  `pairs` subcommand (and whatever parameters it needs: mass sign, statistics sign,
  transformed boundary conditions) with outputs in
  artifacts/dirac16complex/pair-creation/rust/; the Stage-4 subcommands and outputs
  must stay BYTE-IDENTICAL (new parameters default to the Stage-4 values and are not
  written when default; verify by rerunning `spectrum`, `excited --quick` and one scf
  run and comparing bytes); the reference solver scripts/ks_reference_solver.py gains
  the same options (Stage-4 outputs unchanged) with outputs in .../pair-creation/reference/;
  a checker scripts/check_dirac16complex_pairs.py (Rust vs reference; pairing
  identities; pair totals).
* Documents: provenance/DIRAC16COMPLEX00_FIELD_THEORY.{md,tex,pdf} (item 5 of §0 for
  both fields) and provenance/DIRAC16COMPLEX_PAIR_CREATION.{md,tex,pdf} (items 6: the
  DFT of both fields, the theorems with proofs, verification records, the numerics,
  what is and is not proved), registered, pinned in tests.
* Gate scripts/verify_stage5_pair_creation.{ps1,sh} (Stage-3/4 pattern; final line
  stage5_pair_creation_verification=OK); unit tests tests/test_d16c_stage5_*.py.

## 7. Process rules

Exact first (Wolfram + independent sympy), then numerics, then documents, then four
adversarial review lenses, then fixes, then the gate from a fresh public clone, then
push.  Never modify dirac-main/, vendor/, the author's .nb input notebook, or any
Stage 1-3 output; Stage-4 outputs must stay byte-identical.  The Stage-4 work that
was paused on 2026-09-30 (suspended processes, uncommitted files of stopped agents)
is NOT part of Stage 5: do not touch artifacts/dirac16complex/kohn-sham/** except by
the byte-identity checks above.

## 8. Lead's independent numerical checks (2026-09-30, binding input for the numerics agents)

* Block map (reference eigensolver, unmodified, grid N = 240, L = 3, M(y) = 1 + 0.3 cos y,
  v(y) = 0.2 e^y): spec h_{+1}(M, v; parity +1, tip g0) = spec h_{-1}(-M, v; parity -1,
  tip f0) to 7.6e-6 at k = 0 and 7.5e-5 at k = 0.75 (all other parity/tip combinations
  differ by O(0.2..2)).  In the reference's variables: tip g0 <-> f0 and the parity
  sector flips; the vector potential v is unchanged; eps is unchanged.
* lambda = 0, N = 8, L = 3, parity 0, N0 = 40, two levels: m = +1 tip g0: E = 0, gap
  0.4307366923; m = -1 tip f0: E = 0, gap 0.4307336459; m = -1 tip g0 (untransformed):
  gap 0.1008519432.  N = 112: E = 61.0911465 (m = +1, g0) and 61.0907178 (m = -1, f0),
  gaps 0.0955469 and 0.0955462, scalarCharge -20.8526 and +20.8534, nTotal 112 both.
* WARNING (reference negative-mass bookkeeping): in the same N = 112 runs the internal
  arrays lv['n_c'] and lv['s_c'] (which feed M_eff and v_x) satisfy n_c(-M) = -n_c(+M) and
  s_c(-M) = +s_c(+M), although nTotal and scalarCharge are consistent (n invariant, S
  flipped).  With lambda != 0 (lambda_hat = 0.0973, N = 8) no sign of lambda pairs the -M
  universe with the +M one in the unmodified reference: E(+1, +lambda, g0) = -0.0078300806,
  E(-1, +lambda, f0) = +0.0075217455, E(-1, -lambda, f0) = -0.0075217455.  Audit and fix
  the density bookkeeping for m < 0 (branch classification against the free spectrum, the
  type -1 conjugation map, the weights) before any lambda != 0 pairing test.
* Expectation from the block analysis (to be proved or refuted exactly, not assumed):
  with the Stage-4 expectation rule the per-block scalar density carries the factor j and
  flips under the map (s -> -s), the number density does not (n -> n); then
  M_eff -> -M_eff requires (m, lambda) -> (-m, +lambda) and v_x = -(lambda/16) n is
  unchanged as the map requires, so the KS ground and excited states of the +M and -M
  universes would coincide with the SAME lambda (a mirror pair of equal energy), whereas at
  the level of the classical field bilinears (no Krein metric) T1 gives
  (m, lambda) -> (-m, -lambda) with T -> -T.  Which statement holds for which field and
  which density definition must come out of the exact theory (pairing-theory.json).
* Wick sign (independent numpy check): commuting circular Gaussian: Tr(A rho)Tr(B rho) +
  Tr(A rho B rho) (exact Isserlis 0.2307291551, Monte Carlo 0.226); fermionic quasi-free
  state, exact 3-mode Fock space, normal ordered: Tr(AG)Tr(BG) - Tr(AGBG) (0.369553091).
* Diagnosis of the warning above: densities() sums mult * w * n over states with
  w = f on the particle branch and w = -(1 - f) on the sea branch; the branch comes from
  free_branch_counts(grid, m, ...) (rank against the free spectrum with the BARE m).  For
  m < 0 the occupied positive-energy states of the -M universe evidently get sea-branch
  weights, so n_c integrates to -N while the physical scalar density flip (s -> -s) is
  undone by the negative weights.  Under the exact map the -M universe has the SAME eps
  spectrum as the +M universe, so its particle/sea classification must be the image of
  the +M one (by energy rank of the mapped levels), not the rank against a free spectrum
  computed with the wrong conventions.  Fix it at the root in both solvers and test it on
  lambda = 0 (n_c(-M) = n_c(+M), s_c(-M) = -s_c(+M) node by node).

## 9. Errata (2026-10-08, stage5-plan)

* E5.1 (quantum reading of the T1 corollary; matter-antimatter review finding F1, confirmed by
  MA_M4_imageFieldFockModel and provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.md section 7.3).  The
  COROLLARY of §5 T1 is a statement about classical fields (commuting c-number fields, or two
  independent classical fields in the correlated configuration Psi_- = gamma^8 Psi_+).  For the
  quantum field the identities H[Psi_-; -m] = -H[Psi; m], Q[Psi_-] = -Q[Psi] and
  :T[gamma^8 Psi; -m, -lambda]: = -:T[Psi; m, lambda]: hold as operator identities, but the image
  field (anticommutator -B) is the same quantum system: [Psi_-, H[Psi_-; -m]] = -h(-m) Psi_-,
  [Psi_-, Q[Psi_-]] = -Psi_-, so its own x4-generator, charge and metric EMT are +H_+, +Q_+, +T_+, and
  the values -|eps|, -1 per quantum are those of the L_{-m,-lambda} formulas.  At the quantum level
  no reading gives a cancellation between two independent, consistently quantised universes.
  Corrected at the root in wolfram/Dirac16ComplexPairing.wl (T1krein.imageField / consequence,
  T1.kreinMetric, T1.corollaryPair statement / hypotheses / meaning, T3.theoremImageRule,
  T3.pairTotalsKS.kreinImagePair, numericsPrescription.pairTotalsToReport, notProved,
  notebookHypothesis) and scripts/check_dirac16complex_pairing.py (statements); the existing checks
  PAIR_T1krein_imageOperatorIdentities and S5_T1krein_imageOperatorIdentities now also verify the
  four commutators above (check names and counts unchanged: 141 and 172).  The Krein-image pair
  totals of T3/T4 (E = 0, charge 0, T = 0) stay exact identities; their reading is X + (-X) = 0.
* E5.2 (Rust y-grid uncertainty in scripts/check_dirac16complex_pairs.py, as STAGE4_SPEC E4.12 and
  E4.14).  Every member of a Rust y-grid refinement family is compared with the reference, each with
  its OWN grid-error term (check_dirac16complex_kohn_sham.member_grid_errors): the coarsest member
  |X_1 - X_0|, a finer member only |X_k - X_(k-1)| / (r^p - 1), p measured per quantity from three
  grids of equal ratio, otherwise the scheme's smallest order 2 (reason recorded).  Before, the finer
  members were not compared and the 301-point member got the largest difference to any partner.
  Tests: tests/test_d16c_stage5_pairs.py CheckerGridUncertaintyTests (negative control: a planted
  deviation of the finer member is detected).
