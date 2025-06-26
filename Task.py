def chatbot():
    print("Welcome! I am a simple chatbot. Type something to talk (type 'exit' to quit).")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Bot: Hi!")
        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Bot: Goodbye!")
        elif user_input == "exit":
            print("Bot: Chat ended.")
            break
        else:
            print("Bot: I don't understand that.")

# Run the chatbot
chatbot()
