import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def updateWindow(nums, tvs):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()
    
    ttk.Label(frame, text="Placements", style='TLabel', font=("Helvetica", 30, "bold")).pack(side = 'top', pady=30 )
    ttk.Label(frame, text="Number of Players: " + str(nums), style='info.TLabel').pack(pady=10)
    ttk.Label(frame, text="Number of TVs: " + str(tvs), style='info.TLabel').pack(pady=10)
   

def onSubmit():
    num = int(inputnum.get())
    tvs = int(inputtvs.get())
    updateWindow(num, tvs)

root = ttk.Window(themename="darkly")
root.title("Mario Kart Tournament Generator")

root.geometry("500x500")

frame = ttk.Frame(root)
frame.pack(expand = True)

ttk.Label(frame, text="Mario Kart Tournament Generator", style='TLabel', font=("Helvetica", 16, "bold")).pack(pady=40)

ttk.Label(frame, text="Number of Players", style='info.TLabel').pack(pady=10)
inputnum = ttk.Spinbox(frame, from_=1, to=100, style='info.TSpinbox')
inputnum.pack(pady=10)

ttk.Label(frame, text="Number of TVs", style='info.TLabel').pack(pady=10)
inputtvs = ttk.Spinbox(frame, from_=1, to=100, style='info.TSpinbox')
inputtvs.pack(pady=10)

b = ttk.Button(frame, text='Submit', style='info.TButton', command=onSubmit)
b.pack(padx=5, pady=10)

root.mainloop()