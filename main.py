# main.py
from dotenv import load_dotenv
import os

from src.data.get_media_duration import get_media_duration
from src.services.generate_story import generate_story
from src.services.text_length import spotify_story_length
# from src.data.spt_track_duration import get_spotify_duration
# from src.data.yt_vid_duration import get_video_details_from_youtube
# from src.utils.estimate_story_length import spotify_story_length

load_dotenv() # Load env variables once

def main():
    service = input("Choose service (YouTube/Spotify): ").strip().lower()
    track_url = input("Enter the track URL: ").strip()

    duration = get_media_duration(service, track_url)
    story = generate_story(duration)
    speech = text_to_speech(story)
    
    if duration:
        estimated_chars = spotify_story_length(duration)
        print(f"Estimated story length: {estimated_chars} characters")
    else:
        print("Could not retrieve track duration. Please try again.")

if __name__ == "__main__":
    main()
