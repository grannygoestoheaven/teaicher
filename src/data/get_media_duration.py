from src.data.fetch_spotify_duration import fetch_spotify_duration
from src.data.fetch_youtube_duration import fetch_youtube_duration

def extract_service_name(track_url: str) -> str:
    if "spotify.com" in track_url:
        return "spotify"
    elif "youtube.com" in track_url:
        return "youtube"
    else:
        return "unknown"

def get_media_duration(track_url: str) -> int:
    service = extract_service_name(track_url)

    if service == "spotify":
        return fetch_spotify_duration(track_url, client_id, client_secret)
    elif service == "youtube":
        return fetch_youtube_duration(track_url, api_key)
    else:
        raise ValueError("Unsupported URL format.")
