#james hooper
#11/23/2020
#car classes

class Car():

    def __init__(self):
        self.color = input("What color do you want your car? ")
        self.brand = input("What brand is your car? ")
        self.model = input("What model is your car? ")
        self.tire_brand = input("What tire brand does your car have? ")
        self.tire_size = input("What tire size does your car have? ")
        self.type = input("What type of car is your car (sport, mini van, truck? ")
        self.price = input("How expensive is your car? ")
        self.year = input("What is the year of your car? ")
        self.fuel_type = input("What fuel type does your car need? ")
        self.max_fuel = input("How much fuel is in the full tank? ")
        self.max_speed = int.input("How expensive is your car? ")
        self.engine = Engine()
##        self.radio = Radio()
    def display(self):
        if self.color!="":
            print(self.color)

              
class Engine():

    def __init__(self):
        self.cylinder = input("How many cylinders does your car have? ")
        self.cylinder_ornt = input("What orentation are the cylinders in? ")
        self.mpg = input("How many miles per gallon does your engine get? ")


class Radio():

    def __init__(self):
        

def main():
    my_dream_car = Car()
    print(my_dream_car.color)

main()
