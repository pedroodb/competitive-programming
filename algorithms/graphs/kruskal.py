from ufds import UFDS

#Expects an edgeList as a list of (origin,destiny,weigth) and the amount of nodes in the graph
def kruskal(edgeList, nodesAmount):
    edgeList = sorted(edgeList, key = lambda edge: edge[2])
    ufds = UFDS(nodesAmount)
    mst = []
    for edge in edgeList:
        if not ufds.is_same_set((edge[0] - 1), (edge[1] - 1)):
            ufds.union((edge[0] - 1), (edge[1] - 1))
            mst.append(edge)
    return mst