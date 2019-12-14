from abc import ABC, abstractmethod


class AllBird(ABC):
    @abstractmethod
    def getDarkMarketValue(self):
        pass