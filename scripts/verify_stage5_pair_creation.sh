#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 5 gate (dirac16complex and dirac16complex00: the exact {+M, -M}
# pairing theory, the Kohn-Sham pairs of both fields, the two documents).
# Twin of scripts/verify_stage5_pair_creation.ps1; the step list, the checks
# and the final line are the same.  Same pattern as the Stage 4 gate
# scripts/verify_stage4_kohn_sham.sh (itself modelled on the Stage 3 gate and
# the verify_phase*.sh gates of https://github.com/once-ere/dirac,
# GPL-3.0-or-later, with the command resolution of its
# scripts/resolve_wolframscript.sh inlined).  The comparisons, and the launch
# of the Rust runs and of the reference reproduction, are made by one
# program, scripts/verify_stage5_pair_creation_audit.py, which both twins
# call, so that both apply exactly the same rules.
#
# Run from any directory with Git Bash or WSL:
#   bash scripts/verify_stage5_pair_creation.sh
#
# Options (the full gate uses none of them):
#   --dry-run          print every step with its expected wall time and command,
#                      run nothing; last line stage5_pair_creation_verification=DRY-RUN
#   --steps 03,04,...  run only the listed steps (two-digit numbers or full
#                      names; build/stage5 is kept unless step 00 is listed);
#                      the last line is then stage5_pair_creation_verification=PARTIAL
#                      (exit 3), never OK
#   --sequential-rust  run the Rust processes of steps 11 and 14 one after
#                      another instead of concurrently (same outputs)
#
# Needs: python (numpy, sympy, mpmath, matplotlib), cargo with rustfmt and
# clippy, git, pdflatex (PATH or MiKTeX); wolframscript is optional: without
# it the two exact Wolfram verifiers (steps 01, 02) are skipped with the
# message stage5_skipped_step=..., and the line before the final line says
# which cross-checks were not run.  Every step runs through
# scripts/run_logged.sh with its log in build/logs/ (*-bash.log, so the
# PowerShell twin's logs are not overwritten; build/ is git-ignored; the gate
# deletes and recreates only build/stage5/).  The gate stops at the first
# failing step and prints stage5_failed_step, stage5_failed_log and
# stage5_pair_creation_verification=FAILED.  A Wolfram step whose log shows a
# licence or kernel-limit message is retried after 30 s, at most 3 attempts;
# a Wolfram step whose log contains "Failed to open file" FAILS even when
# wolframscript exits 0 (audit wolfram-log).  Never two gates at once: the
# gate holds the lock directory build/stage5.lock (shared with the PowerShell
# twin; removed when the gate ends, also on failure); a second gate stops at
# once with stage5_failed_step=lock.
#
# What is and is not re-run, the step list (stage5-00 .. stage5-29), the
# interface required from scripts/build_dirac16complex_pairs_figures.py and
# the measured wall time of every step (TIMING): see the header of the
# PowerShell twin scripts/verify_stage5_pair_creation.ps1; --dry-run prints
# the expected wall time of every step.
#
# The Wolfram report paths are passed positionally, never after "--"
# (WolframScript 1.14 drops "--" and every argument after it).
set -euo pipefail

dry_run=0
sequential_rust=0
steps_option=""
usage() {
    printf 'usage: %s [--dry-run] [--steps LIST] [--sequential-rust]\n' "$0" >&2
    exit 2
}
while (($# > 0)); do
    case "$1" in
        --dry-run) dry_run=1 ;;
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
lock_directory=build/stage5.lock
lock_held=0

release_lock() {
    if ((lock_held == 1)); then
        rm -rf -- "$lock_directory"
        lock_held=0
    fi
}
trap release_lock EXIT

stop_gate() {
    # stop_gate STEP LOG REASON [CODE]
    printf 'stage5_failed_step=%s\n' "$1"
    [[ -z "$2" ]] || printf 'stage5_failed_log=%s\n' "$2"
    [[ -z "$3" ]] || printf 'stage5_failure_reason=%s\n' "$3"
    printf '%s\n' 'stage5_pair_creation_verification=FAILED'
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

# The Windows executables come first, as in the Stage 1, 3 and 4 gates, so
# that Git Bash and WSL use the same Python and the same Rust toolchain as
# the PowerShell twin.
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
printf 'stage5_tool_python=%s\n' "$python_command"
printf 'stage5_tool_cargo=%s\n' "$cargo_command"
printf 'stage5_tool_git=%s\n' "$git_command"
printf 'stage5_tool_pdflatex=%s\n' "$pdflatex_command"
if [[ -n "$wolframscript_command" ]]; then
    printf 'stage5_tool_wolframscript=%s\n' "$wolframscript_command"
else
    printf '%s\n' 'stage5_tool_wolframscript=NOT FOUND (the two exact Wolfram verifier steps will be skipped)'
fi
# The audit program and the PDF builder run git themselves.
export PATH="$(dirname -- "$git_command"):$PATH"

wolfram_limit_pattern='licen[cs]e|password|kernel limit|maximum number of'
wolfram_limit_pattern+='|too many kernels|could not (launch|start|connect)'
audit=("$python_command" scripts/verify_stage5_pair_creation_audit.py)

# Never two gates at once (either twin): mkdir is atomic and fails when the
# lock directory exists (another gate runs, or one was killed).
if ((dry_run == 0)); then
    mkdir -p -- build
    if ! mkdir -- "$lock_directory" 2>/dev/null; then
        owner="$(cat -- "$lock_directory/owner" 2>/dev/null || true)"
        stop_gate lock "" "another Stage-5 gate holds build/stage5.lock (${owner}); never run two gates at once (remove the directory by hand only when no gate runs)"
    fi
    lock_held=1
    printf 'pid=%s twin=sh started_utc=%s\n' "$$" "$(date -u +'%Y-%m-%dT%H:%M:%SZ')" >"$lock_directory/owner"
fi

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
    # run_step NAME WOLFRAM(0|1) EXPECTED INPUTS("a|b|..." or "") COMMAND [ARG ...]
    local name="$1" wolfram="$2" expected="$3" inputs="$4" attempt maximum_attempts=1 log_path code
    local started seconds input missing
    local -a input_list=()
    shift 4
    if ! step_selected "$name"; then
        printf 'stage5_step_not_selected=%s\n' "$name"
        return 0
    fi
    if [[ -n "$inputs" ]]; then
        IFS='|' read -r -a input_list <<<"$inputs"
    fi
    if ((dry_run == 1)); then
        printf 'stage5_dry_run_step=%s expected=[%s]\n' "$name" "$expected"
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
    if [[ "$wolfram" == 1 ]]; then
        maximum_attempts=3
    fi
    for ((attempt = 1; attempt <= maximum_attempts; attempt++)); do
        if ((attempt == 1)); then
            log_path="build/logs/$name-bash.log"
        else
            log_path="build/logs/$name-attempt$attempt-bash.log"
        fi
        printf 'stage5_step=%s (expected %s)\n' "$name" "$expected"
        started="$(date +%s)"
        set +e
        # Through "$BASH", so that a missing executable bit (a checkout made
        # on Windows) does not matter.
        "$BASH" "$script_dir/run_logged.sh" "$log_path" -- "$@"
        code=$?
        set -e
        seconds=$(($(date +%s) - started))
        if ((code == 0)) && [[ "$wolfram" == 1 ]]; then
            # wolframscript can print "Failed to open file" and still exit 0.
            "${audit[@]}" wolfram-log --log "$log_path" ||
                stop_gate "$name" "$log_path" "wolframscript printed 'Failed to open file' (exit code 0 is not accepted)"
        fi
        if ((code == 0)); then
            printf 'stage5_step_ok=%s seconds=%d\n' "$name" "$seconds"
            return 0
        fi
        if [[ "$wolfram" == 1 ]] && ((attempt < maximum_attempts)) &&
            grep -Eiq "$wolfram_limit_pattern" "$log_path"; then
            printf 'stage5_retry=%s attempt %d reported a Wolfram licence or kernel limit; retrying in 30 s\n' \
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
        printf 'stage5_skipped_step=%s (%s)\n' "$1" "$2"
    fi
}

# Expected wall time per step (TIMING in the PowerShell twin; same strings).
expect() {
    case "$1" in
        01) printf '%s' "about 4-12 min (its provenance file, part 4.3)" ;;
        02) printf '%s' "about 4-12 min (its provenance file, part 4.5)" ;;
        03) printf '%s' "about 3.5 min (213 s on 2026-10-15, under load)" ;;
        04) printf '%s' "about 1 min (68 s on 2026-10-15, under load)" ;;
        08) printf '%s' "about 1-2 min (estimate)" ;;
        11) printf '%s' "about 7 min (estimate, see TIMING)" ;;
        14) printf '%s' "about 3-5 h (estimate, see TIMING)" ;;
        16) printf '%s' "under 1 min (estimate)" ;;
        18 | 20 | 21) printf '%s' "minutes (estimate, not measured)" ;;
        23) printf '%s' "not measured (script written after the runs)" ;;
        25 | 26) printf '%s' "under 1 min (Stage-3 analogue)" ;;
        28) printf '%s' "about 4 min (225 s on 2026-10-15)" ;;
        *) printf '%s' "seconds" ;;
    esac
}

crate=studies/dirac16complex_kohn_sham
manifest=$crate/Cargo.toml
pair_creation=artifacts/dirac16complex/pair-creation
committed_rust=$pair_creation/rust
committed_reference=$pair_creation/reference
committed_figures=$pair_creation/figures
stage4_rust=artifacts/dirac16complex/kohn-sham/rust
stage_build=build/stage5
snapshot=$stage_build/snapshot
theory_build=$stage_build/theory
identity_run=$stage_build/stage4-identity
fresh_identity=$stage_build/stage4-identity-report.json
run_a=$stage_build/run-a
refined_root=$stage_build/refined
fresh_determinism=$stage_build/determinism-report.json
reference_quick=$stage_build/reference-quick
reference_reproduce=$stage_build/reference-reproduce
fresh_check_report=$stage_build/python-pairs-check-report.json
figures_build=$stage_build/figures
figures_script=scripts/build_dirac16complex_pairs_figures.py
compare_pairs=$crate/tools/compare_pairs_runs.py
documents=(
    provenance/DIRAC16COMPLEX00_FIELD_THEORY
    provenance/DIRAC16COMPLEX_PAIR_CREATION
)
# Committed files that the gate regenerates in place (.tex/.pdf) or must
# leave alone; all must end the run byte-identical.
committed_paths=(
    "$pair_creation"
    "$stage4_rust"
    wolfram/Dirac16Complex00.wl
    wolfram/Dirac16ComplexPairing.wl
    "$crate/src"
    "$crate/tools"
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
    wolfram/Dirac16Complex00.wl
    wolfram/Dirac16ComplexPairing.wl
    scripts/verify_dirac16complex00.wls
    scripts/verify_dirac16complex_pairing.wls
    scripts/check_dirac16complex00.py
    scripts/check_dirac16complex_pairing.py
    scripts/check_dirac16complex_pairs.py
    scripts/ks_reference_pairs.py
    "$compare_pairs"
    "$pair_creation/wolfram-dirac16complex00-report.json"
    "$pair_creation/dirac16complex00-theory.json"
    "$pair_creation/wolfram-pairing-report.json"
    "$pair_creation/pairing-theory.json"
    "$pair_creation/python-dirac16complex00-report.json"
    "$pair_creation/python-pairing-report.json"
    "$pair_creation/python-pairs-check-report.json"
    "$committed_rust/stage4-identity-report.json"
    "$committed_rust/determinism-report.json"
    "$committed_rust/pairs/summary.json"
    "$committed_reference/reference-pairs-summary.json"
    "$figures_script"
    "${documents[0]}.md"
    "${documents[0]}.tex"
    "${documents[0]}.pdf"
    "${documents[1]}.md"
    "${documents[1]}.tex"
    "${documents[1]}.pdf"
    provenance/pdf-specifications.json
    "$manifest"
)
for subcommand in spectrum scf excited; do
    inputs+=("$stage4_rust/$subcommand/summary.json")
done
if ((partial == 0 && dry_run == 0)); then
    for input in "${inputs[@]}"; do
        [[ -f "$input" ]] || stop_gate inputs "" "missing $input"
    done
    [[ -d "$committed_figures" ]] || stop_gate inputs "" "missing $committed_figures/"
fi

# build/stage5 belongs to this gate: start from an empty directory (a partial
# run keeps it unless it includes the snapshot step 00).
if ((dry_run == 0)) && step_selected stage5-00-snapshot; then
    rm -rf -- "$stage_build"
fi
if ((dry_run == 0)); then
    mkdir -p -- "$stage_build"
fi

run_step stage5-00-snapshot 0 "$(expect 00)" "" \
    "${audit[@]}" snapshot --into "$snapshot" "${committed_paths[@]}"

# Exact theory.  The sympy checkers compare with the committed Wolfram files
# (their reports record those paths and sha256); step 05 proves that the
# fresh Wolfram files are identical to them.
theory_pairs=()
if [[ -n "$wolframscript_command" ]]; then
    run_step stage5-01-theory-wolfram-00 1 "$(expect 01)" \
        "scripts/verify_dirac16complex00.wls|wolfram/Dirac16Complex00.wl" \
        "$wolframscript_command" -file scripts/verify_dirac16complex00.wls \
        "$theory_build/wolfram-dirac16complex00-report.json"
    run_step stage5-02-theory-wolfram-pairing 1 "$(expect 02)" \
        "scripts/verify_dirac16complex_pairing.wls|wolfram/Dirac16ComplexPairing.wl" \
        "$wolframscript_command" -file scripts/verify_dirac16complex_pairing.wls \
        "$theory_build/wolfram-pairing-report.json"
    theory_pairs+=(--pair "$pair_creation/wolfram-dirac16complex00-report.json" "$theory_build/wolfram-dirac16complex00-report.json"
        --pair "$pair_creation/dirac16complex00-theory.json" "$theory_build/dirac16complex00-theory.json"
        --pair "$pair_creation/wolfram-pairing-report.json" "$theory_build/wolfram-pairing-report.json"
        --pair "$pair_creation/pairing-theory.json" "$theory_build/pairing-theory.json")
else
    skip_step stage5-01-theory-wolfram-00 "wolframscript was not found; the exact Wolfram verifier of dirac16complex00 was NOT run"
    skip_step stage5-02-theory-wolfram-pairing "wolframscript was not found; the exact Wolfram verifier of the pairing theorems was NOT run"
fi
run_step stage5-03-theory-sympy-00 0 "$(expect 03)" "$pair_creation/dirac16complex00-theory.json" \
    "$python_command" scripts/check_dirac16complex00.py \
    --output "$theory_build/python-dirac16complex00-report.json"
run_step stage5-04-theory-sympy-pairing 0 "$(expect 04)" "$pair_creation/pairing-theory.json" \
    "$python_command" scripts/check_dirac16complex_pairing.py \
    --output "$theory_build/python-pairing-report.json"
theory_pairs+=(--pair "$pair_creation/python-dirac16complex00-report.json" "$theory_build/python-dirac16complex00-report.json"
    --pair "$pair_creation/python-pairing-report.json" "$theory_build/python-pairing-report.json")
run_step stage5-05-theory-same 0 "$(expect 05)" "" \
    "${audit[@]}" same --rtol 1e-9 --atol 1e-12 "${theory_pairs[@]}"

run_step stage5-06-cargo-fmt 0 "$(expect 06)" "" \
    "$cargo_command" fmt --manifest-path "$manifest" --check
run_step stage5-07-cargo-clippy 0 "$(expect 07)" "" \
    "$cargo_command" clippy --manifest-path "$manifest" --release --all-targets \
    -- -D warnings
run_step stage5-08-cargo-test 0 "$(expect 08)" "" \
    "$cargo_command" test --manifest-path "$manifest" --release
run_step stage5-09-cargo-build 0 "$(expect 09)" "" \
    "$cargo_command" build --manifest-path "$manifest" --release

binary=$crate/target/release/dirac16complex_kohn_sham.exe
if [[ ! -f "$binary" ]]; then
    binary=$crate/target/release/dirac16complex_kohn_sham
fi
if ((dry_run == 0 && partial == 0)) && [[ ! -f "$binary" ]]; then
    stop_gate binary "" "cargo build did not produce $binary"
fi
printf 'stage5_binary=%s\n' "$binary"
rust_mode=()
if ((sequential_rust == 1)); then
    rust_mode=(--sequential)
fi

run_step stage5-10-print-config 0 "$(expect 10)" "$binary" "./$binary" print-config

# The Stage-4 subcommands of the Stage-5 binary must reproduce the committed
# Stage-4 bytes (STAGE5_SPEC section 6): spectrum in full, scf and excited in
# their --quick subsets, as recorded in rust/stage4-identity-report.json.
run_step stage5-11-stage4-identity-runs 0 "$(expect 11)" "$binary" \
    "${audit[@]}" rust-run --binary "$binary" --log-prefix build/logs/stage5-11-stage4-identity-bash \
    "${rust_mode[@]}" --job spectrum "$identity_run" canonical --job scf "$identity_run" quick \
    --job excited "$identity_run" quick
run_step stage5-12-stage4-identity-compare 0 "$(expect 12)" "" \
    "$python_command" "$compare_pairs" --stage4-committed "$stage4_rust" --stage4-run "$identity_run" \
    --full spectrum --quick excited scf --binary "$binary" --report "$fresh_identity"
run_step stage5-13-stage4-identity-audit 0 "$(expect 13)" "$committed_rust/stage4-identity-report.json" \
    "${audit[@]}" report --fresh "$fresh_identity" --committed "$committed_rust/stage4-identity-report.json"

# The canonical pairs tree (build/stage5/run-a) and the refined pairs tree
# (build/stage5/refined), launched by the audit program.
run_step stage5-14-rust-pairs 0 "$(expect 14)" "$binary" \
    "${audit[@]}" rust-run --binary "$binary" --log-prefix build/logs/stage5-14-rust-pairs-bash \
    "${rust_mode[@]}" --job pairs "$run_a" canonical --job pairs "$refined_root" refined
run_step stage5-15-rust-pairs-compare 0 "$(expect 15)" "$committed_rust/pairs/summary.json" \
    "${audit[@]}" rust-outputs --committed "$committed_rust" --run "$run_a" --sub pairs
run_step stage5-16-pairs-determinism 0 "$(expect 16)" "" \
    "$python_command" "$compare_pairs" --canonical "$committed_rust" --repeat "$run_a" \
    --refined "$refined_root" --binary "$binary" --report "$fresh_determinism"
run_step stage5-17-pairs-determinism-audit 0 "$(expect 17)" "$committed_rust/determinism-report.json" \
    "${audit[@]}" report --fresh "$fresh_determinism" --committed "$committed_rust/determinism-report.json"

# The Python reference pairs runner: its --quick matrix, and the
# re-execution of the committed N = 8, lambda = 0, T = 0 pairs on the
# canonical grids (the canonical reference run takes several hours and is
# not repeated); then the pairs checker on the committed trees with the
# gate's run-a and refined trees as --repeat / --refined.
run_step stage5-18-reference-quick 0 "$(expect 18)" "" \
    "$python_command" scripts/ks_reference_pairs.py --quick --output "$reference_quick"
run_step stage5-19-reference-quick-audit 0 "$(expect 19)" "" \
    "${audit[@]}" reference-quick --summary "$reference_quick/reference-pairs-summary.json"
run_step stage5-20-reference-reproduce 0 "$(expect 20)" "$committed_reference/reference-pairs-summary.json" \
    "${audit[@]}" reference-reproduce --committed "$committed_reference" --output "$reference_reproduce" \
    --log build/logs/stage5-20-reference-reproduce-runner-bash.log
run_step stage5-21-pairs-check 0 "$(expect 21)" \
    "$committed_reference/reference-pairs-summary.json|$committed_rust/pairs/summary.json" \
    "$python_command" scripts/check_dirac16complex_pairs.py --reference "$committed_reference" \
    --rust "$committed_rust" --theory "$pair_creation/pairing-theory.json" --repeat "$run_a" \
    --refined "$refined_root" --report "$fresh_check_report"
run_step stage5-22-pairs-check-audit 0 "$(expect 22)" "$pair_creation/python-pairs-check-report.json" \
    "${audit[@]}" report --fresh "$fresh_check_report" --committed "$pair_creation/python-pairs-check-report.json" \
    --require-check rust_repeat_byte_identity --require-check rust_refined_convergence

# The figures of the pairs (document B, section 7): the script is written by
# the lead after the runs; until then this step fails with "missing input".
run_step stage5-23-figures 0 "$(expect 23)" "$figures_script|$committed_figures" \
    "$python_command" "$figures_script" --output "$figures_build"
run_step stage5-24-figures-same 0 "$(expect 24)" "$committed_figures" \
    "${audit[@]}" tree-same --committed "$committed_figures" --fresh "$figures_build"

run_step stage5-25-pdf-field-theory 0 "$(expect 25)" "${documents[0]}.md" \
    "$python_command" scripts/build_provenance_pdf.py "${documents[0]}.md"
run_step stage5-26-pdf-pair-creation 0 "$(expect 26)" "${documents[1]}.md" \
    "$python_command" scripts/build_provenance_pdf.py "${documents[1]}.md"
run_step stage5-27-committed-unchanged 0 "$(expect 27)" "" \
    "${audit[@]}" unchanged --snapshot "$snapshot" "${committed_paths[@]}"
run_step stage5-28-unit-tests 0 "$(expect 28)" "" \
    "$python_command" -m unittest discover -s tests -p "test_d16c_stage5*.py" -v

outputs=(
    "$theory_build/python-dirac16complex00-report.json"
    "$theory_build/python-pairing-report.json"
)
if [[ -n "$wolframscript_command" ]]; then
    outputs+=("$theory_build/wolfram-dirac16complex00-report.json" "$theory_build/dirac16complex00-theory.json"
        "$theory_build/wolfram-pairing-report.json" "$theory_build/pairing-theory.json")
fi
outputs+=(
    "$identity_run/spectrum/summary.json"
    "$identity_run/scf/summary.json"
    "$identity_run/excited/summary.json"
    "$fresh_identity"
    "$run_a/pairs/summary.json"
    "$refined_root/pairs/summary.json"
    "$fresh_determinism"
    "$reference_quick/reference-pairs-summary.json"
    "$reference_reproduce/reference-pairs-summary.json"
    "$fresh_check_report"
)
for document in "${documents[@]}"; do
    outputs+=("$document.tex" "$document.pdf")
done
run_step stage5-29-fresh-outputs 0 "$(expect 29)" "" \
    "${audit[@]}" fresh --since "$gate_started_epoch" "${outputs[@]}"

release_lock
if ((dry_run == 1)); then
    printf '%s\n' 'stage5_pair_creation_verification=DRY-RUN'
    exit 0
fi
if ((partial == 1)); then
    printf 'stage5_selected_steps=%s\n' "$(IFS=,; printf '%s' "${selected_steps[*]}")"
    printf '%s\n' 'stage5_pair_creation_verification=PARTIAL'
    exit 3
fi
if [[ -z "$wolframscript_command" ]]; then
    printf '%s\n' 'stage5_wolfram=SKIPPED (wolframscript not found: the two exact Wolfram verifiers were not run; every other step passed)'
fi
printf '%s\n' 'stage5_pair_creation_verification=OK'
