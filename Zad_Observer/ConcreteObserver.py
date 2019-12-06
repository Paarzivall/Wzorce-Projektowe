from ConcreteSubject import ConcreteSubject
from Observer import Observer


class ConcreteObserver(Observer):
    def __init__(self, observerName, subject):
        self._subject = subject
        self._observerName = observerName
        self._subject.Attach(self)

    def Update(self):
        self._observerState = self._subject.GetState()
        print(f'Zmiania stanu obserwatora {self._observerName}: {self._observerState}')