class Wektor3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Wektor3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


class Wektor2D(object):
    def __init__(self, vec:Wektor3D=None, x=0, y=0):
        if vec != None:
            self.wektor = vec
        else:
            self.wektor = Wektor3D(x, y, 0)

    def __add__(self, other):
        return Wektor2D(self.wektor + other.wektor)

    def __str__(self):
        return f"{self.wektor}"


ob = Wektor2D(x=1, y=2)
ob2 = Wektor2D(x=1, y=2)

print(ob)
print(ob2)
ob3 = Wektor2D(vec=ob+ob2)
print(ob3)