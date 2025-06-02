@echo off
echo Building Epic Games Manifest Updater...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

REM Build the executable
echo.
echo Building executable...
pyinstaller --onefile --windowed --name "EpicManifestUpdater" --icon=icon.ico epic_manifest_updater.py

REM Check if build was successful
if exist "dist\EpicManifestUpdater.exe" (
    echo.
    echo ✓ Build successful!
    echo ✓ Executable created: dist\EpicManifestUpdater.exe
    echo.
    echo You can now distribute the .exe file without requiring Python!
) else (
    echo.
    echo ✗ Build failed!
    echo Check the output above for errors.
)

echo.
pause
