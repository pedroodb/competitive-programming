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
    
    # Recibe un vector de lineas y devuelve la cantidad maxima de puntos que se encuentran alineados en linea recta
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

points = [ # 10 Puntos
    Point(0,0),
    Point(1,0),
    Point(3,0),
    Point(1,1),
    Point(4,1),
    Point(2,2),
    Point(3,2),
    Point(3,3),
    Point(4,3),
    Point(1,4)
]
print(Point.pointsAligned(points)) #Deveria devolver 4 de la diagonal principal