from Handler import Handler


class Button(Handler):
    def __init__(self, successor=None):
        self._successor = successor

    def HandleHelp(self):
        print("aPrintButtonButton: Nie potrafie obsluzyc zadania, przekazuje dalej")
        self._successor.HandleHelp()

    def ShowHelp(self):
        raise NotImplementedError()
