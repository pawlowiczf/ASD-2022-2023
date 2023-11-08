# Sort a k-sorted array
# Given a k–sorted array that is almost sorted such that each of the n elements may be misplaced by no more than k positions from the correct sorted order. 
# Find a space-and-time efficient algorithm to sort the array.


"""
We can solve this problem in O(n.log(k)) using a min-heap. 
The idea is to construct a min-heap of size k+1 and insert the first k+1 elements into the heap. 
Then remove minimum from the heap and insert the next element from the array into the heap and continue the process till both array and heap are exhausted. 
Each pop operation from the heap should insert the corresponding top element in its correct position into the array.
"""

def right(i): return 2 * i + 2
def left(i): return 2 * i + 1
def parent(i): return ( i - 1 ) // 2
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
        T[min_ind], T[i] = T[i], T[min_ind]
        heapify(T, min_ind, n)
#end def ^^^


def buildheap(T):
    n = len(T)
    for i in range( parent(n-1), -1, -1):
        heapify(T,i,n)
#end def ^^^

def extractMin(heap):
    min_value = heap[0]
    #
    heap[0], heap[-1] = heap[-1], heap[0]
    heap.pop( -1 )
    heapify( heap, 0, len(heap) )
    #
    return min_value
#end def ^^^

def insert(heap, value):
    heap.append( value )
    i = len( heap ) - 1
    #
    while i > 0 and heap[ parent(i) ] > heap[ i ]:
        heap[ parent(i) ], heap[ i ] = heap[ i ], heap[ parent(i) ]
        i = parent(i)
    #end while

#end def ^^^


def sort(T,k):
    #
    heap = [ T[i] for i in range( k + 1 ) ]
    buildheap( heap )
    index = 0
    n = len(T)
    #
    for i in range( k+1, len(T) ):
        T[index] = extractMin( heap )
        insert( heap, T[i] )
        index += 1
    #end for

    while heap:
        T[index] = extractMin(heap)
        index += 1
    #end while

#end def 

T = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9,11,14,13]
sort(T, 2)
print(T)
