#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on:

@author:
"""

from random import randint
from random import shuffle

# *****************************************************
def topSymbolAndPosition(contents):
    """
    The symbol and position of the top of the bottle, that is,
    of the last position of the list contents

    Parameters
    ----------
    contents : a sequence of characters
        The contents of a bottle.

    Returns
    -------
    symbol : string
        The symbol at the last position. "_" if contents is empty.
    position : int
        The index of the last position. -1 if contents is empty.

    """
    position = len(contents) - 1
    symbol = "_" if contents == [] else contents[position]
    return symbol, position

# *****************************************************
def showBottles(bottles,botSize,nrErrors):
    """
    Prints in the standard output a representation of the
    game bottles.

    Parameters
    ----------
    bottles : dictionary
        Keys are strings and values are lists.
    botSize : int
        The capacity of bottles.
    nrErrors : int
        The number of errors the user already made.

    Returns
    -------
    None.

    """
    print(" " * 3, end = "")
    for letter in bottles.keys():
        print(letter, end = " " * 6) 
    print()
    
    line = botSize - 1
    while line >= 0:
       for content in bottles.values():
           print(" " * 2, end = "")
           if line < len(content):
               print("|" + content[line] + "|", end = "")
           else:
               print("| |", end = "")               
           print(" " * 2, end = "")
       line -= 1
       print()
    print("NUMBER OF ERRORS:", nrErrors)
# *****************************************************
def allBottlesFull(nrBotts, nrBottFull, expert):
    """
    Are all the bottles that are supposed to be full at the end  
    of the game already full?

    Parameters
    ----------
    nrBotts : int
        The number of bottles in the game.
    nrBottFull : int
        The number of bottles already full (with equal symbol).
    expert : int
        The user's expert level.

    Returns
    -------
    True if the number of bottles that are supposed to be full at
    the end of the game is already achieved.

    """
    expectFull = nrBotts - expert
    return nrBottFull == expectFull
# *****************************************************
def full(bottle, botSize):
    """
    Is a given bottle all full with a same symbol?

    Parameters
    ----------
    bottle : list of characters
        The contents of a bottle.
    botSize : int
        The capacity of the bottle.

    Returns
    -------
    bool
        True if the list bottle has botSize elements, all equal.

    """
    if len(bottle) < botSize:
        return False
    top = bottle[0]
    for char in bottle:
        if not char == top:
            return False
    return True

# *****************************************************
def doMove(botSize, source, destin, bottles):
    """
    Transfers as much "liquid" as possible from source to destin

    Parameters
    ----------
    botSize : int
        The capacity of bottles.
    source : string
        The letter that identifies the source bottle in the dict bottles.
    destin : string
        The letter that identifies the destination bottle in the dict bottles.
    bottles : dictionary
        Keys are strings and values are lists.

    Returns
    -------
    int
        The quantity of "liquid" that was transferred from source to destin.

    Requires: 
    --------
        moveIsPossible(botSize, source, destin, bottles)
    """
    sourceSymb, sourceTop = topSymbolAndPosition(bottles[source])
    destSymb, destTop = topSymbolAndPosition(bottles[destin])    
    # How many there are in source to transfer?
    howManyEqual = 0
    i = sourceTop
    sourceContent = bottles[source]
    while i >= 0 and sourceContent[i] == sourceSymb:
       i -= 1
       howManyEqual += 1
    # Transfer as many as possible
    transfer = min(howManyEqual, botSize - destTop - 1)
    for i in range(transfer):
        sourceContent.pop()
        bottles[destin].append(sourceSymb)
    
    return transfer
# *****************************************************
def moveIsPossible(botSize, source, destin, bottles):
    """
    Is it possible to transfer any "liquid" from source to destin?

    Parameters
    ----------
    botSize : int
        The capacity of bottles.
    source : string
        The letter that identifies the source bottle in the dict bottles.
    destin : string
        The letter that identifies the destination bottle in the dict bottles.
    bottles : dictionary
        Keys are strings and values are lists.

    Returns
    -------
    bool
        True if the source is not empty, and, either the destination is empty
        or it has some empty position(s) and the top symbols of both bottles
        are the same.

    Requires: 
    --------
        bottles contain keys source and destin

    """
    sourceSymb, sourceTop = topSymbolAndPosition(bottles[source])
    destSymb, destTop = topSymbolAndPosition(bottles[destin])    
 
    return sourceTop != -1 and \
           (destTop == -1 or
           (destTop < botSize - 1 and sourceSymb == destSymb)) 
# ***************************************************************
def buildGameBottles(nrBotts, botSize, expert, letters, symbols):
    """
    Builds a dictionary of bottles, filled in a random way.

    Parameters
    ----------
    nrBotts : int
        The number of bottles in the game.
    botSize : int
        The capacity of bottles.
    expert : int
        The level of the user's expertise.
    letters : string
        The letters that identify bottles.
    symbols : string
        The symbols that compose the liquid in bottles.

    Returns
    -------
    result : dictionary where keys are strings and values are lists. 
        The dictionary contains nrBotts items, whose keys are the first nrBotts
        characters of letters. The different symbols used to populate the lists
        corresponding to keys are the first (nrBotts - expert) characters of
        symbols. In total, ((nrBotts - expert) * botSize) symbols will be
        randomly distributed by the nrBotts bottles.

    Requires: 
    --------
        letters length is >= nrBotts; symbols length is >= (nrBotts - expert);
        expert < nrBotts

    """   
    result = {}
    howManyFullBott = nrBotts - expert
    allSymbols = randomSymbols(botSize,howManyFullBott,symbols)
    letter = 0
    indexFrom = 0
    # In this way we obtain a more balanced symbol distribution
    indexTo = randint(botSize - expert,botSize)
    for nr in range(nrBotts - 1):
        symbolsToPut = allSymbols[indexFrom : indexTo]
        result[letters[letter]] = symbolsToPut
        letter += 1
        indexFrom = indexTo
        newValueTo = indexTo + randint(botSize - expert,botSize)
        indexTo = min(len(allSymbols), newValueTo)
    symbolsToPut = allSymbols[indexFrom : indexTo]
    result[letters[letter]] = symbolsToPut
        
    return result
# *****************************************************
def randomSymbols(botSize, howMany, symbols):
    """
    Builds and returns a list with (botSize * howMany) characters of symbols

    Parameters
    ----------
    botSize : int
        Capacity of bottles.
    howMany : int
        The number of different symbols to be used.
    symbols : string
        The symbols that can be used.

    Returns
    -------
    list of characters

    Requires: 
    --------
        symbols length is >= howMany;

    """
    # botSize chars of each of the first howMany symbols
    symbolsToUse = symbols[0:howMany]
    result = [s for s in symbolsToUse for _ in range(botSize)]
    shuffle(result)
    return result

# *****************************************************
def askUserFor(ask, options, end = ""):
    """
    Asks the user for some information

    Parameters
    ----------
    ask : string
        The text to be shown the user.
    options : sequence
        The options the user has.
    end : string, optional
        Additional messages to add to the above options. 
        The default is "".

    Returns
    -------
    string
        The user's choice (that belongs to the available options),
        in uppercase.

    """
    listOptions = list(options) + [end]
    answer = input(ask).upper()
    while answer not in listOptions:
       answer = input("Wrong choice! Repeat input: ").upper()
     
    return answer

# *****************************************************
# ***************** NEW FUNCTIONS HERE ****************
# *****************************************************


def newGameInfo(fileName):
    """
    Opens and reads the information in the fileName file, which contains valid
    information about the game in the following order: level of maximum expertise,
    level of minimum expertise, total number of bottles, letters, and symbols that will be
    used to fill the bottles

    Parameters
    ----------
    fileName : str
        The name of the file containing information regarding the game

    Returns
    -------
    tuple
        A tuple containing expertise, fullBottlesByEnd, and bottleInfo

    Requires
    --------
        The file fileName must exist and it must contain the valid information
        necessary to play the game

    Raises
    ------
    Exception
        If the file is not found or if it does not contain valid information about the game

    """
    try:
        with open(f'{fileName}.txt', 'r') as file:
            dataLines = file.read().split('\n')

            # Level of expertise
            MAX_EXPERT = int(dataLines[0])
            LESS_EXPERT = int(dataLines[1])
            expertise = randint(MAX_EXPERT, LESS_EXPERT)

            # Number of bottles that have to be full by the end of the game
            totalNumberOfBottles = int(dataLines[2])
            fullBottlesByEnd = totalNumberOfBottles - expertise

            # Bottle size
            bottleSize = int(dataLines[3])

            # Letters and symbols
            letters = dataLines[4]  # Assuming the 5th line contains letters
            symbols = dataLines[5]  # Assuming the 6th line contains symbols

            # Dictionary containing bottle information
            bottleInfo = buildGameBottles(totalNumberOfBottles, bottleSize, expertise, letters, symbols)

            return expertise, fullBottlesByEnd, bottleInfo

    except FileNotFoundError:
        print(f"The file '{fileName}.txt' does not exist. Creating a new file with initial game information.")

        # Initialize initial game information (modify this part according to your game logic)
        MAX_EXPERT = 1
        LESS_EXPERT = 5
        expertise = randint(MAX_EXPERT, LESS_EXPERT)
        totalNumberOfBottles = 10
        fullBottlesByEnd = totalNumberOfBottles - expertise
        bottleSize = 8
        letters = "ABCDEFGHIJ"
        symbols = "@#%$!+o?§"

        # Create a new file and write the initial game information
        with open(f'{fileName}.txt', 'w') as new_file:
            new_file.write(f"{MAX_EXPERT}\n{LESS_EXPERT}\n{totalNumberOfBottles}\n{bottleSize}\n{letters}\n{symbols}")

        # Return the initial game information
        return expertise, fullBottlesByEnd, buildGameBottles(totalNumberOfBottles, bottleSize, expertise, letters, symbols)

    except ValueError:
        raise Exception(f"The file '{fileName}.txt' does not contain valid information about the game! Please try again with a different file!")

# *****************************************************
def oldGameInfo(fileName):
    """
    Reads information about an old game from a file and returns the necessary values.

    Parameters
    ----------
    fileName : str
        The name of the file containing the game information.

    Returns
    -------
    tuple
        A tuple containing the necessary values for an old game.

    Raises
    ------
    FileNotFoundError
        If the file is not found.
    ValueError
        If the file contents are not as expected.

    """
    try:
        with open(fileName, 'r') as file:
            # Read expertise level from the file
            expertise = int(file.readline().strip())

            # Read the number of full bottles from the file
            fullBottles = int(file.readline().strip())

            # Read the number of errors from the file
            nrErrors = int(file.readline().strip())

            # Read the contents of each bottle from the file
            bottles = {}
            for letter in letters[:expertise]:
                contents = file.readline().strip()
                bottles[letter] = list(contents)

            # Return the necessary values for an old game
            return bottles, botSize, nrErrors, expertise, fullBottles
    except FileNotFoundError:
        raise FileNotFoundError(f"File {fileName} not found.")
    except ValueError:
        raise ValueError(f"Unexpected content in file {fileName}.")


def writeGameInfo(fileName, bottles, botSize, nrErrors, expertise, fullBottles):
    """
    Writes information about the game to a file for future playing.

    Parameters
    ----------
    fileName : str
        The name of the file to store the game information.
    bottles : dict
        A dictionary representing the game bottles.
    botSize : int
        The capacity of bottles.
    nrErrors : int
        The number of errors made in the game.
    expertise : int
        The level of user expertise.
    fullBottles : int
        The number of bottles that are already full.

    Returns
    -------
    None

    """
    try:
        with open(fileName, 'w') as file:
            # Write expertise level to the file
            file.write(str(expertise) + '\n')

            # Write the number of full bottles to the file
            file.write(str(fullBottles) + '\n')

            # Write the number of errors to the file
            file.write(str(nrErrors) + '\n')

            # Write the contents of each bottle to the file
            for letter in LETTERS[:expertise]:
                file.write(''.join(bottles[letter]) + '\n')
    except Exception as e:
        print(f"An error occurred while writing to {fileName}: {e}")