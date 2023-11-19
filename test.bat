@echo off
REM Change the paths below to the actual paths of your .ico and .py files
SET iconPath=D:\Python_Repos\OpenSesame\NPC.ico
SET scriptPath=D:\Python_Repos\OpenSesame\OpenSesame_AI.py

REM Running PyInstaller
pyinstaller --onefile --windowed --icon=%iconPath% %scriptPath%

REM Pause the script to view any messages
pause
