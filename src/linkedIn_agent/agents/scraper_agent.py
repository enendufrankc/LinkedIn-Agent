from src.linkedIn_agent.tools.linkedIn_scraper import scrape_linkedin_posts_tool
from crewai import Agent
from src.linkedIn_agent.clients.llm import openai_client


openai_llm = openai_client()

def linkedin_scraper_agent():

    # Define the LinkedIn scraper agent
    linkedin_scraper_agent = Agent(
        role="LinkedIn Post Scraper",
        goal="Your goal is to scrape a LinkedIn profile to get a list of posts from the given profile",
        tools=[scrape_linkedin_posts_tool],
        backstory=dedent(
            """
            You are an experienced programmer who excels at web scraping.
            """
        ),
        verbose=True,
        allow_delegation=False,
        llm=openai_llm
    )
    
    return linkedin_scraper_agent