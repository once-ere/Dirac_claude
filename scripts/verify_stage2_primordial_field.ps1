# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 2 gate (dirac16complex in the notebook's primordial field).
# Twin of scripts/verify_stage2_primordial_field.sh; the step list, the
# checks and the final line are the same.  Same pattern as the Stage 1 gate
# scripts/verify_stage1_arbitrary_field.ps1, itself modelled on the
# verify_phase*.ps1 gates of https://github.com/once-ere/dirac
# (GPL-3.0-or-later).
#
# Run from any directory with PowerShell 7:
#   pwsh -NoProfile -File scripts/verify_stage2_primordial_field.ps1
# Started from Windows PowerShell 5.1 (for example
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify_stage2_primordial_field.ps1)
# the gate re-runs itself under pwsh (PATH, else
# %ProgramFiles%\PowerShell\7\pwsh.exe) and exits with its exit code:
# scripts/run_logged.ps1 uses -Encoding utf8NoBOM, which Windows PowerShell
# 5.1 rejects.
#
# Steps (each through scripts/run_logged.ps1, log in build/logs/; build/ is
# git-ignored):
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
# PYTHONUTF8=1 and a UTF-8 console encoding are set for this process only,
# so that Python output containing Greek letters survives the pipes.
#
# The Wolfram report path is passed as a plain positional script argument,
# NOT after "--" as in the dirac-main gates: with WolframScript 1.14.0,
# "wolframscript -file s.wls -- r.json" gives $ScriptCommandLine = {"s.wls"}
# (the "--" and everything after it are dropped), whereas
# "wolframscript -file s.wls r.json" gives {"s.wls", "r.json"}.
[CmdletBinding()]
param()

if ($PSVersionTable.PSEdition -ne "Core") {
    $pwshCommand = Get-Command pwsh -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    $pwshPath = if ($pwshCommand) {
        $pwshCommand.Source
    } else {
        Join-Path $env:ProgramFiles "PowerShell\7\pwsh.exe"
    }
    if (-not (Test-Path -LiteralPath $pwshPath -PathType Leaf)) {
        Write-Output "stage2_failed_step=tools"
        Write-Output ("stage2_failure_reason=PowerShell 7 (pwsh) is required " +
            "and was not found on PATH or at $pwshPath")
        Write-Output "stage2_primordial_field_verification=FAILED"
        exit 1
    }
    [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
    & $pwshPath -NoProfile -ExecutionPolicy Bypass -File $PSCommandPath
    exit $LASTEXITCODE
}

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repositoryRoot
$gateStartedUtc = [DateTime]::UtcNow
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

function Stop-Gate {
    param([string]$Step, [string]$Log, [string]$Reason, [int]$Code = 1)
    Write-Output "stage2_failed_step=$Step"
    if ($Log) { Write-Output "stage2_failed_log=$Log" }
    if ($Reason) { Write-Output "stage2_failure_reason=$Reason" }
    Write-Output "stage2_primordial_field_verification=FAILED"
    if ($Code -eq 0) { $Code = 1 }
    exit $Code
}

foreach ($tool in @("python", "wolframscript")) {
    $resolved = Get-Command $tool -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $resolved) {
        Stop-Gate -Step "tools" -Reason "$tool was not found on PATH"
    }
    Write-Output "stage2_tool_$tool=$($resolved.Source)"
}
if (-not (Get-Command pdflatex -CommandType Application `
        -ErrorAction SilentlyContinue)) {
    $miktexBin = Join-Path $env:ProgramFiles "MiKTeX\miktex\bin\x64"
    if (-not (Test-Path -LiteralPath (Join-Path $miktexBin "pdflatex.exe"))) {
        Stop-Gate -Step "tools" `
            -Reason "pdflatex was not found on PATH or in $miktexBin"
    }
    $env:Path = "$miktexBin;$env:Path"
}
$pdflatexCommand = Get-Command pdflatex -CommandType Application |
    Select-Object -First 1
Write-Output "stage2_tool_pdflatex=$($pdflatexCommand.Source)"

$wolframLimitPattern = "licen[cs]e|password|kernel limit|maximum number of" +
    "|too many kernels|could not (launch|start|connect)"

function Invoke-GateStep {
    param(
        [string]$Name,
        [string]$Command,
        [switch]$WolframRetry
    )
    $maximumAttempts = if ($WolframRetry) { 3 } else { 1 }
    for ($attempt = 1; $attempt -le $maximumAttempts; $attempt++) {
        $logPath = if ($attempt -eq 1) {
            "build/logs/$Name.log"
        } else {
            "build/logs/$Name-attempt$attempt.log"
        }
        Write-Output "stage2_step=$Name"
        & "$PSScriptRoot\run_logged.ps1" -LogPath $logPath -Command $Command
        $code = $LASTEXITCODE
        if ($code -eq 0) {
            Write-Output "stage2_step_ok=$Name"
            return
        }
        $retryable = $false
        if ($WolframRetry -and $attempt -lt $maximumAttempts) {
            $retryable = Select-String -LiteralPath `
                (Join-Path $repositoryRoot $logPath) `
                -Pattern $wolframLimitPattern -Quiet
        }
        if (-not $retryable) {
            Stop-Gate -Step $Name -Log $logPath -Code $code
        }
        Write-Output ("stage2_retry=$Name attempt $attempt reported a " +
            "Wolfram licence or kernel limit; retrying in 30 s")
        Start-Sleep -Seconds 30
    }
}

$wolframReport = "artifacts/dirac16complex/primordial-field/wolfram-primordial-report.json"
$wolframComponents = "artifacts/dirac16complex/primordial-field/primordial-components.json"
$pythonReport = "artifacts/dirac16complex/primordial-field/python-primordial-report.json"
$provenanceMarkdown = "provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.md"

# Stage 1 and notebook inputs (read, never rebuilt, by this gate).
$inputs = @(
    "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
    "Pair_Creation_of_Universes_WaveFunctionOfUniverse-4+4-Einstein-Lovelock-Nash.nb",
    "wolfram/Dirac16ComplexPrimordial.wl"
)
foreach ($input in $inputs) {
    if (-not (Test-Path -LiteralPath $input -PathType Leaf)) {
        Stop-Gate -Step "inputs" -Reason "missing $input"
    }
}

# No "--" before the report path: WolframScript 1.14.0 drops "--" and every
# argument after it from $ScriptCommandLine (see the header).
Invoke-GateStep -Name "stage2-01-wolfram-primordial" -WolframRetry `
    -Command "wolframscript -file scripts/verify_dirac16complex_primordial.wls $wolframReport"
Invoke-GateStep -Name "stage2-02-check-primordial" `
    -Command "python scripts/check_dirac16complex_primordial.py"
Invoke-GateStep -Name "stage2-03-python-tests" `
    -Command 'python -m unittest discover -s tests -p "test_d16c_primordial*.py" -v'
Invoke-GateStep -Name "stage2-04-provenance-pdf" `
    -Command "python scripts/build_provenance_pdf.py $provenanceMarkdown"

$outputs = @(
    $wolframReport,
    $wolframComponents,
    $pythonReport,
    "provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.tex",
    "provenance/DIRAC16COMPLEX_PRIMORDIAL_FIELD.pdf"
)
foreach ($output in $outputs) {
    if (-not (Test-Path -LiteralPath $output -PathType Leaf)) {
        Stop-Gate -Step "outputs" -Reason "missing $output"
    }
    if ((Get-Item -LiteralPath $output).LastWriteTimeUtc -lt $gateStartedUtc) {
        Stop-Gate -Step "outputs" -Reason "$output was not rewritten by this run"
    }
}

# The same audit program as in the bash twin, so that both apply identical
# JSON semantics (ConvertFrom-Json, for example, rejects keys that differ
# only in case).  With a second argument (the component file) it also
# requires P_EL_agreesWithWolfram = true, wolframAgreement = compared and an
# inputSha256 entry for that file equal to its current sha256.
$auditProgram = @'
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
'@
$audits = @(
    @($wolframReport),
    @($pythonReport, $wolframComponents)
)
foreach ($auditArguments in $audits) {
    $audit = @($auditProgram | & python - @auditArguments)
    if ($LASTEXITCODE -ne 0 -or $audit.Count -ne 1) {
        Stop-Gate -Step "reports" -Reason "could not audit $($auditArguments[0])"
    }
    $auditLine = [string]$audit[0]
    if ($auditLine.StartsWith("OK ")) {
        Write-Output "stage2_report_checks=$($auditLine.Substring(3))"
    } else {
        Stop-Gate -Step "reports" -Reason $auditLine.Substring(5)
    }
}

foreach ($output in $outputs) {
    $hash = (Get-FileHash -LiteralPath $output -Algorithm SHA256).Hash
    Write-Output "stage2_sha256=$($hash.ToLowerInvariant())  $output"
}
Write-Output "stage2_primordial_field_verification=OK"
exit 0
