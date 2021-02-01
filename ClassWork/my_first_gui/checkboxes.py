# James Hooper
# 1/28/2021
# thing that has to do with checkboxes

from tkinter import *

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.likes_Pizza = BooleanVar()
        self.likes_Tacos = BooleanVar()
        self.likes_Hotdogs = BooleanVar()
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.title_lbl = Label(self, text="Choose your favorite types of Food")
        self.select_all_lbl = Label(self, text = "Select all that apply: ")
        Checkbutton(self,
                    text="Pizza",
                    variable=self.likes_Pizza,
                    command=self.update
                    ).grid(row=2, column=0, sticky=W)
        Checkbutton(self,
                    text="Tacos",
                    variable=self.likes_Tacos,
                    command=self.update
                    ).grid(row=3, column=0, sticky=W)
        Checkbutton(self,
                    text="Hotdogs",
                    variable=self.likes_Hotdogs,
                    command=self.update
                    ).grid(row=4, column=0, sticky=W)

        self.title_lbl.grid(row=0, column=0, columnspan=2)
        self.select_all_lbl.grid(row=1, columnspan=1)

        self.worst_food = StringVar()
        self.worst_food.set(None)
        Radiobutton(self,
                    text="Food",
                    value = "Food",
                    variable = self.worst_food,
                    command=self.update
                    ).grid(row=5, column=0, sticky=W)
        Radiobutton(self,
                    text="Yams",
                    value="Yams",
                    variable=self.worst_food,
                    command=self.update
                    ).grid(row=6, column=0, sticky=W)
        Radiobutton(self,
                    text="Beats",
                    value="Beats",
                    variable=self.worst_food,
                    command=self.update
                    ).grid(row=7, column=0, sticky=W)

        self.output = Text(self)
        self.output.grid(row=8, columnspan=2)

    def update(self):
        likes = ""
        if self.likes_Pizza.get():
            likes += " you like Pizza\n"
        if self.likes_Tacos.get():
            likes += " you like Tacos\n"
        if self.likes_Hotdogs.get():
            likes += " you like Hotdogs\n"
        likes += "Your least favorite food is "+self.worst_food.get()
        self.output.delete(0.0,END)
        self.output.insert(0.0,likes)


def main():
    root = Tk()
    root.title("this is a window")
    root.geometry("643x500")
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()