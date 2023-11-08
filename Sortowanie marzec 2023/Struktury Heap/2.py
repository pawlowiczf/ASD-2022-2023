# Convert min heap to max heap in linear time
# Wystarczy zbudowac kopiec max, tak jakby z nieposortowanej tablicy.
# Nie ma znaczenia, czy jest to juz kopiec min 
# https://www.techiedelight.com/convert-min-heap-to-max-heap-linear-time/


def parent(i): return (i-1) // 2
def right(i): return 2 * i + 2
def left(i): return 2 * i + 1
#


def heapify(T, i, n):
    min_ind = i
    l = left(i)
    r = right(i)
    #
    if l < n and T[l] > T[min_ind]: min_ind = l
    if r < n and T[r] > T[min_ind]: min_ind = r
    #
    if min_ind != i:
        T[i], T[min_ind] = T[min_ind], T[i]
        heapify(T, min_ind, n)
#end def ^^^


def change(T):
    n = len(T)
    for i in range( parent(n - 1), -1, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, n)
#end def ^^^


T = [16,5,4,9,3,-10,20]
# [-10, 3, 4, 9, 5, 16, 20]
change(T)
print(T)
