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

    # Retorna si otra linea es paralela con esta
    def isParallel(self, otherLine):
        return math.isclose((math.fabs(self.a - otherLine.getA())), 0) and math.isclose(math.fabs(self.b - otherLine.getB()), 0)

    # Retorna si se tratan de la misma linea
    def isSameLine(self, otherLine):
        return self.isParallel(otherLine) and math.isclose(self.c - otherLine.getC(), 0)

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

class Triangle:

    def __init__(self, firstPoint, secondPoint, threePoint):
        self.point1 = firstPoint
        self.point2 = secondPoint
        self.point3 = threePoint

    def perimeter(self):
        return self.point1 + self.point2 + self.point3

    def semiperimeter(self):
        return self.perimeter() / 2

    def height(self):
        s = self.semiperimeter()
        return (2 / self.point1) * math.sqrt(s * (s - self.point1) * (s - self.point2) * (s - self.point2))

    def area(self):
        return (self.height() * self.point1) / 2   

    def containtPoint(self, aPoint):
        pass

class Circle:

    def __init__(self, c, r):
        self.center = c
        self.radio = r

    # Devuelve la longuitud de la circunferencia
    def girthLength(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * (self.radio**2)

    def archLength(self, angle):
        return (self.girthLength() * angle) / 360

    def archArea(self, angle):
        return (self.area() * angle) / 360

    def containtPoint(self, aPoint):
        return (self.radio > aPoint.distanceToPoint(self.center))

class RectangleByTwoPoints:

    def __init__(self, firstPoint, secondPoint):
        self.ulPoint = firstPoint
        self.lrPoint = secondPoint

    def getulPoint(self):
        return self.ulPoint

    def getlrPoint(self):
        return self.lrPoint

    def base(self):
        return self.lrPoint.getX() - self.ulPoint.getX()

    def height(self):
        return self.ulPoint.getY() - self.lrPoint.getY()

    def area(self):
        return self.base() * self.height()

    def perimeter(self):
        return (2 * self.base()) + (2 * self.height())

    def containtPoint(self, aPoint):
        return (aPoint.getX() > self.ulPoint.getX()) and (aPoint.getY() < self.ulPoint.getY()) and (aPoint.getX() < self.lrPoint.getX()) and (aPoint.getY() > self.lrPoint.getY())

class Rectangle:
    
    def __init__(self, base, altura):
        self.b = base
        self.h = altura

    def getBase(self):
        return self.b

    def height(self):
        return self.h

    def area(self):
        return self.b * self.h

    def perimeter(self):
        return (2 * self.b) + (2 * self.h)

class Segment:

    def __init__(self, firstPoint, secondPoint):
        self.a = firstPoint
        self.b = secondPoint

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    # Realiza el producto cruzazo entre el B y el punto
    def crossWithSecondPoint(self, otherPoint):
        return (otherPoint.getX() * self.b.getY()) - (self.b.getX() * otherPoint.getY())

    # Retorna true si el segmento esta en sentido horario a este
    def isClockwise(self, otherSegment):
        return (True if self.crossWithSecondPoint(otherSegment.getB()) > 0 else False)

    # Recibe otro segmento y se fija si interceptan utilizando producto en cruz
    def segmentsIntersect(self, segment2):
        d1 = Point.direction(segment2.getA(), segment2.getB(), self.a)
        d2 = Point.direction(segment2.getA(), segment2.getB(), self.b)
        d3 = Point.direction(self.a, self.b, segment2.getA())
        d4 = Point.direction(self.a, self.b, segment2.getB())
        if ( (d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0) ) and ( (d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0) ):
            return True
        elif d1 == 0 and Point.onSegment(segment2.getA(), segment2.getB(), self.a):
            return True
        elif d2 == 0 and Point.onSegment(segment2.getA(), segment2.getB(), self.b):
            return True
        elif d3 == 0 and Point.onSegment(self.a, self.b, segment2.getA()):
            return True
        elif d4 == 0 and Point.onSegment(self.a, self.b, segment2.getB()):
            return True
        return False