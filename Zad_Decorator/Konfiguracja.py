from DekoratorNaglowka1 import DekoratorNaglowka1
from DekoratorNaglowka2 import DekoratorNaglowka2
from DekoratorStopki1 import DekoratorStopki1
from DekoratorStopki2 import DekoratorStopki2


class Konfiguracja(object):
    def __init__(self, komponent):
        self.komponent = komponent
        self.dekoratory = [
            'NAGLOWEK1',
            'NAGLOWEK2',
            'STOPKA1',
            'STOPKA2'
        ]

    def dekorujPotwierdzenie(self, element):
        for x in self.dekoratory:
            if x == element:
                self.komponent = DekoratorNaglowka1(self.komponent)
                break
            elif x == element:
                self.komponent = DekoratorNaglowka2(self.komponent)
                break
            elif x == element:
                self.komponent = DekoratorStopki1(self.komponent)
                break
            elif x == element:
                self.komponent = DekoratorStopki2(self.komponent)
                break

    def pobierzPotwierdzenie(self):
        return self.komponent
