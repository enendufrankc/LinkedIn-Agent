from config.configurations import Config

config = Config()

api_key = config.OPENAI_API_KEY
model = config.DEPLOYMENT

def openai_client():
    openai_llm = ChatOpenAI(
        api_key=api_key, 
        model=model
        )
    return openai_llm


def mistral_client():
    mistral_llm = ChatMistralAI(
        api_key=os.environ.get("MISTRAL_API_KEY"), 
        model="mistral-large-latest"
        )
    return mistral_llm