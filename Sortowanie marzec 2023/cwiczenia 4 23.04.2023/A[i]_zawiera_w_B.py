# len(A) = n
# len(B) = log(n)
# dla kazdego i: A[i] zawiera sie w B
# Znajdz tablice B
# O( n*loglogn )


def binarySearch(T, key):
    if not T: return -1
    #
    _start = 0
    _end = len(T) - 1
    #
    while _start <= _end:
        mid = ( _start + _end ) // 2
        if T[mid] == key: return mid
        elif T[mid] > key: _end = mid - 1
        else: _start = mid + 1
    #end while

    return False
#end def ^^^


# Wstawiasz na koniec i while dopoki nie bedzie w dobrym miejscu 
def insert(T, value):
    pass 


def findValues(T): # O( nloglogn )
    B = []
    for value in T:
        check = binarySearch(B, value)
        #
        if not check:
            insert(B, value)
    #end for
    return B
#end def ^^^

def countingSort(A):
    B = findValues(A)
    C = [ 0 for _ in range( len(B) ) ]
    #

    for i in range( len(A) ):
        idx = binarySearch(B, A[i] )
        C[ idx ] += 1
    #
    for i in range( 1, len(C) ):
        C[ i ] += C[ i - 1 ]
    #
    res = [0 for _ in range(A) ]
    for i in range( len(A) - 1, -1, -1):
        idx = binarySearch(B, i)
        res[ C[idx] - 1 ] = A[i]
        C[ idx ] -= 1 
    #
    # return res ???
#end def ^^^   
    






