import math
class shape:
    perimeter = 0
    area = 0
    def calcArea(self):
        pass
    def calcPerimeter(self):
        pass
    def output(self):
        print "area: {0}, perimeter: {1}".format(self.area, self.perimeter)

class Rectangle(shape):
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def calcArea(self):
        self.area = self.x*self.y
    def calcPerimeter(self):
        self.perimeter = 2*(self.x+self.y)

class Triangle(shape):
    n = 0
    def __init__(self, n):
        self.n = n
    def calcArea(self):
        self.area = math.sqrt(3)/4*(self.n**2)
    def calcPerimeter(self):
        self.perimeter = 3*self.n

class Circle(shape):
    r = 0
    def __init__(self, r):
        self.r = r
    def calcArea(self):
        self.area = 3.14*self.r**2
    def calcPerimeter(self):
        self.perimeter = 2*3.14*self.r

rect = Rectangle(5,4)
tria = Triangle(3)
circ = Circle(2)

Rectangle.calcArea(rect)
Rectangle.calcPerimeter(rect)
Rectangle.output(rect)

Triangle.calcArea(tria)
Triangle.calcPerimeter(tria)
Triangle.output(tria)

Circle.calcArea(circ)
Circle.calcPerimeter(circ)
Circle.output(circ)