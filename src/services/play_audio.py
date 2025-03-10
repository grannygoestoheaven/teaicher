import vlc
import tempfile

def play_audio_with_sync(track_url: str, speech_audio: bytes):
    # Save speech to temporary file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as speech_file:
        speech_file.write(speech_audio)
        speech_file_path = speech_file.name

    # Create VLC players
    track_player = vlc.MediaPlayer(track_url)
    speech_player = vlc.MediaPlayer(speech_file_path)

    # Start track, delay speech slightly for sync
    track_player.play()
    time.sleep(3)  # Adjust timing if needed
    speech_player.play()
