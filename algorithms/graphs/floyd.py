import sys

INF = sys.maxsize
  
def floyd(graph,prev):
    v = len(graph) 
    for k in range(v): 
        for i in range(v): 
            for j in range(v): 
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    prev[i][j] = prev[k][j]
    return graph

def getPrev(graph):
    v = len(graph)
    prev = [[None for _ in range(v)] for i in range(v)]
    for i in range(0,v):
        for j in range(0,v):
            prev[i][j] = i
            if (i != j and graph[i][j] == 0):
                prev[i][j] = None
    return prev

graph = [[INF,10,20,30,INF,INF],[INF,INF,INF,INF,INF,7],[INF,INF,INF,INF,INF,5],[INF,INF,INF,INF,10,INF],[2,INF,INF,INF,INF,4],[INF,5,7,INF,6,INF]] 
# Print the solution 
pr = getPrev(graph)
print(floyd(graph,pr))
print(pr)