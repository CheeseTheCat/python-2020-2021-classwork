# James Hooper
# 1/26/2021
# textbox tikinter

from tkinter import *

class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()
    usernames = ["cheesethecat"]
    passwords = ["1234567890"]
    trys = 0

    def create_widgets(self):
        self.lbl = Label(self, text="Enter your password to gain entry")
        self.userlbl = Label(self, text="Username")
        self.passlbl = Label(self, text="Password")
        self.bttn = Button(self, width = 16,text="Submit")
        self.bttn["command"]=self.submit1
        self.user_tb = Entry(self)
        self.pass_tb = Entry(self)
        self.add_user_bttn = Button(self, text="Add User")
        self.add_user_bttn["command"]=self.submit2


        self.lbl.grid(row=0, column=0, columnspan=3, sticky=N)
        self.userlbl.grid(row=1,column=0,sticky=E)
        self.passlbl.grid(row=2,column=0,sticky=E)
        self.bttn.grid(row=3,column=1,columnspan=1,sticky=W)
        self.user_tb.grid(row=1,column=1,columnspan=1,sticky=W)
        self.pass_tb.grid(row=2,column=1,columnspan=1,sticky=W)
        self.add_user_bttn.grid(row=3, column=2, sticky=W)

        self.output = Text(self)
        self.output.grid(row=4,columnspan=3)

    def submit1(self):
        username = self.user_tb.get()
        password = self.pass_tb.get()
        if username.lower() in self.usernames and self.trys <= 5:
            if password in self.passwords and self.trys <= 5:
                msg = "You are in "
                self.trys = 0

            else:
                msg = "Incorrect Password"
                self.trys += 1
        else:
            msg = "Incorrect Username"
            self.trys += 1

        if self.trys > 5:
            msg = "Sorry you reached the maximum number of tries"
        self.output.delete(0.0,END)
        self.output.insert(0.0,msg)

    def submit2(self):
        msg = ""
        username = self.user_tb.get()
        password = self.pass_tb.get()
        if username.lower() not in self.usernames and self.trys <= 5:
            self.usernames.append(username.lower())
            self.passwords.append(password)
        else:
            msg = "Username is taken"
        self.output.delete(0.0, END)
        self.output.insert(0.0, msg)


def main():
    root = Tk()
    root.title("password entry")
    root.geometry("800x500")
    root.configure(bg = "#FF6F00")
    app = App(root)

    root.mainloop()

main()