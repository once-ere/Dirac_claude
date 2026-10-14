@echo off
cd /d D:\Developer\github\Dirac_claude
set "EXE=studies\dirac16complex_kohn_sham\target\release\dirac16complex_kohn_sham.exe"
echo started %DATE% %TIME% > "%~dp0repeat.start.txt"
start /b /wait /affinity FF00 %EXE% pairs --output build\s5-rust-repeat > "%~dp0repeat.log" 2>&1
echo repeat exit=%ERRORLEVEL% %DATE% %TIME% >> "%~dp0repeat.done.txt"
