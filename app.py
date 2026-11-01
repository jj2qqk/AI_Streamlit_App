import streamlit as st

st.title("AI-enabled Web Application")
st.write("Welcome to the AI-enabled Web Application deployed using Streamlit Community Cloud.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello, {name}! Your application is running successfully.")
    st.balloons()
    st.write(f"Your name has {len(name)} letters!")
    st.image("https://cataas.com/cat", caption="Here's a random cat for you! 🐱")
