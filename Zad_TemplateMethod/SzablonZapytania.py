from abc import ABC, abstractmethod


class SzablonZapytania(ABC):
    def __init__(self):
        pass

    def wykonajZapytanie(self, nazwaBD, zapytanie):
        print(self._formatujConnect(nazwaBD))
        return self._formatujSelect(zapytanie)


    @abstractmethod
    def _formatujConnect(self, nazwaBD):
        pass

    @abstractmethod
    def _formatujSelect(self, zapytanie):
        pass