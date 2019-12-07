from Handler import Handler


class Dialog(Handler):
    def __init__(self, successor=None):
        self._successor = successor

    def HandleHelp(self):
        print("aPrintDialog: Nie potrafie obsluzyc zadania, przekazuje dalej")
        self._successor.HandleHelp()

    def ShowHelp(self):
        raise NotImplementedError()
