# Stage 2 specification — dirac16complex in the primordial (pair-creation) field

Binding: CONTRACT.md (as corrected by the Stage-1 reports; where a Stage-1 report
records a contract problem, the report's measured truth wins) and CONTRACT §9.

Primordial field (the notebook's `MatrixMetric44`), zero-based coordinates
x0..x7, z = 6 H x0 ∈ (0, π/2), t = H x4, a4 = arbitrary smooth function:
  g = diag(cot²z, s^{1/3}e^{2a4(t)} ×3, -1, -s^{1/3}e^{-2a4(t)} ×3),  s = sin z,
  vielbein h = (cot z, s^{1/6}e^{a4} ×3, 1, s^{1/6}e^{-a4} ×3) (diagonal gauge).
Warped form (verify): with ζ := ln(sin z)/(6H) ∈ (-∞, 0),
  ds² = dζ² - dx4² + e^{2Hζ}[e^{2a4} (dx1²+dx2²+dx3²) - e^{-2a4}(dx5²+dx6²+dx7²)].

Required exact results (each a named check, Wolfram + independent Python/sympy):
P_metric       g = e η e^T, signature (4,4), det g = -cos²z·(...) ⇒ √|g| = cos z.
P_zeta         the warped form above (coordinate change x0 -> ζ).
P_christoffel  complete list of nonzero Γ^ρ_μν (count and closed forms).
P_spinconn     complete list of the 24 nonzero ω_μab (closed forms), antisymmetry,
               vielbein postulate (512 components).
P_Omega        the eight 16×16 matrices Ω_μ in closed form (block form in the
               notebook basis) and γ^μΩ_μ = 3Hγ^0 (a4-independent).
P_gammaConst   D_μγ^ν = 0; notebook contraction fails (measured violation).
P_EL           the Euler–Lagrange equations γ^μD_μΨ = (m + U'(S))Ψ written
               component by component for Ψ_0..Ψ_15 with dependence on all eight
               coordinates, each equation an explicit linear combination of
               ∂_0..∂_7 of named components with coefficients tan z, s^{-1/6}e^{∓a4},
               3H, m + λS; verified against the covariant operator.  Also the
               x0 form and the ζ form.
P_blocks       for fields depending on (x0,x4) only: the equations split into four
               blocks of four components; compare the coupling sets with the
               notebook's {0,5,8,13},{1,4,9,12},{2,7,10,15},{3,6,11,14}.
P_notebookCompare  rebuild the notebook's own La[] (commuting fields, the notebook
               contraction, its ωμIJ/spinCoefficients) and reproduce its cell-1137
               block equations (with q = Q1 sinh(a4) a4' e^{-a4}); identify the origin
               of every term that differs from the correct equations (in particular
               the q term).  If exact reproduction is not achieved, say so and give
               the closest reproduction and the residual.
P_EMT          {γ_μ,Ω_ν}+{γ_ν,Ω_μ} for all μ ≤ ν (nonzero list); T_μν of CONTRACT §7
               in terms of bilinears for this field; homogeneous sector
               (k = q = 0, ζ-plane waves Ψ = e^{-3Hζ}e^{iKζ}u(t)):
               ρ, p_(i) for every transverse direction, KE_L, PE_L, KE_H, PE_H, w,
               frozen in x4, a4-independent; conservation.
P_modes        exact reduction γ^4 u̇ = (M_eff - iKγ^0)u, E² = M_eff² + K²;
               k ≠ 0 modes are not separable (the product e^{-Hζ}e^{-a4(t)}) — say
               so; q ≠ 0 modes: local E² = M² + K² + (k e^{-Hζ-a4})² - (q e^{-Hζ+a4})²
               (WKB, stated as local) and onset of the instability.
P_einstein     Ricci scalar R = 6H²(a4'² - 7); G^μ_ν diagonal (closed forms); the
               source required by 8D Einstein gravity: ρ_req = -3H²(7 + a4'²)/κ < 0,
               pressures; for a4 = t: ρ = -24H²/κ, isotropic p = 12H²/κ, w = -1/2;
               energy conditions violated/satisfied (list).  The dirac16complex
               homogeneous condensate has S ∝ 1/sin z and cannot supply it — prove.
P_quant        canonical quantization in this field: Π = √|g|Ψ^†Cγ^4 with √|g| = cos z;
               {Ψ_a(x),Ψ_b^†(y)} = B_ab δ^7(x-y)/cos z at equal x4; Hamiltonian
               density written out; good sector (q = 0) Hermitian single-particle
               operator; γ^8 map (±M) in this field.
P_a4linear     specialisation a4 = t (notebook cell 150 alternatives a4' = 2(M±1)/3
               also tabulated): numbers for R, G, ρ_req, p_req.

Relabelled files: wolfram/Dirac16ComplexPrimordial.wl,
scripts/verify_dirac16complex_primordial.wls, scripts/check_dirac16complex_primordial.py,
artifacts/dirac16complex/primordial-field/*.json,
provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.{md,tex,pdf},
tests/test_d16c_primordial.py, scripts/verify_stage2_primordial_field.{ps1,sh}.
Component labels: x0..x7, Ψ_0..Ψ_15 (and the notebook's f16[k], Z[k], yZ[k] cross-
reference table).
