import math 

class Point:
    
    def __init__(self, xValue, yValue):
        self.x = xValue
        self.y = yValue

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def distanceToPoint(self, otherPoint):
        dx = math.fabs(self.x - otherPoint.getX())
        dy = math.fabs(self.y - otherPoint.getY())
        return math.hypot(dx,dy)  # sqrt(x*x + y*y)

class Triangle:

    def __init__(self, firstPoint, secondPoint, threePoint):
        self.point1 = firstPoint
        self.point2 = secondPoint
        self.point3 = threePoint

    def containtPoint(self, aPoint):
        pass

class Circle:

    def __init__(self, c, r):
        self.center = c
        self.radio = r

    def containtPoint(self, aPoint):
        return (self.radio > aPoint.distanceToPoint(self.center))

class Rectangle:

    def __init__(self, firstPoint, secondPoint):
        self.ulPoint = firstPoint
        self.lrPoint = secondPoint

    def containtPoint(self, aPoint):
        return (aPoint.getX() > self.ulPoint.getX()) and (aPoint.getY() < self.ulPoint.getY()) and (aPoint.getX() < self.lrPoint.getX()) and (aPoint.getY() > self.lrPoint.getY())

def crearFigura(figura):
    if figura[0] == "c":
        return Circle(Point(float(figura[1]), float(figura[2])), float(figura[3]))
    elif figura[0] == "r":
        return Rectangle(Point(float(figura[1]), float(figura[2])), Point(float(figura[3]), float(figura[4])))
    else:
        return Triangle(Point(float(figura[1]), float(figura[2])),Point(float(figura[3]), float(figura[4])),Point(float(figura[5]), float(figura[6])))

entrada = input()
listaFiguras = []
while not entrada == "*":
    figura = entrada.split(" ")
    listaFiguras.append(crearFigura(figura))
    entrada = input()
entrada = input().split(" ")
numberOfPoint = 1
while not entrada[0] == "9999.9" and not entrada[1] == "9999.9":
    p = Point(float(entrada[0]), float(entrada[1]))
    algunaFigura = False
    for figura in listaFiguras:
        if figura.containtPoint(p): 
            print("Point " + str(numberOfPoint) + " is contained in figure " + str(listaFiguras.index(figura)+1))
            algunaFigura = True
    if not algunaFigura:
        print("Point " + str(numberOfPoint) +  " is not contained in any figure")
    entrada = input().split(" ")
    numberOfPoint += 1
            