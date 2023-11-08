def partition(T, left, right):
    i = left - 1

    for j in range( left, right ):
        if T[ j ] < T [ right ]:
            i += 1
            T[j], T[i] = T[i], T[j]
        #
    #end for 
    T[ i + 1 ], T[ right ] = T[ right ], T[ i + 1] 
    return i + 1
#end def ^^^

def quickSort(T, left, right):
    
    while left < right:
        pivot = partition(T, left, right)
        #
        if ( pivot - left ) > ( right - pivot ) :
            quickSort(T, pivot + 1, right)
            right = pivot - 1
        else:
            quickSort(T, left, pivot - 1)
            left = pivot + 1
    #end while
#end def ^^^