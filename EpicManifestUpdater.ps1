Add-Type -AssemblyName System.Windows.Forms

# Function to close Epic Games Launcher
function Close-EpicGames {
    $processes = @("EpicGamesLauncher", "EpicWebHelper")
    foreach ($proc in $processes) {
        Get-Process -Name $proc -ErrorAction SilentlyContinue | Stop-Process -Force
    }
    Start-Sleep -Seconds 2
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
Write-ColorOutput Yellow "Epic Games Manifest Updater"
Write-ColorOutput Yellow "=========================="
Write-ColorOutput Green "`nBefore running this script:"
Write-ColorOutput White "1. Make sure you've already moved your games to the new location"
Write-ColorOutput White "2. The new location should contain your game folders"
Pause

Write-ColorOutput Cyan "`nClosing Epic Games Launcher..."
Close-EpicGames

Write-ColorOutput Cyan "`nSelect your new Epic Games folder in the popup window..."
$newLocation = Select-Folder

if ($null -eq $newLocation) {
    Write-ColorOutput Red "No folder selected. Exiting..."
    Pause
    exit
}

$manifestsDir = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"

if (-not (Test-Path $manifestsDir)) {
    Write-ColorOutput Red "Error: Cannot find Epic Games manifests directory!"
    Write-ColorOutput Red "Make sure Epic Games Launcher is installed."
    Pause
    exit
}

Write-ColorOutput Cyan "`nUpdating manifest files..."
$updateCount = 0

Get-ChildItem $manifestsDir -Filter "*.item" | ForEach-Object {
    $content = Get-Content $_.FullName | ConvertFrom-Json
    $oldPath = $content.InstallLocation
    
    if ($oldPath -and $oldPath -ne $newLocation) {
        $gameName = Split-Path $oldPath -Leaf
        $newPath = Join-Path $newLocation $gameName
        
        if (Test-Path $newPath) {
            $content.InstallLocation = $newPath
            $content.ManifestLocation = "$newPath/.egstore"
            $content.StagingLocation = "$newPath/.egstore/bps"
            $content | ConvertTo-Json -Depth 10 | Set-Content $_.FullName
            Write-ColorOutput Green "Updated: $gameName"
            $updateCount++
        }
    }
}

Write-ColorOutput Yellow "`nComplete! Updated $updateCount manifest(s)"
Write-ColorOutput Green "You can now start Epic Games Launcher"
Pause
