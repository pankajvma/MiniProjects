import random
import art
from os import system

print(art.logo)

print('''******************Blackjack House Rules******************
The deck is unlimited in size. 
There are no jokers. 
The Jack/Queen/King all count as 10.
The the Ace can count as 11 or 1.
''')

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']

def check_score(card, score):
  if card == 'A' and (score + 11) <= 21:
    score += 11
  elif card == 'A' and (score + 11) > 21:
    score += 1
  elif card == 'J' or card == 'K' or card == 'Q':
    score += 10
  else:
    score += card

  return score


def play_again():
  choice = input("Do you want to play again? Enter 'yes' or 'no': ").lower()
  if choice == 'yes':
    system('cls')
    start_blackjack()
  else:
    print("Exiting...")

def compare_score(com_score, u_score):
  if com_score > 21:
    print("You've Won!")
  elif u_score > 21:
    print("You Lose!")
  else:
    if com_score == 21:
      print("Computer've Won Already!")
    elif u_score == 21:
      print("You Won Already!")
    elif com_score > u_score:
      print(f"Computer have won with score {com_score}")
    elif com_score < u_score:
      print(f"You have won with score {u_score}")
    else:
      print("It's a draw")
  play_again()

def start_blackjack():
  user_deck = []
  computer_deck = []
  user_score = 0
  computer_score = 0  

  for _ in range(2):
    computers_card = random.choice(cards)
    computer_deck.append(computers_card)
    computer_score = check_score(computers_card, computer_score)
    users_card = random.choice(cards)
    user_deck.append(users_card)
    user_score = check_score(users_card, user_score)

  if computer_score == 21:
    print(f"Computer've got: {user_deck}")
    print("Computer Won!")
    play_again()
    return
  else:
    print(f"Computer got: [{computer_deck[0]}, ?]")

  if user_score == 21:
    print(f"You've got: {user_deck}")
    print("You Won Already!")
    play_again()
    return
  else:
    print(f"You've got: {user_deck}")
    while True:
      want_another_card = input("Do you want another card? Enter 'yes' or 'no': ").lower()
      if want_another_card == 'yes':
        users_card = random.choice(cards)
        user_deck.append(users_card)
        user_score = check_score(users_card, user_score)
        print(f"You've got: {user_deck}")
        print(f"Your score is: {user_score}")
        if user_score == 21:
          print("You Won Already!")
          play_again()
          return
        elif user_score > 21:
          print("You Lose!")
          play_again()
          return
      else:
        break

  while computer_score < 17:
    computers_card = random.choice(cards)
    computer_deck.append(computers_card)
    computer_score = check_score(computers_card, computer_score)

  print(f"Computer've got: {computer_deck}")
  print(f"Computer's score is: {computer_score}")

  compare_score(computer_score, user_score)
  return

start_blackjack()
