# James Hooper
# 2/3/2021
# tkinter template

from tkinter import *
HEIGHT = 500
WIDTH = 500

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        pass



def main():
    root = Tk()
    root.title("Title")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()