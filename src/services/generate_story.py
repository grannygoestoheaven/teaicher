from openai import OpenAI  # OpenAI API client
import math  # For character-to-token conversion

def generate_story(subject, pattern, nb_of_characters: int) -> str:
    tokens_to_use = math.ceil(nb_of_characters / 4)  # 1 token ≈ 4 characters
    
    # client = openai.Client()  # Initialize the client
    
    # response = client.chat.completions.create(
    #     model="gpt-4o",
    #     messages=[{"role": "system", "content": prompt}],
    #     max_tokens=tokens_to_use
    # )
    
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    
    response = client.responses.create(
        model="gpt-4o",
        input=pattern,
        max_tokens=tokens_to_use
    )
    story = response.output_text
    # story = response.choices[0].message.content.strip()
    return story
