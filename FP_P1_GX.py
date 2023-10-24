#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FUNDAMENTOS DE PROGRAMAÇÃO - PROJETO 1

@author: Duarte Gonçalves (nº 56095) e Pedro Travessa (nº 59479)
"""
import random
from random import seed
from random import randint
 
# *****************************************************
def askInfoGame():
    """
    Asks the user for three values that are important for the game

    Returns
    -------
    minL : integer
        The minimum quantity of liquid the bottle must have.
    maxL : integer
        The maximum quantity of liquid the bottle can have (capacity).
    nrPlayers : integer
        The number of players playing the game.

    """
# The try and except blocks allow the detection of invalid inputs, i.e. not integers
    try:     
        # Prompts user to enter value to be assigned to the minL variable
        minL = int(input("Minimum volume of bottle?  "))

        # Prompts user to enter value to be assigned to the maxL variable
        maxL = int(input("Maximum volume of bottle?  "))
        
        # Checks if the minL is equal or bigger than zero, and if maxL is bigger than minL
        if minL < 0 or maxL <= minL:
            print("\nPlease make sure that the minimum quantity of liquid is >=0 and that the maximum quantity is higher than the lower quantity of liquid.")
            return None
        
        else:
            # Prompts user to enter value to be assigned to the nrPlayers variable
            nrPlayers = int(input("How many players? "))
        
            # Checks if the the number of players is > 0
            if nrPlayers <=0:
                print("\nThe number of players has to be higher than 0.")
                return None
        
            # Returns a tuple with the values of the variables
            return minL, maxL, nrPlayers

# If any of the inputs are not integers, there occurs a ValueError error, which leads to the execution of this block
    except ValueError:
        
        # Prints a statement that indicates invalid input, i.e. not integers
        print("\nYour input was not valid. Please try again, and insert integers only.")
        return None

    
# *****************************************************
def randomFill(min, max, useSeed = 0):
    """
    Generates and returns a random integer, in the interval [min,max].
    
    Parameters
    ----------
    min : integer
        The minimum value of the random value to be generated.
    max : integer
        The minimum value of the random value to be generated.
    useSeed : integer, optional
        The seed for the random generator. The default is 0.

    Returns
    -------
    integer
        A random integer, in the interval [min,max].

    """
    # Sets the seed to ensure reproducible results
    random.seed(useSeed)
    
    # Returns the random integer generated between the interval [min,max]
    return random.randint(min,max+1) # +1 to ensure that max is included in the interval

# *****************************************************
def initializePlayers(number):
    """
    Creates and returns a list of dictionaries, where each dictionary
    corresponds to a different player. Each player has a name, a
    current number of score points (equal to the sum of the quantities
    he has already chosen), and whether they are
    still playing or have already lost.

    Parameters
    ----------
    number : integer
        The number of players that are going to play.

    Returns
    -------
    list
        A list that represents the game players at the
        beginning of the game.

    """
    # Creates an empty list to which the information regarding the players will be added
    playerList=[]

    # Creates a list for the player names to ensure different usernames
    nameList =[]
    
    # Employs a for cycle which will create a dictionary for each player with their information, i.e name, score and playing status
    for i in range(1, number+1): # The number of the players starts with 1 - number (+1 so number is included)

        # Checks if the name is different from all previous player names
        while True:
            
            # Prompts the user to enter the name of player number i
            name = input("Name of player " + str(i) + "? ")
            if name not in nameList:
                nameList.append(name) # If the name is not in the list, add it to the list
                break
            else:
                print("\nThat name is taken. Please insert a different name.") # If the name is on the list, prints error message
        
        # Creating the dictionaries with the information of each player to add to the list
        player = {
            'name': name,
            'score': 0, # Every player starts with 0 points
            'playingStatus': True # Every player is playing in the beginning of the game
        }
        
        # Adds the dictionaries with the information of the players to the list
        playerList.append(player)
        
    # Returns the list with all the players information
    return playerList


# *****************************************************
def showInfoRound(nrR):
    """
    Prints a line in the standard output informing the number of
    the current round.

    Parameters
    ----------
    nrR : integer
        The number of the current round.

    Returns
    -------
    None.

    """
    print(f"========== ROUND NUMBER {nrR} ==========")

    
# *****************************************************
def showInfoBottle(liquid, maxLiquid, deltaDown, deltaUp):
    """
    Prints several lines in the standard output informing about the
    current state of the game:
        - The first line informs about the interval of percentages within which 
          lies the current bottle content percentage. This interval depends on
          the values of deltaDown and deltaUp.
        - The next 11 lines give a somewhat visual representation of that
          interval of percentages (each line accounts for 10% ; the last one
          represents the bottom of the bottle).
    The minimum value of the left side of the interval is 0
    The maximum value of the right side of the interval is 100

    Parameters
    ----------
    liquid : integer
        The current content of the bottle.
    maxLiquid : integer
        The capacity of the bottle.
    deltaDown : float
        A value that allows to calculate the left endpoint of the interval.
    deltaUp : float
        A value that allows to calculate the right endpoint of the interval.

    Returns
    -------
    None.

    """
    # Calculates the current liquid percentage of the bottle
    liquid_percentage = (liquid / maxLiquid) * 100

    # Calculates the bounds taking into account the delta values
    lowerBound = liquid_percentage*(1-deltaLeft)
    upperBound = liquid_percentage*(1+deltaDown)
    
    # Checks if the bounds belong to the interval [0,100]. If they do not, they are altered to ensure they do
    if lowerBound <0:
        lowerBound=0
    if upperBound >100:
        upperBound=100
    
    # Prints the interval of percentages within which the bottle content percentage lies, with two decimal places
    print("The bottle is between {:.2f}% and {:.2f}% full".format(lowerBound, upperBound))

    # Defines the size of the bottle, i.e. number of partitions
    bottle_length = 10

    # Prints the visual representation of the bottle content
    for i in range(bottle_length, 0, -1):
        if lowerBound//10 < i <=upperBound//10:
            print("|@@|")
        else:
            print("|  |")
    print("----") # Represents the bottom of the bottle
    

# *****************************************************
def notLostYet(players, nr):
    """
    Checks if the player number nr is still playing or has lost the game.

    Parameters
    ----------
    players : list
        A list containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    boolean
        True if the player with number nr has not yet lost the game. 
        False otherwise.

    """
    return players[nr]['playingStatus']

# *****************************************************
def askForQuantity(players, nr):
    """
    Asks the user for the value of the quantity that the player number nr 
    wants to add to the bottle

    Parameters
    ----------
    players : list
        A list containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    integer
        The the quantity that the player number nr wants to add to the bottle.

    """
    # The while loop ensures the game will only continue if the user input is valid
    while True:

        # The try and except blocks are used to ensure valid input, i.e. integers
        try:

            # Prompts user to enter quantity to be added to the bottle and returning that value
            qty = int(input(f"Player {players[nr]['name']}: how much liquid? "))
            return qty
        
        # In case the input is NOT valid, i.e. not integers
        except ValueError:
            print("Invalid input. Please retry again, and enter an integer.")


# *****************************************************
def updatePlayerScores(players, nr, qty):
    """
    Updates the accumulated score of player number nr by adding it the value
    of qty

    Parameters
    ----------
    players : list
        A list containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.
    qty : integer
        The quantity that the player number nr decided to add to the bottle.

    Returns
    -------
    None.

    """
    players[nr]['score'] += qty


# *****************************************************
def updatePlayerLost(players, nr):
    """
    Updates the status of the player number nr to lost

    Parameters
    ----------
    players : list
        A list containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    None.

    """
    players[nr]['playingStatus'] = False
    
# *****************************************************
def allLost(players):
    """
    Is it the case that all the players have already lost the game?

    Parameters
    ----------
    players : list
        A list containing the information about players.

    Returns
    -------
    result : boolean
        True is all players have already lost. False otherwise.

    """
    # Creates a cycle thats checks every players playing status
    for player in players:
       if player['playingStatus']: # If any player still has not lost, the game continues
           return False
       
    # If all players have lost, the game ends
    return True

# *****************************************************
def showInfoResult(bottle,maxL,players,nr,nrRounds):
    """
    Shows the information about the outcome of the game

    Parameters
    ----------
    bottle : integer
        The current content of the bottle.
    maxL : integer
        The capacity of the bottle.
    players : list
        A list containing the information about players.
    nr : integer
        A number that allows to identify which player has won, if any.
    nrRounds : integer
        The number of rounds played in the game.

    Returns
    -------
    None.

    """
    print("********** GAME OVER **********")
    if bottle == maxL:
        # Creates a list for the winners
        winnerList = [player['name'] for player in players if player['playingStatus'] == True]

        # In case there is one winner
        if len(winnerList)==1:
            print("The bottle is finally full. Game over!!")
            print(f"{winnerList[0]} won the game in {nrRounds} plays")


        # In case there is more than one winner (tie)
        elif len(winnerList)>1:
            print("It's a tie. The winners are:")

        else:
            print("All players lost! The game is over")


    # In case the initial condition is not met
    else:
        print("All players lost! The game is over")

    # Prints the table format
    print(" ")
    print("FINAL SCORES:")
    print("{:<20} {:>20} {:>20}".format('NAME', 'SCORE', 'BONUS'))

   # Determines the game scores that will be displayed in the table
    for player in players:
        if player['playingStatus'] == False: # If the player has lost, they will not have a score nor bonus points
          print("{:<20} {:>20}".format(player['name'], 'Lost'))

        else: # If the player has not lost, they will have a score and bonus
          print("{:<20} {:>20} {:>20}".format(player['name'], player['score'], '50'))



#######################################################
##################  MAIN PROGRAM ######################
#######################################################
winBonus = 50         # The bonus to be given to the winner, if any
deltaLeft = 0.2       # Used to inform the user about the state of the bottle
deltaRight = 0.23     # Used to inform the user about the state of the bottle

minLiquid, maxLiquid, nrPlayers = askInfoGame()

liquidInBottle = randomFill(minLiquid, maxLiquid, useSeed = 1)
players = initializePlayers(nrPlayers)

# It can be the case that the bottle is iniatilly full
endGame = liquidInBottle == maxLiquid  

nrRounds = 0
showInfoBottle(liquidInBottle, maxLiquid, deltaLeft, deltaRight)

# Let's play the game
while not endGame:
    nrRounds += 1
    showInfoRound(nrRounds)
    # Let's play the next round
    nr = -1
    while nr < nrPlayers - 1 and not endGame:
        nr += 1
        # Only players that have not yet lost, are allowed to play their turn
        if notLostYet(players, nr):
           qty = askForQuantity(players, nr)
           updatePlayerScores(players, nr, qty) 
           if qty + liquidInBottle > maxLiquid:
              updatePlayerLost(players, nr)
              print("Oops! You tried to overfill the bottle! The game is over for you!\n")
           else: 
              liquidInBottle += qty
              showInfoBottle(liquidInBottle, maxLiquid, deltaLeft, deltaRight)
           # Should the game end after this turn?
           endGame = liquidInBottle == maxLiquid or allLost(players)

showInfoResult(liquidInBottle,maxLiquid,players,nr,nrRounds)







