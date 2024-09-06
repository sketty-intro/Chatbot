# Simple chatbot using if-else statements

def chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()  # Convert the input to lowercase for case-insensitive matching
        
        # Exit condition
        if 'bye' in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Greeting response
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I assist you?")
        
        # How are you response
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I'm doing well! How about you?")
        
        # Responding to user being fine
        elif 'i am fine' in user_input or 'i am good' in user_input:
            print("Chatbot: That's great to hear!")

        # Asking for name
        elif 'your name' in user_input:
            print("Chatbot: My name is Chatbot, and I'm here to assist you!")
        
        # Asking about time
        elif 'time' in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime('%H:%M')
            print(f"Chatbot: The current time is {current_time}.")
        
        # Weather inquiry (sample response)
        elif 'weather' in user_input:
            print("Chatbot: I can't check the weather right now, but you can try a weather app!")
        
        # General fallback response
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you please ask something else?")

# Run the chatbot
chatbot()
