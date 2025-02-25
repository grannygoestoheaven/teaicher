import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv# Load .env from the parent directory

load_dotenv(dotenv_path='../.env')

def get_spotify_duration(track_url:"https://open.spotify.com/track/4U45aEWtQhrm8A5mxPaFZ7?si=fefed69ae34741c") -> str:
    try:
        # Fetch credentials from environment variables
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        
        # Authenticate with Spotify API
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

        # Extract the track ID from the URL
        track_id = track_url.split('/')[-1].split('?')[0]

        # Get track details
        track = sp.track(track_id)
        duration_ms = track['duration_ms']
        duration_sec = duration_ms / 1000
        return str(duration_sec)

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    track_url = "https://open.spotify.com/track/YOUR_TRACK_ID"
    duration = get_spotify_duration(track_url)
    if duration:
        print(f"Track duration: {duration} seconds")
    else:
        print("Failed to fetch duration.")
