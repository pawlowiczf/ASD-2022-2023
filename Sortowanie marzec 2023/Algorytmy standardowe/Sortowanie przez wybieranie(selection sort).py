import time
# Sortowanie przez proste wybieranie
# Szukamy minimum w tablicy i zamieniamy z kolejnym elementem tablicy 
# Jest niestabilne, ale mozemy zrobic je stabilnym, gdy zamiast zamienic dwa elementy, bedziemy elementy tablicy przesuwac o 1w prawo

# Jeśli chcemy posortować zbiór malejąco, to zamiast elementu minimalnego poszukujemy elementu maksymalnego

def selection_sort( T ):
    n = len( T )
    
    for i in range(0, n - 1 ):
        minimum = i

        for j in range(i+1, n):
            if T[j] < T[ minimum ]:
                minimum = j 
        #end for 2
        T[i], T[minimum] = T[minimum], T[i]
        
        
    #end for 1
    return T
#end def


def stableSelectionSort(T):
    n = len(T)

    for i in range( n ):
        minimum = i 

        for j in range(i+1, n):
            if T[minimum] > T[j]:
                minimum = j 
        #end for 
        key = T[minimum]

        while minimum > i:
            T[minimum] = T[minimum - 1]
            minimum -= 1
        #end while 
        T[i] = key 
    #end for
    return T
#end def


T = [3,4,9,14,18,25,7,3,1,2,4,-1]
print( selection_sort(T) )

T = [3,4,9,14,18,25,7,3,1,2,4,-1]
print( stableSelectionSort(T) )