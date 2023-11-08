# Find k’th smallest element in an array
# Kopiec min

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


def extractMin(T):
    T[0], T[-1] = T[-1], T[0]
    T.pop( -1 )
    heapify( T, 0, len(T) )
#end def ^^^


def extractKth(T, k):
    buildheap(T)

    for i in range( k - 1 ):
        extractMin(T)
    #
    return T[0]
#end def ^^^


T = [7,4,6,3,9,1]
print( extractKth(T, 3) )

T = [7,4,6,3,9,1]
T.sort()
print(T)