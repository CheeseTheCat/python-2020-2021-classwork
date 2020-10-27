## James Hooper
## 9/20
## Guess my number 1.1

import random

maxNumber = 10
numTries = 3

win = False

#difficult settings
print("Welcome to Guess The Number! ")
question = input ("What difficulty would you like Easy, Medium, Hard. ")

if question.startswith ("E") or question.startswith ("e"):
    maxNumber = 10
    numTries = 3
    diff = 1
    diffvar = "easy"
elif question.startswith ("M") or question.startswith ("m"):
    maxNumber = 50
    numTries = 5
    diff = 2
    diffvar = "medium"
else:
    maxNumber = 100
    numTries = 10
    diff = 3
    diffvar = "hard"
theNumber = random.randint (1,maxNumber)

print("""

Your difficulty is""",diffvar)
print(str.format("I'm thinking of a number between 1 and {}. ", maxNumber))
print(str.format("Try to guess it in {} attempts. ", numTries))
#print("The Number is",theNumber) # for testing remove when finished
#guess 1
guess = int(input(str.format("Pick a number between 1 and {}. ", maxNumber)))
if guess == theNumber:
    print("You win")
elif (not win) and (guess > theNumber):
    print("Guess lower")
else:
    print("Guess higher")

##    if guess == theNumber:
##        print("You win")
##        win = True
##    elif guess > theNumber:
##        print("guess lower")
##    else:
##        print("guess higher")
    
#quess 2
if not win:
    guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
if (guess == theNumber) and (not win):
    print("You win")
    win = True
elif (guess > theNumber) and (not win):
    print("guess lower")
else:
    print("guess higher")
#quess 3
if not win:
    if (diff == 2) or (diff == 3):
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#quess 4
if not win:
    if (diff == 2) or (diff == 3):
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#quess 5
if not win:
    if diff == 3:
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#quess 6
if not win:
    if diff == 3:
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#quess 7
if not win:
    if diff == 3:
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#quess 8
if not win:
    if diff == 3:
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#quess 9
if not win:
    if diff == 3:
        guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
        if (guess == theNumber) and (not win):
            print("You win")
            win = True
        elif (guess > theNumber) and (not win):
            print("guess lower")
        else:
            print("guess higher")
#guess 10
if not win:
    guess = int(input(str.format("""
Pick a number between 1 and {}. """, maxNumber)))
if (guess == theNumber) and (not win):
    print("You win")
    win = True
elif (guess > theNumber) and (not win):
    print("The number was",theNumber)
else:
    print("The number was",theNumber)
    
if win:
    print("Great Job")
else:
    print("Better luck Next time")
input()
