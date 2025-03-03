# main.py

from src.spt_track_duration import get_spotify_duration
from src.yt_vid_duration import get_video_details_from_youtube

def main():
    api_key = 'YOUR_YOUTUBE_API_KEY'  # Replace with your YouTube API key
    spotify_client_id = 'YOUR_SPOTIFY_CLIENT_ID'  # Replace with your Spotify Client ID
    spotify_client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'  # Replace with your Spotify Client Secret

    # Get the URL input
    service = input("Choose service (YouTube/Spotify): ").strip().lower()
    track_url = input("Enter the track URL: ").strip()

    if service == "youtube":
        duration = get_video_details_from_youtube(track_url, api_key)
        if duration:
            print(f"The YouTube track duration is: {duration}")
        else:
            print("Could not retrieve YouTube video duration.")
    
    elif service == "spotify":
        duration = get_spotify_duration(track_url, spotify_client_id, spotify_client_secret)
        if duration:
            print(f"The Spotify track duration is: {duration} seconds")
        else:
            print("Could not retrieve Spotify track duration.")
    
    else:
        print("Invalid service selected. Please choose either YouTube or Spotify.")

if __name__ == "__main__":
    main()
