from zad1testy import runtests

def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2
def left(i): return 2 * i + 1
#

def Heapify(T, i, n):
    minInd = i
    l = left(i)
    r = right(i)
    #
    if l < n and T[l] < T[minInd]: minInd = l
    if r < n and T[r] < T[minInd]: minInd = r
    #
    if minInd != i:
        T[i], T[minInd] = T[minInd], T[i]
        Heapify(T, minInd, n)
#end def ^^^

def buildHeap(T):
    n = len(T)

    for i in range( parent(n-1), -1, -1):
        Heapify(T, i, n)

#end def ^^^

def chaos_index( T ):
    #
    Heap = []
    return None


runtests( chaos_index )
