import os
from dotenv import load_dotenv
import google.generativeai as genai
import datetime  # Added for getting the current time

# Assuming system_info.py is a local file with these functions
from system_info import (get_cpu_info, get_memory_info, get_battery_info, get_network_info)

# Load environment variables from a .env file
load_dotenv()

# Configure the Gemini API key
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except Exception as e:
    print(f"Error configuring Gemini API: {e}")
    print("Please ensure your GOOGLE_API_KEY is set correctly in your .env file.")
    exit()

def ask_llm_gemini(user_input):
    """
    Answers a user's question about system status using the Gemini API.
    """
    # --- FIX: Get the current time dynamically ---
    # This creates a formatted string like "Wednesday, October 01, 2025 at 11:29 AM IST"
    now = datetime.datetime.now()
    current_time_str = now.strftime("%A, %B %d, %Y at %I:%M %p %Z")

    # Create the context string with live, up-to-date information
    context = f"""
    You are a helpful assistant that answers questions about the user's system status.
    Provide clear, concise answers based ONLY on the real-time information provided below.
    Do not make up information if it is not present in the status data.

    Current System Status:
    - CPU Info: {get_cpu_info()}
    - Memory Info: {get_memory_info()}
    - Battery Info: {get_battery_info()}
    - Network Info: {get_network_info()}
    - Current Time: {current_time_str} 
    """

    # Initialize the Gemini model
    model = genai.GenerativeModel(
        model_name='gemini-pro-latest', # This is a great choice for this task
        system_instruction=context
    )

    # Send the user's query to the model
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"An error occurred while communicating with the Gemini API: {e}"

# --- Example Usage ---
if __name__ == "__main__":
    print("System Assistant Initialized. Ask me about your system status.")
    print("Type 'exit' to quit.")

    while True:
        user_question = input("> ")
        if user_question.lower() == 'exit':
            break
        
        answer = ask_llm_gemini(user_question)
        print(f"\nAssistant: {answer}\n")