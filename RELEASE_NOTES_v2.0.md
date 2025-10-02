# Epic Games Transfer Tool v2.0 - Production Release

**Release Date:** October 2, 2025

## Overview

Version 2.0 marks the Epic Games Transfer Tool as **production-ready** with comprehensive safety features, verification checks, and detailed logging. This release adds all the critical features needed for safe, reliable manifest file updates.

## What's New in v2.0

### 🔐 Safety Features

**Automatic Backups**
- Creates timestamped backups before any changes
- Backups saved to `Backups/Backup_YYYYMMDD_HHMMSS/` folder
- Asks for confirmation if backup fails
- Complete restore capability (manual copy)

**Verification Checks**
- Validates selected folder exists
- Confirms game folders are present in new location
- Checks for `.egstore` folders (warns if missing)
- Skips games that aren't found

### 📝 Logging & Reporting

**Comprehensive Logging**
- Creates `EpicManifestUpdater.log` in script directory
- Timestamped entries with log levels (INFO, SUCCESS, WARNING, ERROR)
- Complete audit trail of all changes
- Easy to review what happened

**Summary Statistics**
- Shows count of updated manifests
- Reports skipped games (not found in new location)
- Tracks errors during processing
- Displays backup and log file locations

### 🛡️ Error Handling

**Enhanced Robustness**
- Try/catch blocks around all file operations
- Graceful degradation - continues even if individual games fail
- Informative error messages
- Validation of all user inputs

## How to Use v2.0

### Windows (Recommended)

1. **Download** `EpicManifestUpdater.ps1`
2. **Move your games** to the new location first
3. **Right-click** the script and select "Run with PowerShell"
4. **Follow prompts** - script will:
   - Close Epic Games Launcher
   - Create backup of manifests
   - Prompt you to select new games folder
   - Update all manifests
   - Show summary of changes
5. **Start Epic Games Launcher** - your games should be recognized!

### Python (Cross-Platform)

```bash
# Install dependencies
pip install -r requirements.txt

# Run GUI
python epic_manifest_updater.py
```

## Requirements

### PowerShell Version
- Windows 10/11
- PowerShell 5.1+ (included with Windows)
- Epic Games Launcher installed

### Python Version
- Python 3.8 or higher
- tkinter (usually included)
- psutil library

## What's Included

- `EpicManifestUpdater.ps1` - Enhanced PowerShell script
- `epic_manifest_updater.py` - Python GUI version
- `requirements.txt` - Python dependencies
- `README.md` - Complete documentation
- `CHANGELOG.md` - Version history

## Upgrade from v1.x

If you're using v1.x, simply download the new v2.0 script. No configuration changes needed. The new version is backward-compatible and adds safety features without changing how you use it.

## Safety & Reliability

**This version is production-ready:**
- ✅ Automatic backups protect your manifests
- ✅ Verification prevents mistakes
- ✅ Logging provides complete audit trail
- ✅ Error handling prevents crashes
- ✅ Tested with multiple Epic Games installations

## Known Limitations

**By Design:**
- Single directory only (all games must be in same location)
- Manual restore from backup (copy files back from Backups/ folder)
- No dry run mode (but backups make this safe)

**Platform:**
- PowerShell script is Windows-only
- Python version works on Windows/Linux/Mac

These are intentional design decisions to keep the tool simple and focused.

## Troubleshooting

**Script won't run:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Games not found:**
Make sure you select the parent folder containing your game folders, not an individual game folder.

**Launcher doesn't recognize games:**
Restart Epic Games Launcher completely (close from system tray).

**Want to restore backup:**
Copy files from `Backups/Backup_YYYYMMDD_HHMMSS/` back to `C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests\`

## Support

- **Issues:** https://github.com/wesellis/APP-Epic-Games-Transfer-Tool-PowerShell-Manifest-Path-Updater/issues
- **Documentation:** https://github.com/wesellis/APP-Epic-Games-Transfer-Tool-PowerShell-Manifest-Path-Updater#readme

## License

MIT License - See [LICENSE](LICENSE) for details.

## Acknowledgments

- Built for the Epic Games community
- Inspired by the need to avoid re-downloading large game libraries
- Thanks to all users who tested and provided feedback

---

**Thank you for using the Epic Games Transfer Tool!**

If you find this tool helpful, please consider starring the repository on GitHub.
