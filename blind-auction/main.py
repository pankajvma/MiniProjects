from os import system
import  art

print(art.logo)
print("Welcome to the secret auction program.")

bidders_and_bids = {}

more_bidders = True

def find_highest_bidder():
  system('cls')
  max_bidder = ""
  max_bid = 0
  for bidder in bidders_and_bids:
    if bidders_and_bids[bidder] > max_bid:
      max_bid = bidders_and_bids[bidder]
      max_bidder = bidder

  print(f"The winner is {max_bidder} with a bid of {bidders_and_bids[max_bidder]}")
  

while more_bidders:
  name = input("What's Your name?: ")
  bid = int(input("What's Your bid?: "))
  bidders_and_bids[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if more_bidders == "yes":
    more_bidders = True
    system('cls')
  else:
    more_bidders = False
    find_highest_bidder()
  

