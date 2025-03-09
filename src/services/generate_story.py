import openai
import math  # For character-to-token conversion
import os

from src.config import prompts
from src.services.get_story_length import get_story_length

def generate_story(prompt: str, num_chars: int) -> str:
    tokens_to_use = math.ceil(num_chars / 4)  # 1 token ≈ 4 characters

    openai.api_key = os.environ["OPENAI_API_KEY"]
    response = openai.ChatCompletion.create(  # Correct method for GPT-4o
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=tokens_to_use
    )
    story = response['choices'][0]['message']['content'].strip()
    return story
