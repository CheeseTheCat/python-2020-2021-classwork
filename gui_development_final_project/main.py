# James Hooper and Emily Briggs
# Basic Calculator

from tkinter import *
from tkinter.ttk import *
#declare the expression variable

HEIGHT = 200
WIDTH = 302
TITLE = "Calculator"
BACKGROUND = "black"

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.screen = ""
        self.opperand1 = None
        self.opperand2 = None
        self.opperator = ""

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.spacerlbl1 = Label(self,text="").grid(row=0, columnspan=4)
        self.output = Text(self, height=2, width = 37)
        self.output.grid(row=1, columnspan=4)

        self.bttn_0 = Button(self, text="0", command=self.number_0).grid(row=5, column=0)
        self.bttn_1 = Button(self, text="1", command=self.number_1).grid(row=4, column=0)
        self.bttn_2 = Button(self, text="2", command=self.number_2).grid(row=4, column=1)
        self.bttn_3 = Button(self, text="3", command=self.number_3).grid(row=4, column=2)
        self.bttn_4 = Button(self, text="4", command=self.number_4).grid(row=3, column=0)
        self.bttn_5 = Button(self, text="5", command=self.number_5).grid(row=3, column=1)
        self.bttn_6 = Button(self, text="6", command=self.number_6).grid(row=3, column=2)
        self.bttn_7 = Button(self, text="7", command=self.number_7).grid(row=2, column=0)
        self.bttn_8 = Button(self, text="8", command=self.number_8).grid(row=2, column=1)
        self.bttn_9 = Button(self, text="9", command=self.number_9).grid(row=2, column=2)

        self.dot_bttn = Button(self, text=".", command=self.dot_button).grid(row=5, column=1)
        self.add_bttn = Button(self, text="+", command=self.add_button).grid(row=5, column=3)
        self.sub_bttn = Button(self, text="-", command=self.sub_button).grid(row=4, column=3)
        self.mult_bttn = Button(self, text="X", command=self.mult_button).grid(row=3, column=3)
        self.div_bttn = Button(self, text="/", command=self.div_button).grid(row=2, column=3)
        self.clearBttn = Button(self, text="All Clear", command=self.clear_button
                                ).grid(row=5, column=2)


    def number_0(self):
        self.screen += "0"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_1(self):
        self.screen += "1"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_2(self):
        self.screen += "2"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_3(self):
        self.screen += "3"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_4(self):
        self.screen += "4"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_5(self):
        self.screen += "5"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_6(self):
        self.screen += "6"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_7(self):
        self.screen += "7"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_8(self):
        self.screen += "8"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def number_9(self):
        self.screen += "9"
        self.output.delete(0.0, END)
        self.output.insert(0.0, self.screen)

    def dot_button(self):
        if not "." in self.screen:
            self.screen += "."
            self.output.delete(0.0, END)
            self.output.insert(0.0, self.screen)

    def add_button(self):
        self.opperand1 = int(self.screen)
        self.opperator = "+"

    def sub_button(self):
        self.opperand1 = int(self.screen)
        self.opperator = "-"

    def mult_button(self):
        self.opperand1 = int(self.screen)
        self.opperator = "*"

    def div_button(self):
        self.opperand1 = int(self.screen)
        self.opperator = "/"

    def clear_button(self):
        text_output = ""
        self.screen = ""
        self.opperand1 = None
        self.opperand2 = None
        self.opperator = ""
        self.output.delete(0.0, END)
        self.output.insert(0.0, text_output)



def main():
    root = Tk()
    root.title(TITLE)
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = BACKGROUND)
    app = App(root)

    root.mainloop()

main()