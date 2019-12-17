from Animal import Animal


class Mammal(Animal):
    def __init__(self, name, value, ill):
        super().__init__(name, value, ill)

    def Accept(self, visitor):
        visitor.VisitAnimal(self)