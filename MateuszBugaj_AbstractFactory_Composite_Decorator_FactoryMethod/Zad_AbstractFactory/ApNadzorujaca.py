class ApNadzorujaca(object):

    def __init__(self, typFabryka):
        self.typFabryka = typFabryka
        self.fabrykaSter = self.typFabryka.getTypFabryki()

    def drukuj(self):
        self.fabrykaSter.pobierzSterDruk().drukuj()

    def rysuj(self):
        self.fabrykaSter.pobierzSterEkrn().rysuj()