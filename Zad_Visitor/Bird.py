from Animal import Animal
from AllBird import AllBird


class Bird(Animal, AllBird):
    def __init__(self, name, value, ill, darkMarketValue):
        super().__init__(name, value, ill)
        self.darkMarketValue = darkMarketValue

    def accept(self, visitor):
        visitor.visit(self)

    def getDarkMarketValue(self):
        return self.darkMarketValue




