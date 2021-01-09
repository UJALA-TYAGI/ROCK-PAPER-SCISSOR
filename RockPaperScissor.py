""" Rock Paper Scissors
----------------------------------------
"""
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Let's Go!")
    userChoice =input("Choose your weapon [R]ock, [P]aper, [S]cissors, or press 'N' to exit: ")
    if not re.match("[SsRrPpNn]", userChoice):
        print ("Please choose a letter: and enter 'N' to end the game")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue
    if userChoice.upper()=='N':
        print("The game ends!")
        exit()
    # Echo the user's choice
    print ("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print ("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print ("It's a Tie! ")
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print ("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print ("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beat rock, I win! ")
        continue
    else:
        print ("You win!")
