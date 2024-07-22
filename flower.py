import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
nltk.download('wordnet')

pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"what is your name?", [" my name is  karan kumar chaudhary "]),
    (r"how are you?", ["I'm  fine  i am  engineer student but i am lazy coder but  i love  coding"]),
    (r"what can you do?", [" i make to instagram  automation tool project management "]),
    (r"what is your friend?", ["  my friend name is amin "]),
    (r"what is your old  friend?", ["  my friend name is rambabu "]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Have a great day!"]),

]

reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

chatbot = Chat(pairs, reflections)


def chatbot_interface():
    print("Hi, I'm your chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot_interface()
