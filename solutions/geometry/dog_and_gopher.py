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

def dobleDistance(dog, gopher, hole):
    return (hole.distanceToPoint(gopher) * 2) <= (hole.distanceToPoint(dog))

try:
    while True:
        entrada = list(map(float, input().split(' ')))
        gopher = Point(entrada[1], entrada[2])
        dog = Point(entrada[3], entrada[4])
        escapo = False
        for case in range(int(entrada[0])):
            holeInput = input().split(' ')
            if not escapo:
                hole = Point(float(holeInput[0]), float(holeInput[1]))
                if dobleDistance(dog, gopher, hole):
                    escapo = True
                    holeWin = hole
        print("The gopher can escape through the hole at (" + str("%.3f" % hole.getX()) + "," + str("%.3f" % hole.getY()) + ").") if escapo else print("The gopher cannot escape.")
        input()
except:
    pass

    
