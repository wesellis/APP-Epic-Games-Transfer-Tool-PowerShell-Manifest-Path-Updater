Add-Type -AssemblyName System.Windows.Forms

# Initialize logging
$logPath = Join-Path $PSScriptRoot "EpicManifestUpdater.log"
$backupDir = Join-Path $PSScriptRoot "Backups"

# Logging function
function Write-Log {
    param($Message, $Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "[$timestamp] [$Level] $Message"
    Add-Content -Path $logPath -Value $logEntry

    switch ($Level) {
        "ERROR" { Write-ColorOutput Red $Message }
        "SUCCESS" { Write-ColorOutput Green $Message }
        "WARNING" { Write-ColorOutput Yellow $Message }
        default { Write-ColorOutput White $Message }
    }
}

# Function to close Epic Games Launcher
function Close-EpicGames {
    Write-Log "Attempting to close Epic Games Launcher..." "INFO"
    $processes = @("EpicGamesLauncher", "EpicWebHelper")
    $closed = $false

    foreach ($proc in $processes) {
        $process = Get-Process -Name $proc -ErrorAction SilentlyContinue
        if ($process) {
            Stop-Process -Name $proc -Force
            $closed = $true
            Write-Log "Closed $proc" "INFO"
        }
    }

    if ($closed) {
        Start-Sleep -Seconds 2
    } else {
        Write-Log "Epic Games Launcher was not running" "INFO"
    }
}

# Function to create backup
function Backup-Manifests {
    param($ManifestsDir)

    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupPath = Join-Path $backupDir "Backup_$timestamp"

    Write-Log "Creating backup at: $backupPath" "INFO"

    try {
        if (-not (Test-Path $backupDir)) {
            New-Item -ItemType Directory -Path $backupDir | Out-Null
        }

        New-Item -ItemType Directory -Path $backupPath | Out-Null
        Copy-Item -Path "$ManifestsDir\*.item" -Destination $backupPath -ErrorAction Stop

        $backupCount = (Get-ChildItem $backupPath -Filter "*.item").Count
        Write-Log "Backed up $backupCount manifest file(s)" "SUCCESS"
        return $backupPath
    }
    catch {
        Write-Log "Failed to create backup: $_" "ERROR"
        return $null
    }
}

# GUI folder selector
function Select-Folder {
    $folderBrowser = New-Object System.Windows.Forms.FolderBrowserDialog
    $folderBrowser.Description = "Select the folder where your Epic Games are now located"
    $folderBrowser.ShowNewFolderButton = $false

    if ($folderBrowser.ShowDialog() -eq "OK") {
        return $folderBrowser.SelectedPath
    }
    return $null
}

# Color output function
function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

# Pause function
function Pause {
    Write-ColorOutput Green "Press Enter to continue..."
    Read-Host | Out-Null
}

Clear-Host
Write-ColorOutput Yellow "Epic Games Manifest Updater v2.0"
Write-ColorOutput Yellow "================================="
Write-Log "Script started" "INFO"

Write-ColorOutput Green "`nBefore running this script:"
Write-ColorOutput White "1. Make sure you've already moved your games to the new location"
Write-ColorOutput White "2. The new location should contain your game folders"
Write-ColorOutput White "3. A backup will be created automatically before any changes"
Pause

Write-ColorOutput Cyan "`nClosing Epic Games Launcher..."
Close-EpicGames

Write-ColorOutput Cyan "`nSelect your new Epic Games folder in the popup window..."
$newLocation = Select-Folder

if ($null -eq $newLocation) {
    Write-Log "No folder selected. Exiting." "ERROR"
    Pause
    exit
}

Write-Log "Selected new location: $newLocation" "INFO"

# Validate new location exists
if (-not (Test-Path $newLocation)) {
    Write-Log "Selected folder does not exist: $newLocation" "ERROR"
    Pause
    exit
}

$manifestsDir = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"

if (-not (Test-Path $manifestsDir)) {
    Write-Log "Cannot find Epic Games manifests directory: $manifestsDir" "ERROR"
    Write-Log "Make sure Epic Games Launcher is installed." "ERROR"
    Pause
    exit
}

# Create backup before making any changes
Write-ColorOutput Cyan "`nCreating backup of manifest files..."
$backupPath = Backup-Manifests -ManifestsDir $manifestsDir

if ($null -eq $backupPath) {
    Write-ColorOutput Yellow "`nWARNING: Backup failed! Do you want to continue anyway?"
    $continue = Read-Host "Type 'yes' to continue without backup"
    if ($continue -ne "yes") {
        Write-Log "User canceled after backup failure" "INFO"
        Pause
        exit
    }
}

Write-ColorOutput Cyan "`nUpdating manifest files..."
$updateCount = 0
$skipCount = 0
$errorCount = 0

Get-ChildItem $manifestsDir -Filter "*.item" | ForEach-Object {
    try {
        $content = Get-Content $_.FullName | ConvertFrom-Json
        $oldPath = $content.InstallLocation

        if ($oldPath -and $oldPath -ne $newLocation) {
            $gameName = Split-Path $oldPath -Leaf
            $newPath = Join-Path $newLocation $gameName

            # Verify game folder exists
            if (Test-Path $newPath) {
                # Verify .egstore folder exists
                $egstorePath = Join-Path $newPath ".egstore"

                if (-not (Test-Path $egstorePath)) {
                    Write-Log "WARNING: $gameName is missing .egstore folder - game may not work!" "WARNING"
                }

                # Update paths
                $content.InstallLocation = $newPath
                $content.ManifestLocation = "$newPath/.egstore"
                $content.StagingLocation = "$newPath/.egstore/bps"

                # Save updated manifest
                $content | ConvertTo-Json -Depth 10 | Set-Content $_.FullName
                Write-Log "Updated: $gameName -> $newPath" "SUCCESS"
                $updateCount++
            }
            else {
                Write-Log "Skipped: $gameName (folder not found at $newPath)" "WARNING"
                $skipCount++
            }
        }
    }
    catch {
        Write-Log "Error processing $($_.Name): $_" "ERROR"
        $errorCount++
    }
}

Write-ColorOutput Yellow "`n================================="
Write-ColorOutput Yellow "Summary:"
Write-Log "Updated: $updateCount manifest(s)" "SUCCESS"

if ($skipCount -gt 0) {
    Write-Log "Skipped: $skipCount game(s) (not found in new location)" "WARNING"
}

if ($errorCount -gt 0) {
    Write-Log "Errors: $errorCount manifest(s) failed to update" "ERROR"
}

if ($backupPath) {
    Write-Log "Backup saved to: $backupPath" "INFO"
}

Write-Log "Log saved to: $logPath" "INFO"

Write-ColorOutput Green "`nYou can now start Epic Games Launcher!"
Write-Log "Script completed" "SUCCESS"
Pause
