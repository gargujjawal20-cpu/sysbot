import os
import datetime
from dotenv import load_dotenv

# Import LangChain components
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from system_info import (get_cpu_info, get_memory_info, get_battery_info, get_network_info)

# Load environment variables
load_dotenv()

# --- 1. Define the LangChain Components ---

# Initialize the LLM (Large Language Model)
# This is the LangChain wrapper for the Gemini model.
llm = ChatGoogleGenerativeAI(model="gemini-pro-latest")

# Create a Prompt Template
# This replaces the f-string. Variables are enclosed in {}.
template = """
You are a helpful assistant that answers questions about the user's system status.
Provide clear, concise answers based ONLY on the real-time information provided below.

Current System Status:
- CPU Info: {cpu_info}
- Memory Info: {memory_info}
- Battery Info: {battery_info}
- Network Info: {network_info}
- Current Time: {current_time}

Now, please answer the following user question:
User Question: {user_question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Create a simple Output Parser to get the string output
output_parser = StrOutputParser()

# --- 2. Chain the components together using LangChain Expression Language (LCEL) ---
# The '|' (pipe) operator links the components in a sequence.
chain = prompt | llm | output_parser

def ask_llm_langchain(user_input):
    """
    Answers a user's question by invoking the LangChain chain.
    """
    # Get the current time dynamically
    now = datetime.datetime.now()
    current_time_str = now.strftime("%A, %B %d, %Y at %I:%M %p %Z")

    # Prepare the input dictionary for the chain
    # The keys MUST match the variable names in the prompt template.
    chain_input = {
        "cpu_info": get_cpu_info(),
        "memory_info": get_memory_info(),
        "battery_info": get_battery_info(),
        "network_info": get_network_info(),
        "current_time": current_time_str,
        "user_question": user_input
    }
    
    # Invoke the chain with the dynamic data
    response = chain.invoke(chain_input)
    return response