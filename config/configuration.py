import os

class Config:
    """
    A configuration class that fetches environment variables.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
    LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
    LINKEDIN_PROFILE_NAME = os.getenv("LINKEDIN_PROFILE_NAME")
    
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")