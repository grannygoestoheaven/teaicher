import import openai
import os

def text_to_speech(story: str, filename: str = "story.mp3") -> None:
    # Set the path to save audio in the static/audio folder
    static_audio_path = os.path.join('static', 'audio', filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(static_audio_path), exist_ok=True)
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Get audio response from OpenAI
    response = client.Audio.create(
        model="gpt-4o-mini-tts",  # Choose the appropriate TTS model
        voice="en_us_male",  # Select from available voices
        stream=False  # Set to True for streaming audio
) 
    # Save the audio file in the specified location
    with open(static_audio_path, 'wb') as speech_file:
        audio_file.write(response['audio'])