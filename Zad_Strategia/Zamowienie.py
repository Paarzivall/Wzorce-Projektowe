from PodatekPolska import PodatekPolska
from PodatekNiemcy import PodatekNiemcy


class Zamowienie(object):
    def __init__(self, krajPodatku, lista_towarow):
        self.listaTowarow = lista_towarow
        self.krajPodatku = krajPodatku

    def obliczPodatek(self):
        suma = 0

        for towar in self.listaTowarow:
            suma += self.krajPodatku.getKraj().kwotaPodatku(1, towar)

        return suma
