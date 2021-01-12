# James hooper
# 1/12/2021
# Mr.Roboto

class Robot(object):
    def __init__(self):
        self.name = "Mr. Roboto"
        self.thankYou = "Domo arigato"
    def thanks(self):
        print(self.thankYou, self.name)
        return self.thankYou, self.name

def main():
    Roboto = Robot()
    Roboto.thanks()

