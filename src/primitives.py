class Vec2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        return Vec2d(self.x * k, self.y * k)

    def __truediv__(self, k):
        return Vec2d(self.x / k, self.y / k)

    def mirror(self):
        return Vec2d(self.x, -self.y)

    def __eq__(self, other):
        if isinstance(other, Vec2d):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return "[" + str(round(self.x, 2)) + ", " + str(round(self.y, 2)) + "]"


class Column:
    def __init__(self, name="", height=0):
        self.name = name
        self.height = height
