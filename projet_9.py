from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program")

end=False
auctionners={}

while not end:
  name=input("what is your name ?\n")
  bid=int(input("what is your bid ?\n"))
  auctionners[name]=bid
  other=input("Are there any other bidders ? Type 'yes' or 'no'.\n")
  clear()
  print(logo)
  if other == "no":
    big_bid=0
    for key in auctionners:
      if auctionners[key]>big_bid:
        big_bid=auctionners[key]
        winner=key
    print(f"The winner is {winner} with a bid of {big_bid}")
    end=True