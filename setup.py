from setuptools import setup, find_packages

setup(
    name="teaicher",
    version="0.1.0",
    author="Morgan Saunier",
    description="An AI storytelling tool",
    packages=find_packages(),
    install_requires=[
    "openai",
    "elevenlabs",
    "TTS",
    "python-vlc",
    "google-api-python-client",
    "spotipy",
    "isodate",
    "torch",
    "huggingface_hub==0.28.1",
    "gradio==5.23.1"
    ],
    extras_require={
    "dev": ["python-dotenv"]
}
)
