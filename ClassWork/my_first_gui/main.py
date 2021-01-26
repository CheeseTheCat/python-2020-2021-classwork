# James Hooper
# 1/20/2021
# My First Gui
# simple gui in a window

from tkinter import *

# creates the window
root = Tk()

# sets the title
root.title("Gui thing")

# sets the default size of the window
root.geometry("1000x700")

# makes the window not resizeable
#root.resizable(0,0)

# makes it full screen by default
#root.attributes("-fullscreen",True)

# sets the bacground color
root.configure(background = "black")
#or
root.configure(bg = "#FF6F00")

# makes it translucent
#root.attributes("-alpha", .75)

# create frame to place widgets on
app = Frame(root)
app.grid()

# create labels
lbl = Label(app, text = "This is a label",bg = "lightgrey")
#lbl.config(font = ("Courier", 44))
lbl.grid()

# make buttons
bttn1 = Button(app, text = "Don't Click Me!")
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
for i in range(5):
    x1 = Button(app)
    x1["text"] = "button " + str(i+1)
    x1.grid()
bttn2.config(text = "This is another Button")

#kick off the window's event loop
root.mainloop()

