class Singleton(object):
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance == None:
            print("Inicjalizuję")
        Singleton._instance = self

    def komunikat(self):
        print("Jestem Singletonem")


if __name__ == '__main__':
    ob1 = Singleton.getInstance()
    ob1.komunikat()
    ob2 = Singleton.getInstance()
    ob2.komunikat()
