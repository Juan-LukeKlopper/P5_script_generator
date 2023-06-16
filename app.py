import os
import streamlit as st
from apikey import apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ['OPENAI_API_KEY'] = apikey

st.title("P5 script generator")
prompt = st.text_input("what do you want the script to draw?")

prompt_template = PromptTemplate(
        input_variables= ['topic'],
        template='Please write me a prompt which will allow me to then create a P5.js script of {topic} without preload items and by using all the capabilities of P5.js, there should be no comments in the script and it should be as consice as possible'
        )


script_template = PromptTemplate(
        input_variables= ['gen_prompt'],
        template='{gen_prompt}'
        )

completer_template = PromptTemplate(
        input_variables= ['script'],
        template=' if the script is incomplete please generate the rest of it, if it is complete return a whitespace. SCRIPT: {script}'
        )



llm = OpenAI(temperature=0.9)
prompt_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True, output_key='gen_prompt')
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
completer_chain = LLMChain(llm=llm, prompt=completer_template, verbose=True, output_key='script_completer')
sequential_chain = SequentialChain(chains=[prompt_chain, script_chain, completer_chain], input_variables=['topic'], output_variables=['gen_prompt','script', 'script_completer'], verbose=True)



if prompt:
    response = sequential_chain({'topic':prompt})
    st.write(response['gen_prompt'])
    st.write(response['script'])
    st.write(response['script_completer'])
