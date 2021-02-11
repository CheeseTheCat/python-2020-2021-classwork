from tkinter import *
import os


HEIGHT = 200
WIDTH = 200
TITLE = "new program"
BACKGROUND = "darkgray"
FONT = "San_Serif"



class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.col = 0
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu = menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit",command=self.onExit)
        fileMenu.add_command(label="Open",command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.onSave)
        menubar.add_cascade(label="File",menu=fileMenu)

        editmenu = Menu(menubar)
        editmenu.add_command(label="create frame", command=self.createframe)
        editmenu.add_command(label="destroy frame", command=self.destroyframe)
        menubar.add_cascade(label="Edit", menu=editmenu)

        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_separator()
        fileMenu.add_cascade(label="import", menu=submenu)
        fileMenu.add_separator()


    def onExit(self):
        self.quit()
    def onOpen(self):
        os.system("checkboxes.py")
    def onSave(self):
        pass
    def destroyframe(self):
        self.frame1.destroy
    def createframe(self):
        self.frame1 = Frame(self, bg="red", width=250, height=250)
        self.frame1.grid(row=1, column=self.col)
        self.lbl1 = Label(self.frame1, text="testing")
        self.lbl1.pack(padx=20, pady=20, fill=BOTH, expand=1)
        self.lbl1["text"] = "change"
        self.col+=1


def main():
    root = Tk()
    root.geometry(str.format("{}x{}",WIDTH,HEIGHT))
    root.title(TITLE)
    root.config(bg = BACKGROUND)
    app = App(root)
    root.mainloop()

main()
