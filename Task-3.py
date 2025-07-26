def chatbot():
    print("🤖 Chatbot: Hello! Type something to chat (type 'bye' to exit).")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! 👋")
            break
        else:
            print("🤖 Chatbot: I don't understand that.")

# --- Run the chatbot ---
chatbot()
