from HTMLConverter import HTMLConverter


class HTMLToText(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        tag = str(tag)
        return tag.replace(tag, "<(\w)>(.+?)<\/\1>", 2)