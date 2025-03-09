from src.services.generate_story import generate_story

def text_to_speech(generate_story(): str) -> bytes:
    """
    Generate a speech from the given text using the ElevenLabs API.
    Args:
        story(str): The text to convert to speech.
    Returns:
        str: The speech generated from the given text.
    """
    return f"Speech generated from the text: {text}"