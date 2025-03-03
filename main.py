# main.py
import os
from src.spt_track_duration import get_spotify_duration
from src.yt_vid_duration import get_video_details_from_youtube

def main():
    youtube_api_key = os.getenv(YOUTUBE_API_KEY)  # Replace with your YouTube API key
    spotify_client_id = os.getenv(SPOTIFY_CLIENT_ID)  # Replace with your Spotify Client ID
    spotify_client_secret = os.getenv(SPOTIFY_CLIENT_SECRET)  # Replace with your Spotify Client Secret

    # Get the URL input
    service = input("Choose service (YouTube/Spotify): ").strip().lower()
    track_url = input("Enter the track URL: ").strip()

    if service == "youtube":
        video_duration = get_video_details_from_youtube(track_url, api_key)
        if video_duration:
            print(f"The YouTube track video_duration is: {video_duration}")
        else:
            print("Could not retrieve YouTube video video_duration.")
    
    elif service == "spotify":
        track_duration = get_spotify_duration(track_url, spotify_client_id, spotify_client_secret)
        if duration:
            print(f"The Spotify track duration is: {video_duration} seconds")
        else:
            print("Could not retrieve Spotify track video_duration.")
    
    else:
        print("Invalid service selected. Please choose either YouTube or Spotify.")

if __name__ == "__main__":
    main()
