import random

#Simple chat program
#Responds randomly with an arrary of programmed responses 
#Has multiple topics to choose from

def generate_topic():
  topics = [
    "How many siblings do you have?",
    "How many pets do you have?",
    "What kind of music do you listen to?",
    "What's your favorite color?",
    "What's your favorite song?",
    "What's you favorite band?",
    "What's your favorite movie?",
    "What's your favorite movie genre?",
    "Do you play any instruments? If so then what?",
    "If you could go anywhere for vacation where would it be?",
    "If you could live anywhere, where would it be?",
    "Do you have a job?",
    "If you do you work, what kind of job?",
    "What grade are you in?",
    "How old are you?",
    "who's your favorite actor?",
    "What's your dream job?",
    "Is there anyone you look up to?",
    "What makes you happy?",
    "What do you do during your free time?",
    "Do you have any hobbies?",
    "Do you play any games? If so what console?",
    "If you play games, what's your favorite genre of games?"
  ]
  return random.choice(topics)

def generate_response(user_input):
  responses = [
    "Oh wow!",
    "No way!",
    "That's crazy!",
    "That's really interesting.",
    "That's awesome!",
    "Oh really?",
    "Same here.",
    "That's really sweet."
  ]
  return random.choice(responses) + "\n" + random.choice(generate_topic())

def init_chat():
  quit_character = 'q'

  user_input = input(f"Nice to meetcha! I'd like to get to know you better.{generate_topic()}\n")


  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_response(user_input) + "\n")
  

if __name__ == "__main__":
  init_chat()