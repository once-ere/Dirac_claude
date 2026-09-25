#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 1 gate (dirac16complex in an arbitrary gravitational field).
# Twin of scripts/verify_stage1_arbitrary_field.ps1; the step list, the
# checks and the final line are the same.  Modelled on the verify_phase*.sh
# gates of https://github.com/once-ere/dirac (GPL-3.0-or-later), with the
# command resolution of its scripts/resolve_wolframscript.sh inlined.
#
# Run from any directory with Git Bash or WSL:
#   bash scripts/verify_stage1_arbitrary_field.sh
# Before the provenance document exists (Stage 1 integration), the steps up
# to, but not including, the provenance PDF step can be run with
#   bash scripts/verify_stage1_arbitrary_field.sh --skip-provenance-pdf
# which audits everything except the .tex/.pdf and then prints
#   stage1_arbitrary_field_verification=INCOMPLETE
# and exits 3: a run with --skip-provenance-pdf never prints OK.
#
# Every step runs through scripts/run_logged.sh with its log in build/logs/
# (*-bash.log, so the PowerShell twin's logs are not overwritten; build/ is
# git-ignored).  The gate stops at the first failing step and prints
# stage1_failed_step, stage1_failed_log and
# stage1_arbitrary_field_verification=FAILED.  A Wolfram step whose log shows
# a licence or kernel-limit message is retried after 30 s, at most 3 attempts
# (each attempt keeps its own log).  After the steps the gate requires that
# the five Stage 1 reports, stage1-summary.json and
# provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{tex,pdf} were rewritten during
# this run, that every check in the five reports is true, and that the
# cross-implementation checks ALG_fixtureAgreement (Wolfram reads the Python
# fixture), ALG_wolframAgreement and GEO_wolframAgreement (Python reads the
# Wolfram reports) are present and true.  Only then does it print
#   stage1_arbitrary_field_verification=OK
# Step 02 runs the Python algebra checker without the Wolfram comparison
# (--wolfram-report=), because the Wolfram report on disk may predate this
# run; step 07 repeats it against the report written by step 03.  The unit
# test steps run the Stage 1 test files only (tests/test_d16c_[ag]*.py, i.e.
# algebra, geometry and the arbitrary-field publication test, and
# tests/test_publication_tooling.py); Stage 2 and Stage 3 tests have their
# own gates.
# Step 12 runs tests/test_d16c_arbitrary_field_publication.py once more, after
# the summary (step 10) and the provenance PDF (step 11) have been rebuilt:
# that test compares the stage1-summary.json hash quoted in the document with
# the file on disk, and step 08 runs before step 10 rewrites the summary.
# PYTHONUTF8=1 is exported for this process only, so that Python output
# containing Greek letters survives the pipes.
#
# The Wolfram report paths are passed as plain positional script arguments,
# NOT after "--" as in the dirac-main gates: with WolframScript 1.14.0,
# "wolframscript -file s.wls -- r.json" gives $ScriptCommandLine = {"s.wls"}
# (the "--" and everything after it are dropped; checked from PowerShell 7.6
# and Git Bash on 2026-09-25), whereas "wolframscript -file s.wls r.json"
# gives {"s.wls", "r.json"}.  Scripts that filter "--" out of
# Rest[$ScriptCommandLine] read the path the same way in both forms.
set -euo pipefail

skip_provenance_pdf=0
for argument in "$@"; do
    case "$argument" in
        --skip-provenance-pdf) skip_provenance_pdf=1 ;;
        *)
            printf 'usage: %s [--skip-provenance-pdf]\n' "$0" >&2
            exit 2
            ;;
    esac
done

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
cd -- "$repository_root"
gate_started_epoch="$(date +%s)"
export PYTHONUTF8=1

stop_gate() {
    # stop_gate STEP LOG REASON [CODE]
    printf 'stage1_failed_step=%s\n' "$1"
    [[ -z "$2" ]] || printf 'stage1_failed_log=%s\n' "$2"
    [[ -z "$3" ]] || printf 'stage1_failure_reason=%s\n' "$3"
    printf '%s\n' 'stage1_arbitrary_field_verification=FAILED'
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

# The Windows executables come first, as in dirac-main, so that Git Bash and
# WSL use the same Python (with numpy and sympy) as the PowerShell twin.
python_command="$(resolve_command python.exe python python3)" ||
    stop_gate tools "" "python was not found"
wolframscript_command="$(resolve_command wolframscript.exe wolframscript)" ||
    stop_gate tools "" "wolframscript was not found"
pdflatex_command=""
if ! pdflatex_command="$(resolve_command pdflatex.exe pdflatex)"; then
    for candidate in \
        "/c/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe" \
        "/mnt/c/Program Files/MiKTeX/miktex/bin/x64/pdflatex.exe"; do
        if [[ -f "$candidate" ]]; then
            pdflatex_command="$candidate"
            export PATH="$(dirname -- "$candidate"):$PATH"
            break
        fi
    done
fi
[[ -n "$pdflatex_command" ]] ||
    stop_gate tools "" "pdflatex was not found on PATH or in MiKTeX"
printf 'stage1_tool_python=%s\n' "$python_command"
printf 'stage1_tool_wolframscript=%s\n' "$wolframscript_command"
printf 'stage1_tool_pdflatex=%s\n' "$pdflatex_command"

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
        printf 'stage1_step=%s\n' "$name"
        set +e
        # Through "$BASH", so that a missing executable bit (a checkout made
        # on Windows) does not matter.
        "$BASH" "$script_dir/run_logged.sh" "$log_path" -- "$@"
        code=$?
        set -e
        if ((code == 0)); then
            printf 'stage1_step_ok=%s\n' "$name"
            return 0
        fi
        if [[ "$retry" == 1 ]] && ((attempt < maximum_attempts)) &&
            grep -Eiq "$wolfram_limit_pattern" "$log_path"; then
            printf 'stage1_retry=%s attempt %d reported a Wolfram licence or kernel limit; retrying in 30 s\n' \
                "$name" "$attempt"
            sleep 30
            continue
        fi
        stop_gate "$name" "$log_path" "" "$code"
    done
}

artifact_directory=artifacts/dirac16complex/arbitrary-field
algebra_report=$artifact_directory/wolfram-algebra-report.json
geometry_report=$artifact_directory/wolfram-geometry-report.json
python_algebra_report=$artifact_directory/python-algebra-report.json
python_geometry_report=$artifact_directory/python-geometry-report.json
grassmann_report=$artifact_directory/grassmann-demo-report.json
summary_report=$artifact_directory/stage1-summary.json
provenance_markdown=provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md

run_step stage1-01-build-fixture 0 \
    "$python_command" scripts/build_dirac16complex_fixture.py
# Python-only pass: the Wolfram report on disk may predate this run.
run_step stage1-02-check-algebra 0 \
    "$python_command" scripts/check_dirac16complex_algebra.py --wolfram-report=
# No "--" before the report path: WolframScript 1.14.0 drops "--" and every
# argument after it from $ScriptCommandLine (see the header).
run_step stage1-03-wolfram-algebra 1 \
    "$wolframscript_command" -file scripts/verify_dirac16complex_algebra.wls \
    "$algebra_report"
run_step stage1-04-wolfram-geometry 1 \
    "$wolframscript_command" -file scripts/verify_dirac16complex_geometry.wls \
    "$geometry_report"
# Reads the Wolfram geometry report written by step 04 (GEO_wolframAgreement).
run_step stage1-05-check-geometry 0 \
    "$python_command" scripts/check_dirac16complex_geometry.py \
    --wolfram-report "$geometry_report"
run_step stage1-06-grassmann-demo 0 \
    "$python_command" scripts/demo_grassmann_lagrangians.py
# Reads the Wolfram algebra report written by step 03 (ALG_wolframAgreement).
run_step stage1-07-check-algebra-crosscheck 0 \
    "$python_command" scripts/check_dirac16complex_algebra.py \
    --wolfram-report "$algebra_report"
run_step stage1-08-python-tests 0 \
    "$python_command" -m unittest discover -s tests -p 'test_d16c_[ag]*.py' -v
run_step stage1-09-publication-tests 0 \
    "$python_command" -m unittest discover -s tests \
    -p 'test_publication_tooling.py' -v
run_step stage1-10-summary 0 \
    "$python_command" scripts/build_stage1_summary.py --output "$summary_report"
if ((skip_provenance_pdf == 0)); then
    run_step stage1-11-provenance-pdf 0 \
        "$python_command" scripts/build_provenance_pdf.py "$provenance_markdown"
    # Repeats the publication test against the summary and PDF just rebuilt.
    run_step stage1-12-publication-recheck 0 \
        "$python_command" -m unittest discover -s tests \
        -p 'test_d16c_arbitrary_field_publication.py' -v
fi

outputs=(
    "$algebra_report"
    "$geometry_report"
    "$python_algebra_report"
    "$python_geometry_report"
    "$grassmann_report"
    "$summary_report"
)
if ((skip_provenance_pdf == 0)); then
    outputs+=(
        provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.tex
        provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf
    )
fi
for output in "${outputs[@]}"; do
    [[ -f "$output" ]] || stop_gate outputs "" "missing $output"
    modified_epoch="$(
        stat -c %Y -- "$output" 2>/dev/null || stat -f %m -- "$output"
    )"
    if ((modified_epoch < gate_started_epoch)); then
        stop_gate outputs "" "$output was not rewritten by this run"
    fi
done

# Each report with the cross-implementation checks it must contain.
audit_specs=(
    "$algebra_report ALG_fixtureAgreement"
    "$geometry_report"
    "$python_algebra_report ALG_fixtureAgreement ALG_wolframAgreement"
    "$python_geometry_report GEO_wolframAgreement"
    "$grassmann_report"
)
for audit_spec in "${audit_specs[@]}"; do
    read -r -a audit_arguments <<<"$audit_spec"
    report="${audit_arguments[0]}"
    audit="$(
        "$python_command" - "${audit_arguments[@]}" <<'PYTHON'
import json
import sys

path = sys.argv[1]
required = sys.argv[2:]
try:
    with open(path, "rb") as handle:
        report = json.loads(handle.read().decode("utf-8"))
except (OSError, ValueError) as error:
    print(f"FAIL {path} is not valid UTF-8 JSON: {error}")
    raise SystemExit(0)
if not isinstance(report, dict):
    print(f"FAIL {path} top level is not a JSON object")
    raise SystemExit(0)
checks = report.get("checks")
if report.get("schemaVersion") != 1:
    print(f"FAIL {path} schemaVersion is not 1")
elif not isinstance(checks, dict) or not checks:
    print(f"FAIL {path} has no non-empty checks object")
else:
    failed = [name for name, value in checks.items() if value is not True]
    missing = [name for name in required if name not in checks]
    if failed:
        print(f"FAIL {path} failed checks: {','.join(failed)}")
    elif missing:
        print(f"FAIL {path} lacks the agreement checks: {','.join(missing)}")
    else:
        print(f"OK {path} {len(checks)} true")
PYTHON
    )" || stop_gate reports "" "could not audit $report"
    audit="${audit%$'\r'}"
    case "$audit" in
        "OK "*) printf 'stage1_report_checks=%s\n' "${audit#OK }" ;;
        *) stop_gate reports "" "${audit#FAIL }" ;;
    esac
done

for output in "${outputs[@]}"; do
    printf 'stage1_sha256=%s  %s\n' \
        "$(sha256sum -- "$output" | cut -d' ' -f1)" "$output"
done
if ((skip_provenance_pdf == 1)); then
    printf 'stage1_skipped_step=stage1-11-provenance-pdf,stage1-12-publication-recheck (--skip-provenance-pdf; %s not built or checked)\n' \
        "$provenance_markdown"
    printf '%s\n' 'stage1_arbitrary_field_verification=INCOMPLETE'
    exit 3
fi
printf '%s\n' 'stage1_arbitrary_field_verification=OK'
