import sys

def existenCiclosNegativos(nodos, aristas):
    distancia = [0 if i == 0 else sys.maxsize for i in nodos]
    for nodo in nodos[:len(nodos)-1]:
        for arista in aristas:
            if distancia[arista[1]] > distancia[arista[0]] + arista[2]:
                distancia[arista[1]] = distancia[arista[0]] + arista[2]
    for arista in aristas:
        if distancia[arista[1]] > distancia[arista[0]] + arista[2]:
            return True
    return False

testCases = int(input())
for i in range(testCases):
    case = list(map(int, input().split(' ')))
    nodos = [[]for i in range(case[0])]
    aristas = []
    for j in range(case[1]):
        aristas.append(list(map(int, input().split(' '))))
    print('possible') if existenCiclosNegativos(nodos, aristas) else print('not possible')
