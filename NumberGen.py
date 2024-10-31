import numpy as np
import random

def main():
    #Number of players
    num = int(input("How many players? "))
    #Number of tvs
    tvs = int(input("How many tvs are you using? "))
    #Number of numbers per tv
    playerPerTv = int(input("How many players per tv? "))

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
            print()
        

if __name__ == "__main__":
    main()
