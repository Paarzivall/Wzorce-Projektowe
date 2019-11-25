from ObliczPodatek import ObliczPodatek


class PodatekNiemcy(ObliczPodatek):
    def __init__(self):
        self.VAT = 0.20

    def kwotaPodatku(self, ilosc, cena):
        return ilosc * (cena + (cena * self.VAT))