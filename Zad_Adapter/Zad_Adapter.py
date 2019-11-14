from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self):
        self.polozenie = []

    def pobierzPolozenie(self):
        pass

    def NadajPolozenie(self):
        pass

    @abstractmethod
    def wyswietl(self):
        pass

    @abstractmethod
    def wypelnij(self):
        pass

    @abstractmethod
    def usun(self):
        pass