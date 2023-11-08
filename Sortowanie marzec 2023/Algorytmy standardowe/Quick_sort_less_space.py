def partition(T, left, right):
    i = left - 1
    q = T[ right ] 
    for j in range(left, right):
        if T[j] < q:
            i += 1
            T[j], T[i] = T[i], T[j]
    #end for
    T[i+1], T[right] = T[right], T[i+1]
    #
    return i + 1
#end def ^^^

def quick_sort_optimized(T, left, right):
    while left < right:
        #
        pivot = partition(T, left, right)
        #
        if ( pivot - left ) < ( right - pivot ):
            quick_sort_optimized(T, left, pivot - 1)
            left = pivot + 1
        
        else:
            quick_sort_optimized(T, pivot + 1, right)
            right = pivot - 1
    #end while

#end def ^^^


T = [-16,5,-10,4,100,10000000016,734,-10,17,-100,600,1000000]
quick_sort_optimized(T, 0 , len(T) - 1)
print(T)

