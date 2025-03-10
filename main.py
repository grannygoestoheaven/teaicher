# main.py
import os

from dotenv import load_dotenv

from src.config import prompts
from src.data.get_media_duration import get_media_duration
from src.services.get_story_length import get_story_length
from src.services.generate_story import generate_story
from src.services.text_to_speech import text_to_speech
from src.services.play_audio import play_audio_with_sync

def main():
    # Step 1: User Input
    subject = input("Enter the subject: ")
    track_url = input("Paste the track URL: ")

    # Step 2: Get Media Duration
    duration = get_media_duration(track_url)

    # Step 3: Determine Story Length
    story_length = get_story_length(duration)

    # Step 4: Generate Story
    story = generate_story(subject, story_length)

    # Step 5: Generate Speech
    speech_audio = text_to_speech(story)

    # Step 6: Sync Audio
    play_audio_with_sync(track_url, speech_audio)

if __name__ == "__main__":
    main()
