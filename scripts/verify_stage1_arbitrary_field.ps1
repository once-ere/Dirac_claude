# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 1 gate (dirac16complex in an arbitrary gravitational field).
# Twin of scripts/verify_stage1_arbitrary_field.sh; the step list, the
# checks and the final line are the same.  Modelled on the
# verify_phase*.ps1 gates of https://github.com/once-ere/dirac
# (GPL-3.0-or-later).
#
# Run from any directory with PowerShell 7:
#   pwsh -NoProfile -File scripts/verify_stage1_arbitrary_field.ps1
# or from Windows PowerShell 5.1 (the "powershell" command):
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify_stage1_arbitrary_field.ps1
# Windows PowerShell lacks the utf8NoBOM encoding that scripts/run_logged.ps1
# uses (its Set-Content rejects it), so under the Desktop edition the gate
# relaunches itself under pwsh with the same arguments, prints
# stage1_powershell_relaunch, and exits with the relaunched gate's exit code;
# without pwsh on PATH it prints stage1_arbitrary_field_verification=FAILED.
# Before the provenance document exists (Stage 1 integration), the steps up
# to, but not including, the provenance PDF step can be run with
#   pwsh -NoProfile -File scripts/verify_stage1_arbitrary_field.ps1 -SkipProvenancePdf
# which audits everything except the .tex/.pdf and then prints
#   stage1_arbitrary_field_verification=INCOMPLETE
# and exits 3: a run with -SkipProvenancePdf never prints OK.
#
# Every step runs through scripts/run_logged.ps1 with its log in build/logs/
# (build/ is git-ignored).  The gate stops at the first failing step and
# prints stage1_failed_step, stage1_failed_log and
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
# PYTHONUTF8=1 and a UTF-8 console encoding are set for this process only,
# so that Python output containing Greek letters survives the pipes.
#
# The Wolfram report paths are passed as plain positional script arguments,
# NOT after "--" as in the dirac-main gates: with WolframScript 1.14.0,
# "wolframscript -file s.wls -- r.json" gives $ScriptCommandLine = {"s.wls"}
# (the "--" and everything after it are dropped; checked from PowerShell 7.6
# and Git Bash on 2026-09-25), whereas "wolframscript -file s.wls r.json"
# gives {"s.wls", "r.json"}.  Scripts that filter "--" out of
# Rest[$ScriptCommandLine] read the path the same way in both forms.
[CmdletBinding()]
param(
    [switch]$SkipProvenancePdf
)

# Windows PowerShell 5.1 cannot run scripts/run_logged.ps1 (no utf8NoBOM
# encoding); relaunch under PowerShell 7 with the same arguments.
if ($PSVersionTable.PSEdition -eq "Desktop") {
    $pwsh = Get-Command pwsh -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $pwsh) {
        Write-Output "stage1_failed_step=tools"
        Write-Output ("stage1_failure_reason=PowerShell 7 (pwsh) was not found " +
            "on PATH; Windows PowerShell $($PSVersionTable.PSVersion) cannot " +
            "run scripts/run_logged.ps1 (no utf8NoBOM encoding)")
        Write-Output "stage1_arbitrary_field_verification=FAILED"
        exit 1
    }
    Write-Output ("stage1_powershell_relaunch=$($pwsh.Source) (Windows " +
        "PowerShell $($PSVersionTable.PSVersion) relaunches the gate under pwsh)")
    $relaunchArguments = @("-NoProfile", "-ExecutionPolicy", "Bypass",
        "-File", $PSCommandPath)
    if ($SkipProvenancePdf) { $relaunchArguments += "-SkipProvenancePdf" }
    & $pwsh.Source @relaunchArguments
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
    Write-Output "stage1_failed_step=$Step"
    if ($Log) { Write-Output "stage1_failed_log=$Log" }
    if ($Reason) { Write-Output "stage1_failure_reason=$Reason" }
    Write-Output "stage1_arbitrary_field_verification=FAILED"
    if ($Code -eq 0) { $Code = 1 }
    exit $Code
}

foreach ($tool in @("python", "wolframscript")) {
    $resolved = Get-Command $tool -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $resolved) {
        Stop-Gate -Step "tools" -Reason "$tool was not found on PATH"
    }
    Write-Output "stage1_tool_$tool=$($resolved.Source)"
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
Write-Output "stage1_tool_pdflatex=$($pdflatexCommand.Source)"

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
        Write-Output "stage1_step=$Name"
        & "$PSScriptRoot\run_logged.ps1" -LogPath $logPath -Command $Command
        $code = $LASTEXITCODE
        if ($code -eq 0) {
            Write-Output "stage1_step_ok=$Name"
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
        Write-Output ("stage1_retry=$Name attempt $attempt reported a " +
            "Wolfram licence or kernel limit; retrying in 30 s")
        Start-Sleep -Seconds 30
    }
}

$artifactDirectory = "artifacts/dirac16complex/arbitrary-field"
$algebraReport = "$artifactDirectory/wolfram-algebra-report.json"
$geometryReport = "$artifactDirectory/wolfram-geometry-report.json"
$pythonAlgebraReport = "$artifactDirectory/python-algebra-report.json"
$pythonGeometryReport = "$artifactDirectory/python-geometry-report.json"
$grassmannReport = "$artifactDirectory/grassmann-demo-report.json"
$summaryReport = "$artifactDirectory/stage1-summary.json"
$provenanceMarkdown = "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md"

Invoke-GateStep -Name "stage1-01-build-fixture" `
    -Command "python scripts/build_dirac16complex_fixture.py"
# Python-only pass: the Wolfram report on disk may predate this run.
Invoke-GateStep -Name "stage1-02-check-algebra" `
    -Command "python scripts/check_dirac16complex_algebra.py --wolfram-report="
# No "--" before the report path: WolframScript 1.14.0 drops "--" and every
# argument after it from $ScriptCommandLine (see the header).
Invoke-GateStep -Name "stage1-03-wolfram-algebra" -WolframRetry `
    -Command "wolframscript -file scripts/verify_dirac16complex_algebra.wls $algebraReport"
Invoke-GateStep -Name "stage1-04-wolfram-geometry" -WolframRetry `
    -Command "wolframscript -file scripts/verify_dirac16complex_geometry.wls $geometryReport"
# Reads the Wolfram geometry report written by step 04 (GEO_wolframAgreement).
Invoke-GateStep -Name "stage1-05-check-geometry" `
    -Command "python scripts/check_dirac16complex_geometry.py --wolfram-report $geometryReport"
Invoke-GateStep -Name "stage1-06-grassmann-demo" `
    -Command "python scripts/demo_grassmann_lagrangians.py"
# Reads the Wolfram algebra report written by step 03 (ALG_wolframAgreement).
Invoke-GateStep -Name "stage1-07-check-algebra-crosscheck" `
    -Command "python scripts/check_dirac16complex_algebra.py --wolfram-report $algebraReport"
Invoke-GateStep -Name "stage1-08-python-tests" `
    -Command "python -m unittest discover -s tests -p `"test_d16c_[ag]*.py`" -v"
Invoke-GateStep -Name "stage1-09-publication-tests" `
    -Command "python -m unittest discover -s tests -p `"test_publication_tooling.py`" -v"
Invoke-GateStep -Name "stage1-10-summary" `
    -Command "python scripts/build_stage1_summary.py --output $summaryReport"
if (-not $SkipProvenancePdf) {
    Invoke-GateStep -Name "stage1-11-provenance-pdf" `
        -Command "python scripts/build_provenance_pdf.py $provenanceMarkdown"
    # Repeats the publication test against the summary and PDF just rebuilt.
    Invoke-GateStep -Name "stage1-12-publication-recheck" `
        -Command "python -m unittest discover -s tests -p `"test_d16c_arbitrary_field_publication.py`" -v"
}

$outputs = @(
    $algebraReport,
    $geometryReport,
    $pythonAlgebraReport,
    $pythonGeometryReport,
    $grassmannReport,
    $summaryReport
)
if (-not $SkipProvenancePdf) {
    $outputs += @(
        "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.tex",
        "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf"
    )
}
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
# only in case).
$auditProgram = @'
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
'@
# Each report with the cross-implementation checks it must contain.
$audits = @(
    @($algebraReport, "ALG_fixtureAgreement"),
    @($geometryReport),
    @($pythonAlgebraReport, "ALG_fixtureAgreement", "ALG_wolframAgreement"),
    @($pythonGeometryReport, "GEO_wolframAgreement"),
    @($grassmannReport)
)
foreach ($auditArguments in $audits) {
    $report = $auditArguments[0]
    $audit = @($auditProgram | & python - @auditArguments)
    if ($LASTEXITCODE -ne 0 -or $audit.Count -ne 1) {
        Stop-Gate -Step "reports" -Reason "could not audit $report"
    }
    $auditLine = [string]$audit[0]
    if ($auditLine.StartsWith("OK ")) {
        Write-Output "stage1_report_checks=$($auditLine.Substring(3))"
    } else {
        Stop-Gate -Step "reports" -Reason $auditLine.Substring(5)
    }
}

foreach ($output in $outputs) {
    $hash = (Get-FileHash -LiteralPath $output -Algorithm SHA256).Hash
    Write-Output "stage1_sha256=$($hash.ToLowerInvariant())  $output"
}
if ($SkipProvenancePdf) {
    Write-Output ("stage1_skipped_step=stage1-11-provenance-pdf,stage1-12-publication-recheck " +
        "(-SkipProvenancePdf; $provenanceMarkdown not built or checked)")
    Write-Output "stage1_arbitrary_field_verification=INCOMPLETE"
    exit 3
}
Write-Output "stage1_arbitrary_field_verification=OK"
exit 0
