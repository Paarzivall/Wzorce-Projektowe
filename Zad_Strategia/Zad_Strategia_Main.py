from Konfiguracja import Konfiguracja
from Zamowienie import Zamowienie


if __name__ == '__main__':
    cenyTowarow = [10.1, 9.2, 8.3, 7.4, 6.5, 5.6, 4.7, 3.8, 2.9]
    typ1 = Konfiguracja('Polska')
    zamowienie1 = Zamowienie(typ1, cenyTowarow)
    typ2 = Konfiguracja('Niemcy')
    zamowienie2 = Zamowienie(typ2, cenyTowarow)

    print(f'Kwota brutto zamowionego w Polsce towaru wynosi: {round(zamowienie1.obliczPodatek(), 2)}')
    print(f'Kwota brutto zamowionego w Niemczech towaru wynosi: {round(zamowienie2.obliczPodatek(), 2)}')