import random

choices=['r', 'p', 's']
number_of_chances_available=10
availed_chances=0
comp_points=0
player_points=0
print("\t\t\t\t Rock,Paper,Scissor Game\n\n")
print("Press r for Rock\nPress p for Paper\nPress s for Scissor\n")

while availed_chances<number_of_chances_available:
    player_guess=input("Rock,Paper,Scissor:")
    comp_guess=random.choice(choices)

    if player_guess==comp_guess:
        print("Draw","0 Points to both","Play again\n")

    elif player_guess== "r" and comp_guess== "p":
        comp_points=comp_points+1
        print(f"Opponent Showed {comp_guess} and You Showed {player_guess}\n")
        print("Opponent wins 1 Point\n")
        print(f"Opponent points:{comp_points} and Your points:{player_points}\n")

    elif player_guess== "r" and comp_guess== "s":
        player_points=player_points+1
        print(f"You Showed {player_guess} and Opponent Showed {comp_guess}\n")
        print("You wins 1 Point\n")
        print(f"Your points:{player_points} and Opponent points:{comp_points}\n")

    elif player_guess== "p" and comp_guess== "s":
        comp_points=comp_points+1
        print(f"Opponent Showed {comp_guess} and You Showed {player_guess}\n")
        print("Opponent wins 1 Point\n")
        print(f"Opponent points:{comp_points} and Your points:{player_points}\n")

    elif player_guess== "p" and comp_guess== "r":
        player_points=player_points+1
        print(f"You Showed {player_guess} and Opponent Showed {comp_guess}\n")
        print("You wins 1 Point\n")
        print(f"Your points:{player_points} and Opponent points:{comp_points}\n")

    elif player_guess== "s" and comp_guess== "r":
        comp_points=comp_points+1
        print(f"Opponent Showed {comp_guess} and You Showed {player_guess}\n")
        print("Opponent wins 1 Point\n")
        print(f"Opponent points:{comp_points} and Your points:{player_points}\n")

    elif player_guess== "s" and comp_guess== "p":
        player_points=player_points+1
        print(f"You Showed {player_guess} and Opponent Showed {comp_guess}\n")
        print("You wins 1 Point\n")
        print(f"Your points:{player_points} and Opponent points:{comp_points}\n")

    else:
        print("YOU ARE PLAYING A WRONG GAME\n")

    availed_chances=availed_chances+1
    print(f"{number_of_chances_available-availed_chances} Chances are left out of{number_of_chances_available} \n")

print("GAME OVER")
if comp_points==player_points:
    print("GAME TIED")
elif comp_points<player_points:
    print("CONGRATULATIONS!! YOU WON")
else:
    print("OPPONENT WON....BETTER LUCK NEXT TIME!")

print(f"Your points are {player_points} and Opponent points are {comp_points}")