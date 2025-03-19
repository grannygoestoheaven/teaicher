import openai
import os

def text_to_speech(story: str, filename: str = "story.mp3") -> None:
    # Set the path to save audio in the static/audio folder
    static_audio_path = os.path.join('static', 'audio', filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(static_audio_path), exist_ok=True)

    # Get audio response from OpenAI
    response = openai.Completion.create(
        model="tts-1",
        input=story,
        voice="alloy",
        response_format="mp3"
    )

    # Save the audio file in the specified location
    with open(static_audio_path, 'wb') as speech_file:
        audio_file.write(response['audio'])