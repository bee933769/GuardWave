@echo off
REM GuardWave Windows Launcher

IF EXIST "..\venv\Scripts\activate.bat" (
    call ..\venv\Scripts\activate.bat
)

python ..\src\guardwave.py
pause
