import streamlit as st
import random

st.title("AI-enabled Web Application")
st.write("Welcome to the AI-enabled Web Application deployed using Streamlit Community Cloud.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello, {name}! Your application is running successfully.")
    st.balloons()
    st.write(f"Your name has {len(name)} letters!")
    st.write(random.choice([f"Have a wonderful day, {name}!", f"Keep smiling, {name}!", f"Keep learning and growing, {name}!"]))
    st.image(f"https://cataas.com/cat?random={random.randint(1, 100000)}", caption="Here's a random cat for you! 🐱")
