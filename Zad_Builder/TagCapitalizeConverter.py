from HTMLConverter import HTMLConverter
import re


class TagCapitalizeConverter(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        t = str(tag)
        content = re.search("<(\w)>(.+?)</(\w)>", t).group(2)
        name = re.search("<(\w)>(.+?)</(\w)>", t).group(1)
        return f'<{name}>{content.upper()}</{name}>'
