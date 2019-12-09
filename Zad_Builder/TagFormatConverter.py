from HTMLConverter import HTMLConverter


class TagFormatConverter(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        tag = str(tag)
        return tag.replace(tag, "<(\w)>(.+?)<\/\1>", "{$1#$2}")
