
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from mainchat import *
root = tk.Tk()

Label(root, text = 'click the mic..', font =( 'Verdana', 15)).pack(side = TOP, pady = 10)
root.iconphoto(False, tk.PhotoImage(file = "icons8-microphone-64.png"))
photo = PhotoImage(file = "icons8-microphone-64.png")
btn = Button(root,image = photo, command = mainbot) 
btn.pack()
root.mainloop()



