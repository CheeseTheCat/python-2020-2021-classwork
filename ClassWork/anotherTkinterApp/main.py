# James Hooper
# tkinter template

from tkinter import *
from tkinter.ttk import *
HEIGHT = 500
WIDTH = 500
TITLE = "This is a Dropdown list"
BACKGROUND = "white"

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pack(fill=X)
        self.create_widgets()

    def create_widgets(self):
        self.itemslist = [1,2,3,4,5,"hello"]
        self.combobox = Combobox(self,values = self.itemslist)
        self.combobox.current(0)
        self.combobox.pack(side=LEFT)

        # list box
        self.listbox = Listbox(self)
        listitems = ["Hi", "Hello", "pizzaburger", 1, 2, 3]
        for i in range(len(listitems)):
            self.listbox.insert(i, listitems[i])
        self.listbox.pack(side=LEFT)

        self.progressbar = Progressbar(self,length=200,value = 50)
        self.progressbar.pack(side=LEFT)

        self.increase = Button(self, text=">>>>>", command = self.inc)
        self.increase.pack(side=LEFT)
        self.decrease = Button(self, text="<<<<<", command = self.dec)
        self.decrease.pack(side=LEFT)

        self.submit = Button(self, text="Try Me", command=self.on_change_values)
        self.submit.pack(side=LEFT)

    def inc(self):
        self.progressbar['value']=self.progressbar['value']+1

    def dec(self):
        self.progressbar['value']=self.progressbar['value']-1



    def on_change_values(self):
        cbtext = self.combobox.get()
        print(cbtext)
        self.listbox.insert(END, cbtext)
        lbtext = self.listbox.get(ANCHOR)
        print(lbtext)
        #itemslist.append(lbtext)
        #self.combobox["value"]=self.itemslist




def main():
    root = Tk()
    root.title(TITLE)
    #root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = BACKGROUND)
    app = App(root)

    root.mainloop()

main()