from FabrykaSter import FabrykaSter
from SterDrukWysRozdz import SterDrukWysRozdz
from SterEkrnWysRozdz import SterEkrnWysRozdz


class FabrykaWysRozdz(FabrykaSter):
    def pobierzSterEkrn(self):
        return SterEkrnWysRozdz()

    def pobierzSterDruk(self):
        return SterDrukWysRozdz()
