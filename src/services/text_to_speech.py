import openai

def text_to_speech(story: str, filename: str = "story.mp3") -> None:
    response = openai.Audio.create(
        model="tts-1",
        input=story,
        voice="alloy",
        response_format="mp3"
    )
    with open(filename, 'wb') as audio_file:
        audio_file.write(response['audio'])
