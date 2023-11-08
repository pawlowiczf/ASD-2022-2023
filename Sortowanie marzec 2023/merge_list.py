# Merge k posortowanych tablic 

def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2 
def left(i): return 2 * i + 1

def heapify(T, i, n):
    min_ind = i 
    l = left(i)
    r = right(i)
    #
    if l < n and T[l].val < T[min_ind].val: min_ind = l
    if r < n and T[r].val < T[min_ind].val: min_ind = r
    #
    if min_ind != i:
        T[i], T[min_ind] = T[min_ind], T[i]
        return heapify(T, min_ind, n)
#end def ^^^


def buildheap(T):
    n = len(T)
    for i in range( parent(n-1), -1, -1):
        heapify(T, i, n)
    #end for
#end def ^^^


class Node:
    def __init__(self, val, index, list_num, ):
        self.val = val
        self.index = index
        self.list_num = list_num
    #
#end Class


def extractMin(L, heap):
    minValue = heap[0].val
    minNode = heap[0]
    #
    if minNode.index + 1 < len( L[ minNode.list_num ] ):
        minNode.val = L[ minNode.list_num ][ minNode.index + 1 ]
        minNode.index += 1
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop()
    #
    heapify( heap, 0, len(heap) )
    #
    return minValue
#end def ^^^


def merge(L):
    #
    heap = []
    result = []
    #
    for i in range( len(L) ):
        heap.append( Node( L[i][0], 0, i ) )
    #
    buildheap(heap)

    while heap:
        #
        minValue = extractMin(L, heap)
        result.append( minValue )
    #end while

    return result
#end def ^^^


T = [ [10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33], [1,5,15,18,19,19,25,100,1000] ]
P = merge(T)
print(P)





