from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor):
        self._successor = successor

    @abstractmethod
    def HandleHelp(self):
        pass

    @abstractmethod
    def ShowHelp(self):
        pass

    def SetSuccesor(self, successor):
        self._successor = successor
