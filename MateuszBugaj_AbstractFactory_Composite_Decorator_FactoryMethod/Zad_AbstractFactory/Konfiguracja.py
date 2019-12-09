from FabrykaNisRozdz import FabrykaNisRozdz
from FabrykaWysRozdz import FabrykaWysRozdz


class Konfiguracja(object):
    def __init__(self, typFabryki):
        self.typFabryki = typFabryki

    def getTypFabryki(self):
        if self.typFabryki == 'Nis':
            return FabrykaNisRozdz()
        elif self.typFabryki == 'Wys':
            return FabrykaWysRozdz()
        else:
            print('Nie ma takiej fabryki')



