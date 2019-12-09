from HTMLConverter import HTMLConverter


class TagCapitalizeConverter(HTMLConverter):
    def ConvertCharacter(self, character):
        return character

    def ConvertTag(self, tag):
        t = tag
        content = t[t.find(">") + 1: t.find("<")]
        print(type(content))
        # content = t.replace(t, "<(\w)>(.+?)<\/\1>", 2)
        # name = t.replace(t, "<(\w)>(.+?)<\/\1>", 1)
        name = t[t.find("<") + 1: t.find(">")]
        print(type(name))
        return f'<{name}>{content.upper()}</{name}>'
