#James Hooper
#6.4 What's in Your Pocket, Revisited

items = []                  # initialize an empty list
item = input("What's in Your Pocket? ")
# loop until user is done 
while item != "":
    items.append(item)
    print("Item added")
    item = input("What's in Your Pocket? ")
	
print("Your pockets contain: ",items)  # print final list

input("Press Enter to Quit")
