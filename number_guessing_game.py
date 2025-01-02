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


the_number=(random.randint(1,100))

while True:
  print('Guess the number between 1 and 100:')
  try:
      guessed_number=int(input())
      if guessed_number >= 1 and guessed_number <= 100:
        if guessed_number> the_number:
            print('Too high!')
        if guessed_number< the_number:
            print('Too low!')
        if guessed_number== the_number:
            print('Congratulations! You guessed the number.')
            break
      else:
        print('Please, enter a number between 1 and 100')
  except ValueError:
      print('Invalid input! Please enter a valid number.')

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

number_to_guess=(random.randint(1,100))

while True:
    try:
      guess= int(input('Guess the number between 1 and 100:'))
      if guess< number_to_guess:
        print('Too low!')
      elif guess> number_to_guess:
        print('Too high!')
      else:
        print('Congratulations! You guessed the number.')
        break
    except ValueError:
      print('Please enter a valid number')

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