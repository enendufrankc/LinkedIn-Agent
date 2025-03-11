import streamlit as st
from src.linkedIn_agent.agents.agent_executor import agent_executor
from src.linkedIn_agent.tools.linkedIn_poster import LinkedinAutomate
from config.configuration import Config
from src.linkedIn_agent.agents.topic_generator_agent import topic_generator
import sys
import streamlit as st

def main():
    st.title("LinkedIn Post Generator")
    st.write("Generate and post LinkedIn content with ease.")

    # Initialize configuration and access token
    config = Config()
    access_token = config.ACCESS_TOKEN

    # 1. User enters a topic
    user_topic = st.text_input("Enter your topic")

    # 2. Generate the post content
    if st.button("Generate Post"):
        if not user_topic.strip():
            st.warning("Please enter a topic before generating the post.")
        else:
            with st.spinner("Generating content..."):
                # Generate topic
                topic = topic_generator(user_topic)

                # Get the content using your agent
                crew = agent_executor(user_topic)
                result = crew.kickoff()

            # Store the generated data in session state
            st.session_state["topic"] = topic
            st.session_state["result"] = result

    # 3. If content is generated, display the editable fields
    if "topic" in st.session_state and "result" in st.session_state:
        st.subheader("Generated Topic")
        edited_topic = st.text_input("Edit topic (if needed)",
                                     value=st.session_state["topic"])
        
        st.subheader("Generated Post Content")
        edited_result = st.text_area("Edit post content (if needed)",
                                     value=st.session_state["result"],
                                     height=200)

        # 4. Post the edited content to LinkedIn
        if st.button("Post to LinkedIn"):
            with st.spinner("Posting your content to LinkedIn..."):
                post_content = LinkedinAutomate(
                    access_token=access_token,
                    topic=edited_topic,
                    description=edited_result
                )
                success = post_content.main_func()
            
                if success:
                    st.success("Post successfully published to LinkedIn!")
                else:
                    st.error("Failed to publish post to LinkedIn. Please check logs or configurations.")

if __name__ == "__main__":
    main()
