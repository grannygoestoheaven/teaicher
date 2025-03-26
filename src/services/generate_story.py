import os
import math  # For character-to-token conversion

from openai import OpenAI  # OpenAI API client
# from mistral import Mistral  # Mistral API client

def generate_story(subject, pattern, story_length: int) -> str:
    tokens_to_use = math.ceil(story_length / 4)  # 1 token ≈ 4 characters
    
    # client = openai.Client()  # Initialize the client
    
    # response = client.chat.completions.create(
    #     model="gpt-4o",
    #     messages=[{"role": "system", "content": prompt}],
    #     max_tokens=tokens_to_use
    # )
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    response = client.responses.create(
        model="gpt-4o",
        instructions=pattern,
        input=subject,
    )
    story = response.output_text
    # story = response.choices[0].message.content.strip()
    return story
