from abc import ABC, abstractmethod


class ObliczPodatek(ABC):
    def __init__(self, krajPodatku):
        self.krajPodatku = krajPodatku

    @abstractmethod
    def kwotaPodatku(self, ilosc, cena):
        self.krajPodatku.kwotaPodatku()