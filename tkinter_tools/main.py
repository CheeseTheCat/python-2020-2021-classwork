# James Hooper
# 2/3/2021
# more things made with tkinter

from tkinter import *
from PIL import Image, ImageTk
HEIGHT = 750
WIDTH = 250


class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.index = 0
        self.pack(fill=BOTH,expand=1)
        self.create_widgets()

    def create_widgets(self):
        Label(text="my favorite Images",width=20).place(x=WIDTH/2-70,y=5)
        # load Images
        img1 = Image.open("bearing.jpg")
        img2 = Image.open("diamondblock.jpg")
        img3 = Image.open("pizzaburger.jpg")
        # convert img to tk objects
        logo1=ImageTk.PhotoImage(img1)
        logo2=ImageTk.PhotoImage(img2)
        logo3=ImageTk.PhotoImage(img3)
        self.imglist = [logo1,logo2,logo3]

        self.imglbl1 = Label(self, image=self.imglist[0])
        self.imglbl1.image = self.imglist[0]
        self.imglbl1.place(x=25,y=75)

        imglbl2 = Label(self, image=self.imglist[1])
        imglbl2.image = self.imglist[1]
        imglbl2.place(x=25, y=280)

        imglbl3 = Label(self, image=self.imglist[2])
        imglbl3.image = self.imglist[2]
        imglbl3.place(x=25, y=485)

        Button(self,
               text = "Change image",
               command = self.changeimg
               ).place(x=75,y=695)

    def changeimg(self):
        self.index +=1
        if self.index > 2:
            self.index = 0
        self.imglbl1.config(image=self.imglist[self.index])

def main():
    root = Tk()
    root.title("Title")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))

    app = App(root)

    root.mainloop()

main()