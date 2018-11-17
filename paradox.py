def convertToBolean(aValue):
    if aValue == "true":
        return True
    else:
        return False
        
def dfs(origen, index, cantidad, aristas, visitados):
    if visitados[index]:
        if origen == index:
            return cantidad
        else: 
            return 0
    visitados[index] = True
    peso = 0 if aristas[index][1] else 1
    return dfs(origen, aristas[index][0], cantidad + peso, aristas, visitados)

def isParadox(cantNodos, aristas):
    for i in range(cantNodos):
        visitados = [False]*cantNodos
        if dfs(i, i, 0, aristas, visitados)%2 == 1:
            return True
    return False

cantDeclaraciones = int(input())
while not cantDeclaraciones == 0:
    aristas = []
    for i in range(cantDeclaraciones):
        aristaNueva = input().split(' ')
        aristaNueva[0] = int(aristaNueva[0]) - 1
        aristaNueva[1] = convertToBolean(aristaNueva[1])
        aristas.append(aristaNueva)
    print("PARADOX") if isParadox(cantDeclaraciones, aristas) else print("NOT PARADOX")
    cantDeclaraciones = int(input())