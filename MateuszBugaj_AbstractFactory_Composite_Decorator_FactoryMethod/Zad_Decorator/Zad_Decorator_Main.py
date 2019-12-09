from Zamowienie import Zamowienie


if __name__ == '__main__':
    zamowienie = Zamowienie()
    komponent1 = zamowienie.generuj(['NAGLOWEK1', 'STOPKA1', 'STOPKA2'])

    komponent2 = zamowienie.generuj(['NAGLOWEK2', 'NAGLOWEK1', 'STOPKA1'])

    zamowienie.drukuj([komponent1])
    print("\n")
    zamowienie.drukuj([komponent2])