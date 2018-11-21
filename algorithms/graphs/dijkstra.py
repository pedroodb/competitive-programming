import heapq

#Dijkstra implementation using heap
#Expects a graph as a lists of lists of adjacent indexes and the index of the origin node
#Result is a dictionary where for each index you get the cost of getting to that node from the origin and the path followed 
def dijkstra(graph,origin):
    result = dict()
    accessibles = [(0,origin,list())]
    seen = set()
    minCost = {origin:0}
    while accessibles:
        (cost,node,path) = heapq.heappop(accessibles)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            result.update({node:(cost,path)})
            for adjNode, adjCost in graph[node]:
                if not adjNode in seen:
                    if minCost.get(adjNode) is None or (adjCost + cost) < minCost[adjNode]:
                        minCost[adjNode] = (adjCost + cost)
                        heapq.heappush(accessibles,(minCost[adjNode],adjNode,path))
    return result
