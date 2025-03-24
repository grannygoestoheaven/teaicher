from src.data.fetch_spotify_duration import fetch_spotify_duration
from src.data.fetch_youtube_duration import fetch_youtube_duration

def user_story_length(length, wpm: int = 178) -> int:
    words = (wpm / 60) * (length * 60) # the user will input the length of the track in minutes.
    story_length = words * 5
    return int(story_length)

def spotify_story_length(track_duration: int, wpm: int = 178) -> int:
    words = (wpm / 60) * track_duration  # Words based on WPM and duration
    story_length = words * 5  # Approximate story_length (average word length)
    return int(story_length)

def youtube_story_length(track_duration: int, wpm: int = 178) -> int:
    words = (wpm / 60) * track_duration  # Words based on WPM and duration
    story_length = words * 5  # Approximate story_length (average word length)
    return int(story_length)
