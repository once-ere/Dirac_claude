@echo off
set "PYTHONUTF8=1"
set "OPENBLAS_NUM_THREADS=1"
set "OMP_NUM_THREADS=1"
cd /d D:\Developer\github\Dirac_claude
echo started %DATE% %TIME% > "%~dp0s5_reference_guarded.start.txt"
python -B scripts\ks_reference_pairs.py --workers 8 --resume > "%~dp0s5_reference_guarded.log" 2>&1
echo exit=%ERRORLEVEL% %DATE% %TIME% >> "%~dp0s5_reference_guarded.done.txt"
