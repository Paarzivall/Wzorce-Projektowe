from Figura import Figura


class Okrag(Figura):
    def __init__(self, bg,x, y, r):
        super().__init__()
        self.x = x
        self.y = y
        self.r = r

    def rysuj(self):
        self.rysujOkrag(self.x, self.y, self.r)