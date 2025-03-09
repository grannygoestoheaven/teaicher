from googleapiclient.discovery import build
from googleapiclient.errors import HttpErrordef get_youtube_client(api_key: str):
    """
    Initialize and return the YouTube API client.
    """
    return build('youtube', 'v3', developerKey=api_key)


def get_video_details_from_youtube(video_url: str, api_key: str) -> str:
    """
    Get the duration of a YouTube video from its URL.
    :param video_url: The URL of the YouTube video.
    :param api_key: The YouTube API key.
    :return: The video duration in ISO 8601 format.
    """
    try:
        # Extract the video ID from the URL
        video_id = video_url.split('v=')[1].split('&')[0]

        # Initialize YouTube client
        youtube = get_youtube_client(api_key)

        # Get video details
        request = youtube.videos().list(part="contentDetails", id=video_id)
        response = request.execute()

        # Extract and return duration
        duration = response['items'][0]['contentDetails']['duration']
        return duration

    except HttpError as e:
        print(f"An error occurred: {e}")
        return None