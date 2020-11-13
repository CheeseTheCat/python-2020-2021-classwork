#James Hooper
#Burger Castle

validOrders = ("burger","fries","salid","soda","milkshake")
itemDescriptions = ("Half-pound Burger","Large Fries","Side Salad","Diet Root Beer","Chocolate Shake")
order = []
print("Welcome to Burger Castle")
print(str.format("Menu: {}",validOrders))
print("Please enter each item in your order. Press 'Enter' or type 'quit' on an empty line when done.")
item = input("Enter item: ")
while item not in ("","quit"):
    if item in validOrders:
        order.append(item)
    else:
        print(str.format("Sorry, we don't sell {}.",item))
    item = input("Enter item: ")

print()
print("Order complete; you are having:")

for item in order:
    print(itemDescriptions[validOrders.index(item)])
print("Thanks for visiting Burger Castle!")
input()
