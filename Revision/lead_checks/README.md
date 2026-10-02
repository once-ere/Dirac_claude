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
