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
#
# Every step runs through scripts/run_logged.ps1 with its log in build/logs/
# (build/ is git-ignored).  The gate stops at the first failing step and
# prints stage1_failed_step, stage1_failed_log and
# stage1_arbitrary_field_verification=FAILED.  A Wolfram step whose log shows
# a licence or kernel-limit message is retried after 30 s, at most 3 attempts
# (each attempt keeps its own log).  After the steps the gate requires that
# both Wolfram reports and provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.{tex,pdf}
# were rewritten during this run and that every check in the two Wolfram
# reports is true.  Only then does it print
#   stage1_arbitrary_field_verification=OK
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
param()

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
Write-Output "stage1_tool_pdflatex=$((Get-Command pdflatex -CommandType Application | Select-Object -First 1).Source)"

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

$algebraReport = "artifacts/dirac16complex/arbitrary-field/wolfram-algebra-report.json"
$geometryReport = "artifacts/dirac16complex/arbitrary-field/wolfram-geometry-report.json"
$provenanceMarkdown = "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.md"

Invoke-GateStep -Name "stage1-01-build-fixture" `
    -Command "python scripts/build_dirac16complex_fixture.py"
Invoke-GateStep -Name "stage1-02-check-algebra" `
    -Command "python scripts/check_dirac16complex_algebra.py"
# No "--" before the report path: WolframScript 1.14.0 drops "--" and every
# argument after it from $ScriptCommandLine (see the header).
Invoke-GateStep -Name "stage1-03-wolfram-algebra" -WolframRetry `
    -Command "wolframscript -file scripts/verify_dirac16complex_algebra.wls $algebraReport"
Invoke-GateStep -Name "stage1-04-wolfram-geometry" -WolframRetry `
    -Command "wolframscript -file scripts/verify_dirac16complex_geometry.wls $geometryReport"
Invoke-GateStep -Name "stage1-05-check-geometry" `
    -Command "python scripts/check_dirac16complex_geometry.py"
Invoke-GateStep -Name "stage1-06-grassmann-demo" `
    -Command "python scripts/demo_grassmann_lagrangians.py"
Invoke-GateStep -Name "stage1-07-check-algebra-crosscheck" `
    -Command "python scripts/check_dirac16complex_algebra.py"
Invoke-GateStep -Name "stage1-08-python-tests" `
    -Command "python -m unittest discover -s tests -v"
Invoke-GateStep -Name "stage1-09-provenance-pdf" `
    -Command "python scripts/build_provenance_pdf.py $provenanceMarkdown"

$outputs = @(
    $algebraReport,
    $geometryReport,
    "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.tex",
    "provenance/DIRAC16COMPLEX_ARBITRARY_FIELD.pdf"
)
foreach ($output in $outputs) {
    if (-not (Test-Path -LiteralPath $output -PathType Leaf)) {
        Stop-Gate -Step "outputs" -Reason "missing $output"
    }
    if ((Get-Item -LiteralPath $output).LastWriteTimeUtc -lt $gateStartedUtc) {
        Stop-Gate -Step "outputs" -Reason "$output was not rewritten by this run"
    }
}

foreach ($report in @($algebraReport, $geometryReport)) {
    try {
        $parsed = Get-Content -LiteralPath $report -Raw -Encoding utf8 |
            ConvertFrom-Json
    } catch {
        Stop-Gate -Step "reports" -Reason "$report is not valid JSON"
    }
    if ($parsed.schemaVersion -ne 1) {
        Stop-Gate -Step "reports" -Reason "$report schemaVersion is not 1"
    }
    if ($null -eq $parsed.checks) {
        Stop-Gate -Step "reports" -Reason "$report has no checks object"
    }
    $checkProperties = @($parsed.checks.PSObject.Properties)
    if ($checkProperties.Count -eq 0) {
        Stop-Gate -Step "reports" -Reason "$report has an empty checks object"
    }
    $failedChecks = @(
        $checkProperties | Where-Object { $_.Value -isnot [bool] -or -not $_.Value }
    )
    if ($failedChecks.Count -gt 0) {
        $names = ($failedChecks | ForEach-Object { $_.Name }) -join ","
        Stop-Gate -Step "reports" -Reason "$report failed checks: $names"
    }
    Write-Output "stage1_report_checks=$report $($checkProperties.Count) true"
}

foreach ($output in $outputs) {
    $hash = (Get-FileHash -LiteralPath $output -Algorithm SHA256).Hash
    Write-Output "stage1_sha256=$($hash.ToLowerInvariant())  $output"
}
Write-Output "stage1_arbitrary_field_verification=OK"
exit 0
