from HTMLConverter import HTMLConverter
import re


class HTMLToText(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        tag = str(tag)
        return re.match("<(\w)>(.+?)</(\w)>", tag).group(2)[0]