from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent
from src.linkedIn_agent.clients.llm import openai_client
from textwrap import dedent
from src.linkedIn_agent.prompts.prompt_loader import prompt_loader
from config.configuration import Config

config = Config()

scrape_website_tool = ScrapeWebsiteTool()
search_tool = SerperDevTool()


openai_llm = openai_client()

def web_researcher_agent(user_topic):
    
    WEB_SCRAPER_PROMPT_PATH = config.WEB_SCRAPER_PROMPT_PATH
    goal = prompt_loader(WEB_SCRAPER_PROMPT_PATH, user_topic, "goal")
    backstory = prompt_loader(WEB_SCRAPER_PROMPT_PATH, user_topic, "backstory")

    # Define the LinkedIn scraper agent
    web_researcher_agent = Agent(
        role="Web Researcher",
        goal= goal,
        tools=[scrape_website_tool, search_tool],
        backstory=dedent(
            backstory
        ),
        verbose=False,
        allow_delegation=False,
        llm=openai_llm
    )
    
    return web_researcher_agent