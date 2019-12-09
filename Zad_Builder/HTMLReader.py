import re


class HTMLReader(object):
    def __init__(self, text):
        self.converter = None
        self.text = str(text)

    def SetConverter(self, converter):
        self.converter = converter

    def ParseHTML(self):
        pattern = "<(\w)>(.+?)<\/\1>"
        output = []
        pos = 0
        while pos < len(self.text):
            tmp = str(self.text[pos])
            if tmp != "<":
                output.append(self.converter.ConvertCharacter(tmp[0]))
                pos += 1
            else:
                tag = re.search(pattern, self.text)
                t = str(tag)
                output.append(self.converter.ConvertTag(t))
                pos += len(t)
        return str(output)
