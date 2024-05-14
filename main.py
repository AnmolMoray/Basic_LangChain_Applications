import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st

st.title("Langchain Search application using OPENAI api")
input_text=st.text_input("Search the topic you want")

os.environ["OPENAI_API_KEY"]=openai_key

llm=OpenAI(temprature=0.8)
if input_text:
    st.write(llm(input_text))