# SPDX-License-Identifier: GPL-3.0-or-later
#
# Stage 5 gate (dirac16complex and dirac16complex00: the exact {+M, -M}
# pairing theory, the Kohn-Sham pairs of both fields, the two documents).
# Twin of scripts/verify_stage5_pair_creation.sh; the step list, the checks
# and the final line are the same.  Same pattern as the Stage 4 gate
# scripts/verify_stage4_kohn_sham.ps1 (itself modelled on the Stage 3 gate
# and the verify_phase*.ps1 gates of https://github.com/once-ere/dirac,
# GPL-3.0-or-later).  The comparisons, and the launch of the Rust runs and of
# the reference reproduction, are made by one program,
# scripts/verify_stage5_pair_creation_audit.py, which both twins call, so
# that both apply exactly the same rules.
#
# Run from any directory with PowerShell 7:
#   pwsh -NoProfile -File scripts/verify_stage5_pair_creation.ps1
# Started from Windows PowerShell 5.1 the gate re-runs itself under pwsh
# (PATH, else %ProgramFiles%\PowerShell\7\pwsh.exe) with the same arguments
# and exits with its exit code: scripts/run_logged.ps1 uses -Encoding
# utf8NoBOM, which Windows PowerShell 5.1 rejects.
#
# Options (the full gate uses none of them):
#   -DryRun          print every step with its expected wall time and command,
#                    run nothing; last line stage5_pair_creation_verification=DRY-RUN
#   -Steps 03,04,..  run only the listed steps (two-digit numbers or full
#                    names; build/stage5 is kept unless step 00 is listed);
#                    the last line is then stage5_pair_creation_verification=PARTIAL
#                    (exit 3), never OK
#   -SequentialRust  run the Rust processes of steps 11 and 14 one after
#                    another instead of concurrently (same outputs)
#
# Needs: python (numpy, sympy, mpmath, matplotlib), cargo with rustfmt and
# clippy, git, pdflatex (PATH or MiKTeX); wolframscript is optional: without
# it the two exact Wolfram verifiers (steps 01, 02) are skipped with the
# message stage5_skipped_step=..., the sympy checkers still compare with the
# committed Wolfram theory files, and the line before the final line says
# which cross-checks were not run.  Every step runs through
# scripts/run_logged.ps1 with its log in build/logs/ (build/ is git-ignored;
# the gate deletes and recreates only build/stage5/).  The gate stops at the
# first failing step and prints stage5_failed_step, stage5_failed_log and
# stage5_pair_creation_verification=FAILED.  A Wolfram step whose log shows a
# licence or kernel-limit message is retried after 30 s, at most 3 attempts;
# a Wolfram step whose log contains "Failed to open file" FAILS even when
# wolframscript exits 0 (audit wolfram-log).
# Never two gates at once: the gate holds the lock directory build/stage5.lock
# (created atomically, removed when the gate ends, also on failure; the bash
# twin uses the same lock).  A second gate started meanwhile stops at once
# with stage5_failed_step=lock.  A lock left behind by a killed gate is
# removed by hand (only when no gate runs).  Do not run this gate while the
# Stage-4 gate or the Stage-5 numerics run either: they share the crate's
# target directory and the machine.
#
# WHAT IS AND IS NOT RE-RUN
#   Re-run and compared with the committed files: the two exact Wolfram
#   verifiers (with wolframscript; their reports and the theory files
#   dirac16complex00-theory.json and pairing-theory.json), the two sympy
#   checkers (their reports), byte for byte, or value by value at relative
#   1e-9 / absolute 1e-12 (which rule matched is logged); the Stage-4
#   identity of the Stage-5 binary (spectrum, scf --quick and excited --quick
#   into build/stage5/stage4-identity, compared by
#   tools/compare_pairs_runs.py with the committed Stage-4 trees: the same
#   checks as the committed rust/stage4-identity-report.json, all true); the
#   COMPLETE canonical Rust pairs tree (pairs --output build/stage5/run-a:
#   every file listed by the committed rust/pairs/summary.json, and no other
#   file, byte-identical; this is also the repeat-run determinism check) and
#   the refined pairs tree (pairs --refined --output build/stage5/refined),
#   compared by tools/compare_pairs_runs.py (repeat byte identity, refined
#   convergence; the same checks as the committed rust/determinism-report.json,
#   all true); the pairs checker scripts/check_dirac16complex_pairs.py on the
#   committed reference and Rust trees with the gate's run-a and refined trees
#   as --repeat / --refined (the same checks and comparisonsNotRun as the
#   committed python-pairs-check-report.json, all true); the figures
#   (scripts/build_dirac16complex_pairs_figures.py --output build/stage5/figures,
#   every file byte-identical to artifacts/dirac16complex/pair-creation/figures/,
#   the same file set); both PDFs (verify mode of scripts/build_provenance_pdf.py:
#   page count and sha256 of the registered edition).
#   Re-run in reduced form: the Python reference pairs runner.  Its canonical
#   run (the whole matrix of scripts/ks_reference_pairs.py on the grids
#   N0, 2 N0, 4 N0; several hours with several worker processes) is NOT
#   repeated.  The gate runs (a) "ks_reference_pairs.py --quick" (its reduced
#   matrix on coarse grids) into build/stage5/reference-quick, which must be
#   complete with no failed run other than controls, and (b) the audit
#   reference-reproduce: per field (d16c, then d16c00) the first configuration
#   of N = 8, lambda = 0, T = 0, |m| = 1 then |m| = 3 whose plusM and minusM
#   records in the committed reference-pairs-summary.json are converged, both
#   universes (at most 4 runs), re-executed on the canonical grids with
#   "--runs LABELS --output build/stage5/reference-reproduce"; every committed
#   file of those run directories must be byte-identical, and each fresh
#   summary record equal to the committed one.  The interacting, the T > 0
#   and the N = 112 reference runs are compared with the Rust runs by the
#   pairs checker (step 21) but not re-executed.
#   Not re-run at all: the canonical reference pairs run (see above).
#   The exact theory is proved by the Wolfram and sympy steps; the numerical
#   steps reproduce and compare numbers; nothing in this gate proves a
#   creation process of universes (STAGE5_SPEC section 0 and erratum E5.1).
#
# INTERFACE REQUIRED FROM THE FIGURES SCRIPT (written by the lead after the
# runs): python scripts/build_dirac16complex_pairs_figures.py --output DIR
# writes every committed figure file of
# artifacts/dirac16complex/pair-creation/figures/ (same relative paths) into
# DIR and nothing else.  While the script or the committed figures directory
# is absent the full gate stops before its first step
# (stage5_failed_step=inputs, stage5_failure_reason=missing ...), and a
# partial run of step 23 stops with "missing input".
#
# STEPS (expected wall time: TIMING below; -DryRun prints the same figures)
#   stage5-00-snapshot              copy the committed Stage-5 files (and the
#                                   Stage-4 Rust tree, which must stay unchanged)
#                                   into build/stage5/snapshot
#   stage5-01-theory-wolfram-00     wolframscript -file scripts/verify_dirac16complex00.wls
#                                   build/stage5/theory/wolfram-dirac16complex00-report.json
#                                   (writes dirac16complex00-theory.json next to it)
#   stage5-02-theory-wolfram-pairing wolframscript -file scripts/verify_dirac16complex_pairing.wls
#                                   build/stage5/theory/wolfram-pairing-report.json
#                                   (writes pairing-theory.json next to it)
#   stage5-03-theory-sympy-00       scripts/check_dirac16complex00.py --output build/stage5/theory/...
#                                   (compares with the COMMITTED Wolfram files; step 05
#                                   proves that the fresh Wolfram files equal them)
#   stage5-04-theory-sympy-pairing  scripts/check_dirac16complex_pairing.py --output ...
#   stage5-05-theory-same           the fresh theory files equal the committed ones
#   stage5-06..09-cargo             fmt --check; clippy --release --all-targets -D warnings;
#                                   test --release; build --release (from the repository root
#                                   so that .cargo/config.toml (+fma) applies)
#   stage5-10-print-config          the release binary answers print-config with SUCCESS
#   stage5-11-stage4-identity-runs  audit rust-run: spectrum, scf --quick, excited --quick
#                                   --output build/stage5/stage4-identity
#   stage5-12-stage4-identity-compare tools/compare_pairs_runs.py --stage4-committed
#                                   artifacts/dirac16complex/kohn-sham/rust --stage4-run ...
#                                   --full spectrum --quick excited scf
#   stage5-13-stage4-identity-audit all checks true, the same checks as the committed
#                                   rust/stage4-identity-report.json
#   stage5-14-rust-pairs            audit rust-run: pairs --output build/stage5/run-a and
#                                   pairs --refined --output build/stage5/refined (concurrent;
#                                   -SequentialRust: one after the other)
#   stage5-15-rust-pairs-compare    every file listed by the committed rust/pairs/summary.json
#                                   is byte-identical in build/stage5/run-a/pairs, no other file
#   stage5-16-pairs-determinism     tools/compare_pairs_runs.py --canonical (committed)
#                                   --repeat run-a --refined refined
#   stage5-17-pairs-determinism-audit all checks true, the same checks as the committed
#                                   rust/determinism-report.json
#   stage5-18-reference-quick       ks_reference_pairs.py --quick --output build/stage5/reference-quick
#   stage5-19-reference-quick-audit complete, no pending run, no failed run other than controls
#   stage5-20-reference-reproduce   audit reference-reproduce (see above)
#   stage5-21-pairs-check           check_dirac16complex_pairs.py --repeat run-a --refined refined
#                                   --report build/stage5/python-pairs-check-report.json
#   stage5-22-pairs-check-audit     all checks true, rust_repeat_byte_identity and
#                                   rust_refined_convergence present, the same checks and
#                                   comparisonsNotRun as the committed python-pairs-check-report.json
#   stage5-23-figures               build_dirac16complex_pairs_figures.py --output build/stage5/figures
#   stage5-24-figures-same          the same files as the committed figures/, byte for byte
#   stage5-25/26-pdf-*              build_provenance_pdf.py (verify mode) for
#                                   provenance/DIRAC16COMPLEX00_FIELD_THEORY.md and
#                                   provenance/DIRAC16COMPLEX_PAIR_CREATION.md (default layout)
#   stage5-27-committed-unchanged   every snapshotted committed file is byte-identical
#   stage5-28-unit-tests            python -m unittest discover -s tests
#                                   -p "test_d16c_stage5*.py" -v
#   stage5-29-fresh-outputs         the gate's outputs were written during this run
# Only then does it print
#   stage5_pair_creation_verification=OK
#
# TIMING (wall times on the machine of the committed outputs: Intel Core
# Ultra 9 275HX, 24 cores, Windows 11; measured on 2026-10-14 at a CPU load
# of 100 % from the Stage-5 numerics running at the same time, so an idle
# machine is faster.  "Stage-4 analogue" marks a figure of the matching
# Stage-4 gate step (its TIMING), "estimate" a figure that was not measured.)
#   00 seconds (estimate: about 230 MB of committed files are copied; the
#   Stage-4 gate copied 205 MB in 2.4 s).  01 about 4-12 min (its provenance file, part 4.3).  02 about 4-12 min (its provenance file, part 4.5).
#   03 about 3.5 min (213 s on 2026-10-15, under load).  04 about 1 min (68 s on 2026-10-15, under load).  05 seconds.
#   06-10 Stage-4 analogue: fmt 3 s, clippy 3 s, test 35-79 s (the crate now
#   also holds the pairs tests: estimate 1-2 min), build 1 s warm, print-config
#   1 s.  11 Stage-4 analogue: spectrum about 1 min, scf --quick 434 s and
#   excited --quick 81 s one after another under full load (2026-09-30), as
#   three concurrent processes bounded by scf --quick: about 7 min (estimate).
#   12, 13 seconds.  14 not yet measured as a gate step: the canonical,
#   repeat and refined pairs runs of October 2026 ran as detached jobs for
#   several hours; about 3-5 h (estimate) with the canonical and the refined
#   process concurrent.  15-17 seconds to a minute (estimate).
#   18 minutes (estimate, not measured: the reduced --quick matrix on the
#   coarse grids).  19 seconds.  20 minutes (estimate, not measured: at most
#   four N = 8, lambda = 0, T = 0 runs on the canonical grids).
#   21 minutes (estimate, not measured: the checker reads both committed trees
#   and runs its own small solver computations).  22 seconds.
#   23-24 not measured (the figures script is written after the runs).
#   25-26 Stage-3 analogue under 1 min each.  27 seconds.  28 about 4 min (225 s on 2026-10-15).
#   29 seconds.  Total: about 4-6 h (estimate), dominated by step 14.
#
# PYTHONUTF8=1 and a UTF-8 console encoding are set for this process only.
# The Wolfram report paths are passed positionally, never after "--"
# (WolframScript 1.14 drops "--" and every argument after it).
[CmdletBinding()]
param(
    [switch]$DryRun,
    [string[]]$Steps = @(),
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
        Write-Output "stage5_failed_step=tools"
        Write-Output ("stage5_failure_reason=PowerShell 7 (pwsh) is required " +
            "and was not found on PATH or at $pwshPath")
        Write-Output "stage5_pair_creation_verification=FAILED"
        exit 1
    }
    [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
    $relaunch = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $PSCommandPath)
    if ($DryRun) { $relaunch += "-DryRun" }
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
$lockDirectory = Join-Path $repositoryRoot "build/stage5.lock"
$script:lockHeld = $false

function Remove-GateLock {
    if ($script:lockHeld -and (Test-Path -LiteralPath $lockDirectory)) {
        Remove-Item -LiteralPath $lockDirectory -Recurse -Force
    }
    $script:lockHeld = $false
}

function Stop-Gate {
    param([string]$Step, [string]$Log, [string]$Reason, [int]$Code = 1)
    Remove-GateLock
    Write-Output "stage5_failed_step=$Step"
    if ($Log) { Write-Output "stage5_failed_log=$Log" }
    if ($Reason) { Write-Output "stage5_failure_reason=$Reason" }
    Write-Output "stage5_pair_creation_verification=FAILED"
    if ($Code -eq 0) { $Code = 1 }
    exit $Code
}

# A terminating error anywhere below (not a failed step) also ends the gate
# with the FAILED line and releases the lock.
trap {
    Remove-GateLock
    Write-Output "stage5_failed_step=error"
    Write-Output "stage5_failure_reason=$($_.Exception.Message)"
    Write-Output "stage5_pair_creation_verification=FAILED"
    exit 1
}

foreach ($tool in @("python", "cargo", "git")) {
    $resolved = Get-Command $tool -CommandType Application `
        -ErrorAction SilentlyContinue | Select-Object -First 1
    if (-not $resolved) {
        Stop-Gate -Step "tools" -Reason "$tool was not found on PATH"
    }
    Write-Output "stage5_tool_$tool=$($resolved.Source)"
}
$pythonExecutable = (Get-Command python -CommandType Application | Select-Object -First 1).Source
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
Write-Output "stage5_tool_pdflatex=$($pdflatexCommand.Source)"
$wolframscriptCommand = Get-Command wolframscript -CommandType Application `
    -ErrorAction SilentlyContinue | Select-Object -First 1
if ($wolframscriptCommand) {
    Write-Output "stage5_tool_wolframscript=$($wolframscriptCommand.Source)"
} else {
    Write-Output ("stage5_tool_wolframscript=NOT FOUND (the two exact Wolfram " +
        "verifier steps will be skipped)")
}

$wolframLimitPattern = "licen[cs]e|password|kernel limit|maximum number of" +
    "|too many kernels|could not (launch|start|connect)"
$audit = "python scripts/verify_stage5_pair_creation_audit.py"

# Never two gates at once (either twin): the lock directory is created
# atomically; an existing one means that another gate runs (or was killed).
if (-not $DryRun) {
    New-Item -ItemType Directory -Path (Join-Path $repositoryRoot "build") -Force | Out-Null
    try {
        # New-Item without -Force fails when the directory exists.
        New-Item -ItemType Directory -Path $lockDirectory -ErrorAction Stop | Out-Null
        $script:lockHeld = $true
        Set-Content -LiteralPath (Join-Path $lockDirectory "owner") -Encoding utf8NoBOM `
            -Value "pid=$PID twin=ps1 started_utc=$([DateTimeOffset]::UtcNow.ToString('o'))"
    } catch {
        $owner = ""
        $ownerFile = Join-Path $lockDirectory "owner"
        if (Test-Path -LiteralPath $ownerFile) { $owner = (Get-Content -LiteralPath $ownerFile -Raw).Trim() }
        Write-Output "stage5_failed_step=lock"
        Write-Output ("stage5_failure_reason=another Stage-5 gate holds build/stage5.lock ($owner); " +
            "never run two gates at once (remove the directory by hand only when no gate runs)")
        Write-Output "stage5_pair_creation_verification=FAILED"
        exit 1
    }
}

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
        [switch]$Wolfram
    )
    if (-not (Test-StepSelected $Name)) {
        Write-Output "stage5_step_not_selected=$Name"
        return
    }
    if ($DryRun) {
        $missing = @($Inputs | Where-Object { -not (Test-Path -LiteralPath $_) })
        Write-Output "stage5_dry_run_step=$Name expected=[$Expected]"
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
    $maximumAttempts = if ($Wolfram) { 3 } else { 1 }
    for ($attempt = 1; $attempt -le $maximumAttempts; $attempt++) {
        $logPath = if ($attempt -eq 1) {
            "build/logs/$Name.log"
        } else {
            "build/logs/$Name-attempt$attempt.log"
        }
        Write-Output "stage5_step=$Name (expected $Expected)"
        $started = [DateTimeOffset]::UtcNow
        & "$PSScriptRoot\run_logged.ps1" -LogPath $logPath -Command $Command
        $code = $LASTEXITCODE
        $seconds = [math]::Round(([DateTimeOffset]::UtcNow - $started).TotalSeconds)
        if ($code -eq 0 -and $Wolfram) {
            # wolframscript can print "Failed to open file" and still exit 0.
            $logCheck = & $pythonExecutable scripts/verify_stage5_pair_creation_audit.py wolfram-log --log $logPath
            $logCheck | ForEach-Object { Write-Output $_ }
            if ($LASTEXITCODE -ne 0) {
                Stop-Gate -Step $Name -Log $logPath `
                    -Reason "wolframscript printed 'Failed to open file' (exit code 0 is not accepted)"
            }
        }
        if ($code -eq 0) {
            Write-Output "stage5_step_ok=$Name seconds=$seconds"
            return
        }
        $retryable = $false
        if ($Wolfram -and $attempt -lt $maximumAttempts) {
            $retryable = Select-String -LiteralPath `
                (Join-Path $repositoryRoot $logPath) `
                -Pattern $wolframLimitPattern -Quiet
        }
        if (-not $retryable) {
            Stop-Gate -Step $Name -Log $logPath -Code $code
        }
        Write-Output ("stage5_retry=$Name attempt $attempt reported a " +
            "Wolfram licence or kernel limit; retrying in 30 s")
        Start-Sleep -Seconds 30
    }
}

function Write-Skipped {
    param([string]$Name, [string]$Reason)
    if (Test-StepSelected $Name) {
        Write-Output "stage5_skipped_step=$Name ($Reason)"
    }
}

$crate = "studies/dirac16complex_kohn_sham"
$manifest = "$crate/Cargo.toml"
$pairCreation = "artifacts/dirac16complex/pair-creation"
$committedRust = "$pairCreation/rust"
$committedReference = "$pairCreation/reference"
$committedFigures = "$pairCreation/figures"
$stage4Rust = "artifacts/dirac16complex/kohn-sham/rust"
$stageBuild = "build/stage5"
$snapshot = "$stageBuild/snapshot"
$theoryBuild = "$stageBuild/theory"
$identityRun = "$stageBuild/stage4-identity"
$freshIdentity = "$stageBuild/stage4-identity-report.json"
$runA = "$stageBuild/run-a"
$refinedRoot = "$stageBuild/refined"
$freshDeterminism = "$stageBuild/determinism-report.json"
$referenceQuick = "$stageBuild/reference-quick"
$referenceReproduce = "$stageBuild/reference-reproduce"
$freshCheckReport = "$stageBuild/python-pairs-check-report.json"
$figuresBuild = "$stageBuild/figures"
$figuresScript = "scripts/build_dirac16complex_pairs_figures.py"
$comparePairs = "$crate/tools/compare_pairs_runs.py"
$documents = @(
    "provenance/DIRAC16COMPLEX00_FIELD_THEORY",
    "provenance/DIRAC16COMPLEX_PAIR_CREATION"
)
# Committed files that the gate regenerates in place (.tex/.pdf) or must
# leave alone; all must end the run byte-identical.
$committedPaths = @(
    $pairCreation,
    $stage4Rust,
    "wolfram/Dirac16Complex00.wl",
    "wolfram/Dirac16ComplexPairing.wl",
    "$crate/src",
    "$crate/tools",
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
    "wolfram/Dirac16Complex00.wl",
    "wolfram/Dirac16ComplexPairing.wl",
    "scripts/verify_dirac16complex00.wls",
    "scripts/verify_dirac16complex_pairing.wls",
    "scripts/check_dirac16complex00.py",
    "scripts/check_dirac16complex_pairing.py",
    "scripts/check_dirac16complex_pairs.py",
    "scripts/ks_reference_pairs.py",
    $comparePairs,
    "$pairCreation/wolfram-dirac16complex00-report.json",
    "$pairCreation/dirac16complex00-theory.json",
    "$pairCreation/wolfram-pairing-report.json",
    "$pairCreation/pairing-theory.json",
    "$pairCreation/python-dirac16complex00-report.json",
    "$pairCreation/python-pairing-report.json",
    "$pairCreation/python-pairs-check-report.json",
    "$committedRust/stage4-identity-report.json",
    "$committedRust/determinism-report.json",
    "$committedRust/pairs/summary.json",
    "$committedReference/reference-pairs-summary.json",
    $figuresScript,
    "$($documents[0]).md",
    "$($documents[0]).tex",
    "$($documents[0]).pdf",
    "$($documents[1]).md",
    "$($documents[1]).tex",
    "$($documents[1]).pdf",
    "provenance/pdf-specifications.json",
    $manifest
)
foreach ($subcommand in @("spectrum", "scf", "excited")) { $inputs += "$stage4Rust/$subcommand/summary.json" }
if (-not $partial -and -not $DryRun) {
    foreach ($inputPath in $inputs) {
        if (-not (Test-Path -LiteralPath $inputPath -PathType Leaf)) {
            Stop-Gate -Step "inputs" -Reason "missing $inputPath"
        }
    }
    if (-not (Test-Path -LiteralPath $committedFigures -PathType Container)) {
        Stop-Gate -Step "inputs" -Reason "missing $committedFigures/"
    }
}

# Expected wall time per step (TIMING above; the bash twin prints the same).
$expect = @{
    "00" = "seconds"; "01" = "about 4-12 min (its provenance file, part 4.3)"; "02" = "about 4-12 min (its provenance file, part 4.5)"; "03" = "about 3.5 min (213 s on 2026-10-15, under load)"; "04" = "about 1 min (68 s on 2026-10-15, under load)";
    "05" = "seconds"; "06" = "seconds"; "07" = "seconds"; "08" = "about 1-2 min (estimate)"; "09" = "seconds";
    "10" = "seconds"; "11" = "about 7 min (estimate, see TIMING)"; "12" = "seconds"; "13" = "seconds";
    "14" = "about 3-5 h (estimate, see TIMING)"; "15" = "seconds"; "16" = "under 1 min (estimate)"; "17" = "seconds";
    "18" = "minutes (estimate, not measured)"; "19" = "seconds"; "20" = "minutes (estimate, not measured)";
    "21" = "minutes (estimate, not measured)"; "22" = "seconds"; "23" = "not measured (script written after the runs)";
    "24" = "seconds"; "25" = "under 1 min (Stage-3 analogue)"; "26" = "under 1 min (Stage-3 analogue)";
    "27" = "seconds"; "28" = "about 4 min (225 s on 2026-10-15)"; "29" = "seconds"
}

# build/stage5 belongs to this gate: start from an empty directory (a partial
# run keeps it unless it includes the snapshot step 00).
if (-not $DryRun -and (Test-StepSelected "stage5-00-snapshot")) {
    if (Test-Path -LiteralPath $stageBuild) {
        Remove-Item -LiteralPath $stageBuild -Recurse -Force
    }
}
if (-not $DryRun) {
    New-Item -ItemType Directory -Path $stageBuild -Force | Out-Null
}

$committedArguments = $committedPaths -join " "
Invoke-GateStep -Name "stage5-00-snapshot" -Expected $expect["00"] `
    -Command "$audit snapshot --into $snapshot $committedArguments"

# Exact theory.  The sympy checkers compare with the committed Wolfram files
# (their reports record those paths and sha256); step 05 proves that the
# fresh Wolfram files are identical to them.
$theoryPairs = @()
if ($wolframscriptCommand) {
    Invoke-GateStep -Name "stage5-01-theory-wolfram-00" -Wolfram -Expected $expect["01"] `
        -Inputs @("scripts/verify_dirac16complex00.wls", "wolfram/Dirac16Complex00.wl") `
        -Command "wolframscript -file scripts/verify_dirac16complex00.wls $theoryBuild/wolfram-dirac16complex00-report.json"
    Invoke-GateStep -Name "stage5-02-theory-wolfram-pairing" -Wolfram -Expected $expect["02"] `
        -Inputs @("scripts/verify_dirac16complex_pairing.wls", "wolfram/Dirac16ComplexPairing.wl") `
        -Command "wolframscript -file scripts/verify_dirac16complex_pairing.wls $theoryBuild/wolfram-pairing-report.json"
    $theoryPairs += @(
        "--pair $pairCreation/wolfram-dirac16complex00-report.json $theoryBuild/wolfram-dirac16complex00-report.json",
        "--pair $pairCreation/dirac16complex00-theory.json $theoryBuild/dirac16complex00-theory.json",
        "--pair $pairCreation/wolfram-pairing-report.json $theoryBuild/wolfram-pairing-report.json",
        "--pair $pairCreation/pairing-theory.json $theoryBuild/pairing-theory.json")
} else {
    Write-Skipped -Name "stage5-01-theory-wolfram-00" `
        -Reason "wolframscript was not found; the exact Wolfram verifier of dirac16complex00 was NOT run"
    Write-Skipped -Name "stage5-02-theory-wolfram-pairing" `
        -Reason "wolframscript was not found; the exact Wolfram verifier of the pairing theorems was NOT run"
}
Invoke-GateStep -Name "stage5-03-theory-sympy-00" -Expected $expect["03"] `
    -Inputs @("$pairCreation/dirac16complex00-theory.json") `
    -Command "python scripts/check_dirac16complex00.py --output $theoryBuild/python-dirac16complex00-report.json"
Invoke-GateStep -Name "stage5-04-theory-sympy-pairing" -Expected $expect["04"] `
    -Inputs @("$pairCreation/pairing-theory.json") `
    -Command "python scripts/check_dirac16complex_pairing.py --output $theoryBuild/python-pairing-report.json"
$theoryPairs += @(
    "--pair $pairCreation/python-dirac16complex00-report.json $theoryBuild/python-dirac16complex00-report.json",
    "--pair $pairCreation/python-pairing-report.json $theoryBuild/python-pairing-report.json")
Invoke-GateStep -Name "stage5-05-theory-same" -Expected $expect["05"] `
    -Command "$audit same --rtol 1e-9 --atol 1e-12 $($theoryPairs -join ' ')"

Invoke-GateStep -Name "stage5-06-cargo-fmt" -Expected $expect["06"] `
    -Command "cargo fmt --manifest-path $manifest --check"
Invoke-GateStep -Name "stage5-07-cargo-clippy" -Expected $expect["07"] `
    -Command "cargo clippy --manifest-path $manifest --release --all-targets -- -D warnings"
Invoke-GateStep -Name "stage5-08-cargo-test" -Expected $expect["08"] `
    -Command "cargo test --manifest-path $manifest --release"
Invoke-GateStep -Name "stage5-09-cargo-build" -Expected $expect["09"] `
    -Command "cargo build --manifest-path $manifest --release"

$binary = "$crate/target/release/dirac16complex_kohn_sham.exe"
if (-not (Test-Path -LiteralPath $binary -PathType Leaf)) {
    $binary = "$crate/target/release/dirac16complex_kohn_sham"
}
if (-not $DryRun -and -not $partial -and -not (Test-Path -LiteralPath $binary -PathType Leaf)) {
    Stop-Gate -Step "binary" -Reason "cargo build did not produce $binary"
}
Write-Output "stage5_binary=$binary"
$binaryPath = Join-Path $repositoryRoot $binary
$rustMode = if ($SequentialRust) { " --sequential" } else { "" }

Invoke-GateStep -Name "stage5-10-print-config" -Expected $expect["10"] -Inputs @($binary) `
    -Command "& '$binaryPath' print-config"

# The Stage-4 subcommands of the Stage-5 binary must reproduce the committed
# Stage-4 bytes (STAGE5_SPEC section 6): spectrum in full, scf and excited in
# their --quick subsets, as recorded in rust/stage4-identity-report.json.
Invoke-GateStep -Name "stage5-11-stage4-identity-runs" -Expected $expect["11"] -Inputs @($binary) `
    -Command ("$audit rust-run --binary $binary --log-prefix build/logs/stage5-11-stage4-identity$rustMode " +
        "--job spectrum $identityRun canonical --job scf $identityRun quick --job excited $identityRun quick")
Invoke-GateStep -Name "stage5-12-stage4-identity-compare" -Expected $expect["12"] `
    -Command ("python $comparePairs --stage4-committed $stage4Rust --stage4-run $identityRun " +
        "--full spectrum --quick excited scf --binary $binary --report $freshIdentity")
Invoke-GateStep -Name "stage5-13-stage4-identity-audit" -Expected $expect["13"] `
    -Inputs @("$committedRust/stage4-identity-report.json") `
    -Command "$audit report --fresh $freshIdentity --committed $committedRust/stage4-identity-report.json"

# The canonical pairs tree (build/stage5/run-a) and the refined pairs tree
# (build/stage5/refined), launched by the audit program.
Invoke-GateStep -Name "stage5-14-rust-pairs" -Expected $expect["14"] -Inputs @($binary) `
    -Command ("$audit rust-run --binary $binary --log-prefix build/logs/stage5-14-rust-pairs$rustMode " +
        "--job pairs $runA canonical --job pairs $refinedRoot refined")
Invoke-GateStep -Name "stage5-15-rust-pairs-compare" -Expected $expect["15"] `
    -Inputs @("$committedRust/pairs/summary.json") `
    -Command "$audit rust-outputs --committed $committedRust --run $runA --sub pairs"
Invoke-GateStep -Name "stage5-16-pairs-determinism" -Expected $expect["16"] `
    -Command ("python $comparePairs --canonical $committedRust --repeat $runA --refined $refinedRoot " +
        "--binary $binary --report $freshDeterminism")
Invoke-GateStep -Name "stage5-17-pairs-determinism-audit" -Expected $expect["17"] `
    -Inputs @("$committedRust/determinism-report.json") `
    -Command "$audit report --fresh $freshDeterminism --committed $committedRust/determinism-report.json"

# The Python reference pairs runner: its --quick matrix, and the
# re-execution of the committed N = 8, lambda = 0, T = 0 pairs on the
# canonical grids (the canonical reference run takes several hours and is
# not repeated); then the pairs checker on the committed trees with the
# gate's run-a and refined trees as --repeat / --refined.
Invoke-GateStep -Name "stage5-18-reference-quick" -Expected $expect["18"] `
    -Command "python scripts/ks_reference_pairs.py --quick --output $referenceQuick"
Invoke-GateStep -Name "stage5-19-reference-quick-audit" -Expected $expect["19"] `
    -Command "$audit reference-quick --summary $referenceQuick/reference-pairs-summary.json"
Invoke-GateStep -Name "stage5-20-reference-reproduce" -Expected $expect["20"] `
    -Inputs @("$committedReference/reference-pairs-summary.json") `
    -Command ("$audit reference-reproduce --committed $committedReference --output $referenceReproduce " +
        "--log build/logs/stage5-20-reference-reproduce-runner.log")
Invoke-GateStep -Name "stage5-21-pairs-check" -Expected $expect["21"] `
    -Inputs @("$committedReference/reference-pairs-summary.json", "$committedRust/pairs/summary.json") `
    -Command ("python scripts/check_dirac16complex_pairs.py --reference $committedReference --rust $committedRust " +
        "--theory $pairCreation/pairing-theory.json --repeat $runA --refined $refinedRoot --report $freshCheckReport")
Invoke-GateStep -Name "stage5-22-pairs-check-audit" -Expected $expect["22"] `
    -Inputs @("$pairCreation/python-pairs-check-report.json") `
    -Command ("$audit report --fresh $freshCheckReport --committed $pairCreation/python-pairs-check-report.json " +
        "--require-check rust_repeat_byte_identity --require-check rust_refined_convergence")

# The figures of the pairs (document B, section 7): the script is written by
# the lead after the runs; until then this step fails with "missing input".
Invoke-GateStep -Name "stage5-23-figures" -Expected $expect["23"] -Inputs @($figuresScript, $committedFigures) `
    -Command "python $figuresScript --output $figuresBuild"
Invoke-GateStep -Name "stage5-24-figures-same" -Expected $expect["24"] -Inputs @($committedFigures) `
    -Command "$audit tree-same --committed $committedFigures --fresh $figuresBuild"

Invoke-GateStep -Name "stage5-25-pdf-field-theory" -Expected $expect["25"] `
    -Inputs @("$($documents[0]).md") `
    -Command "python scripts/build_provenance_pdf.py $($documents[0]).md"
Invoke-GateStep -Name "stage5-26-pdf-pair-creation" -Expected $expect["26"] `
    -Inputs @("$($documents[1]).md") `
    -Command "python scripts/build_provenance_pdf.py $($documents[1]).md"
Invoke-GateStep -Name "stage5-27-committed-unchanged" -Expected $expect["27"] `
    -Command "$audit unchanged --snapshot $snapshot $committedArguments"
Invoke-GateStep -Name "stage5-28-unit-tests" -Expected $expect["28"] `
    -Command "python -m unittest discover -s tests -p `"test_d16c_stage5*.py`" -v"

$outputs = @(
    "$theoryBuild/python-dirac16complex00-report.json",
    "$theoryBuild/python-pairing-report.json"
)
if ($wolframscriptCommand) {
    $outputs += @("$theoryBuild/wolfram-dirac16complex00-report.json", "$theoryBuild/dirac16complex00-theory.json",
        "$theoryBuild/wolfram-pairing-report.json", "$theoryBuild/pairing-theory.json")
}
$outputs += @(
    "$identityRun/spectrum/summary.json",
    "$identityRun/scf/summary.json",
    "$identityRun/excited/summary.json",
    $freshIdentity,
    "$runA/pairs/summary.json",
    "$refinedRoot/pairs/summary.json",
    $freshDeterminism,
    "$referenceQuick/reference-pairs-summary.json",
    "$referenceReproduce/reference-pairs-summary.json",
    $freshCheckReport
)
foreach ($document in $documents) { $outputs += @("$document.tex", "$document.pdf") }
Invoke-GateStep -Name "stage5-29-fresh-outputs" -Expected $expect["29"] `
    -Command "$audit fresh --since $gateStartedEpoch $($outputs -join ' ')"

Remove-GateLock
if ($DryRun) {
    Write-Output "stage5_pair_creation_verification=DRY-RUN"
    exit 0
}
if ($partial) {
    Write-Output "stage5_selected_steps=$($selectedSteps -join ',')"
    Write-Output "stage5_pair_creation_verification=PARTIAL"
    exit 3
}
if (-not $wolframscriptCommand) {
    Write-Output ("stage5_wolfram=SKIPPED (wolframscript not found: the two exact Wolfram " +
        "verifiers were not run; every other step passed)")
}
Write-Output "stage5_pair_creation_verification=OK"
exit 0
