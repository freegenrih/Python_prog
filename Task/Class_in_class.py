import math


# ================================================== Класс геометрии (имен) ===========================================

class Geometry:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return "Name:{};".format(
            self.name,
        )


# ================================================== Класс круга ======================================================

class Circle(Geometry):
    def __init__(self, name: str, radius: int):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        area = self.radius * math.pi
        print("Area Circle", end=' ')
        return area

    def get_perimeter(self):
        p = 2 * math.pi * self.radius
        print('Perimeter Circle', end=' ')
        return p

    def __str__(self):
        return "Name:{}; Radius:{};".format(
            self.name,
            self.radius
        )


# ============================================== Класс прямоугольника =================================================

class Rectangle(Geometry):
    def __init__(self, name: str, a: int, b: int):
        super().__init__(name)
        self.a = a
        self.b = b

    def get_area(self):
        s = self.a * self.b
        print("Area Rectangle", end=' ')
        return s

    def get_perimeter(self):
        p = self.a + self.b
        print("Perimeter Rectangle", end=' ')
        return p

    def __str__(self):
        return 'Name:{}; A:{}; B:{};'.format(
            self.name,
            self.a,
            self.b,
        )


# ============================================== Класс Треугольника ===================================================

class Triangle(Geometry):
    def __init__(self, name: str, a: int, b: int, c: int):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = 1 / 2 * (self.a + self.b + self.c)
        s = math.sqrt(p * ((p - self.a) * (p - self.b) * (p - self.c)))
        print('Area Triangle', end=' ')
        return s

    def get_perimeter(self):
        p = self.a + self.b + self.c
        print('Perimetr Triangle', end=' ')
        return p

    def __str__(self):
        return 'Name:{}; A:{}; B:{}; C:{};'.format(
            self.name,
            self.a,
            self.b,
            self.c,
        )


# =====================================================================================================================


geom = Rectangle('rectangle', 1, 1)
geom_1 = Circle('circle', 6)
geom_2 = Triangle('triangle', 2, 7, 7)

print(geom)
print('Name', geom.name)
print(geom.get_area())
print(geom.get_perimeter(), '\n')
print(geom_1)
print('Name', geom_1.name)
print(geom_1.get_area())
print(geom_1.get_perimeter(), '\n')
print(geom_2)
print('Name', geom_2.name)
print(geom_2.get_area())
print(geom_2.get_perimeter(), '\n')
