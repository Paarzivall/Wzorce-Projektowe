from DekoratorPotwierdzenia import DekoratorPotwierdzenia


class DekoratorNaglowka2(DekoratorPotwierdzenia):
    def __init__(self, komponent):
        super().__init__(self, komponent)

    def drukuj(self):
        self.drkNaglowek()
        super().drukuj()

    def drkNaglowek(self):
        print("Naglowek 2")