# streamlit_app.py
import streamlit as st
from datetime import datetime
from crewapp.crew import Crewapp

st.set_page_config(page_title="CrewApp Interface", layout="centered")

# Helper function to run the crew
def run_crew():
    inputs = {
        'topic': st.session_state.topic,
        'current_year': str(datetime.now().year)
    }
    try:
        Crewapp().crew().kickoff(inputs=inputs)
        st.success("Crew executed successfully.")
    except Exception as e:
        st.error(f"Error: {e}")

# Helper function to train the crew
def train_crew(n_iterations, filename):
    inputs = {
        'topic': st.session_state.topic,
        'current_year': str(datetime.now().year)
    }
    try:
        Crewapp().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
        st.success("Crew trained successfully.")
    except Exception as e:
        st.error(f"Error: {e}")

# Helper function to replay the crew
def replay_crew(task_id):
    try:
        Crewapp().crew().replay(task_id=task_id)
        st.success("Replay completed successfully.")
    except Exception as e:
        st.error(f"Error: {e}")

# Helper function to test the crew
def test_crew(n_iterations, eval_llm):
    inputs = {
        'topic': st.session_state.topic,
        'current_year': str(datetime.now().year)
    }
    try:
        Crewapp().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)
        st.success("Test completed successfully.")
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit UI
st.title("🧠 CrewApp Control Panel")

st.text_input("Topic", value="AI LLMs", key="topic")

option = st.selectbox("Choose Operation", ["Run", "Train", "Replay", "Test"])

if option == "Run":
    st.button("Run Crew", on_click=run_crew)

elif option == "Train":
    n_iterations = st.number_input("Number of Iterations", min_value=1, value=5)
    filename = st.text_input("Output Filename", value="training_results.json")
    if st.button("Train Crew"):
        train_crew(n_iterations, filename)

elif option == "Replay":
    task_id = st.text_input("Task ID")
    if st.button("Replay"):
        replay_crew(task_id)

elif option == "Test":
    n_iterations = st.number_input("Number of Test Iterations", min_value=1, value=3)
    eval_llm = st.text_input("Evaluation LLM", value="gpt-4")
    if st.button("Test Crew"):
        test_crew(n_iterations, eval_llm)
