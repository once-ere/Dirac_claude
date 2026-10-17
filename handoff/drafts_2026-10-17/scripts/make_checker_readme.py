"""W5: write Revision/kohn_sham/checker/README.md from scratchpad/checker_readme_draft.md, the cross-check report of this
run (reports/ks-crosscheck.json) and the measured times (scratchpad logs).  Every number of the results is parsed from
the report; the run fails loudly if a pattern is missing.
Usage: make_checker_readme.py - STEPLOG (the step log of run_h15.sh)"""
import json
import re
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
KS = Path(r"D:\Developer\github\Dirac_claude\Revision\kohn_sham")
t = (S / "checker_readme_draft.md").read_text(encoding="utf-8")
rep = json.loads((KS / "reports" / "ks-crosscheck.json").read_text(encoding="utf-8"))
C = {c["name"]: c for c in rep["checks"]}
n = rep["summary"]["checks"]
assert rep["summary"]["pass"] == n and rep["summary"]["fail"] == 0, rep["summary"]
PAT = re.compile(r"(\d+) comparisons; worst \|diff\|/tolerance ([0-9.e+-]+) \(([^)]*)\)")


def cmpinfo(name):
    m = PAT.search(C[name]["detail"])
    assert m, name
    return int(m.group(1)), m.group(2), m.group(3)


def grab(name, pat):
    m = re.search(pat, C[name]["detail"])
    assert m, (name, pat)
    return m.groups() if len(m.groups()) > 1 else m.group(1)


def sub(a, b):
    global t
    assert t.count(a) == 1, (t.count(a), a[:70])
    t = t.replace(a, b)


nlev = cmpinfo("ground_eigenvalues")[0]
nprof = cmpinfo("ground_profiles")[0]
sub("the 9616 levels and 113250\nprofile points are aggregated in the report only)",
    f"the {nlev} levels and {nprof}\nprofile points are aggregated in the report only)")
sub("@@NS2@@ --jobs 20    # i = 1..@@NS2@@", "6 --jobs 20    # i = 1..6")

bullets = []
for name, what in (("ground_energies", "E_KS, E_band, E_int"), ("ground_homo_lumo_gap", "HOMO, LUMO, gap"),
                   ("ground_eigenvalues", "levels label by label"), ("excited_delta_scf", "Delta-SCF and E_excited"),
                   ("emt_integrals", "EMT integrals"), ("emt_brane_tip_values", "fold and tip values"),
                   ("ground_profiles", "profile points"), ("exchange_delta_E_x", "Delta E_x"),
                   ("adiabatic_dE_da4", "dE/da4 in both forms"), ("adiabatic_Q_max", "Q_max, its pair, matrix element and level spacing"),
                   ("exx_variant_scf", "exact-Fock variant: E_EXX, gap and E_EXX - (E_uniform_gas + Delta E_x)"),
                   ("rescaling_partners", "rescaling partners"), ("crossing_demonstration", "crossing demonstration"),
                   ("thermo_state_functions", "thermal mu, E, S, F, Omega"), ("thermo_derivatives", "C_V, dE/dT and -dF/dT"),
                   ("thermo_sea_hole_diagnostic", "sea-hole diagnostic"), ("thermo_levels", "thermal levels label by label"),
                   ("thermo_mu_high_precision", "mu in 40 digits from each solver's own levels")):
    if name not in C:
        raise SystemExit("missing check " + name)
    m = PAT.search(C[name]["detail"])
    if m:
        bullets.append(f"* {what} ({m.group(1)}): {float(m.group(2)):.3f} ({m.group(3)}).")
    else:
        bullets.append(f"* {what}: " + C[name]["detail"])
pre = C["inputs_all_pass"]["detail"]
res = (f"## Results (`reports/ks-crosscheck.json`: {n} checks, all PASS; run of 2026-10-17, the corrected metric)\n\n"
       "Preconditions: " + pre + ".\n\n"
       + "* " + C["rust_refinement_applies_to_matrix"]["detail"] + "\n"
       + "* " + C["rust_refinement_applies_to_matrix_exx"]["detail"] + "\n"
       + "* " + C["problem_definition_identical"]["detail"] + "\n"
       + "* " + C["parameters_particle_numbers"]["detail"] + "\n"
       + "* " + C["parameters_couplings"]["detail"] + "\n\n"
       "Rust and the reference agree within the stated tolerances everywhere. Each line gives the number of comparisons "
       "and the largest ratio |diff| / tolerance (where it occurs).\n\n"
       "* " + C["ground_occupations_and_groups"]["detail"] + "\n"
       + "\n".join(bullets) + "\n"
       + "* " + C["excited_particle_hole_lists"]["detail"] + "\n"
       + "* " + C["thermo_mu_rounding_diagnostic"]["detail"] + "\n"
       + "* " + C["thermo_mu_rust_stated_bound"]["detail"] + "\n\n"
       + C["reference_outputs_lf_only"]["detail"] + "; " + C["reference_manifest"]["detail"] + ". "
       + C["reference_repeat_byte_identical"]["detail"] + ".")
sub("@@RESULTS@@", res)

steps = {}
for line in Path(sys.argv[2]).read_text(encoding="utf-8").splitlines():
    m = re.match(r"(\S+) rc=0 ([0-9.]+) s", line)
    if m:
        steps[m.group(1)] = float(m.group(2))
cc_seconds = "%.1f" % steps["crosscheck"]
NL = chr(10)
tim = ("## Timings (this machine, 24 cores)" + NL + NL
       + "Runs of 2026-10-17 (the corrected metric, the record of `claude_failures.md` H15; every call under "
       "`timeout -k 5 423`, the machine otherwise idle):" + NL + NL
       + "* `run_reference.py` (canonical) in two stages of six parts each with the job cache `--cache DIR --stage 1|2 "
       "--part i/6 --jobs 20`, then the assembly (%.1f s); the parts' times are in `../reference/README.md`." % steps["ref-assembly"] + NL
       + "* `measure_rust_refinement.py --jobs 20`: 550 `single` runs (275 states, canonical and refined) in %.1f s." % steps["rust-refinement"] + NL
       + "* The checker's reference repeat into its own job cache: stage 1 "
       + ", ".join("%.1f" % steps["cc-s1p%d" % i] for i in range(1, 7)) + " s, stage 2 "
       + ", ".join("%.1f" % steps["cc-s2p%d" % i] for i in range(1, 7)) + " s." + NL
       + f"* `crosscheck_ks.py --jobs 22 --repeat-cache DIR`: {cc_seconds} s in total (the 40-digit mu roots, the assembly "
       f"of the reference repeat from the cache and the comparisons); {n} checks, all PASS." + NL + NL
       + "The runs of 2026-10-08 and 2026-10-14 (the earlier records) are in the git history of this file.")
sub("@@TIMINGS@@", tim)

corr = (S / "checker_corrected_section.md").read_text(encoding="utf-8")
run_sentence = (f"The run of 2026-10-17: {n} of {n} checks PASS (section Results); the reference repeat, computed into "
                "its own cache, is byte-identical to the committed reference.")
assert corr.count("@@RUN@@") == 1
corr = corr.replace("@@RUN@@", run_sentence)
sub("@@CORRECTED@@", corr.rstrip("\n"))

# the rounding bound of mu quoted in the tolerance rule: from the stated-bound check
mx = grab("thermo_mu_rust_stated_bound", r"largest \|mu_Rust - root\| ([0-9.e+-]+) m")
sub("the exact values are needed to test the rounding bound of mu (about 1e-16 m).",
    f"the exact values are needed to test the rounding bound of mu (|mu_Rust - root| at most {mx} m in this run).")
assert "@@" not in t, re.findall(r"@@\w+@@", t)
(KS / "checker" / "README.md").write_bytes(t.encode("utf-8"))
print("wrote checker/README.md", len(t.splitlines()), "lines")
