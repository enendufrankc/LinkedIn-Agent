from langchain_mistralai import ChatMistralAI
from langchain_openai import ChatOpenAI

from config.configuration import Config

config = Config()

api_key = config.OPENAI_API_KEY
model = config.DEPLOYMENT
mistral_model = config.MISTRAL_DEPLOYMENT
mistral_api_key = config.MISTRAL_API_KEY

def openai_client():
    openai_llm = ChatOpenAI(
        api_key=api_key, 
        model=model
        )
    return openai_llm


def mistral_client():
    mistral_llm = ChatMistralAI(
        api_key=mistral_api_key, 
        model=mistral_model,
        streaming=True,
        stop=[]
        )
    return mistral_llm