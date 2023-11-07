#!/usr/bin/env python
# coding: utf-8



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
    
# The use of the try and except blocks allow the detection of invalid inputs, in this case inputs that are not integers
    try: 
         # Prints an introductory statement
        print("Hello! Please answer the following questions in order to play the game.")
    
        # Asks the user to insert the value that is to be assigned to the minL variable
        minL = int(input("What is the minimum quantity of liquid the bottle will have? "))

        # Asks the user to insert the value that is to be assigned to the maxL variable
        maxL = int(input("What is the maximum quantity of liquid the bottle will have? "))
        
        # Checks if the minL is equal or bigger than zero, and if maxL is bigger than minL
        if minL < 0 or maxL <= minL:
            print(" ")
            print("Please make sure that the minimum quantity of liquid is >=0 and that the maximum quantity is higher than the lower quantity of liquid.")
            return None
        
        else:
            # Asks the user to insert the value that is to be assigned to the nrPlayers variable
            nrPlayers = int(input("How many players will be playing? "))
        
            # Checks if the the number of players is >=0
            if nrPlayers <=0:
                print(" ")
                print("The number of players has to be higher than 0.")
                return None
        
            # Returns a tuple with the values of the variables
            return minL, maxL, nrPlayers

# If any of the user input are not integers, there occurs a ValueError error, which leads to the execution of this block
    except ValueError:
        
        # Prints a statement that indicates invalid input, i.e. not integers
        print(" ")
        print("Your input was not valid. Please try again, and insert integers only.")
        return None



import random

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
        A list (of dictionaries) that represents the game players at the
        beginning of the game.

    """
    
    # Creates an empty list to which the information regarding the players will be added
    playerList=[]
    
    # Employs a for cycle which will create a dictionary for each player with their information, i.e name, score and playing status
    for i in range(1, number+1): # The number of the players starts with 1 - number (+1 so number is included)
        
        # Asks the user to input the name of player number i (the other information is = for all players in the beginning)
        name = input("Insert the name of player " + str(i) + ": ")
        player = {
            'name': name,
            'score': 0, # Every player starts with 0 points
            'playingStatus': True # Every player is playing in the beginning of the game
        }
        
        # Adds the dictionaries with the information of the players to the list
        playerList.append(player)
        
    # Returns the list with all the players information
    return playerList

def showInfoRound(nrRounds):
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
    print(f'Round {nrRounds}:')
        
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
        A value that allows calculating the left endpoint of the interval.
    deltaUp : float
        A value that allows calculating the right endpoint of the interval.

    Returns
    -------
    None.

    """
    liquid_percentage = (liquid / maxL) * 100
    bottle_length = 10
    fill_length = int(bottle_length * (liquid_percentage / 100))
    
    print(" | |")
    for i in range(bottle_length, 0, -1):
        if i == fill_length:
            print("|@@@|")
        else:
            print("|   |")

####################################
"Done until here"
####################################
def notLostYet(players, nr):
    """
    Is it the case that the player number nr hasn't yet lost the game?

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
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
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player we are referring to.

    Returns
    -------
    integer
        The quantity that the player number nr wants to add to the bottle.

    """
    while True:
        try:
            qty = int(input(f"{players[nr]['name']}, enter the quantity you want to add to the bottle: "))
            return qty
        except ValueError:
            print("Invalid input. Please enter an integer.")

# *****************************************************
def updatePlayerScores(players, nr, qty):
    """
    Updates the accumulated score of player number nr by adding it the value
    of qty

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
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
    Updates the status of the player number nr to a loser one

    Parameters
    ----------
    players : A data structure (your decision)
        A data structure containing the information about players.
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
    players : A data structure (your decision)
        A data structure containing the information about players.

    Returns
    -------
    result : boolean
        True if all players have already lost. False otherwise.

    """
    return all(not player['playingStatus'] for player in players)

# *****************************************************
def showInfoResult(bottle, maxL, players, nr, nrRounds):
    """
    Shows the information about the outcome of the game (see the examples 
    given in the text of the project)

    Parameters
    ----------
    bottle : integer
        The current content of the bottle.
    maxL : integer
        The capacity of the bottle.
    players : A data structure (your decision)
        A data structure containing the information about players.
    nr : integer
        A number that allows to identify which player has won, if any.
    nrRounds : integer
        The number of rounds played in the game.

    Returns
    -------
    None.

    """
    if bottle == maxL:
        winner = [player for player in players if player['score'] == maxL]
        if winner:
            print("Game Over!")
            print(f"{winner[0]['name']} has filled the bottle to its capacity and wins the game with {maxL} points!")
            print(f"Total rounds played: {nrRounds}")
        else:
            print("Game Over! No player filled the bottle, and it's a tie.")
    else:
        print("Game Over! All players have lost.")


# Actual Game snipnet

winBonus = 50         # The bonus to be given to the winner, if any
deltaLeft = 0.2       # Used to inform the user about the state of the bottle
deltaRight = 0.23     # Used to inform the user about the state of the bottle

minLiquid, maxL, nrPlayers = askInfoGame()

liquidInBottle = randomFill(minLiquid, maxL, useSeed = 1)

players = initializePlayers(nrPlayers)
print(players)

# It can be the case that the bottle is initially full
endGame = liquidInBottle == maxL  

nrRounds = 0
showInfoBottle(liquidInBottle, maxL, deltaLeft, deltaRight)

# Let's play the game
while not endGame:
    nrRounds += 1
    showInfoRound(nrRounds)
    # Let's play the next round
    nr = -1
    while nr < nrPlayers - 1 and not endGame:
        nr += 1
        # Only players that have not yet lost are allowed to play their turn
        if notLostYet(players, nr):
            qty = askForQuantity(players, nr)
            updatePlayerScores(players, nr, qty) 
            if qty + liquidInBottle > maxL:
                updatePlayerLost(players, nr)
                print(f"Oops! {players[nr]['name']}, you tried to overfill the bottle! The game is over for you!\n")
            else: 
                liquidInBottle += qty
                showInfoBottle(liquidInBottle, maxL, deltaLeft, deltaRight)
            # Should the game end after this turn?
            endGame = liquidInBottle == maxL or allLost(players)

showInfoResult(liquidInBottle, maxL, players, nr, nrRounds)