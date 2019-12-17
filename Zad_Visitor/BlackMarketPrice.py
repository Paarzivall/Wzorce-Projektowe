from Visitor import Visitor


class BlackMarketPrice(Visitor):
    def __init__(self):
        self.price = 0

    def VisitAnimal(self, animal):
        self.price += animal.Price

    def VisitBird(self, bird):
        self.price += bird.blackMarketPrice

    def PrintVisitorResult(self):
        print(f'Suma cen czarnorynkowych odwiedzonych zwierzat wynosi: {self.price}')