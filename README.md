# Epic Games Transfer Tool

A utility to update Epic Games manifest files after moving game installations to a new location.

[![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white)](EpicManifestUpdater.ps1)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/wesellis/APP-Epic-Games-Transfer-Tool-PowerShell-Manifest-Path-Updater?style=flat-square)](https://github.com/wesellis/APP-Epic-Games-Transfer-Tool-PowerShell-Manifest-Path-Updater/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/wesellis/APP-Epic-Games-Transfer-Tool-PowerShell-Manifest-Path-Updater?style=flat-square)](https://github.com/wesellis/APP-Epic-Games-Transfer-Tool-PowerShell-Manifest-Path-Updater/commits)

## Overview

When you move Epic Games installations to a new drive or folder, the Epic Games Launcher loses track of them. This tool updates the manifest files so the launcher recognizes your games in their new location without requiring re-download.

## Features

- **PowerShell Version**: Simple script with GUI folder selection
- **Python Version**: Cross-platform GUI application with progress tracking
- **Automatic Detection**: Finds and updates all manifest files
- **Safe Operation**: Closes Epic Games Launcher before making changes
- **Batch Updates**: Processes all games in one operation

## Requirements

### PowerShell Version
- Windows 10/11
- PowerShell 5.1+ (included with Windows)
- Epic Games Launcher installed

### Python Version
- Python 3.8 or higher
- tkinter (usually included with Python)
- psutil library

## Installation

### PowerShell Script

No installation needed. Just download `EpicManifestUpdater.ps1` and run it.

### Python GUI

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python epic_manifest_updater.py
```

## Usage

### Before You Start

1. **Move your games first**: Copy or move your Epic Games folders to the new location
2. **Close Epic Games Launcher**: The tool will attempt to close it, but it's safer to close it manually first

### Using the PowerShell Script

1. Right-click `EpicManifestUpdater.ps1` and select "Run with PowerShell"
2. When prompted, select the folder containing your moved games
3. The script will update all manifest files automatically
4. Restart Epic Games Launcher

If you get an execution policy error, run this command in PowerShell as Administrator:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Using the Python GUI

1. Run `python epic_manifest_updater.py`
2. Click "Select New Games Folder" and choose your new games location
3. Click "Update Manifests"
4. The tool will show progress for each game updated
5. Restart Epic Games Launcher

## How It Works

The tool updates manifest files located in:
```
C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests
```

For each `.item` file, it updates:
- `InstallLocation`: Path to the game folder
- `ManifestLocation`: Path to `.egstore` folder
- `StagingLocation`: Path to `.egstore/bps` folder

## Troubleshooting

**Script won't run**: Set PowerShell execution policy (see Usage section)

**Games not found**: Make sure you select the parent folder containing your game folders, not an individual game folder

**Launcher doesn't recognize games**: Restart the Epic Games Launcher completely (close from system tray)

**Some games still missing**: The game folders must have the same names as before you moved them

## Project Structure

```
EpicManifestUpdater.ps1    # PowerShell script version
epic_manifest_updater.py   # Python GUI version
requirements.txt           # Python dependencies
CHANGELOG.md              # Version history
CONTRIBUTING.md           # Contribution guidelines
SECURITY.md               # Security policy
LICENSE                   # MIT License
```

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Disclaimer

This tool modifies Epic Games Launcher manifest files. While it's been tested and works safely, use at your own risk. The tool does not modify game files, only the launcher's configuration files.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgments

- Built for the Epic Games community
- Inspired by the need to avoid re-downloading large game libraries

---

## Project Status & Roadmap

**Completion: ~90%**

### What Works
- ✅ PowerShell script with GUI folder selection
- ✅ Python GUI version with progress tracking
- ✅ Automatic Epic Games Launcher closing
- ✅ Manifest file detection and updating (InstallLocation, ManifestLocation, StagingLocation)
- ✅ Batch processing of all games
- ✅ Cross-platform support (Python version works on Windows/Linux/Mac)
- ✅ User-friendly interfaces for both versions
- ✅ Safe operation (only modifies manifest files, not game data)

### Known Limitations & Missing Features

**Safety Features:**
- ⚠️ **No Backup**: Doesn't create backup of original manifest files before modifying
- ⚠️ **No Undo**: Can't revert changes if something goes wrong
- ⚠️ **No Verification**: Doesn't verify games work after path update

**Error Handling:**
- ⚠️ **Limited Error Messages**: Basic error handling but could be more informative
- ⚠️ **No Validation**: Doesn't verify selected folder contains actual Epic game directories
- ⚠️ **No Recovery**: If Epic launcher is running and can't be closed, script may fail

**Features:**
- ⚠️ **No Logging**: Doesn't create log file of changes made
- ⚠️ **No CLI Mode**: Python version is GUI-only (no command-line arguments)
- ⚠️ **No Dry Run**: Can't preview changes before applying
- ⚠️ **Single Directory Only**: Must move all games to same location (can't handle split libraries)

**Code Quality:**
- ⚠️ **No Tests**: No unit tests or integration tests
- ⚠️ **No Configuration**: Settings are hardcoded (manifest path location)
- ⚠️ **Limited Documentation**: Works well but lacks detailed troubleshooting guide

### What Needs Work

1. **Backup System** - Auto-backup manifest files before modification
2. **Verification** - Check that .egstore folders exist in new location
3. **Better Error Handling** - More informative error messages and validation
4. **Logging System** - Create detailed log file of all changes
5. **Dry Run Mode** - Preview changes before applying
6. **Undo Functionality** - Restore from backups if needed
7. **Multi-Location Support** - Handle games split across multiple drives
8. **CLI Interface** - Add command-line arguments for automation
9. **Testing** - Add unit tests
10. **Enhanced Documentation** - More troubleshooting scenarios

### Current Status

This tool **works reliably** for its core purpose: updating Epic Games manifest files after moving games. It's been tested successfully and does what it claims. The main limitations are around safety features (backups, verification) and edge cases (multi-location libraries, advanced error scenarios).

For most users moving their entire Epic library to a new drive, this tool works perfectly as-is.

### Contributing

If you'd like to help improve the tool, contributions are welcome. Priority areas:
1. Adding automatic manifest backups
2. Implementing verification checks
3. Adding comprehensive error handling
4. Writing tests

---

**Note:** This tool works well for its intended purpose. Core functionality is solid. Safety features and edge case handling could be improved.
