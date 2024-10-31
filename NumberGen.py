import numpy as np
import random

def generateNumbers(num, tvs):
    if num % tvs == 0: #if the number is evenly divisible
        playerPerTv = num // tvs

    else:
        playerPerTv = num // tvs + 1

    return playerPerTv

def main():
    #Number of players
    num = int(input("How many players? "))
    #Number of tvs
    tvs = int(input("How many tvs are you using? "))
    #Number of numbers per tv
    #playerPerTv = int(input("How many players per tv? "))
   
    # Calculate Players per TV
    playerPerTv = generateNumbers(num, tvs)

    #players array 
    players = np.arange(1, num+1)

    #Generate the numbers
    random.shuffle(players)

    for i in range(tvs):
        print(f"TV {i + 1}:")
        for j in range(playerPerTv):
            if len(players) == 0:
                break
            print(f"  Player {players[0]}")
            players = np.delete(players, 0)
        print()  # Print an empty line for separation



"""""
    while len(players) > 0:
        for i in range(tvs):
            for j in range(playerPerTv):

                if len(players) == 0:
                    break

                print("TV:", i+1, " Player: ", players[j]) #Print the player number

            if len(players) == 0:
                break

            players = np.delete(players, range(playerPerTv)) # Remove the players that have been printed
            print()
"""""
        

if __name__ == "__main__":
    main()
