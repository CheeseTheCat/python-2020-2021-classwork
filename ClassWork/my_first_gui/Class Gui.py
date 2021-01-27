# James Hooper
# 1/20/2021
# Class Gui
from tkinter import *
class Application(Frame):
    """ A Gui app with tree buttons"""
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.clicks = 0

    def create_widgets(self):
        self.tclbl = Label(self, text = "Total Clicks")
        self.numclicks = Label(self, text = str(self.clicks))

        self.addbttn = Button(self, text = "Add to Clicks")
        self.minbttn = Button(self, text = "take away from Clicks")

        self.colorbttn = Button(self, text = "Change Background Color")

        self.colorbttn.grid()
        self.tclbl.grid()
        self.numclicks.grid()
        self.addbttn.grid()
        self.minbttn.grid()


root = Tk()
root.title("Gui thing")
root.geometry("1000x700")
root.configure(bg = "#FF6F00")
app = Application(root)

root.mainloop()
