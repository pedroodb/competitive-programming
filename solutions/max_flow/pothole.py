'''
To keep it simple, we will use a 2-dimensional array for storing 
the capacities of the residual network that we are left with 
after each step in the algorithm. Initially the residual network 
is just the original network. We will not store the flows along 
the edges explicitly, but it’s easy to figure out how to find 
them upon the termination of the algorithm: for each edge x-y 
in the original network the flow is given by the capacity of 
the backward edge y-x in the residual network. 
Be careful though; if the reversed arc y-x also exists in the 
original network, this will fail, and it is recommended that the 
initial capacity of each arc be stored somewhere, and then the 
flow along the edge is the difference between the initial and 
the residual capacity.
'''

import queue

graph = [[-1 for i in range(201)] for j in range(201)]

def maxFlow(v):
    result = 0
    while True:
        pathCapacity = findPath(v)
        if pathCapacity != 0:
            result += pathCapacity
        else:
            return result

def findPath(vSize):
    visited = [False for i in range(vSize)]
    prev = [-1 for i in range(vSize)]
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        v = q.get()
        # Sink is the last vertex
        if v == vSize-1:
            break
        visited[v] = True
        adjacents = list(map(lambda x: x[0],filter(lambda x: x[1] > 0 and not visited[x[0]],enumerate(graph[v][:vSize]))))
        for adj in adjacents:
            visited[adj] = True
            prev[adj] = v
            q.put(adj)

    #Get pathCapacity as the lowest capacity from edges in the path
    pathCapacity = 0
    where = vSize-1
    while prev[where] != -1:
        pathCapacity = min([graph[prev[where]][where],pathCapacity]) if pathCapacity != 0 else graph[prev[where]][where]
        where = prev[where]
    
    #Update residual capacities
    where = vSize-1
    while prev[where] != -1:
        graph[prev[where]][where] -= pathCapacity
        graph[where][prev[where]] += pathCapacity
        where = prev[where]
    return pathCapacity

def resetGraph():
    for i in range(200):
        for j in range(200):
            graph[i][j] = -1

def buildGraph(v):
    resetGraph()
    for i in range(0,v-1):
        ady = list(map(lambda x: int(x)-1,input().split(' ')[1:]))
        if i == 0:
            maxval = len(ady)
        for j in ady:
            graph[i][j] = (1 if (i == 0 or j == v-1) else maxval)
            graph[j][i] = 0

tc = int(input())
for i in range(tc):
    v = int(input())
    if v != 0:
        buildGraph(v)
        print(maxFlow(v))
    else:
        print(0)
    input()
