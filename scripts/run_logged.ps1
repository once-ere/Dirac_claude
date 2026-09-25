# SPDX-License-Identifier: GPL-3.0-or-later
#
# Origin: scripts/run_logged.ps1 of https://github.com/once-ere/dirac
# (GPL-3.0-or-later), copied into this repository on 2026-09-25.
#
# Changes relative to the origin: this header, and a trailing newline at the
# end of the file.  The code is unchanged.
#
# Usage (from any directory; a relative -LogPath is resolved against the
# repository root, and the command runs in the current directory):
#   & scripts/run_logged.ps1 -LogPath build/logs/a.log -Command "python a.py"
# The log starts with started_utc, repository and command lines, then holds
# the combined stdout/stderr of the command (also echoed to the console), and
# ends with finished_utc and exit_code lines.  The script exits with the
# command's exit code.
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$LogPath,

    [Parameter(Mandatory = $true)]
    [string]$Command
)

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
$resolvedLogPath = if ([System.IO.Path]::IsPathRooted($LogPath)) {
    $LogPath
} else {
    Join-Path $repositoryRoot $LogPath
}

$logDirectory = Split-Path -Parent $resolvedLogPath
New-Item -ItemType Directory -Path $logDirectory -Force | Out-Null

$startedAt = [DateTimeOffset]::UtcNow.ToString("o")
@(
    "started_utc=$startedAt"
    "repository=$repositoryRoot"
    "command=$Command"
) | Set-Content -LiteralPath $resolvedLogPath -Encoding utf8NoBOM

$script:commandExitCode = 0
$scriptBlock = [ScriptBlock]::Create($Command)
& {
    & $scriptBlock
    $commandSucceeded = $?
    $nativeExitCode = $LASTEXITCODE
    if (-not $commandSucceeded) {
        $script:commandExitCode = 1
    } elseif ($null -ne $nativeExitCode) {
        $script:commandExitCode = $nativeExitCode
    }
} 2>&1 | Tee-Object -FilePath $resolvedLogPath -Append

$finishedAt = [DateTimeOffset]::UtcNow.ToString("o")
@(
    "finished_utc=$finishedAt"
    "exit_code=$script:commandExitCode"
) | Add-Content -LiteralPath $resolvedLogPath -Encoding utf8NoBOM

exit $script:commandExitCode
