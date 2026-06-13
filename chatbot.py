import os
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# LangSmith Tracing (Optional)
# --------------------------------------------------
if "LANGCHAIN_API_KEY" in st.secrets:
    os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
    os.environ["LANGCHAIN_TRACING_V2"] = "true"

    # Optional: Name your project in LangSmith
    os.environ["LANGCHAIN_PROJECT"] = "streamlit-chatbot"

# --------------------------------------------------
# Groq API Key
# --------------------------------------------------
groq_api_key = st.secrets["GROQ_API_KEY"]

# --------------------------------------------------
# Prompt Template
# --------------------------------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful AI assistant. Answer the user's questions clearly, accurately, and concisely."
    ),
    (
        "user",
        "Question: {question}"
    ),
])

# --------------------------------------------------
# LLM
# --------------------------------------------------
llm = ChatGroq(
    model="qwen/qwen3-32b",
    api_key=groq_api_key
)

# --------------------------------------------------
# Output Parser
# --------------------------------------------------
output_parser = StrOutputParser()

# --------------------------------------------------
# Chain
# --------------------------------------------------
chain = prompt | llm | output_parser

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.title("🤖 My AI Chatbot")

st.write("Ask me anything!")

input_text = st.text_input(
    "Enter your question:",
    placeholder="e.g. What is Agentic AI?"
)

# --------------------------------------------------
# Generate Response
# --------------------------------------------------
if input_text:
    try:
        with st.spinner("Thinking..."):
            response = chain.invoke(
                {"question": input_text}
            )

        st.success("Response generated!")
        st.write(response)

    except Exception as e:
        st.error(f"Error: {e}")