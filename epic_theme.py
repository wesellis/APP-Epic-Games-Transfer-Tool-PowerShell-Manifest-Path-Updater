"""
Epic Games Theme Configuration
Provides Epic Games official color scheme and styling
"""

import tkinter as tk
from tkinter import ttk

class EpicTheme:
    """Epic Games color scheme and styling"""
    # Epic Games Official Colors
    PRIMARY_BG = "#0f1419"      # Epic's dark background
    SECONDARY_BG = "#1a1f29"    # Lighter dark background
    ACCENT_BG = "#2a3441"       # Card/panel background
    BUTTON_BG = "#313c4e"       # Button background
    
    # Epic's Blue Gradient
    EPIC_BLUE = "#0078f2"       # Primary Epic blue
    EPIC_BLUE_LIGHT = "#40a9ff" # Lighter blue
    EPIC_BLUE_DARK = "#005cb8"  # Darker blue
    
    # Status Colors
    SUCCESS_GREEN = "#52c41a"   # Success green
    WARNING_ORANGE = "#fa8c16"  # Warning orange  
    ERROR_RED = "#ff4d4f"       # Error red
    
    # Text Colors
    TEXT_PRIMARY = "#ffffff"    # Primary white text
    TEXT_SECONDARY = "#8c9196"  # Secondary gray text
    TEXT_MUTED = "#5c6370"      # Muted text
    
    # Epic Orange/Yellow accent
    EPIC_ORANGE = "#f99e1a"     # Epic's orange accent
    
    @classmethod
    def configure_style(cls, style):
        """Configure ttk styles with Epic Games theme"""
        
        # Configure main styles
        style.configure("Epic.TFrame", 
                       background=cls.PRIMARY_BG,
                       borderwidth=0)
        
        style.configure("EpicCard.TFrame",
                       background=cls.ACCENT_BG,
                       relief="flat",
                       borderwidth=1)
        
        style.configure("Epic.TLabel",
                       background=cls.PRIMARY_BG,
                       foreground=cls.TEXT_PRIMARY,
                       font=("Segoe UI", 10))
        
        style.configure("EpicTitle.TLabel",
                       background=cls.PRIMARY_BG,
                       foreground=cls.EPIC_BLUE,
                       font=("Segoe UI", 16, "bold"))
        
        style.configure("EpicSubtitle.TLabel",
                       background=cls.PRIMARY_BG,
                       foreground=cls.TEXT_SECONDARY,
                       font=("Segoe UI", 11))
        
        style.configure("EpicMuted.TLabel",
                       background=cls.PRIMARY_BG,
                       foreground=cls.TEXT_MUTED,
                       font=("Segoe UI", 9))
        
        # Epic-style buttons
        style.configure("EpicPrimary.TButton",
                       background=cls.EPIC_BLUE,
                       foreground=cls.TEXT_PRIMARY,
                       borderwidth=0,
                       focuscolor="none",
                       font=("Segoe UI", 10, "bold"))
        
        style.map("EpicPrimary.TButton",
                 background=[("active", cls.EPIC_BLUE_LIGHT),
                           ("pressed", cls.EPIC_BLUE_DARK)])
        
        style.configure("EpicSecondary.TButton",
                       background=cls.BUTTON_BG,
                       foreground=cls.TEXT_PRIMARY,
                       borderwidth=0,
                       focuscolor="none",
                       font=("Segoe UI", 10))
        
        style.map("EpicSecondary.TButton",
                 background=[("active", cls.ACCENT_BG),
                           ("pressed", cls.SECONDARY_BG)])
        
        # Epic-style entry
        style.configure("Epic.TEntry",
                       fieldbackground=cls.ACCENT_BG,
                       background=cls.ACCENT_BG,
                       foreground=cls.TEXT_PRIMARY,
                       borderwidth=1,
                       insertcolor=cls.TEXT_PRIMARY)
        
        # Epic-style progressbar
        style.configure("Epic.Horizontal.TProgressbar",
                       background=cls.EPIC_BLUE,
                       troughcolor=cls.ACCENT_BG,
                       borderwidth=0,
                       lightcolor=cls.EPIC_BLUE,
                       darkcolor=cls.EPIC_BLUE)

    @classmethod
    def create_epic_button(cls, parent, text, command=None, style="secondary"):
        """Create Epic Games styled button"""
        if style == "primary":
            bg_color = cls.EPIC_BLUE
            active_bg = cls.EPIC_BLUE_LIGHT
        else:
            bg_color = cls.BUTTON_BG
            active_bg = cls.ACCENT_BG
            
        return tk.Button(parent, text=text, font=("Segoe UI", 10),
                        bg=bg_color, fg=cls.TEXT_PRIMARY,
                        activebackground=active_bg,
                        activeforeground=cls.TEXT_PRIMARY,
                        relief=tk.FLAT, bd=0, cursor="hand2",
                        command=command)
    
    @classmethod
    def create_epic_label(cls, parent, text, style="normal"):
        """Create Epic Games styled label"""
        if style == "title":
            font = ("Segoe UI", 18, "bold")
            color = cls.TEXT_PRIMARY
        elif style == "subtitle":
            font = ("Segoe UI", 11)
            color = cls.TEXT_SECONDARY
        elif style == "accent":
            font = ("Segoe UI", 10, "bold")
            color = cls.EPIC_ORANGE
        else:
            font = ("Segoe UI", 10)
            color = cls.TEXT_PRIMARY
            
        return tk.Label(parent, text=text, font=font,
                       bg=cls.PRIMARY_BG, fg=color)
