# super snake time

import random
from tkinter import *
import sys
from PIL import ImageTk
from PIL import Image as im

class Cons:
    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27



class Board(Canvas):

    def __init__(self):
        super(Board, self).__init__(width=Cons.BOARD_WIDTH,height=Cons.BOARD_HEIGHT,
                                    background="black",highlightthickness=0)
        self.initGame()
        self.pack()

    def initGame(self):
        """initializes game"""
        self.inGame = True
        self.dots = 3
        self.score = 0

        # variables used to move snake object
        self.moveX = Cons.DOT_SIZE
        self.moveY = 0

        #starting apple coordinates
        self.appleX = 100
        self.appleY = 190

        #load images
        self.loadImages()

        #create game objects
        self.createObjects()

        #place apple on screen
        self.locateApple()

        #bind keys
        self.bind_all("<Key>",self.onKeyPressed)

        self.after(Cons.DELAY,self.onTimer)

    def loadImages(self):
        """load images"""
        try:
            self.ibody = im.open("images/body1.png")
            self.ihead = im.open("images/head1.png")
            self.iapple = im.open("images/apple1.png")
            self.body = ImageTk.PhotoImage(self.ibody)
            self.head = ImageTk.PhotoImage(self.ihead)
            self.apple = ImageTk.PhotoImage(self.iapple)


        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects(self):
        """creates objects on Canvas"""
        self.create_text(30, 10, text="Score: {0}".format(self.score),
                         tag = "score", fill = "white")
        self.create_image(self.appleX, self.appleY, image= self.apple,
                          anchor=NW, tag="apple")
        self.create_image(50, 50, image=self.head, anchor=NW, tag="head")
        self.create_image(30, 50, image=self.body, anchor=NW, tag="body")
        self.create_image(40, 50, image=self.body, anchor=NW, tag="body")

    def locateApple(self):
        apple=self.find_withtag("apple")
        self.delete(apple[0])
        r = random.randint(0,Cons.MAX_RAND_POS)
        self.appleX = r * Cons.DOT_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleY = r * Cons.DOT_SIZE

        self.create_image(self.appleX, self.appleY, anchor=NW,
                          image=self.apple, tag="apple")

    def onKeyPressed(self,e):
        """controls direction variables with cursor keys"""
        key = e.keysym
        LEFT_CURSOR_KEY="Left"
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:
            self.moveX = -Cons.DOT_SIZE
            self.moveY = 0

        RIGHT_CURSOR_KEY="Right"
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:
            self.moveX = Cons.DOT_SIZE
            self.moveY = 0

        UP_CURSOR_KEY="Up"
        if key == RIGHT_CURSOR_KEY and self.moveY <= 0:
            self.moveX = 0
            self.moveY = -Cons.DOT_SIZE

        DOWN_CURSOR_KEY = "Down"
        if key == RIGHT_CURSOR_KEY and self.moveY >= 0:
            self.moveX = 0
            self.moveY = Cons.DOT_SIZE

    def onTimer(self):
        """Create a game cycle each timer """
        self.drawScore()
        self.checkCollision()
        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()


    def drawScore(self):
        pass

    def checkCollision(self):
        pass

    def checkAppleCollision(self):
        pass

    def moveSnake(self):
        pass

    def gameOver(self):
        pass


class Snake(Frame):
    def __init__(self,master):
        super(Snake, self).__init__(master)
        self.master.title("Super Snake Time")
        self.board = Board()
        self.pack()





def main():
    root = Tk()
    snake = Snake(root)
    root.mainloop()




main()
