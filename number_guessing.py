    # PLAN:
# 1) generate a number from 1 to 100
# 2) if type NaN or >100: 
#       print invalid message
# 3) if type 1-100 --> 50: 
#       print message:
  #       print message 'Too high!' if entered number is lower
  #       print message 'Too low!' if entered number is higher
  #       print message 'Congratulations! You guessed the number.' if entered number is higher

import random


# the_number=(random.randint(1,100))

# while True:
#   print('Guess the number between 1 and 100:')
#   try:
#       guessed_number=int(input())
#       if guessed_number >= 1 and guessed_number <= 100:
#         if guessed_number> the_number:
#             print('Too high!')
#         if guessed_number< the_number:
#             print('Too low!')
#         if guessed_number== the_number:
#             print('Congratulations! You guessed the number.')
#             break
#       else:
#         print('Please, enter a number between 1 and 100')
#   except ValueError:
#       print('Invalid input! Please enter a valid number.')

# =========================================
    # mosh:
    # PLAN:
    # Generate a random number
    # Loop
      # Ask the user to make a guess
      # If not a valid number
      #   Print an error
      # If number<guess
      #   Print too low
      # If number>guess
      #   Print too high
      # Else
      #   Print well done

# number_to_guess=(random.randint(1,100))

# while True:
#     try:
#       guess= int(input('Guess the number between 1 and 100:'))
#       if guess< number_to_guess:
#         print('Too low!')
#       elif guess> number_to_guess:
#         print('Too high!')
#       else:
#         print('Congratulations! You guessed the number.')
#         break
#     except ValueError:
#       print('Please enter a valid number')

# =========================================

# Optional Enhancements
# • Allow the user to specify the minimum and maximum values for the number
# range before the game starts. This gives the player more control over the
# difficulty level.
# • Implement a feature that limits the number of guesses a player can make. If
# the player runs out of attempts, the game should end, and the correct number
# should be revealed.
# • Add a feature that keeps track of the fewest attempts it took to guess the
# number correctly. The program should display this "best score" at the end of
# each game. 

the_best_score= float('inf')

while True:
  min= int(input('Enter the minimum number:'))
  max= int(input('Enter the maximum number:'))
  attempts= int(input('Enter the amount of attempts:'))

  counter=0
  number_to_guess=(random.randint(min,max))

  while True:
      try:
          guess= int(input(f'Guess the number between {min} and {max}:'))
          counter= counter+1
          if guess< number_to_guess:
            print('Too low!')
          elif guess> number_to_guess:
            print('Too high!')
          else:
            print(f'Congratulations! You guessed the number from {counter} attempt(s).')
            if counter<the_best_score:
              print(f'The best score for now is {counter} attempts')
              the_best_score=counter
            else:
              print(f'The best score for now is {the_best_score} attempts')
            break
          if counter==attempts:
              print(f'Fail! You have not guessed the number from {attempts} attempt(s).')
              print(f'The guessed number was {number_to_guess}.')
              break
      except ValueError:
        print('Please enter a valid number')

  play_again = input("Do you want to play again? y/n: ").strip().lower()
  if play_again != 'y':
    print(f"Thanks for playing! The best score was {the_best_score} attempt(s).")
    break
