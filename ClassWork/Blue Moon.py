#James Hooper
#Blue Moon

blueMoon = input("Is there a blue moon tonight (Yes / No)?")
WeekDay = input("What is the day of the week (Monday - Sunday)?")
MonthDay = int(input("What is the day of the month (1 - 31)?"))

if blueMoon == "Yes":
    print("Once in a Blue Moon")
elif MonthDay <= 7:
    if WeekDay == "Monday":
        print("Manic Monday")
    elif WeekDay == "Tuesday":
        print("Tuesday's Gone")
    elif WeekDay == "Wednesday":
        print("Just Wednesday")
    elif WeekDay == "Thursday":
        print("Sweet Thursday")
    elif WeekDay == "Friday":
        print("Friday I'm in Love")
    elif WeekDay == "Saturday":
        print("Saturday in the Park")
    elif WeekDay == "Sunday":
        print("Lazing on a Sunday Afternoon")
    else:
        print("Days of the Week")
else:
    print("Day Dream Believer")

input("Press Enter To Close")
