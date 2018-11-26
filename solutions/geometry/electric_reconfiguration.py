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

    # Distancia entre el punto y otro
    def distanceToPoint(self, otherPoint):
        dx = math.fabs(self.x - otherPoint.getX())
        dy = math.fabs(self.y - otherPoint.getY())
        return math.hypot(dx,dy)  # sqrt(x*x + y*y)

    # Determina si el punto se encuentra en un box 
    # Recibe punto inferior izquierdo y superior derecho
    def pointInBox(self, lbPoint, rtPoint):
        return (self.x >= lbPoint.getX() and self.x <= rtPoint.getX() and self.y >= lbPoint.getY() and self.y <= rtPoint.getY())

    @staticmethod
    def direction(p1, p2, p3): #Realiza producto en cruz
        return ((p2.getX() - p1.getX()) * (p3.getY() - p1.getY())) - ((p3.getX() - p1.getX()) * (p2.getY() - p1.getY())) #(p2 - p1) x (p3 - p1)
    
    @staticmethod
    def onSegment(p1, p2, p3):
        return ((min(p1.getX(), p2.getX()) <= p3.getX() <= max(p1.getX(), p2.getX())) and (min(p1.getY(), p2.getY()) <= p3.getY() <= max(p1.getY(), p2.getY())))

    # Recibe un vector de puntos y devuelve la cantidad maxima de puntos que se encuentran alineados en linea recta
    @staticmethod
    def pointsAligned(points):
        res = 0
        for p in range(len(points)-1):
            pend = []
            for j in range(p+1, len(points)):
                aux = ((Line.lineByPoints(points[p], points[j])).pendiente() if not points[p].getX() == points[j].getX() else sys.maxsize)
                pend.append((j, aux))
            pend = sorted(pend, key = lambda x : x[1])
            resAct = 0 
            for k in range(0, j-p-1):
                if math.isclose(math.fabs(pend[k][1]-pend[k+1][1]), 0):
                    resAct+=1
                else:
                    if resAct > res:
                        res = resAct
                    resAct = 0
            if resAct > res:
                res = resAct
        return res + 2 

class Line:

    # Retorna una recta a partir de la forma ax + by + c =0
    def __init__(self, aValue, bValue, cValue):
        self.a = aValue
        self.b = bValue
        self.c = cValue

    # Retorna una recta a partir de la forma y = mx + b
    @staticmethod
    def lineByTwoValues(mValue, nValue):
        return Line((0 - mValue), 1, (0 - nValue))
        
    # Retorna una recta que pase entre dos puntos
    @staticmethod
    def lineByPoints(aPoint, bPoint):
        if aPoint.getX() == bPoint.getX(): # Es una recta vertical
            return Line(1, 0, (0 - aPoint.getX()))
        a = -(aPoint.getY() - bPoint.getY()) / (aPoint.getX() - bPoint.getX())
        c = (a * aPoint.getX()) - aPoint.getY()
        return Line(a, 1, c)

    @staticmethod
    def lineByPointAndSlop(point, slope):
        a = -slope
        return Line(a, 1, -((a * point.getX()) + point.getY()))

    def getA(self):
        return self.a
        
    def getB(self):
        return self.b

    def getC(self):
        return self.c

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
        
    # Retorna si otra linea es paralela con esta
    def isParallel(self, otherLine):
        return self.pendiente() == otherLine.pendiente()

    # Retorna si se tratan de la misma linea
    def isSameLine(self, otherLine):
        return self.isParallel(otherLine) and (self.ordenada() == otherLine.ordenada())

    # Retorna si un punto esta sobre la linea
    def pointInLine(self, aPoint):
        return aPoint.getY() == ((self.pendiente() * aPoint.getX()) + self.ordenada())

    # Retorna el punto de interseccion entre las rectas, en caso de no haber retorna False
    def pointInterseccion(self, otherLine):
        if self.isParallel(otherLine) or self.isSameLine(otherLine): 
            return False
        x = (otherLine.getB() * self.c - self.b * otherLine.getC()) / (otherLine.getA() * self.b - self.a * otherLine.getB())
        y = -(self.a * x + self.c) / self.b if math.isclose(math.fabs(self.b)) else - (self.a * x + otherLine.getC()) / otherLine.getB()
        return Point(x,y)

    # Retorna si otra linea es perpendicular a esta
    def isPerpendicular(self, otherLine):
        return (-1 / self.pendiente()) == otherLine.pendiente()

    def isVertical(self):
        return math.isclose(math.fabs(self.b), 0)

    def isHorizontal(self):
        return math.isclose(math.fabs(self.a), 0)

    # Retorna el punto mas cercano sobre la linea al punto que recibe
    def closestPoint(self, aPoint):
        if self.isVertical():
            return Point(-(self.c), aPoint.getY())
        elif self.isHorizontal():
            return Point(aPoint.getX(), -(self.c))
        perpendicular = Line.lineByPointAndSlop(aPoint, -1 * self.a)
        return self.pointInterseccion(perpendicular)

n = int(input())
while n!=0:
    dots = []
    for i in range(n):
        x,y = list(map(int,input().split(' ')))
        dots.append(Point(x,y))
    print(Point.pointsAligned(dots))
    n = int(input())
