# James Hooper
# 12/7/2020
# Verification Function

import datetime

def get_verified_integer(prompt, min, max):
  while True:
    try:
      input_string = input(prompt)
      input_int = int(input_string)

      if (input_int >= min) and (input_int <= max):
        return input_int
      else:
        print("Try again - ",end="")
    except:
        print("Try again - ",end="")

# main program starts here
month = get_verified_integer("Please enter today's month (1-12): ",1,12)
day   = get_verified_integer("Please enter today's day (1-31): ",1,31)
year  = get_verified_integer("Please enter today's year (2000 - 2030): ",2000,2030)

# build date object and print out the day of the week
today = datetime.date(year,month,day)
print("Today is a " + today.strftime("%A"))
