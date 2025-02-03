from src.linkedIn_agent.clients.llm import openai_client


client = openai_client()

def topic_generator(user_topic):
    messages = [
        {"role": "system", "content": f"You're tasked to create a LinkedIn Post title using the {user_topic} provided by the user, the topic should be very catchy and not be more that 60 characters"},
        {"role": "user", "content": f"Create a topic out of: '{user_topic}', make sure the topic is engaging and informative and make sure it is related to the {user_topic}"},
    ]
    
    completion = client.invoke(messages)  # Use invoke() instead of .chat.completions.create()
    
    return completion.content