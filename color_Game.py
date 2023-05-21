from tkinter import Tk, Label, Entry, END
import random

# create tkinter GUI
root = Tk()

# set the title of window
root.title('Color Game')

# set the window size
root.geometry('700x500')

# background color of the window
# root.config(bg="white")


# list of possible colors.
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
          'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially it is 30 seconds.
timeleft = 30

# function that will start the game


def startGame(event):
    if timeleft == 30:
        # start the countdown
        countdown()

    # run the function to choose the next color
    nextColor()

# function to choose and display the next color


def nextColor():

    # use the globally declared 'score' and 'timeleft' variables above.
    global score
    global timeleft

    # if a game is currently in play
    if timeleft > 0:

        # make the text entry box active
        color_entry.focus_set()

        # if the color typed is equal to the color of the text
        if color_entry.get().lower() == colors[1].lower():
            score += 1

        # clear the text entry box
        color_entry.delete(0, END)

        random.shuffle(colors)

        # change the color to type, by changing the
        # text and the color to a random color value
        color_name.config(fg=str(colors[1]), text=str(colors[0]))

        # update the score
        score_label.config(text="Score: " + str(score))

# Countdown timer function


def countdown():
    global timeleft

    # if a game is in play
    if timeleft > 0:
        # decrement the timer
        timeleft -= 1

        # update the time left label
        time.config(text='Time left: ' + str(timeleft))

        # run the function again after 1 second
        time.after(1000, countdown)


# Instruction Label
instruction = Label(root, text="Type the color of the words.",
                    font=("Helvetica", 20, 'bold'))
instruction.place(x=150, y=30, width=400)

# Score Label
score_label = Label(root, text='Press Enter to Start',
                    font=("Helvetica", 15, "bold"))
score_label.place(x=250, y=70, width=200)

# Time left label
time = Label(root, text='Time Left: ' + str(timeleft),
             font=("Helvetica", 15, "bold"))
time.place(x=250, y=100, width=200)

# Label for displaying the color name
color_name = Label(root, font=('Helvetica', 50, 'bold'))
color_name.place(x=150, y=150, width=400, height=100)

# text entry fox for typing
color_entry = Entry(root, font=('helvetica', 15, ))

# Run the 'startGame' function when the enter key is pressed
root.bind('<Return>', startGame)

color_entry.place(x=250, y=300, width=200, height=30)


# set focus on the entry box
color_entry.focus_set()


# start the GUI
root.mainloop()
