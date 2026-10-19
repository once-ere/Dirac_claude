#!/bin/bash
# Fresh-clone verification of UM-2 version 4: every computation as a separate step, timed; then the comparison and the build.
V=/tmp/claude-0/-home-claude/b01d490e-90a5-59ef-9e41-d6c1af230b6f/scratchpad/verify5
cd $V
rm -rf clone
git clone -q https://github.com/once-ere/Dirac_claude.git clone || exit 2
cd clone
git log --oneline -1 > $V/commit.txt
: > $V/times.txt
run() {
  local t0=$(date +%s.%N)
  timeout -k 5 3000 python3 "$@" > $V/log_$(echo "$*" | tr ' /' '__').txt 2>&1
  local rc=$?
  local t1=$(date +%s.%N)
  echo "$* exit=$rc $(python3 -c "print(round($t1-$t0,1))") s" >> $V/times.txt
}
T0=$(date +%s)
for c in "universe_model_2/code/um2_algebra.py" "universe_model_2/code/um2_geometry.py" "universe_model_2/code/um2_background.py" \
         "universe_model_2/code/um2_fields.py" "universe_model_2/code/um2_spectra.py" "universe_model_2/code/um2_flavour.py" \
         "universe_model_2/code/um2_neutrino.py" "universe_model_2/code/um2_ks_jobs.py validate" "universe_model_2/code/um2_ks_jobs.py spectrum" \
         "universe_model_2/code/um2_ks_jobs.py ground8" "universe_model_2/code/um2_ks_jobs.py ground592" "universe_model_2/code/um2_ks_jobs.py darkmatter" \
         "universe_model_2/code/um2_ks_jobs.py portals" "universe_model_2/code/um2_ks_jobs.py feedback" "universe_model_2/code/um2_electroweak.py" \
         "universe_model_2/code/um2_primordial.py" "universe_model_2/code/um2_cosmology.py" "universe_model_2/code/um2_analysis.py" \
         "universe_model_2/code/um2_thermal.py" "universe_model_2/code/um2_coupled.py" "universe_model_2/code/um2_series.py" "universe_model_2/code/um2_residuals.py" \
         "universe_model_2/tools/build_docs.py"; do
  run $c
done
echo "TOTAL $(( $(date +%s) - T0 )) s" >> $V/times.txt
grep -h "checks, " $V/log_*.txt > $V/checks.txt
grep -h "checks, " $V/log_*.txt | awk '{s += $2; f += $4} END {print "TOTAL", s, "checks,", f, "failed"}' >> $V/checks.txt
python3 universe_model_2/tools/symbols_tool.py check > $V/symbols.txt 2>&1
echo "symbols exit $?" >> $V/symbols.txt
python3 universe_model_2/tools/compare_outputs.py > $V/compare.txt 2>&1
echo "compare exit $?" >> $V/compare.txt
echo DONE > $V/done.txt
