# Revision/lead_checks — the lead's independent checks

Written by the lead from scratch; they import no other Revision code (they read only the fixture
`Revision/algebra/gammas.json`, and `einstein_gauss_bonnet_a4.py` reads the record it compares,
`Revision/field_equations_a4/a4-equations.json`).  They check, independently of the Wolfram and sympy records of
`Revision/theory`, `Revision/field_equations_a4` and `Revision/kohn_sham`, facts those records use.

**Metric.** Since 2026-10-16 all three use the corrected primordial metric (version 2; `Revision/SPEC.md` section 1,
`Revision/metric_warped/`), g = diag(e^{-2 a4} b4 cot^2 z, e^{2 a4} (x3), -1, -e^{-2 a4} b4 (sin^2 z)^{1/6} (x3)),
z = 6 H x0, for general functions a4(x4) and b4(x4) > 0 and EVERY real z with sin z cos z != 0 (x0 is space-like, x4 the
time; (sin^2 z)^{1/6} is the positive branch).  Each statement is computed for both signs of sin z, writing
(sin^2 z)^{1/6} = (s sin z)^{1/3} with s = sign sin z (no Abs or sign function appears), so the two cases cover every
real z.  The coordinates are the author's x0..x7.  (Until 2026-10-16 they used the metric of 2026-10-14, now withdrawn.)

## Divergence of the energy-momentum tensor and the gravity term

| check | statement |
|---|---|
| `divergence_x4_component` | nabla_mu T^mu_x4 = -d rho/d x4 - 3 a4' (rho + p3) - 3 h4 (rho + p_t) - h4 (rho + p0), h4 = b4'/(2 b4) - a4', for a diagonal source |
| `divergence_x0_component` | nabla_mu T^mu_x0 = d p0/d x0 + 3 H cot z (p0 - p_t), z = 6 H x0 |
| `divergence_other_components_zero` | the other six components vanish identically |
| `ks_coordinate_jacobian`, `ks_coordinate_form` | in y = ln\|sin z\|/(6H) the x0 component is cot z [p0'(y) + 3 H (p0 - p_t)] |
| `fixture_clifford`, `vielbein_reproduces_metric` | the inputs (e^x0 = e^{-a4} b4^{1/2} cot z, signed) |
| `gamma_Omega_equals_hidden_block_terms` | gamma^mu Omega_mu = (3/2) H e^{a4} b4^{-1/2} gamma^(x0) + (b4'/b4 - a4'/2) gamma^(x4) exactly, from the canonical spin connection |
| `gamma_Omega_divergence_formula` | the same from (1/2) gamma^a (1/sqrt\|g\|) d_mu (sqrt\|g\| e_a^mu) |
| `negative_control_growing_block` | with the block (x0, x5, x6, x7) growing like 3-space the a4' coefficient of the gamma^(x4) term is +7/2 instead of -1/2 |

```
python Revision/lead_checks/emt_divergence_and_spin_connection.py
```

writes `reports/emt-divergence-and-spin-connection.json` (deterministic, LF; about 8 s; 10 checks).

## The a4 and b4 field equations (Einstein and Gauss-Bonnet)

`einstein_gauss_bonnet_a4.py` (about 4 s, 12 checks; an exact ring calculus of its own: t = |sin z|^(1/6), c = cos z
with c^2 = 1 - t^12, sin z = s t^6, e = e^(a4), q = b4^(1/2), u = b4'/b4, v = u') recomputes the Einstein tensor of the
corrected metric for general a4(x4) and b4(x4) and compares it with `Revision/field_equations_a4/a4-equations.json`:
G^mu_nu is diagonal, independent of x0, isotropic in 3-space and equal on x0 and the three extra times (so p0 = p_t), and
depends on a4, b4 only through a4', a4'', u, v and k = e^{2 a4}/b4; the constraint, space and hidden components and the
null combinations (kappa (rho + p0) = -(3/2)(2 H^2 k + 4 a4'^2 - a4' u + v)) agree with the record; the flat member
a4 = 0, b4 = H^2 (x4 - c)^2 is a vacuum; no exponential history a4 = A H x4 + a0, b4 = b4(0) e^(beta A H x4) is a vacuum
of the Einstein equations; for the exponential history the Gauss-Bonnet tensor from the CLASSICAL Lanczos formula
(independent of the GKD route) is diagonal and reproduces the alpha_2 terms of the record's required source rho, p3, p0,
p_t exactly, and G the alpha_1 terms.

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
exact matrix identities; the U(1) Noether identity in the corrected metric is reduced exactly to a 16 x 16 matrix
identity and verified for both signs of sin z, so the LOCAL law d_mu(sqrt|g| J^mu) = 0 (sqrt|g| = e^{-a4} b4^2 |cot z|
(sin^2 z)^{1/4}) holds on shell; the total charge Q = Int sqrt|g| Psi^dagger B Psi d^7x over an interval of z between
degenerate points is constant only if no charge flows through its ends (constancy of Q is not established).  The
quantised bilinears keep the classical anticommuting signs: normal ordering subtracts a number and adds no sign (an
earlier version of the detail text said the opposite; corrected 2026-10-08).  For the QUANTISED Grassmann field the
conjugation that preserves the canonical anticommutator {Psi, Psi^dagger} = B delta is Psi -> Gamma Psi^{dagger T}
(M B^T M^dagger = B holds for M = Gamma and fails, = -B, for M = 1): it reverses the mass.

```
python Revision/lead_checks/charge_conjugation_and_u1.py
```

Every report is deterministic (LF); `Revision/tests/test_lead_checks.py` runs the three scripts and requires their
committed reports byte for byte.
