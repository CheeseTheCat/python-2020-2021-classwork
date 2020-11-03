# James Hooper and Spencer Burton

#**********************************Functions**************************************************************
def logo_screen() :
    """This is the first screen"""

    logo = \
"""
-----        _____ _                      __          __      _            
|    \      / ____| |                     \ \        / /     | |           
|     \    | |    | |__   ___  ___  ___  __\ \  /\  / /__  __| | __ _  ___ 
|      \   | |    | '_ \ / _ \/ _ \/ __|/ _ \ \/  \/ / _ \/ _` |/ _` |/ _ \\
|       \  | |____| | | |  __/  __/\__ \  __/\  /\  /  __/ (_| | (_| |  __/
----------  \_____|_| |_|\___|\___||___/\___| \/  \/ \___|\__,_|\__, |\___|
            Studios                                              __/ |     
                                                                |___/   
                                Presents                               
                           - The Oregon Trail -
"""
    
    names = "Jame Hooper and Spencer Burton"
    copy_right = "Copyright (c) 2020"

    print(str.format("{} {}\n {}", copy_right, names, logo))

    input("\nPress Enter to stop appreciating our art")

def menu(options) :
    value = ""
    success = False

    print("You may:")

    for i in range(len(options)) :
        print(str.format("  {}. {}", i + 1, options[i]))

    while not success :
        value = input("What do you choose: ")

        if value in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9") :
            int_value = int(value)

            if int_value in range(1, len(options) + 1) :
                success = True

    return int(value)


def start_screen() :

    oregon_trail = \
"""
_______________________________________________________________________________
  _______ _             ____                               _______        _ _ 
 |__   __| |           / __ \                             |__   __|      (_) |
    | |  | |__   ___  | |  | |_ __ ___  __ _  ___  _ __      | |_ __ __ _ _| |
    | |  | '_ \ / _ \ | |  | | '__/ _ \/ _` |/ _ \| '_ \     | | '__/ _` | | |
    | |  | | | |  __/ | |__| | | |  __/ (_| | (_) | | | |    | | | | (_| | | |
    |_|  |_| |_|\___|  \____/|_|  \___|\__, |\___/|_| |_|    |_|_|  \__,_|_|_|
                                        __/ |                                 
                                       |___/                                   
"""

    print(oregon_trail)

    finished = False

    while not finished :
        choice = menu(["Start Game", "Learn about the Trail", "End"])

        if choice == 1 : # Start game
            print("Starting game...") # Temp call game function
            # start_game()
            finished = True
        elif choice == 2 : # Tell about game
            print()
            print("It's a trail")
            input("Press Enter to continue")
        else :
            finished = True

        # For spacing
        if not finished :
            print()

#***********************************************************************************************************

# Display splash screen
logo_screen()

# Display start menu
start_screen()
