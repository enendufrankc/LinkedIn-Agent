from src.linkedIn_agent.agents.post_creator_agent import post_creator_agent
from src.linkedIn_agent.tasks.scraper_task import scrape_linkedin_task
from src.linkedIn_agent.tasks.web_research_task import web_research_task
from crewai import Task
from textwrap import dedent
from src.linkedIn_agent.prompts.prompt_loader import prompt_loader
from config.configuration import Config

config = Config()


def create_linkedin_post_task(user_topic):
    POST_CREATOR_PROMPT_PATH = config.POST_CREATOR_PROMPT_PATH
    description = prompt_loader(POST_CREATOR_PROMPT_PATH, user_topic, "description")
    expected_output = prompt_loader(POST_CREATOR_PROMPT_PATH, user_topic, "expected_output")
    
    doppelganger_agent = post_creator_agent(user_topic)
    scrape_task_instance = scrape_linkedin_task(user_topic)
    web_research_task_instance = web_research_task(user_topic)
    
    task = Task(
        description=dedent(
            description
        ),
        expected_output=dedent(
            expected_output
        ),
        agent=doppelganger_agent,
    )
    task.async_execution = False
    task.context = [scrape_task_instance, web_research_task_instance]
    return task
