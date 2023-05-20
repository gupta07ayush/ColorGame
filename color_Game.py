from tkinter import Tk, Label, Entry, Button
import random

# create tkinter GUI
root = Tk()

# set the title of window
root.title('Color Game')

# set the window size
root.geometry('700x500')

# background color of the window
root.config(bg="#d6ccc2")


# list of possible colors.
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially it is 30 seconds.
timeleft = 30


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

# Label for displaying the colors name
colors_name = Label(root, font=('Helvetica', 20, 'bold'))
colors_name.place(x=200, y=150, width=400, height=100)

# text entry fox for typing
color_entry = Entry(root, font=('helvetica', 15, ))
color_entry.place(x=300, y=300, width=200, height=30)


# start the GUI
root.mainloop()
