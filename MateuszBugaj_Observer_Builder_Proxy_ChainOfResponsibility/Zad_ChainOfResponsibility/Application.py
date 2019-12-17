from Handler import Handler


class Application(Handler):
    def __init__(self, successor=None):
        self._successor = successor

    def HandleHelp(self):
        self.ShowHelp()

    def ShowHelp(self):
        print("anApplication: Potrafie obsluzyc zadanie, wyswietlam pomoc")