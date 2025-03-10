import openai

def text_to_speech(story: str) -> bytes:
    response = openai.Audio.create(
        model="tts-1",
        input=story,
        voice="alloy"
    )

    return response['audio']