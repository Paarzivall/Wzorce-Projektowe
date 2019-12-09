from abc import ABC, abstractmethod


class FabrykaSter(ABC):
    @abstractmethod
    def pobierzSterEkrn(self):
        pass

    @abstractmethod
    def pobierzSterDruk(self):
        pass
