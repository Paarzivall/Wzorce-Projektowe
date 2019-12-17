from HTMLConverter import HTMLConverter
import re


class TagFormatConverter(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        tag = str(tag)
        finalString = "{"
        finalString += re.match("<(\w)>(.+?)</(\w)>", tag).group(1)[0]
        finalString += "#"
        finalString += re.match("<(\w)>(.+?)</(\w)>", tag).group(2)[0]
        finalString += "}"

        return finalString
