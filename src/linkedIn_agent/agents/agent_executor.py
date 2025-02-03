from crewai import Crew
from src.linkedIn_agent.tasks.scraper_task import scrape_linkedin_task
from src.linkedIn_agent.tasks.create_linkedin_post_task import create_linkedin_post_task
from src.linkedIn_agent.tasks.web_research_task import web_research_task
from src.linkedIn_agent.agents.post_creator_agent import post_creator_agent

from src.linkedIn_agent.agents.scraper_agent import linkedin_scraper_agent
from src.linkedIn_agent.agents.web_researcher_agent import web_researcher_agent



def agent_executor(user_topic):
    
    create_linkedin_task_instance = create_linkedin_post_task(user_topic)
    scrape_task_instance = scrape_linkedin_task(user_topic)
    web_research_task_instance = web_research_task(user_topic)
    doppelganger_agent_instance = post_creator_agent(user_topic)
    linkedin_scraper_agent_instance = linkedin_scraper_agent(user_topic)
    web_researcher_agent_instance = web_researcher_agent(user_topic)
    
    crew = Crew(
        agents=[
            linkedin_scraper_agent_instance,
            web_researcher_agent_instance,
            doppelganger_agent_instance,
        ],
        tasks=[
            scrape_task_instance,
            web_research_task_instance,
            create_linkedin_task_instance,
        ]
    )
    
    
    return crew
