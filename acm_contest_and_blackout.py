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

def indicesAristasMst(aristas, nodos, excluir = -1):
    ufds = UnionFind(nodos)
    indicesAristasMst = []
    for numArista in range(len(aristas)):
        if not excluir == numArista :
            if not ufds.is_same_set((aristas[numArista][0] - 1), (aristas[numArista][1] - 1)):
                ufds.union((aristas[numArista][0] - 1), (aristas[numArista][1] - 1))
                indicesAristasMst.append(numArista)
    return (indicesAristasMst)

def pesosAristas(aristasTotal, aristasAPesar):
    total = 0
    for index in aristasAPesar:
        total += aristasTotal[index][2]
    return total

casos = int(input())
for i in range(casos):
    cantNodos, cantAristas = list(map(int,input().split(' ')))
    aristas = []
    for i in range(cantAristas):
        aristas.append(list(map(int,input().split(' '))))
    aristas = sorted(aristas, key=lambda arista:arista[2])
    aristasMst = indicesAristasMst(aristas,cantNodos)
    msts = []
    for j in aristasMst:
        msts.append(pesosAristas(aristas,indicesAristasMst(aristas, cantNodos, j)))
    print(pesosAristas(aristas, aristasMst),' ',min(msts))

