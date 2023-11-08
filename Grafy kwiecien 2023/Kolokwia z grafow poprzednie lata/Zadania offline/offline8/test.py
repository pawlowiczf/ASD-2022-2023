from zad8testy import runtests
from math import sqrt
from math import ceil


class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self



def findset(x):
    if x != x.parent:
        x.parent = findset(x.parent)
    return x.parent

def union(x, y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1




def kruskal_algorithm(A,Edges, i):
    n = len(A)
    MST = []
    node = [Node(u) for u in range(n)]
    for edge in Edges[i:len(Edges)]:
        u, v = node[edge[0]], node[edge[1]]
        if findset(u) != findset(v):
            MST.append(edge[2])
            union(u, v)
        if len( MST ) == n - 1: return MST
    return MST

def weight(A,i,j):
    y1, x1 = A[i]
    y2, x2 = A[j]
    weight = ceil( sqrt( (y2 - y1 ) ** 2 + (x2 - x1) ** 2 ) )
    return weight

def build_graph(A):
    Edges = []
    n = len(A)
    for i in range(n-1):
        for j in range(i+1,n):
            Edges.append((i,j,weight(A,i,j)))
    return Edges


def highway( A ):
    Edges = build_graph(A)
    Edges.sort(key = lambda x: x[2])
    n = len(A)

    
    minDifference = float('inf')

    for i in range( len(Edges) ):
        MST = kruskal_algorithm(A, Edges, i)
        length = len( MST )
        if length != n - 1: break
        minDifference = min( MST[ n - 2 ] - Edges[i][2], minDifference )

    return minDifference

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )