# Revision/lead_checks — the lead's independent checks

Written by the lead from scratch; they import no other Revision code (they read only the fixture
`Revision/algebra/gammas.json`).  They check, independently of the Wolfram and sympy records of
`Revision/theory`, `Revision/field_equations_a4` and `Revision/kohn_sham`, three facts those records use:

| check | statement |
|---|---|
| `divergence_x4_component` | nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t) for the homogeneous diagonal source |
| `divergence_x8_component` | nabla_mu T^mu_x8 = d p8/d x8 + 3 H cot z (2 p8 - p3 - p_t), z = 6 H x8 |
| `divergence_other_components_zero` | the other six components vanish identically |
| `ks_coordinate_jacobian`, `ks_coordinate_form` | in y = ln(sin z)/(6H) the x8 component is cot z [p8'(y) + 6 H p8 - 3 H (p3 + p_t)], the form the Kohn-Sham solver checks (`emt_y_conservation_*`) |
| `fixture_clifford`, `vielbein_reproduces_metric` | the inputs |
| `gamma_Omega_equals_3H_gamma8` | gamma^mu Omega_mu = 3 H gamma^(x8) exactly, from the canonical spin connection |
| `gamma_Omega_divergence_formula` | the same from (1/2) gamma^a (1/sqrt|g|) d_mu (sqrt|g| e_a^mu) |
| `negative_control_inflating_extra_times` | with inflating extra times an a4' gamma^(x4) term survives: the cancellation is due to the deflation |

```
python Revision/lead_checks/emt_divergence_and_spin_connection.py
```

writes `reports/emt-divergence-and-spin-connection.json` (deterministic, LF; about 6 s).

## The a4 field equations (Einstein and Gauss-Bonnet)

`einstein_gauss_bonnet_a4.py` (about 15 s) recomputes, with its own curvature code, the Einstein tensor of the
author's metric for a general a4(x4) and compares it with `Revision/field_equations_a4/a4-equations.json`
(15 checks): G^mu_nu is diagonal, isotropic in 3-space and in the extra times, and independent of x8; the
constraint, space, extra-time, hidden and evolution equations agree with the record (ratio exactly 1);
kappa (rho + p8) = -6 (a4'^2 + H^2) < 0 (the null energy condition fails along x8); a zero source has no
real solution for H > 0 and any Lambda (the vacuum system's only solutions are a4' = +-i H, Lambda = -18 H^2);
for the linear member a4 = A H x4 the Gauss-Bonnet tensor from the CLASSICAL Lanczos formula (independent of
the GKD route) reproduces the alpha_2 terms of the record's rho and p exactly, and G the alpha_1 terms.

```
python Revision/lead_checks/einstein_gauss_bonnet_a4.py
```

## Charge conjugation is a MATRIX; U(1) charge conservation

`charge_conjugation_and_u1.py` (about 9 s, 12 checks).  The author's gammas are real, so for a REAL field plain
complex conjugation is the identity and cannot be charge conjugation (a statement of the lead's of 2026-10-02 that
said otherwise was wrong and is corrected here).  Charge conjugation is the matrix map Psi^c = calC Psibar^T =
calC C Psi*.  Solving exactly for every matrix that maps solutions to solutions gives two one-dimensional families:
calC_+ = C (the author's sigma16; calC_+^-1 gamma^a calC_+ = -(gamma^a)^T; same mass; Psi^c = Psi*) and
calC_- = Gamma C (calC_-^-1 gamma^a calC_- = +(gamma^a)^T; mass reversed; Psi^c = Gamma Psi*).  Both reality
(Majorana) conditions are consistent.  For REAL commuting fields J = 0 identically and calC_+ is the identity (a
real field is its own conjugate); the nontrivial real matrix map is Gamma with (m, lambda) -> (-m, -lambda), which
reverses J and the kinetic term (theorem T1).  The bilinears' signs for commuting and Grassmann components are
exact matrix identities; the U(1) Noether identity in the author's metric is reduced exactly to a 16 x 16 matrix
identity and verified, so the charge Q = Int cos z Psi^dagger B Psi d^7x is conserved on shell.  For the QUANTISED Grassmann field the
conjugation that preserves the canonical anticommutator {Psi, Psi^dagger} = B delta is Psi -> Gamma Psi^{dagger T}
(M B^T M^dagger = B holds for M = Gamma and fails, = -B, for M = 1): it reverses the mass.

```
python Revision/lead_checks/charge_conjugation_and_u1.py
```
