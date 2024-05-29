import requests

def get_spotify_token(client_id, client_secret):
    """Obtient un token d'accès à l'API Spotify."""
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_spotify_playlist(access_token, playlist_id):
    """Récupère les informations de la playlist Spotify."""
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(playlist_url, headers=headers)
    return response.json()

