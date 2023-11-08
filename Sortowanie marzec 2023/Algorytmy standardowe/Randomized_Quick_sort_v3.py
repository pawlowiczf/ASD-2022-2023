# Randomizowana wersja algorytmu quick-sort 
from random import randint



def partition(T, low, high):
    
    pivot = T[high]
    i = low - 1

    for j in range(low, high):
        if T[j] <= pivot:
            i = i + 1
            T[i], T[j] = T[j], T[i]
    #end for
    T[i+1], T[high] = T[high], T[i+1]

    return i + 1 
#end def

def random_pivot(T, low, high):
    pivot = randint(low, high)
    T[pivot], T[high] = T[high], T[pivot]
    return partition(T, low, high)


def quick_sort(T, low, high):
    
    if low < high:
        pivot = partition(T, low, high)
        quick_sort(T, low, pivot - 1)
        quick_sort(T, pivot + 1, high)
    #end if 

#end def



T = [1,4,-10,16,-100,0,9,1,2]
quick_sort(T, 0, len(T) - 1)
print(T)


