class UnionFind:

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

def mst(aristas, nodos):
    aristas = sorted(aristas, key=lambda arista:arista[2])
    ufds = UnionFind(nodos)
    aristasMst = []
    for arista in aristas:
        if not ufds.is_same_set((arista[0] - 1), (arista[1] - 1)):
            ufds.union((arista[0] - 1), (arista[1] - 1))
            aristasMst.append(arista)
    return aristasMst

casos = int(input())
for i in range(casos):
    cantNodos, cantAristas = list(map(int,input().split(' ')))
    aristas = []
    for i in range(cantAristas):
        aristas.append(list(map(int,input().split(' '))))
    aristasMst = mst(aristas,cantNodos)
    print(sum([arista[2] for arista in aristasMst]))

