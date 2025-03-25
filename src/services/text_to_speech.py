from openai import OpenAI  # OpenAI API client
from elevenlabs import ElevenLabs # ElevenLabs API client

import os

def openai_text_to_speech(story: str, filename: str = "story.mp3") -> None :
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

def elevenlabs_text_to_speech(story: str, filename: str = "story.mp3") -> None :
    # Set the path to save audio in the static/audio folder
    static_audio_path = os.path.join('static', 'audio', filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(static_audio_path), exist_ok=True)

    # Initialize client
    client = ElevenLabs(api_key=os.environ.get("ELEVENLABS_API_KEY"))

    # Define the text and parameters
    text = story
    voice_id = "YOUR_VOICE_ID"  # Replace with your voice ID
    model_id = "eleven_multilingual_v2"

    # Generate speech
    response = client.text_to_speech.convert(
        voice_id=voice_id,
        text=text,
        model_id=model_id,
        output_format="mp3_22050_32"
    )

    # Save the audio
    with open("output.mp3", "wb") as file:
        file.write(response)
