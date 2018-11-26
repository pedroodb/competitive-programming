import math

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

class Segment:

    def __init__(self, firstPoint, secondPoint):
        self.a = firstPoint
        self.b = secondPoint

    def getA(self):
        return self.a

    def getB(self):
        return self.b

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

seg1 = Segment(Point(0,0), Point(3,3))
seg2 = Segment(Point(1,0), Point(4,3))
print(seg1.segmentsIntersect(seg2))