import os
from constants import openai_key
from langchain.llms import OpenAI
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

st.title("Langchain Search application using OPENAI api")
input_text=st.text_input("Search the topic you want")

os.environ["OPENAI_API_KEY"]=openai_key

first_input_prompt=PromptTemplate(

input_variables=["name"],
template="Tell me about {name}"
)

person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')


llm=OpenAI(temprature=0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key="person",memory=person_memory)

second_input_prompt=PromptTemplate(

input_variables=["person"],
template="when was  {person} born?"
)
chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key="dob",memory=dob_memory)

third_input_prompt=PromptTemplate(

input_variables=["dob"],
template="Mention 5 specefic major events happens around that specefic {dob}"
)
chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key="description",memory=descr_memory)



parent_chain=SequentialChain(chains=[chain,chain2,chain3],input_variables=["name"],output_variables=["person","dob","description"],verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(descr_memory.buffer)