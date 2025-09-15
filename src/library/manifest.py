"""Manifest manager for handling Epic Games manifest repairs and updates."""

import json
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
import logging
from datetime import datetime

from .game import Game
from .scanner import LibraryScanner

logger = logging.getLogger(__name__)


class ManifestManager:
    """Manages Epic Games manifest files and repairs."""
    
    def __init__(self, scanner: Optional[LibraryScanner] = None):
        """Initialize the manifest manager.
        
        Args:
            scanner: Optional LibraryScanner instance to use
        """
        self.scanner = scanner or LibraryScanner()
        self.backup_dir = self._get_backup_directory()
    
    @staticmethod
    def _get_backup_directory() -> Path:
        """Get the backup directory for manifest files.
        
        Returns:
            Path to the backup directory
        """
        backup_dir = Path.home() / '.epic_games_manager' / 'backups'
        backup_dir.mkdir(parents=True, exist_ok=True)
        return backup_dir
    
    def backup_manifest(self, game: Game) -> Optional[Path]:
        """Create a backup of a game's manifest file.
        
        Args:
            game: Game instance to backup
            
        Returns:
            Path to the backup file or None if backup failed
        """
        if not game.manifest_path or not game.manifest_path.exists():
            logger.error(f"Cannot backup manifest for {game.display_name}: manifest path not found")
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{game.app_name}_{timestamp}.item"
        backup_path = self.backup_dir / backup_filename
        
        try:
            shutil.copy2(game.manifest_path, backup_path)
            logger.info(f"Created backup: {backup_path}")
            return backup_path
        except Exception as e:
            logger.error(f"Failed to backup manifest for {game.display_name}: {e}")
            return None
    
    def update_game_location(self, game: Game, new_base_path: Path) -> bool:
        """Update a game's location in its manifest file.
        
        Args:
            game: Game instance to update
            new_base_path: New base directory for the game
            
        Returns:
            True if update was successful
        """
        if not game.manifest_path or not game.manifest_path.exists():
            logger.error(f"Cannot update manifest for {game.display_name}: manifest path not found")
            return False
        
        # Check if the new location actually exists
        new_game_path = new_base_path / game.get_game_folder_name()
        if not new_game_path.exists():
            logger.error(f"New game location does not exist: {new_game_path}")
            return False
        
        # Backup the manifest first
        backup_path = self.backup_manifest(game)
        if not backup_path:
            logger.warning("Failed to create backup, proceeding anyway...")
        
        try:
            # Read the current manifest
            with open(game.manifest_path, 'r', encoding='utf-8') as f:
                manifest_data = json.load(f)
            
            # Update the game object
            game.update_location(new_base_path)
            
            # Update the manifest data
            manifest_data['InstallLocation'] = str(game.install_location)
            manifest_data['ManifestLocation'] = str(game.manifest_location)
            manifest_data['StagingLocation'] = str(game.staging_location)
            
            # Write the updated manifest
            with open(game.manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest_data, f, indent=2)
            
            logger.info(f"Updated manifest for {game.display_name} to {new_game_path}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to update manifest for {game.display_name}: {e}")
            
            # Try to restore from backup
            if backup_path and backup_path.exists():
                try:
                    shutil.copy2(backup_path, game.manifest_path)
                    logger.info("Restored manifest from backup")
                except Exception as restore_error:
                    logger.error(f"Failed to restore backup: {restore_error}")
            
            return False
    
    def bulk_update_location(self, new_base_path: Path) -> Tuple[List[Game], List[Game]]:
        """Update the location for all games that exist in the new path.
        
        Args:
            new_base_path: New base directory containing game folders
            
        Returns:
            Tuple of (updated_games, failed_games)
        """
        if not new_base_path.exists() or not new_base_path.is_dir():
            logger.error(f"New base path does not exist or is not a directory: {new_base_path}")
            return [], []
        
        # Scan for current manifests
        games = self.scanner.scan_manifests()
        
        updated_games = []
        failed_games = []
        
        for game in games:
            # Check if the game exists in the new location
            new_game_path = new_base_path / game.get_game_folder_name()
            
            if new_game_path.exists() and new_game_path.is_dir():
                # Update the manifest
                if self.update_game_location(game, new_base_path):
                    updated_games.append(game)
                else:
                    failed_games.append(game)
            else:
                logger.info(f"Skipping {game.display_name}: not found in new location")
        
        logger.info(f"Updated {len(updated_games)} games, {len(failed_games)} failed")
        return updated_games, failed_games
    
    def repair_manifest(self, game: Game) -> bool:
        """Attempt to repair a corrupt or missing manifest.
        
        Args:
            game: Game instance to repair
            
        Returns:
            True if repair was successful
        """
        if not game.is_installed():
            logger.error(f"Cannot repair manifest for {game.display_name}: game not installed")
            return False
        
        try:
            # Ensure the manifest has all required fields
            manifest_data = game.to_manifest_dict()
            
            # Add any missing required fields with defaults
            required_fields = {
                'AppName': game.app_name,
                'DisplayName': game.display_name,
                'CatalogNamespace': game.catalog_namespace or 'unknown',
                'CatalogItemId': game.catalog_item_id or 'unknown',
                'AppVersionString': game.app_version or '1.0',
                'InstallLocation': str(game.install_location),
                'ManifestLocation': str(game.manifest_location),
                'StagingLocation': str(game.staging_location),
                'InstallSize': game.install_size or 0,
                'bIsIncompleteInstall': False,
                'LaunchCommand': '',
                'LaunchParameters': '',
                'ManifestHash': '',
                'ManifestFileVersion': '18',
                'AppCategories': [],
                'ChunkDbs': [],
                'CompatibleApps': [],
                'DisplayName': game.display_name,
                'InstallationGuid': '',
                'InstallSessionId': '',
                'PrereqIds': [],
                'StagingLocation': str(game.staging_location),
                'TechnicalType': 'normal',
                'VaultThumbnailUrl': '',
                'VaultTitleText': '',
                'bCanRunOffline': True,
                'bIsApplication': True,
                'bIsExecutable': True,
                'bIsManaged': True,
                'bNeedsValidation': False,
                'bRequiresAuth': True
            }
            
            # Merge with existing data
            for key, value in required_fields.items():
                if key not in manifest_data:
                    manifest_data[key] = value
            
            # Write the repaired manifest
            if game.manifest_path and game.manifest_path.exists():
                # Backup first
                self.backup_manifest(game)
            else:
                # Create a new manifest path
                game.manifest_path = self.scanner.manifest_dir / f"{game.app_name}.item"
            
            with open(game.manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest_data, f, indent=2)
            
            logger.info(f"Repaired manifest for {game.display_name}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to repair manifest for {game.display_name}: {e}")
            return False
    
    def validate_manifest(self, game: Game) -> Dict[str, Any]:
        """Validate a game's manifest file.
        
        Args:
            game: Game instance to validate
            
        Returns:
            Dictionary with validation results
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Check if manifest file exists
        if not game.manifest_path or not game.manifest_path.exists():
            results['valid'] = False
            results['errors'].append("Manifest file does not exist")
            return results
        
        try:
            # Load and parse the manifest
            with open(game.manifest_path, 'r', encoding='utf-8') as f:
                manifest_data = json.load(f)
            
            # Check required fields
            required_fields = ['AppName', 'DisplayName', 'InstallLocation']
            for field in required_fields:
                if field not in manifest_data:
                    results['valid'] = False
                    results['errors'].append(f"Missing required field: {field}")
            
            # Check if install location exists
            if 'InstallLocation' in manifest_data:
                install_path = Path(manifest_data['InstallLocation'])
                if not install_path.exists():
                    results['warnings'].append(f"Install location does not exist: {install_path}")
            
            # Check manifest integrity
            if manifest_data.get('bIsIncompleteInstall', False):
                results['warnings'].append("Installation is marked as incomplete")
            
            if manifest_data.get('bNeedsValidation', False):
                results['warnings'].append("Installation needs validation")
            
        except json.JSONDecodeError as e:
            results['valid'] = False
            results['errors'].append(f"Invalid JSON in manifest: {e}")
        except Exception as e:
            results['valid'] = False
            results['errors'].append(f"Error reading manifest: {e}")
        
        return results
    
    def remove_manifest(self, game: Game) -> bool:
        """Remove a game's manifest file (uninstall from Epic launcher).
        
        Args:
            game: Game instance to remove
            
        Returns:
            True if removal was successful
        """
        if not game.manifest_path or not game.manifest_path.exists():
            logger.warning(f"Manifest for {game.display_name} does not exist")
            return True
        
        # Create backup before removal
        backup_path = self.backup_manifest(game)
        if not backup_path:
            logger.warning("Failed to create backup before removal")
        
        try:
            game.manifest_path.unlink()
            logger.info(f"Removed manifest for {game.display_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to remove manifest for {game.display_name}: {e}")
            return False