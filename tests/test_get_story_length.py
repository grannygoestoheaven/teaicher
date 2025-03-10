import pytest
from src.fetch_spotify_duration import fetch_spotify_duration
from src.fetch_youtube_duration import fetch_youtube_duration
from src.services.get_story_length import spotify_story_length, youtube_story_length

@pytest.mark.parametrize("track_duration, wpm, expected", [
    (180, 178, 53400),  # 3 minutes
    (300, 200, 100000), # 5 minutes, higher WPM
    (0, 178, 0)         # Zero duration
])
def test_spotify_story_length(track_duration, wpm, expected):
    assert spotify_story_length(track_duration, wpm) == expected

@pytest.mark.parametrize("video_duration, wpm, expected", [
    (240, 178, 71200),  # 4 minutes
    (600, 150, 75000),  # 10 minutes, lower WPM
    (0, 178, 0)         # Zero duration
])
def test_youtube_story_length(video_duration, wpm, expected):
    assert youtube_story_length(video_duration, wpm) == expected
