"""Game data class for Epic Games."""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any


@dataclass
class Game:
    """Represents an Epic Games installation."""
    
    app_name: str
    display_name: str
    catalog_namespace: str
    catalog_item_id: str
    app_version: str
    install_location: Path
    manifest_location: Path
    staging_location: Path
    install_size: int
    main_game_app_name: Optional[str] = None
    installed_files: Optional[list] = None
    manifest_path: Optional[Path] = None
    
    @classmethod
    def from_manifest(cls, manifest_data: Dict[str, Any], manifest_path: Path) -> 'Game':
        """Create a Game instance from manifest data.
        
        Args:
            manifest_data: Parsed JSON data from the manifest file
            manifest_path: Path to the manifest file
            
        Returns:
            Game instance
        """
        install_location = Path(manifest_data['InstallLocation'])
        
        return cls(
            app_name=manifest_data['AppName'],
            display_name=manifest_data['DisplayName'],
            catalog_namespace=manifest_data['CatalogNamespace'],
            catalog_item_id=manifest_data['CatalogItemId'],
            app_version=manifest_data['AppVersionString'],
            install_location=install_location,
            manifest_location=Path(manifest_data.get('ManifestLocation', install_location / '.egstore')),
            staging_location=Path(manifest_data.get('StagingLocation', install_location / '.egstore' / 'bps')),
            install_size=manifest_data.get('InstallSize', 0),
            main_game_app_name=manifest_data.get('MainGameAppName'),
            installed_files=manifest_data.get('InstalledFiles'),
            manifest_path=manifest_path
        )
    
    def to_manifest_dict(self) -> Dict[str, Any]:
        """Convert Game instance back to manifest dictionary format.
        
        Returns:
            Dictionary in Epic manifest format
        """
        manifest_dict = {
            'AppName': self.app_name,
            'DisplayName': self.display_name,
            'CatalogNamespace': self.catalog_namespace,
            'CatalogItemId': self.catalog_item_id,
            'AppVersionString': self.app_version,
            'InstallLocation': str(self.install_location),
            'ManifestLocation': str(self.manifest_location),
            'StagingLocation': str(self.staging_location),
            'InstallSize': self.install_size
        }
        
        if self.main_game_app_name:
            manifest_dict['MainGameAppName'] = self.main_game_app_name
            
        if self.installed_files:
            manifest_dict['InstalledFiles'] = self.installed_files
            
        return manifest_dict
    
    def is_installed(self) -> bool:
        """Check if the game is actually installed at the specified location.
        
        Returns:
            True if the game directory exists
        """
        return self.install_location.exists() and self.install_location.is_dir()
    
    def get_game_folder_name(self) -> str:
        """Get the folder name of the game installation.
        
        Returns:
            Name of the game folder
        """
        return self.install_location.name
    
    def update_location(self, new_base_path: Path) -> None:
        """Update the game's installation paths to a new location.
        
        Args:
            new_base_path: New base directory for the game
        """
        game_folder = self.get_game_folder_name()
        new_location = new_base_path / game_folder
        
        self.install_location = new_location
        self.manifest_location = new_location / '.egstore'
        self.staging_location = new_location / '.egstore' / 'bps'
    
    def __str__(self) -> str:
        """String representation of the game."""
        return f"{self.display_name} ({self.app_name}) - {self.install_location}"