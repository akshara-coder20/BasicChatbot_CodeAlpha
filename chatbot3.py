def chatbot():  

    print(" Welcome to Basic Chatbot")
    print("Type 'bye' to exit")

    while True:   

        user = input("\nYou: ").lower()   # Input

        if user == "hello":   
            print("Bot: Hi! Nice to meet you.")   # Output

        elif user == "how are you":   
            print("Bot: I am fine, thank you!")

        elif user == "what is your name":
            print("Bot: My name is ChatBot.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions.")

        elif user == " bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:   
            print("Bot: Sorry, I don't understand that.")

chatbot()   