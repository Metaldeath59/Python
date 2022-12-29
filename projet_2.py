#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill=input("What was the total bill? \n")
tip_percentage=input("What percentage tip would you like to give ? 10, 12, or 15? \n")
nb_people=input("How many people to split the bill ? \n")

tax=int(total_bill)*(int(tip_percentage)/100)
ttc=int(total_bill)+tax
ttc_per_pers=ttc/int(nb_people)
rounded_ttc_per_pers=round(ttc_per_pers,2)
print(f"Each person should pay ${rounded_ttc_per_pers}")