import openai
import math  # For character-to-token conversion

def generate_story(prompt: str, num_chars: int) -> str:
    # Estimate tokens directly from character count
    tokens_to_use = math.ceil(num_chars / 4)  # 1 token ≈ 4 characters

    openai.api_key = os.environ["OPENAI_API_KEY"]
    response = openai.Completion.create(
        model="gpt-4o",
        prompt=prompt,
        max_tokens=tokens_to_use
    )
    return response.choices[0].text

