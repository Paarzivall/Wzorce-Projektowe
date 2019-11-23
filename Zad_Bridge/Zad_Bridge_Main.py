from Okrag import Okrag
from Prostokat import Prostokat
from BibliotekaV1 import BibliotekaV1
from BibliotekaV2 import BibliotekaV2

if __name__ == '__main__':
    biblioteka1 = BibliotekaV1()
    biblioteka2 = BibliotekaV2()

    figura1 = Okrag(biblioteka1, 2, 3, 4)
    figura2 = Prostokat(biblioteka2, 1, 2, 3, 4)
    figura1.rysuj()
    figura2.rysuj()