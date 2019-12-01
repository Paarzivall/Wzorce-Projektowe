from SterownikDrukarki import SterownikDrukarki
from SDWR import SDWR


class SterDrukWysRozdz(SterownikDrukarki):
    def __init__(self):
        self.sdwr = SDWR()

    def drukuj(self):
        self.sdwr.drukuj()