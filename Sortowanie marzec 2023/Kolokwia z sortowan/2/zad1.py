from zad1testy import Node, runtests

class Node2:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
#end def ^^^

def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2
def left(i): return 2 * i + 1
#

def heapify(heap, i, n):
    min_ind = i
    l = left(i)
    r = right(i)
    #
    if l < n and heap[l].val < heap[min_ind].val: min_ind = l
    if r < n and heap[r].val < heap[min_ind].val: min_ind = r
    #
    if min_ind != i:
        heap[min_ind], heap[i] = heap[i], heap[min_ind]
        heapify(heap, min_ind, n)
    #
#end def ^^^

def buildheap(heap):
    n = len(heap)
    for i in range( parent(n-1), -1, -1):
        heapify(heap, i, n)
#end def ^^^


def extractMin(heap, q):
    minNode = heap[0]

    if q is not None:
        heap[0] = q 
        q = q.next
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop( -1 )
    #
    heapify( heap, 0, len(heap) )
    return minNode, q
#end def ^^^

def SortH(p,k):
    q = p
    heap = []
    #
    
    newPointer = Node2(None)
    newPointerGuard = newPointer
    #
    for i in range( k + 1 ):
        pointer = q
        q = q.next
        pointer.next = None
        heap.append( pointer )

        if q is None:
            break
    #end for 
    
    buildheap(heap)
    #
    while heap:
        minNode, q = extractMin(heap, q)
        minNode.next = None
        #
        newPointer.next = minNode
        newPointer = newPointer.next
    #end while

    return newPointerGuard.next
#end def ^^^


#
runtests( SortH ) 
