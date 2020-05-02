import queue

def maxFlow(s,t):
    flow = 0
    prev = [-1 for i in range(V)]
    pathCapacity = findPath(s,t,prev)
    while pathCapacity != 0:
        flow += pathCapacity
        where = t
        ah = 0
        while prev[where] != -1:
            print(ah)
            ah=ah+1
            capacities[prev[where]][where] -= pathCapacity
            capacities[where][prev[where]] += pathCapacity
            where = prev[where]
        prev = [-1 for i in range(V)]
        pathCapacity = findPath(s,t,prev)
    return flow

def findPath(s,t,prev):
    visited = [False for i in range(V)]
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        v = q.get()
        if v == t:
            break
        visited[v] = True
        adjacents = list(map(lambda x: x[0],filter(lambda x: x[1] > 0 and not visited[x[0]],enumerate(capacities[v][:V]))))
        for adj in adjacents:
            visited[adj] = True
            prev[adj] = v
            q.put(adj)
    pathCapacity = 0
    where = t
    while prev[where] != -1:
        pathCapacity = min([capacities[prev[where]][where],pathCapacity]) if pathCapacity != 0 else capacities[prev[where]][where]
        where = prev[where]
    return pathCapacity

def addEdge(i,j,n):
    adj[i].append(j)
    adj[j].append(i)
    capacities[i][j] = n
    capacities[j][i] = 0

def getWorkerRoad(worker):
    for i, val in enumerate(capacities[worker+2+N][2:N+2]):
        if val == 1: return (i+1,roads[i]+1)
    return (0,0)

N, K = map(int,input().split(' '))

# Un vertice por cada ciudad, uno por cada trabajador, un origen y un destino, y uno extra para limitar el flujo desde el origen
V = N+K+3
capacities = [[-1 for i in range(V)] for j in range(V)]
adj = [[] for i in range(V)]

# Una lista para almacenar los caminos y otra para los posibles materiales
roads = []
roadsForMaterials = {}

# Se crea un vertice extra con flujo n
addEdge(0,1,N)

# Proceso la entrada de ciudades
for city in range(N):
    inp = list(map(int,input().split(' ')))
    roads.append(inp[0]-1)

    for material in inp[2:]:
        rfm = roadsForMaterials.get(material,[])
        rfm.append(city)
        roadsForMaterials[material] = rfm

    # Se une el vertice origen' con el vertice del camino a construir por la ciudad city
    addEdge(1,city+2,1)

for i, worker in enumerate(map(int,input().split(' '))):
    for road in roadsForMaterials.get(worker,[]):
        addEdge(road+2,i+N+2,1)
        addEdge(i+N+2,N+K+2,1)

flow = maxFlow(0,V-1)
if (flow != N):
    print(-1)
else:
    for worker in range(K):
        a, b = getWorkerRoad(worker)
        print(a,b)
