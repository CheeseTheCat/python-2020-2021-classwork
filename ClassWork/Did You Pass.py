#James Hooper
#Did  you pass?

grade = input("What is your grade percentage? ")
yourgrade = "A"

if grade >= "90":
    yourgrade = "A"
elif grade >= "80":
    yourgrade = "B"
elif grade >= "70":
    yourgrade = "C"
elif grade >= "60":
    yourgrade = "D"
else:
    yourgrade = "F"

print(str.format("Your letter grade is a {}",yourgrade))

input()
