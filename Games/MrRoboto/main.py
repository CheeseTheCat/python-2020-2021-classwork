# James Hooper
# 1/8/2021
# Mr Roboto

class Robot(object):
    def __init__(self):
        self.name = "Mr. Roboto"
        self.thankYou = "Domo arigato"

    def thanks(self):
        print(self.thankYou, self.name)

Robot.thanks()
