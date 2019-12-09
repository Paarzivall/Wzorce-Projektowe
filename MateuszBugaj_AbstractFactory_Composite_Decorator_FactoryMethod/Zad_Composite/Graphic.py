from abc import ABC, abstractmethod


class Graphic(ABC):
    @abstractmethod
    def draw(self):
        pass

    def add(self, graphic):
        pass

    def remove(self, graphic):
        pass

    def GetChild(self, child):
        pass