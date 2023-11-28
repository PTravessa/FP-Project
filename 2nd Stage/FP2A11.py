#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FUNDAMENTOS DE PROGRAMAÇÃO - PROJETO 2

@author: Duarte Gonçalves (nº 56095) e Pedro Travessa (nº 59479) - GRUPO 11

Observation: We made a few changes to the main program to ensure the game
ends as intended (the changes are commented)
"""
import random

#######################################################
####################  FUNCTIONS  ######################
#######################################################        

# *****************************************************
def askForExpertise():
    """
    Asks the user the level of expertise they want

    Returns
    -------
    exp : integer
        The level of expertise chosen, between MAX_EXPERT and LESS_EXPERT

    Raises
    -------
    ValueError:
        If the user input isn't a valid integer

    """
    while True:

        # Prompt user to enter value of the expertise they want
        exp = input("Expert level - from 1 (radical) to 5 (beginner)? ")

        try:
            # Convert user input to integer
            exp = int(exp)

            # Check if user input is valid
            if exp in [1, 2, 3, 4, 5]:
                return exp
            else:
                print("Please enter a value between", MAX_EXPERT, "and", LESS_EXPERT,".")

        # If user input is not valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# *****************************************************
def buildGameBottles(expertise):
    """
    Builds and returns a list of dictionaries containing all the information
    regarding the game bottles (name, capacity and contents)

    Parameters:
    -------
    expertise : integer
        The level of expertise chosen by the user
    
    Returns:
    -------
    list
        A list of dictionaries containing the information regarding the game bottles
    """
    # Number of bottles that have to be full for the end of the game
    N = NR_BOTTLES-expertise

    # Number of symbols that have to be distributed throughout all the bottles
    numberSymbols = N * CAPACITY

    # Number of symbols per bottle
    symbolsInBottle = numberSymbols//NR_BOTTLES

    # Number of remaining symbols to be distributed
    restSymbols = (numberSymbols%NR_BOTTLES)

    # Create a list of the symbols to be distributed
    symbolList = [symbol for symbol in SYMBOLS[:N] for _ in range(CAPACITY)]
    random.shuffle(symbolList)

    # Create the list containing the information about the bottles
    bottles = []
    for i in range(NR_BOTTLES):
        bottle_name = LETTERS[i]
        bottle_symbols = symbolList[i * symbolsInBottle : (i + 1) * symbolsInBottle]
        bottles.append({"name": bottle_name, "capacity": CAPACITY, "contents": bottle_symbols})
        if restSymbols > 0:
            bottles[i]["contents"].append(symbolList[-restSymbols])
            restSymbols -= 1

    return bottles

# *****************************************************
def showBottles(bottles, nrErrors):
    """
    Writes in the standard output a representation of the bottles in the game

    Parameters:
    -------
    bottles : list
        A list of dictionaries which contains the information regarding the game bottles
    nrErrors : integer
        The number of errors the user has already committed
    """
    # Print name row
    names = " "
    for bottle in bottles:
        names += f"{bottle['name']}      "
    print(names)
    
    # Print bottles
    for i in range(CAPACITY - 1, -1, -1):
        row = ""
        for bottle in bottles:
            if i < len(bottle["contents"]):
                row += f"|{bottle['contents'][i]}|    "
            else:
                row += "| |    "
        print(row)

    # Print errors
    print("NUMBER OF ERRORS: ", nrErrors)

# *****************************************************
def askForPlay(bottles):
    """
    Asks the user for the letters that identify the source and destination bottles
    for the next "liquid" transfer, and returns those two letters

    Returns
    -------
    tuple
        A tuple containing the source and destination letters entered by the user.
    """
    # Initialize the bottles with no value
    sourceBottle = None
    destinBottle = None

    while sourceBottle is None or destinBottle is None:

        # Assign the source and destination bottles
        sourceBottleName = input("Source Bottle? ").upper()
        destinationBottleName = input("Destination bottle? ").upper()

        for bottle in bottles:
            if bottle['name'] == sourceBottleName:
                sourceBottle = bottle
            elif bottle['name'] == destinationBottleName:
                destinBottle = bottle

        # Check if the names of the bottles are valid
        if sourceBottle is None or destinBottle is None:
            print("Source or destination bottle not found.")

    return sourceBottle, destinBottle

# *****************************************************
def moveIsPossible(source, destin, bottles):
    """
    Checks if the move from the source bottle to the destination bottle is possible

    Parameters
    ----------
    source : str
        The name of the source bottle
    destin : str
        The name of the destination bottle
    bottles : list
        A list of dictionaries containing the information about the game bottles

    Returns
    -------
    boolean
        True if it is possible to transfer from the source bottle to the destination bottle, False otherwise

    Raises
    -------
    ValueError
        If the names the user entered for the source or destination bottles are not valid
    """
    # Initialize the bottles with no value
    sourceContents = None
    destinContents = None

    # Assign the source and destination bottle
    for bottle in bottles:
        if bottle['name'] == source:
            sourceContents = bottle['contents']
        elif bottle['name'] == destin:
            destinContents = bottle['contents']

    # Check if the name of the bottles are valid
    if sourceContents is None or destinContents is None:
        raise ValueError("Source or destination bottle not found.")

    # Check if the source bottle is not empty
    if sourceContents == []:
        return False

    # Check if the destination bottle is not full
    if len(destinContents) == CAPACITY:
        return False
    
    # Check if the destination bottle is empty or if top symbols are equal
    if not destinContents:
        return True
    else:
        if destinContents[-1] == sourceContents[-1]:
            return True

    return False

# *****************************************************
def doMove(source, destin, bottles):
    """
    Transfers as many equal symbols as possible from the source to the destination 
    
    Parameters
    ----------
    source : str
        The name of the source bottle
    destin : str
        The name of the destination bottle
    bottles : list
        A list of dictionaries containing the information about the game bottles
    """
    # Get contents of the bottle
    sourceContents = source['contents']
    destinContents = destin['contents']

    # Transfer the liquid from source bottle to destination bottle
    while sourceContents and len(destinContents) < CAPACITY and sourceContents != [] and (not destinContents or sourceContents[-1] == destinContents[-1]):
        destinContents.append(sourceContents.pop())

    # Ensure that the bottle contents are updated
    for bottle in bottles:
        if bottle['name'] == source['name']:
            bottle['contents'] = sourceContents
        elif bottle['name'] == destin['name']:
            bottle['contents'] = destinContents

# *****************************************************
def full(aBottle):
    """
    Checks if a bottle is filled to the top with all equal symbols
    
    Parameters
    ----------
    aBottle : dictionary
        A dictionary containing the information about the bottle

    Returns
    -------
    boolean
        True if the bottle is full with equal symbols, False otherwise
    """
    # Extract the current "liquid" from the bottle
    contents = aBottle['contents']

    # Check if the bottle is empty
    if len(contents) == 0:
        return False
    
    # Check if the bottle is full
    if len(contents) != CAPACITY:
        return False

    # Store the first symbol to compare with the rest
    firstSymbol = contents[0]

    # Check if any symbol is not the same as the first symbol
    for symbol in contents[1:]:
        if symbol != firstSymbol:
            return False

    # All symbols are equal
    return True

# *****************************************************
def allBottlesFull(fullBottles, expertise):
    """
    Checks if the user has filled all the necessary bottles to end the game
    
    Parameters
    ----------
    fullBots : integer
        The current number of full bottles in the game
    expertise : integer
        The level of expertise chosen by the user

    Returns
    -------
    boolean
        True if all the bottles necessary to win the game are full, False otherwise
    """
    # Number of bottles that have to be full for the end of the game
    bottlesEnd = NR_BOTTLES-expertise

    if bottlesEnd == fullBottles:
        return True
    else:
        return False

#######################################################
##################  MAIN PROGRAM ######################
#######################################################        
CAPACITY = 8
LETTERS = "ABCDEFGHIJ"
SYMBOLS = "@#%$!+o?§"
NR_BOTTLES = 10
LESS_EXPERT = 5
MAX_EXPERT = 1
expertise = askForExpertise()
bottles = buildGameBottles(expertise)
nrErrors = 0
fullBottles = 0 
endGame = False
ending = 0 # Added to ensure game ends as intended
showBottles(bottles, nrErrors)
# Let's play the game
while not endGame:
    source, destin = askForPlay(bottles)
    if moveIsPossible(source['name'], destin['name'], bottles):
        doMove(source, destin, bottles)
        showBottles(bottles, nrErrors)
        if full(destin):
            fullBottles += 1
            keepGo = input("Bottle filled!!! Congrats!! Keep playing? (Y/N)")
            if keepGo.upper() == "N": # Altered to ensure game ends as intended
                endGame = True
                ending = 1 # Added to ensure game ends as intended
    else:
        print("Error!")
        nrErrors += 1  
    endGame = allBottlesFull(fullBottles, expertise) or nrErrors == 3 or ending ==1 # Altered to ensure game ends as intended

print("Full bottles =", fullBottles, "  Errors =", nrErrors)
if nrErrors >= 3:
    print("Better luck next time!")
else:
    print("CONGRATULATIONS!!")
  