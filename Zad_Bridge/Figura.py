from abc import ABC, abstractmethod
from Biblioteka import Biblioteka


class Figura(ABC):
    @abstractmethod
    def __init__(self):
        self.biblioteka = Biblioteka()

    def rysujLinie(self, x1, y1, x2, y2):
        self.biblioteka.rysujLinie(x1, y1, x2, y2)

    def rysujOkrag(self, x, y, r):
        self.biblioteka.rysujOkrag(x, y, r)