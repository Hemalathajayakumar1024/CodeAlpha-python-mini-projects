# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # get input and convert to lowercase
        
        if user_input == "hello":
            print("Chatbot: Hi there!👋🏼 How can i assist you today")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!☺️  How about you?")
        elif user_input in ["hi", "hey"]:
            print("Chatbot: Hello! Nice to meet you☺️")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day ahead!🌟")
            break
        else:
            print("Chatbot: Sorry, I didn't quite understand that🤔-could you please clarify what you meant?")

# Run the chatbot
chatbot()