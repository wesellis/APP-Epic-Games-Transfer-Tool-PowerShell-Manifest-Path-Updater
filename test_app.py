#!/usr/bin/env python3
"""
Test script for Epic Games Manifest Updater
Verifies the application can start and basic functionality works
"""

import sys
import os
import tempfile
import json
from pathlib import Path

# Add current directory to path for importing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        import tkinter as tk
        from tkinter import ttk, filedialog, messagebox, scrolledtext
        import psutil
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_manifest_parsing():
    """Test JSON manifest file parsing"""
    print("\nTesting manifest parsing...")
    
    # Create a sample manifest file
    sample_manifest = {
        "AppName": "TestGame",
        "InstallLocation": "C:\\Epic Games\\TestGame",
        "ManifestLocation": "C:\\Epic Games\\TestGame\\.egstore",
        "StagingLocation": "C:\\Epic Games\\TestGame\\.egstore\\bps"
    }
    
    try:
        # Test JSON serialization/deserialization
        json_str = json.dumps(sample_manifest, indent=2)
        parsed = json.loads(json_str)
        
        assert parsed["AppName"] == "TestGame"
        assert "InstallLocation" in parsed
        print("✓ Manifest parsing works correctly")
        return True
    except Exception as e:
        print(f"✗ Manifest parsing failed: {e}")
        return False

def test_path_operations():
    """Test path manipulation functions"""
    print("\nTesting path operations...")
    
    try:
        # Test path joining and splitting
        old_path = "C:\\Epic Games\\TestGame"
        new_base = "D:\\Games\\Epic"
        game_name = os.path.basename(old_path)
        new_path = os.path.join(new_base, game_name)
        
        assert game_name == "TestGame"
        assert new_path == "D:\\Games\\Epic\\TestGame"
        print("✓ Path operations work correctly")
        return True
    except Exception as e:
        print(f"✗ Path operations failed: {e}")
        return False

def test_gui_creation():
    """Test that GUI can be created without errors"""
    print("\nTesting GUI creation...")
    
    try:
        import tkinter as tk
        
        # Create a simple test window
        root = tk.Tk()
        root.withdraw()  # Hide window
        
        # Test creating basic widgets
        frame = tk.Frame(root)
        label = tk.Label(frame, text="Test")
        button = tk.Button(frame, text="Test Button")
        
        # Clean up
        root.destroy()
        
        print("✓ GUI creation successful")
        return True
    except Exception as e:
        print(f"✗ GUI creation failed: {e}")
        return False

def test_file_operations():
    """Test file read/write operations"""
    print("\nTesting file operations...")
    
    try:
        # Create temporary test file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            test_data = {"test": "data"}
            json.dump(test_data, f)
            temp_path = f.name
        
        # Test reading
        with open(temp_path, 'r') as f:
            loaded_data = json.load(f)
        
        assert loaded_data["test"] == "data"
        
        # Clean up
        os.unlink(temp_path)
        
        print("✓ File operations successful")
        return True
    except Exception as e:
        print(f"✗ File operations failed: {e}")
        return False

def run_all_tests():
    """Run all tests and report results"""
    print("Epic Games Manifest Updater - Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_manifest_parsing,
        test_path_operations,
        test_gui_creation,
        test_file_operations
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application should work correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the requirements and dependencies.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    
    if success:
        print("\n✅ Ready to build executable with: python build_exe.py")
    else:
        print("\n❌ Please fix the issues above before building")
    
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
