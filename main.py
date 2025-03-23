# import os

# from dotenv import load_dotenv

# from src.config import prompts
# from src.data.get_media_duration import get_media_duration, extract_service_name
# from src.services.get_story_length import get_story_length
# from src.services.generate_story import generate_story
# from src.services.text_to_speech import text_to_speech
# from src.services.play_audio import play_audio_with_sync

# def main():
#     # Step 0: Load environment variables
#     load_dotenv()
    
#     client_id = os.environ["SPOTIFY_CLIENT_ID"]
#     client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
#     api_key = os.environ["YOUTUBE_API_KEY"]

#     # Step 1: User Input
#     subject = input("Enter the subject: ")
#     track_url = input("Paste the track URL: ")

#     # Step 2: Get Media Duration
#     service = extract_service_name(track_url)  # Added this
#     duration = get_media_duration(track_url, client_id, client_secret, api_key)

#     # Step 3: Determine Story Length
#     story_length = get_story_length(duration)

#     # Step 4: Generate Story
#     story = generate_story(subject, story_length)

#     # Step 5: Generate Speech
#     speech_audio = text_to_speech(story)

#     # Step 6: Sync Audio
#     play_audio_with_sync(track_url, speech_audio)

# if __name__ == "__main__":
#     main()
    
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

from src.config import patterns
from src.data.get_track_duration import get_track_duration, extract_service_name
from src.services.get_story_length import spotify_story_length, youtube_story_length
from src.services.generate_story import generate_story
from src.services.text_to_speech import text_to_speech
from src.services.play_audio import play_audio_with_sync

app = Flask(__name__)

# Load environment variables
load_dotenv()
client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
api_key = os.environ.get("YOUTUBE_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def generate_story_ui():
    subject = request.form['subject']
    length = request.form['length']
    track_url = request.form['track_url']

    # Load the default pattern (first .md file)
    with open('src/patterns/insightful_brief.md', 'r') as file:
        pattern = file.read()  # Default pattern content

    # Step 2: Get Media Duration & story_length (Spotify or YouTube)
    if track_url :
        service = extract_service_name(track_url)
        duration = get_track_duration(track_url, client_id, client_secret, api_key)
        story_length = spotify_story_length(duration) if service == 'spotify' else youtube_story_length(duration)
    else :
        story_length = length

    # Step 4: Generate Story
    story = generate_story(subject, pattern, story_length)

    # Step 5: Generate Speech
    speech_audio = text_to_speech(story)

    # Step 6: Sync Audio
    play_audio_with_sync(track_url, speech_audio)

    return jsonify({"story": story, "audio_link": "path/to/speech_audio.mp3"})  # Adjust path as needed

if __name__ == "__main__":
    app.run(debug=True)
