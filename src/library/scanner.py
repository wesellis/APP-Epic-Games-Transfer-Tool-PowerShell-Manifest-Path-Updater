"""Library scanner for finding Epic Games installations."""

import json
import platform
from pathlib import Path
from typing import List, Optional, Dict, Any
import logging

from .game import Game

logger = logging.getLogger(__name__)


class LibraryScanner:
    """Scans for Epic Games installations and manifests."""
    
    def __init__(self):
        """Initialize the library scanner."""
        self.manifest_dir = self._get_manifest_directory()
        self.games: List[Game] = []
    
    @staticmethod
    def _get_manifest_directory() -> Path:
        """Get the Epic Games manifest directory based on the platform.
        
        Returns:
            Path to the manifest directory
            
        Raises:
            NotImplementedError: If platform is not supported
        """
        system = platform.system()
        
        if system == 'Windows':
            return Path('C:/ProgramData/Epic/EpicGamesLauncher/Data/Manifests')
        elif system == 'Darwin':  # macOS
            return Path.home() / 'Library' / 'Application Support' / 'Epic' / 'EpicGamesLauncher' / 'Data' / 'Manifests'
        elif system == 'Linux':
            # Linux path may vary based on Wine/Proton setup
            return Path.home() / '.config' / 'Epic' / 'EpicGamesLauncher' / 'Data' / 'Manifests'
        else:
            raise NotImplementedError(f"Platform {system} is not supported")
    
    def scan_manifests(self) -> List[Game]:
        """Scan the manifest directory for installed games.
        
        Returns:
            List of Game instances found
        """
        self.games = []
        
        if not self.manifest_dir.exists():
            logger.warning(f"Manifest directory does not exist: {self.manifest_dir}")
            return self.games
        
        # Scan for .item files
        for manifest_file in self.manifest_dir.glob("*.item"):
            try:
                game = self._load_manifest(manifest_file)
                if game:
                    self.games.append(game)
                    logger.info(f"Found game: {game.display_name}")
            except Exception as e:
                logger.error(f"Error loading manifest {manifest_file}: {e}")
        
        return self.games
    
    def _load_manifest(self, manifest_path: Path) -> Optional[Game]:
        """Load a single manifest file.
        
        Args:
            manifest_path: Path to the manifest .item file
            
        Returns:
            Game instance or None if loading failed
        """
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest_data = json.load(f)
            
            # Basic validation
            required_fields = ['AppName', 'DisplayName', 'InstallLocation']
            if not all(field in manifest_data for field in required_fields):
                logger.warning(f"Manifest {manifest_path} missing required fields")
                return None
            
            return Game.from_manifest(manifest_data, manifest_path)
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in manifest {manifest_path}: {e}")
        except Exception as e:
            logger.error(f"Error loading manifest {manifest_path}: {e}")
        
        return None
    
    def find_installed_games(self) -> List[Game]:
        """Find games that are actually installed on disk.
        
        Returns:
            List of installed Game instances
        """
        if not self.games:
            self.scan_manifests()
        
        installed_games = [game for game in self.games if game.is_installed()]
        logger.info(f"Found {len(installed_games)} installed games out of {len(self.games)} manifests")
        
        return installed_games
    
    def find_missing_games(self) -> List[Game]:
        """Find games with manifests but missing installations.
        
        Returns:
            List of Game instances with missing installations
        """
        if not self.games:
            self.scan_manifests()
        
        missing_games = [game for game in self.games if not game.is_installed()]
        logger.info(f"Found {len(missing_games)} missing games out of {len(self.games)} manifests")
        
        return missing_games
    
    def find_games_in_directory(self, directory: Path) -> List[Path]:
        """Find potential Epic Games installations in a directory.
        
        Args:
            directory: Directory to search for games
            
        Returns:
            List of paths that appear to be Epic Games installations
        """
        games_found = []
        
        if not directory.exists() or not directory.is_dir():
            logger.warning(f"Directory does not exist or is not a directory: {directory}")
            return games_found
        
        # Look for directories containing .egstore folder (Epic Games marker)
        for item in directory.iterdir():
            if item.is_dir():
                egstore_path = item / '.egstore'
                if egstore_path.exists() and egstore_path.is_dir():
                    games_found.append(item)
                    logger.info(f"Found Epic Games installation: {item}")
        
        return games_found
    
    def get_game_by_name(self, name: str) -> Optional[Game]:
        """Get a game by its display name or app name.
        
        Args:
            name: Display name or app name to search for
            
        Returns:
            Game instance if found, None otherwise
        """
        if not self.games:
            self.scan_manifests()
        
        for game in self.games:
            if game.display_name.lower() == name.lower() or game.app_name.lower() == name.lower():
                return game
        
        return None
    
    def refresh(self) -> List[Game]:
        """Refresh the game list by rescanning manifests.
        
        Returns:
            Updated list of games
        """
        logger.info("Refreshing game library...")
        return self.scan_manifests()