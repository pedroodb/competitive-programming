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
    resultado = []
    for arista in aristas:
        if not ufds.is_same_set((arista[0] - 1), (arista[1] - 1)):
            ufds.union((arista[0] - 1), (arista[1] - 1))
            resultado.append(arista)
    return resultado

def dfs(memo, visitados, grafo, actual, inicio, maximo):
    if memo[inicio][actual] == -2:
        memo[inicio][actual] = maximo
        visitados[actual] = True
        for i in grafo[actual]:
            if not visitados[i[0]]:
                dfs(memo, visitados, grafo, i[0], inicio, max(i[1], maximo))

        
entrada = list(map(int, input().split(' ')))
caso = 1
while not entrada[0] == 0 and not entrada[1] == 0 and not entrada[2] == 0:
    if caso > 1:
        print()
    print('Case #' + str(caso) )
    nodos = [[] for i in range(entrada[0])]
    aristas = []
    for i in range(entrada[1]):
        aristas.append(list(map(int, input().split(' '))))
    aristas_mst = mst(aristas, len(nodos))
    for arista in aristas_mst:
        nodos[(arista[0]-1)].append(((arista[1]-1), arista[2]))
        nodos[(arista[1]-1)].append(((arista[0]-1), arista[2]))
    memo = [[-2 for i in nodos] for j in nodos]
    for q in range(entrada[2]):
        query = list(map(int, input().split(' ')))
        query[0] -= 1
        query[1] -= 1
        visitados = [False for i in nodos]
        dfs(memo, visitados, nodos, query[0], query[0], 0)
        print("no path") if memo[query[0]][query[1]] == -2 else print(memo[query[0]][query[1]] )
    entrada = list(map(int, input().split(' ')))
    caso+=1