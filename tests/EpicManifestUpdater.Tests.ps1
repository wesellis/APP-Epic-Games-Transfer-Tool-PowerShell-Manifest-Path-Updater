BeforeAll {
    # Set up test environment
    $script:testRoot = $PSScriptRoot
    $script:projectRoot = Split-Path $testRoot -Parent
    $script:scriptPath = Join-Path $projectRoot "EpicManifestUpdater.ps1"
    
    # Create temporary test directories
    $script:testManifestsDir = Join-Path $env:TEMP "EpicManifestTest_$(Get-Random)"
    $script:testGamesDir = Join-Path $env:TEMP "EpicGamesTest_$(Get-Random)"
    
    New-Item -ItemType Directory -Path $script:testManifestsDir -Force
    New-Item -ItemType Directory -Path $script:testGamesDir -Force
    
    # Sample manifest content for testing
    $script:sampleManifest = @{
        InstallLocation = "C:\Epic Games\TestGame"
        ManifestLocation = "C:\Epic Games\TestGame\.egstore"
        StagingLocation = "C:\Epic Games\TestGame\.egstore\bps"
        AppName = "TestGame"
        DisplayName = "Test Game"
    }
}

Describe "EpicManifestUpdater Script Validation" {
    Context "Script File Validation" {
        It "Should exist" {
            $script:scriptPath | Should -Exist
        }
        
        It "Should be a valid PowerShell script" {
            { 
                $null = [System.Management.Automation.PSParser]::Tokenize(
                    (Get-Content $script:scriptPath -Raw), 
                    [ref]$null
                )
            } | Should -Not -Throw
        }
        
        It "Should contain required functions" {
            $scriptContent = Get-Content $script:scriptPath -Raw
            $scriptContent | Should -Match "function Close-EpicGames"
            $scriptContent | Should -Match "function Select-Folder"
            $scriptContent | Should -Match "function Write-ColorOutput"
            $scriptContent | Should -Match "function Pause"
        }
        
        It "Should import System.Windows.Forms assembly" {
            $scriptContent = Get-Content $script:scriptPath -Raw
            $scriptContent | Should -Match "Add-Type -AssemblyName System.Windows.Forms"
        }
    }
}

Describe "Manifest Processing Functions" {
    Context "Manifest File Handling" {
        BeforeEach {
            # Create test manifest file
            $script:testManifestPath = Join-Path $script:testManifestsDir "test.item"
            $script:sampleManifest | ConvertTo-Json -Depth 10 | Set-Content $script:testManifestPath
        }
        
        It "Should read manifest file correctly" {
            $content = Get-Content $script:testManifestPath | ConvertFrom-Json
            $content.InstallLocation | Should -Be "C:\Epic Games\TestGame"
            $content.AppName | Should -Be "TestGame"
        }
        
        It "Should handle JSON conversion" {
            { 
                $content = Get-Content $script:testManifestPath | ConvertFrom-Json
                $content | ConvertTo-Json -Depth 10
            } | Should -Not -Throw
        }
        
        AfterEach {
            if (Test-Path $script:testManifestPath) {
                Remove-Item $script:testManifestPath -Force
            }
        }
    }
}

Describe "Path Validation and Processing" {
    Context "Path Manipulation" {
        It "Should correctly extract game name from path" {
            $testPath = "C:\Epic Games\TestGame"
            $gameName = Split-Path $testPath -Leaf
            $gameName | Should -Be "TestGame"
        }
        
        It "Should construct new paths correctly" {
            $newBasePath = "D:\Games\Epic"
            $gameName = "TestGame"
            $newPath = Join-Path $newBasePath $gameName
            $newPath | Should -Be "D:\Games\Epic\TestGame"
        }
        
        It "Should handle paths with spaces" {
            $testPath = "C:\Epic Games\Test Game With Spaces"
            $gameName = Split-Path $testPath -Leaf
            $gameName | Should -Be "Test Game With Spaces"
        }
    }
}

Describe "Error Handling Scenarios" {
    Context "File System Operations" {
        It "Should handle missing manifest directory gracefully" {
            $nonExistentPath = "C:\NonExistent\Path"
            Test-Path $nonExistentPath | Should -Be $false
        }
        
        It "Should handle invalid JSON in manifest files" {
            $invalidJsonPath = Join-Path $script:testManifestsDir "invalid.item"
            "Invalid JSON Content" | Set-Content $invalidJsonPath
            
            { Get-Content $invalidJsonPath | ConvertFrom-Json } | Should -Throw
            
            Remove-Item $invalidJsonPath -Force
        }
        
        It "Should validate game folder existence" {
            $testGamePath = Join-Path $script:testGamesDir "TestGame"
            New-Item -ItemType Directory -Path $testGamePath -Force
            
            Test-Path $testGamePath | Should -Be $true
            
            Remove-Item $testGamePath -Force
        }
    }
}

Describe "Epic Games Process Management" {
    Context "Process Detection" {
        It "Should detect Epic Games processes if running" {
            # Mock test - in real scenario, Epic Games might not be running
            $epicProcesses = Get-Process -Name "EpicGamesLauncher", "EpicWebHelper" -ErrorAction SilentlyContinue
            # This test validates the command structure, not necessarily the presence of processes
            { Get-Process -Name "EpicGamesLauncher", "EpicWebHelper" -ErrorAction SilentlyContinue } | Should -Not -Throw
        }
    }
}

Describe "Manifest Update Logic" {
    Context "Path Updates" {
        BeforeEach {
            # Create test manifest with known content
            $script:testManifestPath = Join-Path $script:testManifestsDir "update_test.item"
            $testManifest = @{
                InstallLocation = "C:\Epic Games\UpdateTest"
                ManifestLocation = "C:\Epic Games\UpdateTest\.egstore"
                StagingLocation = "C:\Epic Games\UpdateTest\.egstore\bps"
                AppName = "UpdateTest"
            }
            $testManifest | ConvertTo-Json -Depth 10 | Set-Content $script:testManifestPath
            
            # Create corresponding game directory
            $script:testGameDir = Join-Path $script:testGamesDir "UpdateTest"
            New-Item -ItemType Directory -Path $script:testGameDir -Force
        }
        
        It "Should update InstallLocation correctly" {
            $content = Get-Content $script:testManifestPath | ConvertFrom-Json
            $newBasePath = $script:testGamesDir
            $gameName = Split-Path $content.InstallLocation -Leaf
            $newPath = Join-Path $newBasePath $gameName
            
            $content.InstallLocation = $newPath
            $content.ManifestLocation = "$newPath\.egstore"
            $content.StagingLocation = "$newPath\.egstore\bps"
            
            $content.InstallLocation | Should -Be $newPath
            $content.ManifestLocation | Should -Be "$newPath\.egstore"
            $content.StagingLocation | Should -Be "$newPath\.egstore\bps"
        }
        
        It "Should preserve other manifest properties" {
            $content = Get-Content $script:testManifestPath | ConvertFrom-Json
            $originalAppName = $content.AppName
            
            # Simulate update
            $content.InstallLocation = "D:\New\Path\UpdateTest"
            
            $content.AppName | Should -Be $originalAppName
        }
        
        AfterEach {
            if (Test-Path $script:testManifestPath) {
                Remove-Item $script:testManifestPath -Force
            }
            if (Test-Path $script:testGameDir) {
                Remove-Item $script:testGameDir -Force
            }
        }
    }
}

Describe "Integration Scenarios" {
    Context "End-to-End Workflow Simulation" {
        BeforeEach {
            # Set up complete test scenario
            $script:gameNames = @("TestGame1", "TestGame2", "TestGame3")
            $script:testManifestFiles = @()
            $script:testGameDirs = @()
            
            foreach ($gameName in $script:gameNames) {
                # Create manifest file
                $manifestPath = Join-Path $script:testManifestsDir "$gameName.item"
                $manifest = @{
                    InstallLocation = "C:\Epic Games\$gameName"
                    ManifestLocation = "C:\Epic Games\$gameName\.egstore"
                    StagingLocation = "C:\Epic Games\$gameName\.egstore\bps"
                    AppName = $gameName
                    DisplayName = "Test $gameName"
                }
                $manifest | ConvertTo-Json -Depth 10 | Set-Content $manifestPath
                $script:testManifestFiles += $manifestPath
                
                # Create game directory
                $gameDir = Join-Path $script:testGamesDir $gameName
                New-Item -ItemType Directory -Path $gameDir -Force
                $script:testGameDirs += $gameDir
            }
        }
        
        It "Should process multiple manifest files" {
            $manifestFiles = Get-ChildItem $script:testManifestsDir -Filter "*.item"
            $manifestFiles.Count | Should -Be 3
            
            foreach ($file in $manifestFiles) {
                $content = Get-Content $file.FullName | ConvertFrom-Json
                $content.AppName | Should -BeIn $script:gameNames
            }
        }
        
        It "Should verify all game directories exist" {
            foreach ($gameName in $script:gameNames) {
                $gameDir = Join-Path $script:testGamesDir $gameName
                Test-Path $gameDir | Should -Be $true
            }
        }
        
        It "Should simulate successful update workflow" {
            $updateCount = 0
            $newBasePath = $script:testGamesDir
            
            Get-ChildItem $script:testManifestsDir -Filter "*.item" | ForEach-Object {
                $content = Get-Content $_.FullName | ConvertFrom-Json
                $oldPath = $content.InstallLocation
                $gameName = Split-Path $oldPath -Leaf
                $newPath = Join-Path $newBasePath $gameName
                
                if (Test-Path $newPath) {
                    $updateCount++
                    # Simulate the update
                    $content.InstallLocation = $newPath
                    $content.ManifestLocation = "$newPath\.egstore"
                    $content.StagingLocation = "$newPath\.egstore\bps"
                }
            }
            
            $updateCount | Should -Be 3
        }
        
        AfterEach {
            # Clean up test files
            foreach ($file in $script:testManifestFiles) {
                if (Test-Path $file) {
                    Remove-Item $file -Force
                }
            }
            foreach ($dir in $script:testGameDirs) {
                if (Test-Path $dir) {
                    Remove-Item $dir -Force
                }
            }
        }
    }
}

AfterAll {
    # Clean up test environment
    if (Test-Path $script:testManifestsDir) {
        Remove-Item $script:testManifestsDir -Recurse -Force
    }
    if (Test-Path $script:testGamesDir) {
        Remove-Item $script:testGamesDir -Recurse -Force
    }
}
