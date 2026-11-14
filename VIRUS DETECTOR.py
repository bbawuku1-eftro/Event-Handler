# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter window
root = Tk()
root.geometry("200x200")

# Function for displaying warning message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be dislayed")
def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button widget to the window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()