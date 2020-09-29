## James Hooper
## 9/20
## Guess my number 1.0

import random

theNumber = random.randint (1,10)

print("Welcom to Guess The Number! ")
print("I'm thinking of a number between 1 and 10. ")
print("Try to guess it in 3 attempts. ")

guess = int (input("Pick a number between 1 and 10. "))

if guess == theNumber:
    pass
elif guess > theNumber:
    pass
else:
    pass
