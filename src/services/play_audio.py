import vlc
import time
import tempfile

def play_audio_with_sync(track_url: str, speech_audio: bytes):
    """
    Plays a track and speech audio in sync.

    Args:
    - track_url (str): The URL of the track to play.
    - speech_audio (bytes): The audio data for speech to play.
    """
    # Save speech audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as speech_file:
        speech_file.write(speech_audio)
        speech_file_path = speech_file.name

    # Create VLC media players for the track and speech
    track_player = vlc.MediaPlayer(track_url)
    speech_player = vlc.MediaPlayer(speech_file_path)

    # Start playing the track
    track_player.play()

    # Wait briefly before playing speech to sync audio
    time.sleep(3)  # Adjust delay as needed for sync

    # Start playing the speech
    speech_player.play()
