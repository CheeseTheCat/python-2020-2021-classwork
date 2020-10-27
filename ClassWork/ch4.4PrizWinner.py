# James Hooper
#10/1/2020
#Prize Winner

import random

##theNumber = random.randint (0,9)
##theNumber = random.randint (0,9)
##theNumber = random.randint (0,9)
##theNumber = random.randint (0,9)
##theNumber = random.randint (0,9)
##theNumber = random.randint (0,9)

number1 = 8
number2 = 6
number3 = 7
number4 = 5
number5 = 3
number6 = 0

print("Your Math Club has made a raffle. ")
want_ticket = input("Do you want a ticket for the raffle? ")

if (want_ticket == "yes") and (number1 > number6) and ((number2 * number3) > 20) and ((number4 - (number5 * number1)) < 0):
    print("Winner! ")
else:
    print("Thanks for your contribution to the math club. ")
