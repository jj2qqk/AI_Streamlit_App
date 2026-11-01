import streamlit as st
import datetime
import random

# Page Configuration
st.set_page_config(
    page_title="AI Smart Assistant",
    page_icon="🤖",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Application Title
st.title("🤖 AI-Powered Smart Assistant")
st.subheader("Welcome to your Personal AI Web Application!")

st.write(
    "This application demonstrates an interactive AI-enabled "
    "web interface using Streamlit."
)

st.divider()

# User Information
st.header("👤 User Information")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
interest = st.selectbox(
    "Select your area of interest",
    ["Artificial Intelligence", "Machine Learning",
     "Cloud Computing", "Data Science", "Web Development"]
)

if st.button("Submit Details"):
    if name.strip():
        st.success(f"Welcome, {name}!")
        st.write(f"**Age:** {age}")
        st.write(f"**Area of Interest:** {interest}")
    else:
        st.warning("Please enter your name.")

st.divider()

# AI Text Assistant
st.header("💡 AI Text Assistant")

user_input = st.text_area(
    "Enter a question or topic:",
    placeholder="Example: What is Artificial Intelligence?"
)

if st.button("Generate Response"):
    if user_input.strip():
        text = user_input.lower()

        if "artificial intelligence" in text or " ai " in f" {text} ":
            response = (
                "Artificial Intelligence (AI) is a branch of computer "
                "science that enables machines to perform tasks requiring "
                "human intelligence, such as learning, reasoning and "
                "problem-solving."
            )
        elif "machine learning" in text:
            response = (
                "Machine Learning is a subset of AI that enables computers "
                "to learn patterns from data and make predictions without "
                "being explicitly programmed for every task."
            )
        elif "cloud computing" in text:
            response = (
                "Cloud Computing provides computing resources such as "
                "servers, storage and databases over the internet."
            )
        elif "python" in text:
            response = (
                "Python is a high-level programming language widely used "
                "in AI, machine learning, automation and web development."
            )
        else:
            response = (
                "Your query has been successfully processed! This is a "
                "sample response generated using predefined logic. "
                "An actual AI model can be integrated to provide "
                "intelligent responses."
            )

        st.info(response)
    else:
        st.warning("Please enter a question.")

st.divider()

# Application Statistics
st.header("📊 Application Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Platform", "Streamlit")

with col2:
    st.metric("Deployment", "Cloud")

with col3:
    st.metric("Status", "Active 🟢")

# Footer
st.divider()

st.caption(
    "AI-Powered Smart Assistant | Developed using Python and Streamlit"
)

st.caption(
    f"Last accessed: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)
