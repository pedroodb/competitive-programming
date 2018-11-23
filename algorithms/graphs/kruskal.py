from ufds import UFDS
import heapq
from functools import reduce

#Expects an edgeList as a list of (origin, destiny, weigth) and the amount of nodes in the graph and returns the edges corresponding to the MST of the graph
def kruskal(edgeList, nodesAmount):
    edgeList = sorted(edgeList, key = lambda edge: edge[2])
    ufds = UFDS(nodesAmount)
    mst = []
    for edge in edgeList:
        if not ufds.is_same_set((edge[0] - 1), (edge[1] - 1)):
            ufds.union((edge[0] - 1), (edge[1] - 1))
            mst.append(edge)
    return mst

#The first n MSTs
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