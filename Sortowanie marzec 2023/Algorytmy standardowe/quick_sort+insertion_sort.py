from random import randint
import time

def insertion_sort(T, left, right):
    #
    for i in range( left + 1 , right + 1 ):
        j = i
        #
        while j > 0 and T[ j ] < T[ j - 1 ]:
            T[ j ], T[ j - 1 ] = T[ j - 1 ], T[ j ]
            j -= 1  
    #end for
#end def


def partition(T, left, right):
    q = left - 1
    for i in range(left, right):
        if T[i] <= T[right]:
            q += 1 
            T[i], T[q] = T[q], T[i]
    T[right], T[q+1] = T[q+1], T[right]
    return q + 1
#end def 


def quick_sort(T, left, right):
    #
    if right - left < 9:
        insertion_sort(T, left, right)
    #
    else:
        pivot = partition(T, left, right)
        quick_sort(T, left, pivot - 1)
        quick_sort(T, pivot + 1, right)
#end def


T = [randint(0,1000000) for i in range(1000000)]
t1 = time.time()
quick_sort(T, 0, len(T) - 1)
t2 = time.time()

print(t2-t1)


