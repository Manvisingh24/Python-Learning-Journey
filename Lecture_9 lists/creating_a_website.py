import streamlit as st

st.title("Welcome to My AI App")
st.header("AI, ML, Automation Demo")

if st.button("Click me!"):
    st.success("You clicked the button!")

name = st.text_input("What is your name?")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age", 0, 100)
st.write("Your age is: ", age)