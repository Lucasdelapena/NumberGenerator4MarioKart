import numpy as np
import random

def generateNumbers(num):
    oneRemaining, twoRemaining, threeRemaining = False, False, False
    
    if num % 4 == 0: #if the number is evenly divisible
        playerPerTv = 4

    elif num % 3 == 0: #3 playres per tv
        playerPerTv = 3
    
    else:
        playerPerTv = 4
        if num % 4 == 1:
            #last 3 tvs will have 3 players
            oneRemaining = True
        elif num % 4 == 2:
            #last 2 tvs will have 3 players
            twoRemaining = True
        elif num % 4 == 3:
            #last tv will have 3 players
            threeRemaining = True

    return playerPerTv, oneRemaining, twoRemaining, threeRemaining

def main():
    #Number of players
    num = int(input("How many players? "))
    #Number of tvs
    tvs = int(input("How many tvs are you using? "))

    # Calculate Players per TV
    playerPerTv, oneRemaining, twoRemaining, threeRemaining = generateNumbers(num)

    #players array 
    players = np.arange(1, num+1)

    #Generate the numbers
    random.shuffle(players)

    while len(players) > 0:
        for i in range(tvs):
            for j in range(playerPerTv):
                if len(players) == 0:
                    break
                print("TV:", i+1, " Player: ", players[j]) #Print the player number
            if len(players) == 0:
                break
            players = np.delete(players, range(playerPerTv)) # Remove the players that have been printed
            if oneRemaining and len(players) == 9 or twoRemaining and len(players) == 6 or threeRemaining and len(players) == 3:
                #dividing the remaining players by 3
                playerPerTv = 3
            print()

        

if __name__ == "__main__":
    main()
