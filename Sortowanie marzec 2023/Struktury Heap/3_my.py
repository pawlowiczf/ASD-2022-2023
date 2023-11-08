# Merge k-sorted arrays with integers in one. 

class Node():
    def __init__(self, value, index, list_num):
        self.value = value
        self.index = index
        self.list_num = list_num
#end Class


def right(i): return 2 * i + 2 
def left(i): return 2 * i + 1
def parent(i): return ( i - 1 ) // 2
#
def heapify( heap, i, n ):
    min_ind = i
    r = right(i)
    l = left(i)

    #
    if r < n and heap[ r ].value < heap[ min_ind ].value: min_ind = r
    if l < n and heap[ l ].value < heap[ min_ind ].value: min_ind = l
    #
    if min_ind != i:
        heap[ min_ind ], heap[ i ] = heap[ i ], heap[ min_ind ]
        heapify(heap, min_ind, n)
#end def ^^^

def extractMin(L, heap):
    min_value = heap[0].value
    index = heap[0].index
    list_num = heap[0].list_num
    #
    if index + 1 < len( L[list_num] ):
        heap[0].value = L[list_num][index+1]
        heap[0].index += 1 
    else:
        heap[0], heap[-1] = heap[-1], heap[0]
        heap.pop( -1 )
    #
    heapify( heap, 0, len(heap) )
    return min_value 
#end def ^^^

def buildheap(L):
    n = len(L)
    for i in range( parent(n-1), -1, -1):
        heapify(L, i , n)
#end def ^^^

def merge(L):
    heap = [ Node( L[i][0], 0, i ) for i in range( len(L) ) ]
    buildheap( heap )
    new_list = []

    while heap:
        min_value = extractMin(L, heap)
        new_list.append( min_value )
    #
    return new_list
#end def ^^^

T = [ [10, 20, 30, 40],
[15, 25, 35],
[27, 29, 37, 48, 93],
[32, 33,33,100]
]

new_list = merge(T)
print(new_list)