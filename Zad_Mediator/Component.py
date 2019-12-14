from abc import ABC


class Component(ABC):
    def __init__(self, mediator=None):
        self._mediator = mediator

    def SetMediator(self, mediator):
        self._mediator = mediator