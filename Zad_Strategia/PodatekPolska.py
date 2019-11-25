from ObliczPodatek import ObliczPodatek


class PodatekPolska(ObliczPodatek):
    def __init__(self):
        self.VAT = 0.23

    def kwotaPodatku(self, ilosc, cena):
        return ilosc * (cena + (cena * self.VAT))