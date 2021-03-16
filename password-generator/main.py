#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))


password = ""
for letter in range(nr_letters):
  rand = random.randint(0, len(letters)-1)
  # rand = random.choice(letters)
  password += letters[rand]
for symbol in range(nr_symbols):
  rand = random.randint(0, len(symbols)-1)
  password += symbols[rand]
for number in range(nr_numbers):
  rand = random.randint(0, len(numbers)-1)
  password += numbers[rand]

print("Password: "+password)

password = []

for letter in range(nr_letters):
  rand = random.randint(0, len(letters)-1)
  password.append(letters[rand])
  # password += letters[rand]
for symbol in range(nr_symbols):
  rand = random.randint(0, len(symbols)-1)
  password.append(symbols[rand])
for number in range(nr_numbers):
  rand = random.randint(0, len(numbers)-1)
  password.append(numbers[rand])


strong_pass = ""
for i in range(len(password)):
  rand = random.randint(0, len(password)-1)
  strong_pass += password[rand]
  password.pop(rand)

print("Strong Password: "+strong_pass)