import vlc
import time
import tempfile

def play_audio_with_sync(track_url: str, speech_file: bytes):
    """
    Plays a track and speech audio in sync, mixing the track at a lower volume.

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

    # Set the track volume lower than speech
    track_player.audio_set_volume(30)  # 0 to 100, lower value for quieter track
    speech_player.audio_set_volume(100)  # 100 is normal volume for speech

    # Start playing the track
    track_player.play()

    # Wait briefly before playing speech to sync audio
    time.sleep(3)  # Adjust delay as needed for sync

    # Start playing the speech
    speech_player.play()
    
    # Wait for the speech to finish and fade out the music
    time.sleep(len(speech_audio) + 3)  # Assuming speech_audio length is the duration of the speech

    # Fade out music (simple volume control, fade out over 3 seconds)
    for volume in range(100, -1, -1):
        player.audio_set_volume(volume)
        time.sleep(0.06)  # Adjust for the fade time

    player.stop()
    speech_player.stop()

    return story, "path/to/speech_audio.mp3"