class iterator_with_zeros(object):
    def __init__(self, tab):
        self.tab = tab
        self.pos = 0

    def First(self):
        self.pos = 0

    def Next(self):
        self.pos += 1

    def IsDone(self):
        if self.pos < len(self.tab):
            return True
        else:
            return False

    def CurrentItem(self):
        return self.tab[self.pos]


class iterator_without_zeros(object):
    def __init__(self, tab):
        self.tab = tab
        self.pos = 0

    def First(self):
        self.pos = 0

    def Next(self):
        self.pos += 1


    def IsDone(self):
        if self.pos < len(self.tab):
            return True
        else:
            return False

    def CurrentItem(self):
        return self.tab[self.pos]


class iterator(object):
    def __init__(self, tab):
        self.tab = tab
        self.it = iterator_with_zeros(self.tab)
        self.it2 = iterator_without_zeros(self.tab)

    def getIterator_with_zeros(self):
        self.it.First()
        while self.it.IsDone():
            print(self.it.CurrentItem())
            self.it.Next()

    def getIterator_without_zeros(self):
        self.it2.First()
        while self.it2.IsDone():
            if self.it2.CurrentItem() != 0:
                print(self.it2.CurrentItem())
            self.it2.Next()


if __name__ == '__main__':
    tab = [0, 1, 2, 0, 0, 3, 4]

    ob = iterator(tab)
    print("Przejście po wszystkich elementach")
    ob.getIterator_with_zeros()
    print("Przejście po niezerowych elementach")
    ob.getIterator_without_zeros()



