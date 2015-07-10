import math
class shape:
    perimeter = 0
    area = 0
    volume = 0
    def calcArea(self):
        pass
    def printInfo(self):
        pass

class TwoDim(shape):
    def calcPerimeter(self):
        pass

class Rectangle(TwoDim):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calcArea(self):
        self.area = self.x*self.y
    def calcPerimeter(self):
        self.perimeter = 2*(self.x+self.y)
    def printInfo(self):
        print "Rectangle -> area: {0}, perimeter: {1}".format(self.area, self.perimeter)

class Triangle(TwoDim):
    n = 0
    def __init__(self, n):
        self.n = n
    def calcArea(self):
        self.area = math.sqrt(3)/4*(self.n**2)
    def calcPerimeter(self):
        self.perimeter = 3*self.n
    def printInfo(self):
        print "Triangle -> area: {0}, perimeter: {1}".format(self.area, self.perimeter)

class Circle(TwoDim):
    r = 0
    def __init__(self, r):
        self.r = r
    def calcArea(self):
        self.area = 3.14*self.r**2
    def calcPerimeter(self):
        self.perimeter = 2*3.14*self.r
    def printInfo(self):
        print "Circle -> area: {0}, perimeter: {1}".format(self.area, self.perimeter)

class ThreeDim(shape):
    def calcVolume(self):
        pass

class Cube(ThreeDim):
    a = 0
    def __init__(self, a):
        self.a = a
    def calcArea(self):
        self.area = 6*self.a**2
    def calcVolume(self):
        self.volume = self.a**3
    def printInfo(self):
        print "Cube -> area: {0}, volume: {1}".format(self.area, self.volume)

class Sphere(ThreeDim):
    r = 0
    def __init__(self, r):
        self.r = r
    def calcArea(self):
        self.area = 4*3.14*self.r**2
    def calcVolume(self):
        self.volume = (4.0/3)*3.14*self.r**3
    def printInfo(self):
        print "Sphere -> area: {0}, volume: {1}".format(self.area, self.volume)


rect = Rectangle(3,4)
tria = Triangle(3)
circ = Circle(2)

cube = Cube(3)
sphe = Sphere(3)

Rectangle.calcArea(rect)
Rectangle.calcPerimeter(rect)
Rectangle.printInfo(rect)

Triangle.calcArea(tria)
Triangle.calcPerimeter(tria)
Triangle.printInfo(tria)

Circle.calcArea(circ)
Circle.calcPerimeter(circ)
Circle.printInfo(circ)

Cube.calcArea(cube)
Cube.calcVolume(cube)
Cube.printInfo(cube)

Sphere.calcArea(sphe)
Sphere.calcVolume(sphe)
Sphere.printInfo(sphe)