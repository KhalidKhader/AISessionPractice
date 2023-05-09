import nltk
nltk.download('punkt')

# Define a dictionary of response patterns
responses = {
    "hi": "Hello!",
    "hello": "Hi there!",
    "how are you": "I'm doing well, thank you!",
    "what's your name": "My name is Chatbot.",
    "bye": "Goodbye!",
    "default": "I'm sorry, I don't understand. Can you please rephrase that?"
}

# Define a function to process user input and generate a response
def chatbot_response(user_input):
    # Tokenize the user input
    tokens = nltk.word_tokenize(user_input.lower())
    # Check if the user input matches any response pattern
    for pattern in responses:
        if pattern in tokens:
            return responses[pattern]
    # If no pattern matches, return the default response
    return responses['default']

# Start the chatbot loop
print("Welcome to Chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot_response(user_input)
    print("Chatbot: " + response)
