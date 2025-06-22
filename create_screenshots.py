#!/usr/bin/env python3
"""Generate screenshots for Epic Games Manager marketing"""

import os
import sys
from pathlib import Path

# Create assets directory
assets_dir = Path('assets')
assets_dir.mkdir(exist_ok=True)

# Create a sample terminal output for screenshots
sample_output = """
===========================================
    Epic Games Manager Pro v1.2.0
===========================================

🔍 Scanning Epic Games library...

✅ Found 12 games:

  - Fortnite (142.3 GB)
  - Grand Theft Auto V (95.8 GB)
  - Red Dead Redemption 2 (116.2 GB)
  - Control (42.5 GB)
  - Rocket League (23.1 GB)
  - Metro Exodus (72.9 GB)
  - Borderlands 3 (85.4 GB)
  - The Witcher 3 (64.7 GB)
  - Cyberpunk 2077 (102.5 GB)
  - Hades (12.3 GB)
  - Among Us (385 MB)
  - Fall Guys (8.7 GB)

📂 Current location: C:\\Epic Games
🎯 New location detected: D:\\Games\\Epic

Would you like to update all game locations? [Y/n]: Y

🔧 Updating game manifests...
  ✓ Fortnite - Updated
  ✓ Grand Theft Auto V - Updated
  ✓ Red Dead Redemption 2 - Updated
  ✓ Control - Updated
  ✓ Rocket League - Updated
  ✓ Metro Exodus - Updated
  ✓ Borderlands 3 - Updated
  ✓ The Witcher 3 - Updated
  ✓ Cyberpunk 2077 - Updated
  ✓ Hades - Updated
  ✓ Among Us - Updated
  ✓ Fall Guys - Updated

✅ Successfully updated 12 games!
💾 Saved 766.8 GB from re-downloading

🎮 You can now launch Epic Games and all your games will work!

Pro Features Active:
  ✓ Unlimited games
  ✓ Automatic backups created
  ✓ Batch operations enabled
  ✓ Priority support available
"""

# Save as text file that can be used for screenshots
with open(assets_dir / 'sample_output.txt', 'w') as f:
    f.write(sample_output)

# Create marketing copy
marketing_copy = """
EPIC GAMES MANAGER PRO - MARKETING COPY

Tagline: "Moved Your Games? Don't Re-Download!"

Short Description:
Fix your Epic Games library in seconds after moving games to a new drive. Save hundreds of GB of downloads!

Key Benefits:
• Save hours of re-downloading
• One-click fix for moved games
• Works with any Epic Games installation
• Automatic backup protection
• Lifetime updates included

Customer Testimonials (Mock):
"Saved me from re-downloading 500GB of games!" - John D.
"Finally, a tool that just works!" - Sarah M.
"Worth every penny. Saved so much time!" - Mike R.

Screenshot Ideas:
1. Before/After showing Epic Games not finding games vs. all games working
2. Terminal showing the scan and update process
3. Diagram showing how it works
4. Success message with GB saved

Price Points:
- Free Version: Basic features, 5 game limit
- Pro Version: $4.99 - Unlimited games, all features
"""

with open(assets_dir / 'marketing_copy.txt', 'w') as f:
    f.write(marketing_copy)

# Create README for Gumroad
gumroad_description = """
Epic Games Manager Pro - Never Re-Download Your Games Again!

🚨 THE PROBLEM:
You moved your Epic Games to a new drive, and now Epic Launcher can't find them. 
It wants you to re-download EVERYTHING. That's hundreds of gigabytes!

✅ THE SOLUTION:
Epic Games Manager updates your game locations in seconds. 
No re-downloading. No waiting. Just fixed.

🎯 FEATURES:
• Automatic game detection
• One-click manifest repair  
• Batch update all games at once
• Backup before changes
• Command line automation
• Works with Epic Games on Windows/Mac/Linux

💎 PRO VERSION INCLUDES:
• Unlimited games (Free: 5 games only)
• Automatic backups
• Priority email support
• Lifetime updates
• Command line integration

🛠️ HOW IT WORKS:
1. Run the tool
2. It finds your games
3. Updates Epic's manifest files
4. Your games work again!

⏱️ TIME SAVED:
- Average game: 50GB = 2+ hours to download
- 10 games = 20+ hours saved
- Your time is worth more than $4.99!

📋 REQUIREMENTS:
- Epic Games Launcher installed
- Python 3.8+ (or use PowerShell version)
- Windows 10/11 (Mac/Linux supported)

🎁 INSTANT DELIVERY:
Download immediately after purchase. 
License key sent via email.

💬 SUPPORT:
Email support included for Pro users.
Response within 24 hours.

🔒 GUARANTEE:
30-day money back guarantee if it doesn't work for you.

Don't waste hours re-downloading. Fix it now!
"""

with open(assets_dir / 'gumroad_description.txt', 'w') as f:
    f.write(gumroad_description)

print("✅ Marketing assets created in 'assets' directory:")
print("  - sample_output.txt (for terminal screenshots)")
print("  - marketing_copy.txt (for promotional materials)")
print("  - gumroad_description.txt (for product listing)")
print("\nNext steps:")
print("1. Take screenshots of sample_output.txt in a terminal")
print("2. Create a simple cover image (1280x720)")
print("3. Use gumroad_description.txt for your product listing")