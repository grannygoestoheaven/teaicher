# main.py
import os
from src.data.spt_track_duration import get_spotify_duration
from src.data.yt_vid_duration import get_video_details_from_youtube
from src.utils.estimate_story_length import spotify_story_length
from src.config.env_loader import env_loader

def get_duration(service, track_url):
    if service == "youtube":
        return get_video_details_from_youtube(track_url, os.getenv("YOUTUBE_API_KEY"))
    elif service == "spotify":
        return get_spotify_duration(
            track_url,
            os.getenv("SPOTIFY_CLIENT_ID"),
            os.getenv("SPOTIFY_CLIENT_SECRET")
        )
    return None

def main():
    service = input("Choose service (YouTube/Spotify): ").strip().lower()
    track_url = input("Enter the track URL: ").strip()

    duration = get_duration(service, track_url)
    
    if duration:
        estimated_chars = spotify_story_length(duration)
        print(f"Estimated story length: {estimated_chars} characters")
    else:
        print("Could not retrieve track duration. Please try again.")

if __name__ == "__main__":
    main()
