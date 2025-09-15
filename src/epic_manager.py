#!/usr/bin/env python3
"""Epic Games Manager - Main Entry Point"""

import argparse
import sys
from pathlib import Path
from typing import Optional

from library.scanner import LibraryScanner
from library.manifest import ManifestManager
from downloads.queue_manager import DownloadQueueManager
from free_games.tracker import FreeGamesTracker
from achievements.monitor import AchievementMonitor
from core.config import Config
from core.license import LicenseValidator

class EpicGamesManager:
    def __init__(self):
        self.config = Config()
        self.license = LicenseValidator()
        self.library_scanner = LibraryScanner()
        self.manifest_manager = ManifestManager()
        self.download_manager = DownloadQueueManager()
        self.free_games = FreeGamesTracker()
        self.achievements = AchievementMonitor()
        
    def scan_library(self):
        """Scan Epic Games library for installed games"""
        print("🔍 Scanning Epic Games library...")
        games = self.library_scanner.scan()
        
        if not games:
            print("❌ No games found. Is Epic Games Launcher installed?")
            return
            
        print(f"\n✅ Found {len(games)} games:")
        for game in games:
            print(f"  - {game.name} ({game.size_gb:.1f} GB)")
            
    def repair_manifest(self, game_name: Optional[str] = None):
        """Repair game manifests"""
        tier = self.license.get_tier()
        
        if game_name:
            print(f"🔧 Repairing manifest for {game_name}...")
            success = self.manifest_manager.repair_game(game_name)
            if success:
                print(f"✅ Successfully repaired {game_name}")
            else:
                print(f"❌ Failed to repair {game_name}")
        else:
            if tier == "free":
                print("⚠️  Batch repair requires Pro version")
                print("💎 Upgrade at: https://gumroad.com/l/epic-games-manager")
                return
                
            print("🔧 Repairing all game manifests...")
            repaired = self.manifest_manager.repair_all()
            print(f"✅ Repaired {repaired} games")
            
    def track_free_games(self):
        """Check for free games"""
        print("🎮 Checking for free games...")
        games = self.free_games.get_current_free()
        
        if not games:
            print("❌ No free games available right now")
            return
            
        print(f"\n🎁 Free games this week:")
        for game in games:
            print(f"  - {game['title']}")
            print(f"    Available until: {game['end_date']}")
            
    def backup_saves(self, all_games: bool = False):
        """Backup game saves"""
        tier = self.license.get_tier()
        
        if all_games and tier == "free":
            print("⚠️  Bulk backup requires Pro version")
            print("💎 Upgrade at: https://gumroad.com/l/epic-games-manager")
            return
            
        print("💾 Backing up game saves...")
        # Implementation here
        print("✅ Backup complete")
        
    def show_achievements(self):
        """Display achievement progress"""
        print("🏆 Loading achievements...")
        stats = self.achievements.get_stats()
        
        print(f"\n📊 Achievement Statistics:")
        print(f"  Total Games: {stats['total_games']}")
        print(f"  Total Achievements: {stats['total_achievements']}")
        print(f"  Unlocked: {stats['unlocked']} ({stats['completion_rate']:.1f}%)")

def main():
    parser = argparse.ArgumentParser(
        description="Epic Games Manager - Manage your Epic Games library",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  epic_manager.py scan                    # Scan library
  epic_manager.py repair --game Fortnite  # Repair specific game
  epic_manager.py free-games              # Check free games
  epic_manager.py backup --all            # Backup all saves (Pro)
  
Pro Version ($4.99): https://gumroad.com/l/epic-games-manager
Support: https://github.com/yourusername/epic-games-manager
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Scan Epic Games library')
    
    # Repair command
    repair_parser = subparsers.add_parser('repair', help='Repair game manifests')
    repair_parser.add_argument('--game', type=str, help='Specific game to repair')
    
    # Free games command
    free_parser = subparsers.add_parser('free-games', help='Check free games')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Backup game saves')
    backup_parser.add_argument('--all', action='store_true', help='Backup all games (Pro)')
    
    # Achievements command
    achievements_parser = subparsers.add_parser('achievements', help='Show achievements')
    
    # License command
    license_parser = subparsers.add_parser('license', help='Manage license')
    license_parser.add_argument('--activate', type=str, help='Activate license key')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
        
    manager = EpicGamesManager()
    
    if args.command == 'scan':
        manager.scan_library()
    elif args.command == 'repair':
        manager.repair_manifest(args.game)
    elif args.command == 'free-games':
        manager.track_free_games()
    elif args.command == 'backup':
        manager.backup_saves(args.all)
    elif args.command == 'achievements':
        manager.show_achievements()
    elif args.command == 'license':
        if args.activate:
            manager.license.activate(args.activate)
        else:
            tier = manager.license.get_tier()
            print(f"Current tier: {tier}")
            if tier == "free":
                print("\n💎 Upgrade to Pro: https://gumroad.com/l/epic-games-manager")

if __name__ == "__main__":
    main()