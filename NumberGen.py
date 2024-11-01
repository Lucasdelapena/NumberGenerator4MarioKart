import numpy as np
import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def updateWindow(nums, tvs):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    ttk.Label(frame, text="Placements", style='warning.TLabel', font=("Helvetica", 30, "bold")).pack(side = 'top', pady=30 )
    ttk.Label(frame, text="Number of Players: " + str(nums), style='TLabel').pack(pady=0)
    ttk.Label(frame, text="Number of TVs: " + str(tvs), style='TLabel').pack(pady=0)
    placements(nums, tvs)

    
def onSubmit():
    num = int(inputnum.get())
    tvs = int(inputtvs.get())
    updateWindow(num, tvs)


def generateNumbers(num):
    oneRemaining, twoRemaining, threeRemaining = False, False, False
    
    if num % 4 == 0: #if the number is evenly divisible
        playerPerTv = 4

    #elif num % 3 == 0: #3 playres per tv
        #playerPerTv = 3
    
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

def placements(num, tvs):
    # Calculate Players per TV
    playerPerTv, oneRemaining, twoRemaining, threeRemaining = generateNumbers(num)

    #players array 
    players = np.arange(1, num+1)

    #Generate the numbers
    random.shuffle(players)
    round = 0

    while len(players) > 0:
        round += 1
        for i in range(tvs):
            if i == 0 and len(players) != 0:
                ttk.Label(frame, text="Round " + str(round), style='danger.TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
            if len(players) != 0:
                ttk.Label(frame, text="TV "+ str(i+1), style='TLabel', font=("Helvetica", 12, "bold")).pack(pady=10)
            for j in range(playerPerTv):
                if len(players) == 0:
                    break
                #print("TV:", i+1, " Player: ", players[j]) #Print the player number
                #ttk.Label(frame, text="TV "+ i+1, style='TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
                ttk.Label(frame, text= "Player " + str(players[j]), style='info.TLabel').pack(pady=0)
            if len(players) == 0:
                break
            players = np.delete(players, range(playerPerTv)) # Remove the players that have been printed
            if oneRemaining and len(players) == 9 or twoRemaining and len(players) == 6 or threeRemaining and len(players) == 3:
                #dividing the remaining players by 3
                playerPerTv = 3
            print()

    ttk.Label(frame, text="End of Tournament", style='success.TLabel', font=("Helvetica", 18, "bold")).pack(pady=100)

#Window
root = ttk.Window(themename="darkly")
root.title("Mario Kart Tournament Generator")

#Size
root.geometry("700x700")

#Canvas and scrollbar
canvas = ttk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

#Frame inside the canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="n")

#Configure the canvas to scroll with the scrollbar
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.configure(yscrollcommand=scrollbar.set)

#mouseWheel
canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

#Labels
ttk.Label(frame, text="Mario Kart Tournament Generator", style='warning.TLabel', font=("Helvetica", 16, "bold")).pack(pady=40, anchor = 'center')

ttk.Label(frame, text="Number of Players", style='info.TLabel').pack(pady=10)
inputnum = ttk.Spinbox(frame, from_=1, to=100, style='info.TSpinbox')
inputnum.pack(pady=10, anchor = 'center')

ttk.Label(frame, text="Number of TVs", style='info.TLabel').pack(pady=10)
inputtvs = ttk.Spinbox(frame, from_=1, to=100, style='info.TSpinbox')
inputtvs.pack(pady=10, anchor = 'center')

#Button
b = ttk.Button(frame, text='Submit', style='info.TButton', command=onSubmit)
b.pack(padx=5, pady=10, anchor = 'center')

root.mainloop()