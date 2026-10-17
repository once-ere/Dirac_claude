"""Assemble Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md from KS.draft.md: every @@NAME@@ is filled from the Revision
records (reports, results, READMEs), the table generators of ks_tables.py and the part files ks_*.md.
Usage: fill_ks.py OUT.md"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ks_tables  # noqa: E402

ROOT = Path(r"D:\Developer\github\Dirac_claude")
REV = ROOT / "Revision"
KS = REV / "kohn_sham"
REP = KS / "reports"
draft = (HERE / "KS.draft.md").read_text(encoding="utf-8")


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def checks(p):
    return load(p)["checks"]


def detail(p, name):
    for c in checks(p):
        if c["name"] == name:
            return c["detail"]
    raise KeyError(name)


def grab(p, name, pat):
    m = re.search(pat, detail(p, name))
    assert m, (name, pat)
    return m.group(1)


def count(p):
    c = checks(p)
    n = len(c)
    ok = sum(str(x["verdict"]).upper() == "PASS" for x in c)
    assert ok == n, p
    return n


def g7(v):
    return format(float(v), ".7g")


F = {}
# counts
F["PW"] = str(count(REP / "ks-theory-wolfram.json"))
F["PP"] = str(count(REP / "ks-theory-python.json"))
T3 = REV / "pairing" / "kohn_sham" / "reports"
F["T3W"], F["T3P"] = str(count(T3 / "wolfram-t3.json")), str(count(T3 / "python-t3.json"))
F["T3CW"], F["T3CP"] = str(count(T3 / "wolfram-t3-completion.json")), str(count(T3 / "python-t3-completion.json"))
hist = count(REV / "dark_sector" / "dirac16complex" / "reports" / "ks-history-run.json")
F["HIST_COUNT"] = f"{hist} of {hist}"
cc = load(REP / "ks-crosscheck.json")
F["CC_N"] = str(count(REP / "ks-crosscheck.json"))
F["CC_COMPARISONS"] = str(cc["comparisons"])
F["CC_ABSTRACT"] = f"{F['CC_N']} of {F['CC_N']} checks PASS over {cc['comparisons']} comparisons"
F["DET_N"] = str(count(REP / "ks-rust-determinism.json"))
DET = REP / "ks-rust-determinism.json"
F["DET_E"] = grab(DET, "refined_ground_energies", r"max relative difference of E_KS ([0-9.e+-]+)")
F["DET_LEV"] = grab(DET, "refined_eigenvalues", r"max \|difference\| ([0-9.e+-]+) m")
F["DET_NLEV"] = grab(DET, "refined_eigenvalues", r"(\d+) Kohn-Sham levels")
F["DET_PROF"] = grab(DET, "refined_profiles", r"the largest of their maxima\) ([0-9.e+-]+)")
F["DET_ADIA"] = grab(DET, "refined_adiabatic_derivatives", r"max relative difference ([0-9.e+-]+)")
F["DET_THERMO"] = grab(DET, "refined_thermodynamics", r"\): max ([0-9.e+-]+)")
F["DET_CV"] = grab(DET, "refined_heat_capacity", r"1e-6\)\) ([0-9.e+-]+)")
RS = REP / "ks-rust-solver.json"
F["HF"] = grab(RS, "adiabatic_hellmann_feynman", r"worst value ([0-9.e+-]+)")
F["DSCF"] = grab(RS, "excited_delta_scf_free_equals_gap", r"worst value ([0-9.e+-]+)")
F["RESC_LEV"] = grab(RS, "rescaling_identity_between_slices", r"worst value ([0-9.e+-]+)")
F["RESC_PROF"] = grab(RS, "rescaling_identity_energy_profiles", r"worst value ([0-9.e+-]+)")
F["ROOT_PREC"] = grab(REP / "ks-rust-mermin-roots.json", "root_precision_self_check", r"agree to ([0-9.e+-]+)")
params = load(KS / "results" / "parameters.json")
F["VOL7"] = repr(params["physics"]["Vol7AtA4Zero"])
F["BULK_EDGE"] = repr(params["particleNumbers"]["bulkEdge"])
with open(KS / "results" / "adiabatic" / "adiabaticity.csv", encoding="utf-8", newline="") as h:
    adia = list(csv.DictReader(h))
top = max(adia, key=lambda r: float(r["Q_max"]))
F["QMAX"], F["QMAX_ID"], F["QMAX_PAIR"] = g7(top["Q_max"]), top["id"], top["Q_max_pair"]
n8 = max((r for r in adia if r["N"] == "8"), key=lambda r: float(r["Q_max"]))
F["N8_Q"], F["N8_Q_ID"], F["N8_Q_PAIR"] = g7(n8["Q_max"]), n8["id"], n8["Q_max_pair"]
free8 = next(r for r in adia if r["id"] == "N8_lam0_a00")
F["N8_FREE_Q"] = f"state N8_lam0_a00: {g7(free8['Q_max'])}"
# result tables
for key, fn in ks_tables.TABLES.items():
    F[key.strip("@")] = fn()
# record tables
F["T_RECORDS_2"] = "\n".join([
    "| gammas, $C$, $B$, $\\Gamma$ | `fixture_input`, `clifford_relation`, `C_B_Gamma` | `fixture_input`, "
    "`fixture_python_equals_wolfram`, `clifford_relation`, `C_B_Gamma`, `BC_and_Cg4` |",
    "| hidden coordinate, line element, $\\sqrt{\\lvert g\\rvert}$ | `geometry_hidden_coordinate`, `geometry_line_element`, "
    "`geometry_sqrt_det` | `geometry_hidden_coordinate`, `geometry_sqrt_det`, `geometry_line_element` |",
    "| spin connection | `spin_connection_compatibility`, `spin_connection_slash`, `spin_connection_time_terms`, "
    "`spin_connection_slash_x0_chart` | `spin_connection_compatibility`, `spin_connection_slash`, "
    "`spin_connection_time_terms`, `spin_connection_slash_x0_chart` |"])
F["T_RECORDS_3"] = "\n".join([
    "| ansatz and Hamiltonian | `ansatz_removes_spin_connection`, `ansatz_without_y_factor_term_survives`, "
    "`ansatz_without_x4_factor_term_survives`, `ansatz_norm`, `hamiltonian_16_hermitian` | "
    "`ansatz_removes_spin_connection`, `ansatz_without_y_factor_term_survives`, `ansatz_without_x4_factor_term_survives`, "
    "`ansatz_norm`, `hamiltonian_16_hermitian` |",
    "| blocks | `blocks_commuting_set`, `blocks_basis_unitary`, `blocks_forms`, `blocks_relation_to_Gamma`, "
    "`block_hamiltonian`, `block_ode_equivalent` | `blocks_commuting_set`, `blocks_projectors`, `blocks_basis_unitary`, "
    "`blocks_forms`, `blocks_not_everything_block_diagonal`, `blocks_relation_to_Gamma`, `block_hamiltonian`, "
    "`block_ode_equivalent` |",
    "| symmetries | `block_type_relation`, `block_Gamma_map`, `rotation_invariance` | `block_type_relation`, "
    "`block_Gamma_map`, `rotation_invariance` |",
    "| solver (numerical basis) | | `theory_input_metric_forms`, `block_reduction_numeric`, `gamma_fixture_numeric` "
    "(Rust solver report) |"])
F["T_RECORDS_4"] = "\n".join([
    "| uniform gas and exchange | `gas_mode_projector`, `gas_angular_average`, `gas_densities`, `exchange_uniform_gas` | "
    "`gas_mode_projector`, `gas_angular_average`, `gas_negative_energy_modes`, `gas_densities`, `hf_wick_contraction`, "
    "`exchange_uniform_gas`, `filled_shell_ratio` |",
    "| Kohn-Sham potentials | `ks_potentials`, `ks_onshell_lagrangian` | `ks_potentials`, `ks_onshell_lagrangian`, "
    "`ks_theory_json_exchange` |",
    "| coupling, cell volume and history | `ks_coupling_volume_scaling`, `history_solver_units` | "
    "`ks_coupling_volume_scaling`, `history_solver_units` |",
    "| exact Fock exchange of the slab | `exchange_slab_exact_fock` | `exchange_slab_exact_fock` |"])
F["T_RECORDS_5"] = "\n".join([
    "| boundary conditions (Wolfram and sympy) | `bc_fold_same_equation_on_both_halves`, `bc_fold_conditions`, "
    "`bc_self_adjoint_boundary_term`, `bc_tip_family`, `bc_current_conserved_along_y`, `bc_exact_k0_spectra`, "
    "`bc_tip_asymptotics`, `brane_band_slope` |",
    "| free problem (Rust solver) | `free_k0_analytic_spectra`, `free_zero_mode_exact`, `free_brane_band_slope`, "
    "`free_block_type_symmetries`, `free_particle_branch_labels`, `free_tip_angle_boundary_identity` |",
    "| free problem and parameters (reference) | `free_k0_analytic_spectra`, `free_convergence_order_two`, "
    "`free_k0_block_type_symmetry`, `free_zero_mode`, `free_brane_band_slope`, `free_particle_branch`, "
    "`parameters_closed_shells`, `parameters_calibration`, `richardson_asymptotic_ratio`, `richardson_uncertainty_validated` |",
    "| parameters (cross-check) | `problem_definition_identical`, `parameters_particle_numbers`, `parameters_couplings` |"])
F["T_RECORDS_6"] = "\n".join([
    "| ground states | `ground_runs_completed`, `ground_scf_converged`, `ground_closed_shell`, `ground_window_complete`, "
    "`ground_N_conservation`, `ground_energy_two_forms`, `ground_orbital_boundary_conditions` | `ground_scf_converged`, "
    "`ground_a4_neighbours_tight`, `ground_grid_consistency`, `ground_closed_shell`, `ground_window_complete`, "
    "`ground_N_conservation`, `ground_energy_two_forms` | `ground_occupations_and_groups`, `ground_energies`, "
    "`ground_homo_lumo_gap`, `ground_eigenvalues`, `ground_profiles` |",
    "| first excited state | `excited_delta_scf_free_equals_gap`, `excited_scf_converged` | "
    "`excited_delta_scf_free_equals_gap`, `excited_particle_hole_lowest_is_gap` | `excited_delta_scf`, "
    "`excited_particle_hole_lists` |",
    "| exact-Fock variant | `exx_variant_scf_converged`, `exx_variant_y_conservation`, `exx_variant_occupation_order` | "
    "`exx_scf_converged`, `exx_N_conservation`, `exx_energy_two_forms`, `exx_emt_energy_integral`, "
    "`exx_y_conservation_integrated` | `exchange_delta_E_x`, `exx_variant_scf` |",
    "| SCF path (information) | `thermo_scf_path` | `scf_paths` | |"])
F["T_RECORDS_9"] = (
    "| tensor and identities | `emt_orbital_components`, `emt_trace_identity`, `emt_y_conservation_orbital`, "
    "`emt_y_conservation_selfconsistent`, `emt_x4_component`, `emt_energy_change_history` | `emt_energy_integral`, "
    "`emt_trace_derivative_form`, `emt_y_conservation_integrated`, `emt_y_conservation_pointwise`, "
    "`emt_energy_change_dE_da4` | `emt_energy_integral`, `emt_y_conservation_integrated`, `emt_energy_change_dE_da4`, "
    "`emt_integrals`, `emt_brane_tip_values` |")
# the cross-check table (three columns)
names = [c["name"] for c in checks(REP / "ks-crosscheck.json")]
rows = ["| check | check | check |", "| --- | --- | --- |"]
for i in range(0, len(names), 3):
    part = names[i:i + 3] + [""] * (3 - len(names[i:i + 3]))
    rows.append("| " + " | ".join(f"`{n}`" if n else "" for n in part) + " |")
F["CC_TABLE"] = "\n".join(rows)
# the count table
COUNTED = ("Revision/kohn_sham/reports/ks-theory-wolfram.json", "Revision/kohn_sham/reports/ks-theory-python.json",
           "Revision/kohn_sham/reports/ks-rust-solver.json", "Revision/kohn_sham/reports/ks-rust-determinism.json",
           "Revision/kohn_sham/reports/ks-rust-mermin-roots.json", "Revision/kohn_sham/reports/ks-reference.json",
           "Revision/kohn_sham/reports/ks-crosscheck.json", "Revision/field_equations_a4/reports/ks-source-conditions.json",
           "Revision/field_equations_a4/ks_source/reports/ks-source-a4.json",
           "Revision/field_equations_a4/reports/wolfram-a4-report.json",
           "Revision/field_equations_a4/reports/python-a4-report.json", "Revision/pairing/kohn_sham/reports/wolfram-t3.json",
           "Revision/pairing/kohn_sham/reports/python-t3.json", "Revision/kohn_sham/tip_convergence/tip-convergence.json")
rows = ["| report | checks | PASS | FAIL |", "| --- | --- | --- | --- |"]
for rel in COUNTED:
    n = count(ROOT / rel)
    rows.append(f"| `{rel}` | {n} | {n} | 0 |")
F["COUNT_TABLE"] = "\n".join(rows)
# parts
for key, name in (("TIP_5", "ks_tip_5.md"), ("SOURCE_11", "ks_source_11.md"), ("REVERIFY", "ks_reverify.md"),
                  ("RUNTIMES_14", "ks_runtimes.md")):
    F[key] = (HERE / name).read_text(encoding="utf-8").strip("\n")
tip15 = (HERE / "ks_tip_15.md").read_text(encoding="utf-8")
for block in re.split(r"(?m)^(?=@@TIP_)", tip15):
    if block.strip():
        head, body = block.split("\n", 1)
        F[head.strip().strip("@")] = body.strip("\n")
out = draft
for key, val in F.items():
    tag = "@@" + key + "@@"
    assert tag in out, tag
    out = out.replace(tag, val)
left = sorted(set(re.findall(r"@@[A-Z0-9_]+@@", out)))
assert not left, left
Path(sys.argv[1]).write_text(out, encoding="utf-8", newline="\n")
print("wrote", sys.argv[1], len(out.splitlines()), "lines")
