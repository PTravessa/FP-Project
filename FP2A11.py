#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FUNDAMENTOS DE PROGRAMAÇÃO - PROJETO 2

@author: Duarte Gonçalves (nº 56095) e Pedro Travessa (nº 59479) - GRUPO 11
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

    ValueError:
    Raises an error if the value isn't within the range and asks to prompt again the input

    """
    while True:
        # Prompt user to enter value of the expertise they want
        exp = input("Expert level - from 1 (radical) to 5 (beginner)? ")

        try:
            # Try to convert the user input to an integer
            exp = int(exp)

            # Check if the user input is within the valid range
            if exp in [1, 2, 3, 4, 5]:
                return exp
            else:
                print("Please enter a value between 1 and 5.")
        except ValueError:
            # If conversion to int fails, handle the ValueError
            print("Invalid input. Please enter a valid integer.")

# *****************************************************
def buildGameBottles(expertise):
    """
    Builds and returns a list of dictionaries containing all the information
    regarding the game bottles (name, capacity and "liquid")

    Parameters:
    -------
    expertise : integer
        The level of expertise chosen by the user
    
    Returns:
    -------
    list
        A list of dictionaries containing the information regarding the game bottles
    """

    # Create a variable that represents the number of bottles that have to be full by the end of the game
    N = NR_BOTTLES-expertise

    # Create a variable that represents the amount of symbols that have to be distributed throughout all the bottles
    numberSymbols = N * 8

    # Number of symbols per bottle
    symbolsInBottle = int(numberSymbols/NR_BOTTLES)

    # Create an empty list of symbols to be distributed
    symbolList = [symbol for symbol in SYMBOLS[:N] for _ in range(8)]
    random.shuffle(symbolList)

    # Create the list of arrays
    bottles = []
    for i in range(NR_BOTTLES):
        bottle_name = LETTERS[i]
        bottle_symbols = symbolList[i * symbolsInBottle : (i + 1) * symbolsInBottle]
        bottles.append({"name": bottle_name, "capacity": CAPACITY, "contents": bottle_symbols})

    # Return the list containing information about the bottles
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
        The number of errors the user has already commited

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
def askForPlay():
    """
    Asks the user for the letters that identify the source and destination bottles
    for the next "liquid" transfer, and returns those two letters

    Returns
    -------
    tuple
        A tuple containing the source and destination letters entered by the user.

    Raises
    -------
    ValueError if the user input was not valid
    """
    # Initialize the bottles with no value
    sourceBottle = None
    destinBottle = None

    sourceBottle = input("Source Bottle? ").upper()
    destinationBottle = input("Destination bottle? ").upper()

    # Assign the source and destination bottle
    for bottle in bottles:
        if bottle['name'] == sourceBottle:
            sourceBottle = bottle
        elif bottle['name'] == destinationBottle:
            destinBottle = bottle

    # Check if the name of the bottles are valid
    if sourceBottle is None or destinBottle is None:
         raise ValueError("Source or destination bottle not found.")

    return sourceBottle, destinationBottle

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
    """
    sourceContents = None
    destinContents = None

    for bottle in bottles:
        if bottle['name'] == source:
            sourceContents = bottle['contents']
        elif bottle['name'] == destin:
            destinContents = bottle['contents']

    # Check if the source bottle is not empty
    if len(sourceContents) == 0 or sourceContents == None:
        return False

    # Check if the destination bottle is not full
    if len(destinContents) != CAPACITY or destinContents == None:
        return False

    # Check if the last symbol in the destination bottle is the same as the symbol in the source bottle
    if destinContents[-1] == sourceContents[-1]:
        return True

    return False

# *****************************************************
def doMove(source, destin, bottles):
    """
    Transfers as many symbols as possible from the source to the destination 
    
    Parameters
    ----------
    source : char
        The name of the source bottle
    destin : char
        The name of the destination bottle
    bottles : list
        A list of dictionaries containing the information about the game bottles
    """

    sourceContents = source['contents']
    destinContents = destin['contents']

    sourceTop = len(sourceContents) - 1
    destinTop = len(destinContents) - 1

    sourceTopSymbol = sourceContents[sourceTop]
    destTopSymbol = destinContents[destinTop]

    while sourceTopSymbol == destTopSymbol and destinTop < source['capacity']:
        destinContents[destinTop] = sourceContents[sourceTop]
        sourceContents[sourceTop] = ' '
        destinTop -= 1
        sourceTop -= 1

        if sourceTop < 0:
            break

        sourceTopSymbol = sourceContents[sourceTop]
        destTopSymbol = destinContents[destinTop]
   
# *****************************************************
def full(aBottle):
    """
    Checks if a bottle is filled with all equal symbols
    
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
        return True

    # Store the first symbol to compare with the rest
    firstSymbol = contents[0]

    # Check if any symbol is not the same as the first symbol
    for symbol in contents[1:]:
        if symbol != firstSymbol:
            return False

    # All symbols are equal
    return True


# *****************************************************
def allBottlesFull(fullBots, expertise):
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
        True if all the bottles are full, False otherwise
    """

    # Calculate number of bottles that have to be full for the end of the game
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
showBottles(bottles, nrErrors)
# Let's play the game
while not endGame:
    source, destin = askForPlay()
    if moveIsPossible(source, destin, bottles):
        doMove(source, destin,bottles)
        showBottles(bottles, nrErrors)
        if full(bottles[destin]):
            fullBottles += 1
            keepGo = input("Bottle filled!!! Congrats!! Keep playing? (Y/N)")
            if keepGo == "N":
                endGame = True
    else:
        print("Error!")
        nrErrors += 1
    endGame = allBottlesFull(fullBottles, expertise) or nrErrors == 3

print("Full bottles =", fullBottles, "  Errors =", nrErrors)
if nrErrors >= 3:
    print("Better luck next time!")
else:
    print("CONGRATULATIONS!!")
  