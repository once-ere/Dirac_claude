# MATTER–ANTIMATTER SPEC (binding; 2026-09-30)

## 0. The request and the honesty rule

The user: "Prove that this theory solves current matter anti-matter mysteries. ... Write
out and record (also provide .md, .tex, and .pdf provenance files) for this proof."

The statement cannot be proved, because within the theory as built its central part is
false: the dirac16complex Lagrangian (both statistics) is invariant under the phase
transformation Psi -> e^{i alpha} Psi, so the charge Q = integral of j^4 is conserved in
every gravitational field, and no dynamics of the theory can create a net charge inside a
universe (Sakharov's first condition fails for this charge).  The deliverable is therefore
the exact, correct analysis: everything that CAN be proved about matter and antimatter in
this theory, with proofs and machine checks, and a precise statement of what the "pair of
universes" picture can and cannot explain, under explicitly labelled hypotheses.  Never
write "proved" for anything not proved; never present the conditional scenario as a result.

## 1. Background to present from zero (with literature citations, no numbers invented)

The observed baryon asymmetry (the baryon-to-photon ratio eta ~ 6e-10 from the cosmic
microwave background and big-bang nucleosynthesis; cite the Planck 2018 cosmological
parameters paper, Astron. Astrophys. 641, A6 (2020), for Omega_b h^2), the absence of
antimatter domains, Sakharov's three conditions (A. D. Sakharov, JETP Lett. 5, 24 (1967)):
baryon-number violation, C and CP violation, departure from thermal equilibrium; why the
Standard Model's CP violation is insufficient (state as literature consensus, cited); the
universe/anti-universe class of ideas (L. Boyle, K. Finn, N. Turok, "CPT-Symmetric
Universe", Phys. Rev. Lett. 121, 251301 (2018)) as the known example of a "pair" picture.

## 2. Theorems to prove exactly (Wolfram + independent sympy), both fields

M1 (exact U(1) and charge conservation). L of STAGE5_SPEC (L1) is invariant under
   Psi -> e^{i alpha} Psi for every U(S); Noether current j^mu = Psibar gamma^mu Psi;
   nabla_mu j^mu = 0 on shell in any gravitational field (cite the Stage-1 checks and
   re-verify); Q conserved.  Consequence: no process of the theory changes Q inside one
   universe.  Also: the Kohn–Sham states of Stages 4/5 have fixed N (the chemical potential
   fixes Q).
M2 (discrete symmetries). Determine exactly, for both statistics, which charge conjugation
   (Psi -> M Psi^* or M Psibar^T with a constant 16x16 M), parity-like reflections (Pin
   elements with coordinate reflections) and time reversal leave L invariant or map it to
   -L; whether L is C-invariant and CP-invariant (with the Pin(4,4) meaning of P); the
   CPT-like combination.  Record exactly which symmetries hold; a C- and CP-invariant L
   fails Sakharov's second condition.
M3 (charge-violating terms allowed by the symmetry). Classify all constant 16x16 matrices
   M for which the bilinear Psi^T M Psi (and Psi^T M gamma^a D_a Psi) is invariant under
   Spin(4,4) (and under Pin(4,4) with its characters): solve S^{ab T} M + M S^{ab} = 0
   exactly; for Grassmann Psi the mass-type bilinear survives only for antisymmetric M,
   for commuting Psi only for symmetric M; determine which invariant "Majorana-type" terms
   exist for each statistics (they would violate the U(1) charge: Psi^T M Psi has charge 2).
   This is what the theory would need to add to meet Sakharov's first condition; state it
   as a classification, not as a claim that such a term is present or natural.
M4 (the pair). From Stage 5 T1: under Psi -> gamma^8 Psi, j^mu -> -j^mu, so the gamma^8
   partner universe carries charge -Q; the pair's total charge is 0 and (classical
   bilinears) its total energy-momentum is 0.  Use the Stage-5 exact Krein-level result
   (artifacts/dirac16complex/pair-creation/pairing-theory.json, PAIR_T1krein) to state
   exactly how particles and antiparticles (positive- and negative-norm / hole states) of
   the +M universe map to states of the -M universe; if that report is not final, state the
   field-level result only and mark the Krein-level mapping OPEN.
M5 (the conditional scenario, as a labelled HYPOTHESIS with an exact consequence). IF (H1)
   our universe is one member of a gamma^8 pair created together, (H2) the creation assigns
   Q_+ = -Q_- != 0, and (H3) the dirac16complex charge is identified with baryon number
   (or B-L), THEN the total charge of the pair vanishes and the excess seen in one member is
   exactly compensated by the other (a global symmetry with local asymmetry).  Prove the
   implication (trivial given M1, M4) and state plainly that H1-H3 are assumptions, that the
   theory contains no Standard-Model baryons (H3 is not derivable), that nothing here
   computes Q_+ (H2 is not derived), that a creation process is not computed (H1), and that
   the observed value eta ~ 6e-10 is NOT predicted.
M6 (Sakharov scorecard). A table: condition / status in the theory as built (with the
   theorem) / what would have to be added.

## 3. Deliverables

* wolfram/Dirac16ComplexMatterAntimatter.wl + scripts/verify_dirac16complex_matter_antimatter.wls
  -> artifacts/dirac16complex/matter-antimatter/wolfram-matter-antimatter-report.json
* scripts/check_dirac16complex_matter_antimatter.py (independent sympy) ->
  .../python-matter-antimatter-report.json, tests/test_d16c_matter_antimatter.py
* provenance/DIRAC16COMPLEX_MATTER_ANTIMATTER.{md,tex,pdf} (registered, pinned in
  tests/test_d16c_matter_antimatter_publication.py): title "Matter and antimatter in the
  dirac16complex theory: what can be proved"; sections: summary (the honest answer first),
  the problem from zero, the theorems M1-M5 with proofs, the Sakharov scorecard M6, what
  would be needed, verification records, reproduction commands, non-claims.
* The textbook chapter 17 (TEXTBOOK_SPEC) must agree with this document.
