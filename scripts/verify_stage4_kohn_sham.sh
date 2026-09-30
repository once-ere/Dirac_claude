#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 4 gate (dirac16complex Kohn-Sham DFT in the primordial field).
# Twin of scripts/verify_stage4_kohn_sham.ps1; the step list, the checks and
# the final line are the same.  Same pattern as the Stage 3 gate
# scripts/verify_stage3_dark_sector.sh (itself modelled on the
# verify_phase*.sh gates of https://github.com/once-ere/dirac,
# GPL-3.0-or-later, with the command resolution of its
# scripts/resolve_wolframscript.sh inlined).  The comparisons, and the launch
# of the Rust runs, are made by one program,
# scripts/verify_stage4_kohn_sham_audit.py, which both twins call, so that
# both apply exactly the same rules.
#
# Run from any directory with Git Bash or WSL:
#   bash scripts/verify_stage4_kohn_sham.sh
#
# Options (the full gate uses none of them):
#   --dry-run          print every step with its expected wall time and command,
#                      run nothing; last line stage4_kohn_sham_verification=DRY-RUN
#   --steps 03,04,...  run only the listed steps (two-digit numbers or full
#                      names; build/stage4 is kept unless step 00 is listed);
#                      the last line is then stage4_kohn_sham_verification=PARTIAL
#                      (exit 3), never OK
#   --refined-thermo   also run "thermo --refined" in step 14 so that the
#                      refined tree is complete and the fresh determinism report
#                      must equal the committed one byte for byte
#   --sequential-rust  run the Rust processes of step 14 one after another
#                      instead of concurrently (same outputs)
#
# Needs: python (numpy, matplotlib, nbformat, nbclient, nbconvert,
# ipykernel), cargo with rustfmt and clippy, git, pdflatex (PATH or MiKTeX);
# wolframscript is optional: without it the two Wolfram steps (the exact
# theory verifier and the Mathematica notebook) are skipped with the message
# stage4_skipped_step=..., the sympy theory checker still compares with the
# committed kohn-sham-theory.json, and the line before the final line says
# which cross-checks were not run.  Every step runs through
# scripts/run_logged.sh with its log in build/logs/ (*-bash.log, so the
# PowerShell twin's logs are not overwritten; the Rust processes of step 14
# write build/logs/stage4-14-rust-runs-bash-<canonical|refined>-<sub>.log;
# build/ is git-ignored; the gate deletes and recreates only build/stage4/).
# The gate stops at the first failing step and prints stage4_failed_step,
# stage4_failed_log and stage4_kohn_sham_verification=FAILED.  A Wolfram step
# whose log shows a licence or kernel-limit message is retried after 30 s, at
# most 3 attempts.  Never run two gates at once (either twin): both would
# delete and rewrite build/stage4.
#
# What is and is not re-run, the step list (stage4-00 .. stage4-36) and the
# measured wall time of every step (TIMING): see the header of the PowerShell
# twin scripts/verify_stage4_kohn_sham.ps1; --dry-run prints the expected
# wall time of every step.
#
# The Wolfram report path is passed positionally, never after "--"
# (WolframScript 1.14 drops "--" and every argument after it).
set -euo pipefail

dry_run=0
refined_thermo=0
sequential_rust=0
steps_option=""
usage() {
    printf 'usage: %s [--dry-run] [--steps LIST] [--refined-thermo] [--sequential-rust]\n' "$0" >&2
    exit 2
}
while (($# > 0)); do
    case "$1" in
        --dry-run) dry_run=1 ;;
        --refined-thermo) refined_thermo=1 ;;
        --sequential-rust) sequential_rust=1 ;;
        --steps)
            shift
            (($# > 0)) || usage
            steps_option="$1"
            ;;
        --steps=*) steps_option="${1#--steps=}" ;;
        *) usage ;;
    esac
    shift
done
selected_steps=()
if [[ -n "$steps_option" ]]; then
    IFS=', ' read -r -a selected_steps <<<"$steps_option"
fi
partial=0
if ((${#selected_steps[@]} > 0)); then
    partial=1
fi

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
cd -- "$repository_root"
gate_started_epoch="$(date +%s)"
export PYTHONUTF8=1

stop_gate() {
    # stop_gate STEP LOG REASON [CODE]
    printf 'stage4_failed_step=%s\n' "$1"
    [[ -z "$2" ]] || printf 'stage4_failed_log=%s\n' "$2"
    [[ -z "$3" ]] || printf 'stage4_failure_reason=%s\n' "$3"
    printf '%s\n' 'stage4_kohn_sham_verification=FAILED'
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
    # resolve_command NAME [NAME ...]: first match on PATH, else via Windows
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

# The Windows executables come first, as in the Stage 1 and Stage 3 gates, so
# that Git Bash and WSL use the same Python (with numpy, matplotlib and the
# Jupyter packages) and the same Rust toolchain as the PowerShell twin.
python_command="$(resolve_command python.exe python python3)" ||
    stop_gate tools "" "python was not found"
cargo_command="$(resolve_command cargo.exe cargo)" ||
    stop_gate tools "" "cargo was not found"
git_command="$(resolve_command git.exe git)" ||
    stop_gate tools "" "git was not found"
pdflatex_command=""
if ! pdflatex_command="$(resolve_command pdflatex.exe pdflatex)"; then
    for candidate in \
        "/c/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe" \
        "/mnt/c/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe"; do
        if [[ -f "$candidate" ]]; then
            pdflatex_command="$candidate"
            break
        fi
    done
fi
[[ -n "$pdflatex_command" ]] ||
    stop_gate tools "" "pdflatex was not found on PATH or in MiKTeX"
# scripts/build_provenance_pdf.py looks pdflatex up on PATH.
export PATH="$(dirname -- "$pdflatex_command"):$PATH"
wolframscript_command=""
wolframscript_command="$(resolve_command wolframscript.exe wolframscript)" ||
    wolframscript_command=""
printf 'stage4_tool_python=%s\n' "$python_command"
printf 'stage4_tool_cargo=%s\n' "$cargo_command"
printf 'stage4_tool_git=%s\n' "$git_command"
printf 'stage4_tool_pdflatex=%s\n' "$pdflatex_command"
if [[ -n "$wolframscript_command" ]]; then
    printf 'stage4_tool_wolframscript=%s\n' "$wolframscript_command"
else
    printf '%s\n' 'stage4_tool_wolframscript=NOT FOUND (the Wolfram theory verifier and the Mathematica notebook steps will be skipped)'
fi
# The audit program runs git itself.
export PATH="$(dirname -- "$git_command"):$PATH"

wolfram_limit_pattern='licen[cs]e|password|kernel limit|maximum number of'
wolfram_limit_pattern+='|too many kernels|could not (launch|start|connect)'

step_selected() {
    # step_selected NAME: 0 when the step runs in this invocation
    local name="$1" number wanted
    ((partial == 1)) || return 0
    number="${name:7:2}"
    for wanted in "${selected_steps[@]}"; do
        if [[ "$wanted" == "$name" || "$wanted" == "$number" ]]; then
            return 0
        fi
    done
    return 1
}

run_step() {
    # run_step NAME RETRY(0|1) EXPECTED INPUTS("a|b|..." or "") COMMAND [ARG ...]
    local name="$1" retry="$2" expected="$3" inputs="$4" attempt maximum_attempts=1 log_path code
    local started seconds input missing
    local -a input_list=()
    shift 4
    if ! step_selected "$name"; then
        printf 'stage4_step_not_selected=%s\n' "$name"
        return 0
    fi
    if [[ -n "$inputs" ]]; then
        IFS='|' read -r -a input_list <<<"$inputs"
    fi
    if ((dry_run == 1)); then
        printf 'stage4_dry_run_step=%s expected=[%s]\n' "$name" "$expected"
        printf '    command: %s\n' "$*"
        missing=""
        for input in "${input_list[@]}"; do
            [[ -e "$input" ]] || missing+="${missing:+, }$input"
        done
        [[ -z "$missing" ]] || printf '    missing now: %s\n' "$missing"
        return 0
    fi
    for input in "${input_list[@]}"; do
        [[ -e "$input" ]] || stop_gate "$name" "" "missing input $input"
    done
    if [[ "$retry" == 1 ]]; then
        maximum_attempts=3
    fi
    for ((attempt = 1; attempt <= maximum_attempts; attempt++)); do
        if ((attempt == 1)); then
            log_path="build/logs/$name-bash.log"
        else
            log_path="build/logs/$name-attempt$attempt-bash.log"
        fi
        printf 'stage4_step=%s (expected %s)\n' "$name" "$expected"
        started="$(date +%s)"
        set +e
        # Through "$BASH", so that a missing executable bit (a checkout made
        # on Windows) does not matter.
        "$BASH" "$script_dir/run_logged.sh" "$log_path" -- "$@"
        code=$?
        set -e
        seconds=$(($(date +%s) - started))
        if ((code == 0)); then
            printf 'stage4_step_ok=%s seconds=%d\n' "$name" "$seconds"
            return 0
        fi
        if [[ "$retry" == 1 ]] && ((attempt < maximum_attempts)) &&
            grep -Eiq "$wolfram_limit_pattern" "$log_path"; then
            printf 'stage4_retry=%s attempt %d reported a Wolfram licence or kernel limit; retrying in 30 s\n' \
                "$name" "$attempt"
            sleep 30
            continue
        fi
        stop_gate "$name" "$log_path" "" "$code"
    done
}

skip_step() {
    # skip_step NAME REASON
    if step_selected "$1"; then
        printf 'stage4_skipped_step=%s (%s)\n' "$1" "$2"
    fi
}

# Expected wall time per step (TIMING in the PowerShell twin; same strings).
expect() {
    case "$1" in
        00) printf '%s' "about 10 s" ;;
        01) printf '%s' "about 10 s (about 1 min when the engine is cloned)" ;;
        03) printf '%s' "about 45 s" ;;
        04) printf '%s' "about 3 min" ;;
        10) printf '%s' "PROVISIONAL" ;;
        11) printf '%s' "PROVISIONAL" ;;
        12) printf '%s' "PROVISIONAL" ;;
        14) printf '%s' "PROVISIONAL" ;;
        15 | 16) printf '%s' "about 1 min" ;;
        18) printf '%s' "PROVISIONAL" ;;
        20) printf '%s' "PROVISIONAL" ;;
        25 | 26) printf '%s' "PROVISIONAL" ;;
        30) printf '%s' "PROVISIONAL" ;;
        32 | 33) printf '%s' "PROVISIONAL" ;;
        34) printf '%s' "about 10 s" ;;
        35) printf '%s' "PROVISIONAL" ;;
        *) printf '%s' "seconds" ;;
    esac
}

solver_pin=a8fdff459adfe181573d7924b18bffbdf378fdb3
crate=studies/dirac16complex_kohn_sham
manifest=$crate/Cargo.toml
kohn_sham=artifacts/dirac16complex/kohn-sham
committed_rust=$kohn_sham/rust
stage_build=build/stage4
snapshot=$stage_build/snapshot
theory_build=$stage_build/theory
constants_build=$stage_build/constants
run_a=$stage_build/run-a
refined_root=$stage_build/refined
reference_quick=$stage_build/reference-quick
fresh_check_report=$stage_build/python-check-report.json
fresh_determinism=$stage_build/determinism-report.json
fresh_summary=$stage_build/kohn-sham-summary.json
notebook_name=dirac16complex_kohn_sham.ipynb
committed_notebook=notebooks/$notebook_name
notebook_auditor=notebooks/check_dirac16complex_kohn_sham_notebook.py
clean_notebook=$stage_build/notebook-clean/$notebook_name
executed_notebook=$stage_build/notebook/$notebook_name
nbconvert_directory=$stage_build/nbconvert
nbconvert_notebook=$nbconvert_directory/$notebook_name
fresh_notebook_report=$stage_build/notebook-report.json
mathematica_notebook=notebooks/Dirac16ComplexKohnSham.nb
mathematica_verifier=scripts/verify_dirac16complex_ks_mathematica_notebook.wls
mathematica_report=$kohn_sham/mathematica-report.json
mathematica_figures=$kohn_sham/figures/mathematica
documents=(
    provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL
    provenance/DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE
)
audit=("$python_command" scripts/verify_stage4_kohn_sham_audit.py)
subcommands=(spectrum scf excited thermo emt)
refined_subcommands=(spectrum scf excited emt)
if ((refined_thermo == 1)); then
    refined_subcommands=("${subcommands[@]}")
fi
# Committed files that the gate regenerates in place (figures, Mathematica
# report, .tex/.pdf) or must leave alone; all must end the run byte-identical
# (mathematica-report.json modulo engine.binary).
committed_paths=(
    "$kohn_sham"
    notebooks
    "$crate/src"
    "$manifest"
    "$crate/Cargo.lock"
    "${documents[0]}.md"
    "${documents[0]}.tex"
    "${documents[0]}.pdf"
    "${documents[1]}.md"
    "${documents[1]}.tex"
    "${documents[1]}.pdf"
    provenance/pdf-specifications.json
)

# Inputs read (never rebuilt) by this gate; a full run checks them all before
# the first step, a partial run checks those of the selected steps.
inputs=(
    artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
    "$manifest"
    "$crate/src/generated.rs"
    scripts/generate_dirac16complex_ks_constants.py
    "$kohn_sham/wolfram-kohn-sham-report.json"
    "$kohn_sham/kohn-sham-theory.json"
    "$kohn_sham/python-theory-report.json"
    "$kohn_sham/exchange-table.json"
    "$committed_rust/generator-report.json"
    "$committed_rust/determinism-report.json"
    "$kohn_sham/reference/reference-summary.json"
    "$kohn_sham/python-check-report.json"
    "$kohn_sham/kohn-sham-summary.json"
    "$committed_notebook"
    "$notebook_auditor"
    "$kohn_sham/notebook-report.json"
    "$mathematica_notebook"
    "$mathematica_verifier"
    "$mathematica_report"
    "${documents[0]}.md"
    "${documents[1]}.md"
)
for subcommand in "${subcommands[@]}"; do
    inputs+=("$committed_rust/$subcommand/summary.json")
done
if ((partial == 0 && dry_run == 0)); then
    for input in "${inputs[@]}"; do
        [[ -f "$input" ]] || stop_gate inputs "" "missing $input"
    done
fi

# build/stage4 belongs to this gate: start from an empty directory (a partial
# run keeps it unless it includes the snapshot step 00).
if ((dry_run == 0)) && step_selected stage4-00-snapshot; then
    rm -rf -- "$stage_build"
fi
if ((dry_run == 0)); then
    mkdir -p -- "$stage_build"
fi

run_step stage4-00-snapshot 0 "$(expect 00)" "" \
    "${audit[@]}" snapshot --into "$snapshot" "${committed_paths[@]}"
run_step stage4-01-solver-setup 0 "$(expect 01)" "" \
    "$BASH" scripts/setup_solver.sh win11
run_step stage4-02-solver-pin 0 "$(expect 02)" "" \
    "${audit[@]}" solver --pin "$solver_pin"

# Exact theory.  The sympy checker compares with the committed
# kohn-sham-theory.json (its report records that path and its sha256); step
# 05 proves that the fresh Wolfram theory file is identical to it.
theory_pairs=()
if [[ -n "$wolframscript_command" ]]; then
    run_step stage4-03-theory-wolfram 1 "$(expect 03)" \
        "scripts/verify_dirac16complex_kohn_sham.wls|wolfram/Dirac16ComplexKohnSham.wl" \
        "$wolframscript_command" -file scripts/verify_dirac16complex_kohn_sham.wls \
        "$theory_build/wolfram-kohn-sham-report.json"
    theory_pairs+=(--pair "$kohn_sham/wolfram-kohn-sham-report.json" "$theory_build/wolfram-kohn-sham-report.json"
        --pair "$kohn_sham/kohn-sham-theory.json" "$theory_build/kohn-sham-theory.json")
else
    skip_step stage4-03-theory-wolfram "wolframscript was not found; the exact Wolfram theory verifier was NOT run"
fi
run_step stage4-04-theory-sympy 0 "$(expect 04)" "$kohn_sham/kohn-sham-theory.json" \
    "$python_command" scripts/check_dirac16complex_kohn_sham_theory.py \
    --output "$theory_build/python-theory-report.json" --table "$theory_build/exchange-table.json"
theory_pairs+=(--pair "$kohn_sham/python-theory-report.json" "$theory_build/python-theory-report.json"
    --pair "$kohn_sham/exchange-table.json" "$theory_build/exchange-table.json")
run_step stage4-05-theory-same 0 "$(expect 05)" "" \
    "${audit[@]}" same --rtol 1e-9 --atol 1e-12 "${theory_pairs[@]}"

constants_generator=scripts/generate_dirac16complex_ks_constants.py
if [[ -f "$constants_generator" ]]; then
    run_step stage4-06-constants-check 0 "$(expect 06)" "" \
        "$python_command" "$constants_generator" --check
    run_step stage4-07-constants-regenerate 0 "$(expect 07)" "" \
        "$python_command" "$constants_generator" --output "$constants_build/generated.rs" \
        --report "$constants_build/generator-report.json"
    run_step stage4-08-constants-same 0 "$(expect 08)" "" \
        "${audit[@]}" same --pair "$crate/src/generated.rs" "$constants_build/generated.rs" \
        --pair "$committed_rust/generator-report.json" "$constants_build/generator-report.json"
else
    for name in stage4-06-constants-check stage4-07-constants-regenerate stage4-08-constants-same; do
        skip_step "$name" "$constants_generator does not exist"
    done
fi

run_step stage4-09-cargo-fmt 0 "$(expect 09)" "" \
    "$cargo_command" fmt --manifest-path "$manifest" --check
run_step stage4-10-cargo-clippy 0 "$(expect 10)" "" \
    "$cargo_command" clippy --manifest-path "$manifest" --release --all-targets \
    -- -D warnings
run_step stage4-11-cargo-test 0 "$(expect 11)" "" \
    "$cargo_command" test --manifest-path "$manifest" --release
run_step stage4-12-cargo-build 0 "$(expect 12)" "" \
    "$cargo_command" build --manifest-path "$manifest" --release

binary=$crate/target/release/dirac16complex_kohn_sham.exe
if [[ ! -f "$binary" ]]; then
    binary=$crate/target/release/dirac16complex_kohn_sham
fi
if ((dry_run == 0 && partial == 0)) && [[ ! -f "$binary" ]]; then
    stop_gate binary "" "cargo build did not produce $binary"
fi
printf 'stage4_binary=%s\n' "$binary"

run_step stage4-13-print-config 0 "$(expect 13)" "$binary" "./$binary" print-config

# The canonical tree (every subcommand into build/stage4/run-a) and the
# refined tree (build/stage4/refined), launched by the audit program: all
# processes concurrently, or one after another with --sequential-rust.
rust_jobs=()
for subcommand in "${subcommands[@]}"; do
    rust_jobs+=(--job "$subcommand" "$run_a" canonical)
done
for subcommand in "${refined_subcommands[@]}"; do
    rust_jobs+=(--job "$subcommand" "$refined_root" refined)
done
rust_mode=()
if ((sequential_rust == 1)); then
    rust_mode=(--sequential)
fi
rust_expected="$(expect 14)"
if ((refined_thermo == 1)); then
    rust_expected+="; with thermo --refined: PROVISIONAL"
fi
run_step stage4-14-rust-runs 0 "$rust_expected" "$binary" \
    "${audit[@]}" rust-run --binary "$binary" --log-prefix build/logs/stage4-14-rust-runs-bash \
    "${rust_mode[@]}" "${rust_jobs[@]}"
run_step stage4-15-rust-compare 0 "$(expect 15)" "" \
    "${audit[@]}" rust-outputs --committed "$committed_rust" --run "$run_a"
determinism_options=()
if ((refined_thermo == 1)); then
    determinism_options=(--full-refined)
fi
run_step stage4-16-determinism 0 "$(expect 16)" "" \
    "$python_command" "$crate/tools/compare_runs.py" --canonical "$committed_rust" \
    --repeat "$run_a" --refined "$refined_root" --report "$fresh_determinism"
run_step stage4-17-determinism-audit 0 "$(expect 17)" "$committed_rust/determinism-report.json" \
    "${audit[@]}" determinism --committed "$committed_rust/determinism-report.json" \
    --fresh "$fresh_determinism" "${determinism_options[@]}"

# The Python reference solver: its --quick self-tests and reduced parameter
# set (the canonical reference run takes several hours and is not repeated),
# then the cross-checker on the committed trees with the gate's run-a and
# refined trees as --repeat / --refined.
run_step stage4-18-reference-quick 0 "$(expect 18)" "" \
    "$python_command" scripts/ks_reference_solver.py --quick --output "$reference_quick"
run_step stage4-19-reference-quick-audit 0 "$(expect 19)" "" \
    "${audit[@]}" reference-quick --summary "$reference_quick/reference-summary.json"
run_step stage4-20-cross-check 0 "$(expect 20)" "$kohn_sham/reference/reference-summary.json" \
    "$python_command" scripts/check_dirac16complex_kohn_sham.py --rust "$committed_rust" \
    --repeat "$run_a" --refined "$refined_root" --report "$fresh_check_report"
run_step stage4-21-cross-check-audit 0 "$(expect 21)" "$kohn_sham/python-check-report.json" \
    "${audit[@]}" checker-report --committed "$kohn_sham/python-check-report.json" \
    --fresh "$fresh_check_report"
run_step stage4-22-summary 0 "$(expect 22)" "" \
    "$python_command" "$crate/tools/build_kohn_sham_summary.py" --output "$fresh_summary"
run_step stage4-23-summary-same 0 "$(expect 23)" "$kohn_sham/kohn-sham-summary.json" \
    "${audit[@]}" same --pair "$kohn_sham/kohn-sham-summary.json" "$fresh_summary"

run_step stage4-24-notebook-prepare 0 "$(expect 24)" "$committed_notebook" \
    "${audit[@]}" prepare-notebook --source "$committed_notebook" \
    --dest "$clean_notebook" --dest "$executed_notebook"
run_step stage4-25-notebook-run 0 "$(expect 25)" "" \
    "$python_command" notebooks/run_notebook.py "$executed_notebook"
run_step stage4-26-notebook-nbconvert 0 "$(expect 26)" "" \
    "$python_command" -m nbconvert --to notebook --execute "$clean_notebook" \
    --output-dir "$nbconvert_directory" --ExecutePreprocessor.timeout=3600 \
    --ExecutePreprocessor.startup_timeout=600
run_step stage4-27-notebook-audit 0 "$(expect 27)" "$notebook_auditor" \
    "$python_command" "$notebook_auditor" "$executed_notebook" \
    --also "$nbconvert_notebook" --report "$fresh_notebook_report"
run_step stage4-28-notebook-compare 0 "$(expect 28)" "$kohn_sham/notebook-report.json" \
    "${audit[@]}" notebook --committed-report "$kohn_sham/notebook-report.json" \
    --fresh-report "$fresh_notebook_report" \
    --committed-notebook "$committed_notebook" \
    --fresh-notebook "$executed_notebook"
run_step stage4-29-figures-unchanged 0 "$(expect 29)" "" \
    "${audit[@]}" unchanged --snapshot "$snapshot" "$kohn_sham/figures"

mathematica_ran=0
if [[ -n "$wolframscript_command" ]]; then
    run_step stage4-30-mathematica-notebook 1 "$(expect 30)" "$mathematica_notebook|$mathematica_verifier" \
        "$wolframscript_command" -file "$mathematica_verifier"
    run_step stage4-31-mathematica-unchanged 0 "$(expect 31)" "$mathematica_report" \
        "${audit[@]}" unchanged --snapshot "$snapshot" \
        --ignore-json-key engine.binary "$mathematica_report" "$mathematica_figures"
    mathematica_ran=1
else
    skip_step stage4-30-mathematica-notebook "wolframscript was not found on PATH; $mathematica_notebook was NOT evaluated"
    skip_step stage4-31-mathematica-unchanged "no Mathematica run"
fi

run_step stage4-32-pdf-primordial 0 "$(expect 32)" "${documents[0]}.md" \
    "$python_command" scripts/build_provenance_pdf.py "${documents[0]}.md"
# The student guide is built in the developer layout of the PDF builder
# (ragged table columns, breakable code spans), as registered; without the
# flag the builder writes a different .tex.
run_step stage4-33-pdf-student-guide 0 "$(expect 33)" "${documents[1]}.md" \
    "$python_command" scripts/build_provenance_pdf.py --developer-layout \
    "${documents[1]}.md"
run_step stage4-34-committed-unchanged 0 "$(expect 34)" "" \
    "${audit[@]}" unchanged --snapshot "$snapshot" \
    --ignore-json-key engine.binary "${committed_paths[@]}"
run_step stage4-35-unit-tests 0 "$(expect 35)" "" \
    "$python_command" -m unittest discover -s tests -p "test_d16c_kohn_sham*.py" -v

outputs=(
    "$theory_build/python-theory-report.json"
    "$theory_build/exchange-table.json"
    "$constants_build/generated.rs"
    "$constants_build/generator-report.json"
)
if [[ -n "$wolframscript_command" ]]; then
    outputs+=("$theory_build/wolfram-kohn-sham-report.json" "$theory_build/kohn-sham-theory.json")
fi
for subcommand in "${subcommands[@]}"; do
    outputs+=("$run_a/$subcommand/summary.json")
done
for subcommand in "${refined_subcommands[@]}"; do
    outputs+=("$refined_root/$subcommand/summary.json")
done
outputs+=(
    "$fresh_determinism"
    "$reference_quick/reference-summary.json"
    "$fresh_check_report"
    "$fresh_summary"
    "$executed_notebook"
    "$nbconvert_notebook"
    "$fresh_notebook_report"
)
if ((mathematica_ran == 1)); then
    outputs+=("$mathematica_report")
fi
for document in "${documents[@]}"; do
    outputs+=("$document.tex" "$document.pdf")
done
run_step stage4-36-fresh-outputs 0 "$(expect 36)" "" \
    "${audit[@]}" fresh --since "$gate_started_epoch" "${outputs[@]}"

if ((dry_run == 1)); then
    printf '%s\n' 'stage4_kohn_sham_verification=DRY-RUN'
    exit 0
fi
if ((partial == 1)); then
    printf 'stage4_selected_steps=%s\n' "$(IFS=,; printf '%s' "${selected_steps[*]}")"
    printf '%s\n' 'stage4_kohn_sham_verification=PARTIAL'
    exit 3
fi
if [[ -z "$wolframscript_command" ]]; then
    printf '%s\n' 'stage4_wolfram=SKIPPED (wolframscript not found: the exact Wolfram theory verifier and the Mathematica notebook were not run; every other step passed)'
fi
printf '%s\n' 'stage4_kohn_sham_verification=OK'
