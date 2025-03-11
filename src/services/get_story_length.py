from src.data.fetch_spotify_duration import fetch_spotify_duration
from src.data.fetch_youtube_duration import fetch_youtube_duration

def spotify_story_length(track_duration: int, wpm: int = 178) -> int:
    words = (wpm / 60) * track_duration  # Words based on WPM and duration
    nb_of_characters = words * 5  # Approximate nb_of_characters (average word length)
    return int(nb_of_characters)

def youtube_story_length(track_duration: int, wpm: int = 178) -> int:
    words = (wpm / 60) * track_duration  # Words based on WPM and duration
    nb_of_characters = words * 5  # Approximate nb_of_characters (average word length)
    return int(nb_of_characters)
