# James Hooper
# 11/25/2020
# Quotable Quotes

import random

def select_quote():
    quotes = ("My fake plants died because I did not pretend to water them - Mitch Hedberg", \
            "There cannot be a crisis next week.  My schedule is already full. - Henry Kissinger", \
            "Weather forecast for tonight: dark. - George Carlin", \
            "All generalizations are false, including this one. - Mark Twain", \
            "Why do they call it rush hour when nothing moves? - Robin Williams")

    quote = random.choice(quotes)
    print(quote)
    return

select_quote()
print()
select_quote()

input()
