def get_menu_choice():
    options = ["Burger, Fries, Soda","Chicken Salad, Iced Tea","Pizza, Soda"]
    cost = [6.99, 10.50, 5.72]

    print("your Menu Choices are:")
    for i in range(len(options)):
        print(str.format("{} - ${:5.2f} : {}",i+1,cost[i],options[i]))
    choice = ask_number("what will you have?",0,len(options)+1)
    order = options[choice-1]
    price = cost[choice-1]
    tax = .075
    total = price + (price*tax)

    print(str.format("ok, you have ordered ----- {}", order))
    print(str.format("out the door you are looking at ----- ${:5.2f}", total))

def ask_number(question,low,high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low,high):
        response = int(input("What will you have? "))
    return response
def ask_yes_no(question):
    """Ask a yes or no question. and will only return yes or no"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
        return response

running = "y"
while running == "y":
    get_menu_choice()               
    running = ask_yes_no("do you want to order more ")
    
