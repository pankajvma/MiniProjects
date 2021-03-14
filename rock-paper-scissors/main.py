import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

choice = int(input("Enter 0 for Rock, 1 for Paper, and 2 for Scissors:\n"))

computer_choice = random.randint(0, 2)
computer_chose = rock_paper_scissors[computer_choice]

if choice in range(0, 3):
  print(rock_paper_scissors[choice])
  print("Computer chose:\n"+computer_chose)
  if choice == computer_choice:
    print("It's a Draw")
  elif choice == 0 and computer_choice == 2 or choice > computer_choice:
    print("You Won!")
  else:
    print("You Lose :(")
else:
    print("Please provide a valid input.")


