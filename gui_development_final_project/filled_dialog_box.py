# James Hooper
# 2/3/2021
# tkinter template

from tkinter import *
from tkinter import filedialog

HEIGHT = 500
WIDTH = 500

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar=Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu=Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File",menu=fileMenu)
        self.text=Text(self)
        self.text.grid(row=1,column=1)

    def onOpen(self):
        ftypes=[("Python file","*.py"),("Allfiles","*")]
        dlg = filedialog.Open(self,filetypes=ftypes)
        f1=dlg.show()
        if f1 != "":
            text = self.readFile(f1)
            self.text.insert(END,text)

    def readFile(selfself,filename):
        with open(filename, "r") as f:
            text = f.read()
        return text




def main():
    root = Tk()
    root.title("Color Chooser")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()