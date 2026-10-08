# SPDX-License-Identifier: GPL-3.0-or-later
#
# Revision gate (Revision/SPEC.md section 10): re-runs EVERY Revision verifier and checker in dependency
# order, then requires that every committed output is byte for byte unchanged and that every report's checks
# pass, then runs the Revision unit tests (except the textbook test, which has its own build).
# Twin of Revision/verify_revision.sh: the step table, the audit program and the final line are the same
# text in both files (Revision/tests/test_revision_gate.py checks that).  Same pattern as the gates
# scripts/verify_stage3_dark_sector.{sh,ps1} (logged steps, stop at the first failing step); no file of the
# old stages is run or read: the run_logged-style logging and the audit program are part of this file.
#
# Run from any directory with PowerShell 7 (Windows PowerShell 5.1 restarts the script in pwsh):
#   pwsh -NoProfile -File Revision/verify_revision.ps1 [--dry-run] [--fast] [--steps a,b,c]
#     --dry-run      print the selected steps with their expected wall times and commands; run nothing
#     --fast         skip the steps documented as longer than 5 minutes and the steps that need them
#                    (printed as revision_skipped_step=...)
#     --steps a,b,c  run only these steps (the two audits committed-unchanged and reports-pass always run)
#
# Needs: python (numpy, sympy, mpmath, matplotlib, nbformat, nbclient, ipykernel), git, cargo,
# wolframscript (activated by the user; the gate never activates it), pdflatex (PATH or MiKTeX).
# Every step runs with its log in build/logs/revision/<step>-pwsh.log (build/ is git-ignored); the gate
# writes its work files only under build/revision/ (each step's work folder is emptied before the step).
# Some verifiers rewrite their committed outputs in place (that is how they are documented); the step
# committed-unchanged then requires `git diff --quiet HEAD` on those output paths and no new untracked
# file there, and lists every path that differs (marking the paths that already differed before the run).
# Before any step the gate stops (revision_failed_step=precheck) when an output path of a selected step
# already differs from HEAD: it verifies the committed record and never overwrites uncommitted work.
# The step reports-pass reads EVERY report of the step table (also of the steps not run now) and requires
# every check to pass.  The gate stops at the first failing step and prints revision_failed_step,
# revision_failed_log and revision_verification=FAILED.  A Wolfram step whose log shows a licence or
# kernel-limit message is retried after 30 s, at most 3 attempts.  The last line is
#   revision_verification=OK      (every selected step passed)
#   revision_verification=FAILED
# (a --dry-run ends with revision_verification=NOT-RUN).
#
# Steps (dependency order; expected wall time on the development machine, Windows 11, 24 threads, from the
# folder READMEs and provenance files or measured by this gate on 2026-10-08; "long" = skipped by --fast):
#   algebra-wolfram                       10 s
#   algebra-sympy                          5 s
#   gkd-rust-build                        60 s
#   gkd-rust-lovelock                     15 s
#   gkd-rust-selftest                    900 s  long
#   gkd-wolfram                          110 s
#   gkd-sympy                             30 s
#   gkd-notebook-extract                  10 s
#   gkd-notebook-digest                    5 s
#   gkd-notebook-image                    10 s
#   gkd-author-extract                   120 s
#   gkd-author-compare                    60 s
#   theory-wolfram                      2700 s  long
#   theory-wolfram-scope                  60 s
#   theory-sympy                         240 s
#   theory-sympy-scope                     5 s
#   theory-compare                         2 s
#   pairing-wolfram                      280 s
#   pairing-sympy                        240 s
#   a4-wolfram                            70 s
#   a4-sympy                              30 s
#   a4-ks-source-conditions                5 s
#   a4-ks-source                          20 s
#   a4-ks-source-unittest                 30 s
#   ks-theory-wolfram                     60 s
#   ks-theory-sympy                       60 s
#   ks-rust-build                         60 s
#   ks-rust-test                          60 s
#   ks-rust-canonical                    250 s
#   ks-rust-mermin-roots                  30 s
#   ks-rust-repeat                       250 s
#   ks-rust-repeat-identical               5 s
#   ks-rust-refined                      620 s  long
#   ks-rust-determinism                   30 s  long
#   ks-reference                         750 s  long
#   ks-rust-refinement                    90 s
#   ks-crosscheck                        780 s  long
#   t3-wolfram                            15 s
#   t3-sympy                              10 s
#   t3-completion-wolfram                 20 s
#   t3-rust-demo                         900 s  long
#   t3-reference-demo                    600 s  long
#   t3-completion-sympy                   10 s
#   dark16-derive                         10 s
#   dark16-ks-history                    150 s
#   dark16-eos                             5 s
#   dark16-independent                   180 s
#   dark00-derive                         30 s
#   dark00-independent                    30 s
#   dark00-unittest                       30 s
#   lead-emt-divergence                   10 s
#   lead-einstein-gauss-bonnet            20 s
#   lead-charge-conjugation               15 s
#   notebooks-check                       90 s
#   pdf-dirac16complex-field-theory       30 s
#   pdf-dirac16complex00-field-theory     30 s
#   pdf-pair-creation-proofs              30 s
#   pdf-kohn-sham-deflating-field         30 s
#   pdf-dark-sector-hypotheses            30 s
#   pdf-lovelock-gkd                      30 s
#   committed-unchanged                   10 s  always
#   reports-pass                           5 s  always
#   unit-tests                           150 s
#
# Order: the GKD Lovelock tensors come right after the algebra because the a4 field equations read
# Revision/gkd_lovelock/results/lovelock-tensors.json; the Kohn-Sham Rust solver is built before every step
# that runs it; ks-rust-mermin-roots follows the canonical matrix (its check compares with it);
# ks-rust-determinism needs the repeat and the refined run; t3-reference-demo reads the Rust demonstration;
# t3-completion-sympy reads both demonstrations; the dark sector reads the Kohn-Sham and a4 records.

if ($PSVersionTable.PSEdition -ne "Core") {
    $pwshCommand = Get-Command pwsh -CommandType Application -ErrorAction SilentlyContinue |
        Select-Object -First 1
    $pwshPath = if ($pwshCommand) { $pwshCommand.Source } else { Join-Path $env:ProgramFiles "PowerShell\7\pwsh.exe" }
    if (-not (Test-Path -LiteralPath $pwshPath -PathType Leaf)) {
        Write-Output "revision_failed_step=tools"
        Write-Output "revision_failure_reason=PowerShell 7 (pwsh) is required and was not found"
        Write-Output "revision_verification=FAILED"
        exit 1
    }
    & $pwshPath -NoProfile -ExecutionPolicy Bypass -File $PSCommandPath @args
    exit $LASTEXITCODE
}

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repositoryRoot
$gateStarted = [DateTimeOffset]::UtcNow
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
$utf8 = [System.Text.UTF8Encoding]::new($false)

function Get-GateSeconds { [int][Math]::Floor(([DateTimeOffset]::UtcNow - $gateStarted).TotalSeconds) }

function Stop-Gate {
    param([string]$Step, [string]$Log, [string]$Reason, [int]$Code = 1)
    Write-Output "revision_failed_step=$Step"
    if ($Log) { Write-Output "revision_failed_log=$Log" }
    if ($Reason) { Write-Output "revision_failure_reason=$Reason" }
    Write-Output "revision_gate_seconds=$(Get-GateSeconds)"
    Write-Output "revision_verification=FAILED"
    if ($Code -eq 0) { $Code = 1 }
    exit $Code
}

$usage = "usage: Revision/verify_revision.ps1 [--dry-run] [--fast] [--steps a,b,c]"
$dryRun = $false
$fast = $false
$stepsOption = ""
$remaining = [System.Collections.Generic.List[string]]::new()
foreach ($argument in $args) { $remaining.Add([string]$argument) }
for ($index = 0; $index -lt $remaining.Count; $index++) {
    $argument = $remaining[$index]
    switch -CaseSensitive ($argument) {
        "--dry-run" { $dryRun = $true }
        "--fast" { $fast = $true }
        "--steps" {
            if ($index + 1 -ge $remaining.Count) { Write-Output $usage; exit 2 }
            $index++
            $stepsOption = $remaining[$index]
        }
        default {
            if ($argument.StartsWith("--steps=")) {
                $stepsOption = $argument.Substring(8)
            } else {
                Write-Output $usage
                exit 2
            }
        }
    }
}

function Resolve-Tool {
    param([string]$Name)
    $resolved = Get-Command $Name -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($resolved) { return $resolved.Source }
    return $null
}

$pythonCommand = Resolve-Tool "python"
if (-not $pythonCommand) { Stop-Gate -Step "tools" -Reason "python was not found" }
Write-Output "revision_tool_python=$pythonCommand"

$gateDirectory = "build/revision"
# A dry run never touches the files of a gate that may be running.
if ($dryRun) { $gateDirectory = "build/revision/dry-run" }
New-Item -ItemType Directory -Force -Path $gateDirectory, "build/logs/revision" | Out-Null
$stepsFile = "$gateDirectory/steps.txt"
$auditScript = "$gateDirectory/gate_audit.py"
$stepsTable = @'
algebra-wolfram|10|0|-|Revision/algebra/gammas.json,Revision/algebra/reports/wolfram-algebra.json|Revision/algebra/reports/wolfram-algebra.json|{wolframscript} -file Revision/algebra/wolfram/verify_algebra.wls
algebra-sympy|5|0|-|Revision/algebra/reports/python-algebra.json,Revision/algebra/reports/python-gammas.json|Revision/algebra/reports/python-algebra.json|{python} Revision/algebra/python/check_algebra.py
gkd-rust-build|60|0|-|-|-|{cargo} build --release --manifest-path Revision/gkd_lovelock/code/Cargo.toml
gkd-rust-lovelock|15|0|-|Revision/gkd_lovelock/results/curvature.json,Revision/gkd_lovelock/results/lovelock-tensors.json,Revision/gkd_lovelock/results/lovelock-components.md,Revision/gkd_lovelock/results/lovelock-report.json|Revision/gkd_lovelock/results/lovelock-report.json|{gkd_exe} lovelock --output Revision/gkd_lovelock/results --brute-force-k2
gkd-rust-selftest|900|1|-|Revision/gkd_lovelock/results/gkd-selftest.json|Revision/gkd_lovelock/results/gkd-selftest.json|{gkd_exe} gkd-selftest --exhaustive-max 4 --output Revision/gkd_lovelock/results
gkd-wolfram|110|0|-|Revision/gkd_lovelock/results/wolfram-gkd-report.json|Revision/gkd_lovelock/results/wolfram-gkd-report.json|{wolframscript} -file Revision/gkd_lovelock/verification/verify_lovelock_gkd.wls Revision/gkd_lovelock/results/wolfram-gkd-report.json
gkd-sympy|30|0|-|Revision/gkd_lovelock/results/python-lovelock-report.json|Revision/gkd_lovelock/results/python-lovelock-report.json|{python} Revision/gkd_lovelock/verification/check_lovelock_gkd.py
gkd-notebook-extract|10|0|-|-|-|{wolframscript} -file Revision/gkd_lovelock/notebook_reading/lovelock_extract_nb_inputs.wls
gkd-notebook-digest|5|0|-|Revision/gkd_lovelock/results/notebook-input-cells.txt|-|{python} Revision/gkd_lovelock/notebook_reading/lovelock_digest_nb_inputs.py
gkd-notebook-image|10|0|-|Revision/gkd_lovelock/results/notebook-in68-image.png|-|{wolframscript} -file Revision/gkd_lovelock/notebook_reading/lovelock_export_nb_image.wls
gkd-author-extract|120|0|-|Revision/gkd_lovelock/comparison/author-curvature-outputs.json|-|{wolframscript} -file Revision/gkd_lovelock/comparison/extract_author_curvature_outputs.wls
gkd-author-compare|60|0|-|Revision/gkd_lovelock/comparison/author-comparison-report.json|Revision/gkd_lovelock/comparison/author-comparison-report.json|{python} Revision/gkd_lovelock/comparison/compare_with_author.py
theory-wolfram|2700|1|-|Revision/theory/field-theory.json,Revision/theory/reports/wolfram-field-theory.json|Revision/theory/reports/wolfram-field-theory.json|{wolframscript} -file Revision/theory/wolfram/verify_field_theory.wls
theory-wolfram-scope|60|0|-|Revision/theory/reports/wolfram-scope.json|Revision/theory/reports/wolfram-scope.json|{wolframscript} -file Revision/theory/wolfram/verify_scope.wls
theory-sympy|240|0|-|Revision/theory/reports/python-field-theory.json|Revision/theory/reports/python-field-theory.json|{python} Revision/theory/python/check_field_theory.py
theory-sympy-scope|5|0|-|Revision/theory/reports/python-scope.json|Revision/theory/reports/python-scope.json|{python} Revision/theory/python/check_scope.py
theory-compare|2|0|-|-|-|{audit} json-equals Revision/theory/reports/python-field-theory.json comparison_with_wolfram.status agree
pairing-wolfram|280|0|-|Revision/pairing/pairing-theory.json,Revision/pairing/reports/wolfram-pairing.json|Revision/pairing/reports/wolfram-pairing.json|{wolframscript} -file Revision/pairing/wolfram/verify_pairing.wls
pairing-sympy|240|0|-|Revision/pairing/reports/python-pairing.json|Revision/pairing/reports/python-pairing.json|{python} Revision/pairing/python/check_pairing.py
a4-wolfram|70|0|-|Revision/field_equations_a4/a4-equations.json,Revision/field_equations_a4/reports/wolfram-a4-report.json|Revision/field_equations_a4/reports/wolfram-a4-report.json|{wolframscript} -file Revision/field_equations_a4/wolfram/verify_field_equations_a4.wls
a4-sympy|30|0|-|Revision/field_equations_a4/reports/python-a4-report.json,Revision/field_equations_a4/reports/a4-equations-summary.md|Revision/field_equations_a4/reports/python-a4-report.json|{python} Revision/field_equations_a4/python/check_field_equations_a4.py
a4-ks-source-conditions|5|0|-|Revision/field_equations_a4/reports/ks-source-conditions.json|Revision/field_equations_a4/reports/ks-source-conditions.json|{python} Revision/field_equations_a4/python/check_ks_source_conditions.py
a4-ks-source|20|0|-|Revision/field_equations_a4/ks_source/results,Revision/field_equations_a4/ks_source/reports|Revision/field_equations_a4/ks_source/reports/ks-source-a4.json|{python} Revision/field_equations_a4/ks_source/ks_source_a4.py
a4-ks-source-unittest|30|0|-|Revision/field_equations_a4/ks_source/results,Revision/field_equations_a4/ks_source/reports|-|{python} -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py -v
ks-theory-wolfram|60|0|-|Revision/kohn_sham/ks-theory.json,Revision/kohn_sham/reports/ks-theory-wolfram.json|Revision/kohn_sham/reports/ks-theory-wolfram.json|{wolframscript} -file Revision/kohn_sham/theory/verify_ks_theory.wls
ks-theory-sympy|60|0|-|Revision/kohn_sham/reports/ks-theory-python.json|Revision/kohn_sham/reports/ks-theory-python.json|{python} Revision/kohn_sham/theory/check_ks_theory.py
ks-rust-build|60|0|-|-|-|{cargo} build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
ks-rust-test|60|0|-|-|-|{cargo} test --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
ks-rust-canonical|250|0|-|Revision/kohn_sham/results,Revision/kohn_sham/reports/ks-rust-solver.json|Revision/kohn_sham/reports/ks-rust-solver.json|{ks_solver} all --out Revision/kohn_sham/results --report Revision/kohn_sham/reports/ks-rust-solver.json
ks-rust-mermin-roots|30|0|build/revision/ks-mermin-roots|Revision/kohn_sham/reports/ks-rust-mermin-roots.json,Revision/kohn_sham/solver/tools/mermin-roots-40digit.json|Revision/kohn_sham/reports/ks-rust-mermin-roots.json|{python} Revision/kohn_sham/solver/tools/mermin_roots_mp.py --work build/revision/ks-mermin-roots
ks-rust-repeat|250|0|build/revision/ks-repeat|-|-|{ks_solver} all --out build/revision/ks-repeat/results --report build/revision/ks-repeat/report.json
ks-rust-repeat-identical|5|0|-|-|-|{audit} same build/revision/ks-repeat/results Revision/kohn_sham/results build/revision/ks-repeat/report.json Revision/kohn_sham/reports/ks-rust-solver.json
ks-rust-refined|620|1|build/revision/ks-refined|-|-|{ks_solver} all --refined --out build/revision/ks-refined/results --report build/revision/ks-refined/report.json
ks-rust-determinism|30|1|-|Revision/kohn_sham/reports/ks-rust-determinism.json|Revision/kohn_sham/reports/ks-rust-determinism.json|{python} Revision/kohn_sham/solver/tools/compare_runs.py --canonical Revision/kohn_sham/results --canonical-report Revision/kohn_sham/reports/ks-rust-solver.json --repeat build/revision/ks-repeat/results --repeat-report build/revision/ks-repeat/report.json --refined build/revision/ks-refined/results --refined-report build/revision/ks-refined/report.json --report Revision/kohn_sham/reports/ks-rust-determinism.json
ks-reference|750|1|-|Revision/kohn_sham/reference/results,Revision/kohn_sham/reports/ks-reference.json|Revision/kohn_sham/reports/ks-reference.json|{python} Revision/kohn_sham/reference/run_reference.py
ks-rust-refinement|90|0|build/revision/ks-refinement|Revision/kohn_sham/checker/rust-refinement.json|-|{python} Revision/kohn_sham/checker/measure_rust_refinement.py --work build/revision/ks-refinement
ks-crosscheck|780|1|build/revision/ks-crosscheck|Revision/kohn_sham/reports/ks-crosscheck.json,Revision/kohn_sham/reports/ks-crosscheck-table.csv|Revision/kohn_sham/reports/ks-crosscheck.json|{python} Revision/kohn_sham/checker/crosscheck_ks.py --work build/revision/ks-crosscheck
t3-wolfram|15|0|-|Revision/pairing/kohn_sham/t3-theory.json,Revision/pairing/kohn_sham/reports/wolfram-t3.json|Revision/pairing/kohn_sham/reports/wolfram-t3.json|{wolframscript} -file Revision/pairing/kohn_sham/wolfram/verify_t3.wls
t3-sympy|10|0|-|Revision/pairing/kohn_sham/reports/python-t3.json|Revision/pairing/kohn_sham/reports/python-t3.json|{python} Revision/pairing/kohn_sham/python/check_t3.py
t3-completion-wolfram|20|0|-|Revision/pairing/kohn_sham/t3-completion.json,Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json|Revision/pairing/kohn_sham/reports/wolfram-t3-completion.json|{wolframscript} -file Revision/pairing/kohn_sham/wolfram/verify_t3_completion.wls
t3-rust-demo|900|1|build/revision/t3-rust-demo|Revision/pairing/kohn_sham/reports/t3-rust-demo.json,Revision/pairing/kohn_sham/numerics/results/t3-rust-states.csv|Revision/pairing/kohn_sham/reports/t3-rust-demo.json|{python} Revision/pairing/kohn_sham/numerics/t3_rust_demo.py --solver {ks_solver} --work build/revision/t3-rust-demo --jobs 8
t3-reference-demo|600|1|-|Revision/pairing/kohn_sham/reports/t3-reference-demo.json,Revision/pairing/kohn_sham/numerics/results/t3-reference-states.csv|Revision/pairing/kohn_sham/reports/t3-reference-demo.json|{python} Revision/pairing/kohn_sham/numerics/t3_reference_demo.py --jobs 8
t3-completion-sympy|10|0|-|Revision/pairing/kohn_sham/reports/python-t3-completion.json|Revision/pairing/kohn_sham/reports/python-t3-completion.json|{python} Revision/pairing/kohn_sham/python/check_t3_completion.py
dark16-derive|10|0|-|Revision/dark_sector/dirac16complex/outputs/effective-formulas.json,Revision/dark_sector/dirac16complex/reports/derivation-checks.json|Revision/dark_sector/dirac16complex/reports/derivation-checks.json|{python} Revision/dark_sector/dirac16complex/derive/derive_effective.py
dark16-ks-history|150|0|-|Revision/dark_sector/dirac16complex/outputs/ks-history-dense.csv,Revision/dark_sector/dirac16complex/reports/ks-history-run.json|Revision/dark_sector/dirac16complex/reports/ks-history-run.json|{python} Revision/dark_sector/dirac16complex/compute/run_ks_history.py --solver {ks_solver}
dark16-eos|5|0|-|Revision/dark_sector/dirac16complex/outputs/eos-history.csv,Revision/dark_sector/dirac16complex/outputs/eos-summary.json,Revision/dark_sector/dirac16complex/reports/eos-checks.json|Revision/dark_sector/dirac16complex/reports/eos-checks.json|{python} Revision/dark_sector/dirac16complex/compute/compute_eos.py
dark16-independent|180|0|-|Revision/dark_sector/dirac16complex/outputs/independent-free-gas.json,Revision/dark_sector/dirac16complex/reports/independent-checks.json|Revision/dark_sector/dirac16complex/reports/independent-checks.json|{python} Revision/dark_sector/dirac16complex/independent/independent_free_gas.py
dark00-derive|30|0|-|Revision/dark_sector/dirac16complex00/eos-theory.json,Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json|Revision/dark_sector/dirac16complex00/reports/python-derive-eos.json|{python} Revision/dark_sector/dirac16complex00/python/derive_eos.py
dark00-independent|30|0|-|Revision/dark_sector/dirac16complex00/results/independent-numerics.json,Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json|Revision/dark_sector/dirac16complex00/reports/python-independent-numerics.json|{python} Revision/dark_sector/dirac16complex00/python/independent_numerics.py
dark00-unittest|30|0|-|Revision/dark_sector/dirac16complex00|-|{python} -m unittest Revision/dark_sector/dirac16complex00/tests/test_dark_sector_dirac16complex00.py -v
lead-emt-divergence|10|0|-|Revision/lead_checks/reports/emt-divergence-and-spin-connection.json|Revision/lead_checks/reports/emt-divergence-and-spin-connection.json|{python} Revision/lead_checks/emt_divergence_and_spin_connection.py
lead-einstein-gauss-bonnet|20|0|-|Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json|Revision/lead_checks/reports/einstein-gauss-bonnet-a4.json|{python} Revision/lead_checks/einstein_gauss_bonnet_a4.py
lead-charge-conjugation|15|0|-|Revision/lead_checks/reports/charge-conjugation-and-u1.json|Revision/lead_checks/reports/charge-conjugation-and-u1.json|{python} Revision/lead_checks/charge_conjugation_and_u1.py
notebooks-check|90|0|-|Revision/notebooks|-|{audit} notebooks Revision/notebooks/tools/build_notebooks.py
pdf-dirac16complex-field-theory|30|0|-|Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.tex,Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX_FIELD_THEORY.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-dirac16complex00-field-theory|30|0|-|Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.tex,Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/DIRAC16COMPLEX00_FIELD_THEORY.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-pair-creation-proofs|30|0|-|Revision/docs/PAIR_CREATION_PROOFS.tex,Revision/docs/PAIR_CREATION_PROOFS.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/PAIR_CREATION_PROOFS.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-kohn-sham-deflating-field|30|0|-|Revision/docs/KOHN_SHAM_DEFLATING_FIELD.tex,Revision/docs/KOHN_SHAM_DEFLATING_FIELD.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/KOHN_SHAM_DEFLATING_FIELD.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-dark-sector-hypotheses|30|0|-|Revision/docs/DARK_SECTOR_HYPOTHESES.tex,Revision/docs/DARK_SECTOR_HYPOTHESES.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/DARK_SECTOR_HYPOTHESES.md --developer-layout --specifications Revision/pdf-specifications.json
pdf-lovelock-gkd|30|0|-|Revision/docs/LOVELOCK_GKD.tex,Revision/docs/LOVELOCK_GKD.pdf|-|{python} scripts/build_provenance_pdf.py Revision/docs/LOVELOCK_GKD.md --developer-layout --specifications Revision/pdf-specifications.json
committed-unchanged|10|A|-|-|-|{audit} unchanged
reports-pass|5|A|-|-|-|{audit} reports
unit-tests|150|0|-|-|-|{audit} unittest Revision/tests test_universes_in_pairs_textbook
'@
$auditSource = @'
# Revision gate audit program (written by Revision/verify_revision.sh and Revision/verify_revision.ps1 into
# build/revision/gate_audit.py; both twins embed this text byte for byte, Revision/tests/test_revision_gate.py
# checks that).  Python standard library only.  Run from the repository root.
import filecmp
import json
import os
import subprocess
import sys
import unittest

# The folder of this program: build/revision (build/revision/dry-run for a dry run, which writes nothing).
GATE = os.path.relpath(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
RUN_AUDIT = "build/revision/gate_audit.py"
SELECTED = os.path.join(GATE, "selected.txt")
OUTPUTS = os.path.join(GATE, "outputs.txt")
REPORTS = os.path.join(GATE, "reports.txt")
PREEXISTING = os.path.join(GATE, "preexisting.txt")
LONG_SECONDS = 300
# Exit code of `precheck` when an output path of a selected step already differs from HEAD.
PRECHECK_PREEXISTING = 3


def fail(message):
    print("revision_audit_error=" + message)
    return 1


def read_table(path):
    steps = []
    with open(path, encoding="utf-8") as handle:
        for line in handle.read().splitlines():
            if not line.strip():
                continue
            fields = line.split("|")
            if len(fields) != 7:
                raise SystemExit("malformed step line: " + line)
            name, seconds, kind, fresh, outputs, reports, command = fields
            steps.append({
                "name": name, "seconds": int(seconds), "kind": kind, "fresh": fresh,
                "outputs": [] if outputs == "-" else outputs.split(","),
                "reports": [] if reports == "-" else reports.split(","),
                "command": command,
            })
    return steps


def executable(stem):
    path = stem + (".exe" if os.name == "nt" else "")
    return path.replace("\\", "/")


def plan(arguments):
    table, fast, dry_run, wanted = arguments[0], False, False, None
    rest = arguments[1:]
    while rest:
        option = rest.pop(0)
        if option == "--fast":
            fast = True
        elif option == "--dry-run":
            dry_run = True
        elif option == "--steps":
            wanted = [name for name in rest.pop(0).split(",") if name]
        else:
            return fail("unknown plan option " + option)
    steps = read_table(table)
    names = [step["name"] for step in steps]
    if len(set(names)) != len(names):
        return fail("duplicate step names")
    if wanted is not None:
        unknown = [name for name in wanted if name not in names]
        if unknown:
            print("revision_unknown_steps=" + ",".join(unknown))
            print("revision_known_steps=" + ",".join(names))
            return 2
    substitutions = {
        "{ks_solver}": executable("Revision/kohn_sham/solver/target/release/revision_ks_solver"),
        "{gkd_exe}": executable("Revision/gkd_lovelock/code/target/release/lovelock_gkd"),
        "{audit}": "{python} " + RUN_AUDIT,
    }
    selected, skipped = [], []
    for step in steps:
        always = step["kind"] == "A"
        if wanted is not None and step["name"] not in wanted and not always:
            continue
        if fast and step["kind"] == "1":
            skipped.append(step)
            continue
        selected.append(step)
    for step in skipped:
        print("revision_skipped_step=%s (expected %d s; --fast skips the steps longer than %d s and the steps "
              "that need them)" % (step["name"], step["seconds"], LONG_SECONDS))
    lines, outputs, total = [], [], 0
    for step in selected:
        command = step["command"]
        for key, value in substitutions.items():
            command = command.replace(key, value)
        lines.append("%s\t%d\t%s\t%s" % (step["name"], step["seconds"], step["fresh"], command))
        total += step["seconds"]
        for path in step["outputs"]:
            if path not in outputs:
                outputs.append(path)
        if dry_run:
            print("revision_dry_run_step=%s expected_seconds=%d command=%s" % (step["name"], step["seconds"], command))
    reports = []
    for step in steps:
        for path in step["reports"]:
            if path not in reports:
                reports.append(path)
    if dry_run:
        print("revision_selected_steps=%d expected_seconds=%d skipped_steps=%d" % (len(selected), total, len(skipped)))
        return 0
    os.makedirs(GATE, exist_ok=True)
    for path, items in ((SELECTED, lines), (OUTPUTS, outputs), (REPORTS, reports)):
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("".join(item + "\n" for item in items))
    print("revision_selected_steps=%d expected_seconds=%d skipped_steps=%d" % (len(selected), total, len(skipped)))
    return 0


def git_lines(arguments):
    result = subprocess.run(["git"] + arguments, capture_output=True, text=True, encoding="utf-8")
    if result.returncode not in (0, 1):
        raise SystemExit("git " + " ".join(arguments[:2]) + " failed: " + result.stderr.strip())
    return [line for line in result.stdout.splitlines() if line.strip()]


def changed_paths(paths):
    if not paths:
        return []
    differing = git_lines(["diff", "--name-only", "HEAD", "--"] + paths)
    untracked = git_lines(["ls-files", "--others", "--exclude-standard", "--"] + paths)
    return sorted(set(differing) | set(untracked))


def read_list(path):
    with open(path, encoding="utf-8") as handle:
        return [line for line in handle.read().splitlines() if line]


def precheck(arguments):
    paths = read_list(OUTPUTS)
    before = changed_paths(paths)
    with open(PREEXISTING, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("".join(path + "\n" for path in before))
    for path in before:
        print("revision_preexisting_change=" + path)
    print("revision_output_paths=%d preexisting_changes=%d" % (len(paths), len(before)))
    # The gate verifies the COMMITTED record and never overwrites uncommitted work: a selected step whose
    # output paths already differ from HEAD stops the gate before anything runs.  Exit code 3 marks this
    # stop; a git error ends this program through SystemExit with exit code 1, so the twins can name the cause.
    if before:
        print("revision_precheck=the output paths above already differ from HEAD; commit or set them aside, "
              "or leave their steps out with --steps")
        return PRECHECK_PREEXISTING
    return 0


def unchanged(arguments):
    paths = read_list(OUTPUTS)
    before = set(read_list(PREEXISTING)) if os.path.exists(PREEXISTING) else set()
    quiet = subprocess.run(["git", "diff", "--quiet", "HEAD", "--"] + paths).returncode if paths else 0
    after = changed_paths(paths)
    for path in after:
        note = " (it already differed from HEAD before the gate ran)" if path in before else ""
        print("revision_changed_output=" + path + note)
    print("revision_output_paths=%d git_diff_quiet=%s changed=%d" % (len(paths), quiet == 0, len(after)))
    return 0 if (quiet == 0 and not after) else 1


def check_verdicts(document):
    """Return (passed, not_available, total, problems) for one report."""
    problems, passed, not_available, total = [], 0, 0, 0
    checks = document.get("checks")
    if isinstance(checks, list):
        for item in checks:
            total += 1
            if not isinstance(item, dict) or "name" not in item or "verdict" not in item or "detail" not in item:
                problems.append("a check without name, verdict and detail")
                continue
            if str(item["verdict"]).upper() == "PASS":
                passed += 1
            elif str(item["verdict"]).upper() == "NOT-AVAILABLE":
                # declared by the author comparison: the author's notebook stores no such output
                not_available += 1
            else:
                problems.append("%s: %s" % (item["name"], item["verdict"]))
    elif isinstance(checks, dict):
        for name, item in checks.items():
            total += 1
            ok = item is True or (isinstance(item, dict) and (item.get("passed") is True or
                                                                str(item.get("verdict", "")).upper() == "PASS"))
            if ok:
                passed += 1
            else:
                problems.append(name)
    elif "results" in document:
        for item in document["results"]:
            total += 1
            if isinstance(item, dict) and item.get("mismatches") == 0:
                passed += 1
            else:
                problems.append("result with mismatches: " + json.dumps(item)[:120])
    else:
        problems.append("no checks")
    if total == 0:
        problems.append("zero checks")
    if "verdict" in document and str(document["verdict"]).upper() not in ("PASS", "SUCCESS"):
        problems.append("verdict " + str(document["verdict"]))
    if document.get("failedCheckCount", 0) != 0:
        problems.append("failedCheckCount %s" % document.get("failedCheckCount"))
    summary = document.get("summary")
    if isinstance(summary, dict):
        for key in ("failed", "FAIL"):
            if summary.get(key, 0) != 0:
                problems.append("summary.%s %s" % (key, summary.get(key)))
    return passed, not_available, total, problems


def reports(arguments):
    # Every report of the step table (also those of steps not run now): the committed record must pass.
    paths = read_list(REPORTS)
    failures = 0
    for path in paths:
        try:
            with open(path, encoding="utf-8") as handle:
                document = json.load(handle)
        except (OSError, ValueError) as error:
            print("revision_report_failed=%s (%s)" % (path, error))
            failures += 1
            continue
        passed, not_available, total, problems = check_verdicts(document)
        extra = " not_available=%d" % not_available if not_available else ""
        if problems:
            failures += 1
            print("revision_report_failed=%s checks=%d/%d%s problems=%s" % (
                path, passed, total, extra, "; ".join(problems)[:400]))
        else:
            print("revision_report=%s checks=%d/%d passed%s" % (path, passed, total, extra))
    print("revision_reports=%d failed=%d" % (len(paths), failures))
    return 1 if failures else 0


def json_equals(arguments):
    path, dotted, expected = arguments
    with open(path, encoding="utf-8") as handle:
        value = json.load(handle)
    for key in dotted.split("."):
        value = value.get(key) if isinstance(value, dict) else None
    print("revision_json_value=%s %s=%s (required %s)" % (path, dotted, value, expected))
    return 0 if str(value) == expected else 1


def tree_files(root):
    found = []
    for directory, _, files in os.walk(root):
        for name in files:
            found.append(os.path.relpath(os.path.join(directory, name), root).replace("\\", "/"))
    return sorted(found)


def same(arguments):
    if len(arguments) % 2 or not arguments:
        return fail("same needs pairs of paths")
    differences, compared = [], 0
    for index in range(0, len(arguments), 2):
        first, second = arguments[index], arguments[index + 1]
        if os.path.isdir(first) and os.path.isdir(second):
            names_first, names_second = tree_files(first), tree_files(second)
            if names_first != names_second:
                differences.append("%s vs %s: different file lists (%d vs %d files)" % (
                    first, second, len(names_first), len(names_second)))
            for name in sorted(set(names_first) & set(names_second)):
                compared += 1
                if not filecmp.cmp(os.path.join(first, name), os.path.join(second, name), shallow=False):
                    differences.append("%s/%s differs" % (first, name))
        elif os.path.isfile(first) and os.path.isfile(second):
            compared += 1
            if not filecmp.cmp(first, second, shallow=False):
                differences.append("%s vs %s differ" % (first, second))
        else:
            differences.append("%s or %s is missing" % (first, second))
    for line in differences[:50]:
        print("revision_difference=" + line)
    print("revision_same_files=%d differences=%d" % (compared, len(differences)))
    return 1 if differences else 0


def notebooks(arguments):
    tool = arguments[0]
    listing = subprocess.run([sys.executable, tool, "list"], capture_output=True, text=True, encoding="utf-8")
    print(listing.stdout, end="")
    if listing.returncode != 0:
        print(listing.stderr, end="")
        return fail("notebook list failed")
    names = [line.split()[0] for line in listing.stdout.splitlines() if line.strip()]
    if not names:
        return fail("no Revision notebook found")
    failures = 0
    for name in names:
        for action in ("audit", "check"):
            sys.stdout.flush()
            code = subprocess.run([sys.executable, tool, action, name]).returncode
            print("revision_notebook=%s action=%s exit_code=%d" % (name, action, code))
            failures += code != 0
    print("revision_notebooks=%d failed_actions=%d" % (len(names), failures))
    return 1 if failures else 0


def flatten(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from flatten(item)
        else:
            yield item


def run_unittests(arguments):
    directory, excluded = arguments
    # The gate test runs this gate itself when REVISION_GATE_FULL=1; never recurse.
    os.environ.pop("REVISION_GATE_FULL", None)
    suite = unittest.defaultTestLoader.discover(directory, pattern="test_*.py")
    tests = list(flatten(suite))
    kept = [test for test in tests if test.id().split(".")[0] != excluded]
    print("revision_unit_tests=%d excluded=%d (%s has its own build)" % (len(kept), len(tests) - len(kept), excluded))
    sys.stdout.flush()
    result = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(unittest.TestSuite(kept))
    return 0 if result.wasSuccessful() else 1


COMMANDS = {
    "plan": plan, "precheck": precheck, "unchanged": unchanged, "reports": reports,
    "json-equals": json_equals, "same": same, "notebooks": notebooks, "unittest": run_unittests,
}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("usage: gate_audit.py " + "|".join(sorted(COMMANDS)) + " ...")
        sys.exit(2)
    sys.exit(COMMANDS[sys.argv[1]](sys.argv[2:]))
'@
[System.IO.File]::WriteAllText((Join-Path $repositoryRoot $stepsFile), ($stepsTable -replace "`r`n", "`n") + "`n", $utf8)
[System.IO.File]::WriteAllText((Join-Path $repositoryRoot $auditScript), ($auditSource -replace "`r`n", "`n") + "`n", $utf8)

$planArguments = @("plan", $stepsFile)
if ($fast) { $planArguments += "--fast" }
if ($dryRun) { $planArguments += "--dry-run" }
if ($stepsOption) { $planArguments += @("--steps", $stepsOption) }
& $pythonCommand $auditScript @planArguments
$planCode = $LASTEXITCODE
if ($planCode -ne 0) { Stop-Gate -Step "plan" -Reason "the step selection was rejected" -Code $planCode }
if ($dryRun) {
    Write-Output "revision_verification=NOT-RUN (dry run: nothing was executed)"
    exit 0
}

$selected = [System.IO.File]::ReadAllLines((Join-Path $repositoryRoot "$gateDirectory/selected.txt"), $utf8)
$selectedText = $selected -join "`n"
$cargoCommand = $null
$wolframscriptCommand = $null
if ($selectedText.Contains("{cargo}")) {
    $cargoCommand = Resolve-Tool "cargo"
    if (-not $cargoCommand) { Stop-Gate -Step "tools" -Reason "cargo was not found" }
    Write-Output "revision_tool_cargo=$cargoCommand"
}
if ($selectedText.Contains("{wolframscript}")) {
    $wolframscriptCommand = Resolve-Tool "wolframscript"
    if (-not $wolframscriptCommand) {
        Stop-Gate -Step "tools" -Reason "wolframscript was not found (install and activate it yourself; the gate never activates it)"
    }
    Write-Output "revision_tool_wolframscript=$wolframscriptCommand"
}
$gitCommand = Resolve-Tool "git"
if (-not $gitCommand) { Stop-Gate -Step "tools" -Reason "git was not found" }
Write-Output "revision_tool_git=$gitCommand"
if ($selectedText.Contains("build_provenance_pdf")) {
    if (-not (Resolve-Tool "pdflatex")) {
        $miktexBin = Join-Path $env:ProgramFiles "MiKTeX\miktex\bin\x64"
        if (-not (Test-Path -LiteralPath (Join-Path $miktexBin "pdflatex.exe"))) {
            Stop-Gate -Step "tools" -Reason "pdflatex was not found on PATH or in $miktexBin"
        }
        # scripts/build_provenance_pdf.py looks pdflatex up on PATH.
        $env:Path = "$miktexBin;$env:Path"
    }
    Write-Output "revision_tool_pdflatex=$(Resolve-Tool 'pdflatex')"
}

$wolframLimitPattern = "licen[cs]e|password|kernel limit|maximum number of" +
    "|too many kernels|could not (launch|start|connect)"

function Invoke-Logged {
    # The log holds started_utc, repository and command lines, the combined output of the command (also
    # echoed) and finished_utc and exit_code lines; returns the exit code.
    param([string]$LogPath, [string[]]$Arguments)
    $logFull = Join-Path $repositoryRoot $LogPath
    $header = "started_utc=$([DateTimeOffset]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'))`n" +
        "repository=$repositoryRoot`ncommand=$($Arguments -join ' ')`n"
    [System.IO.File]::WriteAllText($logFull, $header, $utf8)
    $executable = $Arguments[0]
    $rest = @()
    if ($Arguments.Count -gt 1) { $rest = $Arguments[1..($Arguments.Count - 1)] }
    $previousPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    $global:LASTEXITCODE = 0
    $writer = [System.IO.StreamWriter]::new($logFull, $true, $utf8)
    try {
        & $executable @rest 2>&1 | ForEach-Object {
            $line = "$_"
            $writer.WriteLine($line)
            $writer.Flush()
            Write-Host $line
        }
        $code = $LASTEXITCODE
    } finally {
        $writer.Close()
        $ErrorActionPreference = $previousPreference
    }
    $footer = "finished_utc=$([DateTimeOffset]::UtcNow.ToString('yyyy-MM-ddTHH:mm:ssZ'))`nexit_code=$code`n"
    [System.IO.File]::AppendAllText($logFull, $footer, $utf8)
    return $code
}

function Invoke-GateStep {
    param([string]$Name, [string]$Expected, [string]$Fresh, [string]$Text)
    $words = $Text -split " "
    $arguments = foreach ($token in $words) {
        switch -CaseSensitive ($token) {
            "{python}" { $pythonCommand }
            "{cargo}" { $cargoCommand }
            "{wolframscript}" { $wolframscriptCommand }
            default { $token }
        }
    }
    $maximumAttempts = if ($words[0] -eq "{wolframscript}") { 3 } else { 1 }
    if ($Fresh -ne "-") {
        if (Test-Path -LiteralPath $Fresh) { Remove-Item -LiteralPath $Fresh -Recurse -Force }
        New-Item -ItemType Directory -Force -Path $Fresh | Out-Null
    }
    for ($attempt = 1; $attempt -le $maximumAttempts; $attempt++) {
        $logPath = if ($attempt -eq 1) { "build/logs/revision/$Name-pwsh.log" } else { "build/logs/revision/$Name-attempt$attempt-pwsh.log" }
        Write-Output "revision_step=$Name expected_seconds=$Expected"
        $started = [DateTimeOffset]::UtcNow
        $code = Invoke-Logged -LogPath $logPath -Arguments @($arguments)
        $seconds = [int][Math]::Floor(([DateTimeOffset]::UtcNow - $started).TotalSeconds)
        Write-Output "revision_step_seconds=$Name $seconds (expected $Expected)"
        if ($code -eq 0) {
            Write-Output "revision_step_ok=$Name"
            return
        }
        $retryable = $false
        if ($attempt -lt $maximumAttempts) {
            $retryable = Select-String -LiteralPath (Join-Path $repositoryRoot $logPath) -Pattern $wolframLimitPattern -Quiet
        }
        if (-not $retryable) { Stop-Gate -Step $Name -Log $logPath -Code $code }
        Write-Output "revision_retry=$Name attempt $attempt reported a Wolfram licence or kernel limit; retrying in 30 s"
        Start-Sleep -Seconds 30
    }
}

& $pythonCommand $auditScript precheck
$precheckCode = $LASTEXITCODE
if ($precheckCode -eq 3) {
    Stop-Gate -Step "precheck" -Reason "an output path of a selected step already differs from HEAD (see the revision_preexisting_change lines)" -Code 3
}
if ($precheckCode -ne 0) { Stop-Gate -Step "precheck" -Reason "git status of the output paths could not be read" -Code $precheckCode }

foreach ($line in $selected) {
    if (-not $line) { continue }
    $fields = $line -split "`t"
    Invoke-GateStep -Name $fields[0] -Expected $fields[1] -Fresh $fields[2] -Text $fields[3]
}

Write-Output "revision_gate_seconds=$(Get-GateSeconds)"
Write-Output "revision_verification=OK"
