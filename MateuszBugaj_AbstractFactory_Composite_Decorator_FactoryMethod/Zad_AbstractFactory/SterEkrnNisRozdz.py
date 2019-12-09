from SterownikEkranu import SterownikEkranu
from SENR import SENR


class SterEkrnNisRozdz(SterownikEkranu):
    def __init__(self):
        self.senr = SENR()

    def rysuj(self):
        self.senr.rysuj()