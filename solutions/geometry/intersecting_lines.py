import math
import sys

class Point:
    
    def __init__(self, xValue, yValue):
        self.x = xValue
        self.y = yValue

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

class Line:

    # Retorna una recta a partir de la forma ax + by + c =0
    def __init__(self, aValue, bValue, cValue):
        self.a = aValue
        self.b = bValue
        self.c = cValue
        
    # Retorna una recta que pase entre dos puntos
    @staticmethod
    def lineByPoints(aPoint, bPoint):
        if aPoint.getX() == bPoint.getX(): # Es una recta vertical
            return Line(1, 0, (0 - aPoint.getX()))
        a = -(aPoint.getY() - bPoint.getY()) / (aPoint.getX() - bPoint.getX())
        c = -(a * aPoint.getX()) - aPoint.getY()
        return Line(a, 1, c)

    def getA(self):
        return self.a
        
    def getB(self):
        return self.b

    def getC(self):
        return self.c

        # Retorna la pendiente de la recta
    def pendiente(self):
        if self.isVertical():
            return sys.maxsize
        elif self.isHorizontal():
            return 0
        return self.a / (-self.b)

    def ordenada(self):
        if self.isVertical():
            return sys.maxsize
        return self.c / (-self.b)

    def isVertical(self):
        return math.isclose(math.fabs(self.b), 0)

    def isHorizontal(self):
        return math.isclose(math.fabs(self.a), 0)

    # Retorna si otra linea es paralela con esta
    #def isParallel(self, otherLine):
    #    return math.isclose((math.fabs(self.a) - math.fabs(otherLine.getA())), 0) and math.isclose((math.fabs(self.b) - math.fabs(otherLine.getB())), 0)

    # Retorna si otra linea es paralela con esta
    def isParallel(self, otherLine):
        return self.pendiente() == otherLine.pendiente()

    # Retorna si se tratan de la misma linea
    def isSameLine(self, otherLine):
        return self.isParallel(otherLine) and (self.ordenada() == otherLine.ordenada())

    # Retorna el punto de interseccion entre las rectas, en caso de no haber retorna False
    def pointInterseccion(self, otherLine):
        if self.isSameLine(otherLine): 
            return "LINE"
        if self.isParallel(otherLine):
            return "NONE"
        x = (otherLine.getB() * self.c - self.b * otherLine.getC()) / (otherLine.getA() * self.b - self.a * otherLine.getB())
        if not math.isclose(math.fabs(self.b), 0):
            y = -((self.a * x )+ self.c) / self.b
        else:
            y = - ((self.a * x) + otherLine.getC()) / otherLine.getB()
        if y == 0:
            y = math.fabs(y)
        if x == 0:
            x = math.fabs(x)
        return "POINT " + str("%.2f" % x) + " " + str("%.2f" % y)

testCases = int(input())
print("INTERSECTING LINES OUTPUT")
for i in range(testCases):
    ent = list(map(int, input().split(" ")))
    line1 = Line.lineByPoints(Point(ent[0], ent[1]), Point(ent[2], ent[3]))
    line2 = Line.lineByPoints(Point(ent[4], ent[5]), Point(ent[6], ent[7]))
    # if not line1.isVertical():
    #     print(line1.pointInterseccion(line2))
    # else:
    print(line2.pointInterseccion(line1))
print("END OF OUTPUT")

# Tiene un solo error cuando una linea es vertical y la otra horizontal en el punto de interseccion