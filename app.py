import os
import streamlit as st
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apikey

st.title("P5 script generator")
prompt = st.text_input("what do you want the script to draw?")

prompt_template = PromptTemplate(
        input_variables= ['topic'],
        template='Please write me a prompt which will allow me to then create a P5.js script of {topic} without preload items and by using all the capabilities of P5.js, there should be no comments in the script and it should be as consice as possible'
        )



llm = OpenAI(temperature=0.9)
prompt_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True, output_key='gen_prompt')

if prompt:
    response = prompt_chain.run(topic=prompt)
    st.write(response)
