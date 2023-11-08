# Tablica k-chaotyczna. Posortuj


def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2
def left(i): return 2 * i + 1


def heapify(heap, i, n):
    min_ind = i 
    l = left(i)
    r = right(i)
    #
    if l < n and heap[l] < heap[min_ind]: min_ind = l
    if r < n and heap[r] < heap[min_ind]: min_ind = r

    if min_ind != i:
        heap[min_ind], heap[i] = heap[i], heap[min_ind]
        heapify(heap, min_ind, n)
    #
#end def ^^^

def buildheap(T):
    n = len(T)
    #
    for i in range( parent(n-1), -1, -1 ):
        heapify(T, i, n)
    #
#end def ^^^

def insert(T, heap, pom):
    n = len(T)

    if pom < n:
        heap.append( T[pom] )
        heap[-1], heap[0] = heap[0], heap[-1]
        heap.pop(-1)
    else:
        heap[-1], heap[0] = heap[0], heap[-1]
        heap.pop(-1)
    #
    heapify(heap, 0, len(heap) )
    pom += 1
    #
    return heap, pom
#end def ^^^



def Sort(T,k):
    n = len(T)
    heap = []
    result = []
    #
    for i in range(k+1):
        heap.append( T[i] )
    #
    buildheap(heap)
    pom = k + 1
    #
    while heap:
        #
        minValue = heap[0]
        result.append( minValue )
        heap, pom = insert(T, heap, pom)
    #end while

    return result
#end def ^^^


# T = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9,11,14,13]
# k = 2

T = [ 1,0,3,2,4,6,5 ]
T = Sort(T, 4)
print(T)



