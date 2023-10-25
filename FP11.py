#env python3
#coding: utf-8
"""
FUNDAMENTOS DE PROGRAMAÇÃO - GRUPO 11

@author's: Duarte Gonçalves (nº 56095) e Pedro Travessa (nº 59479)
"""
import random
from random import seed
from random import randint
 
# *****************************************************
def askInfoGame():
    """
    Asks the user for three values that are important for the game:
    The minimum and maximum quantities of liquid the bottle can have, and the number of players.

    Returns:
    A tuple containing three integers: the minimum quantity of liquid the 
    bottle must have (minL); the maximum quantity of liquid the bottle can 
    have (maxL) and the number of players playing the game (nrPlayers). 
    If any input is invalid (not an integer), a message is printed and None is returned.

    Raises a ValueError:
    If any of the inputs are not integers, a ValueError occurs, which leads 
    to the execution of a block that prints a statement indicating invalid input.
        
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
    Generates and returns a random integer within a specified interval.

    Parameters:
    "min" represents the minimum value of the random integer to be generated.
    "max" represents the maximum value of the random integer to be generated.
    "useSeed" represents the seed for the random generator. The default is 0.

    Returns:
    A random integer within the interval [min, max].
    """
    # Sets the seed to ensure reproducible results
    random.seed(useSeed)
    
    # Returns the random integer generated between the interval [min,max]
    return random.randint(min,max+1) # +1 to ensure that max is included in the interval

# *****************************************************
def initializePlayers(number):
    """
    Creates and returns a list of players for the game.
    Each player is represented by a dictionary containing their name, score, and playing status.

    Parameters:
    "number" represetns the number of players that are going to play.

    Returns:
    A list of dictionaries, each representing a player.
    Each dictionary contains 'name', 'score', and 'playingStatus' keys.
    The 'name' value is obtained from user input, the 'score' value is initialized as 0, and 
    the 'playingStatus' value is initialized to True.
        
    """
    # Creates an empty list to which the information regarding the players will be added
    playerList=[]

    # Creates a list for the player names to ensure different usernames
    nameList =[]
    
    # Employs a for cycle which will create a dictionary for each player with their information, i.e name, score and playing status
    for i in range(1, number+1): # The number of the players starts with 1 - number (+1 so number is included)

        """    # Checks if the name is different from all previous player names
        while True:
            
            # Prompts the user to enter the name of player number i
            name = input("Name of player " + str(i) + "? ")
            if name not in nameList:
                nameList.append(name) # If the name is not in the list, add it to the list
                break #Prof doesn't like the use of break fucntions
            else:
                print("\nThat name is taken. Please insert a different name.") # If the name is on the list, prints error message
        """            
        name = None
        while name is None or name in nameList:
            # Ask's user to enter a player name
            name = input("Name of player " + str(i) + "? ")
            if name in nameList:
                print("\nThat name is taken. Please insert a different name.")

        nameList.append(name)  # Add the name to the list to ensure it's not used again

        
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
    Prints information about the current round number.

    Parameters:
    "nrR" represents the number of the current round.

    Output:
    Text informing about the current round number.   
    """
    print(f"========== ROUND NUMBER {nrR} ==========")

    
# *****************************************************
def showInfoBottle(liquid, maxL, deltaLeft, deltaRight):
    """
        Prints information about the current state of the game, including an interval 
        of percentages within which lies the current bottle content percentage and a 
        visual representation of that interval.

        Parameters:
        "liquid" represents the current content of the bottle.
        "maxL" represents the capacity of the bottle.
        "deltaLeft" is a value used to calculate the left endpoint of the interval.
        "deltaRight" likewise deltaLeft it's the value used to calculate the right endpoint of the interval.

        Output:
        It prints the current state of the game.
        The first line informs about the interval of percentages which lies on the current bottle 
        filling percentage. The next 11 lines gives a visual representation of that interval
        (each line accounts for 10%; the last one represents the bottom of the bottle).
        """
    # Calculates the current liquid percentage of the bottle
    liquid_percentage = (liquid / maxL) * 100

    # Calculates the bounds taking into account the delta values
    lowerBound = liquid_percentage*(1-deltaLeft)
    upperBound = liquid_percentage*(1+deltaRight)
    
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
        Checks if all players have lost the game.

        Parameters:
        "players" represents a list of dictionaries, each containing information about a player.
        "nr" represents an index that identifies the player in the players list.

        Returns:
        A boolean value, False if the players have lost and True otherwise.
    """
    return players[nr]['playingStatus']

# *****************************************************
def askForQuantity(players, nr):
    """
    Asks a player for the quantity they want to add to the bottle.

    Parameters:
    "players" represents a list of dictionaries, each containing information about a player.
    "nr" represents an index that identifies the player in the players list.

    Asks:
    The quantity that the player wants to add to the bottle. This is obtained 
    from user input and must be an integer.
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
    Updates the accumulated score of a player by adding a specified quantity.

    Parameters:
    "players" represents a list of dictionaries, each containing information about a player. 
    "nr" represents an index that identifies the player in the players list.
    "qty" represents the quantity to be added to the player's score.

    The 'score' value of the player's dictionary in the "players" list is increased by qty.
    """
    players[nr]['score'] += qty


# *****************************************************
def updatePlayerLost(players, nr):
    """
    Updates the status of a player to lost.

    Parameters:
    "players" represents a list of dictionaries, each containing information about a player. 
    "nr" represents an index that identifies the player in the players list.

    The 'playingStatus' value of the player's dictionary in the players list 
    is set to False, indicating that the player has lost.
    """
    players[nr]['playingStatus'] = False
    
# *****************************************************
def allLost(players):
    """
        Checks if all players have lost the game.

        Parameters:
        "players" represents a list of dictionaries, each containing information about a player. 

        Returns:
        A boolean value, True if all players have lost and False otherwise.
    """
    # Creates a cycle thats checks every players playing status
    for player in players:
       if player['playingStatus']: # If any player still has not lost, the game continues
           return False
       
    # If all players have lost, the game ends
    return True

# *****************************************************
def showInfoResult(bottle, maxL, players, nrRounds):
    """
        Shows the information about the outcome of the game.

        Parameters:
        "bottle" represents the current content of the bottle.
        "maxL" represents the capacity of the bottle.
        "players" represents a list containing dictionaries with information about each player. 
        "nrRounds" represents the number of rounds played in the game.

        Output:
        Prints the game's outcome, including whether it's a tie, who the winners are, 
        and the final scores and bonuses for all players. If a player has lost, 
        their score is displayed as 'Lost'. Otherwise, their score and a bonus 
        of 50 points are displayed.
    """
    print("********** GAME OVER **********")
    
    # Create a list of players who haven't lost
    active_players = [player for player in players if player['playingStatus']]
    
    if bottle == maxL and active_players:
        # Sort the active players by their score in descending order
        active_players.sort(key=lambda player: player['score'], reverse=True)
        top_score = active_players[0]['score']
        
        # Find the winners with the highest score
        winners = [player for player in active_players if player['score'] == top_score]
        
        if len(winners) == 1:
            print(f"The bottle is finally full. Game over!!")
            if nrRounds ==1:
                print(f"{winners[0]['name']} won the game in {nrRounds} round and gets a bonus of 50 points.")
            if nrRounds >1:
                print(f"{winners[0]['name']} won the game in {nrRounds} rounds and gets a bonus of 50 points.")
        else:
            print("It's a tie!")
            print(f"The Winners have the same score of {top_score}. Receiving the bonus of 50 points each.")
            print("The Winners are:")
            for winner in winners:
                print(winner['name'])
            
        
    else:
        print("All players lost! The game is over")
    
    # Print the table format
    print(" ")
    print("FINAL SCORES:")
    print("{:<25} {:>20} {:>20}".format('NAME', 'SCORE', 'BONUS'))
    
    # Print the players' scores and bonuses for players who haven't lost
    for player in players:
        if player['playingStatus'] is False:
            print("{:<25} {:>20}".format(player['name'], 'Lost'))
        else:
            print("{:<25} {:>20} {:>20}".format(player['name'], player['score'], (winBonus) if player in winners else '0'))


#######################################################
##################  MAIN PROGRAM ######################
#######################################################
winBonus = 50         # The bonus to be given to the winner, if any
deltaLeft = 0.2       # Used to inform the user about the state of the bottle
deltaRight = 0.23005     # Used to inform the user about the state of the bottle

minL, maxL, nrPlayers = askInfoGame()

liquid = randomFill(minL, maxL, useSeed = 1)
players = initializePlayers(nrPlayers)

# It can be the case that the bottle is iniatilly full
endGame = liquid == maxL  

nrRounds = 0
showInfoBottle(liquid, maxL, deltaLeft, deltaRight)

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
           if qty + liquid > maxL:
              updatePlayerLost(players, nr)
              print("Oops! You tried to overfill the bottle! The game is over for you!\n")
           else: 
              liquid += qty
              showInfoBottle(liquid, maxL, deltaLeft, deltaRight)
           # Should the game end after this turn?
           endGame = liquid == maxL or allLost(players)

showInfoResult(liquid,maxL,players,nrRounds)

