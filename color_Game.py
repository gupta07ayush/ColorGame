from tkinter import Tk, Label, Entry, Button
import random

# create tkinter GUI
root = Tk()

# set the title of window
root.title('Color Game')

# set the window size
root.geometry('700x500')

# Add an Instruction Label
instruction = Label(root, text="Type the color of the words.",
                    font=("Helvetica", 20, 'bold'))
instruction.place(x=150, y=30, width=400)


# start the GUI
root.mainloop()
