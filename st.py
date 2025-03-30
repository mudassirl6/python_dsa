import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120)

# Button to display the result
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old.")