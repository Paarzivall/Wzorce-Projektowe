from Animal import Animal


class Bird(Animal):
    def __init__(self, name, price, ill, blackMarketValue):
        super().__init__(name, price, ill)
        self.blackMarketPrice = blackMarketValue

    def Accept(self, visitor):
        visitor.VisitBird(self)

    def __str__(self):
        return super().__str__() + f', Cena czarnorynkowa: {self.blackMarketPrice}'




