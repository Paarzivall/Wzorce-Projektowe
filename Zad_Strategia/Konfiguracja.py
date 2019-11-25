from PodatekPolska import PodatekPolska
from PodatekNiemcy import PodatekNiemcy


class Konfiguracja(object):
    def __init__(self, kraj):
        self.kraj = kraj

    def getKraj(self):
        if(self.kraj == 'Polska'):
            return PodatekPolska()
        elif(self.kraj == 'Niemcy'):
            return PodatekNiemcy()
        else:
            return PodatekPolska()
