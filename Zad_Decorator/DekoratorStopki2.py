from DekoratorPotwierdzenia import DekoratorPotwierdzenia


class DekoratorStopki2(DekoratorPotwierdzenia):
    def __init__(self, komponent):
        super().__init__(self, komponent)

    def drukuj(self):
        self.drkStopka()
        super().drukuj()

    def drkStopka(self):
        print("Stopka 2")