import os

from dotenv import load_dotenv

from errors import MissingKeyError

load_dotenv()


# YouTube Data API v3
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
if not YOUTUBE_API_KEY:
    raise MissingKeyError(key_name='YouTube API Key')

# Optional: RapidAPI for additional trends
RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
