from TagCapitalizeConverter import TagCapitalizeConverter
from TagToUppercaseConverter import TagToUppercaseConverter
from TagFormatConverter import TagFormatConverter
from HTMLToText import HTMLToText


class Konfiguracja(object):
    def GetConverter(self, converter):
        if converter == "HTMLToText":
            return HTMLToText()
        elif converter == "TagCapitalizeConverter":
            return TagCapitalizeConverter()
        elif converter == "TagToUppercaseConverter":
            return TagToUppercaseConverter()
        elif converter == "TagFormatConverter":
            return TagFormatConverter()
        else:
            raise NameError

