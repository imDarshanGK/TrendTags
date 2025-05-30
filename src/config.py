import os

from dotenv import load_dotenv

load_dotenv()


# YouTube Data API v3
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')
if not YOUTUBE_API_KEY:
    raise ValueError('Error: YouTube API key is missing from .env file')

# Optional: RapidAPI for additional trends
RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
