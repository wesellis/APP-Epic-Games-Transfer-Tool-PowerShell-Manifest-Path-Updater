# Epic Games Manifest Updater Examples

This directory contains usage examples and scenarios for the Epic Games Manifest Updater.

## Basic Usage Examples

### Example 1: Moving from C: to D: Drive

**Scenario:** You've moved your Epic Games folder from `C:\Epic Games\` to `D:\Games\Epic\`

**Steps:**
1. Move the entire Epic Games folder to the new location
2. Run the script
3. Select `D:\Games\Epic\` when prompted

**Before:**
```
C:\Epic Games\
├── Fortnite\
├── RocketLeague\
└── UnrealEngine\
```

**After:**
```
D:\Games\Epic\
├── Fortnite\
├── RocketLeague\
└── UnrealEngine\
```

### Example 2: Reorganizing Game Library

**Scenario:** Organizing games into a structured folder hierarchy

**Before:**
```
C:\Games\
├── Fortnite\
├── RocketLeague\
├── SteamGames\
└── OtherGames\
```

**After:**
```
C:\Games\
├── Epic\
│   ├── Fortnite\
│   └── RocketLeague\
├── Steam\
└── Other\
```

**Script Usage:** Select `C:\Games\Epic\` as the new location

### Example 3: External Drive Setup

**Scenario:** Moving games to external drive for portability

**From:** `C:\Epic Games\`
**To:** `E:\PortableGames\Epic\`

**Considerations:**
- Ensure external drive has sufficient space
- Verify drive letter consistency
- Consider performance impact of external storage

## Advanced Scenarios

### Scenario A: Network Drive

**Setup:** Moving games to network storage

**Path Example:** `\\NetworkServer\Games\Epic\`

**Special Considerations:**
- Network permissions required
- Potential performance impact
- Ensure network drive is always available

### Scenario B: Multiple Users

**Challenge:** Different users with separate game libraries

**Solution Approach:**
```
D:\Games\
├── User1\
│   └── Epic\
│       ├── Fortnite\
│       └── RocketLeague\
└── User2\
    └── Epic\
        ├── Genshin\
        └── UnrealEngine\
```

**Process:**
1. Each user runs the script separately
2. Select their respective Epic folder
3. Manifests update per-user basis

### Scenario C: Partial Game Migration

**Situation:** Moving only some games to a new location

**Current Limitation:** Script moves all detected games

**Workaround:**
1. Temporarily move unwanted games out of the source folder
2. Run the script for remaining games
3. Move other games back and run script again if needed

## PowerShell Integration Examples

### Example 1: Automated Backup Before Running

```powershell
# Create backup before running the updater
$backupPath = "$env:USERPROFILE\Desktop\EpicManifestBackup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
$manifestsPath = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"

if (Test-Path $manifestsPath) {
    Copy-Item $manifestsPath $backupPath -Recurse
    Write-Host "Backup created at: $backupPath" -ForegroundColor Green
    
    # Now run the main script
    .\EpicManifestUpdater.ps1
} else {
    Write-Host "Epic Games manifests directory not found!" -ForegroundColor Red
}
```

### Example 2: Verification Script

```powershell
# Verify games after running the updater
$manifestsPath = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"

Get-ChildItem $manifestsPath -Filter "*.item" | ForEach-Object {
    $content = Get-Content $_.FullName | ConvertFrom-Json
    $gamePath = $content.InstallLocation
    $gameName = Split-Path $gamePath -Leaf
    
    if (Test-Path $gamePath) {
        Write-Host "✅ $gameName - Found at $gamePath" -ForegroundColor Green
    } else {
        Write-Host "❌ $gameName - Missing at $gamePath" -ForegroundColor Red
    }
}
```

### Example 3: Batch Processing for Multiple Installations

```powershell
# Handle multiple Epic Games installations (if you have multiple)
$installations = @(
    "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests",
    "D:\EpicGames\Data\Manifests"  # Example alternative location
)

foreach ($installPath in $installations) {
    if (Test-Path $installPath) {
        Write-Host "Processing installation at: $installPath" -ForegroundColor Blue
        
        # Set the manifest directory for this installation
        $env:EPIC_MANIFESTS_PATH = $installPath
        
        # Run your custom version of the script here
        # Note: You'd need to modify the main script to use this environment variable
    }
}
```

## Command Line Integration

### Example 1: Silent Operation (Modified Script)

If you modify the script to accept parameters:

```powershell
# Modified script usage with parameters
.\EpicManifestUpdater.ps1 -NewPath "D:\Games\Epic" -Silent
```

### Example 2: Scheduled Task Integration

```powershell
# Create a scheduled task to run the updater
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\Scripts\EpicManifestUpdater.ps1"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(5)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive

Register-ScheduledTask -TaskName "EpicManifestUpdater" -Action $action -Trigger $trigger -Principal $principal
```

## Error Handling Examples

### Example 1: Robust Execution

```powershell
try {
    # Run the manifest updater
    .\EpicManifestUpdater.ps1
    
    Write-Host "Script completed successfully!" -ForegroundColor Green
    
    # Verify results
    Start-Process "com.epicgames.launcher://library"
    
} catch {
    Write-Host "Error occurred: $($_.Exception.Message)" -ForegroundColor Red
    
    # Restore from backup if available
    $backupPath = "$env:USERPROFILE\Desktop\EpicManifestBackup"
    if (Test-Path $backupPath) {
        Write-Host "Restoring from backup..." -ForegroundColor Yellow
        Copy-Item "$backupPath\*" "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests" -Force
    }
}
```

### Example 2: Pre-flight Checks

```powershell
# Comprehensive pre-flight checks
function Test-Prerequisites {
    $checks = @()
    
    # Check if Epic Games Launcher is installed
    $epicPath = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"
    if (Test-Path $epicPath) {
        $checks += "✅ Epic Games Launcher found"
    } else {
        $checks += "❌ Epic Games Launcher not found"
        return $false
    }
    
    # Check PowerShell version
    if ($PSVersionTable.PSVersion.Major -ge 5) {
        $checks += "✅ PowerShell version OK ($($PSVersionTable.PSVersion))"
    } else {
        $checks += "❌ PowerShell version too old"
        return $false
    }
    
    # Check for running Epic processes
    $epicProcesses = Get-Process -Name "EpicGamesLauncher", "EpicWebHelper" -ErrorAction SilentlyContinue
    if ($epicProcesses) {
        $checks += "⚠️ Epic Games Launcher is running - will be closed"
    } else {
        $checks += "✅ Epic Games Launcher not running"
    }
    
    # Display results
    $checks | ForEach-Object { Write-Host $_ }
    return $true
}

# Run pre-flight checks before executing
if (Test-Prerequisites) {
    Write-Host "`nPre-flight checks passed. Running updater..." -ForegroundColor Green
    .\EpicManifestUpdater.ps1
} else {
    Write-Host "`nPre-flight checks failed. Please resolve issues before running." -ForegroundColor Red
}
```

## Integration with Other Tools

### Example 1: Steam Library Manager Integration

```powershell
# Example workflow for users managing multiple game libraries
Write-Host "Game Library Migration Workflow" -ForegroundColor Blue

# 1. Handle Steam games
Write-Host "1. Moving Steam games..." -ForegroundColor Yellow
# Use Steam Library Manager or similar tool

# 2. Handle Epic Games
Write-Host "2. Moving Epic Games..." -ForegroundColor Yellow
.\EpicManifestUpdater.ps1

# 3. Handle other launchers
Write-Host "3. Other game launchers..." -ForegroundColor Yellow
# Handle GOG, Origin, etc.

Write-Host "Game library migration complete!" -ForegroundColor Green
```

### Example 2: Backup Software Integration

```powershell
# Integration with backup software workflow
$backupScript = {
    # Create timestamped backup
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $backupDir = "C:\GameBackups\Epic_$timestamp"
    
    # Backup manifests
    Copy-Item "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests" $backupDir -Recurse
    
    # Backup game folders (if desired)
    # Copy-Item "C:\Epic Games" "$backupDir\Games" -Recurse
    
    Write-Host "Backup completed: $backupDir" -ForegroundColor Green
}

# Run backup, then updater, then verification
& $backupScript
.\EpicManifestUpdater.ps1
# Run verification script
```

## Testing Scenarios

### Test Case 1: Dry Run Mode

```powershell
# Mock version for testing (you'd modify the main script)
function Test-EpicManifestUpdater {
    param(
        [string]$NewPath,
        [switch]$WhatIf
    )
    
    $manifestsDir = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"
    
    if ($WhatIf) {
        Write-Host "What if: Would update manifests to point to $NewPath" -ForegroundColor Yellow
        
        Get-ChildItem $manifestsDir -Filter "*.item" | ForEach-Object {
            $content = Get-Content $_.FullName | ConvertFrom-Json
            $oldPath = $content.InstallLocation
            $gameName = Split-Path $oldPath -Leaf
            $newGamePath = Join-Path $NewPath $gameName
            
            Write-Host "What if: Would update $gameName from $oldPath to $newGamePath" -ForegroundColor Cyan
        }
    } else {
        # Run actual update
        Write-Host "Performing actual update..." -ForegroundColor Green
    }
}

# Test usage
Test-EpicManifestUpdater -NewPath "D:\Games\Epic" -WhatIf
```

### Test Case 2: Validation Suite

```powershell
# Comprehensive validation after running the updater
function Test-UpdateResults {
    param([string]$ExpectedBasePath)
    
    $manifestsPath = "C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests"
    $results = @{
        'TotalManifests' = 0
        'ValidUpdates' = 0
        'InvalidUpdates' = 0
        'MissingGames' = 0
        'Details' = @()
    }
    
    Get-ChildItem $manifestsPath -Filter "*.item" | ForEach-Object {
        $results.TotalManifests++
        $content = Get-Content $_.FullName | ConvertFrom-Json
        $gamePath = $content.InstallLocation
        $gameName = Split-Path $gamePath -Leaf
        
        $testResult = @{
            'Game' = $gameName
            'ManifestFile' = $_.Name
            'ExpectedPath' = Join-Path $ExpectedBasePath $gameName
            'ActualPath' = $gamePath
            'PathCorrect' = $false
            'GameExists' = $false
        }
        
        # Check if path was updated correctly
        if ($gamePath -like "$ExpectedBasePath*") {
            $testResult.PathCorrect = $true
            $results.ValidUpdates++
        } else {
            $results.InvalidUpdates++
        }
        
        # Check if game actually exists
        if (Test-Path $gamePath) {
            $testResult.GameExists = $true
        } else {
            $results.MissingGames++
        }
        
        $results.Details += $testResult
    }
    
    # Display results
    Write-Host "`nValidation Results:" -ForegroundColor Blue
    Write-Host "Total Manifests: $($results.TotalManifests)" -ForegroundColor White
    Write-Host "Valid Updates: $($results.ValidUpdates)" -ForegroundColor Green
    Write-Host "Invalid Updates: $($results.InvalidUpdates)" -ForegroundColor Red
    Write-Host "Missing Games: $($results.MissingGames)" -ForegroundColor Yellow
    
    if ($results.InvalidUpdates -gt 0 -or $results.MissingGames -gt 0) {
        Write-Host "`nDetailed Issues:" -ForegroundColor Yellow
        $results.Details | Where-Object { -not $_.PathCorrect -or -not $_.GameExists } | 
            ForEach-Object {
                Write-Host "Game: $($_.Game)" -ForegroundColor White
                Write-Host "  Expected: $($_.ExpectedPath)" -ForegroundColor Gray
                Write-Host "  Actual: $($_.ActualPath)" -ForegroundColor Gray
                Write-Host "  Path OK: $($_.PathCorrect)" -ForegroundColor $(if($_.PathCorrect){'Green'}else{'Red'})
                Write-Host "  Exists: $($_.GameExists)" -ForegroundColor $(if($_.GameExists){'Green'}else{'Red'})
                Write-Host ""
            }
    }
    
    return $results
}

# Usage example
$results = Test-UpdateResults -ExpectedBasePath "D:\Games\Epic"
```

These examples demonstrate various ways to use and extend the Epic Games Manifest Updater for different scenarios and requirements.
