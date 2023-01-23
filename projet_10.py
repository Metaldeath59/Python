from art import logo
print(logo)

first_number=float(input("What's the first number ?: "))
print("+\n-\n*\n/\n")
operation=input("Pick an operation:")
second_number=float(input("What's the second number ?:"))
end=False

while not end:
  def rounded_nb(number):
    return round(number,1)

  if operation == "+":
    result=first_number+second_number
    print(f"{rounded_nb(first_number)} + {rounded_nb(second_number)} = {rounded_nb(result)}")
  elif operation=="-":
    result=first_number-second_number
    print(f"{rounded_nb(first_number)} - {rounded_nb(second_number)} = {rounded_nb(result)}")
  elif operation=="*":
    result=first_number*second_number
    print(f"{rounded_nb(first_number)} * {rounded_nb(second_number)} = {rounded_nb(result)}")
  elif operation=="/":
    result=first_number/second_number
    print(f"{rounded_nb(first_number)} / {rounded_nb(second_number)} = {rounded_nb(result)}")

  again=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: \n")
  if again=='y':
    first_number=result
    print("+\n-\n*\n/\n")
    operation=input("Pick an operation:")
    second_number=int(input("What's the second number ?:"))
  else:
    end=True
    #print(logo)
    #first_number=float(input("What's the first number ?: "))
    #print("+\n-\n*\n/\n")
    #operation=input("Pick an operation:")
    #second_number=float(input("What's the second number ?:"))