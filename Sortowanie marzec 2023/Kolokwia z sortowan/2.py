"""
Mamy n zolnierzy roznego wzrostu i nieuporzadkowana tablice, w ktorej
podano wzrosty zolnierzy. Zolnierze zostana ustawieni na placu w szeregu malejaco wzgledem wzrostu.
Funkcja, ktora zwroci tablice ze wzrostami zolnierzy na pozycjach od p do q wlacznie

"""

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
        if k == pivot: return True
        elif k < pivot: return select(A, k, left, pivot - 1)
        else: return select(A,k, pivot + 1, right)
    #
#end def

def guardians(T, p, q):
    select(T, p, 0, len(T) - 1)
    select(T, q, p, len(T) - 1)
    heights = T[ p : q+1 ]
    return heights
#end def


T = [144,156,121,95,329,144,348294,192,65,49,79,69,213,731]
heights = guardians(T, 4, 9)
print(heights)

T = [144,156,121,95,329,144,348294,192,65,49,79,69,213,731]
T.sort()
print(T)