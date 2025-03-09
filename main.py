# main.py
from dotenv import load_dotenv
import os

from src.data.spt_track_duration import get_spotify_duration
from src.data.yt_vid_duration import get_video_details_from_youtube
from src.utils.estimate_story_length import spotify_story_length

load_dotenv()  # Load env variables once

def get_duration(service, track_url):
    if service == "youtube":
        return get_video_details_from_youtube(track_url, os.environ["YOUTUBE_API_KEY"])
    elif service == "spotify":
        return get_spotify_duration(
            track_url,
            os.environ["SPOTIFY_CLIENT_ID"],
            os.environ["SPOTIFY_CLIENT_SECRET"]
        )
    return None

def main():
    env_loader()
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
