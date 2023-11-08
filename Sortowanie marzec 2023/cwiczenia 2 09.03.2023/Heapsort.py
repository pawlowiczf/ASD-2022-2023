def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return ( i - 1 ) // 2

def heapify(A, i, n):

    l = left(i)
    r = right(i)
    max_ind = i

    if l < n and A[ l ] > A[ max_ind ]: max_ind = l
    if r < n and A[ r ] > A[ max_ind ]: max_ind = r 

    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)

#end def ^^^

def buildheap(A):
    n = len(A)

    for i in range( parent( n - 1 ), -1, -1):
        heapify(A, i, n)

#end def ^^^

def heapsort(A):
    #
    buildheap(A)
    #
    n = len(A)
    for i in range( n - 1, 0, -1 ):
        A[ 0 ], A[ i ] = A[ i ], A[ 0 ]
        heapify(A, 0, i)

#end def ^^^


# T = [-10,6,16,90,-100,15,8,0,-3,4,3,18,20,-600,2137,6,-1000,100]
# heapsort(T)
# print(T)

A = [4,1,3,2,16,9,10,14,8,7]
buildheap(A)