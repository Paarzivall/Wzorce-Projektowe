from abc import ABC, abstractmethod


class Biblioteka(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def rysujLinie(self, x1, y1, x2, y2):
        pass

    @abstractmethod
    def rysujOkrag(self, x, y, z):
        pass