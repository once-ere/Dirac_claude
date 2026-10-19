#!/bin/bash
# Core 1: a complete canonical repeat of the five Rust subcommands (for the checker's byte-identity check).
S=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/stage4
R=/home/claude/dirac_claude
BIN=$S/bin/dirac16complex_kohn_sham
cd $R
: > $S/repeat_times.txt
for sub in spectrum scf excited emt thermo; do
  t0=$(date +%s)
  taskset -c 1 $BIN $sub --output $S/repeat > $S/repeat-$sub.log 2>&1
  rc=$?
  echo "repeat $sub exit=$rc $(( $(date +%s) - t0 )) s last=$(tail -1 $S/repeat-$sub.log)" >> $S/repeat_times.txt
done
echo "done $(date -u +%FT%TZ)" > $S/core1_done.txt
