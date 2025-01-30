from src.linkedIn_agent.tasks.scraper_agent import linkedin_scraper_agent
from crewai import Task
from textwrap import dedent


def linkedin_scraper_task():
    
    scrape_linkedin_task = Task(
        description=dedent(
            "Scrape a LinkedIn profile to get some relevant posts"
        ),
        expected_output=dedent(
            "A list of LinkedIn posts obtained from a LinkedIn profile"
        ),
        agent=linkedin_scraper_agent,
    )
    return scrape_linkedin_task