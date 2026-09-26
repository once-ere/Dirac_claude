# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 3 gate (dirac16complex dark-sector numerics).
# Twin of scripts/verify_stage3_dark_sector.sh; the step list, the checks and
# the final line are the same.  Same pattern as the Stage 1 and Stage 2 gates
# scripts/verify_stage1_arbitrary_field.ps1 and
# scripts/verify_stage2_primordial_field.ps1, themselves modelled on the
# verify_phase*.ps1 gates of https://github.com/once-ere/dirac
# (GPL-3.0-or-later).  The comparisons are made by one program,
# scripts/verify_stage3_dark_sector_audit.py, which both twins call, so that
# both apply exactly the same rules.
#
# Run from any directory with PowerShell 7:
#   pwsh -NoProfile -File scripts/verify_stage3_dark_sector.ps1
# Started from Windows PowerShell 5.1 (for example
#   powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify_stage3_dark_sector.ps1)
# the gate re-runs itself under pwsh (PATH, else
# %ProgramFiles%\PowerShell\7\pwsh.exe) and exits with its exit code:
# scripts/run_logged.ps1 uses -Encoding utf8NoBOM, which Windows PowerShell
# 5.1 rejects.
#
# Needs: python (numpy, matplotlib, nbformat, nbclient, nbconvert,
# ipykernel), cargo with rustfmt and clippy, git, pdflatex (PATH or
# MiKTeX); wolframscript is optional: without it the Mathematica step is
# skipped with the message stage3_skipped_step=... and the final line says
# which cross-check was not run.  Every step runs through
# scripts/run_logged.ps1 with its log in build/logs/ (build/ is git-ignored;
# the gate deletes and recreates only build/stage3/).  The gate stops at the
# first failing step and prints stage3_failed_step, stage3_failed_log and
# stage3_dark_sector_verification=FAILED.  A Wolfram step whose log shows a
# licence or kernel-limit message is retried after 30 s, at most 3 attempts.
#
# Steps:
#   stage3-00-snapshot            copy the committed Stage-3 files (numerics
#       artifacts, notebooks, the two documents and pdf-specifications.json)
#       into build/stage3/snapshot, for the unchanged checks below
#   stage3-01-solver-setup        scripts/setup_solver.ps1 -Platform win11
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
# PYTHONUTF8=1 and a UTF-8 console encoding are set for this process only,
# so that Python output containing Greek letters survives the pipes.
#
# The Wolfram notebook path is not passed at all (the verifier's default is
# notebooks/Dirac16ComplexDarkSector.nb); WolframScript 1.14.0 drops "--" and
# every argument after it from $ScriptCommandLine (see the Stage 1 gate).
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
        Write-Output "stage3_failed_step=tools"
        Write-Output ("stage3_failure_reason=PowerShell 7 (pwsh) is required " +
            "and was not found on PATH or at $pwshPath")
        Write-Output "stage3_dark_sector_verification=FAILED"
        exit 1
    }
    [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
    & $pwshPath -NoProfile -ExecutionPolicy Bypass -File $PSCommandPath
    exit $LASTEXITCODE
}

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repositoryRoot
$gateStartedEpoch = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

function Stop-Gate {
    param([string]$Step, [string]$Log, [string]$Reason, [int]$Code = 1)
    Write-Output "stage3_failed_step=$Step"
    if ($Log) { Write-Output "stage3_failed_log=$Log" }
    if ($Reason) { Write-Output "stage3_failure_reason=$Reason" }
    Write-Output "stage3_dark_sector_verification=FAILED"
    if ($Code -eq 0) { $Code = 1 }
    exit $Code
}

foreach ($tool in @("python", "cargo", "git")) {
    $resolved = Get-Command $tool -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $resolved) {
        Stop-Gate -Step "tools" -Reason "$tool was not found on PATH"
    }
    Write-Output "stage3_tool_$tool=$($resolved.Source)"
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
Write-Output "stage3_tool_pdflatex=$($pdflatexCommand.Source)"
$wolframscriptCommand = Get-Command wolframscript -CommandType Application `
    -ErrorAction SilentlyContinue | Select-Object -First 1
if ($wolframscriptCommand) {
    Write-Output "stage3_tool_wolframscript=$($wolframscriptCommand.Source)"
} else {
    Write-Output ("stage3_tool_wolframscript=NOT FOUND (the Mathematica " +
        "notebook step will be skipped)")
}
$pwshExecutable = (Get-Process -Id $PID).Path

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
        Write-Output "stage3_step=$Name"
        & "$PSScriptRoot\run_logged.ps1" -LogPath $logPath -Command $Command
        $code = $LASTEXITCODE
        if ($code -eq 0) {
            Write-Output "stage3_step_ok=$Name"
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
        Write-Output ("stage3_retry=$Name attempt $attempt reported a " +
            "Wolfram licence or kernel limit; retrying in 30 s")
        Start-Sleep -Seconds 30
    }
}

$solverPin = "a8fdff459adfe181573d7924b18bffbdf378fdb3"
$manifest = "studies/dirac16complex_cosmology/Cargo.toml"
$numerics = "artifacts/dirac16complex/numerics"
$stageBuild = "build/stage3"
$runA = "$stageBuild/run-a"
$runB = "$stageBuild/run-b"
$repeatRoot = "$stageBuild/repeat"
$refinedRoot = "$stageBuild/refined"
$snapshot = "$stageBuild/snapshot"
$notebookName = "dirac16complex_dark_sector.ipynb"
$committedNotebook = "notebooks/$notebookName"
$cleanNotebook = "$stageBuild/notebook-clean/$notebookName"
$executedNotebook = "$stageBuild/notebook/$notebookName"
$nbconvertDirectory = "$stageBuild/nbconvert"
$nbconvertNotebook = "$nbconvertDirectory/$notebookName"
$freshNotebookReport = "$stageBuild/notebook-report.json"
$mathematicaReport = "$numerics/mathematica-report.json"
$mathematicaFigures = "$numerics/figures/mathematica"
$documents = @(
    "provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS",
    "provenance/DIRAC16COMPLEX_STUDENT_GUIDE"
)
$audit = "python scripts/verify_stage3_dark_sector_audit.py"
# Committed Stage-3 files that the gate regenerates in place (figures,
# Mathematica report, .tex/.pdf) or must leave alone; all must end the run
# byte-identical (mathematica-report.json modulo engine.binary).
$committedPaths = @(
    $numerics,
    "notebooks",
    "provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.md",
    "provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.tex",
    "provenance/DIRAC16COMPLEX_DARK_SECTOR_NUMERICS.pdf",
    "provenance/DIRAC16COMPLEX_STUDENT_GUIDE.md",
    "provenance/DIRAC16COMPLEX_STUDENT_GUIDE.tex",
    "provenance/DIRAC16COMPLEX_STUDENT_GUIDE.pdf",
    "provenance/pdf-specifications.json"
)

# Inputs read (never rebuilt) by this gate.
$inputs = @(
    "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
    $manifest,
    "studies/dirac16complex_cosmology/src/generated.rs",
    $committedNotebook,
    "notebooks/Dirac16ComplexDarkSector.nb",
    "$numerics/notebook-report.json",
    $mathematicaReport,
    "$numerics/numerics-summary.json"
)
foreach ($input in $inputs) {
    if (-not (Test-Path -LiteralPath $input -PathType Leaf)) {
        Stop-Gate -Step "inputs" -Reason "missing $input"
    }
}

# build/stage3 belongs to this gate: start from an empty directory.
if (Test-Path -LiteralPath $stageBuild) {
    Remove-Item -LiteralPath $stageBuild -Recurse -Force
}
New-Item -ItemType Directory -Path $stageBuild -Force | Out-Null

$committedArguments = $committedPaths -join " "
Invoke-GateStep -Name "stage3-00-snapshot" `
    -Command "$audit snapshot --into $snapshot $committedArguments"
Invoke-GateStep -Name "stage3-01-solver-setup" `
    -Command "& '$pwshExecutable' -NoProfile -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11"
Invoke-GateStep -Name "stage3-02-solver-pin" `
    -Command "$audit solver --pin $solverPin"
Invoke-GateStep -Name "stage3-03-cargo-fmt" `
    -Command "cargo fmt --manifest-path $manifest --check"
Invoke-GateStep -Name "stage3-04-cargo-clippy" `
    -Command "cargo clippy --manifest-path $manifest --release --all-targets -- -D warnings"
Invoke-GateStep -Name "stage3-05-cargo-test" `
    -Command "cargo test --manifest-path $manifest --release"
Invoke-GateStep -Name "stage3-06-cargo-build" `
    -Command "cargo build --manifest-path $manifest --release"

$binary = "studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology.exe"
if (-not (Test-Path -LiteralPath $binary -PathType Leaf)) {
    $binary = "studies/dirac16complex_cosmology/target/release/dirac16complex_cosmology"
}
if (-not (Test-Path -LiteralPath $binary -PathType Leaf)) {
    Stop-Gate -Step "binary" -Reason "cargo build did not produce $binary"
}
Write-Output "stage3_binary=$binary"
$binaryPath = (Resolve-Path -LiteralPath $binary).Path

Invoke-GateStep -Name "stage3-07-run-a" -Command "& '$binaryPath' all --output $runA"
Invoke-GateStep -Name "stage3-08-run-b" -Command "& '$binaryPath' all --output $runB"
Invoke-GateStep -Name "stage3-09-compare-outputs" `
    -Command "$audit outputs --committed $numerics --run $runA --run $runB"
Invoke-GateStep -Name "stage3-10-analysis-exp3" `
    -Command "python scripts/analyze_dirac16complex_exp3.py --output $runA"
Invoke-GateStep -Name "stage3-11-compare-analysis" `
    -Command "$audit analysis --committed $numerics --fresh $runA"
$checkerNumber = 12
foreach ($experiment in 1..5) {
    Invoke-GateStep -Name "stage3-$checkerNumber-check-exp$experiment" `
        -Command ("python scripts/check_dirac16complex_exp$experiment.py --output $runA " +
            "--repeat $repeatRoot --refined $refinedRoot")
    $checkerNumber++
}
Invoke-GateStep -Name "stage3-17-audit-reports" `
    -Command "$audit reports --committed $numerics --fresh $runA"
Invoke-GateStep -Name "stage3-18-numerics-summary" `
    -Command "python studies/dirac16complex_cosmology/tools/build_numerics_summary.py --output $runA"
Invoke-GateStep -Name "stage3-19-compare-numerics-summary" `
    -Command "$audit numerics-summary --committed $numerics --fresh $runA"

Invoke-GateStep -Name "stage3-20-notebook-prepare" `
    -Command ("$audit prepare-notebook --source $committedNotebook " +
        "--dest $cleanNotebook --dest $executedNotebook")
Invoke-GateStep -Name "stage3-21-notebook-run" `
    -Command "python notebooks/run_notebook.py $executedNotebook"
Invoke-GateStep -Name "stage3-22-notebook-nbconvert" `
    -Command ("python -m nbconvert --to notebook --execute $cleanNotebook " +
        "--output-dir $nbconvertDirectory --ExecutePreprocessor.timeout=3600")
Invoke-GateStep -Name "stage3-23-notebook-audit" `
    -Command ("python notebooks/check_notebook.py $executedNotebook " +
        "--also $nbconvertNotebook --report $freshNotebookReport")
Invoke-GateStep -Name "stage3-24-notebook-compare" `
    -Command ("$audit notebook --committed-report $numerics/notebook-report.json " +
        "--fresh-report $freshNotebookReport --committed-notebook $committedNotebook " +
        "--fresh-notebook $executedNotebook")
Invoke-GateStep -Name "stage3-25-figures-unchanged" `
    -Command "$audit unchanged --snapshot $snapshot $numerics/figures"

$mathematicaRan = $false
if ($wolframscriptCommand) {
    Invoke-GateStep -Name "stage3-26-mathematica-notebook" -WolframRetry `
        -Command "wolframscript -file scripts/verify_dirac16complex_mathematica_notebook.wls"
    Invoke-GateStep -Name "stage3-27-mathematica-unchanged" `
        -Command ("$audit unchanged --snapshot $snapshot --ignore-json-key engine.binary " +
            "$mathematicaReport $mathematicaFigures")
    $mathematicaRan = $true
} else {
    Write-Output ("stage3_skipped_step=stage3-26-mathematica-notebook,stage3-27-mathematica-unchanged " +
        "(wolframscript was not found on PATH; the Mathematica notebook " +
        "notebooks/Dirac16ComplexDarkSector.nb was NOT evaluated)")
}

Invoke-GateStep -Name "stage3-28-pdf-numerics" `
    -Command "python scripts/build_provenance_pdf.py $($documents[0]).md"
# The student guide is built in the builder's developer layout (ragged table
# columns, breakable code spans), as registered and as its publication test
# requires; without the flag the builder writes a different .tex.
Invoke-GateStep -Name "stage3-29-pdf-student-guide" `
    -Command "python scripts/build_provenance_pdf.py --developer-layout $($documents[1]).md"
Invoke-GateStep -Name "stage3-30-committed-unchanged" `
    -Command ("$audit unchanged --snapshot $snapshot --ignore-json-key engine.binary " +
        "$committedArguments")
Invoke-GateStep -Name "stage3-31-unit-tests" `
    -Command "python -m unittest discover -s tests -v"

$outputs = @()
foreach ($root in @($runA, $runB)) {
    foreach ($experiment in 1..5) { $outputs += "$root/exp$experiment/summary.json" }
}
foreach ($experiment in 1..5) { $outputs += "$runA/exp$experiment/python-check-report.json" }
$outputs += @(
    "$runA/exp3/fits.json",
    "$runA/numerics-summary.json",
    $executedNotebook,
    $nbconvertNotebook,
    $freshNotebookReport
)
if ($mathematicaRan) { $outputs += $mathematicaReport }
foreach ($document in $documents) { $outputs += @("$document.tex", "$document.pdf") }
Invoke-GateStep -Name "stage3-32-fresh-outputs" `
    -Command "$audit fresh --since $gateStartedEpoch $($outputs -join ' ')"

if (-not $mathematicaRan) {
    Write-Output ("stage3_mathematica=SKIPPED (wolframscript not found; every " +
        "other step passed)")
}
Write-Output "stage3_dark_sector_verification=OK"
exit 0
