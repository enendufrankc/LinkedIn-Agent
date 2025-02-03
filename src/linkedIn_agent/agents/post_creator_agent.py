from crewai import Agent
from src.linkedIn_agent.clients.llm import openai_client
from textwrap import dedent
from src.linkedIn_agent.prompts.prompt_loader import prompt_loader
from config.configuration import Config

openai_llm = openai_client()

config = Config()

def post_creator_agent(user_topic):
    
    POST_CREATOR_PROMPT_PATH = config.POST_CREATOR_PROMPT_PATH
    goal = prompt_loader(POST_CREATOR_PROMPT_PATH, user_topic, "goal")
    backstory = prompt_loader(POST_CREATOR_PROMPT_PATH, user_topic, "backstory")

    # Define the LinkedIn scraper agent
    doppelganger_agent = Agent(
        role="LinkedIn Post Creator",
        goal=goal,
        backstory=dedent(
            backstory
        ),
        verbose=False,
        allow_delegation=False,
        llm=openai_llm
    )
    
    return doppelganger_agent