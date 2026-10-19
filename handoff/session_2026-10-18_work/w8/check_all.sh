#!/bin/bash
# nbkit check (re-execution, byte for byte) of the textbook notebooks not under a chapter agent, one at a time, at low
# priority, with numpy's AVX-512 kernels disabled (NPY_DISABLE_CPU_FEATURES=X86_V4: the Windows builds' bytes) and zlib-ng;
# one result line per notebook in check_all.txt; resumable (notebooks already listed are skipped).
S=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad
W=$S/w8
cd /home/claude/dirac_claude
touch $W/check_all.txt
for b in $(ls Revision/textbook/notebooks/src/[0-2]*.py | grep -v -E "/0[3]|/14|/02z"); do
  n=$(basename $b .py)
  if grep -q "^$n " $W/check_all.txt; then continue; fi
  rm -rf $W/scratch_check; mkdir -p $W/scratch_check
  t0=$(date +%s)
  NPY_DISABLE_CPU_FEATURES=X86_V4 LD_LIBRARY_PATH=$S/zng/build-2.3.3 timeout -k 5 3600 nice -n 15 $S/tb314/bin/python \
      Revision/textbook/tools/nbkit.py check $b --scratch $W/scratch_check > $W/log_check_$n.txt 2>&1
  rc=$?
  r=$(grep -h "^check_.*=PASSED\|^check_.*=FAILED\|^nbkit=" $W/log_check_$n.txt | tr '\n' ' ')
  echo "$n rc=$rc $(( $(date +%s) - t0 ))s $r" >> $W/check_all.txt
done
echo DONE >> $W/check_all.txt
