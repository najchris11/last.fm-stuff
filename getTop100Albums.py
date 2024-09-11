import requests
import mySecrets  # Import the secrets module

LIMIT = 100

def get_top_albums(user, api_key, limit):
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'method': 'user.gettopalbums',
        'user': user,
        'api_key': api_key,
        'format': 'json',
        'limit': limit
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        albums = data['topalbums']['album']
        return albums
    else:
        print(f"Error: {response.status_code}")
        return []

def display_albums(albums):
    for i, album in enumerate(albums, start=1):
        name = album['name']
        artist = album['artist']['name']
        playcount = album['playcount']
        print(f"{i}. {artist} - {name} ({playcount} plays)")

if __name__ == '__main__':
    albums = get_top_albums(mySecrets.USER, mySecrets.API_KEY, LIMIT)
    if albums:
        display_albums(albums)