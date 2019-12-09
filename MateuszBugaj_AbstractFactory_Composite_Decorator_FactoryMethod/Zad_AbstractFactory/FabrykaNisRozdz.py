from FabrykaSter import FabrykaSter
from SterDrukNisRozdz import SterDrukNisRozdz
from SterEkrnNisRozdz import SterEkrnNisRozdz

class FabrykaNisRozdz(FabrykaSter):
    def pobierzSterEkrn(self):
        return SterEkrnNisRozdz()


    def pobierzSterDruk(self):
        return SterDrukNisRozdz()
