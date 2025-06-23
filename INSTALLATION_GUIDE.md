# 🎮 Epic Games Manager - Installation Guide

## Overview

Epic Games Manager is a powerful tool for managing your Epic Games Store library, tracking free games, monitoring achievements, and optimizing downloads. Available in both Free and Pro versions.

---

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11 (64-bit)
- **Epic Games Launcher**: Must be installed
- **Storage**: 100MB for application
- **RAM**: 4GB minimum (8GB recommended)
- **Internet**: Required for free game tracking and updates

### Epic Games Store Setup
1. Ensure Epic Games Launcher is installed
2. Sign in to your Epic Games account
3. Have at least one game installed (for library scanning)

---

## 🚀 Quick Installation

### Option 1: Standalone EXE (Recommended)

1. **Download the installer**
   - Visit [Releases page](https://github.com/wesellis/epic-games-manager/releases)
   - Download `EpicGamesManager_Setup.exe` or `EpicGamesManager_Portable.zip`

2. **Run the installer**
   - Double-click `EpicGamesManager_Setup.exe`
   - Follow the installation wizard
   - Choose installation directory (default: `C:\Program Files\Epic Games Manager`)

3. **First launch**
   - Start from desktop shortcut or Start Menu
   - Allow Windows Defender if prompted
   - Complete initial setup wizard

### Option 2: Portable Version

1. **Download portable ZIP**
   - Get `EpicGamesManager_Portable.zip` from releases

2. **Extract to desired location**
   ```
   Recommended locations:
   - C:\Tools\EpicGamesManager
   - D:\Programs\EpicGamesManager
   - Desktop (for easy access)
   ```

3. **Run the application**
   - Navigate to extracted folder
   - Double-click `EpicGamesManager.exe`
   - Create desktop shortcut (optional)

### Option 3: Python Source (Developers)

1. **Clone the repository**
   ```bash
   git clone https://github.com/wesellis/epic-games-manager.git
   cd epic-games-manager
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # For Pro features:
   pip install -r requirements_pro.txt
   ```

4. **Run the application**
   ```bash
   python epic_manifest_updater.py
   # Or for Pro version:
   python epic_manifest_updater_pro.py
   ```

---

## ⚙️ Configuration

### First-Time Setup

1. **Epic Games Location**
   - The app will auto-detect your Epic Games installation
   - If not found, manually browse to Epic Games folder
   - Typical location: `C:\Program Files\Epic Games`

2. **Library Scan**
   - Click "Scan Library" to import your games
   - This may take 1-5 minutes depending on library size
   - Progress will be shown in the status bar

3. **Preferences**
   - Go to Settings → Preferences
   - Configure:
     - Download location
     - Bandwidth limits
     - Notification preferences
     - Auto-start options

### Free Game Tracking Setup

1. **Enable notifications**
   - Settings → Free Games → Enable Notifications
   - Choose notification method:
     - System tray notifications
     - Email alerts (Pro)
     - Discord webhook (Pro)

2. **Auto-claim setup (Pro)**
   - Settings → Free Games → Auto-Claim
   - Enter Epic Games credentials (encrypted storage)
   - Set claim schedule (recommended: Thursday 12 PM)

---

## 🎯 Feature Activation

### Free Version Features
All features are active immediately:
- Library management
- Basic download queue
- Manual free game checking
- Achievement viewing
- Game launch shortcuts

### Pro Version Activation

1. **Purchase license**
   - Buy from [Gumroad](https://gumroad.com/l/epic-games-manager-pro)
   - Or in-app: Help → Upgrade to Pro

2. **Enter license key**
   - Click "Activate Pro" in main window
   - Paste your license key
   - Click "Activate"

3. **Pro features unlocked**
   - ✅ Unlimited download queue
   - ✅ Auto-claim free games
   - ✅ Advanced achievement tracking
   - ✅ Cloud save backup
   - ✅ Priority support
   - ✅ Future updates

---

## 🔧 Advanced Configuration

### Command Line Options
```bash
EpicGamesManager.exe [options]

Options:
  --minimize        Start minimized to tray
  --scan            Auto-scan library on start
  --portable        Use portable mode (settings in app folder)
  --debug           Enable debug logging
  --reset           Reset all settings to default
```

### Configuration Files

**Settings location**:
- Installed: `%APPDATA%\EpicGamesManager\config.json`
- Portable: `.\config\config.json`

**Example config.json**:
```json
{
  "epic_path": "C:\\Program Files\\Epic Games",
  "download_path": "D:\\Games\\Downloads",
  "auto_start": true,
  "minimize_to_tray": true,
  "check_free_games": true,
  "notification_sound": true,
  "bandwidth_limit": 0,
  "theme": "dark"
}
```

### Registry Entries (Installed Version)
```
HKEY_CURRENT_USER\Software\EpicGamesManager
├── InstallPath
├── Version
├── LicenseKey (encrypted)
└── LastUpdateCheck
```

---

## 🎨 Customization

### Themes
1. Go to Settings → Appearance
2. Choose from:
   - Dark (default)
   - Light
   - Epic (purple theme)
   - Custom (Pro)

### Layout Options
- Compact view
- Detailed view
- Grid view
- List view

### Custom Categories
1. Right-click any game
2. Select "Add to Category"
3. Create custom categories:
   - Favorites
   - Currently Playing
   - Completed
   - Backlog

---

## 🔄 Updates

### Automatic Updates
- Free version: Manual check via Help → Check for Updates
- Pro version: Automatic update notifications

### Manual Update Process
1. Download latest version from GitHub
2. Close Epic Games Manager
3. Run new installer (settings preserved)
4. Restart application

---

## 🛠️ Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Epic Games not detected | Manually set path in Settings → Epic Games Location |
| Games not showing | Click "Rescan Library" or check Epic Games is running |
| Slow performance | Disable animations in Settings → Performance |
| License key invalid | Ensure no extra spaces, contact support |
| Free games not updating | Check internet connection, firewall settings |

### Log Files
- Location: `%APPDATA%\EpicGamesManager\logs\`
- Enable debug mode for detailed logging
- Include latest log when reporting issues

### Reset Application
1. Close Epic Games Manager
2. Run with `--reset` flag
3. Or delete config folder manually

---

## 🔐 Security & Privacy

### Data Storage
- All data stored locally
- Passwords encrypted using Windows DPAPI
- No telemetry or tracking
- Open source for transparency

### Firewall Configuration
Allow these for full functionality:
- `EpicGamesManager.exe` - Main application
- Port 443 (HTTPS) - API access
- Epic Games Store API endpoints

---

## 🆘 Support

### Free Version
- GitHub Issues: [Report bugs](https://github.com/wesellis/epic-games-manager/issues)
- Community Discord: [Join server](https://discord.gg/epicmanager)
- Documentation: [Wiki](https://github.com/wesellis/epic-games-manager/wiki)

### Pro Version
- Priority email: support@epicgamesmanager.com
- Response within 24 hours
- Remote assistance available
- Feature request priority

---

## 🚀 Next Steps

1. **Scan your library** - Import all your games
2. **Set up free game alerts** - Never miss free games
3. **Organize with categories** - Better library management
4. **Configure auto-claim** (Pro) - Automatic free game collection
5. **Join the community** - Share tips and get help

---

## 📝 License Agreement

By installing Epic Games Manager, you agree to:
- Use the software for personal use only
- Not redistribute without permission
- Respect Epic Games Store Terms of Service
- Pro license is per-user, non-transferable

---

*Thank you for choosing Epic Games Manager! Happy gaming! 🎮*