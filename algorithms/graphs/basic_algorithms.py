import asyncio

def dfs(index, graph, visited):
    visited[index] = True
    for edge in graph[index]:
        if not visited[edge]:
            dfs(edge, graph, visited)

def bfs(graph):
    visited = [False]*len(graph)
    cola = asyncio.Queue()
    cola.put_nowait(graph[0])
    visited[0] = True
    while not cola.empty():
        node = cola.get_nowait()
        for edge in node:
            if not visited[edge]:
                visited[graph.index(edge)] = True
                cola.put_nowait(edge)
            
def relatedComponents(graph):
    visited = [False]*len(graph)
    cant = 0
    for i in range(0, len(graph)):
        if not visited[i]:
            cant+=1
            dfs(i, graph, visited)
    return cant

