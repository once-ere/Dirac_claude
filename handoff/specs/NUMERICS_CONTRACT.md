# dirac16complex — Stage 3 numerical programme (authoritative)

Extends CONTRACT.md (all its conventions apply).  Everything below is to be solved
with the pure-Rust SUNDIALS 7.8.0 CVODE engine taken from
https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0 (pinned commit
a8fdff459adfe181573d7924b18bffbdf378fdb3; macOS: rustSolveIt_macos-silicon at
5360157f4f6160978f66400566c31b2ae25dd44d; Linux: rustSolveIt_linux at
6f58e02e53717a51375bd4bc5918edc57088d922 — all three vendor the same
byte-identical sundials_rs), cloned by `scripts/setup_solver.{ps1,sh}` into the
git-ignored `vendor/rustSolveIt/`.  The Jupyter notebook is adapted from
`planet_Mercury/notebook/` of that repository (find_binary / run / gauntlet /
run_notebook.py / check_notebook.py).  VERIFIED FACT: none of the three rustSolveIt
repositories contains a Mathematica notebook (.nb/.wl/.wls); the Mathematica
notebook is therefore new, modelled on dirac-main's `notebooks/DiracTriality.nb`
and the verified `RunProcess` + CSV/JSON exchange pattern.  Documentation must say so.

## Physics common to all experiments

Homogeneous diagonal (4,4) backgrounds, t = x4 (lapse 1):
`ds^2 = -dt^2 + Σ_{i∈T} ε_i h_i(t)^2 dx_i^2`, T = {0,1,2,3,5,6,7}, ε = +1 (0..3),
-1 (5..7).  `H_i = ḣ_i/h_i`, `Θ = Σ H_i`, `V = Π h_i` (7-volume).
Groups used: `b` = h_0 (hidden space), `a` = h_1=h_2=h_3 (3-space),
`c` = h_5=h_6=h_7 (extra times).  `Θ = H_b + 3H_a + 3H_c`.
`γ^μ Ω_μ = (1/2) Θ γ^4` (diagonal formula).
Dirac equation for a mode `Ψ = V^{-1/2} e^{i k·x} u(t)` (k along the transverse
directions, flat gammas `γ^j`, coordinate momentum `k_j`):
    γ^4 u̇ + i Σ_j (k_j / h_j) γ^j u = M_eff u,   M_eff = m + U'(S),
    i u̇ = h(t) u,   h(t) = -i M_eff γ^4 - γ^4 Σ_j (k_j/h_j) γ^j.
`h` is Hermitian iff k_5 = k_6 = k_7 = 0 (good sector).  Norms: `u^† u` (Hilbert,
J = B structure) and `u^† B u` (Krein) are both conserved in the good sector;
only the Krein norm is conserved in general.
Mean-field condensate: `S = ⟨:Ψbar Ψ:⟩ ∝ 1/V` EXACTLY (for any M_eff(t)).
Energy–momentum per mode (derived in Stage 1, must be re-derived by the checker):
`ε(u) = u^† h u`, `p_j(u) = -(k_j/h_j) u^† γ^4 γ^j u` (no sum; equals
`(k_j/h_j)^2 / E` on adiabatic eigenmodes), `s(u) = u^†(-i γ^4)u` (scalar density per
mode, `= M_eff/E` on positive-energy eigenmodes).
Two kinetic/potential splits (both exact operator definitions, report both):
(A) Lagrangian split: `KE_L = (1/2) K_4`, `K_4 = (1/2)(Ψbar γ^4 D_4 Ψ - D_4Ψbar γ^4 Ψ)`,
    `PE_L = ρ - KE_L`.  Homogeneous condensate: `KE_L = (1/2)S(m+U')`,
    `PE_L = (1/2)(mS + 2U - S U')`, `ρ = KE_L + PE_L`, `p = KE_L - PE_L`
    (exact analogue of the scalar-field split in the Gmail PDF).
(B) Hamiltonian split: `PE_H = m Ψbar Ψ + U(Ψbar Ψ)` (rest mass + interaction),
    `KE_H = ρ - PE_H = -(1/2)Σ_{j≠4}(Ψbar γ^j D_j Ψ - D_jΨbar γ^j Ψ)`
    (momentum/gradient energy).  Free gas: `PE_H = Σ n m^2/E`, `KE_H = Σ n k^2/E = Σ_j p_j`.

## EXP-1  Primordial (pair-creation) field — frozen dirac16complex

Background: exact notebook field (CONTRACT §9) with an a4 profile
`a4'(t) = A (1 + tanh((t - t1)/Δ))(1 - tanh((t - t2)/Δ))/4` (primordial window);
two profiles (A=1 and A=2) must give IDENTICAL spinor results (a4 cancels from the
k=q=0 sector).  Sector k=q=0, hidden-space plane wave in ζ = ln(sin z)/(6H):
`Ψ = e^{-3Hζ} e^{iKζ} u(t)` ⇒ `γ^4 u̇ = (M_eff - i K γ^0) u` (verify this reduction
symbolically from the Stage-2 component equations).  Integrate 32 real ODEs
(u ∈ C^16) with CVODE for K ∈ {0, 0.5, 2}, several initial spinors; output
ρ, p_i (i∈T), KE_L, PE_L, KE_H, PE_H, w, u^†u, u^†Bu vs t, plus the Einstein
source the field would need: `ρ_req = -3H^2(7+a4'^2)/κ`,
`p_req,0 = -3H^2(a4'^2-5)/κ`, `p_req,1..3 = H^2(15-3a4'^2+a4'')/κ`,
`p_req,5..7 = H^2(15-3a4'^2-a4'')/κ`.  Also the 3-space scale factor e^{a4},
extra-time factor e^{-a4}, V constant.  Expected: ρ, p frozen (constant to solver
tolerance), identical for both profiles; ρ_req < 0 always.

## EXP-2  Self-consistent 8D Einstein – dirac16complex homogeneous cosmology

κ ≡ κ_8 = 1.  State: ln b, ln a, ln c, H_b, H_a, H_c, u ∈ C^16 (32 reals).
EXPECTATION-VALUE RULE (verified numerically in design): in the positive-norm
(J = B) quantization a one-particle state built on the normalised mode u
(u^†u = 1) has `⟨Ψ^† M Ψ⟩ = u^† B M u` (normal-ordered, relative to the Dirac sea).
Hence scalar density `s(u) = u^† B C u = u^†(-iγ^4)u` (= 1 on positive-energy rest
eigenvectors), energy density `u^† h u`, and NEVER `u^† C u` (which is identically 0
on those eigenvectors).  The condensate is `S = S_0 (V_0/V) s(u)`, with u(0) a
positive-energy rest eigenvector of h; s(u(t)) = 1 must be conserved numerically.
Equations:
`Ḣ_i = -H_i Θ + κ(ρ - p)/6`, `ḣ_i = H_i h_i`, spinor equation above with k=0,
`ρ = mS + (λ/2)S^2`, `p = (λ/2)S^2`.  Constraint `Σ_{i<j} H_i H_j = κ ρ`
(= 3H_bH_a + 3H_bH_c + 3H_a^2 + 3H_c^2 + 9H_aH_c) imposed on initial data
(solve for S_0 given H's, x0 := λS_0/(2m)) and monitored.  Runs:
(i) x0=0 (dust), (ii) x0=-0.4 (attractive), (iii) x0=+0.5 (repulsive);
initial H_a=1, H_c=-0.2, H_b=0 (extra times initially deflating).
Output all states, ρ, p, w, KE_L, PE_L, Θ, constraint residual, the bound
`Θ^2 - 3H_a^2 - 2κρ ≥ 0`, and the 3-space-inferred
`w_eff = -1 + (Θ/(3H_a))(1 + w)`.  Expected: anisotropy ∝ 1/V decays, extra times
turn to expansion, Θ > √3 H_a ⇒ w_eff > -1 + 1/√3 for dust.

## EXP-3  4D-effective late universe: dirac16complex condensate as dark energy

Stabilised extra dimensions (b, c constant): S ∝ a^{-3}.  Units H0 = 1,
ρ in units of 3H0^2/κ_4.  `E^2 = Ω_r a^{-4} + Ω_m a^{-3} + ρ_ψ`,
`ρ_ψ = Ω_ψ σ(1 + x0 σ)/(1 + x0)`, σ = S/S_0 = a^{-3} (exact), `w = x0σ/(1+x0σ)`,
`KE_L = (Ω_ψ/2)σ(1+2x0σ)/(1+x0)`, `PE_L = (Ω_ψ/2)σ/(1+x0)`,
`KE_H = 0`, `PE_H = ρ_ψ`.  Ω_r = 0.00009, Ω_m = 0.305, Ω_ψ = 0.69491.
Integrate in N = ln a from N=0 down to N=ln(1/3.5) and up to N=ln 2 with CVODE:
state (u = H0 t, D_C comoving distance, u ∈ C^16 spinor with reduced frequency
μ = M_eff/H0 ∈ {3, 7} to demonstrate phase independence, ln σ).
`dσ/dN = -3σ` must be reproduced from the spinor's scalar density.  Runs:
x0 ∈ {-0.4627 (w0 = -0.861), -0.4331 (w0 = -0.764), -0.3, -0.2, 0 (dust)} and a
fine scan x0 ∈ [-0.49, 0] (Python may do the scan from closed forms, Rust the
canonical runs).  Diagnostics: w(a), ρ_ψ(a) sign change (a = |x0|^{1/3}), w = -1
crossing (a = (2|x0|)^{1/3}), deceleration q(a), distance modulus μ(z); fits:
(1) tangent CPL at a=1: w0 = w(1), wa = -dw/da|_1; (2) least-squares CPL fit of
w(a) on a∈[1/3.26, 1]; (3) least-squares CPL and constant-w fit to the distance
modulus μ(z) on z∈[0.01, 2.26] (implement Nelder–Mead in numpy; no scipy);
compare with Unite: (w0, wa) = (-0.861, -0.60), constant w = -0.764.  Also compute
the CPL model's own μ(z) and the constant-w that best fits it (consistency check of
the -0.764 benchmark as a projection).  Optional variant with extra-time deflation
index γ (c ∝ a^{-γ}, σ = a^{-3(1-γ)}): report the γ that would reproduce the Unite
tangent (w0, wa) and flag the physical objections (8D Einstein bound from EXP-2,
G_N ∝ 1/V_extra variation).

## EXP-4  dirac16complex quanta as dark matter: Fermi gas EoS and pair creation

Background: 3-space FRW, hidden space and extra times static (b=c=1),
q = 0 good sector.  (a) Thermal gas: radiation-dominated `a(t)=(t/t_i)^{1/2}`
then optionally matter; units m = 1; initial comoving temperature T_i = 10 m
(relativistic), `H_i/m` small enough for adiabaticity (e.g. 0.05); momentum grid
k ∈ (0, k_max] (≥ 48 Gauss–Legendre or uniform nodes, k_max ≈ 12 T_i), for each k
integrate u(t) from the instantaneous positive-energy eigenvector (and one
negative-energy eigenvector for the vacuum-subtraction/β diagnostics) with CVODE;
Fermi–Dirac occupation f(k) = 1/(e^{E_i/T_i}+1) ≤ 1 (Pauli), 8 particle + 8
antiparticle states per k.  ρ(a) = (16/(2π^2 a^3)) ∫ k^2 f ε dk, p(a) similarly with
the 3-space pressure; w(a) from 1/3 → 0; compare with the kinetic-theory integrals
(closed-form quadrature in Python) and report max relative deviation; |β_k|^2
(overlap with the instantaneous negative-energy subspace) must stay ≲ 1e-6.
(b) Pair creation: de Sitter 3-space phase H_inf then smooth transition to
radiation (e.g. H(t) = H_inf for t<t_e, a matched radiation law after, or a smooth
tanh blend — specify exactly), vacuum initial state when k/a ≫ H_inf, for
m/H_inf ∈ {0.1, 0.5, 1, 2}: |β_k|^2 spectrum after the transition, produced number
and energy density, and their subsequent EoS (relativistic → dust).  Record that
m=0 gives no production (conformal invariance of the massless mode equation) and
check it numerically (|β|^2 ≤ 1e-10).

## EXP-5  Extra-time sector: the ultrahyperbolic instability

Primordial deflation `c = e^{-Ht}` (H=1), mode with extra-time momentum q (k=0,
m=1): `E^2(t) = m^2 - q^2 e^{2Ht}` turns negative at t* = ln(m/q)/H.  Integrate
from t=0 (q=0.05, 0.1) to t* + 3; output u^†u (grows super-exponentially), u^†Bu
(conserved), and compare the growth with the WKB rate ∫ sqrt(q^2 e^{2Ht} - m^2) dt.
This documents why quantisation and cosmology are restricted to the q=0 sector.

## Software shape

Crate `studies/dirac16complex_cosmology` (edition 2021, `#![forbid(unsafe_code)]`,
`#![deny(warnings)]`), own `[workspace]`, path deps
`../../vendor/rustSolveIt/sundials_rs/crates/{sundials_core,cvode_rs}`,
repo-root `.cargo/config.toml` with `-C target-feature=+fma`.  Gamma matrices
generated from `artifacts/dirac16complex/arbitrary-field/algebra-fixture.json` by
`scripts/generate_dirac16complex_constants.py` into `src/generated.rs` (with the
fixture sha256).  Subcommands: `print-config`, `exp1`, `exp2`, `exp3`, `exp4`,
`exp5`, `all`; flags `--output DIR`, `--rtol`, `--atol`, `--refined`.  Last stdout
line `SUCCESS` / `FAILURE` (planet_Mercury contract).  Deterministic CSV via
`sundials_core::sundials_utils::fmt_e(v, 17)`, LF, header row; `summary.json` per
experiment with solver stats, parameters, fixture hash, verdict.  Outputs under
`artifacts/dirac16complex/numerics/expN/`.  Python checker
`scripts/check_dirac16complex_numerics.py` re-derives every analytic comparison
independently (numpy allowed), checks invariants, finite-difference RHS residuals,
determinism (repeat run byte-identical) and refined-tolerance convergence.
Figures (PNG, matplotlib, deterministic metadata) under
`artifacts/dirac16complex/numerics/figures/`.
