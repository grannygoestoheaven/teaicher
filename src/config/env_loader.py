from dotenv import load_dotenv
import os

def env_loader():
    load_dotenv()
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "SPOTIFY_CLIENT_ID": os.getenv("SPOTIFY_CLIENT_ID")
    }
