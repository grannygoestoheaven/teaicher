from dotenv import load_dotenv
import os
import math  # For character-to-token conversion
import openai

load_dotenv()

def generate_story(prompt: str, num_chars: int) -> str:
    tokens_to_use = math.ceil(num_chars / 4)  # 1 token ≈ 4 characters
    
    openai.api_key = os.environ["OPENAI_API_KEY"]
    client = openai.Client()  # Initialize the client
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=tokens_to_use
    )

    story = response.choices[0].message.content.strip()
    return story
