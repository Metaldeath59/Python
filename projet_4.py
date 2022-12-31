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

#Write your code below this line 👇
import random


choice=input("rock, paper or scissors ?")
choice_list=[rock,paper,scissors]
com_choice=random.randint(0,2)

if choice=="rock":
  print(rock)
  print(choice_list[com_choice])
  if com_choice==0:
    print("égalité!")
  elif com_choice==1:
    print("Perdu !")
  elif com_choice==2:
    print("Gagné !")
elif choice=="paper":
  print(paper)
  print(choice_list[com_choice])
  if com_choice==1:
    print("égalité!")
  elif com_choice==2:
    print("Perdu !")
  elif com_choice==0:
    print("Gagné !")
elif choice=="scissors":
  print(scissors)
  print(choice_list[com_choice])
  if com_choice==2:
    print("égalité!")
  elif com_choice==0:
    print("Perdu !")
  elif com_choice==1:
    print("Gagné !")