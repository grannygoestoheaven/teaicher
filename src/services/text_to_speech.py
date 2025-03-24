from openai import OpenAI  # OpenAI API client
import os

def text_to_speech(story: str, filename: str = "story.mp3") -> None :
    # Set the path to save audio in the static/audio folder
    static_audio_path = os.path.join('static', 'audio', filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(static_audio_path), exist_ok=True)
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Create the audio file
    with open(static_audio_path, 'wb') as speech_file:
        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",  # Use the appropriate TTS model
            voice="en_us_male",  # Select the desired voice
            input=story
        )
        speech_file.write(response['data'])  # Write audio data to file

    return static_audio_path

# def text_to_speech(story: str, filename: str = "story.mp3") -> None:
#     # Define the path to save the audio file
#     static_audio_path = Path('static') / 'audio' / filename

#     # Ensure the directory exists
#     static_audio_path.parent.mkdir(parents=True, exist_ok=True)

#     # Create the audio file
#     with open(static_audio_path, 'wb') as speech_file:
#         response = openai.Audio.create(
#             model="gpt-4o-mini-tts",  # Use the appropriate TTS model
#             prompt=story,
#             voice="en_us_male",  # Select the desired voice
#             response_format="mp3"
#         )
#         speech_file.write(response['data'])  # Write audio data to file

#     return static_audio_path