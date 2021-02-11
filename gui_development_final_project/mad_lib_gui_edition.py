

from tkinter import *
from tkinter.ttk import *
HEIGHT = 500
WIDTH = 500
TITLE = "title"
BACKGROUND = "white"

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        pass


def main():
    root = Tk()
    root.title(TITLE)
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = BACKGROUND)
    app = App(root)

    root.mainloop()

main()