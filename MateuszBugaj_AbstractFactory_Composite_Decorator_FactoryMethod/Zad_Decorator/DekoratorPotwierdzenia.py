from Komponent import Komponent


class DekoratorPotwierdzenia(Komponent):
    def __init__(self, komponent):
        self.komponent = komponent

    def drukuj(self):
        self.komponent.drukuj()