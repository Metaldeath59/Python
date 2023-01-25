import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

go=input("Do you want to play to blackjack ? Press 'y' to accept or 'n' to quit\n")

if go=="y":
    end=False
else :
    end=True

player_cards=[]
pc_cards=[]
player_cards.append(random.choice(cards))
pc_cards.append(random.choice(cards))

player_score=0
pc_score=0

def score_calc():
    global player_score
    global pc_score
    player_score=0
    pc_score=0
    for i in range(len(player_cards)):
        player_score+=player_cards[i]
    for i in range(len(pc_cards)):
        pc_score+=pc_cards[i]
    print(f"Your cards are {player_cards} and your score is {player_score}")
    print(f"Computer cards are {pc_cards} and its score is {pc_score}")

while not end:
    score_calc()
    while pc_score<=16 and (pc_score<21 and player_score<21):
        another=input("Do you want to take another card ? press 'y' or 'n'\n")
        if pc_score<=16:
            print("PC has to take a card")
            pc_cards.append(random.choice(cards))
            score_calc()
        if another=="y":
            player_cards.append(random.choice(cards))
            score_calc()
        elif pc_score>player_score:
            print("Player has to take another card")
            player_cards.append(random.choice(cards))
            score_calc()
        else:
            score_calc()
            break
    another=input("Do you want to take another card ? press 'y' or 'n'\n")
    if another=='y':
        player_cards.append(random.choice(cards))
        score_calc()
    if pc_score>21:
        print("You won !")
        end=True
    elif player_score>21:
        print("PC won !")
        end=True
    elif pc_score==21:
        print("PC won !")
        end=True
    elif player_score==21:
        print("You won !")
        end=True
    elif player_score>pc_score:
        print("You won !")
        end=True
    else:
        print("PC won !")
        end=True
if end==True:
    print("GoodBye !")