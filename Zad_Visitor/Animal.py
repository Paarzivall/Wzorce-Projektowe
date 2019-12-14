from abc import ABC


class Animal(ABC):
    def __init__(self, name, value, ill):
        self.name = name
        self.value = value
        self.ill = ill

    def isIll(self):
        return self.ill

    def getValue(self):
        return self.value

    def accept(self, visitor):
        pass
