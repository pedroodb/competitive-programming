import sys

def bellmanFord(nodes, edges):
    distancia = [0 if i == 0 else sys.maxsize for i in nodes]
    for _ in range(0, nodes-1):
        for edge in edges:
            if distancia[edge[1]] > distancia[edge[0]] + edge[2]:
                distancia[edge[1]] = distancia[edge[0]] + edge[2]
    for edge in edges:
        if distancia[edge[1]] > distancia[edge[0]] + edge[2]:
            return None
    return distancia
