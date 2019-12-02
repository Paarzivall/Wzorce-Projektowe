from abc import ABC, abstractmethod


class Komponent(ABC):
    @abstractmethod
    def drukuj(self):
        pass