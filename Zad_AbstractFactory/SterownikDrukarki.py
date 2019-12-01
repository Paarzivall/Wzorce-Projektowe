from abc import ABC, abstractmethod


class SterownikDrukarki(ABC):
    @abstractmethod
    def drukuj(self):
        pass