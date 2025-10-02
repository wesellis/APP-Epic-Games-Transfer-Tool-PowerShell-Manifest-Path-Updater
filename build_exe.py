#!/usr/bin/env python3
"""
Build script for creating standalone Epic Manifest Updater executable
Requires: pip install pyinstaller
"""

import os
import subprocess
import sys
from pathlib import Path

# Get project root
PROJECT_ROOT = Path(__file__).parent

# Build configuration
APP_NAME = "EpicManifestUpdater"
VERSION = "2.0.0"

def build_exe():
    """Build standalone executable with PyInstaller"""

    print(f"\n{'='*60}")
    print(f"Building {APP_NAME} v{VERSION} Standalone Executable")
    print(f"{'='*60}\n")

    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("Error: PyInstaller not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--name", APP_NAME,
        "--onefile",  # Single executable
        "--windowed",  # GUI application (no console)
        "--clean",
        # Hidden imports
        "--hidden-import", "tkinter",
        "--hidden-import", "psutil",
        str(PROJECT_ROOT / "epic_manifest_updater.py")
    ]

    # Run PyInstaller
    print("Running PyInstaller...")
    result = subprocess.run(cmd, cwd=PROJECT_ROOT)

    if result.returncode == 0:
        exe_path = PROJECT_ROOT / 'dist' / f'{APP_NAME}.exe'
        print(f"\n{'='*60}")
        print(f"✓ Build successful!")
        print(f"{'='*60}")
        print(f"\nExecutable location: {exe_path}")
        if exe_path.exists():
            print(f"Size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
    else:
        print("\n✗ Build failed!")
        sys.exit(1)

if __name__ == "__main__":
    build_exe()
