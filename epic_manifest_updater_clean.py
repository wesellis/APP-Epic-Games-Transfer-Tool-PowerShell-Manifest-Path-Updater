#!/usr/bin/env python3
"""
Epic Games Manifest Updater - Simple Working Version
Author: Wesley Ellis

A working Epic Games themed GUI application for updating manifests.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
from datetime import datetime
import os
import json
import psutil
import shutil

# Epic Games Theme Colors
class EpicTheme:
    PRIMARY_BG = "#0f1419"
    SECONDARY_BG = "#1a1f29"
    ACCENT_BG = "#2a3441"
    BUTTON_BG = "#313c4e"
    EPIC_BLUE = "#0078f2"
    EPIC_BLUE_LIGHT = "#40a9ff"
    EPIC_ORANGE = "#f99e1a"
    SUCCESS_GREEN = "#52c41a"
    WARNING_ORANGE = "#fa8c16"
    ERROR_RED = "#ff4d4f"
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#8c9196"
    TEXT_MUTED = "#5c6370"

class EpicManifestUpdater:
    def __init__(self, root):
        self.root = root
        self.root.title("Epic Games Manifest Updater Pro v2.5")
        self.root.geometry("900x600")
        self.root.configure(bg=EpicTheme.PRIMARY_BG)
        
        # Variables
        self.selected_path = tk.StringVar()
        self.is_processing = False
        self.games_found = []
        
        # Create GUI
        self.create_widgets()
        
        # Center window
        self.center_window()
        
        # Initialize
        self.log_message("[EPIC] Epic Games Manifest Updater Pro v2.5 Ready!", "EPIC")
        
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        pos_x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        
    def create_widgets(self):
        """Create Epic Games themed interface"""
        # Main container
        main_frame = tk.Frame(self.root, bg=EpicTheme.PRIMARY_BG)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header with Epic branding
        header_frame = tk.Frame(main_frame, bg=EpicTheme.PRIMARY_BG)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Epic logo
        logo_frame = tk.Frame(header_frame, bg=EpicTheme.EPIC_BLUE, width=50, height=50)
        logo_frame.pack(side=tk.LEFT, padx=(0, 15))
        logo_frame.pack_propagate(False)
        
        logo_label = tk.Label(logo_frame, text="E", font=("Segoe UI", 20, "bold"),
                             bg=EpicTheme.EPIC_BLUE, fg=EpicTheme.TEXT_PRIMARY)
        logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Title
        title_frame = tk.Frame(header_frame, bg=EpicTheme.PRIMARY_BG)
        title_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        tk.Label(title_frame, text="Epic Games Manifest Updater Pro",
                font=("Segoe UI", 16, "bold"),
                bg=EpicTheme.PRIMARY_BG, fg=EpicTheme.TEXT_PRIMARY).pack(anchor=tk.W)
        
        tk.Label(title_frame, text="Fix your game library after moving installations",
                font=("Segoe UI", 10),
                bg=EpicTheme.PRIMARY_BG, fg=EpicTheme.TEXT_SECONDARY).pack(anchor=tk.W)
        
        # Controls panel
        controls_frame = tk.Frame(main_frame, bg=EpicTheme.ACCENT_BG)
        controls_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Instructions
        inst_frame = tk.Frame(controls_frame, bg=EpicTheme.SECONDARY_BG)
        inst_frame.pack(fill=tk.X, padx=15, pady=15)
        
        tk.Label(inst_frame, text="Quick Start Guide",
                font=("Segoe UI", 11, "bold"),
                bg=EpicTheme.SECONDARY_BG, fg=EpicTheme.EPIC_ORANGE).pack(pady=10)
        
        instructions = [
            "1. Move your Epic Games folder to new location first",
            "2. Select the new folder location below",
            "3. Click 'Update Manifests' to fix Epic Games Launcher",
            "4. Start Epic Games Launcher - your games should be recognized!"
        ]
        
        for inst in instructions:
            tk.Label(inst_frame, text=inst, font=("Segoe UI", 9),
                    bg=EpicTheme.SECONDARY_BG, fg=EpicTheme.TEXT_SECONDARY).pack(anchor=tk.W, padx=10, pady=2)
        
        # Path selection
        path_frame = tk.Frame(controls_frame, bg=EpicTheme.ACCENT_BG)
        path_frame.pack(fill=tk.X, padx=15, pady=15)
        
        tk.Label(path_frame, text="New Games Location:",
                font=("Segoe UI", 10, "bold"),
                bg=EpicTheme.ACCENT_BG, fg=EpicTheme.TEXT_PRIMARY).pack(anchor=tk.W, pady=(0, 5))
        
        path_entry_frame = tk.Frame(path_frame, bg=EpicTheme.ACCENT_BG)
        path_entry_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.path_entry = tk.Entry(path_entry_frame, textvariable=self.selected_path,
                                  font=("Segoe UI", 10), bg=EpicTheme.SECONDARY_BG,
                                  fg=EpicTheme.TEXT_PRIMARY, insertbackground=EpicTheme.TEXT_PRIMARY,
                                  relief=tk.FLAT, bd=5, state="readonly")
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        browse_btn = tk.Button(path_entry_frame, text="Browse",
                              font=("Segoe UI", 10), bg=EpicTheme.BUTTON_BG,
                              fg=EpicTheme.TEXT_PRIMARY, relief=tk.FLAT,
                              activebackground=EpicTheme.EPIC_BLUE,
                              command=self.browse_folder)
        browse_btn.pack(side=tk.RIGHT)
        
        # Action buttons
        buttons_frame = tk.Frame(controls_frame, bg=EpicTheme.ACCENT_BG)
        buttons_frame.pack(fill=tk.X, padx=15, pady=(0, 15))
        
        self.update_btn = tk.Button(buttons_frame, text="Scan & Update Manifests",
                                   font=("Segoe UI", 12, "bold"),
                                   bg=EpicTheme.EPIC_BLUE, fg=EpicTheme.TEXT_PRIMARY,
                                   relief=tk.FLAT, activebackground=EpicTheme.EPIC_BLUE_LIGHT,
                                   command=self.start_update_process)
        self.update_btn.pack(fill=tk.X, pady=(0, 10), ipady=8)
        
        # Secondary buttons
        sec_buttons_frame = tk.Frame(buttons_frame, bg=EpicTheme.ACCENT_BG)
        sec_buttons_frame.pack(fill=tk.X)
        
        close_btn = tk.Button(sec_buttons_frame, text="Close Epic",
                             font=("Segoe UI", 10), bg=EpicTheme.BUTTON_BG,
                             fg=EpicTheme.TEXT_PRIMARY, relief=tk.FLAT,
                             command=self.close_epic_games)
        close_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        
        backup_btn = tk.Button(sec_buttons_frame, text="Backup",
                              font=("Segoe UI", 10), bg=EpicTheme.BUTTON_BG,
                              fg=EpicTheme.TEXT_PRIMARY, relief=tk.FLAT,
                              command=self.create_backup)
        backup_btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
        
        # Activity log
        log_frame = tk.Frame(main_frame, bg=EpicTheme.ACCENT_BG)
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        # Log header
        log_header = tk.Frame(log_frame, bg=EpicTheme.ACCENT_BG)
        log_header.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Label(log_header, text="Activity Log",
                font=("Segoe UI", 12, "bold"),
                bg=EpicTheme.ACCENT_BG, fg=EpicTheme.TEXT_PRIMARY).pack(side=tk.LEFT)
        
        clear_btn = tk.Button(log_header, text="Clear",
                             font=("Segoe UI", 9), bg=EpicTheme.BUTTON_BG,
                             fg=EpicTheme.TEXT_PRIMARY, relief=tk.FLAT,
                             command=self.clear_log)
        clear_btn.pack(side=tk.RIGHT)
        
        # Log text area
        self.log_text = scrolledtext.ScrolledText(log_frame, height=15,
                                                 font=("Consolas", 9),
                                                 bg=EpicTheme.PRIMARY_BG,
                                                 fg=EpicTheme.TEXT_PRIMARY,
                                                 insertbackground=EpicTheme.TEXT_PRIMARY,
                                                 selectbackground=EpicTheme.EPIC_BLUE,
                                                 relief=tk.FLAT, bd=0)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Configure text tags for colored logging
        self.log_text.tag_configure("INFO", foreground=EpicTheme.TEXT_PRIMARY)
        self.log_text.tag_configure("SUCCESS", foreground=EpicTheme.SUCCESS_GREEN)
        self.log_text.tag_configure("WARNING", foreground=EpicTheme.WARNING_ORANGE)
        self.log_text.tag_configure("ERROR", foreground=EpicTheme.ERROR_RED)
        self.log_text.tag_configure("EPIC", foreground=EpicTheme.EPIC_BLUE)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready - Select your new games folder to begin")
        status_bar = tk.Label(main_frame, textvariable=self.status_var,
                             font=("Segoe UI", 9), bg=EpicTheme.SECONDARY_BG,
                             fg=EpicTheme.TEXT_SECONDARY, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, pady=(10, 0))
        
    def log_message(self, message, level="INFO"):
        """Add a message to the log with Epic styling"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry, level)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def clear_log(self):
        """Clear the activity log"""
        self.log_text.delete(1.0, tk.END)
        self.log_message("[INFO] Activity log cleared", "INFO")
        
    def browse_folder(self):
        """Open folder browser dialog"""
        self.log_message("[INFO] Opening folder selection dialog...", "INFO")
        
        folder_path = filedialog.askdirectory(
            title="Select Epic Games Folder Location",
            mustexist=True
        )
        
        if folder_path:
            self.selected_path.set(folder_path)
            self.log_message(f"[SUCCESS] Selected folder: {folder_path}", "SUCCESS")
            self.scan_games_folder(folder_path)
        else:
            self.log_message("[WARNING] Folder selection cancelled", "WARNING")
            
    def scan_games_folder(self, path):
        """Scan folder for Epic Games"""
        self.log_message("[INFO] Scanning for Epic Games...", "INFO")
        self.games_found.clear()
        
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    egstore_path = os.path.join(item_path, ".egstore")
                    if os.path.exists(egstore_path):
                        self.games_found.append(item)
                        self.log_message(f"[SUCCESS] Found game: {item}", "SUCCESS")
            
            if self.games_found:
                self.log_message(f"[SUCCESS] Scan complete: {len(self.games_found)} games found", "SUCCESS")
                self.status_var.set(f"Found {len(self.games_found)} games - Ready to update manifests")
            else:
                self.log_message("[WARNING] No Epic Games found in selected folder", "WARNING")
                self.status_var.set("No games found - Please check folder location")
                
        except Exception as e:
            self.log_message(f"[ERROR] Error scanning folder: {str(e)}", "ERROR")
            
    def find_manifests_directory(self):
        """Find Epic Games manifests directory"""
        possible_paths = [
            "C:\\ProgramData\\Epic\\EpicGamesLauncher\\Data\\Manifests",
            os.path.expanduser("~\\AppData\\Local\\EpicGamesLauncher\\Saved\\Config\\Windows"),
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None
        
    def close_epic_games(self):
        """Close Epic Games processes"""
        self.log_message("[INFO] Closing Epic Games processes...", "INFO")
        
        processes_to_close = ["EpicGamesLauncher", "EpicWebHelper", "UnrealEngineLauncher"]
        closed_count = 0
        
        for proc_name in processes_to_close:
            try:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] and proc_name.lower() in proc.info['name'].lower():
                        proc.terminate()
                        closed_count += 1
                        self.log_message(f"[SUCCESS] Closed: {proc.info['name']}", "SUCCESS")
            except Exception as e:
                self.log_message(f"[WARNING] Error closing {proc_name}: {str(e)}", "WARNING")
        
        if closed_count > 0:
            self.log_message(f"[SUCCESS] Closed {closed_count} processes", "SUCCESS")
        else:
            self.log_message("[INFO] No Epic Games processes found", "INFO")
            
    def create_backup(self):
        """Create backup of manifest files"""
        self.log_message("[INFO] Creating manifest backup...", "INFO")
        
        try:
            manifests_dir = self.find_manifests_directory()
            if not manifests_dir:
                self.log_message("[ERROR] Cannot find manifests directory", "ERROR")
                return
            
            backup_dir = os.path.join(os.path.dirname(manifests_dir), "Manifests_Backup")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{backup_dir}_{timestamp}"
            
            shutil.copytree(manifests_dir, backup_path)
            self.log_message(f"[SUCCESS] Backup created: {backup_path}", "SUCCESS")
            messagebox.showinfo("Backup Complete", f"Backup created at:\n{backup_path}")
            
        except Exception as e:
            self.log_message(f"[ERROR] Backup failed: {str(e)}", "ERROR")
            
    def start_update_process(self):
        """Start the update process"""
        if not self.selected_path.get():
            messagebox.showerror("No Folder Selected", "Please select your games folder first!")
            return
            
        if not self.games_found:
            self.log_message("[WARNING] No games found - scan folder first", "WARNING")
            return
            
        if self.is_processing:
            return
        
        # Run in separate thread
        thread = threading.Thread(target=self.update_manifests)
        thread.daemon = True
        thread.start()
        
    def update_manifests(self):
        """Update Epic Games manifest files"""
        self.is_processing = True
        self.update_btn.config(state="disabled", text="Updating...")
        self.status_var.set("Updating manifest files...")
        
        try:
            new_location = self.selected_path.get()
            self.log_message("[EPIC] Starting manifest update process...", "EPIC")
            
            manifests_dir = self.find_manifests_directory()
            if not manifests_dir:
                self.log_message("[ERROR] Cannot find manifests directory!", "ERROR")
                return
            
            self.log_message(f"[SUCCESS] Found manifests: {manifests_dir}", "SUCCESS")
            
            manifest_files = [f for f in os.listdir(manifests_dir) if f.endswith('.item')]
            if not manifest_files:
                self.log_message("[WARNING] No manifest files found!", "WARNING")
                return
            
            self.log_message(f"[INFO] Processing {len(manifest_files)} manifest files...", "INFO")
            
            update_count = 0
            error_count = 0
            
            for manifest_file in manifest_files:
                try:
                    manifest_path = os.path.join(manifests_dir, manifest_file)
                    
                    with open(manifest_path, 'r', encoding='utf-8') as f:
                        content = json.load(f)
                    
                    old_path = content.get('InstallLocation', '')
                    if not old_path:
                        continue
                    
                    game_name = os.path.basename(old_path.rstrip('\\'))
                    new_path = os.path.join(new_location, game_name)
                    
                    if os.path.exists(new_path) and old_path != new_path:
                        content['InstallLocation'] = new_path
                        content['ManifestLocation'] = os.path.join(new_path, '.egstore')
                        content['StagingLocation'] = os.path.join(new_path, '.egstore', 'bps')
                        
                        with open(manifest_path, 'w', encoding='utf-8') as f:
                            json.dump(content, f, indent=2)
                        
                        self.log_message(f"[SUCCESS] Updated: {game_name}", "SUCCESS")
                        update_count += 1
                    
                except Exception as e:
                    self.log_message(f"[ERROR] Error processing {manifest_file}: {str(e)}", "ERROR")
                    error_count += 1
            
            # Summary
            self.log_message("=" * 50, "INFO")
            self.log_message("[EPIC] EPIC GAMES UPDATE COMPLETE!", "EPIC")
            self.log_message(f"[SUCCESS] Updated: {update_count} games", "SUCCESS")
            if error_count > 0:
                self.log_message(f"[ERROR] Errors: {error_count}", "ERROR")
            self.log_message("[EPIC] You can now start Epic Games Launcher!", "EPIC")
            
            # Show completion dialog
            result_msg = f"Epic Games Update Complete!\n\n"
            result_msg += f"Updated: {update_count} games\n"
            if error_count > 0:
                result_msg += f"Errors: {error_count}\n"
            result_msg += f"\nReady to launch Epic Games!"
            
            messagebox.showinfo("Update Complete", result_msg)
            
        except Exception as e:
            self.log_message(f"[ERROR] FATAL ERROR: {str(e)}", "ERROR")
            messagebox.showerror("Critical Error", f"Error: {str(e)}")
            
        finally:
            self.is_processing = False
            self.update_btn.config(state="normal", text="Scan & Update Manifests")
            self.status_var.set("Update complete - Ready for Epic Games Launcher")


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = EpicManifestUpdater(root)
    root.mainloop()


if __name__ == "__main__":
    main()
