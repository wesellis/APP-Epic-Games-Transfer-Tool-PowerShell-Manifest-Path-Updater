"""License validation for Epic Games Manager"""

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

class LicenseValidator:
    """Handles license validation and tier management"""
    
    def __init__(self):
        self.config_dir = self._get_config_dir()
        self.license_file = self.config_dir / "license.json"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
    def _get_config_dir(self) -> Path:
        """Get platform-specific config directory"""
        if os.name == 'nt':  # Windows
            base = Path(os.environ.get('APPDATA', ''))
        else:  # macOS/Linux
            base = Path.home() / '.config'
        return base / 'epic-games-manager'
        
    def get_tier(self) -> str:
        """Get current license tier"""
        license_data = self._load_license()
        if not license_data:
            return "free"
            
        # Validate license is still valid
        if self._validate_license_data(license_data):
            return license_data.get('tier', 'free')
        return "free"
        
    def activate(self, license_key: str) -> Dict[str, Any]:
        """Activate a license key"""
        # Simple offline validation for now
        # In production, this would validate with a server
        
        if not license_key:
            return {'success': False, 'message': 'Invalid license key'}
            
        # Basic validation
        if len(license_key) < 16:
            return {'success': False, 'message': 'License key too short'}
            
        # Generate checksum
        checksum = hashlib.sha256(license_key.encode()).hexdigest()
        
        # Simple tier detection based on key pattern
        if license_key.startswith('EPIC-PRO-'):
            tier = 'pro'
        elif license_key.startswith('EPIC-TEAM-'):
            tier = 'team'
        else:
            return {'success': False, 'message': 'Invalid license format'}
            
        # Save license data
        license_data = {
            'key': license_key,
            'tier': tier,
            'checksum': checksum,
            'activated_at': datetime.now().isoformat(),
            'valid_until': None  # Lifetime license
        }
        
        self._save_license(license_data)
        
        return {
            'success': True,
            'message': f'Successfully activated {tier.upper()} license!',
            'tier': tier
        }
        
    def deactivate(self):
        """Deactivate current license"""
        if self.license_file.exists():
            self.license_file.unlink()
            
    def _load_license(self) -> Optional[Dict[str, Any]]:
        """Load license data from file"""
        if not self.license_file.exists():
            return None
            
        try:
            with open(self.license_file, 'r') as f:
                return json.load(f)
        except:
            return None
            
    def _save_license(self, data: Dict[str, Any]):
        """Save license data to file"""
        with open(self.license_file, 'w') as f:
            json.dump(data, f, indent=2)
            
    def _validate_license_data(self, data: Dict[str, Any]) -> bool:
        """Validate license data integrity"""
        if not data or 'key' not in data or 'checksum' not in data:
            return False
            
        # Verify checksum
        expected_checksum = hashlib.sha256(data['key'].encode()).hexdigest()
        if expected_checksum != data['checksum']:
            return False
            
        # Check expiration if set
        if data.get('valid_until'):
            try:
                expiry = datetime.fromisoformat(data['valid_until'])
                if datetime.now() > expiry:
                    return False
            except:
                return False
                
        return True
        
    def get_features(self, tier: Optional[str] = None) -> Dict[str, bool]:
        """Get available features for a tier"""
        if tier is None:
            tier = self.get_tier()
            
        features = {
            'free': {
                'scan_library': True,
                'repair_single': True,
                'view_free_games': True,
                'basic_backup': True,
                'batch_repair': False,
                'auto_sync': False,
                'cloud_backup': False,
                'automation': False,
                'priority_support': False
            },
            'pro': {
                'scan_library': True,
                'repair_single': True,
                'view_free_games': True,
                'basic_backup': True,
                'batch_repair': True,
                'auto_sync': True,
                'cloud_backup': True,
                'automation': True,
                'priority_support': True
            }
        }
        
        return features.get(tier, features['free'])