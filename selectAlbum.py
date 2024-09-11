import random
import json
import os
from datetime import datetime
import mySecrets
from getTop100Albums import get_top_albums  # Assuming your original script is named `main.py`

LOG_FILE = 'selected_albums.json'
ALBUMS_FILE = 'current_top_albums.json'

def load_json_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_json_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def compare_album_lists(old_list, new_list):
    old_names = {album['name']: album for album in old_list}
    new_names = {album['name']: album for album in new_list}
    
    new_albums = [album for name, album in new_names.items() if name not in old_names]
    bumped_albums = [album for name, album in old_names.items() if name not in new_names]
    
    return new_albums, bumped_albums

def update_top_albums(albums_file, new_albums):
    current_albums = load_json_file(albums_file)
    new_albums, bumped_albums = compare_album_lists(current_albums, new_albums)
    
    if new_albums:
        print("New albums added to the top 100:")
        for album in new_albums:
            print(f"- {album['artist']['name']} - {album['name']} ({album['playcount']} plays)")
    
    if bumped_albums:
        print("\nAlbums bumped from the top 100:")
        for album in bumped_albums:
            print(f"- {album['artist']['name']} - {album['name']} ({album['playcount']} plays)")
    
    save_json_file(new_albums, albums_file)
    
    return new_albums, bumped_albums

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
    # Fetch the latest top 100 albums from Last.fm
    albums = get_top_albums(mySecrets.USER, mySecrets.API_KEY, 100)
    
    # Update the top albums and print any changes
    new_albums, bumped_albums = update_top_albums(ALBUMS_FILE, albums)
    
    # Load the selected albums
    selected_albums = load_json_file(LOG_FILE)

    # Select and log a random album
    album = select_random_album(albums, [album['name'] for album in selected_albums])
    
    if album:
        selected_album = log_selected_album(album)
        save_json_file(selected_albums + [selected_album], LOG_FILE)
        print(f"\nSelected Album: {selected_album['artist']} - {selected_album['name']} ({selected_album['playcount']} plays)")
    else:
        print("\nNo albums left to select.")