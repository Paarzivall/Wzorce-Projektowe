from Biblioteka import Biblioteka
from BG1 import BG1


class BibliotekaV1(Biblioteka):
    def __init__(self):
        pass

    def rysujLinie(self, x1, y1, x2, y2):
        BG1.rysuj_linie(x1, y1, x2, y2)

    def rysujOkrag(self, x, y, r):
        BG1.rysuj_okrag(x, y, r)