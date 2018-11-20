import heapq

def dijkstra(graph,origin):
    result = []
    accessibles = [(0,origin,list())]
    seen = set()
    minCost = {origin:0}
    while accessibles:
        (cost,node,path) = heapq.heappop(accessibles)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            result.append((node,cost,path))
            for adjNode, adjCost in graph[node]:
                if not adjNode in seen:
                    auxCost = adjCost + cost
                    if minCost.get(adjNode) is None or auxCost < minCost[adjNode]:
                        minCost[adjNode] = auxCost
                        heapq.heappush(accessibles,(auxCost,adjNode,path))
    return result
