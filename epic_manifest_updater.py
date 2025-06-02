#!/usr/bin/env python3
"""
Epic Games Manifest Updater - Python GUI Version
Author: Wesley Ellis
Email: wes@wesellis.com
Website: wesellis.com

A modern Python GUI application to update Epic Games manifest files
after moving your game installations to a new location.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import json
import os
import sys
import subprocess
import time
import threading
from pathlib import Path
from datetime import datetime
import psutil

class EpicManifestUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("Epic Games Manifest Updater v2.0")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Set icon if available
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Variables
        self.selected_path = tk.StringVar()
        self.is_processing = False
        
        # Create GUI
        self.create_widgets()
        
        # Center window
        self.center_window()
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        pos_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        
    def create_widgets(self):
        """Create the main GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Epic Games Manifest Updater", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Instructions
        instructions = """Instructions:
1. Move your Epic Games folder to the new location first
2. Select the new folder containing your game directories
3. Click 'Update Manifests' to fix Epic Games Launcher
4. Start Epic Games Launcher - your games should be recognized!"""
        
        inst_label = ttk.Label(main_frame, text=instructions, justify=tk.LEFT,
                              font=("Arial", 10))
        inst_label.grid(row=1, column=0, columnspan=3, pady=(0, 20), sticky=tk.W)
        
        # Path selection
        ttk.Label(main_frame, text="New Games Location:", 
                 font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W, pady=5)
        
        path_entry = ttk.Entry(main_frame, textvariable=self.selected_path, 
                              font=("Arial", 10), state="readonly")
        path_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 10), pady=5)
        
        browse_btn = ttk.Button(main_frame, text="Browse", command=self.browse_folder)
        browse_btn.grid(row=2, column=2, padx=(0, 0), pady=5)
        
        # Buttons frame
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=3, column=0, columnspan=3, pady=20)
        
        self.update_btn = ttk.Button(buttons_frame, text="Update Manifests", 
                                    command=self.start_update_process,
                                    style="Accent.TButton")
        self.update_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.close_epic_btn = ttk.Button(buttons_frame, text="Close Epic Launcher", 
                                        command=self.close_epic_games)
        self.close_epic_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Button(buttons_frame, text="Exit", 
                  command=self.root.quit).pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Log area
        log_frame = ttk.LabelFrame(main_frame, text="Activity Log", padding="10")
        log_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15, 
                                                 font=("Consolas", 9))
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
        
        # Initial log message
        self.log_message("Epic Games Manifest Updater initialized", "INFO")
        self.log_message("Select your new games folder to begin", "INFO")
        
    def log_message(self, message, level="INFO"):
        """Add a message to the log with timestamp"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {level}: {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def browse_folder(self):
        """Open folder browser dialog"""
        folder_path = filedialog.askdirectory(
            title="Select the folder containing your Epic Games",
            mustexist=True
        )
        
        if folder_path:
            self.selected_path.set(folder_path)
            self.log_message(f"Selected folder: {folder_path}", "INFO")
            
            # Check if folder contains game directories
            game_folders = self.find_game_folders(folder_path)
            if game_folders:
                self.log_message(f"Found {len(game_folders)} potential game folders", "SUCCESS")
                for folder in game_folders[:5]:  # Show first 5
                    self.log_message(f"  - {folder}", "INFO")
                if len(game_folders) > 5:
                    self.log_message(f"  ... and {len(game_folders) - 5} more", "INFO")
            else:
                self.log_message("Warning: No game folders found in selected directory", "WARNING")
                
    def find_game_folders(self, base_path):
        """Find potential game folders in the selected directory"""
        game_folders = []
        try:
            for item in os.listdir(base_path):
                item_path = os.path.join(base_path, item)
                if os.path.isdir(item_path):
                    # Check if it looks like a game folder (.egstore folder is a good indicator)
                    egstore_path = os.path.join(item_path, ".egstore")
                    if os.path.exists(egstore_path):
                        game_folders.append(item)
                    # Also include folders that might be games even without .egstore
                    elif any(ext in os.listdir(item_path) for ext in ['.exe', '.dll'] if os.path.isfile(os.path.join(item_path, ext))):
                        game_folders.append(item)
        except Exception as e:
            self.log_message(f"Error scanning folder: {str(e)}", "ERROR")
            
        return game_folders
        
    def close_epic_games(self):
        """Close Epic Games Launcher processes"""
        self.log_message("Attempting to close Epic Games Launcher...", "INFO")
        processes_to_close = ["EpicGamesLauncher", "EpicWebHelper", "UnrealEngineLauncher"]
        closed_count = 0
        
        for proc_name in processes_to_close:
            try:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] and proc_name.lower() in proc.info['name'].lower():
                        proc.terminate()
                        closed_count += 1
                        self.log_message(f"Closed process: {proc.info['name']} (PID: {proc.info['pid']})", "SUCCESS")
            except Exception as e:
                self.log_message(f"Error closing {proc_name}: {str(e)}", "WARNING")
                
        if closed_count > 0:
            self.log_message(f"Closed {closed_count} Epic Games processes", "SUCCESS")
            time.sleep(2)  # Give processes time to close
        else:
            self.log_message("No Epic Games processes found running", "INFO")
            
    def find_manifests_directory(self):
        """Find the Epic Games manifests directory"""
        possible_paths = [
            "C:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests",
            os.path.expanduser("~\\AppData\\Local\\EpicGamesLauncher\\Saved\\Config\\Windows"),
            "D:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests",
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
                
        return None
        
    def start_update_process(self):
        """Start the manifest update process in a separate thread"""
        if not self.selected_path.get():
            messagebox.showerror("Error", "Please select a folder first!")
            return
            
        if self.is_processing:
            return
            
        # Run in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self.update_manifests)
        thread.daemon = True
        thread.start()
        
    def update_manifests(self):
        """Update the Epic Games manifest files"""
        self.is_processing = True
        self.update_btn.config(state="disabled")
        self.progress.start()
        self.status_var.set("Processing...")
        
        try:
            new_location = self.selected_path.get()
            self.log_message("Starting manifest update process...", "INFO")
            
            # Find manifests directory
            manifests_dir = self.find_manifests_directory()
            if not manifests_dir:
                self.log_message("ERROR: Cannot find Epic Games manifests directory!", "ERROR")
                self.log_message("Make sure Epic Games Launcher is installed.", "ERROR")
                return
                
            self.log_message(f"Found manifests directory: {manifests_dir}", "SUCCESS")
            
            # Get all manifest files
            manifest_files = [f for f in os.listdir(manifests_dir) if f.endswith('.item')]
            if not manifest_files:
                self.log_message("No manifest files found!", "WARNING")
                return
                
            self.log_message(f"Found {len(manifest_files)} manifest files", "INFO")
            
            update_count = 0
            error_count = 0
            
            for manifest_file in manifest_files:
                try:
                    manifest_path = os.path.join(manifests_dir, manifest_file)
                    
                    # Read and parse JSON
                    with open(manifest_path, 'r', encoding='utf-8') as f:
                        content = json.load(f)
                    
                    old_path = content.get('InstallLocation', '')
                    if not old_path:
                        continue
                        
                    # Extract game name from old path
                    game_name = os.path.basename(old_path.rstrip('\\'))
                    new_path = os.path.join(new_location, game_name)
                    
                    # Check if game folder exists in new location
                    if os.path.exists(new_path) and old_path != new_path:
                        # Update the paths
                        content['InstallLocation'] = new_path
                        content['ManifestLocation'] = os.path.join(new_path, '.egstore')
                        content['StagingLocation'] = os.path.join(new_path, '.egstore', 'bps')
                        
                        # Write back to file
                        with open(manifest_path, 'w', encoding='utf-8') as f:
                            json.dump(content, f, indent=2)
                            
                        self.log_message(f"✓ Updated: {game_name}", "SUCCESS")
                        update_count += 1
                    else:
                        if not os.path.exists(new_path):
                            self.log_message(f"⚠ Game folder not found: {game_name}", "WARNING")
                        
                except Exception as e:
                    self.log_message(f"✗ Error processing {manifest_file}: {str(e)}", "ERROR")
                    error_count += 1
                    
            # Summary
            self.log_message("=" * 50, "INFO")
            self.log_message(f"UPDATE COMPLETE!", "SUCCESS")
            self.log_message(f"Successfully updated: {update_count} manifest(s)", "SUCCESS")
            if error_count > 0:
                self.log_message(f"Errors encountered: {error_count}", "WARNING")
            self.log_message("You can now start Epic Games Launcher", "SUCCESS")
            
            # Show completion dialog
            messagebox.showinfo("Update Complete", 
                              f"Successfully updated {update_count} manifest file(s)!\n\n"
                              f"You can now start Epic Games Launcher.")
            
        except Exception as e:
            self.log_message(f"FATAL ERROR: {str(e)}", "ERROR")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
        finally:
            self.is_processing = False
            self.update_btn.config(state="normal")
            self.progress.stop()
            self.status_var.set("Ready")


class SplashScreen:
    """Show a splash screen while the app loads"""
    def __init__(self):
        self.splash = tk.Toplevel()
        self.splash.title("")
        self.splash.geometry("400x300")
        self.splash.resizable(False, False)
        self.splash.configure(bg="#2c3e50")
        
        # Remove window decorations
        self.splash.overrideredirect(True)
        
        # Center splash screen
        self.center_splash()
        
        # Create splash content
        self.create_splash_content()
        
        # Auto-close after 3 seconds
        self.splash.after(3000, self.close_splash)
        
    def center_splash(self):
        """Center the splash screen"""
        self.splash.update_idletasks()
        width = 400
        height = 300
        pos_x = (self.splash.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.splash.winfo_screenheight() // 2) - (height // 2)
        self.splash.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        
    def create_splash_content(self):
        """Create splash screen content"""
        # Title
        title = tk.Label(self.splash, text="Epic Games\nManifest Updater", 
                        font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
        title.pack(pady=40)
        
        # Version
        version = tk.Label(self.splash, text="Version 2.0", 
                          font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
        version.pack()
        
        # Author
        author = tk.Label(self.splash, text="by Wesley Ellis", 
                         font=("Arial", 10), fg="#95a5a6", bg="#2c3e50")
        author.pack(pady=10)
        
        # Loading animation
        self.loading_label = tk.Label(self.splash, text="Loading...", 
                                     font=("Arial", 10), fg="#3498db", bg="#2c3e50")
        self.loading_label.pack(pady=20)
        
        # Start loading animation
        self.animate_loading()
        
    def animate_loading(self):
        """Animate the loading text"""
        current_text = self.loading_label.cget("text")
        if current_text == "Loading...":
            self.loading_label.config(text="Loading")
        elif current_text == "Loading":
            self.loading_label.config(text="Loading.")
        elif current_text == "Loading.":
            self.loading_label.config(text="Loading..")
        elif current_text == "Loading..":
            self.loading_label.config(text="Loading...")
            
        self.splash.after(200, self.animate_loading)
        
    def close_splash(self):
        """Close the splash screen"""
        self.splash.destroy()


def main():
    """Main application entry point"""
    # Create root window (hidden initially)
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    # Show splash screen
    splash = SplashScreen()
    root.wait_window(splash.splash)  # Wait for splash to close
    
    # Show main window
    root.deiconify()
    app = EpicManifestUpdater(root)
    
    # Start the application
    root.mainloop()


if __name__ == "__main__":
    main()
