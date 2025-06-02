@echo off
echo Epic Games Manifest Updater - Simple Build
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

echo [INSTALL] Installing requirements...
pip install psutil pyinstaller

echo.
echo [BUILD] Building simple Epic-themed executable...
pyinstaller --onefile --windowed --name "EpicManifestUpdaterClean" epic_manifest_updater_clean.py

REM Check if build was successful
if exist "dist\EpicManifestUpdaterClean.exe" (
    echo.
    echo [SUCCESS] Build successful!
    echo [SUCCESS] Executable: dist\EpicManifestUpdaterClean.exe
    echo [SUCCESS] Features: Epic Games theme, working manifest updater
    echo.
    echo [SUCCESS] This version should work without issues!
    echo.
    echo [TEST] To test: python epic_manifest_updater_clean.py
) else (
    echo.
    echo [ERROR] Build failed!
    echo Check the output above for errors.
)

echo.
pause
