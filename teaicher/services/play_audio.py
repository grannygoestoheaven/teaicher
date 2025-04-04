import vlc
import time
import tempfile
# import mutagen.mp3 import MP3

# def play_audio_with_sync(speech_audio: bytes, track_url: str = None) -> tuple:
    # """
    # Plays a track and speech audio in sync, mixing the track at a lower volume.

    # Args:
    # - track_url (str): The URL of the track to play.
    # - speech_audio (bytes): The audio data for speech to play.
    # """
    # # Save speech audio to a temporary file
    # with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as speech_file:
    #     speech_file.write(speech_audio)
    #     speech_file_path = speech_file.name

    # speech_duration = MP3(speech_file_path).info.length
    
    # # Create VLC media players for the track and speech
    # track_player = vlc.MediaPlayer(track_url)
    # speech_player = vlc.MediaPlayer(speech_file_path)

    # # Set the track volume lower than speech
    # track_player.audio_set_volume(30)  # 0 to 100, lower value for quieter track
    # speech_player.audio_set_volume(100)  # 100 is normal volume for speech

    # # Start playing the track
    # track_player.play()

    # # Wait briefly before playing speech to sync audio
    # time.sleep(3)  # Adjust delay as needed for sync

    # # Start playing the speech
    # speech_player.play()
    
    # # Wait for the speech to finish and fade out the music
    # time.sleep(len(speech_duraton) + 3)  # Assuming speech_audio length is the duration of the speech

    # # Fade out music (simple volume control, fade out over 3 seconds)
    # for volume in range(100, -1, -1):
    #     player.audio_set_volume(volume)
    #     time.sleep(0.06)  # Adjust for the fade time

    # player.stop()
    # speech_player.stop()

    # return story, speech_file_path  # Return the story and path to speech audio

def play_audio(speech_audio: bytes) -> None:
    """
    Plays the speech audio.

    Args:
    - speech_audio (bytes): The audio data for speech to play.
    """
    # Save speech audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as speech_file:
        speech_file.write(speech_audio)
        speech_file_path = speech_file.name

    # Create a VLC media player for the speech
    speech_player = vlc.MediaPlayer(speech_file_path)

    # Start playing the speech
    speech_player.play()

    # Wait for the speech to finish
    time.sleep(len(speech_audio) + 3)  # Assuming speech_audio length is the duration of the speech

    speech_player.stop()

    return "path/to/speech_audio.mp3"

def play_audio_with_sync(speech_audio: bytes, track_url: str) -> tuple:
    """
    Plays a track and speech audio in sync, mixing the track at a lower volume.

    Args:
    - track_url (str): The URL or path of the track to play (optional).
    - speech_audio (bytes): The audio data for speech to play.

    Returns:
    - tuple: (original speech bytes, path to speech temp file)
    """
    import tempfile, vlc, time, os

    # Save speech audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as speech_file:
        speech_file.write(speech_audio)
        speech_file_path = speech_file.name

    # Create VLC players
    track_player = vlc.MediaPlayer(track_url)
    track_player.audio_set_volume(30)

    speech_player = vlc.MediaPlayer(speech_file_path)
    speech_player.audio_set_volume(100)

    # Start playback
    track_player.play()
    time.sleep(3)  # adjust for sync delay
    speech_player.play()

    # Wait for speech to finish
    time.sleep(len(speech_audio) / 32000 + 3)  # ~32000 bytes/sec for mp3_22050_32

    # Fade out music
    fade_duration = 6  # seconds
    step_delay = 0.02  # seconds
    steps = int(fade_duration / step_delay)  # = 300 steps

    for i in range(steps):
        volume = int(30 * (1 - i / steps))
        track_player.audio_set_volume(volume)
        time.sleep(step_delay)

    track_player.stop()
    speech_player.stop()

    return speech_audio, speech_file_path
