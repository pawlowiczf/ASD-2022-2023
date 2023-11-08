# select (A, k) - k-ta statystyka pozycyjna, czyli element A, ktory bylby na k-ej pozycji po posortowaniu
# select(A,0) = min(A), select(A, len(A) - 1) = max(A)
# select (A, len(A) / 2) = mediana(A)

from random import randint

def partition(T, left, right):
    i = left - 1
    #
    for j in range(left, right):
        if T[j] < T[right]:
            i += 1
            T[j], T[i] = T[i], T[j]
        #
    #end for
    T[i+1], T[right] = T[right], T[i+1]
    return i + 1
#end def 


def random_pivot(T, left, right):
    k = randint(left, right)
    T[k], T[right] = T[right], T[k]
    return partition(T, left, right)
#end def


def select(A,k, left, right):
    if right >= left:
        pivot = random_pivot(A, left, right)
        if k == pivot: return A[k]
        elif k < pivot: return select(A, k, left, pivot - 1)
        else: return select(A,k, pivot + 1, right)
    #
#end def

T = [6,-9,14,16,-89,1,0,7]

T.sort()
print( T )

T = [6,-9,14,16,-89,1,0,7]
print( select(T, 4, 0, len(T) - 1) )


    