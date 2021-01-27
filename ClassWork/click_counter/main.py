# James hooper
# 1/22/2021
# Click Counter

from tkinter import *

class App(Frame):
    """ GUI application which counts button clicks. """
    def __init__(self,master):
        super(App,self).__init__(master)
        self.grid()
        self.total = 0
        self.colors = ["#ffffff", "Red", "Orange", "Yellow", "Green", "Blue", "Purple"]
        self.color_index = 0
        self.create_Widets()

    def create_Widets(self):
        self.lbl1 = Label(self, text = " Total People: ")
        self.lbl2 = Label(self, text = str(self.total))
        self.bttn_add = Button(self,text =  " Add Count")
        self.bttn_add.config(command = self.add_to_count)
        self.bttn_min = Button(self,text =  " Min Count")
        self.bttn_min.config(command = self.min_from_count)
        self.bttn_color = Button(self,text =  " Change Color", command = self.change_color, width = 37)

        self.bttn_color.grid()
        self.lbl1.grid()
        self.lbl2.grid()
        self.bttn_add.grid()
        self.bttn_min.grid()

    def add_to_count(self):
        self.total += 1
        self.lbl2.config(text=str(self.total))

    def min_from_count(self):
        self.total -= 1
        if self.total < 0:
            self.total = 0
        self.lbl2.config(text = str(self.total))

    def change_color(self):
        self.color_index += 1
        if self.color_index > len(self.colors) -1:
            self.color_index = 0
        self.config(bg=self.colors[self.color_index])




def main():
    root = Tk()
    root.title("Clicker Counter")
    root.geometry("260x150")
    root.resizable(0,1)
    root.attributes("-fullscreen", False)
    root.config(bg = "orange")
    app = App(root)

    root.mainloop()


main()