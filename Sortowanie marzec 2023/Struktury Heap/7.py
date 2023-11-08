# Replace each array element by its corresponding rank
# Given an array of distinct integers, replace each array element by its corresponding rank in the array
# The minimum array element has the rank 1; the second minimum element has a rank of 2, and so on… For example:

"""
Input:  { 10, 8, 15, 12, 6, 20, 1 }
 
Output: { 4, 3, 6, 5, 2, 7, 1 }
"""

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
#end Class


def right(i): return 2 * i + 2
def left(i): return 2 * i + 1
def parent(i): return ( i - 1 ) // 2
#

def heapify(T, i, n):
    min_ind = i
    l = left(i)
    r = right(i)
    #
    if l < n and T[l].value < T[min_ind].value: min_ind = l
    if r < n and T[r].value < T[min_ind].value: min_ind = r
    #
    if min_ind != i:
        T[min_ind], T[i] = T[i], T[min_ind]
        heapify(T, min_ind, n)
#end def ^^^

def buildheap(T):
    n = len(T)
    for i in range( parent(n-1), -1, -1):
        heapify(T,i,n)
#end def ^^^

def extractMin(T, heap):
    value = heap[0].value
    index = heap[0].index
    #
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop( -1 )
    heapify( heap, 0, len(heap) )
    return index
#end def ^^^
    

def rank(T):
    heap = [ Node(T[i], i) for i in range( len(T) ) ]
    buildheap( heap )
    pom = 1

    while heap:
        index = extractMin(T, heap)
        T[ index ] = pom
        pom += 1 
    #end while

#end def ^^^


T = [10,8,15,12,6,20,1]
rank(T)
print(T)