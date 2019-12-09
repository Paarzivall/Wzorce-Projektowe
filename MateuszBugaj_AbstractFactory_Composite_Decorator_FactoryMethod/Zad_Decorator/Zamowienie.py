from Konfiguracja import Konfiguracja
from Potwierdzenie import Potwierdzenie


class Zamowienie(object):
    def generuj(self, dekoratory):
        konfiguracja = Konfiguracja(Potwierdzenie())
        for dekorator in dekoratory:
            konfiguracja.dekorujPotwierdzenie(dekorator)
        return konfiguracja.pobierzPotwierdzenie()

    def drukuj(self, komponenty):
        for komponent in komponenty:
            komponent.drukuj()
