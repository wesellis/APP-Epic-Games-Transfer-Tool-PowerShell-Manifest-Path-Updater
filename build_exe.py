#!/usr/bin/env python3
"""
Build script for Epic Games Manifest Updater
Creates a standalone executable using PyInstaller
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def main():
    """Main build process"""
    print("Epic Games Manifest Updater - Build Script")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("ERROR: Python 3.7 or higher is required")
        return False
    
    print(f"✓ Using Python {sys.version}")
    
    # Install requirements
    if not run_command("pip install -r requirements.txt", "Installing requirements"):
        return False
    
    # Build PyInstaller spec file for better control
    spec_content = '''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['epic_manifest_updater.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['tkinter', 'tkinter.ttk', 'tkinter.filedialog', 'tkinter.messagebox'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='EpicManifestUpdater',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
'''
    
    # Write spec file
    with open('EpicManifestUpdater.spec', 'w') as f:
        f.write(spec_content)
    
    print("✓ Created PyInstaller spec file")
    
    # Build executable
    build_command = "pyinstaller --clean EpicManifestUpdater.spec"
    if not run_command(build_command, "Building executable"):
        return False
    
    # Check if build was successful
    exe_path = Path("dist/EpicManifestUpdater.exe")
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"\n🎉 Build successful!")
        print(f"✓ Executable: {exe_path}")
        print(f"✓ Size: {size_mb:.1f} MB")
        print(f"\nYou can now distribute the .exe file!")
        print("No Python installation required on target machines.")
        return True
    else:
        print("\n✗ Build failed - executable not found")
        return False

if __name__ == "__main__":
    success = main()
    input(f"\nPress Enter to exit...")
    sys.exit(0 if success else 1)
