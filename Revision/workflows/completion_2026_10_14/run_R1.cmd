@echo off
set "PYTHONUTF8=1"
cd /d D:\Developer\github\Dirac_claude
echo started %DATE% %TIME% > "%~dp0start.txt"
python -B scripts\ks_reference_solver.py --config "C:\Users\nsh\AppData\Local\Temp\claude\D--Developer-github-Dirac-claude\9e0a6725-1ba0-4d61-be26-82d9c70a6ded\scratchpad\stage4_keep\refsmear120-config.json" --output "%~dp0out" > "%~dp0run.log" 2>&1
echo exit=%ERRORLEVEL% %DATE% %TIME% >> "%~dp0done.txt"
