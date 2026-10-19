#!/bin/bash
# Fill the parts into MODEL.md (inventory displays, AUTO markers), expand the symbol lists, check, summarise.
set -u
M=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/model_v4
ROOT=/home/claude/dirac_claude
cd "$ROOT" || exit 1
python3 "$M"/tools/fill.py universe_model_2/MODEL.md "$M"/parts/p*.md > "$M"/fill.log 2>&1
cat "$M"/fill.log | head -80
python3 universe_model_2/tools/symbols_tool.py expand MODEL > "$M"/expand.log 2>&1
echo "expand exit $?"; head -20 "$M"/expand.log
python3 universe_model_2/tools/symbols_tool.py check MODEL > "$M"/check.log 2>&1
echo "check exit $?"
grep -c '^problem' "$M"/check.log
grep '^problem' "$M"/check.log | head -40
tail -2 "$M"/check.log
