#James Hooper and Emily Briggs
#2/17/21
#mad_lib
from tkinter import *
from tkinter.ttk import *
HEIGHT = 500
WIDTH = 500
TITLE = "title"
BACKGROUND = "white"


class App(Frame):
    def __init__(self,master):
        super(App, self).__init__(master)
        self.index= 0
        self.name1 = "Yoda"
        self.noun1 = ""
        self.name2 = ""
        self.noun2 = ""
        self.adj1 = ""
        self.noun3 = ""
        self.name3 = ""
        self.name4 = ""
        self.adj2 = ""
        self.name5 = ""
        self.noun4 = ""
        self.word_list = [self.name1, self.noun1, self.name2, self.noun2, self.adj1, self.noun3, self.name3, self.name4, self.adj2, self.name5, self.noun4]
        self.prompt_list = ["Give me a name. " ,"Give me noun. ","Give me another name. ", "Give me a noun. ",
                            "Give me an adjective. ","Give me an noun. ","Give me a long name. ",
                            "Give me a wierd name. ","Give me a adjective. ","Give me a scary name. ",
<<<<<<< HEAD
                            "Give me a noun. "]
=======
                            "Give me a noun. ","Story Time"]
>>>>>>> cda702af8f9c67a023f5fe847d395e53b3f4f5df
        self.story = [str.format("""
It is a dark time for the
{0}. Although the {1} has been destroyed,
{2} troops have driven the
{0} forces from their hidden
{3} and pursued them across
the galaxy.

Evading the {4} {2}
Starfleet, a group of {5} 
led by {6}
has established a new secret
{3} on the remote ice world
of {7}.

The {8} {9},
obsessed with finding young
{6}, has dispatched
thousands of {10} into
the far reaches of space....
<<<<<<< HEAD
""", self.name1, self.noun1, self.name2, self.noun2, self.adj1, self.noun3, self.name3, self.name4, self.adj2,
                            self.name5, self.noun4)]
=======
""", self.word_list[0],self.word_list[1],self.word_list[2],self.word_list[3],self.word_list[4],self.word_list[5],self.word_list[6],self.word_list[7],self.word_list[8],self.word_list[9],self.word_list[10])]
>>>>>>> cda702af8f9c67a023f5fe847d395e53b3f4f5df

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl=Label(self,text=self.prompt_list[self.index])
        self.lbl.grid(row=0,column=0)
        self.txtentry=Entry(self, text = "")
        self.txtentry.grid(row=1,column=0)
        self.next=Button(self, text="Next", command=self.onNext).grid(row=2, column=0)



        self.output = Text(self, height=25, width=37)
        self.output.grid(row=3)


    def onNext(self):
        if self.index <= 9:
            text=self.txtentry.get()
            if self.txtentry.get() != "":
                self.word_list[self.index] = text
            self.index+=1
            self.lbl.config(text=self.prompt_list[self.index])
        else:
<<<<<<< HEAD
            self.lbl.config(text="Story Time")
=======
            self.index+=1
            self.lbl.config(text=self.prompt_list[self.index])
            self.index-=1
>>>>>>> cda702af8f9c67a023f5fe847d395e53b3f4f5df
            self.output.delete(0.0, END)
            self.output.insert(0.0, self.story)



def main():
    root = Tk()
    root.title("MadLib")
    root.geometry(str(WIDTH)+"x"+str(HEIGHT))
    root.configure(bg = BACKGROUND)
    app = App(root)

    root.mainloop()

main()

#Credit https://starwars.fandom.com/wiki/Opening_crawl
<<<<<<< HEAD

=======
>>>>>>> cda702af8f9c67a023f5fe847d395e53b3f4f5df
