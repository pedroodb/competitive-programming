import sys

def bellmanFord(nodes, edges):
    distancia = [0 if i == 0 else sys.maxsize for i in nodos]
    for _ in range(0, nodes-1):
        for edge in edges:
            if distancia[arista[1]] > distancia[arista[0]] + arista[2]:
                distancia[arista[1]] = distancia[arista[0]] + arista[2]
    for arista in aristas:
        if distancia[arista[1]] > distancia[arista[0]] + arista[2]:
            return None
    return distancia
