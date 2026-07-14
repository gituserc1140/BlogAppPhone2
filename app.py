import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("Streamlit Blog App")

# Sidebar for API key input
api_key = st.sidebar.text_input("Enter your API Key (e.g., Cohere)", type="password")

# Blog title and content input
title = st.text_input("Blog Title")
content = st.text_area("Write your blog here", height=300)

# Save blog button
if st.button("Publish Blog"):
    if not api_key:
        st.error("Please enter your API Key.")
    else:
        # Here you can integrate API calls using the provided API key
        st.success(f"Blog published successfully! Title: {title}")

# Display saved blogs (placeholder)
st.subheader("Published Blogs")
st.write("(This section will display previously published blogs)")