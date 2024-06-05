import nltk
import re

# NLTK download if not already downloaded
nltk.download('punkt')

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello!",
            "hello": "Hi there!",
            "how are you?": "I'm doing fine, thank you!",
            "bye": "Goodbye!",
            "who are you?":"I am a chatbot builded in python",
            "default": "I'm sorry, I didn't understand that."
        }

    def respond(self, message):
        message = message.lower()
        for pattern, response in self.responses.items():
            if re.search(pattern, message):
                return response
        return self.responses["default"]

# Example usage
chatbot = SimpleChatbot()

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
