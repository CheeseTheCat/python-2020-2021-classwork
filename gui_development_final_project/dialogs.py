# James Hooper
# 2/3/2021
# dialogs

from tkinter import *
from tkinter import messagebox as mb
HEIGHT = 500
WIDTH = 500

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack(fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        error=Button(self, text="Error",command=self.onError)
        error.grid(padx=5,pady=5)
        warning=Button(self, text="Warning",command=self.onWarn)
        warning.grid(row=1,column=0)
        question=Button(self,text="Question",command=self.onQuest)
        question.grid(row=0, column=1)
        inform=Button(self,text="Infromation", command=self.onInfo)
        inform.grid(row=1,column=1)

    def onError(self):
        mb.showerror("Error","could not open File")

    def onWarn(self):
        mb.showwarning("Warning","Intruder Detected")

    def onQuest(self):
        result = mb.askquestion("Question","Are you sure you want to quit?")
        if result=="yes":
            print("you clicked yes")
        else:
            print("you clicked no")

    def onInfo(self):
        mb.showinfo("Info","Download completed now installing minecraft")


def main():
    root = Tk()
    root.title("Title")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()