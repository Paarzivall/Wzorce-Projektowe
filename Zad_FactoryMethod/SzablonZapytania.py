from abc import ABC


class SzablonZapytania(ABC):
    def WykonajZapytanie(self, NazwaBD, specZapyt):
        BD = self.utworzBD()

        komendaBD = self._formatujConnect(NazwaBD)

        komendaBD = self._formatujSelect(specZapyt)
        BD.WykonajSelect(komendaBD)

    def _formatujConnect(self, NazwaBD):
        pass

    def _formatujSelect(self, specZapyt):
        pass

    def utworzBD(self):
        pass