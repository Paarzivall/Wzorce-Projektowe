from SzablonZapytania import SzablonZapytania


class ZapytanieSQLServer(SzablonZapytania):
    def __init__(self):
        pass

    def _formatujConnect(self, nazwaBD):
        return 'Nawiązano połączenie z bazą ' + nazwaBD

    def _formatujSelect(self, zapytanie):
        return zapytanie