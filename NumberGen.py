import os
import sys
import numpy as np
import random
import ttkbootstrap as ttk
from tkinter import *
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

def updateWindow(nums, tvs):
    # Clear the frame
    for widget in secondFrame.winfo_children():
        widget.destroy()
    outerFrame.geometry("400x700")
    #ttk.Scrollbar(secondFrame, orient='vertical').pack(side='right', fill='y')
    ttk.Label(secondFrame, text="Placements", style='warning.TLabel', font=("Helvetica", 30, "bold")).pack(side = 'top', pady=30 )
    ttk.Label(secondFrame, text="Number of Players: " + str(nums), style='TLabel').pack(pady=0)
    ttk.Label(secondFrame, text="Number of TVs: " + str(tvs), style='TLabel').pack(pady=0)
    placements(nums, tvs)
 
def onSubmit():
    num = int(inputnum.get())
    tvs = int(inputtvs.get())
    updateWindow(num, tvs)

def reset():
    # Clear the frame
    for widget in secondFrame.winfo_children():
        widget.destroy()
    
    # Recreate the initial labels and input fields
    ttk.Label(secondFrame, text="Mario Kart Tournament Generator", style='warning.TLabel', font=("Helvetica", 16, "bold")).pack(pady=40, anchor='center')

    ttk.Label(secondFrame, text="Number of Players", style='info.TLabel').pack(pady=10, anchor='center')
    global inputnum  # Declare as global to modify outside of function
    inputnum = ttk.Spinbox(secondFrame, from_=1, to=100, style='info.TSpinbox')
    inputnum.pack(pady=10, anchor='center')

    ttk.Label(secondFrame, text="Number of TVs", style='info.TLabel').pack(pady=10, anchor='center')
    global inputtvs  # Declare as global to modify outside of function
    inputtvs = ttk.Spinbox(secondFrame, from_=1, to=100, style='info.TSpinbox')
    inputtvs.pack(pady=10, anchor='center')

    # Button
    global b  # Declare as global to modify outside of function
    b = ttk.Button(secondFrame, text='Submit', style='info.TButton', command=onSubmit)
    b.pack(padx=5, pady=10, anchor='center')
    imageLabel = ttk.Label(secondFrame, image=photo)
    imageLabel.image = photo
    imageLabel.pack(side = BOTTOM, pady =10)

def showAbout():
    aboutWindow = Toplevel(outerFrame)
    aboutWindow.title("About")
    aboutWindow.geometry("800x400")
    about_label = ttk.Label(aboutWindow, text="This is the Mario Kart Tournament Generator.\nVersion 1.0\nDeveloped by Lucas de la Pena", font=("Helvetica", 12))
    about_label.pack(pady=50)
    description_label = ttk.Label(aboutWindow, text="Description:", font=("Helvetica", 12))
    description_label.pack(pady=5)
    
    descrip1 = ttk.Label(aboutWindow, text="This program generates the placements for a Mario Kart tournament. It takes the number of players and the \n number of TVs as input and outputs the placements for each round. If the players can be divisable by 3 \n it will ask the user if they want to divide the player into groups of 3", font=("Helvetica", 12))
    descrip1.pack(pady=1)
    descrip3 = ttk.Label(aboutWindow, text="Bovey is stanky", font=("Helvetica", 12))
    descrip3.pack(pady=1)

def generateNumbers(num):
    oneRemaining, twoRemaining, threeRemaining = False, False, False
    
    if num % 4 == 0: #if the number is evenly divisible
        playerPerTv = 4
    
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

def threePerTv(players, tvs, nums):
    for widget in secondFrame.winfo_children():
        widget.destroy()

    ttk.Label(secondFrame, text="Placements", style='warning.TLabel', font=("Helvetica", 30, "bold")).pack(side = 'top', pady=30 )
    ttk.Label(secondFrame, text="Number of Players: " + str(nums), style='TLabel').pack(pady=0)
    ttk.Label(secondFrame, text="Number of TVs: " + str(tvs), style='TLabel').pack(pady=0)
    round = 0
    playerPerTv = 3
    while len(players) > 0: #works with 7 and up
        round += 1
        for i in range(tvs):
            if i == 0 and len(players) != 0:
                ttk.Label(secondFrame, text="Round " + str(round), style='danger.TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
            if len(players) != 0:
                ttk.Label(secondFrame, text="TV "+ str(i+1), style='TLabel', font=("Helvetica", 12, "bold")).pack(pady=10)
            for j in range(playerPerTv):
                if len(players) == 0:
                    break
                ttk.Label(secondFrame, text= "Player " + str(players[j]), style='info.TLabel').pack(pady=0)
            if len(players) == 0:
                break
            players = np.delete(players, range(playerPerTv)) # Remove the players that have been printed
            print()

    ttk.Label(secondFrame, text="", style='success.TLabel', font=("Helvetica", 18, "bold")).pack(pady=50)
    
def placements(num, tvs):
    # Calculate Players per TV
    playerPerTv, oneRemaining, twoRemaining, threeRemaining = generateNumbers(num)

    #players array 
    players = np.arange(1, num+1)

    #Generate the numbers
    random.shuffle(players)
    round = 0
    #ttk.Label(frame, text="" + str(tvs), style='TLabel').pack(pady=0)
    
    if num % 3 == 0:
        ttk.Label(secondFrame, text="This is divisible by 3.", style='danger.TLabel', font="bo").pack(pady=(20,0))
        ttk.Label(secondFrame, text="Did you want to have 3 players per tv?", style='TLabel').pack(pady=0)
        players2 = players
        three = ttk.Button(secondFrame, text='3 per tv', style='info.TButton', command=lambda: threePerTv(players2, tvs, num))
        three.pack(padx=5, pady=10, anchor='center')

    if len(players) <= 4:

        ttk.Label(secondFrame, text="Round 1", style='danger.TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
        ttk.Label(secondFrame, text="TV 1", style='TLabel', font=("Helvetica", 12, "bold")).pack(pady=10)
        length = len(players)
        for j in range(length):
            ttk.Label(secondFrame, text= "Player " + str(players[j]), style='info.TLabel').pack(pady=0)
        players = np.delete(players,length) # Remove the players that have been printed

    if len(players) == 5:
        ttk.Label(secondFrame, text="Round 1", style='danger.TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
        ttk.Label(secondFrame, text="TV 1", style='TLabel', font=("Helvetica", 12, "bold")).pack(pady=10)
        for j in range(3):
            ttk.Label(secondFrame, text= "Player " + str(players[j]), style='info.TLabel').pack(pady=0)
        players = np.delete(players,range(3)) # Remove the players that have been printed
        print()
        ttk.Label(secondFrame, text="Round 2", style='danger.TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
        ttk.Label(secondFrame, text="TV 2", style='TLabel', font=("Helvetica", 12, "bold")).pack(pady=10)
        for j in range(2):
            ttk.Label(secondFrame, text= "Player " + str(players[j]), style='info.TLabel').pack(pady=0)
        players = np.delete(players,range(2)) # Remove the players that have been printed

    while len(players) > 0: #works with 7 and up
        round += 1
        for i in range(tvs):
            if i == 0 and len(players) != 0:
                ttk.Label(secondFrame, text="Round " + str(round), style='danger.TLabel', font=("Helvetica", 18, "bold")).pack(pady=10)
            if len(players) != 0:
                ttk.Label(secondFrame, text="TV "+ str(i+1), style='TLabel', font=("Helvetica", 12, "bold")).pack(pady=10)
            for j in range(playerPerTv):
                if len(players) == 0:
                    break
                ttk.Label(secondFrame, text= "Player " + str(players[j]), style='info.TLabel').pack(pady=0)
            if len(players) == 0:
                break
            players = np.delete(players, range(playerPerTv)) # Remove the players that have been printed
            if oneRemaining and len(players) == 9 or twoRemaining and len(players) == 6 or threeRemaining and len(players) == 3:
                #dividing the remaining players by 3
                playerPerTv = 3
            print()

    ttk.Label(secondFrame, text="", style='success.TLabel', font=("Helvetica", 18, "bold")).pack(pady=50)

def on_mouse_wheel(event):
    myCanvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def centerFrame(event):
    canvasWidth = event.width
    frameWidth = secondFrame.winfo_reqwidth()
    x = (canvasWidth - frameWidth) // 2
    myCanvas.coords(windowId, x, 0)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Window
outerFrame = ttk.Window(themename="darkly")
outerFrame.title("Mario Kart Tournament Generator")

# Size
outerFrame.geometry("400x450") #make the window smaller

# Canvas
myCanvas = Canvas(outerFrame)
myCanvas.pack(side=LEFT, fill=BOTH, expand=True)
myCanvas.bind("<Configure>", centerFrame)

# scrollbar
myScrollbar = ttk.Scrollbar(outerFrame, orient=VERTICAL, command=myCanvas.yview)
myScrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas to scroll with the scrollbar
outerFrame.bind("<Configure>", lambda e: myCanvas.configure(scrollregion=myCanvas.bbox("all")))
myCanvas.configure(yscrollcommand=myScrollbar.set)

# Bind the mouse wheel event to the canvas
myCanvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Second Frame
secondFrame = ttk.Frame(myCanvas)
myCanvas.create_window((0,0), window=secondFrame, anchor="nw")
windowId = myCanvas.create_window((0, 0), window=secondFrame, anchor="nw")


# Menu
menu = Menu(outerFrame)
outerFrame.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Reset', command=reset)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=outerFrame.quit)

#Help menu
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About', command=showAbout)

# Labels
ttk.Label(secondFrame, text="Mario Kart Tournament Generator", style='warning.TLabel', font=("Helvetica", 16, "bold")).pack(pady=40, anchor='center')

ttk.Label(secondFrame, text="Number of Players", style='info.TLabel').pack(pady=10, anchor='center')
inputnum = ttk.Spinbox(secondFrame, from_=1, to=100, style='info.TSpinbox')
inputnum.pack(pady=10, anchor='center')

ttk.Label(secondFrame, text="Number of TVs", style='info.TLabel').pack(pady=10, anchor='center')
inputtvs = ttk.Spinbox(secondFrame, from_=1, to=100, style='info.TSpinbox')
inputtvs.pack(pady=10, anchor='center')

# Button
b = ttk.Button(secondFrame, text='Submit', style='info.TButton', command=onSubmit)
b.pack(padx=5, pady=10, anchor='center')

# Image
imagePath = resource_path("yoshi.png")
image = Image.open(imagePath)
image = image.resize((50, 50), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Create a label with the image
imageLabel = ttk.Label(secondFrame, image=photo)
imageLabel.image = photo
imageLabel.pack(side = BOTTOM, pady =10)

outerFrame.mainloop()
