import os

from dotenv import load_dotenv

load_dotenv()


# YouTube Data API v3
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')

# Optional: RapidAPI for additional trends
RAPIDAPI_KEY = os.environ.get('RAPIDAPI_KEY')
