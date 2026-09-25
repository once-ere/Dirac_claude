#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 2 gate (dirac16complex in the notebook's primordial field).
# Twin of scripts/verify_stage2_primordial_field.ps1; the step list, the
# checks and the final line are the same.  Same pattern as the Stage 1 gate
# scripts/verify_stage1_arbitrary_field.sh, itself modelled on the
# verify_phase*.sh gates of https://github.com/once-ere/dirac
# (GPL-3.0-or-later), with the command resolution of its
# scripts/resolve_wolframscript.sh inlined.
#
# Run from any directory with Git Bash or WSL:
#   bash scripts/verify_stage2_primordial_field.sh
#
# Steps (each through scripts/run_logged.sh, log in build/logs/*-bash.log so
# that the PowerShell twin's logs are not overwritten; build/ is git-ignored):
#   stage2-01-wolfram-primordial  wolframscript -file
#       scripts/verify_dirac16complex_primordial.wls <report>
#       (writes wolfram-primordial-report.json and primordial-components.json)
#   stage2-02-check-primordial    python scripts/check_dirac16complex_primordial.py
#       (independent sympy checker; its default invocation requires
#       primordial-components.json and runs P_EL_agreesWithWolfram)
#   stage2-03-python-tests        python -m unittest discover -s tests
#       -p "test_d16c_primordial*.py" -v
#   stage2-04-provenance-pdf      python scripts/build_provenance_pdf.py
#       provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md (verify mode: the edition
#       must already be registered in provenance/pdf-specifications.json)
# Stage 1 files are inputs only: the gate requires the committed algebra
# fixture and the notebook to exist but never rebuilds them.
#
# The gate stops at the first failing step and prints stage2_failed_step,
# stage2_failed_log and stage2_primordial_field_verification=FAILED.  A
# Wolfram step whose log shows a licence or kernel-limit message is retried
# after 30 s, at most 3 attempts (each attempt keeps its own log).  After the
# steps the gate requires that the two Wolfram outputs, the Python report and
# provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.{tex,pdf} were rewritten during
# this run, that every check in the Wolfram and Python reports is true, and
# that the Python report ran P_EL_agreesWithWolfram (wolframAgreement =
# compared) against the primordial-components.json of this run (same
# sha256).  Only then does it print
#   stage2_primordial_field_verification=OK
# PYTHONUTF8=1 is exported for this process only, so that Python output
# containing Greek letters survives the pipes.
#
# The Wolfram report path is passed as a plain positional script argument,
# NOT after "--" as in the dirac-main gates: with WolframScript 1.14.0,
# "wolframscript -file s.wls -- r.json" gives $ScriptCommandLine = {"s.wls"}
# (the "--" and everything after it are dropped), whereas
# "wolframscript -file s.wls r.json" gives {"s.wls", "r.json"}.
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
cd -- "$repository_root"
gate_started_epoch="$(date +%s)"
export PYTHONUTF8=1

stop_gate() {
    # stop_gate STEP LOG REASON [CODE]
    printf 'stage2_failed_step=%s\n' "$1"
    [[ -z "$2" ]] || printf 'stage2_failed_log=%s\n' "$2"
    [[ -z "$3" ]] || printf 'stage2_failure_reason=%s\n' "$3"
    printf '%s\n' 'stage2_primordial_field_verification=FAILED'
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
printf 'stage2_tool_python=%s\n' "$python_command"
printf 'stage2_tool_wolframscript=%s\n' "$wolframscript_command"
printf 'stage2_tool_pdflatex=%s\n' "$pdflatex_command"

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
        printf 'stage2_step=%s\n' "$name"
        set +e
        # Through "$BASH", so that a missing executable bit (a checkout made
        # on Windows) does not matter.
        "$BASH" "$script_dir/run_logged.sh" "$log_path" -- "$@"
        code=$?
        set -e
        if ((code == 0)); then
            printf 'stage2_step_ok=%s\n' "$name"
            return 0
        fi
        if [[ "$retry" == 1 ]] && ((attempt < maximum_attempts)) &&
            grep -Eiq "$wolfram_limit_pattern" "$log_path"; then
            printf 'stage2_retry=%s attempt %d reported a Wolfram licence or kernel limit; retrying in 30 s\n' \
                "$name" "$attempt"
            sleep 30
            continue
        fi
        stop_gate "$name" "$log_path" "" "$code"
    done
}

wolfram_report=artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json
wolfram_components=artifacts/dirac16complex/primordial-field/primordial-components.json
python_report=artifacts/dirac16complex/primordial-field/python-primordial-report.json
provenance_markdown=provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md

# Stage 1 and notebook inputs (read, never rebuilt, by this gate).
inputs=(
    artifacts/dirac16complex/arbitrary-field/algebra-fixture.json
    "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb"
    wolfram/Dirac16ComplexPrimordial.wl
)
for input in "${inputs[@]}"; do
    [[ -f "$input" ]] || stop_gate inputs "" "missing $input"
done

# No "--" before the report path: WolframScript 1.14.0 drops "--" and every
# argument after it from $ScriptCommandLine (see the header).
run_step stage2-01-wolfram-primordial 1 \
    "$wolframscript_command" -file scripts/verify_dirac16complex_primordial.wls \
    "$wolfram_report"
run_step stage2-02-check-primordial 0 \
    "$python_command" scripts/check_dirac16complex_primordial.py
run_step stage2-03-python-tests 0 \
    "$python_command" -m unittest discover -s tests \
    -p 'test_d16c_primordial*.py' -v
run_step stage2-04-provenance-pdf 0 \
    "$python_command" scripts/build_provenance_pdf.py "$provenance_markdown"

outputs=(
    "$wolfram_report"
    "$wolfram_components"
    "$python_report"
    provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.tex
    provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.pdf
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

# The same audit program as in the PowerShell twin.  With a second argument
# (the component file) it also requires P_EL_agreesWithWolfram = true,
# wolframAgreement = compared and an inputSha256 entry for that file equal to
# its current sha256.
audit_report() {
    "$python_command" - "$@" <<'PYTHON'
import hashlib
import json
import sys

path = sys.argv[1]
components = sys.argv[2] if len(sys.argv) > 2 else None
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
    raise SystemExit(0)
if not isinstance(checks, dict) or not checks:
    print(f"FAIL {path} has no non-empty checks object")
    raise SystemExit(0)
failed = [name for name, value in checks.items() if value is not True]
if failed:
    print(f"FAIL {path} failed checks: {','.join(failed)}")
    raise SystemExit(0)
if components is not None:
    measurements = report.get("measurements")
    inputs = report.get("inputSha256")
    agreement = (measurements.get("wolframAgreement")
                 if isinstance(measurements, dict) else None)
    try:
        with open(components, "rb") as handle:
            current = hashlib.sha256(handle.read()).hexdigest()
    except OSError as error:
        print(f"FAIL {components} cannot be read: {error}")
        raise SystemExit(0)
    recorded = inputs.get(components) if isinstance(inputs, dict) else None
    if checks.get("P_EL_agreesWithWolfram") is not True:
        print(f"FAIL {path} did not run P_EL_agreesWithWolfram")
        raise SystemExit(0)
    if agreement != "compared":
        print(f"FAIL {path} wolframAgreement is {agreement!r}, not 'compared'")
        raise SystemExit(0)
    if recorded != current:
        print(f"FAIL {path} compared a different {components} "
              f"(recorded {recorded}, current {current})")
        raise SystemExit(0)
    print(f"OK {path} {len(checks)} true, wolframAgreement=compared")
else:
    print(f"OK {path} {len(checks)} true")
PYTHON
}

check_audit() {
    # check_audit REPORT [COMPONENTS]
    local audit
    audit="$(audit_report "$@")" || stop_gate reports "" "could not audit $1"
    audit="${audit%$'\r'}"
    case "$audit" in
        "OK "*) printf 'stage2_report_checks=%s\n' "${audit#OK }" ;;
        *) stop_gate reports "" "${audit#FAIL }" ;;
    esac
}
check_audit "$wolfram_report"
check_audit "$python_report" "$wolfram_components"

for output in "${outputs[@]}"; do
    printf 'stage2_sha256=%s  %s\n' \
        "$(sha256sum -- "$output" | cut -d' ' -f1)" "$output"
done
printf '%s\n' 'stage2_primordial_field_verification=OK'
