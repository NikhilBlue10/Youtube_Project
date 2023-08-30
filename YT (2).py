import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image
import pymongo  # Import pymongo library
import mysql.connector  # Import mysql.connector module
from googleapiclient.discovery import build

# SETTING PAGE CONFIGURATIONS
icon = Image.open("C:\\Users\\Nikhil\\Desktop\\Youtube_logo.png")
st.set_page_config(
    page_title="Youtube Data Harvesting and Warehousing | By Nikhil Kumar",
    page_icon=icon,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': """# This app is created by *Nikhil Kumar!*"""}
)

# CREATING OPTION MENU (Replace with st.selectbox)
with st.sidebar:
    options = ["Home", "Extract & Transform", "View"]
    selected = st.selectbox("Select an option:", options)

# Bridging a connection with MongoDB Atlas and Creating a new database(youtube_data)
client = pymongo.MongoClient("your unique client id")
db = client.youtube_data

# CONNECTING WITH MYSQL DATABASE
# CONNECTING WITH MYSQL DATABASE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chelseaa",
    database="youtube_db"
)
mycursor = mydb.cursor(buffered=True)


# BUILDING CONNECTION WITH YOUTUBE API
api_key = "AIzaSyDFJmvSNNs7LpZ1JNWln1if8DIrBzdAgeQ"
youtube = build('youtube', 'v3', developerKey=api_key)