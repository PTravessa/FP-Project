#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: 
"""

import gameFunctions as funcs

option = int(input("1 - New game \n2 - Continuation game ?\n"))
fileName = input("Name of the file containing the game information? ")

try:
    if option == 1:
        # Attempt to read information about a new game from an existing file
        expertise, fullBottlesByEnd, bottles = funcs.newGameInfo(fileName)
    else:
        # Attempt to read all the information about an old game from an existing file
        bottles, botSize, nrErrors, expertise, fullBottles = funcs.oldGameInfo(fileName)
    
    # Set nrBotts to the total number of bottles
    nrBotts = len(bottles)

except FileNotFoundError:
    # If the file doesn't exist, create a new file with the contents of the game
    expertise, fullBottlesByEnd, bottles = funcs.newGameInfo(fileName)

    # Handle any other exceptions as needed
except Exception as e:
    print(f"Error: {e}")
    # Handle the exception or exit the program as needed


# infoGame is a tuple with several different values
bottles, botSize, nrErrors, expertise, fullBottles = funcs.newGameInfo(fileName)

endGame = False
funcs.showBottles(bottles, botSize, nrErrors)
source = funcs.askUserFor("Source bottle? ", bottles.keys())

# Let's play the game
while not endGame and not source == 'Z':
    destin = funcs.askUserFor("Destination bottle? ", bottles.keys())
    if funcs.moveIsPossible(botSize, source, destin, bottles):
        funcs.doMove(botSize, source, destin, bottles)
        funcs.showBottles(bottles, botSize, nrErrors)
        if funcs.full(bottles[destin], botSize):
            fullBottles += 1
    else:
        print("Error!")
        nrErrors += 1
    endGame = funcs.allBottlesFull(nrBotts, fullBottles, expertise) or \
              nrErrors == 3

    if not endGame:
        source = funcs.askUserFor("Source bottle? (Z to leave game)",
                                  bottles.keys(), 'Z')

# End of game may have happened either because the user filled all the bottles he
# was supposed to, or he made 3 errors, or he gave up playing (by inputting
# the letter 'Z'' for the source)
if source == 'Z':
    store = funcs.askUserFor("Want to store the game for future playing? (YES,NO)",
                             ['YES', 'NO'], '')
    if store == "YES":
        fileName = input("Name of the file where to store the game information?")
        funcs.writeGameInfo(fileName, bottles, botSize, nrErrors, expertise, fullBottles)
        print("Hope to see you again soon!")
    else:
        print("Better luck next time!")
else:
    print("Full bottles =", fullBottles, "  Errors =", nrErrors)
    if nrErrors >= 3:
        print("Better luck next time!")
    else:
        print("CONGRATULATIONS!!")

print()