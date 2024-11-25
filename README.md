# 🎮 Epic Games Manifest Updater

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=flat&logo=powershell&logoColor=white)](EpicManifestUpdater.ps1)

A PowerShell script that helps you update Epic Games manifest files after moving your game installations. No more manual file editing or game re-downloading needed!

## 🚀 Quick Start

1. **Prepare:**
   - Move your Epic Games folder to its new location
   - Note the new folder path

2. **Download:**
   - Download `EpicManifestUpdater.ps1`
   - Right-click the script and select "Properties"
   - Check "Unblock" if present, then click OK

3. **Run:**
   - Right-click `EpicManifestUpdater.ps1`
   - Select "Run with PowerShell"
   - Epic Games Launcher will automatically close
   - Select your new games folder in the popup window
   - Wait for completion message

4. **Finish:**
   - Start Epic Games Launcher
   - Your games should now be detected in the new location

## ✨ Features

- 🔄 Automatically closes Epic Games Launcher
- 📂 User-friendly folder selection
- 🎯 Updates all manifest paths automatically
- 🎨 Color-coded console output
- ⚡ No manual file editing needed
- 🛡️ Safe to use - no game files are modified

## 📋 Requirements

- Windows 10/11
- PowerShell 5.1 or newer
- Epic Games Launcher installed
- Games already moved to new location

## ⚠️ Important Notes

- **Backup:** While this script is safe, it's always good practice to backup your manifest files before running
- **Location:** Found in `C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests`
- **Games:** Must be moved/copied before running this script
- **Admin:** May require administrator rights depending on manifest location

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest enhancements
- Submit pull requests

## 📄 License

[MIT](LICENSE) - Feel free to use and modify as needed!
