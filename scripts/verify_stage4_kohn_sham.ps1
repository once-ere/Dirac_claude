# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 4 gate (dirac16complex Kohn-Sham DFT in the primordial field).
# Twin of scripts/verify_stage4_kohn_sham.sh; the step list, the checks and
# the final line are the same.  Same pattern as the Stage 3 gate
# scripts/verify_stage3_dark_sector.ps1 (itself modelled on the
# verify_phase*.ps1 gates of https://github.com/once-ere/dirac,
# GPL-3.0-or-later).  The comparisons, and the launch of the Rust runs, are
# made by one program, scripts/verify_stage4_kohn_sham_audit.py, which both
# twins call, so that both apply exactly the same rules.
#
# Run from any directory with PowerShell 7:
#   pwsh -NoProfile -File scripts/verify_stage4_kohn_sham.ps1
# Started from Windows PowerShell 5.1 the gate re-runs itself under pwsh
# (PATH, else %ProgramFiles%\PowerShell\7\pwsh.exe) with the same arguments
# and exits with its exit code: scripts/run_logged.ps1 uses -Encoding
# utf8NoBOM, which Windows PowerShell 5.1 rejects.
#
# Options (the full gate uses none of them):
#   -DryRun          print every step with its expected wall time and command,
#                    run nothing; last line stage4_kohn_sham_verification=DRY-RUN
#   -Steps 03,04,..  run only the listed steps (two-digit numbers or full
#                    names; build/stage4 is kept unless step 00 is listed);
#                    the last line is then stage4_kohn_sham_verification=PARTIAL
#                    (exit 3), never OK
#   -RefinedThermo   also run "thermo --refined" in step 14 (adds about the
#                    canonical thermo time again, see TIMING) so that the
#                    refined tree is complete and the fresh determinism report
#                    must equal the committed one byte for byte
#   -SequentialRust  run the Rust processes of step 14 one after another
#                    instead of concurrently (same outputs, see TIMING)
#
# Needs: python (numpy, matplotlib, nbformat, nbclient, nbconvert,
# ipykernel), cargo with rustfmt and clippy, git, pdflatex (PATH or MiKTeX);
# wolframscript is optional: without it the two Wolfram steps (the exact
# theory verifier and the Mathematica notebook) are skipped with the message
# stage4_skipped_step=..., the sympy theory checker still compares with the
# committed kohn-sham-theory.json, and the line before the final line says
# which cross-checks were not run.  Every step runs through
# scripts/run_logged.ps1 with its log in build/logs/ (build/ is git-ignored;
# the gate deletes and recreates only build/stage4/); the Rust processes of
# step 14 write one log each, build/logs/stage4-14-rust-runs-<canonical|
# refined>-<subcommand>.log.  The gate stops at the first failing step and
# prints stage4_failed_step, stage4_failed_log and
# stage4_kohn_sham_verification=FAILED.  A Wolfram step whose log shows a
# licence or kernel-limit message is retried after 30 s, at most 3 attempts.
# Never run two gates at once: both would delete and rewrite build/stage4.
#
# WHAT IS AND IS NOT RE-RUN
#   Re-run and compared byte for byte: the exact Wolfram theory verifier
#   (with wolframscript) and the sympy theory checker (their four files;
#   value by value at relative 1e-9 / absolute 1e-12 is also accepted, and
#   which rule matched is logged), the constants generator (generated.rs and
#   generator-report.json), the COMPLETE canonical Rust tree (all five
#   subcommands into build/stage4/run-a; every file listed by every committed
#   summary.json, and no other file; this is also the repeat-run determinism
#   check), the summary builder, the Jupyter notebook (twice: run_notebook.py
#   and nbconvert; its report must equal the committed one except the
#   notebook paths, its figures are rewritten byte for byte), the
#   Mathematica notebook (with wolframscript; its report modulo the
#   platform-specific engine.binary and its figures byte for byte), both
#   PDFs (verify mode of scripts/build_provenance_pdf.py: page count and
#   sha256 of the registered edition).
#   Re-run and compared within tolerances: the --refined Rust run of
#   spectrum, scf, excited and emt into build/stage4/refined (thermo only
#   with -RefinedThermo): compare_runs.py (energies relative 1e-7,
#   eigenvalues absolute 1e-7) and the cross-checker's
#   rust_refined_convergence.
#   Re-run in reduced form: the Python reference solver.  Its canonical run
#   (every run of reference-summary.json on the three grids N0, 2 N0, 4 N0,
#   N0 = 60, or 120 for m = 3; several hours with 8 to 12 worker processes)
#   is NOT repeated; the
#   gate runs "ks_reference_solver.py --quick" (its self-tests at N0 = 64
#   plus the reduced parameter set on the two quick grids N0 = 30, 60) into
#   build/stage4/reference-quick, and the cross-checker re-solves one
#   Rust scf parameter set (--max-reproductions 1: the first present of its
#   priority list, m1_L2_N8_lamp1_T0) with the reference solver on the
#   canonical grids at exactly the Rust lambda_hat, and runs its
#   stationarity (Hellmann-Feynman) identities with small self-consistent
#   reference runs.  The committed reference tree is compared with the
#   committed Rust tree (identical to run-a by step 15) run by run.
#   Not re-run at all: the canonical reference runs (see above) and,
#   without -RefinedThermo, thermo --refined (the committed
#   determinism-report.json then cannot be reproduced byte for byte; step 17
#   requires the same checks, all true, and the same repeat file count, and
#   prints the refined counts next to the committed ones).
#
# STEPS (expected wall time: TIMING below; -DryRun prints the same figures)
#   stage4-00-snapshot             copy the committed Stage-4 files into
#                                  build/stage4/snapshot
#   stage4-01-solver-setup         scripts/setup_solver.ps1 -Platform win11
#   stage4-02-solver-pin           the engine is exactly the pin, unmodified
#   stage4-03-theory-wolfram       wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls
#                                  build/stage4/theory/wolfram-kohn-sham-report.json
#                                  (writes kohn-sham-theory.json next to it)
#   stage4-04-theory-sympy         scripts/check_dirac16complex_kohn_sham_theory.py into
#                                  build/stage4/theory/ (it compares with the COMMITTED
#                                  kohn-sham-theory.json, whose path and sha256 its report
#                                  records; step 05 proves that the fresh Wolfram file is
#                                  identical to it)
#   stage4-05-theory-same          the four theory files equal the committed ones
#   stage4-06..08-constants        generate_dirac16complex_ks_constants.py --check; the
#                                  same generator into build/stage4/constants/; its
#                                  generated.rs and generator-report.json equal the
#                                  committed ones byte for byte
#   stage4-09..12-cargo            fmt --check; clippy --release --all-targets -D warnings;
#                                  test --release; build --release (from the repository
#                                  root so that .cargo/config.toml (+fma) applies)
#   stage4-13-print-config         the release binary answers print-config with SUCCESS
#   stage4-14-rust-runs            audit rust-run: the five subcommands --output
#                                  build/stage4/run-a and spectrum, scf, excited, emt
#                                  (+ thermo) --refined --output build/stage4/refined, as
#                                  concurrent processes (-SequentialRust: one after the
#                                  other); every process exits 0 with last line SUCCESS
#   stage4-15-rust-compare         every file listed by every committed summary.json is
#                                  byte-identical in build/stage4/run-a, no other file
#   stage4-16-determinism          tools/compare_runs.py --canonical (committed tree)
#                                  --repeat run-a --refined refined
#   stage4-17-determinism-audit    all checks true, same checks and repeat file count as
#                                  the committed determinism-report.json (byte identity
#                                  required with -RefinedThermo)
#   stage4-18-reference-quick      ks_reference_solver.py --quick into
#                                  build/stage4/reference-quick
#   stage4-19-reference-quick-audit  complete, self-tests present, every run converged
#   stage4-20-cross-check          check_dirac16complex_kohn_sham.py --rust (committed)
#                                  --repeat run-a --refined refined (reproduction and
#                                  stationarity runs of the reference solver) into
#                                  build/stage4/python-check-report.json
#   stage4-21-cross-check-audit    all checks true, the same check names and the same
#                                  comparisons not run as the committed
#                                  python-check-report.json
#   stage4-22/23-summary           build_kohn_sham_summary.py (committed inputs) into
#                                  build/stage4/kohn-sham-summary.json, byte-identical to
#                                  the committed kohn-sham-summary.json
#   stage4-24..28-notebook         a copy of notebooks/dirac16complex_kohn_sham.ipynb
#                                  without outputs is executed headless by
#                                  notebooks/run_notebook.py and by nbconvert, audited by
#                                  notebooks/check_dirac16complex_kohn_sham_notebook.py
#                                  (build/stage4/notebook-report.json), which must equal
#                                  the committed notebook-report.json except the paths
#   stage4-29-figures-unchanged    the notebook rewrote the committed figures byte for byte
#   stage4-30-mathematica-notebook wolframscript -file
#                                  scripts/verify_dirac16complex_ks_mathematica_notebook.wls
#                                  (skipped without wolframscript)
#   stage4-31-mathematica-unchanged mathematica-report.json (modulo engine.binary) and
#                                  figures/mathematica rewritten byte for byte
#   stage4-32/33-pdf-*             build_provenance_pdf.py (verify mode) for
#                                  DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL.md and, with
#                                  --developer-layout, DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE.md
#   stage4-34-committed-unchanged  every snapshotted committed file is byte-identical
#   stage4-35-unit-tests           python -m unittest discover -s tests
#                                  -p "test_d16c_kohn_sham*.py" -v
#   stage4-36-fresh-outputs        the gate's outputs were written during this run
# Only then does it print
#   stage4_kohn_sham_verification=OK
#
# TIMING: PROVISIONAL
#
# PYTHONUTF8=1 and a UTF-8 console encoding are set for this process only.
# The Wolfram report path is passed positionally, never after "--"
# (WolframScript 1.14 drops "--" and every argument after it).
[CmdletBinding()]
param(
    [switch]$DryRun,
    [string[]]$Steps = @(),
    [switch]$RefinedThermo,
    [switch]$SequentialRust
)

if ($PSVersionTable.PSEdition -ne "Core") {
    $pwshCommand = Get-Command pwsh -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    $pwshPath = if ($pwshCommand) {
        $pwshCommand.Source
    } else {
        Join-Path $env:ProgramFiles "PowerShell\7\pwsh.exe"
    }
    if (-not (Test-Path -LiteralPath $pwshPath -PathType Leaf)) {
        Write-Output "stage4_failed_step=tools"
        Write-Output ("stage4_failure_reason=PowerShell 7 (pwsh) is required " +
            "and was not found on PATH or at $pwshPath")
        Write-Output "stage4_kohn_sham_verification=FAILED"
        exit 1
    }
    [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
    $relaunch = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $PSCommandPath)
    if ($DryRun) { $relaunch += "-DryRun" }
    if ($RefinedThermo) { $relaunch += "-RefinedThermo" }
    if ($SequentialRust) { $relaunch += "-SequentialRust" }
    if ($Steps.Count -gt 0) { $relaunch += @("-Steps", ($Steps -join ",")) }
    & $pwshPath @relaunch
    exit $LASTEXITCODE
}

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repositoryRoot
$gateStartedEpoch = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)

# -Steps accepts "03,04" (one argument, as passed on a relaunch) or 03 04.
$selectedSteps = @($Steps | ForEach-Object { $_ -split "," } |
    ForEach-Object { $_.Trim() } | Where-Object { $_ })
$partial = $selectedSteps.Count -gt 0

function Stop-Gate {
    param([string]$Step, [string]$Log, [string]$Reason, [int]$Code = 1)
    Write-Output "stage4_failed_step=$Step"
    if ($Log) { Write-Output "stage4_failed_log=$Log" }
    if ($Reason) { Write-Output "stage4_failure_reason=$Reason" }
    Write-Output "stage4_kohn_sham_verification=FAILED"
    if ($Code -eq 0) { $Code = 1 }
    exit $Code
}

foreach ($tool in @("python", "cargo", "git")) {
    $resolved = Get-Command $tool -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $resolved) {
        Stop-Gate -Step "tools" -Reason "$tool was not found on PATH"
    }
    Write-Output "stage4_tool_$tool=$($resolved.Source)"
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
Write-Output "stage4_tool_pdflatex=$($pdflatexCommand.Source)"
$wolframscriptCommand = Get-Command wolframscript -CommandType Application `
    -ErrorAction SilentlyContinue | Select-Object -First 1
if ($wolframscriptCommand) {
    Write-Output "stage4_tool_wolframscript=$($wolframscriptCommand.Source)"
} else {
    Write-Output ("stage4_tool_wolframscript=NOT FOUND (the Wolfram theory " +
        "verifier and the Mathematica notebook steps will be skipped)")
}
$pwshExecutable = (Get-Process -Id $PID).Path

$wolframLimitPattern = "licen[cs]e|password|kernel limit|maximum number of" +
    "|too many kernels|could not (launch|start|connect)"

function Test-StepSelected {
    param([string]$Name)
    if (-not $partial) { return $true }
    $number = $Name.Substring(7, 2)
    return ($selectedSteps -contains $Name) -or ($selectedSteps -contains $number)
}

function Invoke-GateStep {
    param(
        [string]$Name,
        [string]$Command,
        [string]$Expected = "",
        [string[]]$Inputs = @(),
        [switch]$WolframRetry
    )
    if (-not (Test-StepSelected $Name)) {
        Write-Output "stage4_step_not_selected=$Name"
        return
    }
    if ($DryRun) {
        $missing = @($Inputs | Where-Object { -not (Test-Path -LiteralPath $_) })
        Write-Output "stage4_dry_run_step=$Name expected=[$Expected]"
        Write-Output "    command: $Command"
        if ($missing.Count -gt 0) {
            Write-Output "    missing now: $($missing -join ', ')"
        }
        return
    }
    foreach ($inputPath in $Inputs) {
        if (-not (Test-Path -LiteralPath $inputPath)) {
            Stop-Gate -Step $Name -Reason "missing input $inputPath"
        }
    }
    $maximumAttempts = if ($WolframRetry) { 3 } else { 1 }
    for ($attempt = 1; $attempt -le $maximumAttempts; $attempt++) {
        $logPath = if ($attempt -eq 1) {
            "build/logs/$Name.log"
        } else {
            "build/logs/$Name-attempt$attempt.log"
        }
        Write-Output "stage4_step=$Name (expected $Expected)"
        $started = [DateTimeOffset]::UtcNow
        & "$PSScriptRoot\run_logged.ps1" -LogPath $logPath -Command $Command
        $code = $LASTEXITCODE
        $seconds = [math]::Round(([DateTimeOffset]::UtcNow - $started).TotalSeconds)
        if ($code -eq 0) {
            Write-Output "stage4_step_ok=$Name seconds=$seconds"
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
        Write-Output ("stage4_retry=$Name attempt $attempt reported a " +
            "Wolfram licence or kernel limit; retrying in 30 s")
        Start-Sleep -Seconds 30
    }
}

function Write-Skipped {
    param([string]$Name, [string]$Reason)
    if (Test-StepSelected $Name) {
        Write-Output "stage4_skipped_step=$Name ($Reason)"
    }
}

$solverPin = "a8fdff459adfe181573d7924b18bffbdf378fdb3"
$crate = "studies/dirac16complex_kohn_sham"
$manifest = "$crate/Cargo.toml"
$kohnSham = "artifacts/dirac16complex/kohn-sham"
$committedRust = "$kohnSham/rust"
$stageBuild = "build/stage4"
$snapshot = "$stageBuild/snapshot"
$theoryBuild = "$stageBuild/theory"
$constantsBuild = "$stageBuild/constants"
$runA = "$stageBuild/run-a"
$refinedRoot = "$stageBuild/refined"
$referenceQuick = "$stageBuild/reference-quick"
$freshCheckReport = "$stageBuild/python-check-report.json"
$freshDeterminism = "$stageBuild/determinism-report.json"
$freshSummary = "$stageBuild/kohn-sham-summary.json"
$notebookName = "dirac16complex_kohn_sham.ipynb"
$committedNotebook = "notebooks/$notebookName"
$notebookAuditor = "notebooks/check_dirac16complex_kohn_sham_notebook.py"
$cleanNotebook = "$stageBuild/notebook-clean/$notebookName"
$executedNotebook = "$stageBuild/notebook/$notebookName"
$nbconvertDirectory = "$stageBuild/nbconvert"
$nbconvertNotebook = "$nbconvertDirectory/$notebookName"
$freshNotebookReport = "$stageBuild/notebook-report.json"
$mathematicaNotebook = "notebooks/Dirac16ComplexKohnSham.nb"
$mathematicaVerifier = "scripts/verify_dirac16complex_ks_mathematica_notebook.wls"
$mathematicaReport = "$kohnSham/mathematica-report.json"
$mathematicaFigures = "$kohnSham/figures/mathematica"
$documents = @(
    "provenance/DIRAC16COMPLEX_KOHN_SHAM_PRIMORDIAL",
    "provenance/DIRAC16COMPLEX_KOHN_SHAM_STUDENT_GUIDE"
)
$audit = "python scripts/verify_stage4_kohn_sham_audit.py"
$subcommands = @("spectrum", "scf", "excited", "thermo", "emt")
$refinedSubcommands = @("spectrum", "scf", "excited", "emt")
if ($RefinedThermo) { $refinedSubcommands = $subcommands }
# Committed files that the gate regenerates in place (figures, Mathematica
# report, .tex/.pdf) or must leave alone; all must end the run byte-identical
# (mathematica-report.json modulo engine.binary).
$committedPaths = @(
    $kohnSham,
    "notebooks",
    "$crate/src",
    $manifest,
    "$crate/Cargo.lock",
    "$($documents[0]).md",
    "$($documents[0]).tex",
    "$($documents[0]).pdf",
    "$($documents[1]).md",
    "$($documents[1]).tex",
    "$($documents[1]).pdf",
    "provenance/pdf-specifications.json"
)

# Inputs read (never rebuilt) by this gate; a full run checks them all before
# the first step, a partial run checks those of the selected steps.
$inputs = @(
    "artifacts/dirac16complex/arbitrary-field/algebra-fixture.json",
    $manifest,
    "$crate/src/generated.rs",
    "scripts/generate_dirac16complex_ks_constants.py",
    "$kohnSham/wolfram-kohn-sham-report.json",
    "$kohnSham/kohn-sham-theory.json",
    "$kohnSham/python-theory-report.json",
    "$kohnSham/exchange-table.json",
    "$committedRust/generator-report.json",
    "$committedRust/determinism-report.json",
    "$kohnSham/reference/reference-summary.json",
    "$kohnSham/python-check-report.json",
    "$kohnSham/kohn-sham-summary.json",
    $committedNotebook,
    $notebookAuditor,
    "$kohnSham/notebook-report.json",
    $mathematicaNotebook,
    $mathematicaVerifier,
    $mathematicaReport,
    "$($documents[0]).md",
    "$($documents[1]).md"
)
foreach ($subcommand in $subcommands) { $inputs += "$committedRust/$subcommand/summary.json" }
if (-not $partial -and -not $DryRun) {
    foreach ($inputPath in $inputs) {
        if (-not (Test-Path -LiteralPath $inputPath -PathType Leaf)) {
            Stop-Gate -Step "inputs" -Reason "missing $inputPath"
        }
    }
}

# Expected wall time per step (TIMING above; the bash twin prints the same).
$expect = @{
    "00" = "about 10 s"; "01" = "about 10 s (about 1 min when the engine is cloned)"; "02" = "seconds";
    "03" = "about 45 s"; "04" = "about 3 min"; "05" = "seconds"; "06" = "seconds"; "07" = "seconds";
    "08" = "seconds"; "09" = "seconds"; "10" = "PROVISIONAL"; "11" = "PROVISIONAL"; "12" = "PROVISIONAL";
    "13" = "seconds"; "14" = "PROVISIONAL"; "15" = "about 1 min"; "16" = "about 1 min"; "17" = "seconds";
    "18" = "PROVISIONAL"; "19" = "seconds"; "20" = "PROVISIONAL"; "21" = "seconds"; "22" = "seconds";
    "23" = "seconds"; "24" = "seconds"; "25" = "PROVISIONAL"; "26" = "PROVISIONAL"; "27" = "seconds";
    "28" = "seconds"; "29" = "seconds"; "30" = "PROVISIONAL"; "31" = "seconds"; "32" = "PROVISIONAL";
    "33" = "PROVISIONAL"; "34" = "about 10 s"; "35" = "PROVISIONAL"; "36" = "seconds"
}

# build/stage4 belongs to this gate: start from an empty directory (a partial
# run keeps it unless it includes the snapshot step 00).
if (-not $DryRun -and (Test-StepSelected "stage4-00-snapshot")) {
    if (Test-Path -LiteralPath $stageBuild) {
        Remove-Item -LiteralPath $stageBuild -Recurse -Force
    }
}
if (-not $DryRun) {
    New-Item -ItemType Directory -Path $stageBuild -Force | Out-Null
}

$committedArguments = $committedPaths -join " "
Invoke-GateStep -Name "stage4-00-snapshot" -Expected $expect["00"] `
    -Command "$audit snapshot --into $snapshot $committedArguments"
Invoke-GateStep -Name "stage4-01-solver-setup" -Expected $expect["01"] `
    -Command "& '$pwshExecutable' -NoProfile -ExecutionPolicy Bypass -File scripts/setup_solver.ps1 -Platform win11"
Invoke-GateStep -Name "stage4-02-solver-pin" -Expected $expect["02"] `
    -Command "$audit solver --pin $solverPin"

# Exact theory.  The sympy checker compares with the committed
# kohn-sham-theory.json (its report records that path and its sha256); step
# 05 proves that the fresh Wolfram theory file is identical to it.
$theoryPairs = @()
if ($wolframscriptCommand) {
    Invoke-GateStep -Name "stage4-03-theory-wolfram" -WolframRetry -Expected $expect["03"] `
        -Inputs @("scripts/verify_dirac16complex_kohn_sham.wls", "wolfram/Dirac16ComplexKohnSham.wl") `
        -Command "wolframscript -file scripts/verify_dirac16complex_kohn_sham.wls $theoryBuild/wolfram-kohn-sham-report.json"
    $theoryPairs += @("--pair $kohnSham/wolfram-kohn-sham-report.json $theoryBuild/wolfram-kohn-sham-report.json",
        "--pair $kohnSham/kohn-sham-theory.json $theoryBuild/kohn-sham-theory.json")
} else {
    Write-Skipped -Name "stage4-03-theory-wolfram" `
        -Reason "wolframscript was not found; the exact Wolfram theory verifier was NOT run"
}
Invoke-GateStep -Name "stage4-04-theory-sympy" -Expected $expect["04"] `
    -Inputs @("$kohnSham/kohn-sham-theory.json") `
    -Command ("python scripts/check_dirac16complex_kohn_sham_theory.py --output $theoryBuild/python-theory-report.json " +
        "--table $theoryBuild/exchange-table.json")
$theoryPairs += @("--pair $kohnSham/python-theory-report.json $theoryBuild/python-theory-report.json",
    "--pair $kohnSham/exchange-table.json $theoryBuild/exchange-table.json")
Invoke-GateStep -Name "stage4-05-theory-same" -Expected $expect["05"] `
    -Command "$audit same --rtol 1e-9 --atol 1e-12 $($theoryPairs -join ' ')"

$constantsGenerator = "scripts/generate_dirac16complex_ks_constants.py"
if (Test-Path -LiteralPath $constantsGenerator -PathType Leaf) {
    Invoke-GateStep -Name "stage4-06-constants-check" -Expected $expect["06"] `
        -Command "python $constantsGenerator --check"
    Invoke-GateStep -Name "stage4-07-constants-regenerate" -Expected $expect["07"] `
        -Command ("python $constantsGenerator --output $constantsBuild/generated.rs " +
            "--report $constantsBuild/generator-report.json")
    Invoke-GateStep -Name "stage4-08-constants-same" -Expected $expect["08"] `
        -Command ("$audit same --pair $crate/src/generated.rs $constantsBuild/generated.rs " +
            "--pair $committedRust/generator-report.json $constantsBuild/generator-report.json")
} else {
    foreach ($name in @("stage4-06-constants-check", "stage4-07-constants-regenerate", "stage4-08-constants-same")) {
        Write-Skipped -Name $name -Reason "$constantsGenerator does not exist"
    }
}

Invoke-GateStep -Name "stage4-09-cargo-fmt" -Expected $expect["09"] `
    -Command "cargo fmt --manifest-path $manifest --check"
Invoke-GateStep -Name "stage4-10-cargo-clippy" -Expected $expect["10"] `
    -Command "cargo clippy --manifest-path $manifest --release --all-targets -- -D warnings"
Invoke-GateStep -Name "stage4-11-cargo-test" -Expected $expect["11"] `
    -Command "cargo test --manifest-path $manifest --release"
Invoke-GateStep -Name "stage4-12-cargo-build" -Expected $expect["12"] `
    -Command "cargo build --manifest-path $manifest --release"

$binary = "$crate/target/release/dirac16complex_kohn_sham.exe"
if (-not (Test-Path -LiteralPath $binary -PathType Leaf)) {
    $binary = "$crate/target/release/dirac16complex_kohn_sham"
}
if (-not $DryRun -and -not $partial -and -not (Test-Path -LiteralPath $binary -PathType Leaf)) {
    Stop-Gate -Step "binary" -Reason "cargo build did not produce $binary"
}
Write-Output "stage4_binary=$binary"
$binaryPath = Join-Path $repositoryRoot $binary

Invoke-GateStep -Name "stage4-13-print-config" -Expected $expect["13"] -Inputs @($binary) `
    -Command "& '$binaryPath' print-config"

# The canonical tree (every subcommand into build/stage4/run-a) and the
# refined tree (build/stage4/refined), launched by the audit program: all
# processes concurrently, or one after another with -SequentialRust (TIMING).
$rustJobs = @()
foreach ($subcommand in $subcommands) { $rustJobs += "--job $subcommand $runA canonical" }
foreach ($subcommand in $refinedSubcommands) { $rustJobs += "--job $subcommand $refinedRoot refined" }
$rustMode = if ($SequentialRust) { " --sequential" } else { "" }
$rustExpected = $expect["14"]
if ($RefinedThermo) { $rustExpected += "; with thermo --refined: PROVISIONAL" }
Invoke-GateStep -Name "stage4-14-rust-runs" -Expected $rustExpected -Inputs @($binary) `
    -Command ("$audit rust-run --binary $binary --log-prefix build/logs/stage4-14-rust-runs$rustMode " +
        ($rustJobs -join " "))
Invoke-GateStep -Name "stage4-15-rust-compare" -Expected $expect["15"] `
    -Command "$audit rust-outputs --committed $committedRust --run $runA"
$determinismOptions = if ($RefinedThermo) { " --full-refined" } else { "" }
Invoke-GateStep -Name "stage4-16-determinism" -Expected $expect["16"] `
    -Command ("python $crate/tools/compare_runs.py --canonical $committedRust --repeat $runA " +
        "--refined $refinedRoot --report $freshDeterminism")
Invoke-GateStep -Name "stage4-17-determinism-audit" -Expected $expect["17"] `
    -Inputs @("$committedRust/determinism-report.json") `
    -Command ("$audit determinism --committed $committedRust/determinism-report.json " +
        "--fresh $freshDeterminism$determinismOptions")

# The Python reference solver: its --quick self-tests and reduced parameter
# set (the canonical reference run takes several hours and is not repeated),
# then the cross-checker on the committed trees with the gate's run-a and
# refined trees as --repeat / --refined.
Invoke-GateStep -Name "stage4-18-reference-quick" -Expected $expect["18"] `
    -Command "python scripts/ks_reference_solver.py --quick --output $referenceQuick"
Invoke-GateStep -Name "stage4-19-reference-quick-audit" -Expected $expect["19"] `
    -Command "$audit reference-quick --summary $referenceQuick/reference-summary.json"
Invoke-GateStep -Name "stage4-20-cross-check" -Expected $expect["20"] `
    -Inputs @("$kohnSham/reference/reference-summary.json") `
    -Command ("python scripts/check_dirac16complex_kohn_sham.py --rust $committedRust --repeat $runA " +
        "--refined $refinedRoot --report $freshCheckReport")
Invoke-GateStep -Name "stage4-21-cross-check-audit" -Expected $expect["21"] `
    -Inputs @("$kohnSham/python-check-report.json") `
    -Command "$audit checker-report --committed $kohnSham/python-check-report.json --fresh $freshCheckReport"
Invoke-GateStep -Name "stage4-22-summary" -Expected $expect["22"] `
    -Command "python $crate/tools/build_kohn_sham_summary.py --output $freshSummary"
Invoke-GateStep -Name "stage4-23-summary-same" -Expected $expect["23"] `
    -Inputs @("$kohnSham/kohn-sham-summary.json") `
    -Command "$audit same --pair $kohnSham/kohn-sham-summary.json $freshSummary"

Invoke-GateStep -Name "stage4-24-notebook-prepare" -Expected $expect["24"] -Inputs @($committedNotebook) `
    -Command ("$audit prepare-notebook --source $committedNotebook " +
        "--dest $cleanNotebook --dest $executedNotebook")
Invoke-GateStep -Name "stage4-25-notebook-run" -Expected $expect["25"] `
    -Command "python notebooks/run_notebook.py $executedNotebook"
Invoke-GateStep -Name "stage4-26-notebook-nbconvert" -Expected $expect["26"] `
    -Command ("python -m nbconvert --to notebook --execute $cleanNotebook " +
        "--output-dir $nbconvertDirectory --ExecutePreprocessor.timeout=3600 " +
        "--ExecutePreprocessor.startup_timeout=600")
Invoke-GateStep -Name "stage4-27-notebook-audit" -Expected $expect["27"] -Inputs @($notebookAuditor) `
    -Command ("python $notebookAuditor $executedNotebook " +
        "--also $nbconvertNotebook --report $freshNotebookReport")
Invoke-GateStep -Name "stage4-28-notebook-compare" -Expected $expect["28"] `
    -Inputs @("$kohnSham/notebook-report.json") `
    -Command ("$audit notebook --committed-report $kohnSham/notebook-report.json " +
        "--fresh-report $freshNotebookReport --committed-notebook $committedNotebook " +
        "--fresh-notebook $executedNotebook")
Invoke-GateStep -Name "stage4-29-figures-unchanged" -Expected $expect["29"] `
    -Command "$audit unchanged --snapshot $snapshot $kohnSham/figures"

$mathematicaRan = $false
if ($wolframscriptCommand) {
    Invoke-GateStep -Name "stage4-30-mathematica-notebook" -WolframRetry -Expected $expect["30"] `
        -Inputs @($mathematicaNotebook, $mathematicaVerifier) `
        -Command "wolframscript -file $mathematicaVerifier"
    Invoke-GateStep -Name "stage4-31-mathematica-unchanged" -Expected $expect["31"] `
        -Inputs @($mathematicaReport) `
        -Command ("$audit unchanged --snapshot $snapshot --ignore-json-key engine.binary " +
            "$mathematicaReport $mathematicaFigures")
    $mathematicaRan = $true
} else {
    Write-Skipped -Name "stage4-30-mathematica-notebook" `
        -Reason "wolframscript was not found on PATH; $mathematicaNotebook was NOT evaluated"
    Write-Skipped -Name "stage4-31-mathematica-unchanged" -Reason "no Mathematica run"
}

Invoke-GateStep -Name "stage4-32-pdf-primordial" -Expected $expect["32"] `
    -Inputs @("$($documents[0]).md") `
    -Command "python scripts/build_provenance_pdf.py $($documents[0]).md"
# The student guide is built in the builder's developer layout (ragged table
# columns, breakable code spans), as registered; without the flag the
# builder writes a different .tex.
Invoke-GateStep -Name "stage4-33-pdf-student-guide" -Expected $expect["33"] `
    -Inputs @("$($documents[1]).md") `
    -Command "python scripts/build_provenance_pdf.py --developer-layout $($documents[1]).md"
Invoke-GateStep -Name "stage4-34-committed-unchanged" -Expected $expect["34"] `
    -Command ("$audit unchanged --snapshot $snapshot --ignore-json-key engine.binary " +
        "$committedArguments")
Invoke-GateStep -Name "stage4-35-unit-tests" -Expected $expect["35"] `
    -Command "python -m unittest discover -s tests -p `"test_d16c_kohn_sham*.py`" -v"

$outputs = @(
    "$theoryBuild/python-theory-report.json",
    "$theoryBuild/exchange-table.json",
    "$constantsBuild/generated.rs",
    "$constantsBuild/generator-report.json"
)
if ($wolframscriptCommand) {
    $outputs += @("$theoryBuild/wolfram-kohn-sham-report.json", "$theoryBuild/kohn-sham-theory.json")
}
foreach ($subcommand in $subcommands) { $outputs += "$runA/$subcommand/summary.json" }
foreach ($subcommand in $refinedSubcommands) { $outputs += "$refinedRoot/$subcommand/summary.json" }
$outputs += @(
    $freshDeterminism,
    "$referenceQuick/reference-summary.json",
    $freshCheckReport,
    $freshSummary,
    $executedNotebook,
    $nbconvertNotebook,
    $freshNotebookReport
)
if ($mathematicaRan) { $outputs += $mathematicaReport }
foreach ($document in $documents) { $outputs += @("$document.tex", "$document.pdf") }
Invoke-GateStep -Name "stage4-36-fresh-outputs" -Expected $expect["36"] `
    -Command "$audit fresh --since $gateStartedEpoch $($outputs -join ' ')"

if ($DryRun) {
    Write-Output "stage4_kohn_sham_verification=DRY-RUN"
    exit 0
}
if ($partial) {
    Write-Output "stage4_selected_steps=$($selectedSteps -join ',')"
    Write-Output "stage4_kohn_sham_verification=PARTIAL"
    exit 3
}
if (-not $wolframscriptCommand) {
    Write-Output ("stage4_wolfram=SKIPPED (wolframscript not found: the exact Wolfram " +
        "theory verifier and the Mathematica notebook were not run; every other step passed)")
}
Write-Output "stage4_kohn_sham_verification=OK"
exit 0
