#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Revision gate (Revision/SPEC.md section 10): re-runs EVERY Revision verifier and checker in dependency
# order, then requires that every committed output is byte for byte unchanged and that every report's checks
# pass, then runs the Revision unit tests (except the textbook test, which has its own build).
# Twin of Revision/verify_revision.ps1: the step table, the audit program and the final line are the same
# text in both files (Revision/tests/test_revision_gate.py checks that).  Same pattern as the gates
# scripts/verify_stage3_dark_sector.{sh,ps1} (logged steps, stop at the first failing step); no file of the
# old stages is run or read: the run_logged-style logging and the audit program are part of this file.
#
# Run from any directory with Git Bash, WSL, Linux or macOS:
#   bash Revision/verify_revision.sh [--dry-run] [--fast] [--steps a,b,c]
#     --dry-run      print the selected steps with their expected wall times and commands; run nothing
#     --fast         skip the steps documented as longer than 5 minutes and the steps that need them
#                    (printed as revision_skipped_step=...)
#     --steps a,b,c  run only these steps (the two audits committed-unchanged and reports-pass always run)
#
# Needs: python (numpy, sympy, mpmath, matplotlib, nbformat, nbclient, ipykernel), git, cargo,
# wolframscript (activated by the user; the gate never activates it), pdflatex (PATH or MiKTeX).
# Every step runs with its log in build/logs/revision/<step>-bash.log (build/ is git-ignored); the gate
# writes its work files only under build/revision/ (each step's work folder is emptied before the step).
# Some verifiers rewrite their committed outputs in place (that is how they are documented); the step
# committed-unchanged then requires `git diff --quiet HEAD` on those output paths and no new untracked
# file there, and lists every path that differs (marking the paths that already differed before the run).
# Before any step the gate stops (revision_failed_step=precheck) when an output path of a selected step
# already differs from HEAD: it verifies the committed record and never overwrites uncommitted work.
# The step reports-pass reads EVERY report of the step table (also of the steps not run now) and requires
# every check to pass.  The gate stops at the first failing step and prints revision_failed_step,
# revision_failed_log and revision_verification=FAILED.  A Wolfram step whose log shows a licence or
# kernel-limit message is retried after 30 s, at most 3 attempts.  The last line is
#   revision_verification=OK      (every selected step passed)
#   revision_verification=FAILED
# (a --dry-run ends with revision_verification=NOT-RUN).
#
# Steps (dependency order; expected wall time on the development machine, Windows 11, 24 threads, from the
# folder READMEs and provenance files or measured by this gate on 2026-10-08; "long" = skipped by --fast):
#   algebra-wolfram                       10 s
#   algebra-sympy                          5 s
#   gkd-rust-build                        60 s
#   gkd-rust-lovelock                     15 s
#   gkd-rust-selftest                    900 s  long
#   gkd-wolfram                          110 s
#   gkd-sympy                             30 s
#   gkd-notebook-extract                  10 s
#   gkd-notebook-digest                    5 s
#   gkd-notebook-image                    10 s
#   gkd-author-extract                   120 s
#   gkd-author-compare                    60 s
#   theory-wolfram                      2700 s  long
#   theory-wolfram-scope                  60 s
#   theory-sympy                         240 s
#   theory-sympy-scope                     5 s
#   theory-compare                         2 s
#   pairing-wolfram                      280 s
#   pairing-sympy                        240 s
#   a4-wolfram                            70 s
#   a4-sympy                              30 s
#   a4-ks-source-conditions                5 s
#   a4-ks-source                          20 s
#   a4-ks-source-unittest                 30 s
#   ks-theory-wolfram                     60 s
#   ks-theory-sympy                       60 s
#   ks-rust-build                         60 s
#   ks-rust-test                          60 s
#   ks-rust-canonical                    250 s
#   ks-rust-mermin-roots                  30 s
#   ks-rust-repeat                       250 s
#   ks-rust-repeat-identical               5 s
#   ks-rust-refined                      620 s  long
#   ks-rust-determinism                   30 s  long
#   ks-reference                         750 s  long
#   ks-rust-refinement                    90 s
#   ks-crosscheck                        780 s  long
#   t3-wolfram                            15 s
#   t3-sympy                              10 s
#   t3-completion-wolfram                 20 s
#   t3-rust-demo                         900 s  long
#   t3-reference-demo                    600 s  long
#   t3-completion-sympy                   10 s
#   dark16-derive                         10 s
#   dark16-ks-history                    150 s
#   dark16-eos                             5 s
#   dark16-independent                   180 s
#   dark00-derive                         30 s
#   dark00-independent                    30 s
#   dark00-unittest                       30 s
#   lead-emt-divergence                   10 s
#   lead-einstein-gauss-bonnet            20 s
#   lead-charge-conjugation               15 s
#   notebooks-check                       90 s
#   pdf-dirac16complex-field-theory       30 s
#   pdf-dirac16complex00-field-theory     30 s
#   pdf-pair-creation-proofs              30 s
#   pdf-kohn-sham-deflating-field         30 s
#   pdf-dark-sector-hypotheses            30 s
#   pdf-lovelock-gkd                      30 s
#   committed-unchanged                   10 s  always
#   reports-pass                           5 s  always
#   unit-tests                           150 s
#
# Order: the GKD Lovelock tensors come right after the algebra because the a4 field equations read
# Revision/gkd_lovelock/results/lovelock-tensors.json; the Kohn-Sham Rust solver is built before every step
# that runs it; ks-rust-mermin-roots follows the canonical matrix (its check compares with it);
# ks-rust-determinism needs the repeat and the refined run; t3-reference-demo reads the Rust demonstration;
# t3-completion-sympy reads both demonstrations; the dark sector reads the Kohn-Sham and a4 records.
set -euo pipefail

# The whole gate is one function, so that bash has parsed all of it before the first step runs (an edit of
# this file during a run cannot change the run).
main() {
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
cd -- "$repository_root"
export PYTHONUTF8=1
gate_started_epoch="$(date +%s)"

dry_run=0
fast=0
steps_option=""
while (($# > 0)); do
    case "$1" in
        --dry-run) dry_run=1 ;;
        --fast) fast=1 ;;
        --steps)
            (($# >= 2)) || { printf 'usage: %s [--dry-run] [--fast] [--steps a,b,c]\n' "$0" >&2; exit 2; }
            steps_option="$2"
            shift
            ;;
        --steps=*) steps_option="${1#--steps=}" ;;
        *)
            printf 'usage: %s [--dry-run] [--fast] [--steps a,b,c]\n' "$0" >&2
            exit 2
            ;;
    esac
    shift
done

stop_gate() {
    # stop_gate STEP LOG REASON [CODE]
    printf 'revision_failed_step=%s\n' "$1"
    [[ -z "$2" ]] || printf 'revision_failed_log=%s\n' "$2"
    [[ -z "$3" ]] || printf 'revision_failure_reason=%s\n' "$3"
    printf 'revision_gate_seconds=%d\n' "$(($(date +%s) - gate_started_epoch))"
    printf '%s\n' 'revision_verification=FAILED'
    local code="${4:-1}"
    if [[ "$code" == 0 ]]; then
        code=1
    fi
    exit "$code"
}

to_unix_path() {
    if command -v wslpath >/dev/null 2>&1; then
        wslpath -u "$1"
    elif command -v cygpath >/dev/null 2>&1; then
        cygpath -u "$1"
    else
        printf '%s\n' "$1"
    fi
}

resolve_command() {
    # resolve_command NAME [NAME ...]: first match on PATH, else via Windows PowerShell
    local name windows_path shell_command executable
    for name in "$@"; do
        if executable="$(command -v "$name" 2>/dev/null)"; then
            printf '%s\n' "$executable"
            return 0
        fi
    done
    for shell_command in powershell.exe pwsh.exe; do
        command -v "$shell_command" >/dev/null 2>&1 || continue
        for name in "$@"; do
            windows_path="$(
                "$shell_command" -NoProfile -NonInteractive -Command \
                    "(Get-Command '$name' -ErrorAction Stop).Source" \
                    2>/dev/null | tr -d '\r' | tail -n 1
            )" || true
            [[ -n "$windows_path" ]] || continue
            executable="$(to_unix_path "$windows_path")"
            if [[ -f "$executable" ]]; then
                printf '%s\n' "$executable"
                return 0
            fi
        done
    done
    return 1
}

# The Windows executables come first (as in the stage gates), so that Git Bash and WSL use the same Python
# and the same Rust toolchain as the PowerShell twin.
python_command="$(resolve_command python.exe python python3)" ||
    stop_gate tools "" "python was not found"
printf 'revision_tool_python=%s\n' "$python_command"

gate_directory=build/revision
if ((dry_run == 1)); then
    # A dry run never touches the files of a gate that may be running.
    gate_directory=build/revision/dry-run
fi
mkdir -p -- "$gate_directory" build/logs/revision
steps_file="$gate_directory/steps.txt"
audit_script="$gate_directory/gate_audit.py"
cat >"$steps_file" <<'REVISION_GATE_STEPS'
algebra-wolfram|10|0|-|Revision/algebra/gammas.json,Revision/algebra/reports/wolfram-algebra.json|Revision/algebra/reports/wolfram-algebra.json|{wolframscript} -file Revision/algebra/wolfram/verify_algebra.wls
algebra-sympy|5|0|-|Revision/algebra/reports/python-algebra.json,Revision/algebra/reports/python-gammas.json|Revision/algebra/reports/python-algebra.json|{python} Revision/algebra/python/check_algebra.py
gkd-rust-build|60|0|-|-|-|{cargo} build --release --manifest-path Revision/gkd_lovelock/code/Cargo.toml
gkd-rust-lovelock|15|0|-|Revision/gkd_lovelock/results/curvature.json,Revision/gkd_lovelock/results/lovelock-tensors.json,Revision/gkd_lovelock/results/lovelock-components.md,Revision/gkd_lovelock/results/lovelock-report.json|Revision/gkd_lovelock/results/lovelock-report.json|{gkd_exe} lovelock --output Revision/gkd_lovelock/results --brute-force-k2
gkd-rust-selftest|900|1|-|Revision/gkd_lovelock/results/gkd-selftest.json|Revision/gkd_lovelock/results/gkd-selftest.json|{gkd_exe} gkd-selftest --exhaustive-max 4 --output Revision/gkd_lovelock/results
gkd-wolfram|110|0|-|Revision/gkd_lovelock/results/wolfram-gkd-report.json|Revision/gkd_lovelock/results/wolfram-gkd-report.json|{wolframscript} -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls Revision/gkd_lovelock/results/wolfram-gkd-report.json
gkd-sympy|30|0|-|Revision/gkd_lovelock/results/python-lovelock-report.json|Revision/gkd_lovelock/results/python-lovelock-report.json|{python} Revision/gkd_lovelock/verification/check_lovelock_gkd.py
gkd-notebook-extract|10|0|-|-|-|{wolframscript} -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
gkd-notebook-digest|5|0|-|Revision/gkd_lovelock/results/notebook-input-cells.txt|-|{python} Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py
gkd-notebook-image|10|0|-|Revision/gkd_lovelock/results/notebook-in68-image.png|-|{wolframscript} -file Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
gkd-author-extract|120|0|-|Revision/gkd_lovelock/comparison/author-curvature-outputs.json|-|{wolframscript} -file Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls
gkd-author-compare|60|0|-|Revision/gkd_lovelock/comparison/author-comparison-report.json|Revision/gkd_lovelock/comparison/author-comparison-report.json|{python} Revision/gkd_lovelock/comparison/compare_with_author.py
theory-wolfram|2700|1|-|Revision/theory/field-theory.json,Revision/theory/reports/wolfram-field-theory.json|Revision/theory/reports/wolfram-field-theory.json|{wolframscript} -file Revision/theory/wolfram/verify_field_theory.wls
theory-wolfram-scope|60|0|-|Revision/theory/reports/wolfram-scope.json|Revision/theory/reports/wolfram-scope.json|{wolframscript} -file Revision/theory/wolfram/verify_scope.wls
theory-sympy|240|0|-|Revision/theory/reports/python-field-theory.json|Revision/theory/reports/python-field-theory.json|{python} Revision/theory/python/check_field_theory.py
theory-sympy-scope|5|0|-|Revision/theory/reports/python-scope.json|Revision/theory/reports/python-scope.json|{python} Revision/theory/python/check_scope.py
theory-compare|2|0|-|-|-|{audit} json-equals Revision/theory/reports/python-field-theory.json comparison_with_wolfram.status agree
pairing-wolfram|280|0|-|Revision/pairing/pairing-theory.json,Revision/pairing/reports/wolfram-pairing.json|Revision/pairing/reports/wolfram-pairing.json|{wolframscript} -file Revision/pairing/wolfram/verify_pairing.wls
pairing-sympy|240|0|-|Revision/pairing/reports/python-pairing.json|Revision/pairing/reports/python-pairing.json|{python} Revision/pairing/python/check_pairing.py
a4-wolfram|70|0|-|Revision/field_equations_a4/a4-equations.json,Revision/field_equations_a4/reports/wolfram-a4-report.json|Revision/field_equations_a4/reports/wolfram-a4-report.json|{wolframscript} -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
a4-sympy|30|0|-|Revision/field_equations_a4/reports/python-a4-report.json,Revision/field_equations_a4/reports/a4-equations-summary.md|Revision/field_equations_a4/reports/python-a4-report.json|{python} Revision/field_equations_a4/python/check_field_equations_a4.py
a4-ks-source-conditions|5|0|-|Revision/field_equations_a4/reports/ks-source-conditions.json|Revision/field_equations_a4/reports/ks-source-conditions.json|{python} Revision/field_equations_a4/python/check_ks_source_conditions.py
a4-ks-source|20|0|-|Revision/field_equations_a4/ks_source/results,Revision/field_equations_a4/ks_source/reports|Revision/field_equations_a4/ks_source/reports/ks-source-a4.json|{python} Revision/field_equations_a4/ks_source/ks_source_a4.py
a4-ks-source-unittest|30|0|-|Revision/field_equations_a4/ks_source/results,Revision/field_equations_a4/ks_source/reports|-|{python} -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
ks-theory-wolfram|60|0|-|Revision/kohn_sham/ks-theory.json,Revision/kohn_sham/reports/ks-theory-wolfram.json|Revision/kohn_sham/reports/ks-theory-wolfram.json|{wolframscript} -file Revision/kohn_sham/theory/verify_ks_theory.wls
ks-theory-sympy|60|0|-|Revision/kohn_sham/reports/ks-theory-python.json|Revision/kohn_sham/reports/ks-theory-python.json|{python} Revision/kohn_sham/theory/check_ks_theory.py
ks-rust-build|60|0|-|-|-|{cargo} build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
ks-rust-test|60|0|-|-|-|{cargo} test --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
ks-rust-canonical|250|0|-|Revision/kohn_sham/results,Revision/kohn_sham/reports/ks-rust-solver.json|Revision/kohn_sham/reports/ks-rust-solver.json|{ks_solver} all --out Revision/kohn_sham/results --report Revision/kohn_sham/reports/ks-rust-solver.json
ks-rust-mermin-roots|30|0|build/revision/ks-mermin-roots|Revision/kohn_sham/reports/ks-rust-mermin-roots.json,Revision/kohn_sham/solver/tools/mermin-roots-40digit.json|Revision/kohn_sham/reports/ks-rust-mermin-roots.json|{python} Revision/kohn_sham/solver/tools/mermin_roots_mp.py --work build/revision/ks-mermin-roots
ks-rust-repeat|250|0|build/revision/ks-repeat|-|-|{ks_solver} all --out build/revision/ks-repeat/results --report build/revision/ks-repeat/report.json
ks-rust-repeat-identical|5|0|-|-|-|{audit} same build/revision/ks-repeat/results Revision/kohn_sham/results build/revision/ks-repeat/report.json Revision/kohn_sham/reports/ks-rust-solver.json
ks-rust-refined|620|1|build/revision/ks-refined|-|-|{ks_solver} all --refined --out build/revision/ks-refined/results --report build/revision/ks-refined/report.json
ks-rust-determinism|30|1|-|Revision/kohn_sham/reports/ks-rust-determinism.json|Revision/kohn_sham/reports/ks-rust-determinism.json|{python} Revision/kohn_sham/solver/tools/compare_runs.py --canonical Revision/kohn_sham/results --canonical-report Revision/kohn_sham/reports/ks-rust-solver.json --repeat build/revision/ks-repeat/results --repeat-report build/revision/ks-repeat/report.json --refined build/revision/ks-refined/results --refined-report build/revision/ks-refined/report.json --report Revision/kohn_sham/reports/ks-rust-determinism.json
ks-reference|750|1|-|Revision/kohn_sham/reference/results,Revision/kohn_sham/reports/ks-reference.json|Revision/kohn_sham/reports/ks-reference.json|{python} Revision/kohn_sham/reference/run_reference.py
ks-rust-refinement|90|0|build/revision/ks-refinement|Revision/kohn_sham/checker/rust-refinement.json|-|{python} Revision/kohn_sham/checker/measure_rust_refinement.py --work build/revision/ks-refinement
ks-crosscheck|780|1|build/revision/ks-crosscheck|Revision/kohn_sham/reports/ks-crosscheck.json,Revision/kohn_sham/reports/ks-crosscheck-table.csv|Revision/kohn_sham/reports/ks-crosscheck.json|{python} Revision/kohn_sham/checker/crosscheck_ks.py --work build/revision/ks-crosscheck
t3-wolfram|15|0|-|Revision/pairing/kohn_sham/t3-theory.json,Revision/pairing/kohn_sham/reports/wolfram-t3.json|Revision/pairing/kohn_sham/reports/wolfram-t3.json|{wolframscript} -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
t3-sympy|10|0|-|Revision/pairing/kohn_sham/reports/python-t3.json|Revision/pairing/kohn_sham/reports/python-t3.json|{python} Revision/pairing/kohn_sham/python/check_t3.py
t3-completion-wolfram|20|0|-|Revision/pairing/kohn_sham/t3-completion.json,Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json|Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json|{wolframscript} -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
t3-rust-demo|900|1|build/revision/t3-rust-demo|Revision/pairing/kohn_sham/reports/t3-rust-demo.json,Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv|Revision/pairing/kohn_sham/reports/t3-rust-demo.json|{python} Revision/pairing/kohn_sham/numerics/t3_rust_demo.py --solver {ks_solver} --work build/revision/t3-rust-demo --jobs 8
t3-reference-demo|600|1|-|Revision/pairing/kohn_sham/reports/t3-reference-demo.json,Revision/pairing/kohn_sham/numerics/results/t3-reference-states.csv|Revision/pairing/kohn_sham/reports/t3-reference-demo.json|{python} Revision/pairing/kohn_sham/numerics/t3_reference_demo.py --jobs 8
t3-completion-sympy|10|0|-|Revision/pairing/kohn_sham/reports/python-t3-completion.json|Revision/pairing/kohn_sham/reports/python-t3-completion.json|{python} Revision/pairing/kohn_sham/python/check_t3_completion.py
dark16-derive|10|0|-|Revision/dark_sector/dirac16complex/outputs/effective-formulas.json,Revision/dark_sector/dirac16complex/reports/derivation-checks.json|Revision/dark_sector/dirac16complex/reports/derivation-checks.json|{python} Revision/dark_sector/dirac16complex/derive/derive_effective.py
dark16-ks-history|150|0|-|Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv,Revision/dark_sector/dirac16complex/reports/ks-history-run.json|Revision/dark_sector/dirac16complex/reports/ks-history-run.json|{python} Revision/dark_sector/dirac16complex/compute/run_ks_history.py --solver {ks_solver}
dark16-eos|5|0|-|Revision/dark_sector/dirac16complex/outputs/eos-history.csv,Revision/dark_sector/dirac16complex/outputs/eos-summary.json,Revision/dark_sector/dirac16complex/reports/eos-checks.json|Revision/dark_sector/dirac16complex/reports/eos-checks.json|{python} Revision/dark_sector/dirac16complex/compute/compute_eos.py
dark16-independent|180|0|-|Revision/dark_sector/dirac16complex/outputs/independent-free-gas.json,Revision/dark_sector/dirac16complex/reports/independent-checks.json|Revision/dark_sector/dirac16complex/reports/independent-checks.json|{python} Revision/dark_sector/dirac16complex/independent/independent_free_gas.py
dark00-derive|30|0|-|Revision/dark_sector/dirac16complex00/eos-theory.json,Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json|Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json|{python} Revision/dark_sector/dirac16complex00/python/derive_eos.py
dark00-independent|30|0|-|Revision/dark_sector/dirac16complex00/results/independent-numerics.json,Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json|Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json|{python} Revision/dark_sector/dirac16complex00/python/independent_numerics.py
dark00-unittest|30|0|-|Revision/dark_sector/dirac16complex00|-|{python} -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
lead-emt-divergence|10|0|-|Revision/lead_checks/reports/emt-divergence-and-spin-connection.json|Revision/lead_checks/reports/emt-divergence-and-spin-connection.json|{python} Revision/lead_checks/emt_divergence_and_spin_connection.py
lead-einstein-gauss-bonnet|20|0|-|Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json|Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json|{python} Revision/lead_checks/einstein_gauss_bonnet_a4.py
lead-charge-conjugation|15|0|-|Revision/lead_checks/reports/charge-conjugation-and-u1.json|Revision/lead_checks/reports/charge-conjugation-and-u1.json|{python} Revision/lead_checks/charge_conjugation_and_u1.py
notebooks-check|90|0|-|Revision/notebooks|-|{audit} notebooks Revision/notebooks/tools/build_notebooks.py
pdf-dirac16complex-field-theory|30|0|-|Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.tex,Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-dirac16complex00-field-theory|30|0|-|Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.tex,Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-pair-creation-proofs|30|0|-|Revision/docs/PAIR_CREATION_PROOFS.tex,Revision/docs/PAIR_CREATION_PROOFS.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/PAIR_CREATION_PROOFS.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-kohn-sham-deflating-field|30|0|-|Revision/docs/KOHN_SHAM_DEFLATING_FIELD.tex,Revision/docs/KOHN_SHAM_DEFLATING_FIELD.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-dark-sector-hypotheses|30|0|-|Revision/docs/DARK_SECTOR_HYPOTHESES.tex,Revision/docs/DARK_SECTOR_HYPOTHESES.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/DARK_SECTOR_HYPOTHESES.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-lovelock-gkd|30|0|-|Revision/docs/LOVELOCK_GKD.tex,Revision/docs/LOVELOCK_GKD.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/LOVELOCK_GKD.md --developer-layout --specifications Revision/pdf-specifications.json
committed-unchanged|10|A|-|-|-|{audit} unchanged
reports-pass|5|A|-|-|-|{audit} reports
unit-tests|150|0|-|-|-|{audit} unittest Revision/tests test_universes_in_pairs_textbook
REVISION_GATE_STEPS
cat >"$audit_script" <<'REVISION_GATE_AUDIT_PY'
# Revision gate audit program (written by Revision/verify_revision.sh and Revision/verify_revision.ps1 into
# build/revision/gate_audit.py; both twins embed this text byte for byte, Revision/tests/test_revision_gate.py
# checks that).  Python standard library only.  Run from the repository root.
import filecmp
import json
import os
import subprocess
import sys
import unittest

# The folder of this program: build/revision (build/revision/dry-run for a dry run, which writes nothing).
GATE = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
RUN_AUDIT = "build/revision/gate_audit.py"
SELECTED = os.path.join(GATE, "selected.txt")
OUTPUTS = os.path.join(GATE, "outputs.txt")
REPORTS = os.path.join(GATE, "reports.txt")
PREEXISTING = os.path.join(GATE, "preexisting.txt")
LONG_SECONDS = 300


def fail(message):
    print("revision_audit_error=" + message)
    return 1


def read_table(path):
    steps = []
    with open(path, encoding="utf-8") as handle:
        for line in handle.read().splitlines():
            if not line.strip():
                continue
            fields = line.split("|")
            if len(fields) != 7:
                raise SystemExit("malformed step line: " + line)
            name, seconds, kind, fresh, outputs, reports, command = fields
            steps.append({
                "name": name, "seconds": int(seconds), "kind": kind, "fresh": fresh,
                "outputs": [] if outputs == "-" else outputs.split(","),
                "reports": [] if reports == "-" else reports.split(","),
                "command": command,
            })
    return steps


def executable(stem):
    path = stem + (".exe" if os.name == "nt" else "")
    return path.replace("\\", "/")


def plan(arguments):
    table, fast, dry_run, wanted = arguments[0], False, False, None
    rest = arguments[1:]
    while rest:
        option = rest.pop(0)
        if option == "--fast":
            fast = True
        elif option == "--dry-run":
            dry_run = True
        elif option == "--steps":
            wanted = [name for name in rest.pop(0).split(",") if name]
        else:
            return fail("unknown plan option " + option)
    steps = read_table(table)
    names = [step["name"] for step in steps]
    if len(set(names)) != len(names):
        return fail("duplicate step names")
    if wanted is not None:
        unknown = [name for name in wanted if name not in names]
        if unknown:
            print("revision_unknown_steps=" + ",".join(unknown))
            print("revision_known_steps=" + ",".join(names))
            return 2
    substitutions = {
        "{ks_solver}": executable("Revision/kohn_sham/solver/target/release/revision_ks_solver"),
        "{gkd_exe}": executable("Revision/gkd_lovelock/code/target/release/lovelock_gkd"),
        "{audit}": "{python} " + RUN_AUDIT,
    }
    selected, skipped = [], []
    for step in steps:
        always = step["kind"] == "A"
        if wanted is not None and step["name"] not in wanted and not always:
            continue
        if fast and step["kind"] == "1":
            skipped.append(step)
            continue
        selected.append(step)
    for step in skipped:
        print("revision_skipped_step=%s (expected %d s; --fast skips the steps longer than %d s and the steps "
              "that need them)" % (step["name"], step["seconds"], LONG_SECONDS))
    lines, outputs, total = [], [], 0
    for step in selected:
        command = step["command"]
        for key, value in substitutions.items():
            command = command.replace(key, value)
        lines.append("%s\t%d\t%s\t%s" % (step["name"], step["seconds"], step["fresh"], command))
        total += step["seconds"]
        for path in step["outputs"]:
            if path not in outputs:
                outputs.append(path)
        if dry_run:
            print("revision_dry_run_step=%s expected_seconds=%d command=%s" % (step["name"], step["seconds"], command))
    reports = []
    for step in steps:
        for path in step["reports"]:
            if path not in reports:
                reports.append(path)
    if dry_run:
        print("revision_selected_steps=%d expected_seconds=%d skipped_steps=%d" % (len(selected), total, len(skipped)))
        return 0
    os.makedirs(GATE, exist_ok=True)
    for path, items in ((SELECTED, lines), (OUTPUTS, outputs), (REPORTS, reports)):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("".join(item + "\n" for item in items))
    print("revision_selected_steps=%d expected_seconds=%d skipped_steps=%d" % (len(selected), total, len(skipped)))
    return 0


def git_lines(arguments):
    result = subprocess.run(["git"] + arguments, capture_output=True, text=True, encoding="utf-8")
    if result.returncode not in (0, 1):
        raise SystemExit("git " + " ".join(arguments[:2]) + " failed: " + result.stderr.strip())
    return [line for line in result.stdout.splitlines() if line.strip()]


def changed_paths(paths):
    if not paths:
        return []
    differing = git_lines(["diff", "--name-only", "HEAD", "--"] + paths)
    untracked = git_lines(["ls-files", "--others", "--exclude-standard", "--"] + paths)
    return sorted(set(differing) | set(untracked))


def read_list(path):
    with open(path, encoding="utf-8") as handle:
        return [line for line in handle.read().splitlines() if line]


def precheck(arguments):
    paths = read_list(OUTPUTS)
    before = changed_paths(paths)
    with open(PREEXISTING, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("".join(path + "\n" for path in before))
    for path in before:
        print("revision_preexisting_change=" + path)
    print("revision_output_paths=%d preexisting_changes=%d" % (len(paths), len(before)))
    # The gate verifies the COMMITTED record and never overwrites uncommitted work: a selected step whose
    # output paths already differ from HEAD stops the gate before anything runs.
    if before:
        print("revision_precheck=the output paths above already differ from HEAD; commit or set them aside, "
              "or leave their steps out with --steps")
        return 1
    return 0


def unchanged(arguments):
    paths = read_list(OUTPUTS)
    before = set(read_list(PREEXISTING)) if os.path.exists(PREEXISTING) else set()
    quiet = subprocess.run(["git", "diff", "--quiet", "HEAD", "--"] + paths).returncode if paths else 0
    after = changed_paths(paths)
    for path in after:
        note = " (it already differed from HEAD before the gate ran)" if path in before else ""
        print("revision_changed_output=" + path + note)
    print("revision_output_paths=%d git_diff_quiet=%s changed=%d" % (len(paths), quiet == 0, len(after)))
    return 0 if (quiet == 0 and not after) else 1


def check_verdicts(document):
    """Return (passed, not_available, total, problems) for one report."""
    problems, passed, not_available, total = [], 0, 0, 0
    checks = document.get("checks")
    if isinstance(checks, list):
        for item in checks:
            total += 1
            if not isinstance(item, dict) or "name" not in item or "verdict" not in item or "detail" not in item:
                problems.append("a check without name, verdict and detail")
                continue
            if str(item["verdict"]).upper() == "PASS":
                passed += 1
            elif str(item["verdict"]).upper() == "NOT-AVAILABLE":
                # declared by the author comparison: the author's notebook stores no such output
                not_available += 1
            else:
                problems.append("%s: %s" % (item["name"], item["verdict"]))
    elif isinstance(checks, dict):
        for name, item in checks.items():
            total += 1
            ok = item is True or (isinstance(item, dict) and (item.get("passed") is True or
                                                                str(item.get("verdict", "")).upper() == "PASS"))
            if ok:
                passed += 1
            else:
                problems.append(name)
    elif "results" in document:
        for item in document["results"]:
            total += 1
            if isinstance(item, dict) and item.get("mismatches") == 0:
                passed += 1
            else:
                problems.append("result with mismatches: " + json.dumps(item)[:120])
    else:
        problems.append("no checks")
    if total == 0:
        problems.append("zero checks")
    if "verdict" in document and str(document["verdict"]).upper() not in ("PASS", "SUCCESS"):
        problems.append("verdict " + str(document["verdict"]))
    if document.get("failedCheckCount", 0) != 0:
        problems.append("failedCheckCount %s" % document.get("failedCheckCount"))
    summary = document.get("summary")
    if isinstance(summary, dict):
        for key in ("failed", "FAIL"):
            if summary.get(key, 0) != 0:
                problems.append("summary.%s %s" % (key, summary.get(key)))
    return passed, not_available, total, problems


def reports(arguments):
    # Every report of the step table (also those of steps not run now): the committed record must pass.
    paths = read_list(REPORTS)
    failures = 0
    for path in paths:
        try:
            with open(path, encoding="utf-8") as handle:
                document = json.load(handle)
        except (OSError, ValueError) as error:
            print("revision_report_failed=%s (%s)" % (path, error))
            failures += 1
            continue
        passed, not_available, total, problems = check_verdicts(document)
        extra = " not_available=%d" % not_available if not_available else ""
        if problems:
            failures += 1
            print("revision_report_failed=%s checks=%d/%d%s problems=%s" % (
                path, passed, total, extra, "; ".join(problems)[:400]))
        else:
            print("revision_report=%s checks=%d/%d passed%s" % (path, passed, total, extra))
    print("revision_reports=%d failed=%d" % (len(paths), failures))
    return 1 if failures else 0


def json_equals(arguments):
    path, dotted, expected = arguments
    with open(path, encoding="utf-8") as handle:
        value = json.load(handle)
    for key in dotted.split("."):
        value = value.get(key) if isinstance(value, dict) else None
    print("revision_json_value=%s %s=%s (required %s)" % (path, dotted, value, expected))
    return 0 if str(value) == expected else 1


def tree_files(root):
    found = []
    for directory, _, files in os.walk(root):
        for name in files:
            found.append(os.path.relpath(os.path.join(directory, name), root).replace("\\", "/"))
    return sorted(found)


def same(arguments):
    if len(arguments) % 2 or not arguments:
        return fail("same needs pairs of paths")
    differences, compared = [], 0
    for index in range(0, len(arguments), 2):
        first, second = arguments[index], arguments[index + 1]
        if os.path.isdir(first) and os.path.isdir(second):
            names_first, names_second = tree_files(first), tree_files(second)
            if names_first != names_second:
                differences.append("%s vs %s: different file lists (%d vs %d files)" % (
                    first, second, len(names_first), len(names_second)))
            for name in sorted(set(names_first) & set(names_second)):
                compared += 1
                if not filecmp.cmp(os.path.join(first, name), os.path.join(second, name), shallow=False):
                    differences.append("%s/%s differs" % (first, name))
        elif os.path.isfile(first) and os.path.isfile(second):
            compared += 1
            if not filecmp.cmp(first, second, shallow=False):
                differences.append("%s vs %s differ" % (first, second))
        else:
            differences.append("%s or %s is missing" % (first, second))
    for line in differences[:50]:
        print("revision_difference=" + line)
    print("revision_same_files=%d differences=%d" % (compared, len(differences)))
    return 1 if differences else 0


def notebooks(arguments):
    tool = arguments[0]
    listing = subprocess.run([sys.executable, tool, "list"], capture_output=True, text=True, encoding="utf-8")
    print(listing.stdout, end="")
    if listing.returncode != 0:
        print(listing.stderr, end="")
        return fail("notebook list failed")
    names = [line.split()[0] for line in listing.stdout.splitlines() if line.strip()]
    if not names:
        return fail("no Revision notebook found")
    failures = 0
    for name in names:
        for action in ("audit", "check"):
            sys.stdout.flush()
            code = subprocess.run([sys.executable, tool, action, name]).returncode
            print("revision_notebook=%s action=%s exit_code=%d" % (name, action, code))
            failures += code != 0
    print("revision_notebooks=%d failed_actions=%d" % (len(names), failures))
    return 1 if failures else 0


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def run_unittests(arguments):
    directory, excluded = arguments
    # The gate test runs this gate itself when REVISION_GATE_FULL=1; never recurse.
    os.environ.pop("REVISION_GATE_FULL", None)
    suite = unittest.defaultTestLoader.discover(directory, pattern="test_*.py")
    tests = list(flatten(suite))
    kept = [test for test in tests if test.id().split(".")[0] != excluded]
    print("revision_unit_tests=%d excluded=%d (%s has its own build)" % (len(kept), len(tests) - len(kept), excluded))
    sys.stdout.flush()
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(unittest.TestSuite(kept))
    return 0 if result.wasSuccessful() else 1


COMMANDS = {
    "plan": plan, "precheck": precheck, "unchanged": unchanged, "reports": reports,
    "json-equals": json_equals, "same": same, "notebooks": notebooks, "unittest": run_unittests,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("usage: gate_audit.py " + "|".join(sorted(COMMANDS)) + " ...")
        sys.exit(2)
    sys.exit(COMMANDS[sys.argv[1]](sys.argv[2:]))
REVISION_GATE_AUDIT_PY

plan_arguments=(plan "$steps_file")
((fast == 0)) || plan_arguments+=(--fast)
((dry_run == 0)) || plan_arguments+=(--dry-run)
[[ -z "$steps_option" ]] || plan_arguments+=(--steps "$steps_option")
set +e
"$python_command" "$audit_script" "${plan_arguments[@]}"
plan_code=$?
set -e
((plan_code == 0)) || stop_gate plan "" "the step selection was rejected" "$plan_code"
if ((dry_run == 1)); then
    printf '%s\n' 'revision_verification=NOT-RUN (dry run: nothing was executed)'
    exit 0
fi

cargo_command=""
wolframscript_command=""
git_command=""
pdflatex_command=""
if grep -q '{cargo}' "$gate_directory/selected.txt"; then
    cargo_command="$(resolve_command cargo.exe cargo)" || stop_gate tools "" "cargo was not found"
    printf 'revision_tool_cargo=%s\n' "$cargo_command"
fi
if grep -q '{wolframscript}' "$gate_directory/selected.txt"; then
    wolframscript_command="$(resolve_command wolframscript.exe wolframscript)" ||
        stop_gate tools "" "wolframscript was not found (install and activate it yourself; the gate never activates it)"
    printf 'revision_tool_wolframscript=%s\n' "$wolframscript_command"
fi
git_command="$(resolve_command git.exe git)" || stop_gate tools "" "git was not found"
printf 'revision_tool_git=%s\n' "$git_command"
export PATH="$(dirname -- "$git_command"):$PATH"
if grep -q 'build_provenance_pdf' "$gate_directory/selected.txt"; then
    if ! pdflatex_command="$(resolve_command pdflatex.exe pdflatex)"; then
        pdflatex_command=""
        for candidate in \
            "/c/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe" \
            "/mnt/c/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe"; do
            if [[ -f "$candidate" ]]; then
                pdflatex_command="$candidate"
                break
            fi
        done
    fi
    [[ -n "$pdflatex_command" ]] || stop_gate tools "" "pdflatex was not found on PATH or in MiKTeX"
    printf 'revision_tool_pdflatex=%s\n' "$pdflatex_command"
    # scripts/build_provenance_pdf.py looks pdflatex up on PATH.
    export PATH="$(dirname -- "$pdflatex_command"):$PATH"
fi

wolfram_limit_pattern='licen[cs]e|password|kernel limit|maximum number of'
wolfram_limit_pattern+='|too many kernels|could not (launch|start|connect)'

run_logged() {
    # run_logged LOG COMMAND [ARG ...]: the log holds started_utc, repository and command lines, the combined
    # output of the command (also echoed) and finished_utc and exit_code lines; returns the exit code.
    local log_path="$1" code
    shift
    {
        printf 'started_utc=%s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
        printf 'repository=%s\n' "$repository_root"
        printf 'command='
        printf '%q ' "$@"
        printf '\n'
    } >"$log_path"
    set +e
    "$@" 2>&1 | tee -a "$log_path"
    code=${PIPESTATUS[0]}
    set -e
    {
        printf 'finished_utc=%s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
        printf 'exit_code=%d\n' "$code"
    } >>"$log_path"
    return "$code"
}

run_step() {
    # run_step NAME EXPECTED_SECONDS FRESH_DIRECTORY COMMAND_TEXT
    local name="$1" expected="$2" fresh="$3" text="$4" token attempt maximum_attempts=1 log_path code started
    local -a words argv
    read -r -a words <<<"$text"
    argv=()
    for token in "${words[@]}"; do
        case "$token" in
            '{python}') argv+=("$python_command") ;;
            '{cargo}') argv+=("$cargo_command") ;;
            '{wolframscript}') argv+=("$wolframscript_command") ;;
            *) argv+=("$token") ;;
        esac
    done
    if [[ "${words[0]}" == '{wolframscript}' ]]; then
        maximum_attempts=3
    fi
    if [[ "$fresh" != "-" ]]; then
        rm -rf -- "$fresh"
        mkdir -p -- "$fresh"
    fi
    for ((attempt = 1; attempt <= maximum_attempts; attempt++)); do
        if ((attempt == 1)); then
            log_path="build/logs/revision/$name-bash.log"
        else
            log_path="build/logs/revision/$name-attempt$attempt-bash.log"
        fi
        printf 'revision_step=%s expected_seconds=%s\n' "$name" "$expected"
        started="$(date +%s)"
        set +e
        run_logged "$log_path" "${argv[@]}"
        code=$?
        set -e
        printf 'revision_step_seconds=%s %d (expected %s)\n' "$name" "$(($(date +%s) - started))" "$expected"
        if ((code == 0)); then
            printf 'revision_step_ok=%s\n' "$name"
            return 0
        fi
        if ((attempt < maximum_attempts)) && grep -Eiq "$wolfram_limit_pattern" "$log_path"; then
            printf 'revision_retry=%s attempt %d reported a Wolfram licence or kernel limit; retrying in 30 s\n' \
                "$name" "$attempt"
            sleep 30
            continue
        fi
        stop_gate "$name" "$log_path" "" "$code"
    done
}

set +e
"$python_command" "$audit_script" precheck
precheck_code=$?
set -e
((precheck_code == 0)) || stop_gate precheck "" "git status of the output paths could not be read" "$precheck_code"

local -a selected_lines
mapfile -t selected_lines <"$gate_directory/selected.txt"
local selected_line step_name step_seconds step_fresh step_command
for selected_line in "${selected_lines[@]}"; do
    [[ -n "$selected_line" ]] || continue
    IFS=$'\t' read -r step_name step_seconds step_fresh step_command <<<"$selected_line"
    run_step "$step_name" "$step_seconds" "$step_fresh" "$step_command" </dev/null
done

printf 'revision_gate_seconds=%d\n' "$(($(date +%s) - gate_started_epoch))"
printf '%s\n' 'revision_verification=OK'
}

# One line, parsed completely before main runs: nothing after it is read from this file.
main "$@"; exit 0
