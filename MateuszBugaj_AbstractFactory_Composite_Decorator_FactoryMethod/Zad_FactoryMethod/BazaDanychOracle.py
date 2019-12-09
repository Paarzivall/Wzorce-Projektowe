from BazaDanych import BazaDanych


class BazaDanychOracle(BazaDanych):
    def WykonajSelect(self, zapytanie):
        print(f"Oracle\> {zapytanie}\n\tWykonano pomyślnie")
