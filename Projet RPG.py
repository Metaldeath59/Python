from ast import Break
import random

# Paramètres initiaux
player_hp=50
ennemy_hp=50
player_potion_remaining=3
# Tant que player_hp>0 ou ennemy_hp>0 
while player_hp>0 and ennemy_hp>0:
    #Afficher une ligne et préparer les valeurs aléatoires du tour
    print("__________________________________________________________________")
    player_attack= random.randint(5,10)
    ennemy_attack= random.randint(5,15)
    player_potion_regeneration=random.randint(15,50)
    #choix_str=input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    choix_str=input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    while choix_str.isdigit()==False or int(choix_str)<1 or int(choix_str)>2:
        # Tant que choix.isdigit() and (choix==1 or choix ==2):
            #input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        choix_str=input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
        #Else: 
            #Break
    else:
    # Si attaque, alors l'ennemi et le joueur perdent des hp
        if int(choix_str)==1:
        # Afficher combien de dégats ont étés infligés par le player
            print(f"Vous avez infligé {player_attack} points de dégats à l'ennemi")
        # Afficher combien de dégats le player a subi
            print(f"L'ennemi vous a infligé {ennemy_attack} points de dégats")
        # Faire player_hp= player_hp-ennemy_attack
            player_hp=player_hp-ennemy_attack
        # Faire ennemy_hp= ennemy_hp-player-attack
            ennemy_hp=ennemy_hp-player_attack
        # Afficher combien de point de vie il reste à player
            print(f"Il vous reste {player_hp} points de vie.")
        # Afficher combien de points de vie il reste à l'ennemi
            print(f"Il reste {ennemy_hp} points de vie à l'ennemi.")
    # Sinon
        else:
        #Si player potion remaining==0 alors afficher qu'il n'y a plus de potion
            if player_potion_remaining==0:
                print("Vous n'avez plus de potions !")
        #Sinon alors le joueur gagne des hp et générer un tour où l'ennemi attaque mais pas le joueur et décrémenter une potion
            else:
            #Faire player_hp=player_hp+player_potion_regeneration
                player_hp=player_hp+player_potion_regeneration
            #faire player_potion_remaining-1
                player_potion_remaining=player_potion_remaining-1
            #fstring Afficher combien de regen
                print(f"Vous récupérez {player_potion_regeneration} points de vie ({player_potion_remaining} potions restantes")
            #Faire et afficher player_hp= player_hp-ennemy_attack
                player_hp=player_hp-ennemy_attack
                print(f"L'ennemi vous a infligé {ennemy_attack} points de dégats")
            #Afficher player_hp
                print(f"Il vous reste {player_hp} points de vie.")
            #Afficher ennemy_hp
                print(f"Il reste {ennemy_hp} points de vie à l'ennemi.")
            #Afficher une ligne
                print("__________________________________________________________________")
            #Afficher "Vous passez votre tour..."
                print("Vous passez votre tour...")
                ennemy_attack= random.randint(5,15)
            #Faire et afficher les dégats ennemis player_hp= player_hp-ennemy_attack
                player_hp=player_hp-ennemy_attack
                print(f"L'ennemi vous a infligé {ennemy_attack} points de dégats")
            #Afficher player_hp restants
                print(f"Il vous reste {player_hp} points de vie.")
            #Afficher ennemy_hp restants
                print(f"Il reste {ennemy_hp} points de vie à l'ennemi.")
# Sinon:
else:
    #Si player_hp <=0 
    if player_hp<=0:
        #Afficher vous avez perdu !
        print("Vous avez perdu !")
    #Sinon:
    else:
        #Afficher Bravo vous avez gagné!
        print("Bravo ! Vous avez gagné !")