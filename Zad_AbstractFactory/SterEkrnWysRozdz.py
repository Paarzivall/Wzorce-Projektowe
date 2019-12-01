from SterownikEkranu import SterownikEkranu
from SEWR import SEWR


class SterEkrnWysRozdz(SterownikEkranu):
    def __init__(self):
        self.sewr = SEWR()

    def rysuj(self):
        self.sewr.rysuj()