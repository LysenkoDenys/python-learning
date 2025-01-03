    # PLAN:
# 1) generate a number from 1 to 3
# 2) if type anything except for the r/s/p: 
#       print invalid message
# 3) if type r/s/p:: 
#       print message:
  #       print message 'Your choice: r'
  #       print message 'PC choice: s'
  #       print message 'You lose/Win'
  #       print message 'Continue? y/n:'
# 4) if y - restart
# 5) if n - exit


import random

# while True:
#   stuff=['rock', 'scissors', 'paper']
#   random_choice=(stuff[random.randint(0,2)])

#   while True:
#           guess= input(f'Rock, paper or scissors (r/p/s):').strip().lower()
#           if guess=='r' or guess=='p' or guess=='s':
#             if guess=='r':
#               print('Your choice: rock')
#               print(f'PC choice: {random_choice}')
#               if random_choice=='rock':
#                 print('Nobody wins')
#               if random_choice=='scissors':
#                 print('You Win')
#               if random_choice=='paper':
#                 print('You Lose')
#             elif guess=='p':
#               print('Your choice: paper')
#               print(f'PC choice: {random_choice}')
#               if random_choice=='paper':
#                 print('Nobody wins')
#               if random_choice=='scissors':
#                 print('You Lose')
#               if random_choice=='rock':
#                 print('You Win')
#             elif guess=='s':
#               print('Your choice: scissors')
#               print(f'PC choice: {random_choice}')
#               if random_choice=='scissors':
#                 print('Nobody wins')
#               if random_choice=='paper':
#                 print('You Win')
#               if random_choice=='rock':
#                 print('You Lose')
#             break
#           else:
#             print('Invalid choice!')

#   play_again = input("Continue? y/n: ").strip().lower()
#   if play_again != 'y':
#     print(f"Thanks for playing!")
#     break

# =========================================
# mosh:
# Ask the user to make a choice
# If choice is not valid
#   Print an error
# Let the computer to make a choice
# Print choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
#   Terminate 

ROCK='r'
SCISSORS='s'
PAPER='p'

emojis={ROCK:'🥌', SCISSORS:'✂', PAPER:'🧻'}
choices=(tuple(emojis.keys()))

def get_user_choice():
  while True:
    user_choice= input(f'Rock, paper or scissors? (r/p/s):').strip().lower()
    if user_choice in choices:
      return user_choice
    else:
      print('Invalid choice!')

def display_choices(user_choice,computer_choice):
  print(f'You chose {emojis[user_choice]}')
  print(f'Computer chose {emojis[computer_choice]}')

def determine_winner(user_choice,computer_choice):
  if user_choice==computer_choice:
    print('Tie!')
  elif (
    (user_choice== ROCK and computer_choice==SCISSORS) or 
    (user_choice== SCISSORS and computer_choice==PAPER) or 
    (user_choice== PAPER and computer_choice==ROCK)):
    print('You win')
  else:
    print('You lose')

def play_game():
  while True:
    user_choice=get_user_choice()

    computer_choice=(random.choice(choices))

    display_choices(user_choice,computer_choice)

    determine_winner(user_choice,computer_choice)

    should_continue = input("Continue? y/n: ").strip().lower()
    if should_continue=='n':
      break

play_game()

# Optional Enhancements 
# • Modify the game so that the first player (or computer) to win two out of three 
# rounds is declared the overall winner. This adds a competitive aspect to the 
# game. 
# • Keep a tally of how many times the player wins, loses, or ties with the 
# computer. Display these statistics at the end of the game. 
# • Add an option for two players to play against each other, taking turns to input 
# their choices. The program should then determine the winner based on their 
# inputs. 