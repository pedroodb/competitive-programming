from functools import reduce
import heapq

class UFDS:

    def __init__(self, n):
        self.num_sets = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, i, original=None):
        if self.parent[i] == i:
            if original is not None:  # path compression 
                self.parent[original] = i
            return i
        if original is None:
            original = i
        return self.find(self.parent[i], original)

    def is_same_set(self, i, j):
        return self.find(i) == self.find(j)

    def union(self, i, j):
        if not self.is_same_set(i, j):
            self.num_sets -= 1
            x = self.find(i)
            y = self.find(j)
            if self.rank[x] > self.rank[y]:  # union by rank
                self.parent[y] = x
            else:
                self.parent[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

def auxNKruskal(edgeList, nodesAmount, foldFunction = (lambda accum, edgeIndex: accum + [(edgeIndex[0],edgeIndex[1])]), accumulator = [], exclude = -1):
    ufds = UFDS(nodesAmount)
    for index, edge in enumerate(edgeList):
        if (not index == exclude) and (not ufds.is_same_set((edge[0] - 1), (edge[1] - 1))):
            ufds.union((edge[0] - 1), (edge[1] - 1))
            accumulator = foldFunction(accumulator,(edge,index))
    return accumulator

def nKruskal(edgeList, nodesAmount, foldFunction, accumulator, n):
    edgeList = sorted(edgeList, key = lambda edge: edge[2])
    mst = auxNKruskal(edgeList, nodesAmount)
    msts = [reduce(foldFunction, mst, accumulator)]
    for index in [idx for edge,idx in mst]:
        heapq.heappush(msts, auxNKruskal(edgeList, nodesAmount, foldFunction, accumulator, index))
    return msts[:n]

casos = int(input())
for i in range(casos):
    cantNodos, cantAristas = list(map(int,input().split(' ')))
    aristas = []
    for i in range(cantAristas):
        aristas.append(list(map(int,input().split(' '))))
    msts = nKruskal(aristas,cantNodos,(lambda acum, edgeIndex: acum+edgeIndex[0][2]),0,2)
    print(msts[0],' ',msts[1])