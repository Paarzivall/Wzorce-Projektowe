from Biblioteka import Biblioteka
from BG2 import BG2


class BibliotekaV2(Biblioteka):
    def __init__(self):
        pass

    def rysujLinie(self, x1, y1, x2, y2):
        BG2.narysujlinie(x1, y1, x2, y2)

    def rysujOkrag(self, x, y, r):
        BG2.narysujokrag(x, y, r)