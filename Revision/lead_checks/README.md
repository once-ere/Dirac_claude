# Revision/lead_checks — the lead's independent checks

Written by the lead from scratch; they import no other Revision code (they read only the fixture
`Revision/algebra/gammas.json`).  They check, independently of the Wolfram and sympy records of
`Revision/theory`, `Revision/field_equations_a4` and `Revision/kohn_sham`, three facts those records use:

**Metric.** Since 2026-10-15 all three use the author's metric with b4(x4) for GENERAL functions a4(x4) and
b4(x4) > 0 (the user's orders "b4 is a function of x4; b4 is NEVER 1" and "move everything to b4(x4)"; until then
they used the withdrawn metric b4 = 1); the coordinates are the author's x0..x7.

| check | statement |
|---|---|
| `divergence_x4_component` | nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (p3 - p_t) - (3/2)(b4'/b4)(rho + p_t) for the homogeneous diagonal source |
| `divergence_x0_component` | nabla_mu T^mu_x0 = d p0/d x0 + 3 H cot z (2 p0 - p3 - p_t), z = 6 H x0 |
| `divergence_other_components_zero` | the other six components vanish identically |
| `ks_coordinate_jacobian`, `ks_coordinate_form` | in y = ln(sin z)/(6H) the x0 component is cot z [p0'(y) + 6 H p0 - 3 H (p3 + p_t)], the form the Kohn-Sham solver checks (`emt_y_conservation_*`) |
| `fixture_clifford`, `vielbein_reproduces_metric` | the inputs |
| `gamma_Omega_equals_3H_gamma0_plus_b4_term` | gamma^mu Omega_mu = 3 H gamma^(x0) + (3/4)(b4'/b4) gamma^(x4) exactly, from the canonical spin connection |
| `gamma_Omega_divergence_formula` | the same from (1/2) gamma^a (1/sqrt(det g)) d_mu (sqrt(det g) e_a^mu) |
| `negative_control_inflating_extra_times` | with inflating extra times an a4' gamma^(x4) term survives: the cancellation of the a4' terms is due to the deflation |

```
python Revision/lead_checks/emt_divergence_and_spin_connection.py
```

writes `reports/emt-divergence-and-spin-connection.json` (deterministic, LF; about 6 s).

## The a4 field equations (Einstein and Gauss-Bonnet)

`einstein_gauss_bonnet_a4.py` (about 3 s; an exact ring calculus of its own: t = sin(z)^(1/6), c = cos z with
c^2 = 1 - t^12, e^(a4), b4^(1/2), u = b4'/b4, v = u') recomputes the Einstein tensor of the author's metric for general
a4(x4) and b4(x4) and compares it with `Revision/field_equations_a4/a4-equations.json` (14 checks): the diagonal of
G^mu_nu is independent of x0 and isotropic in 3-space and in the extra times, the only off-diagonal components are
G^x4_x0 = (3/2) H cot z b4'/b4 and G^x0_x4 = -(3/2) H tan z b4'/b4; the constraint, space, extra-time, hidden and
off-diagonal equations agree with the record; kappa (rho + p0) = -6 H^2 - 3 a4'^2 - (3/4)(u - 2 a4')^2 - (3/2) v
(negative wherever v >= 0); a zero source has no solution for H > 0 (the x4-x0 component forces b4' = 0, then
6 a4'^2 + 6 H^2 = 0); for the exponential history a4 = A H x4, b4 = b4(0) e^(beta A H x4) the Gauss-Bonnet tensor
from the CLASSICAL Lanczos formula (independent of the GKD route; all index sums, since the Ricci tensor is not
diagonal) reproduces the alpha_2 terms of the record's rho, p3, p_t, p0 and q40 exactly, and G the alpha_1 terms.

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
exact matrix identities; the U(1) Noether identity in the author's metric with b4 is reduced exactly to a 16 x 16 matrix
identity and verified, so the LOCAL law d_mu(sqrt|g| J^mu) = 0 (sqrt|g| = b4^(3/2) cos z) holds on shell; the total charge Q = Int sqrt|g| Psi^dagger B Psi d^7x
of a slice is constant only if no charge flows through its boundary, and at the brane z = pi/2 the flow is not zero in general
(constancy of Q is not established).  The quantised bilinears keep the classical anticommuting signs: normal ordering subtracts
a number and adds no sign (an earlier version of the detail text said the opposite; corrected 2026-10-08).  For the QUANTISED Grassmann field the
conjugation that preserves the canonical anticommutator {Psi, Psi^dagger} = B delta is Psi -> Gamma Psi^{dagger T}
(M B^T M^dagger = B holds for M = Gamma and fails, = -B, for M = 1): it reverses the mass.

```
python Revision/lead_checks/charge_conjugation_and_u1.py
```
