import math


#================================================== Класс геометрии (имени) ============================================
class geometry:
    def __init__(self, name: str):
        self.name = name


    def __str__(self):
        return "Name:{};".format(
            self.name,
        )

#================================================== Класс круга ========================================================
# Класс круга
class circle(geometry):
    def __init__(self, name: str, radius: int):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        area = self.radius*math.pi
        print("Area Circle", end=' ')
        return area

    def get_perimeter(self):
        P = 2*math.pi*self.radius
        print('Perimeter Circle', end=' ')
        return P



#============================================== Класс прямоугольника ===================================================
#клас прямоугольника
class rectangle(geometry):
    def __init__(self,name: str,a: int, b: int):
        super().__init__(name)
        self.a = a
        self.b = b

    def get_area(self):
        S = self.a * self.b
        print("Area Rectangle", end=' ')
        return S

    def get_perimeter(self):
        P = self.a + self.b
        print("Perimeter Rectangle", end=' ')
        return P

#============================================== Класс Треугольника =====================================================

class triangle(geometry):
    def __init__(self,name: str, a: int, b: int, c: int):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        P = 1/2*(self.a + self.b + self.c)
        S=math.sqrt(P*((P-self.a)*(P-self.b)*(P-self.c)))
        print('Area Triangle', end=' ')
        return S

    def get_perimeter(self):
        P=self.a + self.b + self.c
        print('Perimetr Triangle', end=' ')
        return P
#=======================================================================================================================


geom=rectangle('rectangle', 1, 1 )
geom_1=circle('circle', 6)
geom_2= triangle('triangle', 2, 7, 7)


print('Name',geom.name)
print(geom.get_area())
print(geom.get_perimeter(),'\n')
print('Name',geom_1.name)
print(geom_1.get_area())
print(geom_1.get_perimeter(),'\n')
print('Name',geom_2.name)
print(geom_2.get_area())
print(geom_2.get_perimeter(),'\n')
