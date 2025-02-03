from src.linkedIn_agent.agents.scraper_agent import linkedin_scraper_agent
from crewai import Task
from textwrap import dedent
from src.linkedIn_agent.prompts.prompt_loader import prompt_loader
from config.configuration import Config


config = Config()


def scrape_linkedin_task(user_topic):
    
    LINKEDIN_SCRAPER_PROMPT_PATH = config.LINKEDIN_SCRAPER_PROMPT_PATH
    
    description = prompt_loader(LINKEDIN_SCRAPER_PROMPT_PATH, user_topic, "description")
    expected_output = prompt_loader(LINKEDIN_SCRAPER_PROMPT_PATH, user_topic, "expected_output")
    
    linkedin_scraper_agent_instance = linkedin_scraper_agent(user_topic)
    
    task = Task(
        description=dedent(
            "Scrape a LinkedIn profile to get some relevant posts"
            
        ),
        expected_output=dedent(
            "A list of LinkedIn posts obtained from a LinkedIn profile"
        ),
        agent=linkedin_scraper_agent_instance,
    )
    task.async_execution = False
    return task