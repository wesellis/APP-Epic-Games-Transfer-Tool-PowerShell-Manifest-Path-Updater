@echo off
echo Epic Games Manifest Updater - Quick Launcher
echo =============================================
echo.

REM Check if we're in the right directory
if not exist "epic_manifest_updater_clean.py" (
    echo [ERROR] ERROR: Not in the epic-manifest-updater directory
    echo Please navigate to A:\GITHUB\epic-manifest-updater first
    echo Example: cd A:\GITHUB\epic-manifest-updater
    pause
    exit /b 1
)

echo [TEST] Testing dependencies...
python test_clean.py

echo.
echo [RUN] Starting Epic Games Manifest Updater...
python epic_manifest_updater_clean.py

echo.
echo App closed. Press any key to exit.
pause >nul
