"""Download queue management for Epic Games"""

import json
import os
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DownloadItem:
    """Represents a game download in the queue"""
    game_id: str
    game_name: str
    size_bytes: int
    priority: int = 0
    added_at: datetime = None
    status: str = 'pending'  # pending, downloading, paused, completed, failed
    
    def __post_init__(self):
        if self.added_at is None:
            self.added_at = datetime.now()

class DownloadQueueManager:
    """Manages download queue for Epic Games"""
    
    def __init__(self):
        self.queue: List[DownloadItem] = []
        self.queue_file = Path.home() / '.epic-games-manager' / 'download_queue.json'
        self.queue_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_queue()
    
    def _load_queue(self):
        """Load queue from persistent storage"""
        if self.queue_file.exists():
            try:
                with open(self.queue_file, 'r') as f:
                    data = json.load(f)
                    self.queue = [DownloadItem(**item) for item in data]
            except Exception as e:
                print(f"Failed to load queue: {e}")
                self.queue = []
    
    def _save_queue(self):
        """Save queue to persistent storage"""
        try:
            data = []
            for item in self.queue:
                item_dict = {
                    'game_id': item.game_id,
                    'game_name': item.game_name,
                    'size_bytes': item.size_bytes,
                    'priority': item.priority,
                    'added_at': item.added_at.isoformat(),
                    'status': item.status
                }
                data.append(item_dict)
            
            with open(self.queue_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Failed to save queue: {e}")
    
    def add_to_queue(self, game_id: str, game_name: str, size_bytes: int, priority: int = 0):
        """Add a game to the download queue"""
        # Check if already in queue
        if any(item.game_id == game_id for item in self.queue):
            print(f"{game_name} is already in the queue")
            return False
        
        item = DownloadItem(
            game_id=game_id,
            game_name=game_name,
            size_bytes=size_bytes,
            priority=priority
        )
        
        self.queue.append(item)
        self._sort_queue()
        self._save_queue()
        print(f"Added {game_name} to download queue")
        return True
    
    def remove_from_queue(self, game_id: str):
        """Remove a game from the queue"""
        self.queue = [item for item in self.queue if item.game_id != game_id]
        self._save_queue()
    
    def _sort_queue(self):
        """Sort queue by priority and added time"""
        self.queue.sort(key=lambda x: (-x.priority, x.added_at))
    
    def get_next_download(self) -> Optional[DownloadItem]:
        """Get the next item to download"""
        for item in self.queue:
            if item.status == 'pending':
                return item
        return None
    
    def update_status(self, game_id: str, status: str):
        """Update the status of a download"""
        for item in self.queue:
            if item.game_id == game_id:
                item.status = status
                self._save_queue()
                break
    
    def get_queue_info(self) -> Dict[str, any]:
        """Get information about the queue"""
        total_size = sum(item.size_bytes for item in self.queue if item.status != 'completed')
        pending = sum(1 for item in self.queue if item.status == 'pending')
        downloading = sum(1 for item in self.queue if item.status == 'downloading')
        completed = sum(1 for item in self.queue if item.status == 'completed')
        
        return {
            'total_items': len(self.queue),
            'pending': pending,
            'downloading': downloading,
            'completed': completed,
            'total_size_gb': total_size / (1024**3),
            'items': self.queue
        }
    
    def clear_completed(self):
        """Remove completed downloads from queue"""
        self.queue = [item for item in self.queue if item.status != 'completed']
        self._save_queue()
    
    def prioritize_game(self, game_id: str):
        """Move a game to the top of the queue"""
        for item in self.queue:
            if item.game_id == game_id:
                item.priority = 999
                self._sort_queue()
                self._save_queue()
                break