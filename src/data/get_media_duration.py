import os
from src.data.spt_track_duration import get_spotify_duration
from src.data.yt_vid_duration import get_video_details_from_youtube

def get_media_duration(service, track_url):
    if service == "youtube":
        return get_video_details_from_youtube(track_url, os.environ["YOUTUBE_API_KEY"])
    elif service == "spotify":
        return get_spotify_duration(
            track_url,
            os.environ["SPOTIFY_CLIENT_ID"],
            os.environ["SPOTIFY_CLIENT_SECRET"]
        )
    return None