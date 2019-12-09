from HTMLReader import HTMLReader
from Konfiguracja import Konfiguracja


if __name__ == '__main__':
    tekst = "A<b>l</b>a ma <i>k</i>o<u>t</u>a"
    # tekst = "<b>l</b>"
    reader = HTMLReader(tekst)
    konf1 = Konfiguracja().GetConverter("TagCapitalizeConverter")
    konf2 = Konfiguracja().GetConverter("TagToUppercaseConverter")
    konf3 = Konfiguracja().GetConverter("TagFormatConverter")
    konf4 = Konfiguracja().GetConverter("HTMLToText")

    print(f"Plik wejsciowy:\t\t{tekst}")
    reader.SetConverter(konf1)
    print(f"HTML to HTML, zawartosc tagow wielkimi literami:\t\t{reader.ParseHTML()}")

    reader.SetConverter(konf2)
    print(f"HTML to ASCII, Tagi wielkimi literami:\t\t{reader.ParseHTML()}")

    reader.SetConverter(konf3)
    print(f"HTML to inny format tagow:\t\t{reader.ParseHTML()}")

    reader.SetConverter(konf4)
    print(f"HTML to ASCII:\t\t{reader.ParseHTML()}")
