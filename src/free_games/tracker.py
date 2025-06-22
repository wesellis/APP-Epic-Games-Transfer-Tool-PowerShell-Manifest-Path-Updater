"""Free games tracker for Epic Games Store"""

import json
import urllib.request
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class FreeGamesTracker:
    """Tracks and notifies about free games on Epic Games Store"""
    
    def __init__(self):
        # This would normally use Epic's API, but for demo purposes we'll use mock data
        self.api_url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
        self.cached_games = []
        self.last_check = None
        
    def get_current_free(self) -> List[Dict[str, any]]:
        """Get currently free games"""
        # In a real implementation, this would fetch from Epic's API
        # For now, return mock data
        mock_games = [
            {
                'title': 'Example Game 1',
                'description': 'An amazing adventure game',
                'original_price': '$29.99',
                'end_date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
                'store_url': 'https://store.epicgames.com/en-US/p/example-game-1',
                'image_url': 'https://example.com/game1.jpg'
            },
            {
                'title': 'Example Game 2',
                'description': 'A thrilling action game',
                'original_price': '$19.99',
                'end_date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
                'store_url': 'https://store.epicgames.com/en-US/p/example-game-2',
                'image_url': 'https://example.com/game2.jpg'
            }
        ]
        
        self.cached_games = mock_games
        self.last_check = datetime.now()
        return mock_games
    
    def get_upcoming_free(self) -> List[Dict[str, any]]:
        """Get upcoming free games"""
        # Mock data for upcoming games
        upcoming = [
            {
                'title': 'Future Game 1',
                'description': 'Coming next week',
                'original_price': '$39.99',
                'start_date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
                'image_url': 'https://example.com/future1.jpg'
            }
        ]
        return upcoming
    
    def check_for_new_games(self) -> List[Dict[str, any]]:
        """Check if there are new free games since last check"""
        current_games = self.get_current_free()
        
        # In a real implementation, compare with previously seen games
        # For now, just return current games if it's been more than an hour
        if self.last_check and (datetime.now() - self.last_check).seconds < 3600:
            return []
        
        return current_games
    
    def format_notification(self, games: List[Dict[str, any]]) -> str:
        """Format games list for notification"""
        if not games:
            return "No free games available right now."
        
        lines = ["🎮 Free Games on Epic Games Store:\n"]
        for game in games:
            lines.append(f"• {game['title']} (worth {game['original_price']})")
            lines.append(f"  Available until: {game['end_date']}")
            lines.append(f"  {game['store_url']}\n")
        
        return '\n'.join(lines)
    
    def should_notify(self, game: Dict[str, any]) -> bool:
        """Check if we should notify about this game"""
        # Notify if game ends within 24 hours
        try:
            end_date = datetime.strptime(game['end_date'], '%Y-%m-%d')
            hours_left = (end_date - datetime.now()).total_seconds() / 3600
            return hours_left <= 24 and hours_left > 0
        except:
            return False
    
    def get_games_ending_soon(self) -> List[Dict[str, any]]:
        """Get games that are ending soon"""
        current_games = self.get_current_free()
        return [game for game in current_games if self.should_notify(game)]