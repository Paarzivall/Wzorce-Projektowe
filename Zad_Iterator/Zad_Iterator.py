class iterator(object):
    def __init__(self, tab):
        self.tab = tab
        self.pos = 0

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        x = self.pos
        self.pos += 1
        if x < len(self.tab):
            return self.tab[x]
        else:
            raise StopIteration


if __name__ == '__main__':
    tab = [0, 1, 0, 0, 2, 3, 4, 5, 0, 0]
    x = iterator(tab)
    with_zero = []
    without_zero = []
    for i in x:
        with_zero.append(i)

    for i in x:
        if i != 0:
            without_zero.append(i)
        else:
            continue

    print(str(with_zero))
    print(str(without_zero))

