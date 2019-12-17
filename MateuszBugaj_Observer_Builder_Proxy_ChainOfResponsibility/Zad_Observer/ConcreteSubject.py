from Subject import Subject


class ConcreteSubject(Subject):
    def __init__(self, defaultState=""):
        self._observers = []
        self._subjectState = defaultState

    def Attach(self, observer):
        self._observers.append(observer)

    def Detach(self, observer):
        self._observers.remove(observer)

    def Notify(self):
        for observer in self._observers:
            observer.Update()

    def GetState(self):
        return self._subjectState

    def SetState(self, newState):
        self._subjectState = newState
        self.Notify()