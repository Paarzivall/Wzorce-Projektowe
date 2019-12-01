from Graphic import Graphic


class Picture(Graphic):
    def __init__(self):
        self.figury = []

    def draw(self):
        for figura in self.figury:
            figura.draw()

    def add(self, graphic):
        self.figury.append(graphic)

    def remove(self, graphic):
        self.figury.remove(graphic)

    def GetChild(self, child):
        return self.figury[child]