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

    for i in range(tvs):
        for j in range(playerPerTv):
            print("TV:", i+1, " Player: ", players[j])
        players = np.delete(players, range(playerPerTv))
        print()
        
    if len(players) > 0:
        print("Remaining players: ")
        for i in range(len(players)):
            print("Player: ", players[i])



if __name__ == "__main__":
    main()
