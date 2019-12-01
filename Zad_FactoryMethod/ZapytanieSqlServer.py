from SzablonZapytania import SzablonZapytania
from BazaDanychSqlServer import BazaDanychSqlServer


class ZapytanieSqlServer(SzablonZapytania):
    def _formatujConnect(self, nazwaBD):
        return "Połączono z bazą danych " + nazwaBD

    def _formatujSelect(self, specZapyt):
        return specZapyt

    def utworzBD(self):
        return BazaDanychSqlServer()