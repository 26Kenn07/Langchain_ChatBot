#Uncomment to use the OpenAI 
#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


from langchain_community.llms import Ollama


import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

#Uncomment to use the OpenAI 
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


##Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user", "Question: {question}")       
    ]
)

## streamlit framework
st.title('Langchain ChatBot')
input_text = st.text_input("Hi! I am your assistant ask me anything🤓...")

#Uncomment to use the OpenAI 
# openAI LLm
#llm = ChatOpenAI(model="gpt-3.5-turbo")

llm = Ollama(model='llama3')
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
