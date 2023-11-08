from kol1testy import runtests
from random import randint
from copy import deepcopy


def partition(T, p, r):
    rand = randint(p, r)
    T[rand], T[r] = T[r], T[rand]
    i = p - 1
    for j in range(p, r):
        if T[j] <= T[r]:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1


def select2(A,k, left, right):
    if right >= left:
        pivot = partition(A, left, right)
        if k == pivot: return A[k]
        elif k < pivot: return select(A, k, left, pivot - 1)
        else: return select(A,k, pivot + 1, right)
    #
#end def ^^^

def select(T, p, r, k):
    
    while r >= p:
        q = partition(T, p, r)
        if q == k: return T[k]
        elif k > q: p = q + 1
        else: r = q - 1
    #
#end def ^^^
    



def ksum(T, k, p):
    n = len(T)
    sum_z = 0
    for i in range(0, n - p + 1):
        T_copy = T[i:i+p]
        size = len(T_copy)
        w = select(T_copy, 0, size - 1, size - k,)
        sum_z += w
    return sum_z



runtests( ksum, all_tests=True)