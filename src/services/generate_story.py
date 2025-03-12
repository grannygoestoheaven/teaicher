import openai  # OpenAI API client
import math  # For character-to-token conversion

def generate_story(prompt: str, num_chars: int) -> str:
    tokens_to_use = math.ceil(num_chars / 4)  # 1 token ≈ 4 characters
    client = openai.Client()  # Initialize the client
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=tokens_to_use
    )

    story = response.choices[0].message.content.strip()
    return story
