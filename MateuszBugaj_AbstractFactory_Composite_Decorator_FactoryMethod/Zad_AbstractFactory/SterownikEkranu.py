from abc import ABC, abstractmethod


class SterownikEkranu(ABC):
    @abstractmethod
    def rysuj(self):
        pass