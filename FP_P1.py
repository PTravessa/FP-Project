#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


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


# In[4]:


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
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


winBonus = 50         # The bonus to be given to the winner, if any
deltaLeft = 0.2       # Used to inform the user about the state of the bottle
deltaRight = 0.23     # Used to inform the user about the state of the bottle

minLiquid, maxLiquid, nrPlayers = askInfoGame()

liquidInBottle = randomFill(minLiquid, maxLiquid, useSeed = 1)

players = initializePlayers(nrPlayers)
print(players)


# In[ ]:





# In[ ]:




