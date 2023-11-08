"""
Filip Pawlowicz 414324

Sortuje tablice wejsciowa, aby wykorzystac algorytm Binsearch. Jesli w tablicy znajduje sie element T[i][::-1] to zamieniam T[i] na T[i][::-1].
W ten sposob bede miec w tablicy tylko jedna forme slowa. Nastepnie ponownie sortuje tablice i iteruje po niej liniowo, aby znalezc element, ktory pojawil
sie najczesciej. Zwracam te ilosc. Do sortowania uzywam algorytmu Merge Sort.

"""


from zad3testy import runtests



def binsearch(tab, value):
    #
    _start = 0
    _end = len( tab ) - 1
    #

    while _start <= _end:
        middle = ( _start + _end ) // 2
        if value == tab[middle]: return middle
        if value > tab[ middle ]: _start = middle + 1
        else: _end = middle - 1
    #end while

    return False
#end def ^^^


def merge(T1, T2):
    p_1 = p_2 = 0
    n_1, n_2 = len(T1), len(T2)
    T = [0] * ( n_1 + n_2 )
    #
    while p_1 < n_1 and p_2 < n_2:
        if T1[ p_1 ] < T2[ p_2 ]:
            T[ p_1 + p_2 ] = T1[ p_1 ]
            p_1 += 1
        else:
            T[ p_1 + p_2 ] = T2[ p_2 ]
            p_2 += 1 
    #end while

    while p_1 < n_1:
        T[ p_1 + p_2 ] = T1[ p_1 ]
        p_1 += 1  
    #
    while p_2 < n_2:
        T[ p_1 + p_2 ] = T2[ p_2 ] 
        p_2 += 1 
    #
    return T
#end def ^^^


def mergeSort(T):
    #
    if len(T) >= 2:
        mid = ( len(T) ) // 2
        T1 = T[ 0 : mid ]
        T2 = T[ mid : len(T) ]
        #
        T1 = mergeSort(T1)
        T2 = mergeSort(T2)
        T = merge(T1,T2)
    #end if
    return T
#end def ^^^


def strong_string(T):
    n = len(T)
    #
    T = mergeSort(T)
    #
    for i in range( n ):
        x = binsearch(T, T[i][::-1] )
        if x:
            T[i] = T[i][::-1]
    #

    T = mergeSort(T)
    curr_number = 1
    max_number = 1

    for i in range( 1, n ):
        if T[i-1] == T[i]:
            curr_number += 1
            max_number = max( max_number, curr_number )
        else:
            curr_number = 1
    #end for
    
    return max_number
#end def ^^^


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
