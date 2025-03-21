from setuptools import setup, find_packages

setup(
    name="a_track_for_a_story",
    version="0.1.0",
    author="Morgan Saunier",
    description="An AI storytelling tool",
    packages=find_packages(),
    install_requires=["openai", "elevenlabs"]
)
