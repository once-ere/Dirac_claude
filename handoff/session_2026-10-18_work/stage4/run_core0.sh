#!/bin/bash
# Core 0: the reference rerun of m1_L3_N1016_lamm2_T0 (STAGE4_SPEC E4.14 b) by --resume on a copy of the
# committed reference tree, then the Rust refined runs (spectrum, scf, excited, emt; the gate's default set).
S=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/stage4
R=/home/claude/dirac_claude
BIN=$S/bin/dirac16complex_kohn_sham
cd $R
rm -rf $S/reference && cp -a $R/artifacts/dirac16complex/kohn-sham/reference $S/reference
date -u +%FT%TZ > $S/ref_start.txt
PYTHONUTF8=1 taskset -c 0 python3 -B scripts/ks_reference_solver.py --resume --skip-self-tests --output $S/reference > $S/ref.log 2>&1
echo "exit=$? $(date -u +%FT%TZ)" > $S/ref_done.txt
: > $S/refined_times.txt
for sub in spectrum scf excited emt; do
  t0=$(date +%s)
  taskset -c 0 $BIN $sub --refined --output $S/refined > $S/refined-$sub.log 2>&1
  rc=$?
  echo "refined $sub exit=$rc $(( $(date +%s) - t0 )) s last=$(tail -1 $S/refined-$sub.log)" >> $S/refined_times.txt
done
echo "done $(date -u +%FT%TZ)" > $S/core0_done.txt
