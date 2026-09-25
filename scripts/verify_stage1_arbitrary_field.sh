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
#
# Every step runs through scripts/run_logged.sh with its log in build/logs/
# (*-bash.log, so the PowerShell twin's logs are not overwritten; build/ is
# git-ignored).  The gate stops at the first failing step and prints
# stage1_failed_step, stage1_failed_log and
# stage1_arbitrary_field_verification=FAILED.  A Wolfram step whose log shows
# a licence or kernel-limit message is retried after 30 s, at most 3 attempts
# (each attempt keeps its own log).  After the steps the gate requires that
# both Wolfram reports and provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{tex,pdf}
# were rewritten during this run and that every check in the two Wolfram
# reports is true.  Only then does it print
#   stage1_arbitrary_field_verification=OK
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
        "$script_dir/run_logged.sh" "$log_path" -- "$@"
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

algebra_report=artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json
geometry_report=artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json
provenance_markdown=provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md

run_step stage1-01-build-fixture 0 \
    "$python_command" scripts/build_dirac16complex_fixture.py
run_step stage1-02-check-algebra 0 \
    "$python_command" scripts/check_dirac16complex_algebra.py
# No "--" before the report path: WolframScript 1.14.0 drops "--" and every
# argument after it from $ScriptCommandLine (see the header).
run_step stage1-03-wolfram-algebra 1 \
    "$wolframscript_command" -file scripts/verify_dirac16complex_algebra.wls \
    "$algebra_report"
run_step stage1-04-wolfram-geometry 1 \
    "$wolframscript_command" -file scripts/verify_dirac16complex_geometry.wls \
    "$geometry_report"
run_step stage1-05-check-geometry 0 \
    "$python_command" scripts/check_dirac16complex_geometry.py
run_step stage1-06-grassmann-demo 0 \
    "$python_command" scripts/demo_grassmann_lagrangians.py
run_step stage1-07-check-algebra-crosscheck 0 \
    "$python_command" scripts/check_dirac16complex_algebra.py
run_step stage1-08-python-tests 0 \
    "$python_command" -m unittest discover -s tests -v
run_step stage1-09-provenance-pdf 0 \
    "$python_command" scripts/build_provenance_pdf.py "$provenance_markdown"

outputs=(
    "$algebra_report"
    "$geometry_report"
    provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.tex
    provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf
)
for output in "${outputs[@]}"; do
    [[ -f "$output" ]] || stop_gate outputs "" "missing $output"
    modified_epoch="$(
        stat -c %Y -- "$output" 2>/dev/null || stat -f %m -- "$output"
    )"
    if ((modified_epoch < gate_started_epoch)); then
        stop_gate outputs "" "$output was not rewritten by this run"
    fi
done

for report in "$algebra_report" "$geometry_report"; do
    audit="$(
        "$python_command" - "$report" <<'PYTHON'
import json
import sys

path = sys.argv[1]
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
    if failed:
        print(f"FAIL {path} failed checks: {','.join(failed)}")
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
printf '%s\n' 'stage1_arbitrary_field_verification=OK'
