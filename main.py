from chatbot import ask_llm_langchain
def main():
    print("Welcome to SysBot. Ask me about your system!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit","quit"]:
            break
        response = ask_llm_langchain(user_input)
        print("SysBot:", response)

if __name__ == "__main__":
    main()