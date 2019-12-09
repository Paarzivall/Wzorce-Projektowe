from BazaDanych import BazaDanych


class BazaDanychSqlServer(BazaDanych):
    def WykonajSelect(self, zapytanie):
        print(f"SQL Server\> {zapytanie}\n\tWykonano pomyślnie")
