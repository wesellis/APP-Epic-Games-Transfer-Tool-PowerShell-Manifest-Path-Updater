Epic Games Manager Pro v1.2.0
============================

Thank you for purchasing Epic Games Manager Pro!

QUICK START
-----------
1. Make sure Python 3.8+ is installed (or use the PowerShell version)
2. Place this folder anywhere on your computer
3. Run the tool:
   - Python: python epic_manager.py
   - PowerShell: Right-click EpicManifestUpdater.ps1 → Run with PowerShell

WHAT THIS TOOL DOES
-------------------
Epic Games Manager fixes your Epic Games library when you've moved games to a new location. Instead of re-downloading hundreds of gigabytes, this tool updates Epic's manifest files to point to your games' new location.

PRO VERSION FEATURES
--------------------
✓ Unlimited game management (Free version: 5 games)
✓ Batch operations - update all games at once
✓ Automatic backup before any changes
✓ Command line automation support
✓ Priority email support
✓ Lifetime updates

COMMON COMMANDS
---------------
# Scan your Epic Games library
python epic_manager.py scan

# Repair a specific game
python epic_manager.py repair --game "Fortnite"

# Repair all games (Pro only)
python epic_manager.py repair

# Backup all game saves
python epic_manager.py backup --all

# Activate your license
python epic_manager.py license --activate YOUR-LICENSE-KEY

TYPICAL USE CASE
----------------
1. You moved Epic Games from C:\Epic Games to D:\Games\Epic
2. Epic Launcher can't find your games
3. Run: python epic_manager.py scan
4. Run: python epic_manager.py repair
5. Start Epic Launcher - all games are back!

TROUBLESHOOTING
---------------
If the script doesn't work:
1. Make sure Epic Games Launcher is closed
2. Run as Administrator if needed
3. Check that your games are actually in the new location
4. The manifest directory is usually:
   C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests

SUPPORT
-------
Email: support@epicgamesmanager.com
Documentation: https://github.com/wesellis/epic-games-manager
Response time: Within 24 hours for Pro users

LICENSE
-------
This software is licensed to you under the terms provided at purchase.
Do not distribute or share your license key.

Thank you for supporting independent software development!

- The Epic Games Manager Team