from HTMLConverter import HTMLConverter


class TagToUppercaseConverter(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        t = str(tag)
        finalString = t.replace(t, "<(\w)>(.+?)<\/\1>", 2).upper()
        return finalString