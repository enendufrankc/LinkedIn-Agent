from src.linkedIn_agent.agents.agent_executor import agent_executor
from src.linkedIn_agent.tools.linkedIn_poster import LinkedinAutomate
from config.configuration import Config
from src.linkedIn_agent.agents.topic_generator_agent import topic_generator

config = Config()

access_token = config.ACCESS_TOKEN

user_topic = "right a LinkedIn post comparing DeepSeek and OpenAI"
topic = topic_generator(user_topic)

crew = agent_executor(user_topic)


if __name__ == "__main__":
    
    print("Starting the pipeline...")
    result = crew.kickoff()
    post_conternt = LinkedinAutomate(
        access_token=access_token,
        topic=topic,
        description=result
        ).main_func()