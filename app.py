import os
import streamlit as st
from apikey import apikey
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

st.title("P5 script generator")
prompt = st.text_input("what do you want the script to draw?")

llm = OpenAI(temperature=0.9)

if prompt:
    response = llm(prompt)
    st.write(response)
