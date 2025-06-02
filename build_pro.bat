@echo off
echo 🎮 Epic Games Manifest Updater Pro - Builder
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Install requirements
echo 📦 Installing Epic requirements...
pip install -r requirements_pro.txt

REM Build the Epic-themed executable
echo.
echo 🔨 Building Epic Games themed executable...
python build_pro.py

REM Check if build was successful
if exist "dist\EpicManifestUpdaterPro.exe" (
    echo.
    echo ✅ Epic Games Manifest Updater Pro build successful!
    echo ✅ Executable: dist\EpicManifestUpdaterPro.exe
    echo ✅ Features: Epic Games theme, advanced tools, stats dashboard
    echo.
    echo 🚀 Ready for Epic gaming experience!
) else (
    echo.
    echo ❌ Build failed!
    echo Check the output above for errors.
)

echo.
pause
