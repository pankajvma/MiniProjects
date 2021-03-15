import random
import art

print(art.logo)

print('''******************Blackjack House Rules******************
The deck is unlimited in size. 
There are no jokers. 
The Jack/Queen/King all count as 10.
The the Ace can count as 11 or 1.
''')

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']

def check_Score(card, score):
  if card == 'A' and (score + 11) <= 21:
    score += 11
  elif card == 'A' and (score + 11) > 21:
    score += 1
  elif card == 'J' or card == 'K' or card == 'Q':
    score += 10
  else:
    score += card

  return score

user_Deck = []
computer_Deck = []


def start_BlackJack():
  user_Score = 0
  computer_Score = 0  
  computers_Card = random.choice(cards)
  computer_Deck.append(computers_Card)
  computer_Score = check_Score(computers_Card, computer_Score)
  computers_Card = random.choice(cards)
  computer_Deck.append(computers_Card)
  computer_Score = check_Score(computers_Card, computer_Score)

  if computer_Score == 21:
    print("Computer Won!")
    return
  else:
    print(f"Computer got: [{computer_Deck[0]}, ?]")

  users_Card = random.choice(cards)
  user_Deck.append(users_Card)
  user_Score = check_Score(users_Card, user_Score)
  users_Card = random.choice(cards)
  user_Deck.append(users_Card)
  user_Score = check_Score(users_Card, user_Score)

  if user_Score == 21:
    print("You Won Already!")
    return
  else:
    print(f"You've got: {user_Deck}")
    while True:
      want_Another_Card = input("Do you want another card? Enter 'yes' or 'no': ").lower()
      if want_Another_Card == 'yes':
        users_Card = random.choice(cards)
        user_Deck.append(users_Card)
        user_Score = check_Score(users_Card, user_Score)
        print(f"You've got: {user_Deck}")
        print(f"Your score is: {user_Score}")
        if user_Score == 21:
          print("You Won Already!")
          return
        elif user_Score > 21:
          print("You Lose!")
          return
      else:
        break

  while computer_Score < 17:
    computers_Card = random.choice(cards)
    computer_Deck.append(computers_Card)
    computer_Score = check_Score(computers_Card, computer_Score)

    print(f"Computer've got: {computer_Deck}")
    print(f"Computer's score is: {computer_Score}")

    if user_Score == 21:
      print("Computer've Won Already!")
      return
    elif user_Score > 21:
      print("You Won Already!")
      return

  if computer_Score > user_Score:
    print(f"Computer have won with score {computer_Score}")
  else:
    print(f"You have won with score {user_Score}")

start_BlackJack()
