# Troubleshooting Guide

This guide helps you resolve common issues with the Epic Games Manifest Updater.

## 🚨 Common Issues

### 1. "Execution Policy" Error

**Error Message:**
```
execution of scripts is disabled on this system
```

**Solution:**
```powershell
# Run this command in PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Alternative Solution:**
- Right-click the script → "Run with PowerShell"
- When prompted, type `Y` and press Enter

### 2. "Access Denied" Error

**Error Message:**
```
Access to the path 'C:\ProgramData\Epic\...' is denied
```

**Solutions:**
1. **Run as Administrator:**
   - Right-click PowerShell → "Run as administrator"
   - Navigate to script location and run it

2. **Check Permissions:**
   - Ensure your user has access to the Epic Games data folder
   - Contact your system administrator if on a managed system

### 3. "Cannot find Epic Games manifests directory!"

**Possible Causes:**
- Epic Games Launcher not installed
- Custom installation location
- Corrupted installation

**Solutions:**
1. **Verify Installation:**
   ```powershell
   Test-Path "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"
   ```

2. **Find Custom Location:**
   - Check Epic Games Launcher settings
   - Look for alternative installation paths

3. **Reinstall Epic Games Launcher:**
   - Download from [Epic Games website](https://www.epicgames.com/store/download)

### 4. Games Still Not Detected After Running Script

**Check These Items:**

1. **Verify Game Folders Exist:**
   - Check that games are actually in the new location
   - Ensure folder names match exactly

2. **Restart Epic Games Launcher:**
   - Close completely (check system tray)
   - Restart and wait for library to refresh

3. **Check Manifest Files:**
   ```powershell
   # Check if manifests were updated
   Get-ChildItem "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests" -Filter "*.item" | 
       ForEach-Object { 
           $content = Get-Content $_.FullName | ConvertFrom-Json
           Write-Host "$($_.Name): $($content.InstallLocation)"
       }
   ```

### 5. Script Hangs or Freezes

**Potential Causes:**
- Epic Games Launcher not closing properly
- Antivirus interference
- Corrupted manifest files

**Solutions:**
1. **Manual Process Termination:**
   ```powershell
   Get-Process -Name "EpicGamesLauncher", "EpicWebHelper" | Stop-Process -Force
   ```

2. **Check Task Manager:**
   - Look for stuck Epic Games processes
   - End them manually if needed

3. **Disable Antivirus Temporarily:**
   - Some antivirus software blocks PowerShell scripts
   - Add script to exclusions or disable temporarily

### 6. "No folder selected" Message

**Cause:**
- Folder browser dialog was cancelled
- No folder was selected

**Solution:**
- Run the script again
- Make sure to select a folder in the dialog
- Choose the folder containing your game directories

### 7. Special Characters in Paths

**Issues:**
- Paths with spaces, unicode characters, or special symbols
- Non-English folder names

**Solutions:**
1. **Avoid Special Characters:**
   - Use simple folder names when possible
   - Avoid spaces, special characters, and unicode

2. **Test Path Validity:**
   ```powershell
   Test-Path "Your\Game\Path\Here"
   ```

### 8. Multiple Epic Games Installations

**Current Limitation:**
- Script only supports one Epic Games installation per system

**Workaround:**
- Run the script for each installation separately
- Modify the script to specify different manifest directories

## 🔍 Advanced Troubleshooting

### Debug Mode

Add verbose output to the script for troubleshooting:

```powershell
# Add this line at the beginning of the script
$VerbosePreference = "Continue"
```

### Manual Manifest Inspection

Check individual manifest files:

```powershell
# View a specific manifest file
$manifestPath = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests\YourGame.item"
$content = Get-Content $manifestPath | ConvertFrom-Json
$content | ConvertTo-Json -Depth 3
```

### Backup and Restore

Create a backup of your manifests:

```powershell
# Backup manifests
$backupPath = "$env:USERPROFILE\Desktop\EpicManifestBackup"
$manifestsPath = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"
Copy-Item $manifestsPath $backupPath -Recurse

# Restore from backup if needed
Copy-Item "$backupPath\*" $manifestsPath -Force
```

### Check Epic Games Launcher Logs

Epic Games Launcher logs can provide additional insights:

**Log Locations:**
- `%LOCALAPPDATA%\EpicGamesLauncher\Saved\Logs`
- Look for recent `.log` files

**What to Look For:**
- Error messages about missing games
- Path-related errors
- Authentication issues

## 🛠️ Prevention Tips

### Before Moving Games

1. **Create a Backup:**
   - Backup your manifest files
   - Note down current game locations

2. **Plan Your Move:**
   - Ensure target drive has enough space
   - Verify folder permissions

3. **Move Games Properly:**
   - Copy entire game folders, including subdirectories
   - Don't rename game folders during the move

### After Using the Script

1. **Verify Results:**
   - Check Epic Games Launcher library
   - Launch a game to test functionality

2. **Keep Backups:**
   - Keep manifest backups until confirmed working
   - Document your new game locations

## 📞 Getting Additional Help

### Before Seeking Help

1. **Check System Requirements:**
   - Windows 10/11
   - PowerShell 5.1+
   - Epic Games Launcher installed

2. **Gather Information:**
   - Exact error messages
   - PowerShell version (`$PSVersionTable.PSVersion`)
   - Epic Games Launcher version
   - Console output from the script

3. **Try Basic Solutions:**
   - Restart Epic Games Launcher
   - Run script as Administrator
   - Check that games exist in new location

### Support Channels

- **GitHub Issues:** [Report bugs or request help](https://github.com/wesellis/epic-manifest-updater/issues)
- **GitHub Discussions:** [Ask questions and share experiences](https://github.com/wesellis/epic-manifest-updater/discussions)
- **Documentation:** Check README.md for detailed instructions

### Information to Include in Support Requests

1. **System Information:**
   - Operating System version
   - PowerShell version
   - Epic Games Launcher version

2. **Error Details:**
   - Complete error messages
   - Console output from script
   - Screenshots if helpful

3. **Context:**
   - What you were trying to accomplish
   - Steps taken before the error
   - Whether it worked before

4. **Environment:**
   - Original game location
   - New game location
   - Number and names of affected games

## 🔄 Recovery Procedures

### Complete Reset

If everything goes wrong:

1. **Restore from Backup:**
   ```powershell
   # Restore manifest backups
   Copy-Item "$env:USERPROFILE\Desktop\EpicManifestBackup\*" "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests" -Force
   ```

2. **Reinstall Epic Games Launcher:**
   - Uninstall Epic Games Launcher
   - Download and reinstall from Epic Games website
   - Re-add your library locations

3. **Re-verify Games:**
   - Use Epic Games Launcher's verify feature
   - Point to your game locations manually

### Partial Recovery

If some games work but others don't:

1. **Identify Working vs. Broken Games**
2. **Manually Fix Individual Manifests**
3. **Use Epic Games Launcher's Library Management**

Remember: The worst-case scenario is re-downloading games, but this script is designed to prevent that!
