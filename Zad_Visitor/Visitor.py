from abc import ABC


class Visitor(ABC):
    def VisitAnimal(self, animal):
        pass

    def VisitBird(self, bird):
        pass