#!/bin/bash
# H15 rerun (W5): every step under timeout -k 5 423, in order, stop at the first failure; one line per step in the log
# (the per-step output in h15_<step>.log).  Steps: Rust build, test, canonical repeat (3 parts, assembly, byte-for-byte
# against the committed record), refined run (4 parts, assembly), determinism report, the refinement measurement, the
# reference (2 stages x 6 parts, assembly), the cross-check's repeat (2 x 6 parts), the cross-check, the tip study,
# the dense history, the Kohn-Sham source of the a4 equations.
S="C:/Users/nsh/AppData/Local/Temp/claude/D--Developer-github-Dirac-claude/837d3989-831c-4131-a54e-de216022bedc/scratchpad"
cd /d/Developer/github/Dirac_claude || exit 1
BIN=Revision/kohn_sham/solver/target/release/revision_ks_solver.exe
ONLY="${1:-all}"
step() {  # name, command...
  local name=$1; shift
  local t0=$(date +%s.%N)
  timeout -k 5 423 "$@" > "$S/h15_$name.log" 2>&1
  local rc=$?
  local t1=$(date +%s.%N)
  awk -v n="$name" -v r="$rc" -v a="$t0" -v b="$t1" 'BEGIN { printf "%s rc=%d %.1f s\n", n, r, b - a }'
  if [ $rc -ne 0 ]; then echo "STOPPED at $name"; tail -5 "$S/h15_$name.log"; exit 1; fi
}
if [ "$ONLY" = all ] || [ "$ONLY" = rust ]; then
  step rust-build cargo build --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
  step rust-test cargo test --release --manifest-path Revision/kohn_sham/solver/Cargo.toml
  rm -rf build/revision/ks-repeat-cache build/revision/ks-repeat
  for i in 1 2 3; do step rust-repeat-p$i $BIN all --cache build/revision/ks-repeat-cache --part $i/3 --inner-threads 2; done
  step rust-repeat $BIN all --cache build/revision/ks-repeat-cache --out build/revision/ks-repeat/results --report build/revision/ks-repeat/report.json --inner-threads 3
  step rust-repeat-identical python "$S/same_tree.py" build/revision/ks-repeat/results Revision/kohn_sham/results build/revision/ks-repeat/report.json Revision/kohn_sham/reports/ks-rust-solver.json
  rm -rf build/revision/ks-refined-cache build/revision/ks-refined
  for i in 1 2 3 4; do step rust-refined-p$i $BIN all --refined --cache build/revision/ks-refined-cache --part $i/4; done
  step rust-refined $BIN all --refined --cache build/revision/ks-refined-cache --out build/revision/ks-refined/results --report build/revision/ks-refined/report.json
  step rust-determinism python Revision/kohn_sham/solver/tools/compare_runs.py --canonical Revision/kohn_sham/results --canonical-report Revision/kohn_sham/reports/ks-rust-solver.json --repeat build/revision/ks-repeat/results --repeat-report build/revision/ks-repeat/report.json --refined build/revision/ks-refined/results --refined-report build/revision/ks-refined/report.json --report Revision/kohn_sham/reports/ks-rust-determinism.json
  rm -rf build/revision/ks-refinement
  step rust-refinement python Revision/kohn_sham/checker/measure_rust_refinement.py --work build/revision/ks-refinement
fi
if [ "$ONLY" = all ] || [ "$ONLY" = reference ]; then
  rm -rf build/revision/ks-reference-cache
  for st in 1 2; do for i in 1 2 3 4 5 6; do step ref-s${st}p$i python Revision/kohn_sham/reference/run_reference.py --cache build/revision/ks-reference-cache --stage $st --part $i/6 --jobs 20; done; done
  step ref-assembly python Revision/kohn_sham/reference/run_reference.py --cache build/revision/ks-reference-cache
  rm -rf build/revision/ks-crosscheck-cache
  for st in 1 2; do for i in 1 2 3 4 5 6; do step cc-s${st}p$i python Revision/kohn_sham/reference/run_reference.py --cache build/revision/ks-crosscheck-cache --stage $st --part $i/6 --jobs 20; done; done
  rm -rf build/revision/ks-crosscheck
  step crosscheck python Revision/kohn_sham/checker/crosscheck_ks.py --work build/revision/ks-crosscheck --jobs 22 --repeat-cache build/revision/ks-crosscheck-cache
fi
if [ "$ONLY" = all ] || [ "$ONLY" = tip ]; then
  rm -rf build/revision/ks-tip-convergence
  for i in 1 2 3 4 5 6; do step tip-scan-p$i python Revision/kohn_sham/tip_convergence/tip_convergence.py --work build/revision/ks-tip-convergence --jobs 22 --stage scan --part $i/6; done
  for i in 1 2 3; do step tip-recal-p$i python Revision/kohn_sham/tip_convergence/tip_convergence.py --work build/revision/ks-tip-convergence --jobs 22 --stage recal --part $i/3; done
  step tip-final python Revision/kohn_sham/tip_convergence/tip_convergence.py --work build/revision/ks-tip-convergence --jobs 22 --stage final
fi
if [ "$ONLY" = all ] || [ "$ONLY" = history ]; then
  rm -rf build/revision/ks-history-work
  for i in 1 2 3; do step hist-p$i python Revision/dark_sector/dirac16complex/compute/run_ks_history.py --solver $BIN --jobs 22 --work build/revision/ks-history-work --part $i/3; done
  step hist-assembly python Revision/dark_sector/dirac16complex/compute/run_ks_history.py --solver $BIN --jobs 22 --work build/revision/ks-history-work
  step ks-source-conditions python Revision/field_equations_a4/python/check_ks_source_conditions.py
  step ks-source python Revision/field_equations_a4/ks_source/ks_source_a4.py
  step ks-source-test python -m unittest Revision/field_equations_a4/ks_source/test_ks_source_a4.py
fi
echo "ALL STEPS DONE"
exit 0
