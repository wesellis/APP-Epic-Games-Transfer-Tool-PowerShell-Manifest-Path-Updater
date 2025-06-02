# Epic Games Manifest Updater v2.0 - Quick Start Guide

## 🚀 For End Users (Just Want the Tool)

### **Download & Run (Easiest)**
1. Go to [Releases](https://github.com/wesellis/epic-manifest-updater/releases)
2. Download `EpicManifestUpdater.exe`
3. Double-click to run (no installation needed!)
4. Follow the GUI instructions

### **Problem This Solves**
- Moved Epic Games folder to new drive/location?
- Epic Launcher can't find your games?
- Don't want to re-download everything?
- **This tool fixes it in 30 seconds!**

---

## 🛠️ For Developers (Want to Build/Modify)

### **Quick Build**
```bash
# 1. Clone repository
git clone https://github.com/wesellis/epic-manifest-updater.git
cd epic-manifest-updater

# 2. Test everything works
python test_app.py

# 3. Build executable
python build_exe.py
```

### **File Structure**
```
epic-manifest-updater/
├── epic_manifest_updater.py    # 🎯 Main application
├── build_exe.py               # 🔨 Build script
├── test_app.py                # 🧪 Test suite
├── requirements.txt           # 📦 Dependencies
├── build.bat                  # 🪟 Windows build script
└── README_v2.md              # 📖 Full documentation
```

---

## ⚡ What's New in v2.0

| Feature | Old (PowerShell) | New (Python GUI) |
|---------|------------------|------------------|
| **Interface** | Command line | Modern GUI |
| **Feedback** | Minimal | Real-time log |
| **Error Handling** | Basic | Comprehensive |
| **User Experience** | Technical | User-friendly |
| **Distribution** | Script file | Portable .exe |

---

## 🎯 Usage Examples

### **Scenario 1: Moved to New Drive**
```
Before: C:\Epic Games\
After:  D:\Epic Games\

1. Move folder manually
2. Run Epic Manifest Updater
3. Select D:\Epic Games\
4. Click "Update Manifests"
5. Done! ✅
```

### **Scenario 2: Reorganized Folders**
```
Before: C:\Games\Epic\
After:  D:\Gaming\Epic Games\

1. Move and rename folder
2. Run updater
3. Select new location
4. Update manifests
5. Epic Launcher finds games ✅
```

---

## 🔧 Build Requirements

### **System Requirements**
- Windows 10/11 (for .exe)
- Python 3.7+ (for source)
- ~100MB disk space

### **Python Dependencies**
- `psutil` - Process management
- `pyinstaller` - Executable creation
- `tkinter` - GUI (built into Python)

### **Build Process**
1. **Test** - Verify all dependencies work
2. **Build** - Create standalone executable
3. **Distribute** - Share the .exe file

---

## 💡 Pro Tips

### **For Users**
- ✅ Always close Epic Launcher first
- ✅ Make sure games are actually moved
- ✅ Check the activity log for details
- ✅ Run as admin if permission issues

### **For Developers**
- ✅ Test with `test_app.py` first
- ✅ Use virtual environment for clean builds
- ✅ Check PyInstaller warnings
- ✅ Test .exe on clean Windows machine

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| **"Manifests not found"** | Install Epic Games Launcher |
| **"No games found"** | Check folder contains game directories |
| **"Permission denied"** | Close Epic Launcher, run as admin |
| **"Build failed"** | Check Python version, install requirements |

---

## 📞 Need Help?

- **🐛 Bug Report**: [Create Issue](https://github.com/wesellis/epic-manifest-updater/issues)
- **💭 Questions**: [Discussions](https://github.com/wesellis/epic-manifest-updater/discussions)
- **📧 Contact**: wes@wesellis.com

---

**Ready to fix your Epic Games library? Download now!** 🎮✨
