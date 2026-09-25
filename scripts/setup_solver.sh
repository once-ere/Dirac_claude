#!/usr/bin/env bash
# setup_solver.sh -- fetch the pinned pure-Rust SUNDIALS 7.8.0 engine.
#
# The numerical study studies/dirac16complex_cosmology path-depends on
#   vendor/rustSolveIt/sundials_rs/crates/{sundials_core,cvode_rs}
# This script clones the platform's rustSolveIt repository at a pinned commit
# into vendor/rustSolveIt (vendor/ is git-ignored: the engine is fetched, not
# redistributed).  All three platform repositories vendor a byte-identical
# sundials_rs; only the surrounding tooling differs.
#
# Usage:  bash scripts/setup_solver.sh [win11|macos|linux]
#         (default: detected from uname)
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
target="${repo_root}/vendor/rustSolveIt"

platform="${1:-}"
if [[ -z "${platform}" ]]; then
  case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*) platform=win11 ;;
    Darwin*)              platform=macos ;;
    Linux*)               platform=linux ;;
    *) echo "cannot detect platform; pass win11, macos or linux" >&2; exit 2 ;;
  esac
fi

case "${platform}" in
  win11) url=https://github.com/once-ere/rustSolveIt_Win11_SUNDIALS_7_8_0.git
         pin=a8fdff459adfe181573d7924b18bffbdf378fdb3 ;;
  macos) url=https://github.com/once-ere/rustSolveIt_macos-silicon_SUNDIALS_7_8_0.git
         pin=5360157f4f6160978f66400566c31b2ae25dd44d ;;
  linux) url=https://github.com/once-ere/rustSolveIt_linux_SUNDIALS_7_8_0.git
         pin=6f58e02e53717a51375bd4bc5918edc57088d922 ;;
  *) echo "unknown platform '${platform}'" >&2; exit 2 ;;
esac

if [[ -d "${target}/.git" ]]; then
  have="$(git -C "${target}" rev-parse HEAD)"
  if [[ "${have}" == "${pin}" ]]; then
    echo "solver_platform=${platform}"
    echo "solver_commit=${have}"
    echo "solver_setup=ALREADY-PRESENT"
    exit 0
  fi
  echo "vendor/rustSolveIt is at ${have}, expected ${pin}; remove it and rerun" >&2
  exit 1
fi

mkdir -p "${target}"
git -C "${target}" init -q
git -C "${target}" remote add origin "${url}"
# Only the engine and the Jupyter notebook templates are needed.
git -C "${target}" sparse-checkout init --cone
git -C "${target}" sparse-checkout set sundials_rs planet_Mercury/notebook
git -C "${target}" fetch -q --depth 1 origin "${pin}"
git -C "${target}" checkout -q FETCH_HEAD

have="$(git -C "${target}" rev-parse HEAD)"
if [[ "${have}" != "${pin}" ]]; then
  echo "fetched ${have}, expected ${pin}" >&2
  exit 1
fi
for crate in sundials_core cvode_rs; do
  test -f "${target}/sundials_rs/crates/${crate}/Cargo.toml"
done
echo "solver_platform=${platform}"
echo "solver_commit=${have}"
echo "solver_setup=OK"
