import streamlit as st

# Title and header
st.title("Welcome to My Python Website")
st.header("Explore Amazing Features")

# Adding some text
st.write("This is a simple Streamlit app built in just 15 minutes!")

# Adding a button
if st.button("Click Me"):
    st.write("Thank you for clicking the button! 😊")

# Adding user input
name = st.text_input("What is your name?")
if st.button("Submit"):
    st.write(f"Hello, {name}! Welcome to my website!")
