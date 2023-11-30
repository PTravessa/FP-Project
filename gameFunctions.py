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
    level of minimum expertise, total number of bottles, letters and symbols that will be
    used to fill the bottles

    Parameters
    ----------
    fileName : str
        The name of the file containing information regarding the game

    Returns
    -------

    Requires
    --------
        The file fileName must exist and it must contain the valid information
        necessary to play the game

    Raises
    ------

    """
    try:
        with open (fileName, 'r') as file:
            data = file.read().split('\n')

            # Level of expertise
            MAX_EXPERT = int(data[0])
            LESS_EXPERT = int(data[1])
            expertise = randint(MAX_EXPERT,LESS_EXPERT+1)

            # Number of bottles that have to full by the end of the game
            totalNumberOfBottles = int(data[2])
            #fullBottlesByEnd = totalNumberOfBottles - expertise

            # Bottle size
            bottleSize = int(data[3])

            # Letters and symbols
            letters = str(data[4])
            symbols = str(data[5])

            # Dictionary containing bottle information
            bottleInfo = buildGameBottles(totalNumberOfBottles,bottleSize,expertise,letters,symbols)

            # New games start with 0 bottles full and 0 errors
            fullBottles = 0
            errors = 0

        return expertise,totalNumberOfBottles, fullBottles, bottleSize, bottleInfo, errors

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{fileName}' does not exist. Please try again with a valid file!")
    except IOError:
        raise IOError(f"The file '{fileName}' does not contain valid information about the game! Please try again with a different file!")

#print(newGameInfo('new.txt'))


# *****************************************************
def oldGameInfo(fileName):
    """
    Description

    Parameters
    ----------
    fileName : string
        The name of the file.

    Returns
    -------
    """
    try:
        with open(fileName, 'r') as file:
            data = file.read().split('\n')

            expertise = int(data[0])

            totalNumberOfBottles = int(data[1])

            fullBottles = int(data[2])

            bottleSize = int(data[3])

            bottleInfo_str = data[4].replace("'", "\"")
            print(bottleInfo_str)
            bottleInfo = eval(bottleInfo_str)

            errors = int(data[5])   
          
        return expertise,totalNumberOfBottles, fullBottles, bottleSize, bottleInfo, errors
 
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{fileName}' does not exist. Please try again with a valid file!")
    except IOError:
        raise IOError(f"The file '{fileName}' does not contain valid information about the game! Please try again with a different file!")




# *****************************************************
def writeGameInfo(fileName,expertise,totalNumberOfBottles,fullBottles,bottleSize,bottleInfo,errors):
    """
    Description

    Parameters
    ----------
    fileName : string
        The name of the file.

    Returns
    -------

    """
    with open(fileName,'w') as file:
        file.write(str(expertise) + '\n')
        file.write(str(totalNumberOfBottles) + '\n')
        file.write(str(fullBottles) + '\n')
        file.write(str(bottleSize) + '\n')
        file.write(str(bottleInfo) + '\n')
        file.write(str(errors) + '\n')
    file.close()
