import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    A configuration class that fetches environment variables.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    MISTRAL_DEPLOYMENT = os.getenv("MISTRAL_DEPLOYMENT")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
    LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
    LINKEDIN_PROFILE_NAME = os.getenv("LINKEDIN_PROFILE_NAME")
    DEPLOYMENT = os.getenv("DEPLOYMENT")
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    LINKEDIN_SCRAPER_PROMPT_PATH = os.getenv("LINKEDIN_SCRAPER_PROMPT_PATH")
    POST_CREATOR_PROMPT_PATH = os.getenv("POST_CREATOR_PROMPT_PATH")
    WEB_SCRAPER_PROMPT_PATH = os.getenv("WEB_SCRAPER_PROMPT_PATH")