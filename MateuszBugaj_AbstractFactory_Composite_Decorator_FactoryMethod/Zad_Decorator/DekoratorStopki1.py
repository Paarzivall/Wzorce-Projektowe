from DekoratorPotwierdzenia import DekoratorPotwierdzenia


class DekoratorStopki1(DekoratorPotwierdzenia):
    def __init__(self, komponent):
        super().__init__(komponent)

    def drukuj(self):
        super().drukuj()
        self.drkStopka()

    def drkStopka(self):
        print("Stopka 1")