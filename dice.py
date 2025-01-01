import random

def roll_the_dice():
  print(f'({random.choice([1, 2, 3, 4, 5, 6])}, {random.choice([1, 2, 3, 4, 5, 6])})')

while True:
  print('Roll the dice? (y/n): ')
  answer = input().lower()
  if answer =='y':
      roll_the_dice()
  elif answer =='n':
    print('Thanks for playing!')
    break
  else:
    print('Invalid choice!')

    # mosh:
    while True:
      choice=input('Roll the dice? (y/n): ').lower()
      if choice=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f'({die1}, {die2})')
      elif choice =='n':
        print('Thanks for playing!')
        break
      else:
        print('Invalid choice!')

#         Optional Enhancements
# • Modify the program so the user can specify how many dice they want to roll.
# • Add a feature that keeps track of how many times the user has rolled the dice
# during the session. This will require a counter that increments each time the
# dice are rolled. 

def roll_the_dice2(wishes):
  str_dices=''
  for x in wishes:
    str_dices += random.randint(1,6)
print(str_dices)

while True:
  print('Roll the dice? (y/n): ')
  print('How many dices do you wish?')
  answer = input().lower()
  wishes=int(input())
  if answer =='y':
      roll_the_dice2(wishes)
  elif answer =='n':
    print('Thanks for playing!')
    break
  else:
    print('Invalid choice!')