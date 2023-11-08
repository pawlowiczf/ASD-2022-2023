# Return k’th largest element in a stream
# Given an infinite stream of integers, return the element representing the k'th largest element in the stream.
# https://www.techiedelight.com/find-kth-largest-element-array/

# Pewnie da sie prosciej

# Using Min-heap

def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2
def left(i): return 2 * i + 1
#
def heapify(T, i, n):
    min_ind = i
    l = left(i)
    r = right(i)
    #
    if l < n and T[l] < T[min_ind]: min_ind = l
    if r < n and T[r] < T[min_ind]: min_ind = r
    #
    if min_ind != i:
        T[i], T[min_ind] = T[min_ind], T[i]
        heapify(T, min_ind, n)
#end def ^^^

def buildheap(T):
    n = len(T)
    for i in range( parent(n-1), -1, -1):
        heapify(T, i, n)
    #end def


#end def ^^^
def find(T, k):
    n = len(T)
    heap = []
    #
    if len(T) < k:
        return -1
    #
    for i in range( k ):
        heap.append( T[i] )
    #
    buildheap( heap )
    #end for
    for i in range(k, n):
        if heap[0] < T[i]:
            heap[0] = T[i]
            heapify(heap, 0, len(heap) )
    #end for 
    return heap[0]
#end def ^^^


# T = [16,5,4,9,3,-10,20]
# T.sort()
# print( T )

# T = [16,5,4,9,3,-10,20]
# print( find(T, 7) )


# Using Max - heap
# Dodaj wszystkie elementy do kopca Max, pozniej usun (k-1) pierwszych z wierzchu i k-ty najwiekszy bedzie pod heap[0]

def heapify2(T, i, n):
    max_ind = i
    l = left(i)
    r = right(i)
    #
    if l < n and T[l] > T[max_ind]: max_ind = l
    if r < n and T[r] > T[max_ind]: max_ind = r
    #
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, max_ind, n)
#end def ^^^

    

def find_max_heap(T,k):
    heap = []
    n = len(T)
    #
    for i in range( len(T) ):
        heap.append( T[i] )
    #
    buildheap(T)
    #
    for i in range( k - 1 ):
        heap[0], heap[n-1] = heap[n-1], heap[0]
        heapify(T, 0, n - 1)
    #end for
    return heap[0]
#end for 


T = [16,5,4,9,3,-10,20]
# T.sort()
# print( T )

# T = [16,5,4,9,3,-10,20]
# print( find(T, 1) )
buildheap(T)
print(T)