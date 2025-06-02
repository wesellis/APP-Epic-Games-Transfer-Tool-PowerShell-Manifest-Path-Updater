#!/usr/bin/env python3
"""
Quick test to verify Epic Games Manifest Updater Clean works
No emojis - console safe version
"""

import os
import sys

def test_epic_clean():
    """Test the clean version can be imported"""
    print("[EPIC] Testing Epic Games Manifest Updater Clean...")
    
    try:
        # Test basic imports
        import tkinter as tk
        print("[OK] Tkinter available")
        
        import psutil
        print("[OK] psutil available")
        
        import json
        print("[OK] json available")
        
        # Test the app can be imported
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        
        print("[TEST] Testing app import...")
        
        # Try to import the classes from our clean app
        import epic_manifest_updater_clean
        print("[OK] Epic clean app imported successfully")
        
        # Test Epic theme colors
        from epic_manifest_updater_clean import EpicTheme
        assert EpicTheme.EPIC_BLUE == "#0078f2"
        print("[OK] Epic theme colors verified")
        
        print("")
        print("[SUCCESS] All tests passed! Ready to run Epic Games Manifest Updater!")
        print("[RUN] python epic_manifest_updater_clean.py")
        print("[BUILD] .\\build_simple.bat")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_epic_clean()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
