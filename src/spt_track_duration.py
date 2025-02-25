import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_duration(track_url: str, client_id: str, client_secret: str) -> str:
    """
    Get the duration of a Spotify track from its URL.
    :param track_url: The URL of the Spotify track.
    :param client_id: Your Spotify Client ID.
    :param client_secret: Your Spotify Client Secret.
    :return: The track duration in milliseconds.
    """
    try:
        # Authenticate with Spotify API
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

        # Extract the track ID from the URL
        track_id = track_url.split('/')[-1].split('?')[0]

        # Get track details
        track = sp.track(track_id)
        
        # Extract and return the duration in seconds
        duration_ms = track['duration_ms']  # Duration in milliseconds
        duration_sec = duration_ms / 1000  # Convert to seconds
        return str(duration_sec)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None