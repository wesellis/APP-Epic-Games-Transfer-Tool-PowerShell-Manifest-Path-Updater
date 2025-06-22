"""Configuration management for Epic Games Manager"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

class Config:
    """Manages application configuration"""
    
    def __init__(self):
        self.config_dir = self._get_config_dir()
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self._config = self._load_config()
        
    def _get_config_dir(self) -> Path:
        """Get platform-specific config directory"""
        if os.name == 'nt':  # Windows
            base = Path(os.environ.get('APPDATA', ''))
        else:  # macOS/Linux
            base = Path.home() / '.config'
        return base / 'epic-games-manager'
        
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                pass
        return self._get_default_config()
        
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            'license_key': '',
            'tier': 'free',
            'auto_backup': True,
            'backup_dir': str(Path.home() / 'EpicGamesBackups'),
            'check_updates': True,
            'theme': 'dark',
            'language': 'en',
            'last_scan': '',
            'manifest_dir': self._get_default_manifest_dir(),
            'game_directories': []
        }
        
    def _get_default_manifest_dir(self) -> str:
        """Get default Epic Games manifest directory"""
        if os.name == 'nt':  # Windows
            return r'C:\ProgramData\Epic\EpicGamesLauncher\Data\Manifests'
        elif os.name == 'posix':
            if 'darwin' in os.sys.platform:  # macOS
                return str(Path.home() / 'Library/Application Support/Epic/EpicGamesLauncher/Data/Manifests')
            else:  # Linux
                return str(Path.home() / '.config/Epic/EpicGamesLauncher/Data/Manifests')
        return ''
        
    def save(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self._config, f, indent=2)
            
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self._config.get(key, default)
        
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self._config[key] = value
        self.save()
        
    def get_backup_dir(self) -> Path:
        """Get backup directory path"""
        return Path(self.get('backup_dir', str(Path.home() / 'EpicGamesBackups')))
        
    def get_manifest_dir(self) -> Path:
        """Get Epic Games manifest directory"""
        return Path(self.get('manifest_dir', self._get_default_manifest_dir()))
        
    def add_game_directory(self, path: str):
        """Add a game directory to scan list"""
        dirs = self.get('game_directories', [])
        if path not in dirs:
            dirs.append(path)
            self.set('game_directories', dirs)
            
    def remove_game_directory(self, path: str):
        """Remove a game directory from scan list"""
        dirs = self.get('game_directories', [])
        if path in dirs:
            dirs.remove(path)
            self.set('game_directories', dirs)