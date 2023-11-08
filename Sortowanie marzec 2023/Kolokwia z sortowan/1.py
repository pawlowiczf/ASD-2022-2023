# Znajdz wspolczynnik nieuporzadkowania k tablicy k-chaotycznej
# (sortowanie musi byc stabilne)

def join_two_arrays(T1, T2):
    #
    p_1 = 0
    p_2 = 0
    n_1, n_2 = len(T1), len(T2)
    T = [0] * ( n_1 + n_2 )
    pom = 0
    #
    while p_1 < n_1 and p_2 < n_2:
        if T1[ p_1 ] < T2[ p_2 ]:
            T[ pom ] = T1[ p_1 ]
            p_1 += 1
        else:
            T[ pom ] = T2[ p_2 ]
            p_2 += 1
        #
        pom += 1
    #end while

    #
    while p_2 < n_2:
        T[ pom ] = T2[ p_2 ]
        p_2 += 1
        pom += 1
    #
    while p_1 < n_1:
        T[ pom ] = T1[ p_1 ]
        p_1 += 1
        pom += 1
    #
    return T
#end def ^^^


def MergeSort(T):
    if len(T) >= 2:
        mid = ( len(T) ) // 2
        T1 = T[ 0 : mid ]
        T2 = T[ mid : len(T)]
        T1 = MergeSort(T1)
        T2 = MergeSort(T2)
        T = join_two_arrays(T1, T2)
    return T
#end def ^^^

    
def chaosIndex(T):
    n = len(T)
    #
    for i in range(n):
        T[i] = ( T[i], i )
    #
    T = MergeSort(T)
    #
    max_k = 0
    for i in range( n ):
        max_k = max( max_k, abs( i - T[i][1] ) )
    #
    return max_k
#end def ^^^

T = [0, 2, 1.1, 2]
print( chaosIndex(T) )

    