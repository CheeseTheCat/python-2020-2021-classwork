# James Hooper
# 1/28/2021
# Pizza Ordering App

from tkinter import *

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_cb(self,words,ischecked,commandcall,r,c,cs=1,rs=1):
        self.ischecked=BooleanVar()
        Checkbutton(self,
                    text = words,
                    variable = ischecked,
                    command = commandcall
                    ).grid(row=r,column=c,columnspan=cs,rowspan=rs)


    def create_widgets(self):


        Label(self,
              text = "Ordering Pizza\n Please place your order below"
              ).grid(row=0, columnspan=2)
        Label(self,
              text = "Pizza Size: "
              ).grid(row=1, column=0)
        self.pizza_size = StringVar()
        self.pizza_size.set("Medium")
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
        Label(self,
              text = "Crust Type: "
              ).grid(row=1, column=1)
        self.pizza_crust = StringVar()
        self.pizza_crust.set("Normal")
        Radiobutton(self,
                    text="Normal",
                    value="Normal",
                    variable=self.pizza_crust,
                    command=self.update
                    ).grid(row=2, column=1)
        Radiobutton(self,
                    text="Stuffed",
                    value="Stuffed",
                    variable=self.pizza_crust,
                    command=self.update
                    ).grid(row=3, column=1)
        Radiobutton(self,
                    text="No Crust",
                    value="No Crust",
                    variable=self.pizza_crust,
                    command=self.update
                    ).grid(row=4, column=1)
        Label(self,
              text = "Toppings: "
              ).grid(row=5, column=0, columnspan=2)
        self.chz = BooleanVar()
        self.chzz = BooleanVar()
        self.chzzz = BooleanVar()
        self.pep = BooleanVar()
        self.pna = BooleanVar()
        self.ham = BooleanVar()
        self.mush = BooleanVar()
        self.olv = BooleanVar()
        self.pepp = BooleanVar()
        self.yougurt1 = BooleanVar()
        self.yougurt2 = BooleanVar()
        self.yougurt3 = BooleanVar()
        self.boolsvars = [self.chz,self.chzz,self.chzzz,self.pep,self.pna,self.ham,self.mush,self.olv,self.pepp,self.yougurt1,self.yougurt2,self.yougurt3]
        self.toppings = ["Cheese","Extra Cheese","Extra Extra Cheese","Pepperoni","Pineapple","Ham","Mushrooms","Olives","Yogurt thing","Yogurt thing","Yogurt thing"]
        index=0
        for r in range(6):
            for c in range(2):
                self.create_cb(self.toppings[index],self.boolsvars[index],self.update,r+6,c)
                index+=1

        self.user_address = Entry(self)
        self.user_number = Entry(self)

        self.user_address.grid(row=12, column=1, sticky=W)
        self.user_number.grid(row=13, column=1, sticky=W)
        Label(self,
              text="Address: "
              ).grid(row=12, column=0, sticky=E)
        Label(self,
              text="Phone Number: "
              ).grid(row=13, column=0, sticky=E)

        self.output = Text(self)
        self.output.grid(row=14, columnspan=2)


    def update(self):
        size = ""
        size += "Pizza Size: " +self.pizza_size.get()
        crust = ""
        crust += "Crust Type: "+self.pizza_crust.get()
        toppings = "Toppings:  "
        if self.topping_Cheese.get():
            toppings += "Cheese, "
        if self.topping_Cheese_extra.get():
            toppings += "Extra Cheese, "
        if self.topping_Cheese_extra_extra.get():
            toppings += "Extra Extra Cheese, "
        if self.topping_Pepperoni.get():
            toppings += "Pepperoni, "
        if self.topping_Pineapple.get():
            toppings += "Pineapple, "
        if self.topping_Ham.get():
            toppings += "Ham, "
        if self.topping_Mushrooms.get():
            toppings += "Mushrooms, "


        if toppings == "Toppings:  ":
            toppings = "Toppings: None"

        text_output = size + "\n" + crust + "\n" + toppings
        self.output.delete(0.0,END)
        self.output.insert(0.0,text_output)


def main():
    root = Tk()
    root.title("Pizza Order")
    root.geometry("643x500")
    root.configure(bg = "white")
    app = App(root)

    root.mainloop()

main()