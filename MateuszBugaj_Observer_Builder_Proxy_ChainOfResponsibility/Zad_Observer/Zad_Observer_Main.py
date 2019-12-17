from ConcreteSubject import ConcreteSubject
from ConcreteObserver import ConcreteObserver

if __name__ == '__main__':
    subject1 = ConcreteSubject()
    subject2 = ConcreteSubject()
    observer1 = ConcreteObserver("Observer 1", subject1)
    observer2 = ConcreteObserver("Observer 2", subject1)
    observer3 = ConcreteObserver("Observer 3", subject2)
    observer4 = ConcreteObserver("Observer 4", subject2)
    subject1.SetState("New State")
    subject2.SetState("New State 2")