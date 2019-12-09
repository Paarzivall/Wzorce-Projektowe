from SterownikDrukarki import SterownikDrukarki
from SDNR import SDNR


class SterDrukNisRozdz(SterownikDrukarki):
    def __init__(self):
        self.sdnr = SDNR()

    def drukuj(self):
        self.sdnr.drukuj()