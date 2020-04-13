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

V = 201
capacities = [[-1 for i in range(V)] for j in range(V)]


def maxFlow(s,t):

    flow = 0
    prev = [-1 for i in range(V)]
    pathCapacity = findPath(s,t,prev)

    while pathCapacity != 0:

        flow += pathCapacity
        #Update residual capacities
        where = t
        while prev[where] != -1:
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
        # Sink is the last vertex
        if v == t:
            break
        visited[v] = True
        adjacents = list(map(lambda x: x[0],filter(lambda x: x[1] > 0 and not visited[x[0]],enumerate(capacities[v][:V]))))
        for adj in adjacents:
            visited[adj] = True
            prev[adj] = v
            q.put(adj)

    #Get pathCapacity as the lowest capacity from edges in the path
    pathCapacity = 0
    where = t
    while prev[where] != -1:
        pathCapacity = min([capacities[prev[where]][where],pathCapacity]) if pathCapacity != 0 else capacities[prev[where]][where]
        where = prev[where]
    
    return pathCapacity

def resetGraph():
    for i in range(200):
        for j in range(200):
            capacities[i][j] = -1

def buildGraph(v):
    resetGraph()
    for i in range(0,v-1):
        adj = list(map(lambda x: int(x)-1,input().split(' ')[1:]))
        if i == 0:
            maxval = len(adj)
        for j in adj:
            capacities[i][j] = (1 if (i == 0 or j == v-1) else maxval)
            capacities[j][i] = 0

tc = int(input())
for i in range(tc):
    V = int(input())
    if V != 0:
        buildGraph(V)
        print(maxFlow(0,V-1))
    else:
        print(0)
    input()
