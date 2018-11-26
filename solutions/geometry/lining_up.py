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

    # Recibe una lista de puntos y devuelve la cantidad maxima de puntos que se encuentran alineados en linea recta
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

    # Retorna la pendiente de la recta
    def pendiente(self):
        return self.a / (-self.b)

    def ordenada(self):
        return self.c / (-self.b)

testCases = int(input())
input()
try:
    for i in range(testCases):
        points = list()
        ent = input()
        while not ent == "":
            coord = list(map(int, ent.split(' ')))
            points.append(Point(coord[0], coord[1]))
            ent = input()
        print(Point.pointsAligned(points))
        print()
except:
    print(Point.pointsAligned(points))
    print()

# Los casos de prueba estan bien pero se excede en tiempo
