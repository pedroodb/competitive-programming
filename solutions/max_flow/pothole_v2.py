import queue

# Numero maximo de vertices en la red
V = 200
# Red de capacidades, debe ser un grafo NO DIRIGIDO, con las capacidades de las aristas inversas inicializadas en 0
capacities = [[-1 for i in range(V)] for j in range(V)]
# Red de flujo
flows = [[0 for i in range(V)] for j in range(V)]

# Capacidad residual de la arista (x,y)
def residual(x,y):
    return (capacities[x][y] - flows[x][y])

# Devuelve la capacidad minima del camino encontrado (0 en caso de no encontrar uno) y deja en prev[x] el vertice previo a x en el camino
def findPath(s,t,prev):
    visited = [False for i in range(V)]
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        v = q.get()
        if v == t:
            break
        visited[v] = True
        availables = list(map(lambda x: x[0],filter(lambda x: residual(v,x[0]) > 0 and not visited[x[0]],enumerate(capacities[v][:V]))))
        for adj in availables:
            visited[adj] = True
            prev[adj] = v
            q.put(adj)

    minCapacity = 0
    current = t
    while prev[current] != -1:
        minCapacity = min([residual(prev[current],current),minCapacity]) if minCapacity != 0 else residual(prev[current],current)
        current = prev[current]
    
    return minCapacity


def maxFlow(s,t):
    flow = 0
    prev = [-1 for i in range(V)]
    pathCapacity = findPath(s,t,prev)
    while pathCapacity != 0:
        # Se actualiza el valor del flujo maximo
        flow += pathCapacity
        # Se actualizan los valores de la red de flujo
        current = t
        while prev[current] != -1:
            flows[prev[current]][current] += pathCapacity
            flows[current][prev[current]] -= pathCapacity
            current = prev[current]

        prev = [-1 for i in range(V)]
        pathCapacity = findPath(s,t,prev)
    return flow

def resetGraph():
    for i in range(V):
        for j in range(V):
            capacities[i][j] = -1
            flows[i][j] = 0

def buildGraph(v):
    resetGraph()
    for i in range(0,v-1):
        adj = list(map(lambda x: int(x)-1,input().split(' ')[1:]))
        if i == 0:
            maxval = len(adj)
        for j in adj:
            capacities[i][j] = (1 if (i == 0 or j == v-1) else maxval)
            if capacities[j][i] == -1: capacities[j][i] = 0

tc = int(input())
for i in range(tc):
    V = int(input())
    if V != 0:
        buildGraph(V)
        print(maxFlow(0,V-1))
    else:
        print(0)
    input()
