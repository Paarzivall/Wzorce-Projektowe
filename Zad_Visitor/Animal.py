from abc import ABC


class Animal(ABC):
    def __init__(self, name, price, ill):
        self.name = name
        self.Price = price
        self.ill = ill

    def Accept(self, visitor):
        pass

    def __str__(self):
        return f'Zwierz: {self.name}, Cena: {self.Price}, Stan Zdrowia: {"Zdrowy" if self.ill else "Chory"}'
