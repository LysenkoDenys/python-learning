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
    # =========================================
    # mosh:
    # PLAN:
    # Ask: roll the dice?
    # If y
      # generate 2 random numbers
      # print them
    # If n
      # print thank you message
      # terminate
    # Else
      # print invalid choice

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
    # =========================================
# Optional Enhancements
# • Modify the program so the user can specify how many dice they want to roll.
# • Add a feature that keeps track of how many times the user has rolled the dice
# during the session. This will require a counter that increments each time the
# dice are rolled. 

counter=0

def roll_the_dice2(wishes):
  list_dices=[]
  for x in range(wishes):
    list_dices.append(random.randint(1,6))
  print(tuple(list_dices))

print('How many dices do you wish?')
wishes=int(input())
while True:
  print('Roll the dice? (y/n): ')
  answer = input().lower()
  if answer =='y':
      roll_the_dice2(wishes)
      counter=counter+1
  elif answer =='n':
    print(f'You have rolled the dice(s) {counter} time(s)')
    print('Thanks for playing!')
    break
  else:
    print('Invalid choice!')


