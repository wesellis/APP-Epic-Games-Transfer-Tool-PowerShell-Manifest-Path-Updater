"""
Game Information and Management Classes
"""

import os
import json
import psutil
import shutil
from pathlib import Path
from collections import defaultdict

class GameInfo:
    """Class to hold game information and metadata"""
    def __init__(self, name, path, size=0, last_played=None):
        self.name = name
        self.path = path
        self.size = size
        self.last_played = last_played
        self.has_saves = False
        self.is_updated = False
        self.manifest_file = None

class EpicGameManager:
    """Manages Epic Games operations and manifest handling"""
    
    def __init__(self):
        self.games_found = []
        self.stats = defaultdict(int)
        
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
    
    def close_epic_processes(self):
        """Close Epic Games Launcher processes"""
        processes_to_close = ["EpicGamesLauncher", "EpicWebHelper", "UnrealEngineLauncher", "EpicOnlineServices"]
        closed_count = 0
        closed_processes = []
        
        for proc_name in processes_to_close:
            try:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] and proc_name.lower() in proc.info['name'].lower():
                        proc.terminate()
                        closed_count += 1
                        closed_processes.append(f"{proc.info['name']} (PID: {proc.info['pid']})")
            except Exception as e:
                print(f"Error closing {proc_name}: {str(e)}")
                
        return closed_count, closed_processes
    
    def scan_games_folder(self, path):
        """Scan folder for Epic Games and return found games"""
        self.games_found.clear()
        found_games = []
        
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    # Check for Epic Games indicators
                    egstore_path = os.path.join(item_path, ".egstore")
                    if os.path.exists(egstore_path):
                        # Calculate folder size
                        size = self.get_folder_size(item_path)
                        game = GameInfo(item, item_path, size)
                        self.games_found.append(game)
                        found_games.append(game)
            
            return found_games
                        
        except Exception as e:
            raise Exception(f"Error scanning folder: {str(e)}")
    
    def get_folder_size(self, path):
        """Calculate folder size in bytes"""
        total_size = 0
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                    except (OSError, FileNotFoundError):
                        pass
        except Exception:
            pass
        return total_size
    
    def create_backup(self, manifests_dir=None):
        """Create backup of manifest files"""
        if not manifests_dir:
            manifests_dir = self.find_manifests_directory()
            
        if not manifests_dir:
            raise Exception("Cannot find manifests directory for backup")
        
        backup_dir = os.path.join(os.path.dirname(manifests_dir), "Manifests_Backup")
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{backup_dir}_{timestamp}"
        
        shutil.copytree(manifests_dir, backup_path)
        return backup_path
    
    def verify_games(self):
        """Verify game installations"""
        verified_games = []
        issues = []
        
        for game in self.games_found:
            if os.path.exists(game.path):
                # Check for essential files
                egstore_path = os.path.join(game.path, ".egstore")
                if os.path.exists(egstore_path):
                    verified_games.append(game)
                else:
                    issues.append(f"{game.name} - Missing .egstore folder")
            else:
                issues.append(f"{game.name} - Folder not found")
        
        return verified_games, issues
    
    def cleanup_cache(self):
        """Clean up Epic Games cache"""
        cache_paths = [
            os.path.expanduser("~\\AppData\\Local\\EpicGamesLauncher\\Saved\\webcache"),
            os.path.expanduser("~\\AppData\\Local\\EpicGamesLauncher\\Saved\\Logs"),
        ]
        
        cleaned_paths = []
        errors = []
        
        for cache_path in cache_paths:
            if os.path.exists(cache_path):
                try:
                    shutil.rmtree(cache_path)
                    cleaned_paths.append(cache_path)
                except Exception as e:
                    errors.append(f"Could not clean {cache_path}: {str(e)}")
        
        return cleaned_paths, errors
    
    def update_manifests(self, new_location, auto_verify=True):
        """Update Epic Games manifest files"""
        manifests_dir = self.find_manifests_directory()
        if not manifests_dir:
            raise Exception("Cannot find Epic Games manifests directory!")
        
        # Get all manifest files
        manifest_files = [f for f in os.listdir(manifests_dir) if f.endswith('.item')]
        if not manifest_files:
            raise Exception("No manifest files found!")
        
        results = {
            'updated': 0,
            'errors': 0,
            'skipped': 0,
            'total': len(manifest_files),
            'details': []
        }
        
        for manifest_file in manifest_files:
            try:
                manifest_path = os.path.join(manifests_dir, manifest_file)
                
                # Read and parse JSON
                with open(manifest_path, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                
                old_path = content.get('InstallLocation', '')
                if not old_path:
                    results['skipped'] += 1
                    continue
                    
                # Extract game name from old path
                game_name = os.path.basename(old_path.rstrip('\\'))
                new_path = os.path.join(new_location, game_name)
                
                # Check if game folder exists in new location
                if os.path.exists(new_path) and old_path != new_path:
                    # Verify game folder if enabled
                    if auto_verify:
                        egstore_path = os.path.join(new_path, '.egstore')
                        if not os.path.exists(egstore_path):
                            results['details'].append(f"Warning: {game_name} missing .egstore folder")
                    
                    # Update the paths
                    content['InstallLocation'] = new_path
                    content['ManifestLocation'] = os.path.join(new_path, '.egstore')
                    content['StagingLocation'] = os.path.join(new_path, '.egstore', 'bps')
                    
                    # Write back to file
                    with open(manifest_path, 'w', encoding='utf-8') as f:
                        json.dump(content, f, indent=2)
                        
                    results['updated'] += 1
                    results['details'].append(f"Updated: {game_name}")
                    
                    # Mark game as updated
                    for game in self.games_found:
                        if game.name == game_name:
                            game.is_updated = True
                            game.manifest_file = manifest_file
                            break
                    
                elif not os.path.exists(new_path):
                    results['skipped'] += 1
                    results['details'].append(f"Skipped: {game_name} (folder not found)")
                else:
                    results['skipped'] += 1
                    
            except Exception as e:
                results['errors'] += 1
                results['details'].append(f"Error processing {manifest_file}: {str(e)}")
                
        self.stats.update(results)
        return results
    
    def generate_report(self, output_path):
        """Generate a detailed report"""
        from datetime import datetime
        
        with open(output_path, 'w') as f:
            f.write("Epic Games Manifest Updater Pro - Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Games Found: {len(self.games_found)}\n\n")
            
            if self.games_found:
                total_size = sum(game.size for game in self.games_found)
                f.write(f"Total Size: {total_size / (1024**3):.2f} GB\n\n")
                
                f.write("Game Details:\n")
                f.write("-" * 30 + "\n")
                
                for game in self.games_found:
                    size_gb = game.size / (1024**3)
                    f.write(f"Name: {game.name}\n")
                    f.write(f"Path: {game.path}\n")
                    f.write(f"Size: {size_gb:.2f} GB\n")
                    f.write(f"Status: {'Updated' if game.is_updated else 'Pending'}\n")
                    if game.manifest_file:
                        f.write(f"Manifest: {game.manifest_file}\n")
                    f.write("\n")
            
            # Statistics
            if self.stats:
                f.write("Update Statistics:\n")
                f.write("-" * 20 + "\n")
                for key, value in self.stats.items():
                    if key != 'details':
                        f.write(f"{key.title()}: {value}\n")
        
        return output_path
