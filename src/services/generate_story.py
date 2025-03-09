import openai


def generate_story(prompt: str, max_tokens: int = 500) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text
