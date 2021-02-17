# James Hooper
# 2/3/2021
# tkinter template

from tkinter import *
from tkinter import colorchooser
HEIGHT = 500
WIDTH = 500

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn = Button(self,text="Choose color",command=self.onChoose)
        self.bttn.grid(row=0,column=0)
        self.frame=Frame(self,border=1,relief=SUNKEN, width=100, height=100)
        self.frame.grid(row=1,column=0)



    def onChoose(self):
        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)





def main():
    root = Tk()
    root.title("Color Chooser")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()