# Stage 5 document outlines (binding structure; numbers only from the Stage-5 reports)

Errata E5.1 (quantum reading of the T1 corollary) and E5.2 (Rust y-grid uncertainty per member) of
STAGE5_SPEC.md section 9 (2026-10-08) bind both documents.

## A. provenance/DIRAC16COMPLEX00_FIELD_THEORY.md

Title: "dirac16complex and dirac16complex00: Lagrangians, field equations, energy-momentum
tensors and equations of state in an arbitrary and in the primordial gravitational field"

1. Summary (what is defined, what is proved, where each result is verified; one table
   "result -> Wolfram check -> Python check").
2. Conventions (inherited; the exact fixture; gamma^8, C, B facts used below).
3. The two fields
   3.1 dirac16complex: second-quantized, Grassmann-odd components; Krein-space quantization
       (recall Stage 1, with references to the Stage-1 document sections).
   3.2 dirac16complex00: classical, commuting complex components transforming as a Pin(4,4)
       spinor; the analogue of Dirac's 1928 wave function; what it is not (a quantum field
       of commuting spinors would violate the spin-statistics connection).
   3.3 The real restriction and the author's Lg[]: trivial for real Grassmann Psi16
       (Stage 1), non-trivial for real commuting Psi16 (proved here).
4. The Lagrangians (L1) of both fields
   4.1 kinetic term, canonical spin connection, reality proof for both statistics;
   4.2 the explicit mass term -m sqrt|g| Psibar Psi: linear in m, quadratic in the
       components, non-zero and non-trivial (explicit configurations, dispersion);
   4.3 the interaction U(S) (polynomial for Grassmann, smooth for commuting; default
       (lambda/2) S^2);
   4.4 non-trivial coupling to the spin connection and to gravity (explicit jets,
       divergence identity, Lichnerowicz).
5. Euler–Lagrange equations (derivation for commuting components; identical form).
6. Energy–momentum tensor (operator for dirac16complex, c-number for dirac16complex00):
   definition, symmetry, conservation, trace; the current; energy density, pressures,
   KE/PE splits (Lagrangian and Hamiltonian), equations of state — arbitrary field.
7. Statistics-dependent statements: Krein-space positivity (dirac16complex) versus the
   indefinite charge density and unbounded classical energy of dirac16complex00 (explicit
   solutions).
8. The primordial field: both fields in the Stage-2 cosmological chart and in the Stage-4
   static warped form; reduced equations; homogeneous/mean-field EMT, rho, p, w, KE/PE.
9. Verification records (every check family, counts, agreement Wolfram vs Python).
10. Reproduction commands (PowerShell and Bash).
11. Limitations and non-claims.

## B. provenance/DIRAC16COMPLEX_PAIR_CREATION.md

Title: "Pairs of universes of masses +M and -M: exact pairing theorems and Kohn–Sham
ground and first excited states of dirac16complex and dirac16complex00 in the primordial
field"

1. Summary: the notebook's hypothesis (quoted: cells 6, 7, 17), exactly what is proved,
   exactly what is not (no creation rate/amplitude; interpretation marked).
2. Conventions and the facts about gamma^8, C, B used in the proofs.
3. Theorem T1 (chirality map, field level) with proof; corollary: vanishing total
   energy-momentum and charge of a pair (hypotheses: lambda -> -lambda, or lambda = 0);
   the corollary is a statement about CLASSICAL fields (commuting c-number fields, or two
   independent classical fields in the correlated configuration Psi_- = gamma^8 Psi_+); its
   quantum reading per E5.1: the operator identities hold, but the image field under its own
   anticommutator -B is the same quantum system, with x4-generator, charge and metric EMT
   +H_+, +Q_+, +T_+, so no reading gives a cancellation between two independent, consistently
   quantised universes; what "creation at x4 = 0" means as a statement about
   constraints/conservation.
4. Theorem T2 (mirror map with the same lambda; Pin reflection; the Z2 mirror universe of
   mass -M across the brane).
5. The Kohn–Sham model of each field in the primordial field (Stage-4 frame; the Wick sign
   of the statistics; e_x and the KS potentials for both fields; the model's status).
6. Theorem T3 (KS level): the exact block map, the transformed boundary conditions, the
   mapping of spectra, occupations, energies, densities, EMT; the ground and first excited
   states of the +M and -M universes; pair totals at the KS level (the Krein-image pair
   totals E = 0, charge 0, T = 0 are exact identities read as X + (-X) = 0 between the +M
   values and the (-m, -lambda) formulas on the same state, E5.1); what fails with
   untransformed boundary conditions.
7. Numerical demonstration T4 (both solvers, both fields): tables and figures of the +M,
   -M (transformed) and -M (untransformed) runs; pairing deviations; pair totals; every
   member of a Rust y-grid refinement family compared with the reference with its own
   grid-error term (E5.2).
8. Verification records.
9. Reproduction commands.
10. What is proved, what is interpretation, open problems (including E5.1: no cancellation
    between two independent quantised universes is proved or claimed).
