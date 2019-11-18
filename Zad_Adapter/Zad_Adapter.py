from abc import ABC, abstractmethod


class XXOkrag(object):
    def __init__(self):
        pass

    def wyswietlaj(self):
        return f'Jestem Okręgiem'

    def wypelniaj(self):
        pass

    def usuwaj(self):
        pass

    def pobierzPolozenie(self):
        pass

    def nadajPolozenie(self):
        pass

    def ustawKolor(self):
        pass

class Figura(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def pobierzPolozenie(self):
        pass

    def NadajPolozenie(self):
        pass

    @abstractmethod
    def wyswietl(self):
        pass

    def wypelnij(self):
        pass

    def usun(self):
        pass


class Kwadrat(Figura):
    def __init__(self):
        super().__init__()

    def wyswietl(self):
        return f'Jestem Kwadratem'


class Linia(Figura):
    def __init__(self):
        super().__init__()

    def wyswietl(self):
        return f'Jestem Linią'


class Punkt(Figura):
    def __init__(self):
        super().__init__()

    def wyswietl(self):
        return f'Jestem Punktem'


class Okrag(Figura):
    def __init__(self):
        super().__init__()
        self.xxOkrag = XXOkrag()

    def pobierzPolozenie(self):
        self.xxOkrag.pobierzPolozenie()

    def nadajPolozenie(self):
        self.xxOkrag.nadajPolozenie()

    def wyswietl(self):
        return self.xxOkrag.wyswietlaj()

    def wypelnij(self):
        self.xxOkrag.wypelniaj()

    def nadajKolor(self):
        self.xxOkrag.ustawKolor()

    def usun(self):
        self.xxOkrag.usuwaj()


if __name__ == '__main__':
    punkt = Punkt()
    linia = Linia()
    kwadrat = Kwadrat()
    okrag = Okrag()

    figury = [punkt, linia, kwadrat, okrag]

    for figura in figury:
        print(figura.wyswietl())