# Check if a binary tree is a min-heap or not


def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2
def left(i): return 2 * i + 1


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


def check(T, i, n):
    min_ind = i
    l = left(i)
    r = right(i)
    #
    
    if l < n and T[l] < T[i]: return False 
    if r < n and T[r] < T[i]: return False 
    if r > n or l > n: return True 

    return check(T, l, n) and check(T, r, n)
#end def 

T = [-10,16,5,9,3,-40,36,-40,6,-2,-1,-100,4,96,9,18,24,23]
print( check(T, 0, len(T) ) )

T = [-10,16,5,9,3,-40,36,-40,6,-2,-1,-100,4,96,9,18,24,23]
buildheap(T)
print( check(T, 0, len(T) ) )