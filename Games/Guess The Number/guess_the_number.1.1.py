## James Hooper
## 9/20
## Guess my number 1.1

import random

theNumber = random.randint (1,10)
win = False
#print(theNumber) # for testing remove when finished

print("Welcome to Guess The Number! ")
print("I'm thinking of a number between 1 and 10. ")
print("Try to guess it in 3 attempts. ")
#guess 1
guess = int (input("Pick a number between 1 and 10. "))
if guess == theNumber:
    print("You win")
elif (not win) and (guess > theNumber):
    print("Guess lower")
else print("Guess higher")
##    if guess == theNumber:
##        print("You win")
##        win = True
##    elif guess > theNumber:
##        print("guess lower")
##    else:
##        print("guess higher")
    
#quess 2
if not win:
    guess = int (input("Pick a number between 1 and 10. "))
if (guess == theNumber) and (not win):
    print("You win")
    win = True
elif (guess > theNumber) and (not win):
    print("guess lower")
else and (not win):
    print("guess higher")
    
#guess 3
if not win:
    guess = int (input("Pick a number between 1 and 10. "))
if (guess == theNumber) and (not win):
    print("You win")
    win = True
elif (guess > theNumber) and (not win):
    print("guess lower")
    print("The number was",theNumber)
else and (not win):
    print("guess higher")
    print("The number was",theNumber)
    
if win:
    print("Great Job")
else:
    print("Better luck Next time")
input()
