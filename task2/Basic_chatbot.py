import re
import random
import datetime

# Global variable to store user's name
user_name = ""

def play_rps():
    options = ["rock", "paper", "scissors"]
    bot_choice = random.choice(options)
    user_choice = input("Choose rock, paper or scissors: ").lower()

    if user_choice not in options:
        return "That's not a valid choice."

    if user_choice == bot_choice:
        return f"I chose {bot_choice}. It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "paper" and bot_choice == "rock") or \
         (user_choice == "scissors" and bot_choice == "paper"):
        return f"I chose {bot_choice}. You win!"
    else:
        return f"I chose {bot_choice}. I win!"

def chatbot_response(user_input):
    global user_name
    user_input = user_input.lower()

    if "my name is" in user_input:
        user_name = user_input.split("my name is")[-1].strip().capitalize()
        return f"Nice to meet you, {user_name}!"

    elif "what's my name" in user_input and user_name:
        return f"Your name is {user_name}, of course!"

    elif re.search(r"\bhello\b|\bhi\b", user_input):
        return "Hey there!"
    elif "how are you" in user_input:
        return "I'm doing great! How about you?"
    elif "name" in user_input:
        return "You can call me PyBot!"
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "what can you do" in user_input:
        return "I can chat, tell jokes, play games, and even remember your name!"
    elif "which game" in user_input:
        return "rock paper scissors"
    elif "play rock paper scissors" in user_input:
        return play_rps()
    elif "time" in user_input:
        return f"The time now is {datetime.datetime.now().strftime('%H:%M')}"
    elif "date" in user_input:
        return f"Today is {datetime.datetime.now().strftime('%A, %d %B %Y')}"
    elif "i'm sad" in user_input or "i feel down" in user_input:
        return "I'm here for you. Want to talk about it?"
    elif "i'm happy" in user_input or "i feel great" in user_input:
        return "That’s awesome! Tell me what made your day!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Hmm, I'm still learning. Try saying something else!"

def chat():
    print("Welcome to PyBot 🤖 (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

chat()
