#James Hooper
#6.3 Calculating a Factorial

# get target number from the user
number = int(input("Enter a positive integer: "))

# initialize variable to hold factorial total
factorial = 1   

# loop from 1 up through target number
for index in range(1,number + 1):
  # multiply factorial by loop index value
    factorial = factorial * index
    
# print final results
print("Factorial =",factorial)

input("Press Enter to Quit")
