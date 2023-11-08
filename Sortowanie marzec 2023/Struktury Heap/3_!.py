# Merge `M` sorted lists of variable length
# Given M sorted lists of variable length, merge them efficiently in sorted order.
# https://www.techiedelight.com/merge-m-sorted-lists-variable-length/


'''
Input:  4 sorted lists of variable length
 
[10, 20, 30, 40]
[15, 25, 35]
[27, 29, 37, 48, 93]
[32, 33]
 
Output:
 
[10, 15, 20, 25, 27, 29, 30, 32, 33, 35, 37, 40, 48, 93]

'''
#
'''
We can easily solve this problem in O(N.log(M)) time by using a min-heap. 
The idea is to construct a min-heap of size M and insert the first element of each list into it. 
Then pop the root element (minimum element) from the heap and insert the next element from the “same” list as the popped element.
'''

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1) // 2
#

class Node:
    def __init__(self, value, list_num, index):
        self.value = value
        self.list_num = list_num
        self.index = index
#end Class


def insert(heap, key):
    heap.append( key )
    i = len( heap ) - 1
    
    while i > 0 and heap[ parent(i) ].value > heap[ i ].value:
        heap[ parent(i) ], heap[i] = heap[i], heap[ parent(i) ]
        i = parent(i)
#end def ^^^


def extractMin(L, heap):
    min_value = heap[0].value
    min = heap[0]
    print( min_value, end = " " )
    #
    if min.index + 1 < len( L[ min.list_num ] ):
        min.index = min.index + 1
        min.value = L[ min.list_num ][ min.index ]
        heapify(heap, 0, len(heap) )
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop( -1 )
        heapify(heap, 0, len(heap) )
    #
#end def 


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


def merge(L):
    heap = [ Node( L[i][0], i, 0 ) for i in range( len(L) ) if len( L[i] ) >= 1 ]
    buildheap(heap)

    while heap:
        extractMin(L, heap)

#end def ^^^

list = [ [10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33], [1,5,15,18,19,19,25,100,1000] ]
merge( list )
