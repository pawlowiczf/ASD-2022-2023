# Dana jest tablica T[n]. Ile jest inwersji, tzn. sytuacji, gdy i < j oraz T[i] > T[j] 
# Nie dziala
global cp
cp = 0

from random import randint

def join_two_arrays(T1, T2):
    global cp
    #
    p_1 = 0
    p_2 = 0
    n_1, n_2 = len(T1), len(T2)
    T = [0] * ( n_1 + n_2 )
    pom = 0
    cnt = 0
    #
    while p_1 < n_1 and p_2 < n_2:
        if T1[ p_1 ] > T2[ p_2 ]:
            T[ pom ] = T1[ p_1 ]
            p_1 += 1
            cnt += n_2 - p_2 
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
 
    while p_1 < n_1:
        T[ pom ] = T1[ p_1 ]
        p_1 += 1
        pom += 1
    #
    cp += cnt
    return T
#end def ^^^


def merge_sort(T):
    global cp
    # cnt = 0
    if len(T) >= 2:
        mid = ( len(T) ) // 2
        T1 = T[ 0 : mid ]
        T2 = T[ mid : len(T)]
        T1 = merge_sort(T1)
        T2 = merge_sort(T2)
        T = join_two_arrays(T1, T2)
    #
    return T
#end def ^^^





T = [8,4,2,1] # 6
T = merge_sort( T )
print(cp)

cp = 0

T = [ 1, 20, 6, 4, 5 ] # 5
T = merge_sort( T ) 
print(cp)


