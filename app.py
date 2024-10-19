import os
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


#prompt 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a generative ai expert , please provide any question"),
        ("user", "Question:{question}")
    ]
)

#streamlit framework

st.title("langchain LLM model using Gemma:2B")
input_text = st.text_input("What is your question ? ")

#llm model
llm=Ollama(model="gemma:2b")
output_parse = StrOutputParser()
chain = prompt|llm|output_parse

if input_text:
    st.write(chain.invoke({"question":input_text}))

