# Hangman Game
# James Hooper
# 10/20
# The classic game of Hangman.  The computer picks a random word
# and the player wrong to guess it, one letter at a time.  If the player
# can't guess the word in time, the little stick figure gets hanged.

#imports
import random

hangman = (
"""
-------
|  |
|  
|  
|
|
|
-------
""",
"""
-------
|  |
|  O
|  
|
|
|
-------
""",
"""
-------
|  |
|  O
|  |
|  |
|
|
-------
""",
"""
-------
|  |
|  O
| /|
|  |
|
|
-------
""",
"""
-------
|  |
|  O
| /|\\
|  |
|
|
-------
""",
"""
-------
|  |
|  O
| /|\\
|  |
| /
|
-------
""",
"""
-------
|  |
|  O
| /|\\
|  |
| / \\
|
-------
""")

maxWrong = len(hangman) - 1
words = ("OVERUSED", "CHART", "LOOP", "SNAKE", "PYTHON", "PRINT", "VARIABLE", "LOGIC", "FUNCTION", "ERROR")
word=random.choice(words)
definition = ("To use too much or too often.", "A sheet of information in the form of a table, graph, or diagram.", \
              "A structure, series, or process, the end of which is connected to the beginning.", \
              """a long limbless reptile which has no eyelids, a short tail,
and jaws that are capable of considerable extension.""", \
              "The text appearing in a book, newspaper, or other printed publication.", \
              "An element, feature, or factor that is liable to vary or change.", \
              "A system or set of principles underlying the arrangements of elements so as to perform a specified task.", \
              "A relationship or expression involving one or more variables.", \
              "A mistake.")
wrong = 0
used = []
so_far = "-"*len(word)
defindex = words.index(word) - 1

print("Welcome To Hangman")
while wrong < maxWrong and so_far != word:
    print(hangman[wrong])
    print()
    print("\nSo far , the word is:\n", so_far)
    print("\nYou've  used the following letters:\n", used)
    
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()

    used.append(guess)
    
    if guess in word:
        print("\nYes", guess, "is in the word")
        #create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

if wrong == maxWrong:
    print(hangman[wrong])
    print("\nYou've been hanged!")
    print("\nSo far, the word is:/n", so_far)
else:
    print(hangman[wrong])
    print("\nYou guessed it!")
    print("\the word was:\n", so_far)

input("Press the enter key for the definition. ")


print(definition[defindex])

input()
















