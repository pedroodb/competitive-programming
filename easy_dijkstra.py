import heapq

def dijkstra(graph,origin,destiny):
    accessibles = [(0,origin,list())]
    seen = set()
    minCost = {origin:0}
    while accessibles:
        (cost,node,path) = heapq.heappop(accessibles)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == destiny:
                return cost
            for adjNode, adjCost in graph[node]:
                if not adjNode in seen:
                    auxCost = adjCost + cost
                    if minCost.get(adjNode) is None or auxCost < minCost[adjNode]:
                        minCost[adjNode] = auxCost
                        heapq.heappush(accessibles,(auxCost,adjNode,path))
    return None

tc = input()
for t in range(int(tc)):
    nodos, aristas = list(map(int,input().split(' ')))
    g = [[] for _ in range(nodos)]
    for i in range(aristas):
        o,d,w = list(map(int,input().split(' ')))
        g[o-1].append((d-1,w))
    query = list(map(int,input().split(' ')))
    dj = dijkstra(g,query[0]-1,query[1]-1)
    if dj is None:
        print('NO')
    else:
        print(dj)
    