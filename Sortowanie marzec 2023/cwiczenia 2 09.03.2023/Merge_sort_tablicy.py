from random import randint
import time
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


def merge_sort(T):
    if len(T) >= 2:
        mid = ( len(T) ) // 2
        T1 = T[ 0 : mid ]
        T2 = T[ mid : len(T)]
        T1 = merge_sort(T1)
        T2 = merge_sort(T2)
        T = join_two_arrays(T1, T2)
    return T
#end def ^^^





T = [-10,6,16,90,-100,15,8,0,-3,4,3,18,20,-600,2137,6,-1000,1500,-100]
T = [ randint(0,2000) for i in range(100) ]

T = merge_sort(T)
print(T)







