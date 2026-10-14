@echo off
cd /d D:\Developer\github\Dirac_claude
set "EXE=studies\dirac16complex_kohn_sham\target\release\dirac16complex_kohn_sham.exe"
echo started %DATE% %TIME% > "%~dp0canonical.start.txt"
start /b /wait /affinity FF %EXE% pairs > "%~dp0canonical.log" 2>&1
echo canonical exit=%ERRORLEVEL% %DATE% %TIME% >> "%~dp0done.txt"
start /b /wait /affinity FF %EXE% pairs --refined --output build\s5-rust-refined > "%~dp0refined.log" 2>&1
echo refined exit=%ERRORLEVEL% %DATE% %TIME% >> "%~dp0done.txt"
