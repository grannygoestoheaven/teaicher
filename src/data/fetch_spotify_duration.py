import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException  # Specific error for API issues

def fetch_spotify_duration(track_url: str, client_id: str, client_secret: str) -> int:
    """
    Get the duration of a Spotify track in seconds.
    """
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret
        ))

        track_id = track_url.split('/')[-1].split('?')[0]
        track = sp.track(track_id)

        # Handle missing or unexpected data
        if 'duration_ms' not in track:
            print("Track duration not found in response.")
            return None

        return track['duration_ms'] // 1000  # Return duration in seconds

    except SpotifyException as e:
        print(f"Spotify API error: {e}")
    except IndexError:
        print("Invalid Spotify URL format.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None
