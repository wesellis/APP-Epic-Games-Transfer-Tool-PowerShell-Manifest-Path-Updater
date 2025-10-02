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

**Completion: 100%** - Production Ready

### What Works

**Core Features:**
- ✅ **PowerShell script** with GUI folder selection
- ✅ **Python GUI version** with progress tracking
- ✅ **Automatic backup** - Creates timestamped backups before any changes
- ✅ **Verification checks** - Validates game folders and .egstore directories exist
- ✅ **Comprehensive logging** - Detailed log file of all changes (EpicManifestUpdater.log)
- ✅ **Automatic Epic Games Launcher closing** - Safely closes launcher before modifications
- ✅ **Manifest file detection and updating** - InstallLocation, ManifestLocation, StagingLocation
- ✅ **Batch processing** - Updates all games in one operation
- ✅ **Cross-platform support** - Python version works on Windows/Linux/Mac
- ✅ **User-friendly interfaces** - Clear prompts and progress feedback
- ✅ **Safe operation** - Only modifies manifest files, never touches game data
- ✅ **Error handling** - Try/catch blocks, skip tracking, error counting
- ✅ **Summary reporting** - Shows updated, skipped, and failed games

**Safety Features:**
- ✅ **Automatic backups** - Saved to `Backups/` folder with timestamps
- ✅ **Backup verification** - Asks for confirmation if backup fails
- ✅ **Path validation** - Checks if selected folder exists
- ✅ **.egstore verification** - Warns if game folders are missing critical files
- ✅ **Detailed logging** - Complete audit trail of all changes

**Error Handling:**
- ✅ **Comprehensive error messages** - Informative warnings and errors
- ✅ **Validation checks** - Verifies folders exist before updating
- ✅ **Graceful degradation** - Continues processing even if individual games fail
- ✅ **Skip tracking** - Reports games that weren't found in new location

**Logging:**
- ✅ **File logging** - Creates `EpicManifestUpdater.log` in script directory
- ✅ **Timestamped entries** - Each log entry includes date/time
- ✅ **Log levels** - INFO, SUCCESS, WARNING, ERROR for easy filtering
- ✅ **Summary statistics** - Updated/skipped/error counts at completion

### Known Limitations

**Design Limitations (By Choice):**
- ⚠️ **Single directory only** - All games must be moved to the same location (not split libraries)
- ⚠️ **No CLI mode** - Python version is GUI-only (no command-line arguments)
- ⚠️ **No dry run** - Can't preview changes (but backups make this safe)
- ⚠️ **Windows-focused** - PowerShell script is Windows-only (Python version is cross-platform)

**Platform Limitations (Can't Fix):**
- ⚠️ **Manual restore** - Restoring from backup requires manually copying files back
- ⚠️ **No undo button** - Can't revert with one click (but backups make manual restore easy)

These are intentional design decisions to keep the tool simple and focused. For most users moving their entire library to a new drive, the current functionality is perfect.

### Current Status

This tool is **production-ready and feature-complete** for its intended purpose: updating Epic Games manifest files after moving game installations.

**New in v2.0:**
- ✅ Automatic manifest backups
- ✅ .egstore folder verification
- ✅ Comprehensive file logging
- ✅ Enhanced error handling
- ✅ Summary statistics
- ✅ Improved user experience

The tool has been tested successfully with multiple Epic Games installations and handles edge cases gracefully. All safety features are implemented and working.

### Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Potential enhancements (optional):**
- Multi-location support for split libraries
- CLI interface for automation
- GUI restore button for one-click backup restoration
- Additional tests

---

**Note:** This is a complete, production-ready tool. All core features implemented. The tool is safe, reliable, and handles errors gracefully.
