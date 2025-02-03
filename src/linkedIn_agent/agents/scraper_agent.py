from src.linkedIn_agent.tools.linkedIn_scraper import scrape_linkedin_posts_tool
from crewai import Agent
from textwrap import dedent
from src.linkedIn_agent.clients.llm import openai_client
from src.linkedIn_agent.prompts.prompt_loader import prompt_loader
from config.configuration import Config


config = Config()

def linkedin_scraper_agent(user_topic):
    
    LINKEDIN_SCRAPER_PROMPT_PATH = config.LINKEDIN_SCRAPER_PROMPT_PATH

    openai_llm = openai_client()

    goal = prompt_loader(LINKEDIN_SCRAPER_PROMPT_PATH, user_topic, "goal")
    backstory = prompt_loader(LINKEDIN_SCRAPER_PROMPT_PATH, user_topic, "backstory")

    # Define the LinkedIn scraper agent
    scraper_agent = Agent(
        role="LinkedIn Post Scraper",
        goal=goal,
        tools=[scrape_linkedin_posts_tool],
        backstory=dedent(
            backstory
        ),
        verbose=False,
        allow_delegation=False,
        llm=openai_llm
    )
    
    return scraper_agent