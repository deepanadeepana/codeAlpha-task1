
import nltk
import random
import string

# Download necessary NLTK packages (only first time)
nltk.download('punkt')
nltk.download('wordnet')

from nltk.chat.util import Chat, reflections
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# Sample chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created using NLTK.", "You can call me ChatBuddy!"]
    ],
    [
        r"how are you ?",
        ["I'm just a bunch of code, but I'm doing great!",
         "All good here!How about you?"]

    ],
    [
        r"sorry (.*)",
        ["No problem", "Don't worry about it"]
    ],
    [
        r"(.) thank you (.)",
        ["You're welcome!", "Anytime!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?", "Let's talk about something else!"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
def start_chat():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot.respond(user_input))
start_chat()




