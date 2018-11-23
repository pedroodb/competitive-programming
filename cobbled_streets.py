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

#Expects an edgeList as a list of (origin, destiny, weigth) and the amount of nodes in the graph and returns the edges corresponding to the MST of the graph
def kruskal(edgeList, nodesAmount):
    edgeList = sorted(edgeList, key = lambda edge: edge[2])
    ufds = UFDS(nodesAmount)
    mst = 0
    for edge in edgeList:
        if not ufds.is_same_set((edge[0] - 1), (edge[1] - 1)):
            ufds.union((edge[0] - 1), (edge[1] - 1))
            mst+=edge[2]
    return mst

tc = int(input())
for t in range(tc):
    price = int(input())
    nNodes = int(input())
    nEdges = int(input())
    edgeList = []
    for i in range(nEdges):
        edgeList.append(list(map(int,input().split(' '))))
    print(kruskal(edgeList,nNodes)*price)
    