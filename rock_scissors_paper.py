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
import os

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

# ROCK='r'
# SCISSORS='s'
# PAPER='p'

# emojis={ROCK:'🥌', SCISSORS:'✂', PAPER:'🧻'}
# choices=(tuple(emojis.keys()))

# def get_user_choice():
#   while True:
#     user_choice= input(f'Rock, paper or scissors? (r/p/s):').strip().lower()
#     if user_choice in choices:
#       return user_choice
#     else:
#       print('Invalid choice!')

# def display_choices(user_choice,computer_choice):
#   print(f'You chose {emojis[user_choice]}')
#   print(f'Computer chose {emojis[computer_choice]}')

# def determine_winner(user_choice,computer_choice):
#   if user_choice==computer_choice:
#     print('Tie!')
#   elif (
#     (user_choice== ROCK and computer_choice==SCISSORS) or 
#     (user_choice== SCISSORS and computer_choice==PAPER) or 
#     (user_choice== PAPER and computer_choice==ROCK)):
#     print('You win')
#   else:
#     print('You lose')

# def play_game():
#   while True:
#     user_choice=get_user_choice()

#     computer_choice=(random.choice(choices))

#     display_choices(user_choice,computer_choice)

#     determine_winner(user_choice,computer_choice)

#     should_continue = input("Continue? y/n: ").strip().lower()
#     if should_continue=='n':
#       break

# play_game()

# =========================================

# Optional Enhancements 
# • Modify the game so that the first player (or computer) to win two out of three 
# rounds is declared the overall winner. This adds a competitive aspect to the 
# game. 
# • Keep a tally of how many times the player wins, loses, or ties with the 
# computer. Display these statistics at the end of the game. 
# • Add an option for two players to play against each other, taking turns to input 
# their choices. The program should then determine the winner based on their 
# inputs. 

ROCK='r'
SCISSORS='s'
PAPER='p'

ROUNDS=3

counter=0
user_wins=0
user_loses=0
user_ties=0
computer_wins=0
computer_loses=0
computer_ties=0

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
  global user_wins, user_loses, user_ties, ROUNDS
  if user_choice==computer_choice:
    user_ties=user_ties+1
    print('Tie!')
    print(f'You have wins:{user_wins} loses:{user_loses} ties:{user_ties}')

  elif (
    (user_choice== ROCK and computer_choice==SCISSORS) or 
    (user_choice== SCISSORS and computer_choice==PAPER) or 
    (user_choice== PAPER and computer_choice==ROCK)):
    user_wins=user_wins+1
    print('You win')
    print(f'You have wins:{user_wins} loses:{user_loses} ties:{user_ties}')
    if user_wins>ROUNDS/2:
      print(f'You are the overall winner! You`re lucky ass! 👍')
  else:
    user_loses=user_loses+1
    print('You lose')
    print(f'You have wins:{user_wins} loses:{user_loses} ties:{user_ties}')
    if user_loses>ROUNDS/2:
      print(f'Computer is the overall winner! You`re loser! 👎')

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


# • Add an option for two players to play against each other, taking turns to input 
# their choices. The program should then determine the winner based on their 
# inputs. 
# chatGPT================================
import os
import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

ROUNDS = 3

user_wins = 0
user_loses = 0
user_ties = 0
player1_wins = 0
player1_losses = 0
player1_ties = 0
player2_wins = 0
player2_losses = 0
player2_ties = 0

emojis = {ROCK: '🥌', SCISSORS: '✂', PAPER: '🧻'}
choices = tuple(emojis.keys())

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_hidden_choice(player_name):
    """Get choice from a player with privacy."""
    print(f"{player_name}, it's your turn.")
    input("Press Enter when ready...")  
    clear_screen()
    while True:
        user_choice = input(f'{player_name}, choose Rock, Paper, or Scissors (r/p/s): ').strip().lower()
        if user_choice in choices:
            clear_screen()
            return user_choice
        else:
            print('Invalid choice! Please try again.')

def get_user_choice():
    """Get user choice for single player mode."""
    while True:
        user_choice = input(f'Rock, paper or scissors? (r/p/s): ').strip().lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(choice1, choice2, player1="Player 1", player2="Player 2"):
    """Show choices of both players."""
    print(f'{player1} chose {emojis[choice1]}')
    print(f'{player2} chose {emojis[choice2]}')

def determine_winner(user_choice, computer_choice):
    """Single player winner determination."""
    global user_wins, user_loses, user_ties
    if user_choice == computer_choice:
        user_ties += 1
        print('It\'s a Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        user_wins += 1
        print('You win!')
    else:
        user_loses += 1
        print('You lose!')
    print(f'Wins: {user_wins}, Losses: {user_loses}, Ties: {user_ties}')

def determine_two_player_winner(choice1, choice2):
    """Determine the winner between two players."""
    global player1_wins, player1_losses, player1_ties, player2_wins, player2_losses, player2_ties
    if choice1 == choice2:
        player1_ties += 1
        player2_ties += 1
        print('It\'s a tie!')
    elif (
        (choice1 == ROCK and choice2 == SCISSORS) or 
        (choice1 == SCISSORS and choice2 == PAPER) or 
        (choice1 == PAPER and choice2 == ROCK)
    ):
        player1_wins += 1
        player2_losses += 1
        print('Player 1 wins!')
    else:
        player1_losses += 1
        player2_wins += 1
        print('Player 2 wins!')
    print(f'Player 1: Wins: {player1_wins}, Losses: {player1_losses}, Ties: {player1_ties}')
    print(f'Player 2: Wins: {player2_wins}, Losses: {player2_losses}, Ties: {player2_ties}')

def play_two_player_game():
    """Two-player mode with privacy."""
    for round_num in range(1, ROUNDS + 1):
        print(f'Round {round_num} of {ROUNDS}')
        player1_choice = get_hidden_choice("Player 1")
        player2_choice = get_hidden_choice("Player 2")
        display_choices(player1_choice, player2_choice, "Player 1", "Player 2")
        determine_two_player_winner(player1_choice, player2_choice)
    print("\nFinal Results:")
    if player1_wins > player2_wins:
        print("Player 1 is the overall winner!")
    elif player2_wins > player1_wins:
        print("Player 2 is the overall winner!")
    else:
        print("It's a tie overall!")

def play_game():
    """Main function to play single or two-player mode."""
    mode = input("Choose mode: 1 for single player vs computer, 2 for two players: ").strip()
    if mode == '1':
        for round_num in range(1, ROUNDS + 1):
            print(f'Round {round_num} of {ROUNDS}')
            user_choice = get_user_choice()
            computer_choice = random.choice(choices)
            display_choices(user_choice, computer_choice, "You", "Computer")
            determine_winner(user_choice, computer_choice)
        print("\nFinal Results:")
        if user_wins > user_loses:
            print("You are the overall winner!")
        elif user_loses > user_wins:
            print("Computer is the overall winner!")
        else:
            print("It's a tie overall!")
    elif mode == '2':
        play_two_player_game()
    else:
        print("Invalid mode. Please try again.")

# Start the game
play_game()


