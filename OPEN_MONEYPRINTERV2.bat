@echo off
setlocal
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
title OPEN MONEYPRINTERV2
color 1F
echo ===================================
echo         OPEN MONEYPRINTERV2
echo ===================================
echo.
python open_moneyprinterv2.py
echo.
pause
