import re


class HTMLReader(object):
    def __init__(self, text):
        self.converter = None
        self.text = str(text)

    def SetConverter(self, converter):
        self.converter = converter

    def ParseHTML(self):
        output = []
        pos = 0
        while pos < len(self.text):
            tmp = str(self.text[pos])
            if tmp != "<":
                output.append(self.converter.ConvertCharacter(tmp[0]))
                pos += 1
            else:
                tag = re.search("<(\w)>(.+?)</(\w)>", self.text[pos:])[0]
                t = str(tag)
                output.append(self.converter.ConvertTag(t))
                pos += len(tag)
        return str(output)
