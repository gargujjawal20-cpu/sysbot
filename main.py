from chatbot import ask_llm_gemini
def main():
    print("Welcome to SysBot. Ask me about your system!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit","quit"]:
            break
        response = ask_llm_gemini(user_input)
        print("SysBot:", response)

if __name__ == "__main__":
    main()