import random
import json
import os
from datetime import datetime
import secrets
from getTop100Albums import get_top_albums

LOG_FILE = 'selected_albums.json'

def load_selected_albums(log_file):
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            return json.load(f)
    return []

def save_selected_album(album, log_file):
    selected_albums = load_selected_albums(log_file)
    selected_albums.append(album)
    with open(log_file, 'w') as f:
        json.dump(selected_albums, f, indent=4)

def select_random_album(albums, selected_albums):
    available_albums = [album for album in albums if album['name'] not in selected_albums]
    if not available_albums:
        print("All albums have been selected!")
        return None
    return random.choice(available_albums)

def log_selected_album(album):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return {
        'name': album['name'],
        'artist': album['artist']['name'],
        'playcount': album['playcount'],
        'timestamp': timestamp
    }

if __name__ == '__main__':
    albums = get_top_albums(secrets.USER, secrets.API_KEY, 100)
    selected_albums = load_selected_albums(LOG_FILE)

    album = select_random_album(albums, [album['name'] for album in selected_albums])
    
    if album:
        selected_album = log_selected_album(album)
        save_selected_album(selected_album, LOG_FILE)
        print(f"Selected Album: {selected_album['artist']} - {selected_album['name']} ({selected_album['playcount']} plays)")
    else:
        print("No albums left to select.")