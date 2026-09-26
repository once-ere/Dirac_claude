# setup_solver.ps1 -- fetch the pinned pure-Rust SUNDIALS 7.8.0 engine (Windows 11).
#
# PowerShell twin of scripts/setup_solver.sh.  Clones the rustSolveIt
# repository at a pinned commit into vendor\rustSolveIt (git-ignored) with a
# sparse checkout of sundials_rs and the planet_Mercury notebook templates.
#
# Usage:  .\scripts\setup_solver.ps1 [-Platform win11|macos|linux]
param([ValidateSet('win11','macos','linux')][string]$Platform = 'win11')
$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
$target = Join-Path $repoRoot 'vendor\rustSolveIt'

$pins = @{
  win11 = @('https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0.git',
            'a8fdff459adfe181573d7924b18bffbdf378fdb3')
  macos = @('https://github.com/once-ere/rustSolveIt_macos-silicon_SUNDIALS_7_8_0.git',
            '5360157f4f6160978f66400566c31b2ae25dd44d')
  linux = @('https://github.com/once-ere/rustSolveIt_linux_SUNDIALS_7_8_0.git',
            '6f58e02e53717a51375bd4bc5918edc57088d922')
}
$url = $pins[$Platform][0]
$pin = $pins[$Platform][1]

function Invoke-Git {
  & git @args
  if ($LASTEXITCODE -ne 0) { throw "git $($args -join ' ') failed ($LASTEXITCODE)" }
}

if (Test-Path (Join-Path $target '.git')) {
  $have = (& git -C $target rev-parse -q --verify HEAD 2>$null)
  if ($LASTEXITCODE -ne 0 -or -not $have) {
    throw "vendor\rustSolveIt is an incomplete checkout (an interrupted or failed download); remove it and rerun"
  }
  $have = $have.Trim()
  if ($have -eq $pin) {
    "solver_platform=$Platform"
    "solver_commit=$have"
    'solver_setup=ALREADY-PRESENT'
    exit 0
  }
  throw "vendor\rustSolveIt is at $have, expected $pin; remove it and rerun"
}

New-Item -ItemType Directory -Force -Path $target | Out-Null
Invoke-Git -C $target init -q
Invoke-Git -C $target remote add origin $url
Invoke-Git -C $target sparse-checkout init --cone
Invoke-Git -C $target sparse-checkout set sundials_rs planet_Mercury/notebook
Invoke-Git -C $target fetch -q --depth 1 origin $pin
Invoke-Git -C $target checkout -q FETCH_HEAD

$have = (& git -C $target rev-parse HEAD).Trim()
if ($have -ne $pin) { throw "fetched $have, expected $pin" }
foreach ($crate in 'sundials_core', 'cvode_rs') {
  $manifest = Join-Path $target "sundials_rs\crates\$crate\Cargo.toml"
  if (-not (Test-Path $manifest)) { throw "missing $manifest" }
}
"solver_platform=$Platform"
"solver_commit=$have"
'solver_setup=OK'
