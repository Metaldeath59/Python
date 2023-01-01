#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#list_letter=[]
#for element_1 in range(0,nr_letters):
#  lettre_random=str(random.choice(letters))
#  list_letter.append(lettre_random)
#list_symbol=[]
#for element_2 in range(0,nr_symbols):
#  symbol_random=str(random.choice(symbols))
#  list_symbol.append(symbol_random)
#list_number=[]
#for element_3 in range(0,nr_numbers):
#  number_random=str(random.choice(numbers))
#  list_number.append(number_random)
#print("".join(list_letter+list_symbol+list_number))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

list_letter=[]

for element_1 in range(0,nr_letters):
  lettre_random=str(random.choice(letters))
  list_letter.append(lettre_random)
list_symbol=[]

for element_2 in range(0,nr_symbols):
  symbol_random=str(random.choice(symbols))
  list_symbol.append(symbol_random)
list_number=[]

for element_3 in range(0,nr_numbers):
  number_random=str(random.choice(numbers))
  list_number.append(number_random)

list_finale=list_letter+list_symbol+list_number
nr_total=nr_letters+nr_numbers+nr_symbols
random_list=[]

for element_final in range(0,nr_total):
  element_switch=random.choice(list_finale)
  list_finale.remove(element_switch)
  random_list.append(element_switch)

print("".join(random_list))