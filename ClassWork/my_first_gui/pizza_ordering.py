# James Hooper
# 1/28/2021
# Pizza Ordering App

from tkinter import *

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.pizza_size =BooleanVar()
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        Label(self,
              text = "Ordering Pizza\n Please place your order below"
              ).grid(row=0, columnspan=2)
        Label(self,
              text = "Pizza Size: "
              ).grid(row=1, column=0)
        Radiobutton(self,
                    text="Small",
                    value="Small",
                    variable=self.pizza_size,
                    command=self.update
                    ).grid(row=2, column=0)
        Radiobutton(self,
                    text="Medium",
                    value="Medium",
                    variable=self.pizza_size,
                    command=self.update
                    ).grid(row=3, column=0)
        Radiobutton(self,
                    text="Large",
                    value="Large",
                    variable=self.pizza_size,
                    command=self.update
                    ).grid(row=4, column=0)

        self.user_address = Entry(self)
        self.user_number = Entry(self)

        #self.user_address.grid(row=3)
        #self.user_number.grid(row=4)

        self.output = Text(self)
        self.output.grid(row=8, columnspan=2)


    def update(self):
        size = self.pizza_size.get()



        self.output.delete(0.0,END)
        self.output.insert(0.0,size)


def main():
    root = Tk()
    root.title("password entry")
    root.geometry("643x500")
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()