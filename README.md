# Youtube_Project
The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels.
import streamlit as st

# Sidebar to enter YouTube channel URLs
st.sidebar.header("YouTube Channel URLs")
channel_urls = st.sidebar.text_area("Enter YouTube channel URLs (one per line)", "")

# Display the entered URLs
if channel_urls:
    channel_list = channel_urls.strip().split("\n")
    st.sidebar.write("Selected Channel URLs:")
    st.sidebar.write(channel_list)

    # Main content area
    st.title("YouTube Channel Analyzer")

    # Display data for each channel
    for channel_url in channel_list:
        st.header(f"Analyzing Channel: {channel_url}")
        
        # Here you can use YouTube API or other libraries to fetch and analyze data from the channel
        
        # For demonstration purposes, let's just display the channel URL
        st.write(f"Channel URL: {channel_url}")
else:
    st.sidebar.write("Enter YouTube channel URLs above to begin.")

