"""
Epic Games Themed Splash Screen
"""

import tkinter as tk
from epic_theme import EpicTheme

class EpicSplashScreen:
    """Epic Games themed splash screen"""
    def __init__(self):
        self.splash = tk.Toplevel()
        self.splash.title("")
        self.splash.geometry("500x350")
        self.splash.resizable(False, False)
        self.splash.configure(bg=EpicTheme.PRIMARY_BG)
        
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
        width = 500
        height = 350
        pos_x = (self.splash.winfo_screenwidth() // 2) - (width // 2)
        pos_y = (self.splash.winfo_screenheight() // 2) - (height // 2)
        self.splash.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        
    def create_splash_content(self):
        """Create Epic Games themed splash content"""
        # Background gradient effect
        bg_frame = tk.Frame(self.splash, bg=EpicTheme.PRIMARY_BG)
        bg_frame.pack(fill=tk.BOTH, expand=True)
        
        # Epic logo area
        logo_frame = tk.Frame(bg_frame, bg=EpicTheme.EPIC_BLUE, width=80, height=80)
        logo_frame.pack(pady=40)
        logo_frame.pack_propagate(False)
        
        logo_label = tk.Label(logo_frame, text="E", font=("Segoe UI", 36, "bold"),
                             bg=EpicTheme.EPIC_BLUE, fg=EpicTheme.TEXT_PRIMARY)
        logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Title with Epic styling
        title = tk.Label(bg_frame, text="Epic Games\nManifest Updater Pro", 
                        font=("Segoe UI", 20, "bold"), 
                        fg=EpicTheme.TEXT_PRIMARY, bg=EpicTheme.PRIMARY_BG)
        title.pack(pady=10)
        
        # Version with Epic orange
        version = tk.Label(bg_frame, text="Version 2.5 Pro Edition", 
                          font=("Segoe UI", 12), 
                          fg=EpicTheme.EPIC_ORANGE, bg=EpicTheme.PRIMARY_BG)
        version.pack()
        
        # Author
        author = tk.Label(bg_frame, text="by Wesley Ellis", 
                         font=("Segoe UI", 10), 
                         fg=EpicTheme.TEXT_SECONDARY, bg=EpicTheme.PRIMARY_BG)
        author.pack(pady=10)
        
        # Loading with Epic blue
        self.loading_label = tk.Label(bg_frame, text="🎮 Loading Epic experience...", 
                                     font=("Segoe UI", 10), 
                                     fg=EpicTheme.EPIC_BLUE, bg=EpicTheme.PRIMARY_BG)
        self.loading_label.pack(pady=20)
        
        # Epic-style border
        border_frame = tk.Frame(bg_frame, bg=EpicTheme.EPIC_BLUE, height=2)
        border_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Start loading animation
        self.animate_loading()
        
    def animate_loading(self):
        """Animate the loading text with Epic theme"""
        texts = [
            "🎮 Loading Epic experience...",
            "🎮 Initializing game scanner...",
            "🎮 Preparing manifest tools...",
            "🎮 Almost ready..."
        ]
        
        current_text = self.loading_label.cget("text")
        try:
            current_index = texts.index(current_text)
            next_index = (current_index + 1) % len(texts)
        except ValueError:
            next_index = 0
            
        self.loading_label.config(text=texts[next_index])
        if hasattr(self.splash, 'winfo_exists') and self.splash.winfo_exists():
            self.splash.after(500, self.animate_loading)
        
    def close_splash(self):
        """Close the splash screen"""
        if hasattr(self.splash, 'winfo_exists') and self.splash.winfo_exists():
            self.splash.destroy()
