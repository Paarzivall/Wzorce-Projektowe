from Line import Line
from Rectangle import Rectangle
from Text import Text
from Picture import Picture


if __name__ == '__main__':
    picture1 = Picture()
    picture1.add(Line())
    picture1.add(Rectangle())

    picture2 = Picture()
    picture2.add(Text())
    picture2.add(Line())
    picture2.add(Rectangle())

    picture1.add(picture2)

    picture1.add(Line())
    picture1.draw()