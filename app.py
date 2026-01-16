import streamlit as st

# Configuration dial l-page
st.set_page_config(page_title="The Engineering Lab", page_icon="🚀")

# Sidebar fin ghadi n-zido l-projects
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "AI Project 1"])

if selection == "Home":
    st.title("The Engineering Lab 🚀")
    st.subheader("Welcome to my Portfolio!")
    st.write("I am **Fatima ezzahra Boukhorssa **, an Aspiring AI Engineer.")
    st.write("")

elif selection == "AI Project 1":
    st.title("🌟 AI Project: Name Analyzer")
    st.write("This is a simple interactive project to show how Streamlit works.")
    
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello {name}! You have a great name for an AI Engineer! 💻")
        st.balloons()