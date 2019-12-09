from HTMLReader import HTMLReader
from TagCapitalizeConverter import TagCapitalizeConverter
from TagToUppercaseConverter import TagToUppercaseConverter
from TagFormatConverter import TagFormatConverter
from HTMLToText import HTMLToText
from Konfiguracja import Konfiguracja


if __name__ == '__main__':
    tekst = "A<b>l</b>a ma <i>k</i>o<u>t</u>a"
    reader = HTMLReader(tekst)
    konf1 = Konfiguracja().GetConverter("TagCapitalizeConverter")
    konf2 = Konfiguracja().GetConverter("TagToUppercaseConverter")
    konf3 = Konfiguracja().GetConverter("TagFormatConverter")
    konf4 = Konfiguracja().GetConverter("HTMLToText")

    print(f"Plik wejsciowy:\t\t{tekst}")
    reader.SetConverter(konf1)
    print(f"HTML to ASCII:\t\t{reader.ParseHTML()}")
