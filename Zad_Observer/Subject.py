from abc import ABC


class Subject(ABC):
    def Attach(self, observer):
        pass

    def Detach(self, observer):
        pass

    def Notify(self):
        pass