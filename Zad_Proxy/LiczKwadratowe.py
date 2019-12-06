from RozwiazujRownanie import RozwiazujRownanie


class LiczKwadratowe(object):
    def __init__(self):
        self.rozwiazuj = RozwiazujRownanie()
        self.a = 0
        self.b = 0
        self.c = 0
        self.x = 0
        self.wynik = 0

    def Licz(self, a, b, c, x):
        if not(self.a == a and self.b == b and self.c == c and self.x == x):
            print('Podano nowe dane, obliczam.')
            self.a = a
            self.b = b
            self.c = c
            self.x = x
            self.wynik = self.rozwiazuj.Licz(a, b, c, x)
        else:
            print('Podano drugi raz te same dane')
        return self.wynik