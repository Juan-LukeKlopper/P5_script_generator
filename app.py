import os
import streamlit as st
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey

st.title("P5 script generator")
prompt = st.text_input("what do you want the script to draw?")
    
