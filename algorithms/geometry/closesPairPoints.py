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

# Cuando la cantidad de puntos de un bloque es <=3 se calcula mediante fuerza bruta.
def closestPairByBrute(points):
    mi = points[0].distanceToPoint(points[1]) #Distancia entre primeros dos puntos 
    if len(points) == 2:
        return points[0], points[1], mi
    p1 = points[0]
    p2 = points[1]
    # Para cada combinacion entre los puntos, excepto la primera
    for i in range(1, len(points)-1):
        for j in range(i + 1, len(points)):
            d = points[i].distanceToPoint(points[j])
            # Si la distancia es menor la actualizo
            if d < mi:
                mi = d
                p1, p2 = points[i], points[j]
    return p1, p2, mi

# Se fija si los puntos entre la division en bloques tienen una distancia menor que el mejor de adentro los bloques
def closestSplitPair(pointsOrderByX, pointsOrderByY, delta, bestPair):
    # Me quedo con el x del punto medio 
    middleX = pointsOrderByX[len(pointsOrderByX) // 2].getX()
    # Crea una nueva lista de puntos que no esta de delta del punto medio de pointsByOrderX
    deltaPoints = [x for x in pointsOrderByY if middleX - delta <= x.getX() <= middleX + delta]
    # La mejor distancia incialmente sera delta
    best = delta 
    # Se itera sobre los posibles puntos que pueden ser menores a delta
    for i in range(len(deltaPoints) - 1):
        for j in range(i+1, min(i + 7, len(deltaPoints))):
            p, q = deltaPoints[i], deltaPoints[j]
            dst = p.distanceToPoint(q)
            if dst < best:
                bestPair = p, q
                best = dst
    return bestPair[0], bestPair[1], best

# Metodo recursivo que va calculando por divide and conquer los puntos mas cercanos 
def closest_pair(pointsOrderByX, pointsOrderByY):
    #Si la cantidad de puntos es menor o igual a tres se puede resolver por furza bruta
    if len(pointsOrderByX) <= 3: 
        return closestPairByBrute(pointsOrderByX)
    # Se divide los puntos en dos sobre el eje x
    middle = len(pointsOrderByX) // 2 
    leftPointsX = pointsOrderByX[:middle] 
    rightPointsX = pointsOrderByX[middle:]
    # Se divide los puntos en dos sobre el eje x
    middleX = pointsOrderByX[middle].getX()
    leftPointsY = []
    rightPonitsY = []
    for x in pointsOrderByY:
        if x.getX() <= middleX:
           leftPointsY.append(x)
        else:
           rightPonitsY.append(x)
    # Se llama recursivamente con los dos arreglos
    (p1, q1, dis1) = closest_pair(leftPointsX, leftPointsY)
    (p2, q2, dis2) = closest_pair(rightPointsX, rightPonitsY)
    # Determinar el la distancia minima entre los dos arreglos, mas sencillo si no se quieren los puntos
    if dis1 <= dis2:
        d = dis1
        mn = (p1, q1)
    else:
        d = dis2
        mn = (p2, q2)
    # Verificar los puntos en el borde
    (p3, q3, mi3) = closestSplitPair(pointsOrderByX, pointsOrderByY, d, mn)
    # Elije el menor entre el punto del cuadrado y el del borde
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

# Devuelve los dos puntos que se encuentran mas cerca y la distancia entre ellos en una tupla
# Solo ordena los puntos sobre los ejes y llama al recursivo
def closestPairPoints(points):
    pointsOrderByX = sorted(points, key = lambda p : p.getX())
    pointsOrderByY = sorted(points, key = lambda p : p.getY())
    return closest_pair(pointsOrderByX, pointsOrderByY)

points = [
    Point(0,0),
    Point(1,0),
    Point(1,1),
    Point(4,0),
    Point(5,1),
    Point(3,3),
    Point(4,4),
    Point(4.5,4)
]
(p1, p2, min) = closestPairPoints(points)
print(p1.getX(), " ", p1.getY())
print(p2.getX(), " ", p2.getY())
print("Distance: ", min)

# Llamar unicamente a closestPairPoints que utiliza los demas metodos 
# Devuelve una tupla donde las ubicaciones 0 y 1 son los dos puntos mas cercanos
# Y el tercer lugar esta la distancia entre ellos