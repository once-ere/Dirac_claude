# Outline: provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md

Title (H1): `dirac16complex: a complex Grassmann spinor of Pin(4,4) in an arbitrary gravitational field`
Subtitle (H2, mandatory for the builder): `Lagrangian, covariant field equations, energy-momentum tensor, canonical quantization and equations of state`

Every numbered claim below must be backed by a named check in one of the four
reports (wolfram-algebra, wolfram-geometry, python-algebra, python-geometry,
grassmann-demo) and the document must cite the check name.  Numbers quoted in the
document (ranks, dimensions, signatures, constants such as the Lichnerowicz c)
must be copied from the reports, never from memory.

1. Abstract.
2. Scope, claims and non-claims (what is proved exactly, what is conventional,
   what is NOT claimed: no observational claim, (4,4) is not observed spacetime,
   perturbative stability not studied, Krein/ultrahyperbolic caveats).
3. Counting and notation dictionary.  Table mapping: this document | notebook
   (WolframScript names: X, T16^A, T16^α, σ16, SAB, ωmat, Q1, H*M, detgg, sg,
   constraintVars, Ψ16, Lg[]) | dirac-main (γ_1..γ_8 labels vs e0..e7 indices, C,
   Σ_ab, ω_μab, D_μ) | Gmail PDF (φ, V, ρ_φ, P_φ, w_φ, KE, PE, CPL w0, wa;
   metric signature (+,-,-,-) vs ours).  Zero-based counting; coordinate column
   (v_0..v_7)^T; complex vector space definitions as given by the task.
4. The Clifford module in the split-octonion (notebook) picture and in the
   Clifford (dirac-main) picture: exact construction of τ, τ̄, γ^a; C = σ16;
   expression [1] verbatim in WolframScript and its proof; chirality; the exact
   intertwiners K_clifford and K_octonion (dimensions, ranks, K C K^-1 = C_dm);
   verification record.
5. Definition of dirac16complex: complex, Grassmann-odd, 16 components; Pin(4,4)
   action (twisted vs untwisted adjoint lift); theorem: C^16 is an irreducible
   Pin(4,4) module; theorem: under Spin(4,4) (preimage of SO(4,4), det 1) it is
   the direct sum of two inequivalent irreducible 8-dimensional modules; proofs
   by commutant dimensions; bundle S_C = P_Spin ×_ρ (C ⊗ Δ_R).
6. Canonical spin connection: vielbein, Christoffel, vielbein postulate (the total
   covariant derivative of the vielbein vanishes), ω_μ^a_b, ω_μab, Ω_μ with 1/8
   over ordered pairs, D_μ on Ψ and Ψbar; D_μγ^ν = 0; divergence identity; curvature
   F = (1/2)R S; the notebook contraction ω_μ^a_b S^{ab} and why it is wrong
   (symmetric mixed components; failing D_μγ^ν test with measured violation).
7. Why the notebook Lagrangian Lg[] is empty for a Grassmann field: lemmas
   (Ψ^T M Ψ = Ψ^T M_antisym Ψ), theorem (EL operator E ≡ 0 identically), proof,
   Grassmann-algebra verification; commuting-field remark.
8. The dirac16complex Lagrangian: formula; WolframScript form written in the
   notebook's variable names (ConjugateTranspose, σ16, T16^α, lowered ω, SAB,
   Sqrt[Abs[detgg]]), term-by-term relation to Lg[]; Hermiticity; symmetries
   (local Spin_0(4,4), diffeomorphisms, U(1)); potential restricted to polynomials
   (S^17 = 0); discrete maps: γ^8 (L_m -> -L_{-m}, T -> -T; the ±M observation,
   explicitly labelled structural, not physical), Pin characters.
9. Euler–Lagrange equations in an arbitrary gravitational field: derivation, final
   covariant equations for Ψ and Ψbar, component form γ^μ D_μ Ψ = e_a^μ γ^a(∂_μ +
   (1/8)ω_μbc[γ^b,γ^c])Ψ; non-triviality theorem (Ω pure gauge iff Riemann = 0;
   Lichnerowicz with the measured constant c times R); diagonal-vielbein formula.
10. Energy–momentum tensor operator: derivation from the tetrad/metric variation,
    final formula, symmetry, Hermiticity, conservation on-shell, trace; observer
    decomposition (ρ, p_(i), mean p̄); kinetic/potential energies: Lagrangian split
    (A) and Hamiltonian split (B) with exact definitions; equation of state
    w = p/ρ; homogeneous reductions (ρ = mS + U, p = SU' - U, KE_L, PE_L,
    off-diagonal consistency conditions, conservation law); side-by-side with the
    scalar-field formulas of the Gmail PDF (ρ_φ = φ̇²/2 + V, P_φ = φ̇²/2 - V) and the
    exact analogy/difference; phantom crossing criterion KE_L < 0.
11. Canonical quantization in 4+4 dimensions: x4 slicing, momenta, second-class
    constraints, Dirac brackets, equal-time anticommutators in curved space,
    Hamiltonian density, Heisenberg equations; Krein-space theorem (every
    Spin(4,4)-invariant Hermitian form is chirality-even, γ^4 is odd ⇒ indefinite
    charge, B of signature (8,8)); fundamental symmetry J = B and the positive
    Hilbert structure; flat-space mode expansion, dispersion
    E^2 = m^2 + k_0^2+..+k_3^2 - k_5^2 - k_6^2 - k_7^2, good sector
    (k_5=k_6=k_7=0): Hermitian h_k, 8 particle + 8 antiparticle states per k,
    Dirac sea, normal ordering, Fock space; which symmetries are unitary
    (Spin(4)×Spin(3)) vs Krein-unitary (Spin(4,3)); U(1) current and charge;
    the extra-time sector's complex frequencies (ultrahyperbolic ill-posedness);
    the expectation-value rule ⟨Ψ^†MΨ⟩ = u^†BMu for one-particle states.
12. Verification records (each check, both implementations, counts).
13. Reproduction commands: PowerShell and Git Bash, exact.
14. Limitations.

BUILDER CONSTRAINTS (scripts/build_dissertation_tex.py): see
scratchpad/survey_dirac-main-machinery.md "pitfalls" + whatever the tooling agent
added (check its report): $$ alone on its own line; no blank line inside $$; no
align/equation inside $$ (use aligned); no math in headings; no skipped heading
levels; fenced lines <= 89 chars; no '|' inside table cells; Greek only inside math
unless the tooling agent's extension supports prose Greek (check); no literal $.
