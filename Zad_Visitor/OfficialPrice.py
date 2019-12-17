from Visitor import Visitor


class OfficialPrice(Visitor):
    def __init__(self):
        self.price = 0

    def VisitAnimal(self, animal):
        self.price += animal.Price

    def VisitBird(self, bird):
        self.price += bird.Price

    def PrintVisitorResult(self):
        print(f'Odwiedzone zwierzeta kosztuja lacznie: {self.price}')