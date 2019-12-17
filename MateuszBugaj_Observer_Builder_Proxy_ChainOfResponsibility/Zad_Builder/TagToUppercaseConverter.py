from HTMLConverter import HTMLConverter
import re


class TagToUppercaseConverter(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        t = str(tag)
        finalString = re.match("<(\w)>(.+?)</(\w)>", t).group(2)[0].upper()
        return finalString