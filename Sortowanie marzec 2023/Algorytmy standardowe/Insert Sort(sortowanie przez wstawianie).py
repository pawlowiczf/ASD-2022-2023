import time
# Jest stabilne. Jest lepsze od sortowania przez wybieranie dla tablic czesciowo uporzadkowanych, z mala liczba inwersji.


# Bez wartownika

def insert_sort( T ):
    n = len( T )

    for k in range(1, n):
        m = k-1 

        while T[m+1] < T[m] and m >= 0:
            T[m+1], T[m] = T[m], T[m+1]
            m = m - 1
        #end while
    #end for
    return T
#end def


def insertion_sort_my(T):
    
    n = len(T)
    for i in range(1, n):
        j = i
        while T[j] < T[j-1] and j > 0:
            T[j], T[j-1] = T[j-1], T[j]
            j -= 1
        #end while
    #end for
    return T
#end def

def partial_insertion_sort(T): # wyszukuje polowkowo, zmniejsza sie tylko liczba porownan, ale nie przestawien
    n = len(T)
    
    for i in range(1, n):
        
        l = 0
        p = i - 1
        while l <= p:
            middle = (l + p) // 2
            if T[middle] < T[i]: l = middle + 1
            else: p = middle - 1 
        
        #end while
        key = T[i]
        for k in range(i,l,-1):
            T[k], T[k-1] = T[k-1], T[k]
        T[l] = key
        
    #end for
    return T
#end def


# T = [0,3,2,7,9,11,14,3,3,6]
# print( insert_sort(T) )

T = [0,3,2,7,9,11,14,3,3,6]
print( insertion_sort_my(T) )

# T = [0,3,2,7,9,11,14,3,3,6]
# print( partial_insertion_sort(T) )


