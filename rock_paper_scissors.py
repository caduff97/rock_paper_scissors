import random

def computer_choice():
  choice = random.choice(['r', 'p', 's'])
  if choice == 'r':
    choice_name = 'rock'
  elif choice == 'p':
    choice_name = 'paper'
  else:
    choice_name ='scissors'

  return choice, choice_name

def play():
  user = input("What's your choice? \n 'r' for rock, 'p' for paper, 's' for scissors \n")
  computer, choice_name = computer_choice()

  if user == computer:
    return f'It\'s a tie! You both chose {choice_name}.'

  if is_win(user, computer):
    return f'You won! Computer chose {choice_name}.'

  return f'You lost! Computer chose {choice_name}.'

def is_win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
  or (player == 'p' and opponent == 'r'):
    return True

print(play())