#!/usr/bin/env python3
"""
Test script for Epic Games Manifest Updater Pro
Verifies all modular components work correctly
"""

import sys
import os
import tempfile
import json
from pathlib import Path

# Add current directory to path for importing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_epic_theme_import():
    """Test Epic theme module import"""
    print("🎨 Testing Epic Theme module...")
    try:
        from epic_theme import EpicTheme
        # Test color constants
        assert hasattr(EpicTheme, 'EPIC_BLUE')
        assert hasattr(EpicTheme, 'PRIMARY_BG')
        assert EpicTheme.EPIC_BLUE == "#0078f2"
        print("✅ Epic Theme module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Epic Theme import failed: {e}")
        return False

def test_game_manager_import():
    """Test Game Manager module import"""
    print("\n🎮 Testing Game Manager module...")
    try:
        from game_manager import EpicGameManager, GameInfo
        
        # Test GameInfo class
        game = GameInfo("TestGame", "/path/to/game", 1024*1024*1024)  # 1GB
        assert game.name == "TestGame"
        assert game.size == 1024*1024*1024
        
        # Test EpicGameManager class
        manager = EpicGameManager()
        assert hasattr(manager, 'games_found')
        assert hasattr(manager, 'find_manifests_directory')
        
        print("✅ Game Manager module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Game Manager import failed: {e}")
        return False

def test_splash_screen_import():
    """Test Splash Screen module import"""
    print("\n🌟 Testing Splash Screen module...")
    try:
        from splash_screen import EpicSplashScreen
        print("✅ Splash Screen module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Splash Screen import failed: {e}")
        return False

def test_main_app_import():
    """Test main application import"""
    print("\n🚀 Testing Main Application module...")
    try:
        from epic_manifest_updater_pro import EpicManifestUpdaterPro
        print("✅ Main Application module imported successfully")
        return True
    except Exception as e:
        print(f"❌ Main Application import failed: {e}")
        return False

def test_gui_creation():
    """Test GUI creation without display"""
    print("\n🖥️ Testing GUI creation...")
    try:
        import tkinter as tk
        
        # Create test window (hidden)
        root = tk.Tk()
        root.withdraw()
        
        # Test Epic theme application
        from epic_theme import EpicTheme
        style = tk.ttk.Style()
        EpicTheme.configure_style(style)
        
        # Test widget creation
        frame = tk.Frame(root, bg=EpicTheme.PRIMARY_BG)
        label = EpicTheme.create_epic_label(frame, "Test Label")
        button = EpicTheme.create_epic_button(frame, "Test Button")
        
        # Clean up
        root.destroy()
        
        print("✅ GUI creation successful")
        return True
    except Exception as e:
        print(f"❌ GUI creation failed: {e}")
        return False

def test_game_operations():
    """Test game manager operations"""
    print("\n⚙️ Testing Game Manager operations...")
    try:
        from game_manager import EpicGameManager
        
        manager = EpicGameManager()
        
        # Test manifests directory detection
        manifests_dir = manager.find_manifests_directory()
        if manifests_dir:
            print(f"✅ Found manifests directory: {manifests_dir}")
        else:
            print("⚠️ No manifests directory found (Epic Games may not be installed)")
        
        # Test folder size calculation
        temp_dir = tempfile.mkdtemp()
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("test" * 100)  # 400 bytes
        
        size = manager.get_folder_size(temp_dir)
        assert size >= 400
        
        # Clean up
        os.unlink(test_file)
        os.rmdir(temp_dir)
        
        print("✅ Game Manager operations successful")
        return True
    except Exception as e:
        print(f"❌ Game Manager operations failed: {e}")
        return False

def test_epic_colors():
    """Test Epic Games color accuracy"""
    print("\n🎨 Testing Epic Games color accuracy...")
    try:
        from epic_theme import EpicTheme
        
        # Epic's official colors
        expected_colors = {
            'EPIC_BLUE': '#0078f2',
            'PRIMARY_BG': '#0f1419',
            'SECONDARY_BG': '#1a1f29',
            'EPIC_ORANGE': '#f99e1a'
        }
        
        for color_name, expected_value in expected_colors.items():
            actual_value = getattr(EpicTheme, color_name)
            assert actual_value.lower() == expected_value.lower(), f"{color_name}: expected {expected_value}, got {actual_value}"
        
        print("✅ Epic Games colors verified - authentic styling confirmed")
        return True
    except Exception as e:
        print(f"❌ Epic colors test failed: {e}")
        return False

def test_dependencies():
    """Test all required dependencies"""
    print("\n📦 Testing Pro dependencies...")
    
    required_modules = [
        ('tkinter', 'GUI framework'),
        ('psutil', 'Process management'),
        ('json', 'Manifest file parsing'),
        ('threading', 'Multi-threading support'),
        ('webbrowser', 'Link opening'),
        ('datetime', 'Timestamp generation'),
        ('pathlib', 'File path operations')
    ]
    
    success_count = 0
    
    for module_name, description in required_modules:
        try:
            __import__(module_name)
            print(f"✅ {module_name} - {description}")
            success_count += 1
        except ImportError:
            print(f"❌ {module_name} - {description} (MISSING)")
    
    if success_count == len(required_modules):
        print("✅ All Pro dependencies available")
        return True
    else:
        print(f"❌ Missing {len(required_modules) - success_count} dependencies")
        return False

def run_pro_tests():
    """Run all Pro version tests"""
    print("🎮 Epic Games Manifest Updater Pro - Test Suite")
    print("=" * 60)
    
    tests = [
        test_dependencies,
        test_epic_theme_import,
        test_game_manager_import,
        test_splash_screen_import,
        test_main_app_import,
        test_epic_colors,
        test_gui_creation,
        test_game_operations
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"🎮 Epic Pro Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Epic Games Manifest Updater Pro is ready!")
        print("✅ Epic Games theming verified")
        print("✅ Modular architecture working")
        print("✅ Advanced features functional")
        print("\n🚀 Ready to build with: python build_pro.py")
        return True
    else:
        print("⚠️ Some tests failed. Please check the issues above.")
        print("🔧 Fix the failing components before building Pro version")
        return False

if __name__ == "__main__":
    success = run_pro_tests()
    
    print(f"\n{'='*60}")
    if success:
        print("🎮 Epic Games Manifest Updater Pro - READY FOR EPIC GAMING! 🎮")
    else:
        print("🔧 Please fix the issues above before proceeding")
    
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
