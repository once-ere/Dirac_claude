#!/bin/bash
# assemble SOLUTION.md from the parts, fill the symbol markers, expand the symbol lists, check, and (with "build") build the PDF
set -e
S=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad
R=/home/claude/dirac_claude/universe_model_2
cd $S
python3 sol_tools/coupled_table.py sol_parts/01_coupled.md
# a blank line between the parts, so that the heading that starts each part is a heading
for f in 00_front 01_coupled 02_scheme 10_step1 20_step2 30_step3 40_step4 50_step5 60_step6 70_step7 80_step8 90_step9 \
         95_step10 97_accuracy 99_open; do
  cat sol_parts/$f.md; echo
done | cat -s > sol_src_full.md
python3 sol_tools/automark.py sol_src_full.md $R/SOLUTION.md
cd /home/claude/dirac_claude
python3 universe_model_2/tools/symbols_tool.py expand SOLUTION | tail -2
python3 universe_model_2/tools/symbols_tool.py check SOLUTION | tail -3
if [ "$1" = "build" ]; then
  nice -n 5 python3 universe_model_2/tools/build_docs.py SOLUTION
  grep -n "Overfull" /home/claude/dirac_claude/build/universe_model_2/SOLUTION.log || true
fi
