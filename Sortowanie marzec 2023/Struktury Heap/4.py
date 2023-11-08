# Find the smallest range with at least one element from each of the given lists
# Given M sorted lists of variable length, efficiently compute the smallest range, including at least one element from each list.

"""
Input:  4 sorted lists of variable length
 
[ 3, 6, 8, 10, 15 ]
[ 1, 5, 12 ]
[ 4, 8, 15, 16 ]
[ 2, 6 ]
 
Output:

The minimum range is 4–6
"""

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1) // 2

def heapify(T,i,n):
    l = left(i)
    r = right(i)

    max_ind = i
    if l < n and T[ l ].value < T[ max_ind ].value: max_ind = l
    if r < n and T[ r ].value < T[ max_ind ].value : max_ind = r 

    if max_ind != i:
        T[i], T[ max_ind ] = T[ max_ind ], T[i]
        heapify(T, max_ind, n)
#end def ^^^

def buildheap(T):
    n = len(T)
    for i in range( parent( n - 1 ), -1, -1):
        heapify(T, i, n)
#end def ^^^


class Node():
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index
#end Class

def extractMin(L, heap):
    min_value = heap[0].value
    index = heap[0].index
    list_num = heap[0].list_num
    #
    min = heap[0]
    

    if min.index + 1 < len( L[ min.list_num] ):
        min.index += 1 
        min.value = L[ min.list_num ][ min.index ]
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop( -1 )
    #
    heapify(heap, 0, len(heap) - 1)
    
    return min_value , index, list_num
#end def ^^^


def find_range(L):
    heap = []
    high = -float('inf')
    #
    for i in range( len(L) ):
        heap.append( Node( L[i][0], i, 0) )
        high = max( high, L[i][0] )
    #
    buildheap( heap )
    #
    p = ( 0, float('inf') ) # minimum and maximum elements found so far in a heap
    #
    while True:
        min_value, index, list_num = extractMin(L, heap)
        #
        if high - min_value < p[1] - p[0]:
            p = (min_value, high)
        #
        if index == len( L[ list_num ] ) - 1:
            return p
        #
        high = max( high, L[ list_num ][ index + 1 ] )

#end def ^^^

L = [ [3,6,8,10,15], [1,5,12], [4,8,15,16], [2,6] ]
print( find_range(L) )

L = [ [2,3,4,8,10,15], [1,5,12], [7,8,15,16], [3,6] ]
print( find_range(L) )
