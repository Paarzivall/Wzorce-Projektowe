from Figura import Figura


class Prostokat(Figura):
    def __init__(self, bg, x1, y1, x2, y2):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def rysuj(self):
        self.rysujLinie(self.x1, self.y1, self.x2, self.y2)
        self.rysujLinie(self.x2, self.y1, self.x2, self.y2)
        self.rysujLinie(self.x2, self.y2, self.x1, self.y1)
        self.rysujLinie(self.x1, self.y2, self.x1, self.y1)