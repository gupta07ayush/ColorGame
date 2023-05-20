from tkinter import Tk, Label, Entry, Button
import random

# create tkinter GUI
root = Tk()

# set the title of window
root.title('Color Game')

# set the window size
root.geometry('700x500')

# Instruction Label
instruction = Label(root, text="Type the color of the words.",
                    font=("Helvetica", 20, 'bold'))
instruction.place(x=150, y=30, width=400)

# Score Label
score = Label(root, text='Press Enter to Start',
              font=("Helvetica", 15, "bold"))
score.place(x=250, y=70, width=200)

# Time left label
time = Label(root, text='Time Left: ',
             font=("Helvetica", 15, "bold"))
time.place(x=250, y=100, width=200)


# start the GUI
root.mainloop()
