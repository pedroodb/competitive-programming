def dependencias(vertice,vertices,visitados):
    visitados[vertice]=True
    total = 0
    for hijo in vertices[vertice]:
        if not visitados[hijo]:
            depsDeHijo = dependencias(hijo,vertices,visitados)
            total += depsDeHijo
    return total + 1

def mapearVertice(entrada):
    return int(entrada)-1

cantTareas = int(input())
while not cantTareas == 0:
    vertices=['' for _ in range(cantTareas)]
    for tarea in range(cantTareas):
        vertices[tarea] = list(map(mapearVertice,input().split(' ')))[1:]
    maximo = (-1,0)
    for vertice in range(len(vertices)):
        depsPorVertice = dependencias(vertice,vertices,[False for _ in vertices])
        if depsPorVertice > maximo[1]:
            maximo = (vertice,depsPorVertice)
    print(maximo[0]+1)
    cantTareas = int(input())
