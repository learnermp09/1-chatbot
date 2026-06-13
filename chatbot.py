# Import libs
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

# setup environment variables
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# step 1: prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are very good AI assitant. Please respond to the user question"),
    ("user", "question: {question}"),

])

# step 2: llm model
llm = ChatGroq(model = "qwen/qwen3-32b")

# step 3: output parser
output_parser = StrOutputParser()

# chain
# chain = step 1 + step 2 + step 3
chain = prompt | llm | output_parser

# UI
st.title("MY AI CHATBOT")
input_text = st.text_input("Enter your question here")
if input_text:
    st.write(chain.invoke({"question": input_text}))