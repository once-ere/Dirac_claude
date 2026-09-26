#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 3 gate (dirac16complex dark-sector numerics).
# Twin of scripts/verify_stage3_dark_sector.ps1; the step list, the checks
# and the final line are the same.  Same pattern as the Stage 1 and Stage 2
# gates scripts/verify_stage1_arbitrary_field.sh and
# scripts/verify_stage2_primordial_field.sh, themselves modelled on the
# verify_phase*.sh gates of https://github.com/once-ere/dirac
# (GPL-3.0-or-later), with the command resolution of its
# scripts/resolve_wolframscript.sh inlined.  The comparisons are made by one
# program, scripts/verify_stage3_dark_sector_audit.py, which both twins
# call, so that both apply exactly the same rules.
#
# Run from any directory with Git Bash or WSL:
#   bash scripts/verify_stage3_dark_sector.sh
#
# Needs: python (numpy, matplotlib, nbformat, nbclient, nbconvert,
# ipykernel), cargo with rustfmt and clippy, git, pdflatex (PATH or
# MiKTeX); wolframscript is optional: without it the Mathematica step is
# skipped with the message stage3_skipped_step=... and the final line says
# which cross-check was not run.  Every step runs through
# scripts/run_logged.sh with its log in build/logs/ (*-bash.log, so the
# PowerShell twin's logs are not overwritten; build/ is git-ignored; the gate
# deletes and recreates only build/stage3/).  The gate stops at the first
# failing step and prints stage3_failed_step, stage3_failed_log and
# stage3_dark_sector_verification=FAILED.  A Wolfram step whose log shows a
# licence or kernel-limit message is retried after 30 s, at most 3 attempts.
#
# Steps:
#   stage3-00-snapshot            copy the committed Stage-3 files (numerics
#       artifacts, notebooks, the two documents and pdf-specifications.json)
#       into build/stage3/snapshot, for the unchanged checks below
#   stage3-01-solver-setup        bash scripts/setup_solver.sh win11
#       (clones vendor/rustSolveIt if absent; refuses another commit).  The
#       committed outputs were produced with the Win11 engine a8fdff45, so
#       the gate pins that engine on every platform (NUMERICS_CONTRACT
#       erratum: it reproduces them byte for byte on Windows and Linux)
#   stage3-02-solver-pin          HEAD is exactly the pin, no tracked file of
#       the engine is modified, the two path dependencies exist
#   stage3-03..06                 cargo fmt --check; cargo clippy --release
#       --all-targets -- -D warnings; cargo test --release; cargo build
#       --release (studies/dirac16complex_cosmology, from the repository root
#       so that .cargo/config.toml applies)
#   stage3-07/08-run-a/run-b      dirac16complex_cosmology all --output
#       build/stage3/run-a (resp. run-b); last line SUCCESS
#   stage3-09-compare-outputs     every file of every experiment (the files
#       list of the committed summary.json, 62 files) is byte-identical in
#       run-a, run-b and artifacts/dirac16complex/numerics/exp*/
#   stage3-10-analysis-exp3       scripts/analyze_dirac16complex_exp3.py
#       --output build/stage3/run-a
#   stage3-11-compare-analysis    fits.json, fits_scan.csv, fits_mu_scan.csv
#       equal the committed ones (bytes, else value by value)
#   stage3-12..16-check-expN      scripts/check_dirac16complex_expN.py
#       --output build/stage3/run-a --repeat build/stage3/repeat
#       --refined build/stage3/refined (the checkers, the notebook and the
#       Mathematica notebook all run the binary built by stage3-06 at its
#       default path studies/dirac16complex_cosmology/target/release/)
#   stage3-17-audit-reports       the five fresh checker reports: all checks
#       true, repeatByteIdentity and refinedConvergence present, the same
#       check names as the committed reports
#   stage3-18/19-numerics-summary build_numerics_summary.py --output
#       build/stage3/run-a; same totals as the committed numerics-summary.json
#   stage3-20..24-notebook        a copy of the Jupyter notebook with all
#       outputs cleared is executed headless by notebooks/run_notebook.py
#       (build/stage3/notebook/) and by python -m nbconvert --execute
#       (build/stage3/nbconvert/), audited by notebooks/check_notebook.py
#       (report build/stage3/notebook-report.json), and that report must
#       equal the committed notebook-report.json except the notebook paths
#   stage3-25-figures-unchanged   the notebook rewrote the committed figures
#       byte for byte
#   stage3-26-mathematica-notebook  wolframscript -file
#       scripts/verify_dirac16complex_mathematica_notebook.wls (skipped
#       without wolframscript)
#   stage3-27-mathematica-unchanged the Mathematica notebook rewrote
#       mathematica-report.json (modulo the platform-specific engine.binary)
#       and its 8 figures byte for byte
#   stage3-28/29-pdf-*            python scripts/build_provenance_pdf.py for
#       DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md and (with --developer-layout,
#       as registered) DIRAC16COMPLEX_STUDENT_GUIDE.md (verify mode: the
#       rebuilt PDF must match its edition in provenance/pdf-specifications.json:
#       path, page count, sha256)
#   stage3-30-committed-unchanged every snapshotted committed file is
#       byte-identical at the end of the run
#   stage3-31-unit-tests          python -m unittest discover -s tests -v
#   stage3-32-fresh-outputs       the gate's outputs were written during this
#       run; their sha256 are printed
# Only then does it print
#   stage3_dark_sector_verification=OK
# PYTHONUTF8=1 is exported for this process only, so that Python output
# containing Greek letters survives the pipes.
#
# The Wolfram notebook path is not passed at all (the verifier's default is
# notebooks/Dirac16ComplexDarkSector.nb); WolframScript 1.14.0 drops "--" and
# every argument after it from $ScriptCommandLine (see the Stage 1 gate).
set -euo pipefail

if (($# != 0)); then
    printf 'usage: %s\n' "$0" >&2
    exit 2
fi

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
cd -- "$repository_root"
gate_started_epoch="$(date +%s)"
export PYTHONUTF8=1

stop_gate() {
    # stop_gate STEP LOG REASON [CODE]
    printf 'stage3_failed_step=%s\n' "$1"
    [[ -z "$2" ]] || printf 'stage3_failed_log=%s\n' "$2"
    [[ -z "$3" ]] || printf 'stage3_failure_reason=%s\n' "$3"
    printf '%s\n' 'stage3_dark_sector_verification=FAILED'
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

# The Windows executables come first, as in the Stage 1 gate, so that Git
# Bash and WSL use the same Python (with numpy, matplotlib and the Jupyter
# packages) and the same Rust toolchain as the PowerShell twin.
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
printf 'stage3_tool_python=%s\n' "$python_command"
printf 'stage3_tool_cargo=%s\n' "$cargo_command"
printf 'stage3_tool_git=%s\n' "$git_command"
printf 'stage3_tool_pdflatex=%s\n' "$pdflatex_command"
if [[ -n "$wolframscript_command" ]]; then
    printf 'stage3_tool_wolframscript=%s\n' "$wolframscript_command"
else
    printf '%s\n' 'stage3_tool_wolframscript=NOT FOUND (the Mathematica notebook step will be skipped)'
fi
# The audit program runs git itself.
export PATH="$(dirname -- "$git_command"):$PATH"

wolfram_limit_pattern='licen[cs]e|password|kernel limit|maximum number of'
wolfram_limit_pattern+='|too many kernels|could not (launch|start|connect)'

run_step() {
    # run_step NAME RETRY(0|1) COMMAND [ARG ...]
    local name="$1" retry="$2" attempt maximum_attempts=1 log_path code
    shift 2
    if [[ "$retry" == 1 ]]; then
        maximum_attempts=3
    fi
    for ((attempt = 1; attempt <= maximum_attempts; attempt++)); do
        if ((attempt == 1)); then
            log_path="build/logs/$name-bash.log"
        else
            log_path="build/logs/$name-attempt$attempt-bash.log"
        fi
        printf 'stage3_step=%s\n' "$name"
        set +e
        # Through "$BASH", so that a missing executable bit (a checkout made
        # on Windows) does not matter.
        "$BASH" "$script_dir/run_logged.sh" "$log_path" -- "$@"
        code=$?
        set -e
        if ((code == 0)); then
            printf 'stage3_step_ok=%s\n' "$name"
            return 0
        fi
        if [[ "$retry" == 1 ]] && ((attempt < maximum_attempts)) &&
            grep -Eiq "$wolfram_limit_pattern" "$log_path"; then
            printf 'stage3_retry=%s attempt %d reported a Wolfram licence or kernel limit; retrying in 30 s\n' \
                "$name" "$attempt"
            sleep 30
            continue
        fi
        stop_gate "$name" "$log_path" "" "$code"
    done
}

solver_pin=a8fdff459adfe181573d7924b18bffbdf378fdb3
manifest=studies/dirac16complex_cosmology/Cargo.toml
numerics=artifacts/dirac16complex/numerics
stage_build=build/stage3
run_a=$stage_build/run-a
run_b=$stage_build/run-b
repeat_root=$stage_build/repeat
refined_root=$stage_build/refined
snapshot=$stage_build/snapshot
notebook_name=dirac16complex_dark_sector.ipynb
committed_notebook=notebooks/$notebook_name
clean_notebook=$stage_build/notebook-clean/$notebook_name
executed_notebook=$stage_build/notebook/$notebook_name
nbconvert_directory=$stage_build/nbconvert
nbconvert_notebook=$nbconvert_directory/$notebook_name
fresh_notebook_report=$stage_build/notebook-report.json
mathematica_report=$numerics/mathematica-report.json
mathematica_figures=$numerics/figures/mathematica
documents=(
    provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS
    provenance/DIRAC16COMPLEX_STUDENT_GUIDE
)
audit=("$python_command" scripts/verify_stage3_dark_sector_audit.py)
# Committed Stage-3 files that the gate regenerates in place (figures,
# Mathematica report, .tex/.pdf) or must leave alone; all must end the run
# byte-identical (mathematica-report.json modulo engine.binary).
committed_paths=(
    "$numerics"
    notebooks
    provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md
    provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.tex
    provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.pdf
    provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md
    provenance/DIRAC16COMPLEX_STUDENT_GUIDE.tex
    provenance/DIRAC16COMPLEX_STUDENT_GUIDE.pdf
    provenance/pdf-specifications.json
)

# Inputs read (never rebuilt) by this gate.
inputs=(
    artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
    "$manifest"
    studies/dirac16complex_cosmology/src/generated.rs
    "$committed_notebook"
    notebooks/Dirac16ComplexDarkSector.nb
    "$numerics/notebook-report.json"
    "$mathematica_report"
    "$numerics/numerics-summary.json"
)
for input in "${inputs[@]}"; do
    [[ -f "$input" ]] || stop_gate inputs "" "missing $input"
done

# build/stage3 belongs to this gate: start from an empty directory.
rm -rf -- "$stage_build"
mkdir -p -- "$stage_build"

run_step stage3-00-snapshot 0 \
    "${audit[@]}" snapshot --into "$snapshot" "${committed_paths[@]}"
run_step stage3-01-solver-setup 0 \
    "$BASH" scripts/setup_solver.sh win11
run_step stage3-02-solver-pin 0 \
    "${audit[@]}" solver --pin "$solver_pin"
run_step stage3-03-cargo-fmt 0 \
    "$cargo_command" fmt --manifest-path "$manifest" --check
run_step stage3-04-cargo-clippy 0 \
    "$cargo_command" clippy --manifest-path "$manifest" --release --all-targets \
    -- -D warnings
run_step stage3-05-cargo-test 0 \
    "$cargo_command" test --manifest-path "$manifest" --release
run_step stage3-06-cargo-build 0 \
    "$cargo_command" build --manifest-path "$manifest" --release

binary=studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe
if [[ ! -f "$binary" ]]; then
    binary=studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology
fi
[[ -f "$binary" ]] || stop_gate binary "" "cargo build did not produce $binary"
printf 'stage3_binary=%s\n' "$binary"

run_step stage3-07-run-a 0 "./$binary" all --output "$run_a"
run_step stage3-08-run-b 0 "./$binary" all --output "$run_b"
run_step stage3-09-compare-outputs 0 \
    "${audit[@]}" outputs --committed "$numerics" --run "$run_a" --run "$run_b"
run_step stage3-10-analysis-exp3 0 \
    "$python_command" scripts/analyze_dirac16complex_exp3.py --output "$run_a"
run_step stage3-11-compare-analysis 0 \
    "${audit[@]}" analysis --committed "$numerics" --fresh "$run_a"
checker_number=12
for experiment in 1 2 3 4 5; do
    run_step "stage3-$checker_number-check-exp$experiment" 0 \
        "$python_command" "scripts/check_dirac16complex_exp$experiment.py" \
        --output "$run_a" --repeat "$repeat_root" --refined "$refined_root"
    checker_number=$((checker_number + 1))
done
run_step stage3-17-audit-reports 0 \
    "${audit[@]}" reports --committed "$numerics" --fresh "$run_a"
run_step stage3-18-numerics-summary 0 \
    "$python_command" studies/dirac16complex_cosmology/tools/build_numerics_summary.py \
    --output "$run_a"
run_step stage3-19-compare-numerics-summary 0 \
    "${audit[@]}" numerics-summary --committed "$numerics" --fresh "$run_a"

run_step stage3-20-notebook-prepare 0 \
    "${audit[@]}" prepare-notebook --source "$committed_notebook" \
    --dest "$clean_notebook" --dest "$executed_notebook"
run_step stage3-21-notebook-run 0 \
    "$python_command" notebooks/run_notebook.py "$executed_notebook"
run_step stage3-22-notebook-nbconvert 0 \
    "$python_command" -m nbconvert --to notebook --execute "$clean_notebook" \
    --output-dir "$nbconvert_directory" --ExecutePreprocessor.timeout=3600
run_step stage3-23-notebook-audit 0 \
    "$python_command" notebooks/check_notebook.py "$executed_notebook" \
    --also "$nbconvert_notebook" --report "$fresh_notebook_report"
run_step stage3-24-notebook-compare 0 \
    "${audit[@]}" notebook --committed-report "$numerics/notebook-report.json" \
    --fresh-report "$fresh_notebook_report" \
    --committed-notebook "$committed_notebook" \
    --fresh-notebook "$executed_notebook"
run_step stage3-25-figures-unchanged 0 \
    "${audit[@]}" unchanged --snapshot "$snapshot" "$numerics/figures"

mathematica_ran=0
if [[ -n "$wolframscript_command" ]]; then
    run_step stage3-26-mathematica-notebook 1 \
        "$wolframscript_command" -file \
        scripts/verify_dirac16complex_mathematica_notebook.wls
    run_step stage3-27-mathematica-unchanged 0 \
        "${audit[@]}" unchanged --snapshot "$snapshot" \
        --ignore-json-key engine.binary "$mathematica_report" "$mathematica_figures"
    mathematica_ran=1
else
    printf '%s\n' 'stage3_skipped_step=stage3-26-mathematica-notebook,stage3-27-mathematica-unchanged (wolframscript was not found on PATH; the Mathematica notebook notebooks/Dirac16ComplexDarkSector.nb was NOT evaluated)'
fi

run_step stage3-28-pdf-numerics 0 \
    "$python_command" scripts/build_provenance_pdf.py "${documents[0]}.md"
# The student guide is built in the builder's developer layout (ragged table
# columns, breakable code spans), as registered and as its publication test
# requires; without the flag the builder writes a different .tex.
run_step stage3-29-pdf-student-guide 0 \
    "$python_command" scripts/build_provenance_pdf.py --developer-layout \
    "${documents[1]}.md"
run_step stage3-30-committed-unchanged 0 \
    "${audit[@]}" unchanged --snapshot "$snapshot" \
    --ignore-json-key engine.binary "${committed_paths[@]}"
run_step stage3-31-unit-tests 0 \
    "$python_command" -m unittest discover -s tests -v

outputs=()
for root in "$run_a" "$run_b"; do
    for experiment in 1 2 3 4 5; do
        outputs+=("$root/exp$experiment/summary.json")
    done
done
for experiment in 1 2 3 4 5; do
    outputs+=("$run_a/exp$experiment/python-check-report.json")
done
outputs+=(
    "$run_a/exp3/fits.json"
    "$run_a/numerics-summary.json"
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
run_step stage3-32-fresh-outputs 0 \
    "${audit[@]}" fresh --since "$gate_started_epoch" "${outputs[@]}"

if ((mathematica_ran == 0)); then
    printf '%s\n' 'stage3_mathematica=SKIPPED (wolframscript not found; every other step passed)'
fi
printf '%s\n' 'stage3_dark_sector_verification=OK'
