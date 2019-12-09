from DekoratorNaglowka1 import DekoratorNaglowka1
from DekoratorNaglowka2 import DekoratorNaglowka2
from DekoratorStopki1 import DekoratorStopki1
from DekoratorStopki2 import DekoratorStopki2


class Konfiguracja(object):
    def __init__(self, komponent):
        self.komponent = komponent


    def dekorujPotwierdzenie(self, element):
        #for x in self.dekoratory:
        if element == 'NAGLOWEK1':
            # print('n1')
            self.komponent = DekoratorNaglowka1(self.komponent)
        elif element == 'NAGLOWEK2':
            # print('n2')
            self.komponent = DekoratorNaglowka2(self.komponent)
        elif element == 'STOPKA1':
            # print('s1')
            self.komponent = DekoratorStopki1(self.komponent)
        elif element == 'STOPKA2':
            # print('s2')
            self.komponent = DekoratorStopki2(self.komponent)

    def pobierzPotwierdzenie(self):
        return self.komponent
