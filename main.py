import random

#Simple chat program
#Responds with a question based on the topic given

def generate_topic(user_input):
  if user_input == "Family":
    topic = [
      input("How many pets do you have?"),
      input("How many siblings do you have?")
    ]


  if user_input == "School":
    topic = [
      input("What grade are you in?"),
      input("Do you have a job?"),
      input("What kind of job?"),
      input("where do you work?")
    ]

  if user_input == "Games":
    topic = [
      input("What kind of games do you like to play?"),
      input("What system or console do you play on?"),
      input("How often do you play?")
    ]

  if user_input == "Movies":
    topic = [
      input("What kind of movies do you like?"),
      input("Who's your favorite actor?"),
      input("What's your favorite movie")
    ]

  if user_input == "Music":
    topic = [
      input("What genre of music do you listen to?"),
      input("What's your favorite band?"),
      input("What's your favorite song?")
    ]

  if user_input == "Hobbies":
    topic = [
      input("What kinds of things do you like to do?"),
      input("How long have you been doing it?")
    ]

  return random.choice(topic)
  
def generate_response():
  response = [
    "Oh wow!",
    "That's really interesting",
    "No way! Same here."
  ]
  return random.choice(response) 

def init_chat():
  quit_character = 'q'

  user_input = input("Nice to meetcha, hope things are going well! Pick a topic to talk about. Family, School, Games, Movies, Music, Hobbies.\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input(generate_topic(user_input) + "\n")

if __name__ == "__main__":
  init_chat()