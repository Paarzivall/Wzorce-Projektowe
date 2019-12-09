from ApNadzorujaca import ApNadzorujaca
from Konfiguracja import Konfiguracja

if __name__ == '__main__':
    konf1 = Konfiguracja('Nis')
    apNadzorujaca1 = ApNadzorujaca(konf1)
    apNadzorujaca1.drukuj()
    apNadzorujaca1.rysuj()

    konf2 = Konfiguracja('Wys')
    apNadzorujaca2 = ApNadzorujaca(konf2)
    apNadzorujaca2.drukuj()
    apNadzorujaca2.rysuj()