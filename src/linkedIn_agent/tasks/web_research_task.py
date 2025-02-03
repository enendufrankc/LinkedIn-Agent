from src.linkedIn_agent.agents.web_researcher_agent import web_researcher_agent
from crewai import Task
from textwrap import dedent
from src.linkedIn_agent.prompts.prompt_loader import prompt_loader
from config.configuration import Config

config = Config()


def web_research_task(user_topic):
    
    WEB_SCRAPER_PROMPT_PATH = config.WEB_SCRAPER_PROMPT_PATH
    description = prompt_loader(WEB_SCRAPER_PROMPT_PATH, user_topic, "description")
    expected_output = prompt_loader(WEB_SCRAPER_PROMPT_PATH, user_topic, "expected_output")
    
    web_researcher_agent_instance = web_researcher_agent(user_topic)
    
    task = Task(
        description=dedent(
            description
        ),
        expected_output=dedent(
            expected_output
        ),
        agent=web_researcher_agent_instance,
    )
    task.async_execution = False
    return task