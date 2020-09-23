
question1 = "What is your name? "
user_name = input(question1)
user_age = int(input("how old are you? "))
user_grade = int(input("are you in (9th 10th 11th 0r 12th) grade? "))
ret_age = int(input("when do you want to retire? "))

years_until_21 = 21 - user_age
graduation =  12 - user_grade
years_until_ret =ret_age - user_age

print(years_until_21)
print(graduation)
print(years_until_ret)
