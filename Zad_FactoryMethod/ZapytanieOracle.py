from SzablonZapytania import SzablonZapytania
from BazaDanychOracle import BazaDanychOracle

class ZapytanieOracle(SzablonZapytania):
    def _formatujConnect(self, nazwaBD):
        return "Połączono z bazą danych " + nazwaBD

    def _formatujSelect(self, specZapyt):
        return specZapyt + ";"

    def utworzBD(self):
        return BazaDanychOracle()