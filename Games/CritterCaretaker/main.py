# James hooper
# 12/15/2020
# critterkeeper thing
import random

#################################################################################################################

#################################################################################################################
class Critter(object):
    """This is the class that defines what a critter is"""
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2,7)
        self.name = ""
        self.happy = 50
        self.is_alive = True

    def get_hunger(self):
        return self.hunger

    def get_height(self, height):
        if  height < 5 and height > 1:
            self.height = height

    def get_name(self, name):
        if len(name) > 4:
            if "uck" not in name:
                self.name = name

    def get_weight(self,weight):
        if weight < 3 and weight > 8:
                self.weight = weight

    def set_weight(self, weight):
        self.weight = weight

    def set_health(self, health):
        self.health = health

    def set_hunger(self, hunger):
        self.hunger = hunger

    def set_height(self, height):
        self.height = height

    def set_happy(self, happy):
        self.happy = happy

    def intro(self):
        print("hello my name is " + self.name)

    def hud(self):
        print(self.name)
        health = self.health
        if health >80:
            print("Health: Great")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")
        if self.hunger > 40:
            print("Hunger: starving")
        elif self.hunger > 20:
            print("Hunger: Really Hungry")
        elif self.hunger < 10:
            print("Hunger: Full")
        else:
            print("Hunger: Hungry")
        if self.hunger > 100:
            self.die()
        if self.hunger < -200:
            self.die()
        if self.happy > 50:
            print("Happiness: Happy")
        elif self.happy > 35:
            print("Happiness: Grumpy")
        else:
            print("Happiness: Mad")
        print("Is Alive:", str(self.is_alive))

    def die(self):
        print("Your pet has died you are a horable person for letting this digital creature die")
        self.set_health = 0
        self.is_alive = False

    def feed(self,food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheese burger":
            self.hunger -= 13
        elif food == "steak":
            self.hunger -= 23
        elif food == "corn":
            self.hunger -= 3
        elif food == "pizza burger":
            self.hunger -= 100
            self.health += 10
        elif food == "cheese cake":
            self.hunger -= 100
            self.health -= 5
        else:
            self.hunger -= 5

    def pass_time(self, hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happy += 10
            elif self.hunger < 50:
                self.health -= 5

            if self.hunger > 50:
                self.weight -= 1
                self.happy -= 10
                self.health -= 5
            self.happy -= 5

    def play(self,time):
        self.pass_time(self, time)
        self.happy += 10 * time
        if self.happy > 100:
            self.happy = 100
        self.health += 10 * time
        if self.health > 100:
            self.health = 100






#################################################################################################################
def main():
    pet = Critter()
    name = input("What would you like to name your pet ")
    pet.get_name(name)
    height = int(input("how tall is your pet between 2 and 5 "))
    pet.set_height(height)
    pet.intro()
    pet.hud()
    while pet.is_alive:
        pet.pass_time(1)
        print("what would you like to do? ")
        print("Feed")
        print("Play")
        print("Nothing")
        response = input()
        if response == "feed":
            food = input("what do you want to feed your pet? ")
            pet.feed(food)
        if response == "play":
            time = int(input("how long will you play with your pet? "))
        pet.hud()

#################################################################################################################
main()