#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Origin: scripts/run_logged.sh of https://github.com/once-ere/dirac
# (GPL-3.0-or-later), copied into this repository on 2026-09-25.
#
# Changes relative to the origin: this header, a trailing newline at the end
# of the file, and one trailing blank removed after printf 'command='.  The
# code is otherwise unchanged.
#
# Usage: scripts/run_logged.sh LOG_PATH [--] COMMAND [ARG ...]
# A relative LOG_PATH is resolved against the repository root; the command
# runs in the current directory.  The log starts with started_utc, repository
# and command lines, then holds the combined stdout/stderr of the command
# (also echoed to the terminal), and ends with finished_utc and exit_code
# lines.  The script exits with the command's exit code.
set -euo pipefail

if (($# < 2)); then
    echo "usage: $0 LOG_PATH [--] COMMAND [ARG ...]" >&2
    exit 2
fi

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repository_root="$(cd -- "$script_dir/.." && pwd)"
log_path="$1"
shift
if [[ "${1:-}" == "--" ]]; then
    shift
fi
if (($# == 0)); then
    echo "missing command" >&2
    exit 2
fi

if [[ "$log_path" != /* ]]; then
    log_path="$repository_root/$log_path"
fi
mkdir -p -- "$(dirname -- "$log_path")"

{
    printf 'started_utc=%s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    printf 'repository=%s\n' "$repository_root"
    printf 'command='
    printf '%q ' "$@"
    printf '\n'
} >"$log_path"

set +e
"$@" 2>&1 | tee -a "$log_path"
command_exit_code=${PIPESTATUS[0]}
set -e

{
    printf 'finished_utc=%s\n' "$(date -u +'%Y-%m-%dT%H:%M:%SZ')"
    printf 'exit_code=%d\n' "$command_exit_code"
} >>"$log_path"

exit "$command_exit_code"
