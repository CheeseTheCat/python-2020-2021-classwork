# James Hooper
# 1/4/2021
# functions

def menu(options):
    value = ""
    success = False

    print("You may:")

    for i in range(len(options)):
        print(str.format("  {}. {}", i + 1, options[i]))

    value = get_number("What do you choose: ", 1, len(options))

    return value


def ask_yes_no(question):
    """Ask a yes or no question and get back a yes or no answer. """
    response = None
    while response not in ("y", "n", "no", "yes"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """ask for a number within a range. to use (answer - ask_number(question,low,high))"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def ask_page(option1, option2):
    """Asks the user for a page."""
    response = ""

    # Just for spacing
    print()

    while (response == "") or (int(response) not in (option1, option2)):
        response = input(str.format("Which page do you want to go to?({} or {}): ", option1, option2))

        # Check if it is only digits, if not then just loop again
        if not is_only_digits(response):
            response = ""

    # This is here to divide pages
    print(str.format("\n=============== {} ===============", response))

    return int(response)


def is_only_digits(string):
    """Checks if the provided string has only numerical digits."""
    result = True

    for character in string:
        if character not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            result = False
            break

    return result


def ask_page_extra(option1, option2, option3):
    """Asks the user for a page, with 3 options."""
    response = ""

    # Just for spacing
    print()

    while (response == "") or (int(response) not in (option1, option2, option3)):
        response = input(str.format("Which page do you want to go to?({}, {}, or {}): ", option1, option2, option3))

        # Check if it is only digits, if not then just loop again
        if not is_only_digits(response):
            response = ""

            # This is here to divide pages
    print(str.format("\n=============== {} ===============", response))

    return int(response)


def get_name(question):
    """Get name that is valid"""
    while True:
        name = input(question)

        if len(name) >= 2 and len(name) <= 16:
            return name


def get_number(question, min, max):
    """Gets number in range"""
    while True:
        valid = True

        number = input(question)

        # Make sure it is only numerical digits
        for digit in number:
            if digit not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                valid = False

        if valid and not number == "":
            num = int(number)

            if num >= min and num <= max:
                return num


class Player(object):
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
        self.lives = 3

